# System Integrity

存在账号、持久数据、角色权限、文件、支付、第三方、异步、实时、通知、UGC 或复杂后台时读取。

## 1. MVP 动作链

为每个改变业务状态、共享数据、受保护资源或外部副作用的 `ACT-*` 建立：

```text
用户目标 → 页面/入口 → 动作 → 前端状态与客户端校验
→ 身份/权限 → API/Command/Event → 服务端规则与不变量
→ 领域状态变化 → 持久化 → 外部副作用
→ 成功响应 → 错误响应 → 恢复
→ 日志/监控 → 分析事件 → 验收测试 → 纵向 ticket
```

纯展示、锚点、Tab 或本地视图切换可以标 `local-only`，但仍要定义可访问性和交互状态。不得为了填矩阵伪造后端。

## 2. 领域模型

统一 Actor、Role、Entity、Value Object、Ownership、Lifecycle、State Transition、Invariant、Policy、Event 和 External System。遇到账号/用户/客户/成员/商户/组织等词，明确是否同一概念。

每个核心实体说明：标识、所有者、字段约束、关系、生命周期、允许的状态转换、不变量、查询模式、并发策略、审计、归档/删除、恢复、保留期限和外部映射。

审批、发布、订单、支付、预约、邀请、上传、生成、导入、同步等使用显式状态机：

```text
State | Allowed actor | Trigger | Preconditions | Side effects | Next state | Failure
```

## 3. 身份与权限

区分 Authentication、Authorization、Ownership、Scope、Approval、Visibility 和 Capability。权限以服务端为权威；前端隐藏按钮只是体验优化。

按需覆盖：游客、注册/验证、登录/找回、会话、设备、登出全部设备、角色/组织切换、邀请、资源级权限、审批、注销、导出、数据删除和审计。

只要存在手机号、邮箱、平台 OpenID/UnionID、SSO subject、设备身份等多个身份因子，必须在首个依赖身份的纵向切片前明确：canonical principal（权威用户主体）、各因子的唯一性与可复用范围、绑定/解绑/换绑、碰撞时拒绝/恢复/合并策略、并发绑定、历史资源所有权、会话撤销、审计与迁移。任何会改变数据库唯一约束、资源 ownership 或账号恢复的未知项都是 Blocking，不得由实现 Agent 自行选择，也不得用 happy-path mock 绕过。

## 4. API、错误与一致性

接口或事件按需记录：Purpose、Actor/permission、Trigger、Method/path/topic、Request、Validation、Idempotency、Transaction boundary、Response、Stable error code、Retry/timeout、Side effects、Audit/analytics、Versioning。

至少区分 validation、unauthenticated、forbidden、not found、conflict、rate limit、dependency unavailable、timeout、partial failure 和 internal error。错误同时定义用户可执行信息、是否重试、恢复动作和追踪 ID。

支付、发布、删除、导入和 Webhook 等不可通过“重复点击也许没事”处理；明确幂等键、去重、确认、补偿和对账。

## 5. 文件、第三方与异步

### 文件/媒体

类型、大小、数量、配额、签名上传、分片/中断/重试、预览、缩略图、压缩/转码、恶意文件、审核、访问权限、CDN、过期、孤儿清理、删除传播、版权和备份保留。

### 第三方

业务用途、数据边界、认证/密钥、费用/限额、timeout/retry/backoff、Webhook 验签/去重/重放、缓存新鲜度、降级、用户可见失败、供应商切换和退出策略。

### 异步/实时

Job ID、状态/进度、优先级、幂等、重试/dead-letter、取消、超时、补偿、通知、结果保留、重连、冲突和可观测性。

## 6. 安全与运营

按风险应用：输入校验、输出编码、服务端授权、secret 管理、least privilege、速率限制/滥用防护、CSRF/CORS/CSP/cookie、传输/静态加密、敏感数据最小化、保留/删除、审计、依赖扫描、备份/恢复演练、告警、事件响应和密钥轮换。

使用框架或云服务不等于安全已完成。高风险项目创建 `SECURITY_AND_COMPLIANCE.md`，并记录适用地域、平台或行业要求及来源日期。

## 7. 系统门禁

- 所有 MVP 业务动作有完整或明确 `local-only` 的追踪行。
- 所有重要写入有权限、业务规则、状态、数据变化和审计。
- 异步有进度、失败、重试/取消和恢复；第三方有超时与降级。
- 关键错误给用户可执行恢复，UI、系统契约、测试和 ticket 互相引用。
- 架构刚好支撑已知需求和合理增长，不为不存在的规模购买复杂度。
