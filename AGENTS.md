# AGENTS.md — 本仓库 agent 共享上下文（L0 层，所有 agent 启动必读）

> 维护规则：本文件只放"全局稳定约定"。任务级信息一律进 issue / 交接契约 / 任务板。
> 修改本文件需 Orchestrator 提议 + 人类批准。

## 1. 项目使命
本仓库是 Issue-to-PR 范式 POC：以 issue 文件为任务输入，由 agent 自主完成
分支/实现/自测并产出 PR 文件；人类保留 merge 仲裁权。

## 2. Agent 角色约定
| 角色 | 对应 Qoder 原语 | 职责 | 上下文模式 |
|---|---|---|---|
| Orchestrator | Leader | 全局计划、委派、仲裁、记录 | fork（持有全局视图） |
| Implementer | subagent 1..N | 认领、实现、自测、提交 PR | 继承交接契约（按需上下文） |
| Reviewer | isolated subagent | 独立审查、输出反馈清单 | isolated（强制，防锚定） |
| Librarian（可选） | subagent | 会话复盘后提取经验入长期记忆 | fork |

## 3. 协作规则
1. 通信分工：SendMessage 只传协调信号（认领/完成/请求仲裁）；实质内容一律写入工件文件。
2. 认领：先改 issue 文件状态字段（open → claimed → in_progress），再更新任务板，先到先得。
3. 文件边界：只改交接契约"任务边界"中列出的文件；越界需求先向 Orchestrator 升级。
4. 交接必带四件套：目标 / 输出格式 / 工具与来源指引 / 任务边界。
5. 交付必带测试证据：无真实测试输出的 PR 视为未完成。
6. 终止条件：issue 验收标准全部勾选 + 单测全绿 + lint 无新增告警，三者齐备才可宣布完成。
7. 冲突：发现并行写同一文件 → 停止写入 → SendMessage 上报 Orchestrator 仲裁。
8. 禁止：伪造测试输出；跳过 review 直接请求 merge；agent 自行执行 merge。

## 4. 命令约定（PowerShell 5.1，逐条执行，不使用 &&）
- 全量测试：python -m pytest tests/ -q
- 单文件测试：python -m pytest tests/test_calculator_percent.py -q
- Lint：python -m ruff check src/ tests/（未装 ruff 时用 python -m pyflakes src/ tests/）
- 新建分支：git checkout -b feat/issue-001-percent
- 提交：git add <files>
- 提交说明格式：<type>(<scope>): <summary> (ISSUE-XXX)
- 本机无 python 命令时用 py 替代。

## 5. 目录约定
issues/ = issue 契约；prs/ = PR 文件；docs/ = 指南；docs/reports/ = 仲裁与复盘归档；
src/ = 源码；tests/ = 测试。
