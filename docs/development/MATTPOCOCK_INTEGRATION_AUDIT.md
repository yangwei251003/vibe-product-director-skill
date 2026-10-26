# Vibe Product Director 2.2 · mattpocock-skills-zh-CN 纠偏融合审计

> 审计日期：2026-08-29  
> 目标仓库：https://github.com/vinvcn/mattpocock-skills-zh-CN  
> 固定提交：`9fb0161ac2be0c45c59cbea0878eb77d92cc24b5`  
> 初次升级：`vibe-product-director` 2.0.0 → 2.1.0  
> 真实使用纠偏：2.1.0 → 2.2.0

## 0. 2.1 真实使用失败与纠偏

2.1 对仓库内容的“概念映射”虽然完整，但用户实际使用证明关键行为没有发生：模型问完首轮几个问题便收尾，没有像原工作流那样持续展开 design tree。

根因是抽象层级错误：

- 把 `ask-matt` 简化成阶段边界，遗漏了它真正重要的 `idea → grilling → prototype detour → spec → tickets → implement` 路由。
- 把 `grill-me` 简化成内部 Red-Team 镜头，遗漏了它是持续多轮访谈入口。
- 把 `grill-with-docs` 简化成“先读证据”，遗漏了边访谈边更新 shared language 与 decisions 的 stateful 行为。
- 虽然写了 frontier，却没有强制“用户回答后重算并自动问下一轮，frontier 为空前不得结束”。
- “同一决定最多一次深挖”会把真正的 child decisions 错判为重复，促使模型提前停止。

2.2 因此不再把这些能力藏在审计或条件参考中，而是升格为主入口强制契约：Director Router 每次触发都运行；Stateful Grilling 是默认 Phase；每轮最多 4 问但总轮数不设上限；术语、决定和蓝图边问边更新；九类覆盖扫描与用户共同理解确认通过后才进入 Blueprint Synthesis。

## 1. 审阅范围与方法

本次不是根据 README 或 Skill 名称做表面拼装，而是读取固定提交下 `skills/` 的全部内容：

| 类型 | 文件数 | 物理行数 |
|---|---:|---:|
| Markdown | 62 | 3,815 |
| YAML | 35 | 145 |
| Shell | 3 | 273 |
| CJS | 1 | 95 |
| 合计 | 101 | 4,328 |

其中包含 35 个 `SKILL.md` 入口、2,382 个入口物理行；全部文件共有 2,967 个非空行。 supporting references、模板、配置和脚本也纳入语义审阅，因为真正的运行契约经常位于入口文件之外。

审阅时逐项提取：触发边界、状态模型、步骤/循环、人工检查点、输出契约、停止条件、恢复方式、失败模式和是否依赖特定开发工具。没有复制原仓库的大段文字；融合内容使用 Vibe Product Director 的状态、文档和用户语言重新表达。

## 2. 融合判据

只有同时满足以下条件的机制才进入 2.2：

1. 发生在正式开发之前，或直接提高蓝图到开发的交接质量。
2. 能加强产品价值、视觉体验、系统完整性或决策可靠性中的至少一项。
3. 可以嵌入现有自适应 frontier，不要求用户切换到另一套 Skill 心智模型。
4. 有清楚的触发和停止条件，不会让每个项目都增加文档或仪式。
5. 不把 Git、调试、代码实现、课程制作等后开发职责吞进产品总导演边界。

## 3. 35 个 Skill 的逐项处置

| Skill | 核心机制理解 | 与 VPD 的关系 | 2.2 最终处置 |
|---|---|---|---|
| `ask-matt` | 路由 idea→grilling→detour→spec→tickets→implement，并管理阶段边界 | 是单一 VPD 闭环缺失的流程骨架 | 内置强制 Director Router；自动选入口、显示当前 Phase 并确保支线回到主流程 |
| `claude-handoff` | 为上下文切换持久化当前事实、进度和下一步 | 工具特定命令不通用，交接原则匹配 | 合并为 Index/State 的指针式恢复；移除 Claude 专属语法 |
| `code-review` | 把审查拆成工程标准与规格符合度 | 蓝图交给开发后需要两条独立审查轴 | 在交接契约加入 Standards / Specification 双轴 |
| `codebase-design` | 深模块、窄接口、公开 seam、避免假想抽象；必要时独立做双设计 | 适合高锁定系统边界，不适合所有产品决定 | 条件吸收至 System；只对难逆接口使用 Design It Twice |
| `diagnosing-bugs` | 假设—证据—复现—修复的诊断循环 | 属于明确 Bug 的开发期工作，正是 VPD 排除项 | 保持外部能力；只保留“证据先于结论”的通用原则 |
| `domain-modeling` | 规范语言、场景压力测试、上下文边界和克制 ADR | 直接补强多角色、状态和权限蓝图 | 加入 canonical terms、Avoid aliases、bounded context；词表过大才拆文档 |
| `git-guardrails-claude-code` | 用钩子限制危险 Git 操作 | 与产品规划无直接关系，且依赖具体工具 | 不整合 |
| `grill-me` | 无文档载体时的持续访谈入口，底层运行 grilling | VPD 目标未落盘前需要短暂 stateless on-ramp | 只在目标位置未知时临时使用；位置明确后立即升级为 Stateful Grilling |
| `grill-with-docs` | 持续访谈，同时主动更新 glossary/domain model 与稀疏 ADR | 正是产品总导演在 repo/蓝图目录中的默认行为 | 直接融合：每轮 State、术语、Decisions 与受影响权威章节同步更新 |
| `grilling` | 多轮访问 design tree；每轮问当前 frontier，回答后重算；frontier 空才结束 | 是解决“只问几个问题”的核心 primitive | 直接融合为强制默认；总轮数不限、child decisions 必须继续、退出需覆盖扫描与用户确认 |
| `handoff` | 交接应给权威指针、当前状态和下一动作，避免复制与泄密 | 直接改善 Blind-Handoff | 强化指针式交接、敏感信息排除和耐久入口 |
| `implement` | 按已批准规格实现并验证 | 已超出 VPD“开始开发”前的职责 | 不整合；VPD 只冻结蓝图和首切片 |
| `improve-codebase-architecture` | 以可验证目标渐进改善架构 | Existing Product 的迁移边界可借鉴 | 只吸收渐进迁移与回滚；不把架构改造执行纳入 VPD |
| `loop-me` | Agent 先推进，真正需要人类时才停在检查点 | 直接减少低价值问答 | 加入“先做到 Agent 能完成的最远处，再请求决定/人工门” |
| `migrate-to-shoehorn` | 特定库/架构迁移流程 | 工具和实现特定 | 不整合 |
| `prototype` | 原型只回答一个设计问题；区分逻辑与 UI 证据 | 正好填补“讨论无法收敛但又不能偷跑生产”的缺口 | 直接融合用户授权、隔离、可丢弃和 Question→Observation→Decision 闭环 |
| `research` | 先定义研究问题，偏好一手来源，结论必须改变决定 | 适合平台、市场和高风险未知 | 强化最小证据阶梯与停止研究条件 |
| `resolving-merge-conflicts` | 安全解决代码合并冲突 | 开发维护期职责 | 不整合 |
| `scaffold-exercises` | 构建教学练习和脚手架 | 与产品导演目标无关 | 不整合 |
| `setup-matt-pocock-skills` | 安装/配置一套 Skill 生态及工作流 | VPD 已有自己的安装、manifest 和安全替换 | 不整合其生态；保持 VPD 单一安装契约 |
| `setup-pre-commit` | 配置提交前校验 | 开发基础设施职责 | 不整合 |
| `setup-ts-deep-modules` | 为 TypeScript 强制深模块边界 | 语言和实现特定 | 不整合工具；通用 seam 原则已进入 System |
| `tdd` | 从外部行为和独立期望值开始，沿公开接口做小步验证 | 可提升蓝图验收与首个纵向切片 | 吸收行为验收、公开 seam 与最细端到端切片；不规定实现框架 |
| `teach` | 先建立概念再依赖概念，多种教学输出 | VPD 需要向非专业用户解释术语，但不是教学 Skill | 吸收“一句话普通话解释”和概念先行；不扩展教学文档 |
| `to-questionnaire` | 当信息在别人脑中时，为收件人而不是主题设计问卷 | 直接解决运营/法务/销售知识缺口 | 新增条件问卷模板；答案必须回写决定，问卷不是规范 |
| `to-spec` | 用已经形成的决定合成规格，不重新启动访谈 | 直接增强蓝图冻结 | 强化单一权威和“已有决定不重问” |
| `to-tickets` | 用 tracer-bullet 纵向任务和显式依赖；宽改造分 expand/migrate/contract | 直接增强 Build & Acceptance | 直接融合纵向任务、blocking edges 和宽迁移例外 |
| `triage` | 把模糊工作变成耐久 brief，明确当前/期望行为和 Out of Scope | 适合给新开发 Agent 的 ticket | 融合耐久任务简报，避免聊天和易漂移行号依赖 |
| `wait-what` | 发现目标、前提或术语之间的矛盾，先澄清 framing | 与 Conflict/Fog 强匹配 | 融合为矛盾记录和解雾，不增加单独模式 |
| `wayfinder` | Destination、共享地图、决定票、Fog、frontier 和阻塞边 | 与复杂/多会话产品规划高度匹配 | 直接融合，但 Decision Map 只作索引，不引入外部 issue 仪式 |
| `wizard` | 区分 Agent 可做与人类独占步骤，形成清晰人工门 | 直接解决账号、合同、平台认证等阻塞 | 新增 Human Gate：owner、精确动作、返回证据、blocks 和不可逆确认 |
| `writing-beats` | 信息按依赖排序，先落地概念再使用 | 改善蓝图阅读顺序 | 融合到 Index 的消费者阅读路径和术语先行 |
| `writing-for-agents` | 给执行 Agent 写耐久上下文：权威指针、完成标准、渐进披露、避免易变缓存 | 与 Blind-Handoff 完全匹配 | 直接融合 Index、ticket brief、no-op、验证和单一事实来源 |
| `writing-fragments` | 处理写作片段与表达素材 | 偏内容生产，不是产品决策主链 | 不整合 |
| `writing-shape` | 用简洁结构塑造信息层级和阅读节奏 | 可改善蓝图可读性 | 吸收为最小充分结构；不新增写作阶段 |

## 4. 最终闭环

2.2 不增加另一条平行工作流，完整闭环仍以 Vibe Product Director 为中心：

```text
Director Router 选择入口并显示当前 Phase
→ Stateful Grilling 逐轮访问 design tree frontier
→ 每轮回答实时更新 State / Language / Decisions / Blueprint
→ Fog 经研究、知情人或获准证据原型变成可决定问题，再回原树
→ frontier 为空后运行九类覆盖与 Skeptic scan；新问题继续下一轮
→ 用户确认共同理解，Blueprint Synthesis 不重新访谈
→ tracer-bullet tickets + blocking edges，由用户审阅执行形状
→ Simplifier / Blind-Handoff / Ready
→ 用户明确授权后按 ticket 开发
→ Standards / Specification 双轴验证，矛盾回到原决定
```

每种证据方法都必须关闭循环：`Close / Narrow / Stop` 三选一。研究、问卷或原型若没有改变决定、风险、验收或废弃结论，就不继续维护。

## 5. 具体落点

| 2.2 能力 | 主要文件 |
|---|---|
| Director Router / idea-to-build main flow | `SKILL.md`、`references/director-router-and-main-flow.md` |
| 多轮 design tree / frontier / 退出门 | `references/stateful-grilling.md`、`PROJECT_STATE.template.md` |
| 研究、问卷、原型、Design It Twice | `references/decision-evidence-and-prototyping.md`、三个条件模板 |
| 领域语言、deep module、公开 seam | `references/system-integrity.md`、`SYSTEM_BLUEPRINT.template.md` |
| tracer-bullet、宽迁移、耐久 ticket、Human Gates | `references/readiness-and-handoff.md`、`BUILD_AND_ACCEPTANCE.template.md` |
| 指针式恢复、消费者阅读路径 | `references/blueprint-contracts.md`、`00_BLUEPRINT_INDEX.template.md` |
| 回归验证 | 20 个多轮场景、25 个触发场景、12 维行为量表 |

## 6. 明确保留在边界外的能力

VPD 仍不负责：明确 Bug 诊断、PR/code review 执行、Git/merge/pre-commit、依赖升级、已批准 ticket 实现、特定 TypeScript 架构迁移、课程/练习制作或一般内容写作。这些能力可以在“开始开发”后由相应 Skill 接手，但不得改变 VPD 的产品总导演触发边界。

## 7. 结论

本次纠偏的价值不是“把 35 个 Skill 塞进一个文件”，而是让最关键的流程真的发生。2.2 的核心服务仍是：在写生产代码前，通过持续且有退出门的访谈，把网站、App、小程序和多端产品的产品、视觉、系统与验收决定收敛成可盲交接蓝图，再把它变成可执行 tickets。
