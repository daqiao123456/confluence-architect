# 自动化脚本库 (Python Scripts)

这里存放了用于管理 Confluence 知识库的自动化 Python 脚本。
AI 智能体在处理复杂逻辑（如全量数据分析、树状结构遍历、批量修改）时，会优先调用此目录下的脚本。

## 脚本清单 (Script Registry)

### 1. 获取空间树状架构
- **文件**: `get_space_tree.py`
- **功能**: 递归拉取指定 Confluence 空间的完整树状页面架构。解决了 Confluence 默认 API 无法一次性拉取深层嵌套目录的问题。
- **用法**: `python3 scripts/get_space_tree.py <space_key>`
- **示例**: `python3 scripts/get_space_tree.py dy0YXQtLe7kr`

---
*注：AI Agent 会通过读取此 README.md 或使用 grep 命令来快速检索和复用这些脚本。*