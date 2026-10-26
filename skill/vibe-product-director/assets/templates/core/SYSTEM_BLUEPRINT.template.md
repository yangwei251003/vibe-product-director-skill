# System Blueprint

## 系统边界

- 客户端/平台：{{clients}}
- 服务与存储：{{services}}
- 第三方：{{third parties}}
- 信任边界：{{trust boundaries}}

## 规范语言

| Preferred term | 通俗含义 | 类型/上下文 | Avoid aliases | 示例/边界 |
|---|---|---|---|---|
| {{term}} | {{meaning}} | {{Actor/Role/Entity/Value/Event + context}} | {{ambiguous aliases}} | {{scenario and non-example}} |

若术语跨多个 bounded context 或表格使本文件难读，拆到 `DOMAIN_LANGUAGE.md`，本节只保留关键词与索引。

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

## 模块与公开 seam

| 能力模块 | 调用者 | 公开契约 | 隐藏的复杂性 | 错误/取消/超时 | 测试 seam | 替换/迁移 |
|---|---|---|---|---|---|---|
| {{deep module}} | {{caller}} | {{small complete interface}} | {{internals}} | {{behavior}} | {{public behavior test}} | {{adapter/exit path}} |

只有高锁定或难逆边界才记录双方案比较；普通可逆实现不制造抽象。一个真实适配器时保留 seam，不把假想第三方写成需求。

## 技术决策

{{只记录已批准或授权默认的技术方向；高影响项引用 DEC-*，未知项进入 OPEN-*。}}
