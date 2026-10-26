# Blueprint Contracts

创建、更新、迁移或恢复项目蓝图时读取。模板位于 `assets/templates/core/` 与 `assets/templates/conditional/`。

## 1. 位置与状态

- 代码仓库：`docs/product-blueprint/`
- 非代码目录：`product-blueprint/<project-slug>/`

文档状态：`Draft / In Review / Approved / Superseded`。不要创建 N/A 文档。每份文档写明 Blueprint version、Last updated、Status 和 Authority。

## 2. 六个核心文档

### `00_BLUEPRINT_INDEX.md`

只负责：项目/模式、版本、权威文档地图、阅读顺序、门禁证据、Blocking/Conditional 摘要、旧版资料权威声明和开发入口。不复制产品正文。

### `PROJECT_STATE.md`

运行状态：事实、偏好、推断、推荐、授权默认、决定摘要、假设、矛盾、风险、未决项、依赖、frontier、用户需准备事项、最近变更和下一步最小行动。高影响决定只放一行摘要并链接 `DECISIONS.md`。

### `PRODUCT_BLUEPRINT.md`

唯一权威：产品一句话、用户/场景/问题/结果、价值与指标、角色/JTBD、产品原则、核心旅程、范围、功能优先级、运营/商业责任、信息架构和非目标。

### `EXPERIENCE_BLUEPRINT.md`

唯一权威：页面/屏幕体验、导航和流程细节、内容层级、状态、选定视觉方向、tokens、组件、响应式、动效、可访问性和体验验收。视觉探索过程放条件模块，不复制三套方向。

### `SYSTEM_BLUEPRINT.md`

唯一权威：统一语言、角色/权限、实体/关系、状态机、不变量、持久化、接口/事件约定、错误、文件/第三方/异步、安全、部署和非功能要求。大型契约可拆条件模块并在此建立索引。

### `BUILD_AND_ACCEPTANCE.md`

唯一权威：`ACT-*` 追踪矩阵、行为验收、测试策略、release blockers、纵向切片、ticket 依赖、开发 Agent 阅读顺序、冻结决定、首个 frontier、定义完成和停止升级条件。

## 3. 决定日志

首次出现跨领域、高影响、高成本或难以逆转的决定时创建 `DECISIONS.md`。每项包含：ID、日期、状态、背景、事实/约束、真实选项、决定、理由、影响、可逆性、depends_on、affects 和 revisit trigger。

低风险排版细节或成熟默认留在对应权威文档/State，不制造 ADR 官僚主义。

## 4. 条件模块

| 模块 | 触发条件 | 最终权威关系 |
|---|---|---|
| `CURRENT_PRODUCT_AUDIT.md` | Existing Product | 记录现状证据；未来决定仍归核心蓝图 |
| `VISUAL_EXPLORATION.md` | 需要比较方向或生成视觉资产 | 保留方案与取舍；选定契约归 Experience |
| `PLATFORM_CONSTRAINTS.md` | 小程序、原生、桌面、多端或平台规则显著影响 | 平台证据；产品/体验/系统引用 |
| `CONTENT_AND_COPY.md` | 营销、内容、SEO、本地化或大量结构化文案 | 文案与内容模型权威 |
| `RESEARCH_EVIDENCE.md` | 外部研究改变决策 | 来源、日期、结论与受影响决定 |
| `DATA_AND_API_CONTRACTS.md` | 大型 schema/API 使 System 失去可读性 | 详细契约权威，System 只保留边界与索引 |
| `MIGRATION_PLAN.md` | 现有数据、角色、接口、视觉或平台迁移 | 迁移顺序、兼容、回滚和验收权威 |
| `SECURITY_AND_COMPLIANCE.md` | 支付、敏感数据、合规、UGC、高风险多租户 | 威胁、控制、证据、owner 与验证权威 |

不满足触发条件就不创建。

## 5. 单一事实来源

- 一条事实、规则或决定只有一个完整定义位置。
- 其他文档使用稳定 ID、章节链接或一句摘要。
- State 保存当前进度，不复制最终规格；Index 保存导航，不复制正文；Build 保存追踪，不重新定义业务规则。
- 条件模块被合并或不再适用时标记 Superseded，并在 Index 指向替代来源。

## 6. 更新节奏

- 每轮更新 State。
- 决定闭合或变化时更新对应权威文档、Index 状态和相关追踪。
- 不在每次用户回答后重写所有文档。
- 用户暂停前必须更新下一步最小行动；Ready 前冻结版本并确保所有链接有效。
