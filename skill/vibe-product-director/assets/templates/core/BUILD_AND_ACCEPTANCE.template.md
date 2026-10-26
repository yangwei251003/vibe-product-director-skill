# Build and Acceptance

## 交付策略

- 当前目标：{{outcome}}
- 首个纵向切片：{{end-to-end slice}}
- 冻结默认：{{conditional defaults}}
- 不在本轮：{{later/non-goals}}

## 纵向任务

默认从 tracer-bullet 开始：用最细真实路径贯穿界面、状态、权限、数据和测试。宽迁移仅在必要时使用 `expand → migrate batches → contract`。

| 顺序 | 切片/任务 | 用户价值 | Blocking edges | 涉及 ACT/DEC | 前端 | 后端/数据 | 测试 | 完成条件 |
|---|---|---|---|---|---|---|---|---|
| 1 | {{slice}} | {{value}} | {{deps}} | {{ids}} | {{ui work}} | {{system work}} | {{tests}} | {{observable done}} |

### Ticket map 审阅

- 用户审阅日期/来源：{{date + turn/reference}}
- 粒度结论：{{approved / requested split or merge}}
- Blocking edges 结论：{{approved / corrected}}
- 当前 frontier：{{tickets whose blockers are complete}}

### 耐久任务简报

每张任务补齐：`当前行为 / 期望行为 / 范围 / Out of scope / 权威链接 / 关键接口 / 验收 / 演示 / 验证命令 / no-op 或幂等 / stop-escalate`。不要依赖聊天记录、易漂移行号或实现者自行补产品决定。

## 验收场景

| 场景 | Given | When | Then | 恢复/边界 | 自动化层级 |
|---|---|---|---|---|---|
| {{scenario}} | {{given}} | {{when}} | {{then}} | {{edge}} | {{unit/integration/e2e/manual}} |

存在多个身份因子时，验收至少覆盖：首次绑定、重复登录、因子撞已有主体、并发绑定、换绑/合并/拒绝或恢复、会话撤销、历史资源归属与审计。

## 发布与监控

{{迁移、feature flag、回滚、指标、告警、支持与复盘触发条件。}}

## Human Gates

| Owner | 精确人工动作 | Agent 准备 | 返回证据 | Blocks | 触发/截止 | 不可逆确认 |
|---|---|---|---|---|---|---|
| {{owner}} | {{action}} | {{draft/checklist/test entry}} | {{evidence}} | {{slice/release}} | {{when}} | {{confirmation}} |

## 开发后审查

- Standards：{{quality/security/performance/project conventions + evidence}}
- Specification：{{frozen Product/Experience/System/Acceptance conformance + evidence}}
- 规格矛盾处理：{{pause affected slice → update authority → resume}}

## 交接检查

- [ ] 无 Blocking 未决项
- [ ] Stateful Grilling 退出门与用户共同理解确认已通过
- [ ] 首个纵向切片无需重新做关键产品决定即可执行
- [ ] Skeptic / Simplifier / Blind-Handoff 审查通过
- [ ] 权限、状态、数据、错误、异步、监控和测试均有闭环
- [ ] Conditional 默认及重开条件已冻结
- [ ] 任务依赖、Human Gates、权威链接和停止/升级条件可由新 Agent 独立理解
- [ ] Ticket 粒度、独立演示结果和 blocking edges 已经用户审阅
