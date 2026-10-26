# System Blueprint

## 系统边界

- 客户端/平台：{{clients}}
- 服务与存储：{{services}}
- 第三方：{{third parties}}
- 信任边界：{{trust boundaries}}

## 角色与权限

| 角色 | 资源 | 动作 | 约束 | 拒绝反馈 | 审计 |
|---|---|---|---|---|---|
| {{role}} | {{resource}} | {{action}} | {{policy}} | {{error}} | {{event}} |

## 身份契约（存在账号或外部身份时）

| 权威主体 | 身份因子 | 唯一性范围 | 绑定/解绑 | 碰撞与恢复 | 历史资源归属 | 会话/审计 |
|---|---|---|---|---|---|---|
| {{canonical principal}} | {{phone/email/OpenID/SSO}} | {{scope}} | {{rules}} | {{reject/merge/rebind/recover}} | {{ownership migration}} | {{revocation/audit}} |

若身份冲突策略会改变唯一约束、资源 ownership 或账号恢复，不得留给实现阶段猜测。

## 领域模型与状态机

| 实体 | 关键字段 | 状态 | 允许迁移 | 不变量 | 保留/删除策略 |
|---|---|---|---|---|---|
| {{entity}} | {{fields}} | {{states}} | {{transitions}} | {{invariants}} | {{policy}} |

## 动作闭环

| ID | 权限 | 状态变化 | 数据 | API/事件 | 错误恢复 | 异步/第三方 | 监控 | 测试 |
|---|---|---|---|---|---|---|---|---|
| ACT-001 | {{auth}} | {{transition}} | {{read/write}} | {{contract}} | {{recovery}} | {{dependency}} | {{signal}} | {{coverage}} |

## 非功能约束

{{性能、可靠性、离线/弱网、隐私、安全、合规、容量、兼容性与可观测性。}}

## 技术决策

{{只记录已批准或授权默认的技术方向；高影响项引用 DEC-*，未知项进入 OPEN-*。}}
