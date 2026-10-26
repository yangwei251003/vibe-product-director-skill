# Build and Acceptance

## 交付策略

- 当前目标：{{outcome}}
- 首个纵向切片：{{end-to-end slice}}
- 冻结默认：{{conditional defaults}}
- 不在本轮：{{later/non-goals}}

## 纵向任务

| 顺序 | 切片/任务 | 用户价值 | 涉及 ACT/DEC | 前端 | 后端/数据 | 测试 | 完成条件 |
|---|---|---|---|---|---|---|---|
| 1 | {{slice}} | {{value}} | {{ids}} | {{ui work}} | {{system work}} | {{tests}} | {{observable done}} |

## 验收场景

| 场景 | Given | When | Then | 恢复/边界 | 自动化层级 |
|---|---|---|---|---|---|
| {{scenario}} | {{given}} | {{when}} | {{then}} | {{edge}} | {{unit/integration/e2e/manual}} |

存在多个身份因子时，验收至少覆盖：首次绑定、重复登录、因子撞已有主体、并发绑定、换绑/合并/拒绝或恢复、会话撤销、历史资源归属与审计。

## 发布与监控

{{迁移、feature flag、回滚、指标、告警、支持与复盘触发条件。}}

## 交接检查

- [ ] 无 Blocking 未决项
- [ ] 首个纵向切片无需重新做关键产品决定即可执行
- [ ] Skeptic / Simplifier / Blind-Handoff 审查通过
- [ ] 权限、状态、数据、错误、异步、监控和测试均有闭环
- [ ] Conditional 默认及重开条件已冻结
