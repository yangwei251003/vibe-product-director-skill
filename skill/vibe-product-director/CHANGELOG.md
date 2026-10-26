# Changelog

## 2.2.0 — 2026-08-29

- 将 Ask-Matt 风格的阶段路由升格为强制主流程：Route → Stateful Grilling → Evidence Detour → Blueprint → Tickets → Ready → Development Bridge。
- 修复“一轮问完即收尾”：总轮数不设上限；回答后必须落盘、扩展 design tree、重算 frontier 并自动进入下一轮。
- 删除“同一决定最多一次深挖”的误导约束，明确边界、例外、失败、所有权和恢复是需要继续访问的 child decisions。
- 新增九类最低覆盖扫描、访谈退出门和共同理解确认；未访问分支、未验证 Fog 或等待回答均阻止 Blueprint Synthesis。
- 将 Grill-with-Docs 变成原生行为：每轮更新 State，术语即时进入规范语言，高影响取舍进入 Decisions，关闭结论进入唯一权威蓝图。
- 限定“按推荐”只作用于当前已展示 nodes；Express 使用更多默认但不跳过覆盖。
- 新增 ticket map 用户审阅、阶段边界与上下文卫生契约，并扩展为 28 个多轮行为场景。

## 2.1.0 — 2026-08-29

- 新增 Destination、局部 Decision Map、Fog 和决策就绪简报，使复杂项目按真实依赖解锁而不是延长访谈。
- 新增最小证据阶梯、利益相关者问卷和用户授权的隔离证据原型，形成 `Question → Evidence → Observation → Decision` 闭环。
- 新增规范领域语言、bounded context、深模块、公开测试 seam 和高锁定接口双方案约束。
- 强化阶段边界与后移检查点：先完成 Agent 可做的事实、研究和准备，再请求用户做价值决定或人工门操作。
- 强化 tracer-bullet 纵向切片、宽迁移 expand–migrate–contract、耐久任务简报、Human Gates 和双轴开发审查。
- 增加三个条件模板和四个多轮评测场景；升级构建、校验与安全安装版本契约。

## 2.0.0 — 2026-08-26

- 将固定七阶段重构为依赖驱动的自适应决策引擎。
- 将八种工作方式实现为 Context、Depth、Focus 三个可组合维度。
- 将默认 18 份文档压缩为六份核心蓝图和条件模块。
- 新增决定传播、抗循环、决策疲劳预算和明确停止机制。
- 强化审美翻译、反 AI 模板化、动效行为契约与平台差异。
- 强化 MVP Remove-One、领域状态机、权限、异步、第三方和恢复链路。
- 用证据化 Pass / Conditional / Blocked 门禁替代 100 分 Ready 阈值。
- 新增 Skeptic、Simplifier、Blind-Handoff 三重最终审查。
- 重写安装脚本，默认拒绝静默覆盖并提供 dry-run 与可恢复备份。
- 新增确定性校验、manifest 生成、ZIP 构建和完整行为评测集。

## 1.0.0 — 2026-08-26

- 首个可安装版本。
- 支持 Greenfield、Existing Product、Resume 和 Fast Track。
- 引入视觉、功能、前后端追踪、文档契约和质量门禁。
