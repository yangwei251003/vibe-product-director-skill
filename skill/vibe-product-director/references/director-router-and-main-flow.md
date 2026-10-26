# Director Router and Main Flow

每次 Vibe Product Director 触发时读取。本文件把“当前该走哪条流程”内置为产品总导演职责；用户不需要记住或手动组合其他 Skill。

## 1. 先路由，再行动

读取现有证据后判断当前入口，并用一行自然语言告诉用户当前流程和理由：

| 入口 | 识别信号 | 当前流程 |
|---|---|---|
| 新想法/重大改版，能在当前任务收敛 | 仍有产品、体验或系统决定未关闭 | Stateful Grilling → Blueprint Synthesis → Tickets → Ready |
| 暂无可写目录 | 只有聊天中的想法 | 临时 Grilling；一旦目标位置明确立即转为 Stateful |
| 超出单次任务的大型 effort | 多产品/多团队/多端，路径仍在 Fog 中 | Wayfinding：局部 Decision Map → 逐个关闭 decision tickets → 回到主流程 |
| 纸面无法回答的设计问题 | 状态、业务逻辑或 UI 必须运行/看见才可判断 | Evidence Detour：handoff → throwaway prototype → observation handback → 回到原决定 |
| 关键事实只在他人脑中 | 运营、法务、财务、销售或真实用户掌握 | Stakeholder Questionnaire → 回收证据 → 回到 Grilling |
| 设计树已关闭 | 共同理解已确认，没有未访问的适用分支 | Blueprint Synthesis；不重新访谈 |
| 蓝图已冻结 | 需要拆成可独立执行工作 | Tracer-bullet Tickets → 用户审阅粒度/阻塞边 |
| 用户明确“开始开发”且 Ready | 首切片无 Blocking | Development Bridge；按 ticket 实现和验证 |
| 明确 Bug、单组件/API、PR 或已批准 ticket | 产品决定已完成 | 退出本 Skill，交给对应实现/诊断能力 |

不要把路由做成让用户先选模式的菜单。能从证据推断就直接选择；只有两条路径会造成实质不同的成本、风险或输出且无法推断时才询问。

## 2. 主流程：idea → build

### Phase A — Stateful Grilling

默认入口。读取 [stateful-grilling.md](stateful-grilling.md)，建立 design tree，逐轮访问 frontier，并把答案实时写入 State、领域语言、Decisions 和受影响蓝图。不得在第一轮问答后直接总结 Ready。

### Phase B — Evidence Detours（按需）

如果当前 decision 不能仅靠对话可靠关闭：

1. 在原线程和 State 中写清问题、判据、权威决定与返回格式。
2. 研究、问卷或原型在隔离位置进行；不让 side task 改写生产代码。
3. 带回观察而不是整段噪声，将结果回写原 decision。
4. 重算 design tree，继续下一 frontier。

详细证据契约见 [decision-evidence-and-prototyping.md](decision-evidence-and-prototyping.md)。Detour 是主流程的支线，不是新的终点。

### Phase C — Blueprint Synthesis

只有 Stateful Grilling 退出门通过后进入。综合同一任务中的证据和决定，不重新启动访谈，不悄悄增加新需求。若综合时发现真实缺口，将它变成 design-tree node，退回 Phase A，只重开受影响分支。

### Phase D — Tickets

从冻结蓝图拆 tracer-bullet 纵向切片并声明 blocking edges。先给用户审阅任务粒度、依赖和可独立演示结果；批准后才冻结到 `BUILD_AND_ACCEPTANCE.md`。宽迁移使用 expand → migrate batches → contract。

### Phase E — Ready / Development Bridge

完成 Skeptic、Simplifier、Blind-Handoff 后宣告 Ready。用户明确说“开始开发”才进入首个无阻塞 ticket；实现期按预先约定的公开 seam 建立反馈循环，逐个纵向切片验证，完成后分别检查 Standards 与 Specification。发现产品决定缺失就暂停受影响 ticket，回到 Phase A/C，不在代码里发明规则。

## 3. 大型 effort：Wayfinding on-ramp

只有当 destination 已知但路径无法装进当前任务、决策依赖跨多团队/多阶段时使用。Map 中的节点是 decisions，不是 deliverables；先推开 Fog、关闭互相依赖的决定。路径清晰后必须回到 Blueprint Synthesis → Tickets，不能从模糊 Map 直接跳开发。

普通网站、单一 App MVP 或范围明确的 feature 不使用重量级 Wayfinding；State 中的小型 design tree 足够。

## 4. Context hygiene 与阶段边界

- 从首次 Grilling 到 ticket 草案，优先留在同一个连续任务中，让原始回答和推理保持为 primary source。
- 用户答完一轮不是 phase boundary；只要 design tree 仍有 frontier，就继续下一轮。
- 真正的 boundary 是：访谈关闭、证据支线开始/返回、蓝图冻结、ticket map 批准、开始开发、QA。
- 在 boundary 先问：能否继续当前任务？若下一阶段仍依赖当前推理且上下文健康，优先 Continue。
- 只有换目录/宿主/协作者或必须分叉 side task 时才 handoff；只有任务可在无人 steering 下独立完成时才委派。
- 必须切换或压缩前，先更新 State、唯一权威文档、当前 frontier 和下一最小行动。

## 5. 路由可见性

用户只需要看到简短状态，不需要看到内部 Skill 名单：

```text
当前流程：Stateful Grilling（第 2 轮）→ Blueprint → Tickets → Ready
本轮目标：关闭“谁能创建并审批行程”这一 frontier；回答后会继续展开它解锁的权限和恢复问题。
```

不要用“我先问几个问题”暗示问完这一批就结束。说明这是当前轮，后续轮次由本轮答案动态解锁。
