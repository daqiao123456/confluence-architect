#!/usr/bin/env python3
"""
@description: 递归拉取指定 Confluence 空间的完整树状页面架构。
@usage: python3 scripts/get_space_tree.py [space_key]
@output: 打印缩进的树状目录结构，自动处理所有层级和孤儿页面。
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import base64


def get_config():
    config_path = os.path.expanduser("~/.config/opencode/mcp.json")
    try:
        with open(config_path) as f:
            data = json.load(f)
            return data.get("mcpServers", {}).get("confluence", {}).get("env", {})
    except Exception as e:
        print(f"❌ 无法读取配置文件 {config_path}: {e}")
        sys.exit(1)


def execute_cql(url, auth_b64, space_key):
    cql_query = f'space = "{space_key}"'

    all_results = []
    start = 0
    limit = 100

    while True:
        api_url = f"{url}/rest/api/content/search?cql={urllib.parse.quote(cql_query)}&expand=ancestors&limit={limit}&start={start}"
        req = urllib.request.Request(api_url)
        req.add_header("Authorization", f"Basic {auth_b64}")
        req.add_header("Accept", "application/json")

        try:
            resp = urllib.request.urlopen(req)
            data = json.loads(resp.read())
            results = data.get("results", [])
            if not results:
                break
            all_results.extend(results)

            start += len(results)
            if start >= data.get("totalSize", 0):
                break
        except Exception as e:
            print(f"❌ CQL 查询失败: {e}")
            break

    return all_results


def build_and_print_tree(all_results):
    pages = {}
    roots = []

    for r in all_results:
        page_id = r.get("id")
        title = r.get("title", "Unknown")
        ancestors = r.get("ancestors", [])
        parent_id = ancestors[-1].get("id") if ancestors else None

        pages[page_id] = {
            "id": page_id,
            "title": title,
            "parent_id": parent_id,
            "children": [],
        }

    for page_id, node in pages.items():
        parent_id = node["parent_id"]
        if parent_id and parent_id in pages:
            pages[parent_id]["children"].append(page_id)
        else:
            roots.append(page_id)

    def print_node(node_id, level=0):
        node = pages[node_id]
        prefix = "  " * level + "├── " if level > 0 else "🏠 "
        print(f"{prefix}{node['title']} (ID: {node['id']})")

        children = sorted(node["children"], key=lambda cid: pages[cid]["title"])
        for child_id in children:
            print_node(child_id, level + 1)

    print(f"✅ 共检索到 {len(pages)} 篇文档，架构树如下：\n")
    roots = sorted(roots, key=lambda rid: pages[rid]["title"])
    for root_id in roots:
        print_node(root_id, 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 scripts/get_space_tree.py <space_key>")
        print("例如: python3 scripts/get_space_tree.py dy0YXQtLe7kr")
        sys.exit(1)

    space_key = sys.argv[1]
    env = get_config()

    url = env.get("CONFLUENCE_URL", "").rstrip("/")
    email = env.get("CONFLUENCE_USERNAME", "")
    token = env.get("CONFLUENCE_API_TOKEN", "")

    if not all([url, email, token]):
        print("❌ 环境变量缺失，请检查 mcp.json")
        sys.exit(1)

    auth_str = f"{email}:{token}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")

    print(f"正在拉取空间 '{space_key}' 的全量数据，请稍候...")
    results = execute_cql(url, auth_b64, space_key)
    build_and_print_tree(results)
