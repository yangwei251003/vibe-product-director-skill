# Project State

> 本文件是决策状态与恢复入口；只记录当前有效状态和可追溯历史，不复制其他蓝图正文。

## 项目上下文

- 产品：{{name}}
- 上下文：{{Greenfield|Existing Product|Resume|Blueprint Revision}}
- 深度：{{Express|Standard|Deep}}
- 当前焦点：{{default|Visual-First}}
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

## 风险

| ID | 风险 | 概率/影响 | 缓解 | 触发器 | 状态 |
|---|---|---|---|---|---|
| RISK-001 | {{risk}} | {{rating}} | {{mitigation}} | {{signal}} | {{status}} |

## 决策传播队列

| 变更决定 | 废弃项 | 受影响 ID/文档 | 需重算 | 状态 |
|---|---|---|---|---|
| DEC-001 | {{old}} | {{targets}} | 体验/系统/测试/任务 | {{status}} |

## 下一步

{{只写依赖已满足且影响最大的下一个决策、验证或交接动作。}}

