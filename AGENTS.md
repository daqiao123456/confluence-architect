# Confluence 知识库架构 Skill 项目

## 唯一目标
完善 `skills/confluence-architect.yaml`，使其能准确输出任意部门的 Confluence 知识库架构方案。

## 方法论
读 `Target/Description.md`（体系描述）和 `Target/Mind Map.md`（思维导图）。不要凭记忆，每次都读。

## Skill 文件
- `skills/confluence-architect.yaml` — 主 skill，输入背景+部门→直出完整架构方案
- `skills/confluence-architect.ref.md` — APQC 速查 + 平台硬约束 + 治理参考（合并文件）

## 用户偏好
- 中文
- 高度浓缩，不要废话
- AI 主动维护本文件，确保跨会话记忆不丢

## Git 仓库
- GitHub: https://github.com/daqiao123456/confluence-architect
- 每次修改 skill 后，必须同步提交 AGENTS.md + skills/ 到 GitHub
- git remote 已配置，直接 git add/commit/push 即可

## 自测迭代循环（重要）

### 目的
每轮自测：运行 skill → 对比 Target 文档 → 发现不足 → 修改 skill → 提交 git → 开新会话继续下一轮。
最多 5 轮，达标即止。

### 测试用例
输入：「公司背景：中型互联网公司，主营 SaaS 产品。部门：技术部。」
评判标准：输出是否完整覆盖 Target/Description.md 的"道法术器治理度量"六层体系。

### 每轮流程
1. 读 AGENTS.md（本文件）获取上下文
2. 读 Target/Description.md 和 Target/Mind Map.md 作为评判标准
3. 读 skills/confluence-architect.yaml 当前版本
4. 用测试用例运行 skill（委派子代理执行 skill prompt）
5. 将输出与 Target 对比，记录差距到下方「迭代日志」
6. 修改 skill 文件修复差距
7. git commit + push
8. 更新本文件的「迭代日志」和「当前轮次」
9. 如未达标且轮次 < 5，发送 /new 开新会话，输入「继续」触发下一轮

### 当前轮次
1

### 迭代日志

#### 轮次 1
- 测试输入：「公司背景：中型互联网公司，主营 SaaS 产品。部门：技术部。」
- 差距发现：
  1. ❌ 缺「道」模块——没有体系总纲开篇
  2. ❌ 缺「法」模块——没有方法论说明
  3. ❌ 缺「器」模块——没有工具承载说明
  4. ❌ 缺「度量」模块——没有运营指标
  5. ⚠️ 「术」六步隐含但未显式标注
- 修复：重写 output_format，从 7 模块扩展为 10 模块（道+法+器+列事+列文+列位+成树+定标签+定治理+度量）
- 状态：已修复，待轮次 2 验证

#### 轮次 2
- 测试输入：同轮次 1
- 差距发现：无。10 个模块全部输出，六层体系完整覆盖。
  1. ✅ 道——根规律阐述清晰，含顺序不可反的原因
  2. ✅ 法——三框架各自职责明确
  3. ✅ 器——主器+辅器+边界
  4. ✅ 术——六步显式标注（模块四到九）
  5. ✅ 治理——五维度全覆盖，规则具体
  6. ✅ 度量——四指标+衡量方式+基线值
- 状态：✅ 达标，迭代结束

---
