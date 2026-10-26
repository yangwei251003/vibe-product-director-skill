# Stateful Grilling Protocol

任何重要产品、视觉、业务或系统决定尚未关闭时读取。这是 Vibe Product Director 的默认访谈 primitive；目标不是达到固定问题数，而是形成可验证的共同理解。

## 1. Design tree

把待理解的产品映射成一棵依赖树：上游回答会生成、删除或改写下游问题。每个 node 只是一项 decision，包含：

```text
ID | question | parent | depends_on | unlocks | status
evidence | recommendation | user answer | authority | reopen trigger
```

状态使用：

- `Unvisited`：适用性尚未检查，不能静默忽略。
- `Fog`：知道该区域重要，但还无法准确提出问题；先收集证据。
- `Frontier`：依赖已满足，现在可以让用户决定。
- `Asked`：已经提出，等待完整回答；沉默不等于同意默认。
- `Resolved`：用户明确决定并已回写权威文档。
- `Authorized Default`：用户在看到推荐后授权采用；含理由与重开条件。
- `Conditional`：不阻塞当前切片，默认、影响、owner 和解决时点齐全。
- `Later`：明确不进入当前价值范围；必须有理由，不能用来藏未访问分支。
- `Blocked`：缺失会使核心价值、风险或首切片无法正确实现。
- `Superseded`：被新决定替代，只保留历史。

`Frontier` 只能包含 prerequisites 已关闭的 nodes。依赖本轮另一答案的 child 属于下一轮。

## 2. 最低覆盖扫描

树是自适应的，但在退出前必须检查每个适用根分支：

1. Destination：核心用户、触发场景、问题、可观察结果、成功/失败信号。
2. 角色与价值：不同角色的目标、损失、权限、运营责任和冲突。
3. 核心旅程与范围：入口、主路径、复用、MVP、非目标、Remove-One。
4. Experience：信息架构、关键屏、内容、视觉方向、响应式、动效、可访问性。
5. Domain：规范术语、实体、关系、状态机、不变量、所有权。
6. System：身份、权限、数据、接口/事件、第三方、异步、一致性。
7. Failure & Recovery：空/错/弱网/冲突/撤销/申诉/人工介入/监控。
8. Platform & Risk：平台规则、性能、安全、隐私、合规、迁移和成本锁定。
9. Delivery：行为验收、测试 seam、纵向切片、Human Gates、发布/回滚。

不适用的分支记录 `Not applicable + evidence`，而不是凭感觉不问。覆盖扫描是找遗漏的底线，不是机械地把每个项目问成同一份问卷。

## 3. 每轮算法

收到用户回答后，不等待“继续”命令，按以下顺序自动推进：

1. **Parse**：逐项识别回答、未回答、条件回答、新偏好、矛盾和新术语。
2. **Persist inline**：立即更新 State；已解决术语写入规范语言；高影响决定写入 Decisions；受影响蓝图只更新对应章节。
3. **Expand/prune**：根据答案生成必要 child nodes，删除已经失去意义的分支。
4. **Investigate facts**：读取文件、代码、截图、数据或一手资料。事实是 Agent 的工作，不问用户可自行发现的事实。
5. **Recompute**：刷新依赖、Fog、Frontier、Blocking 和覆盖状态。
6. **Ask next round**：从当前 frontier 选择 1–4 个相互独立、影响最大的 nodes；若 frontier 更多，剩余项排入后续轮次。

只要仍有 `Frontier / Asked / Blocked / 未验证 Fog / Unvisited applicable branch`，下一条回复就必须继续访谈或取证，不能宣告 Ready、输出终局总结或开始生产开发。

## 4. 轮次与问题格式

总轮数和总问题数不设上限；复杂度由 design tree 决定。每轮控制认知负担，不等于整个访谈只问一轮。

```text
第 N 轮 · <当前 frontier 主题>
已确认：<一行>
本轮回答将解锁：<一行>

❓ Q1｜<标题>
<为什么现在必须决定；真实选项及体验/成本/风险差异>
➡️ 推荐：<推荐与理由>

回复示例：Q1 选 B；Q2 按推荐；Q3 ...
```

- 一个复杂 decision 可以单独成轮；通常 2–4 个，最多 4 个。
- 不重复同一句问题；但由答案解锁的边界、例外、失败、所有权等 child decisions 不是“重复深挖”，必须继续。
- 用户只回答部分问题时，关闭已回答项，保留其余 `Asked`，再处理新解锁 frontier；不把沉默当默认。
- “按推荐”默认只批准当前明确展示的问题，不是对尚未披露分支的永久授权。
- 用户明确授权“后续低风险可逆项都按推荐”时可批量默认，但每个默认仍记录；价值、范围、身份/权限、安全、资金、难逆选择和高影响冲突仍需显式展示。
- Express 减少每个 node 的讨论成本并增加安全默认，不减少适用分支覆盖。

## 5. Stateful docs：边问边留下痕迹

有可写目标时，访谈从第一轮开始就是 stateful：

- `PROJECT_STATE.md`：round、design tree、frontier、Fog、未决项、最近回答和下一动作。
- `SYSTEM_BLUEPRINT.md` 或 `DOMAIN_LANGUAGE.md`：术语一旦解决立即写入；选一个 canonical term，把会引发歧义的别名列为 Avoid。
- `DECISIONS.md`：只记录难逆、脱离上下文会令人意外、且来自真实取舍的决定；三项缺一不创建冗长 ADR。
- Product / Experience / System：决定关闭时只更新其唯一权威章节，不把所有原始问答复制进去。
- Index：只更新阶段、权威地图和门禁，不保存访谈正文。

代码、现有页面或旧文档与用户描述冲突时立即指出并建 Conflict node。用具体异常场景压力测试术语和规则，例如并发、部分成功、重复提交、跨角色、历史数据和撤销，而不是只问抽象“还有别的吗”。

## 6. 退出门

访谈只有同时满足以下条件才结束：

1. 当前 frontier 为空，且没有等待回答的 Asked node。
2. 最低覆盖扫描的每个适用根分支都有可追溯状态，不存在未访问分支。
3. 所有 Fog 已通过证据变成 decision、明确 Conditional/Later，或因证据不足保持 Blocking。
4. 对主旅程执行一次 Skeptic scan：边界、失败、恢复、权限、运营和极端场景没有生成新的高影响 node。
5. 文档与回答无未解决矛盾；开发 Agent 不需要猜关键产品规则。
6. 向用户展示共同理解检查点：Destination、核心旅程、范围/非目标、关键决定、授权默认、Conditional/Later、仍需人类证据。
7. 用户确认理解准确，或明确要求在已列明的非 Blocking 默认下继续。

如果扫描产生新 node，继续下一轮；“我已经问了很多”不是退出理由。

## 7. 正反例

错误行为：首轮问“用户是谁、做什么、喜欢什么风格”，收到回答后直接输出完整蓝图。它跳过了由回答才解锁的角色权限、异常旅程、领域规则和交付决定。

正确行为：首轮关闭用户/结果；第二轮根据角色回答追问创建、审批和可见性；第三轮根据审批追问驳回、修改、通知和审计；随后运行覆盖扫描，只有没有新 frontier 才进入共同理解确认。

另一个错误：用户对 Q1 说“按推荐”，于是把以后所有问题都自动默认。正确做法是只关闭 Q1；下一轮仍展示新解锁的高影响 decisions。
