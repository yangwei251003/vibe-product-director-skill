# Vibe Product Director 2.0 · 升级审计

> 审计基线：`vibe-product-director-v1.0.0.zip` 与 `vibe-product-director-SKILL.md`。两份输入保持原样，未纳入 v2 发布包。审计日期：2026-08-26。

## 结论

v1 的核心价值不是“七个阶段”或“十八份文件”，而是把模糊产品想法推进到视觉、功能、系统和交接都可执行。v2 保留这一导演职责，同时把固定流水线改为证据优先的决策图：模式可组合、问题按影响选择、文档按需生成、Ready 由可执行条件而非分数决定。

## 保留 / 重写 / 合并 / 删除

| v1 能力或机制 | v2 处置 | 理由与落点 |
|---|---|---|
| 视觉优先与审美翻译 | 保留并加强 | `visual-experience-system.md` 增加三方向差异、反模板、动效中断与降级 |
| 用户旅程与功能闭环 | 保留并加强 | `PRODUCT_BLUEPRINT` + ACT 追踪链 |
| 前端到后端追踪 | 保留并加强 | `system-integrity.md` 覆盖权限、状态、数据、错误、异步、监控、测试 |
| Resume 与交接 | 保留并迁移 | 同时识别 v2 `00_BLUEPRINT_INDEX.md` 与 v1 `00_INDEX.md` |
| 固定七阶段 | 重写 | 三个正交维度 + 依赖满足、影响最大 frontier |
| 固定 3–6 问 | 重写 | 复杂可单问；通常 2–4；简单独立最多 5 |
| 18 份默认文档 | 重写 | 六核心 + DECISIONS 触发创建 + 八条件模块 |
| 五角色逐份输出 | 合并 | 作为内部审查镜头，只暴露改变结论的风险与推荐 |
| 100 分 Ready | 删除 | 改为 Blocking、首切片、三重审查硬条件 |
| Fast Track 独立模式 | 合并 | 兼容映射到 Express 工作深度 |
| 危险覆盖安装 | 删除 | 默认拒绝；force 先时间戳备份、暂存验证、再替换 |
| 泛化 `SOURCES.md` | 删除 | 升级依据集中在本外部审计，不伪造来源价值 |
| Manifest/README/CHANGELOG/evals | 保留 | 正式发布、升级和可验证性所需 |

## 25 项对抗审查

| # | 对抗问题 | v1 风险 | v2 处置 | 证据 |
|---:|---|---|---|---|
| 1 | 简单项目是否也被迫走七阶段？ | 是 | Express + frontier 自适应 | `adaptive-modes.md` |
| 2 | 单个关键问题能否单独询问？ | 不稳定 | 明确允许复杂问题单问 | `SKILL.md` 问题预算 |
| 3 | 3–6 问会不会制造认知负担？ | 会 | 通常 2–4，最多 5 | `SKILL.md` |
| 4 | 用户说“按推荐”后会否再次追问？ | 可能 | 记录理由和重开条件，无新证据不重开 | `adaptive-modes.md` |
| 5 | 同一决定会否无限深挖？ | 可能 | 最多一次必要深挖 | `SKILL.md` |
| 6 | 五角色是否输出重复独白？ | 容易 | 改为内部镜头 | `SKILL.md` |
| 7 | 是否先读现有证据？ | Resume 有但不统一 | 每轮先读证据 | `SKILL.md` 自适应循环 |
| 8 | 事实、偏好、推断会否混淆？ | 可能 | PROJECT_STATE 分类账本 | 核心模板 |
| 9 | 矛盾是否显式记录？ | 不充分 | 矛盾类型和必要重问 | `PROJECT_STATE.template.md` |
| 10 | 视觉方向是否只是换颜色？ | 有风险 | 要求视觉语法实质不同 | `visual-experience-system.md` |
| 11 | 是否识别 AI 模板感？ | 有覆盖但零散 | 专门反模板审查 | 同上 |
| 12 | 动效是否含无障碍与降级？ | 不完整 | 中断、触摸/键盘、reduced-motion、低性能 | 同上 |
| 13 | 功能是否围绕核心旅程收敛？ | 是但易膨胀 | Journey + Remove-One | `product-scope-and-risk.md` |
| 14 | 本地视图切换会否硬套后端？ | 未明确 | 明确 `local-only` | `system-integrity.md` |
| 15 | 每个业务动作能否追到权限与状态？ | 部分 | ACT 完整追踪链 | `SYSTEM_BLUEPRINT.template.md` |
| 16 | 第三方/异步失败有无恢复？ | 可能遗漏 | 闭环硬门槛 | `system-integrity.md` |
| 17 | 高影响决定变更会否留下双重真相？ | 风险高 | 废弃、In Review、唯一权威、重算 | `adaptive-modes.md` |
| 18 | 是否只重开受影响问题？ | 未约束 | 显式依赖传播 | 同上 |
| 19 | v1 Resume 能否兼容？ | — | 识别 `00_INDEX.md` 为迁移证据 | 同上 |
| 20 | 18 文档是否造成空壳和 token 浪费？ | 是 | 六核心、条件创建 | `blueprint-contracts.md` |
| 21 | Ready 分数能否掩盖关键阻塞？ | 能 | Blocking 是硬否决 | `readiness-and-handoff.md` |
| 22 | 用户提前“开始开发”怎么办？ | 不够精细 | Blocking 先解决；仅 Conditional/Later 则冻结交接 | 同上 |
| 23 | 独立实现者仍需重问怎么办？ | 缺少硬失败 | Blind-Handoff 必须失败并定点回流 | 同上 |
| 24 | 安装是否可能无备份覆盖？ | 是 | 默认拒绝，force 备份和暂存验证 | `scripts/install.*` |
| 25 | 发布包能否混入缓存或报告？ | 可能 | 顶层白名单、manifest 全覆盖、ZIP 安全校验 | `scripts/build_release.py` |

## 兼容策略

- Skill 名称保持 `vibe-product-director`，版本升为 `2.0.0`，隐式调用继续开启。
- “Fast Track”继续可说，但解释为 Express 深度，不再形成另一套状态机。
- Resume 先寻找 `00_BLUEPRINT_INDEX.md`；只发现 `00_INDEX.md` 时读取旧文档作为证据，新索引明确唯一权威来源。
- 稳定 ID 只给跨文档对象：`DEC-*`、`ACT-*`、`RISK-*`、`OPEN-*`；旧文档段落编号不机械继承。

## Token 与认知负担变化

| 指标 | v1 | v2 | 变化 |
|---|---:|---:|---|
| 默认核心文档 | 18 | 6 | 减少 66.7% |
| 条件文档 | 固定体系中混用 | 8 类按需 | 无触发则零成本 |
| 常规每轮问题 | 3–6 | 2–4 | 更适合单一高影响决定 |
| Ready | 100 分模型 | 3 个硬条件 + 13 项门槛 | 避免分数抵消阻塞 |
| 角色输出 | 可能五路展开 | 内部合并 | 只展示会改变结论的信息 |

这是结构性降负担估算，不声称精确 token 基准；真实问题量、重复率与文档量结果记录在 `EVAL_REPORT.md`。

## 安全边界

- 不安装到全局目录；只提供安装脚本和临时目标实测。
- 不修改两份 v1 审计基线。
- 不读取、删除或打包工作区中无关的 `%USERPROFILE%/.npm-cache`。
- 发布报告保留在 Skill 目录外，ZIP 仅包含一个 `vibe-product-director/` 顶层目录。

