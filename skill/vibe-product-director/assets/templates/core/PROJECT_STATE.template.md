# Project State

> 本文件是决策状态与恢复入口；只记录当前有效状态和可追溯历史，不复制其他蓝图正文。

## 项目上下文

- 产品：{{name}}
- Destination：{{actor + scenario + observable result + hard constraints}}
- 上下文：{{Greenfield|Existing Product|Resume|Blueprint Revision}}
- 深度：{{Express|Standard|Deep}}
- 当前焦点：{{default|Visual-First}}
- 当前 phase：{{Stateful Grilling|Evidence Detour|Blueprint Synthesis|Tickets|Ready|Development}}
- 当前 round：{{N}}
- Discovery 状态：{{Active|Coverage Scan|Awaiting Confirmation|Closed}}
- 当前 frontier：{{highest-impact eligible decision}}
- 最近证据读取：{{files, screenshots, repository, user statements}}

## 状态账本

| 类型 | 内容 | 来源/证据 | 置信度 | 最后更新 |
|---|---|---|---|---|
| 事实 | {{fact}} | {{source}} | 高 | {{date}} |
| 偏好 | {{preference}} | 用户 | 高 | {{date}} |
| 推断 | {{inference}} | {{basis}} | {{level}} | {{date}} |
| 推荐 | {{recommendation}} | {{reason}} | — | {{date}} |
| 授权默认 | {{default}} | {{reason + reopen condition}} | — | {{date}} |
| 用户决定 | {{decision}} | {{quote/turn}} | — | {{date}} |
| 假设 | {{assumption}} | {{validation plan}} | {{level}} | {{date}} |
| 矛盾 | {{conflict}} | {{sources}} | — | {{date}} |

## 未决项

| ID | 等级 | 问题 | 默认/选项 | 依赖 | 所有者 | 重开条件 |
|---|---|---|---|---|---|---|
| OPEN-001 | Blocking | {{question}} | {{default}} | {{deps}} | {{owner}} | {{condition}} |

## Design Tree / Decision Map

只索引决定与父子/依赖，不复制决定正文。回答一轮后立即更新状态并生成/删除 child nodes。

| Node | Parent | 状态 | depends_on | unlocks/blocks | 用户回答/默认 | 权威来源 | 下一证据/动作 |
|---|---|---|---|---|---|---|---|
| DEC-001 | {{root/node}} | {{Unvisited|Fog|Frontier|Asked|Resolved|Authorized Default|Conditional|Later|Blocked|Superseded}} | {{ids}} | {{ids/slice}} | {{answer/default}} | {{link}} | {{evidence or brief}} |

## Discovery 覆盖

| 根分支 | 适用性证据 | 状态 | 未关闭 nodes | 最近压力测试 |
|---|---|---|---|---|
| Destination | {{evidence}} | {{Unvisited|Active|Closed|Not applicable}} | {{ids}} | {{scenario/result}} |
| Roles & Value | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |
| Journey & Scope | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |
| Experience | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |
| Domain | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |
| System | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |
| Failure & Recovery | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |
| Platform & Risk | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |
| Delivery | {{evidence}} | {{status}} | {{ids}} | {{scenario/result}} |

## Fog

| 区域 | 为什么重要 | 当前为何不能准确提问 | 解雾证据 | 可能解锁 |
|---|---|---|---|---|
| {{area}} | {{impact}} | {{unknown}} | {{read/research/person/prototype}} | {{decisions}} |

## 风险

| ID | 风险 | 概率/影响 | 缓解 | 触发器 | 状态 |
|---|---|---|---|---|---|
| RISK-001 | {{risk}} | {{rating}} | {{mitigation}} | {{signal}} | {{status}} |

## 决策传播队列

| 变更决定 | 废弃项 | 受影响 ID/文档 | 需重算 | 状态 |
|---|---|---|---|---|
| DEC-001 | {{old}} | {{targets}} | 体验/系统/测试/任务 | {{status}} |

## Human Gates

| Owner | 精确人工动作 | Agent 已完成准备 | 返回证据 | Blocks | 触发/截止 | 不可逆确认 |
|---|---|---|---|---|---|---|
| {{owner}} | {{action}} | {{prep}} | {{evidence}} | {{decision/slice}} | {{when}} | {{yes/no + confirmation}} |

## 下一步

{{只写依赖已满足且影响最大的下一轮 frontier、验证或真正的 phase boundary；若需用户决定，链接已准备好的决策简报。}}
