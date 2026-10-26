# Readiness and Handoff

准备宣告蓝图 Ready、响应“开始开发”或交给新开发 Agent 时读取。

## 1. 未知项分类

- **Blocking**：不解决会使核心价值、范围、视觉方向、权限/数据安全或首个切片无法正确实现。
- **Conditional**：可以使用明确默认实现；记录默认、理由、影响、owner、解决时点和重开条件。
- **Later**：不会阻塞首个纵向价值；进入 Later backlog，不延长访谈。

能用安全默认关闭的问题不要继续问；不能合理默认的价值判断不得伪装成 Conditional。

## 2. 证据门禁

每项使用 `Pass / Conditional / Blocked`，并链接具体文档、章节、`DEC/ACT/RISK/OPEN`。不使用总分决定 Ready。

- Product Clarity
- User Value
- Scope Discipline
- UX Completeness
- Visual Distinctiveness
- Interaction and Motion
- Functional Completeness
- Frontend–Backend Integrity
- Architecture Fitness
- Security and Operations
- Testability
- Agent Handoff
- Simplicity and Token Efficiency

任一关键项 Blocked 即整体 Blocked。Conditional 必须有默认、影响和解决时点。

已知的低对比、键盘不可达、无法关闭的高强度动效或平台合规问题若妨碍核心任务，门禁必须为 Blocked。只有满足可测试阈值或提供等效可访问路径后才能解除，不能仅以“用户坚持”降为 Conditional。

## 3. 三重最终审查

### Skeptic Review

尝试找出致命假设、价值证据缺口、旅程断点、视觉/可用性冲突、功能缺口、权限/数据漏洞、失败/恢复缺失、文档矛盾和开发 Agent 仍需猜测的规则。

### Simplifier Review

寻找可删除功能、页面、角色、服务、技术层、文档、问题和无价值未来扩展。再次执行 Remove-One，并检查条件模块是否仍有真实入口。

### Blind-Handoff Review

假设新 Agent 只读取蓝图，确认它能回答：为谁、解决什么、先做什么、页面/视觉规则、业务/权限/数据、失败恢复、如何测试、完成标准和不能擅改什么。

任何高严重度缺口阻止 Ready。

## 4. Ready 条件

- 一句话价值、核心用户、场景和结果清楚。
- MVP 有一条独立交付价值的闭环旅程，范围经过 Remove-One。
- 视觉方向已选定且能落到 tokens、组件、动效、响应式与降级。
- 正常、异常、权限、恢复和运营责任足够完整。
- 依赖身份的首切片已明确权威用户主体、身份因子唯一性、绑定冲突与历史资源归属。
- 所有 MVP 业务动作有系统承接、测试和纵向 ticket。
- 技术由需求推导，平台约束和高风险未知已解决或显式处理。
- 没有 Blocking；剩余未知不会阻塞首个纵向切片。
- 新 Agent 不需要重新询问关键产品、视觉或业务问题。

## 5. 纵向切片

每个 ticket 贯穿完成一个可演示用户结果所需的界面、状态、权限、API/事件、数据、错误和测试。不要按“先全部前端、再全部后端”横向拆分。

每张 ticket 是可由全新上下文独立执行的耐久简报，包含：用户价值、当前/期望行为、范围/非范围、依赖与阻塞边、涉及 `ACT/DEC`、关键接口/权威链接、实现边界、验收、演示方式、验证命令、no-op/幂等要求和停止/升级条件。避免依赖易漂移的行号或聊天背景。

首个切片优先证明最关键价值和最大未知，不先搭建所有基础设施。

默认使用 tracer-bullet：一条最细但真实的端到端路径先贯穿界面、系统和测试，再逐片扩展。跨全局 schema、接口或组件体系的宽迁移是例外，按 `expand → 分批 migrate → contract` 拆分，每步保持可运行、可回滚。

## 6. Human Gates

Agent 无法代办的账号认证、合同/法务批准、支付主体、真实用户接触、密钥授权或设备操作写成门：`owner / exact action / evidence returned / blocks / trigger or deadline / irreversible confirmation`。Agent 先完成清单、草稿、验证入口和回滚准备，再请求人工动作。

## 7. 响应“开始开发”

1. 运行三重审查与门禁。
2. 若有 Blocking，列出最少阻塞和推荐解决方式，不写生产代码。
3. 若只有 Conditional/Later，冻结 Blueprint version、决定基线与首个 ticket frontier。
4. 开发 Agent 先读 Index、Build、对应 Product/Experience/System 章节和相关决定。
5. 每完成一片按追踪矩阵和验收验证；规格矛盾先回写蓝图。

## 8. 交接与后续审查契约

最终只展示：Ready 状态、首个切片、冻结决定、Conditional 假设、Human Gates、验证方式和明确停止条件。详细内容留在蓝图，用指针交接，不把整套文档复制到聊天；任何摘要都不得包含 secret、token、真实个人信息或不必要的敏感数据。

开发后的审查分两条独立轴：

- **Standards**：代码质量、安全、性能、可维护性和项目约定。
- **Specification**：实现是否满足冻结的产品、体验、系统和验收契约。

两轴都必须引用可观察证据。规格错误不能被“代码写得漂亮”抵消；实现过程中发现蓝图矛盾时暂停受影响切片，回写权威决定后再继续。
