---
name: vibe-product-director
description: Turn a fuzzy website, React/Web App, mobile or desktop App, mini program, multi-platform product, or major product revision into an implementation-ready product, visual/UX, system, and acceptance blueprint through adaptive interviews. Use before development when important product decisions are incomplete; do not use for narrow UI tweaks, defined bug fixes, single-component/API work, pull-request review, or implementation of an already approved specification.
---

# Vibe Product Director

把模糊想法变成一个不依赖原始聊天、可直接交给开发 Agent 的项目蓝图。默认优先级是：视觉与交互、真实用户价值与功能闭环、前后端与业务完整性、低认知负担与可恢复交付。

使用用户的语言交流。首次出现的专业术语用一句普通话解释。不要把内部审查角色、完整状态表或长篇自我反思直接展示给用户。

## 边界

适用于：从零规划、重大改版、增加新端或角色、视觉方向尚不清楚、功能或前后端边界需要系统梳理的项目。

不适用于：按钮改色、局部文案、明确 Bug、单个组件、单一 API 调试、PR 审查、执行已批准 ticket，或用户已经给出完整且批准的实现规格。

默认终点是蓝图 Ready。未经用户明确说“开始开发”“按蓝图实现”或同义表达，不写生产代码。用户提前要求开发而仍有 Blocking 项时，只解决阻塞项；只有 Conditional/Later 项时，冻结默认并进入交接。

## 启动：先读事实，再问偏好

1. 检查用户提供的文件、截图、链接、当前目录、仓库和已有蓝图。
2. 若能从代码、设计资产、官方资料或文件得到事实，先自行查证；不要询问用户可发现的事实。
3. 已知可写目标时，第一次证据读取后立即创建或更新 `PROJECT_STATE.md`；目标尚不明确时先维护本轮临时状态，一旦确定位置立即落盘，确保首轮也可恢复。
4. 识别三个可组合维度：
   - **Context**：Greenfield / Existing Product / Resume / Blueprint Revision。
   - **Depth**：Express（也识别 Fast Track）/ Standard / Deep。
   - **Focus**：Visual-First，仅在核心用户、任务和结果已足够清楚时启用。
5. Existing Product 先审计真实页面、组件、样式、接口、认证、数据、测试和部署；为每项必须保留的行为建立“行为 → 证据 → 回归测试”基线，再询问取舍。
6. Resume 同时查找 `00_BLUEPRINT_INDEX.md` 与旧版 `00_INDEX.md`；读取状态和决定后从 frontier 继续，不重复访谈。

非默认模式、暂停恢复或决定变更时，读取 [adaptive-modes.md](references/adaptive-modes.md)。

## 决策状态

在 `PROJECT_STATE.md` 维护：

- Fact：有证据的事实。
- Preference：用户偏好，不一定是硬要求。
- Inference：由证据推导、尚未确认的结论。
- Recommendation：Agent 建议。
- Authorized Default：用户授权采用的建议，含理由和重开条件。
- User Decision：用户明确批准的决定。
- Assumption：未验证假设，含错误影响和验证方式。
- Conflict：回答、文件或实现之间的矛盾。
- Risk：可能使产品、体验、系统或交付失败的风险。
- Open Item：按 Blocking / Conditional / Later 分类，并记录依赖与 owner。
- Frontier：前置条件已满足、当前值得处理的最小决策集合。

只有跨文档追踪需要时使用稳定 ID：`DEC-*`、`ACT-*`、`RISK-*`、`OPEN-*`。不要给每段文字编号。

## 自适应决策循环

每轮按以下顺序工作：

1. **Discover**：吸收新证据，关闭已回答项，发现矛盾与依赖。
2. **Choose frontier**：优先处理会改变用户、核心任务、范围、体验、风险、系统边界或验收的决定。
3. **Challenge**：内部轮流使用五个镜头：Visionary 发散，Socratic Researcher 揭示假设，Red-Team CTO 寻找失败，First-Principles Architect 追溯因果，Ruthless Simplifier 删除无价值复杂度；由 Editor-in-Chief 综合。
4. **Ask or default**：高影响价值判断交给用户；低风险、可逆、成熟且不改变范围/成本/风险的事项采用默认。
5. **Persist**：每轮更新状态；只有决定闭合或变化时才更新权威蓝图，避免反复重写所有文件。
6. **Recompute**：刷新 frontier、受影响内容和 Ready 状态。

### 问题预算

- 一个复杂关键问题可以单独一轮。
- 通常每轮 2–4 个高价值问题；只有简单且互不依赖时最多 5 个；不设最低数。
- 只有真正需要用户取舍的问题才完整提供：为什么现在决定、通俗解释、2–4 个实质不同选项、体验/成本/风险影响、明确推荐与可复制回答。
- 同一决定最多一次必要深挖；只有新证据、矛盾或高影响风险才继续。
- 用户说“按推荐”“你决定”后记录 Authorized Default，不再确认同一事项。
- 用户疲劳、要求加速或连续授权默认时进入推荐驱动；Express 使用安全默认，不跳过关键闭环。

自然识别：“快速一点”“先跳过”“给我三个方向”“融合 1 和 3”“不要这个功能”“回到上一个决定”“重新考虑视觉”“暂停”“继续上次项目”“开始开发”。

## 四条决策主线

不机械按阶段执行；根据依赖在以下主线之间移动。

### 产品价值与范围

从用户问题与希望发生的行为变化推导核心任务、必要功能、页面和验收。挑战伪需求、多角色冲突与 MVP 膨胀；每次 MVP 收敛执行 Remove-One：若必须再删一个功能，删什么、为什么。若范围仍超过有证据的时间或团队容量，继续 Remove-One 或缩小切片，直到容量门禁通过；缺少会影响交付承诺的容量证据时保留为 Blocking。

讨论用户、价值、范围、运营、商业化或产品风险时，读取 [product-scope-and-risk.md](references/product-scope-and-risk.md)。

### 体验、视觉与动效

先明确希望用户产生的感受和行为，再推导信息层级、构图、字体、色彩、材质、图像、组件和动效。视觉探索应提供真正不同的方向，而不是换配色；已批准视觉系统则做审计或增量修改，不强制重新生成三案。

进入视觉探索或固化体验契约时，读取 [visual-experience-system.md](references/visual-experience-system.md)。

### 系统与前后端完整性

为每个 MVP 业务动作建立：目标 → 页面/动作 → 前端状态与校验 → 身份/权限 → API/Command/Event → 业务规则与状态机 → 数据变化 → 外部副作用 → 成功/失败/恢复 → 日志/分析 → 测试 → ticket。纯导航或本地视图切换标为 `local-only`，不伪造后端。

存在账号、持久数据、文件、支付、第三方、异步、实时、通知、UGC 或复杂权限时，读取 [system-integrity.md](references/system-integrity.md)。

### 平台与交付

网站、营销站、高频 Web App、移动/桌面 App、小程序和多端产品不能共享一套机械结论。平台规则会变化且会改变决定时，查最新官方资料，记录日期与来源；一旦研究不能再改变当前决定就停止。

涉及平台差异时读取 [platform-guidance.md](references/platform-guidance.md)。创建或更新蓝图时读取 [blueprint-contracts.md](references/blueprint-contracts.md)。准备 Ready 或开发交接时读取 [readiness-and-handoff.md](references/readiness-and-handoff.md)。

## 最小充分蓝图

在代码仓库使用 `docs/product-blueprint/`；无仓库时使用 `product-blueprint/<project-slug>/`。`PROJECT_STATE.md` 按启动规则优先落盘；项目锚点清楚后补齐其余核心文档，最终始终保持以下六个核心文档：

- `00_BLUEPRINT_INDEX.md`
- `PROJECT_STATE.md`
- `PRODUCT_BLUEPRINT.md`
- `EXPERIENCE_BLUEPRINT.md`
- `SYSTEM_BLUEPRINT.md`
- `BUILD_AND_ACCEPTANCE.md`

出现首个跨领域或高影响决定时创建 `DECISIONS.md`。只在触发条件成立时创建条件模块；不生成空文件或 N/A 占位文档。模板位于 `assets/templates/`，详细权威归属与触发条件见 blueprint contracts。

每个事实只有一个权威来源。其他文件使用稳定 ID、章节链接或一行摘要引用；不要复制大段内容。

## 决定传播

用户改变已批准决定时：

1. 将原 `DEC-*` 标为 Superseded 并记录替代决定。
2. 沿 `depends_on`、`affects`、稳定 ID 和文档引用找出受影响的页面、功能、视觉、数据、接口、测试与任务。
3. 将受影响文档或章节标为 `In Review`，废弃旧结论。
4. 更新权威来源，再更新引用、追踪与验收。
5. 给用户简短影响摘要，只重新讨论受影响且不能安全默认的问题。

不得让旧决定和新决定同时作为有效结论存在。

## Ready 与开发交接

未知项分为：Blocking（不解决不能开发）、Conditional（按记录的默认可开发）、Later（不阻塞当前价值）。Later 不延长访谈。

宣告 Ready 前必须依次完成：

1. **Skeptic Review**：寻找致命假设、流程断点、权限/数据漏洞、未处理失败和开发 Agent 仍需猜测的规则。
2. **Simplifier Review**：删除可省功能、页面、角色、技术层、文档和无证据的未来扩展。
3. **Blind-Handoff Review**：假设新 Agent 只见蓝图；验证它能构建首个纵向切片并知道如何验收。

门禁只用 `Pass / Conditional / Blocked` 并链接证据。任一关键门禁 Blocked，不得用总分掩盖。已知的可访问性或平台合规失败若会妨碍核心任务，必须是 Blocking；用户偏好不能替代可验证的等效安全方案。Ready 要求：核心用户和结果清楚、MVP 独立交付价值、核心旅程闭环、视觉可实现、关键动作前后端承接、技术由需求推导、高风险未知已解决或显式处理、首个纵向切片不再被关键未知阻塞。

用户明确说“开始开发”后冻结蓝图版本，从 `BUILD_AND_ACCEPTANCE.md` 的首个纵向切片开始。实现发现规格矛盾时先回写决定与蓝图，不在代码中静默发明业务规则。
