# Vibe Product Director 2.2.0 · 评测报告

> 2.2 纠偏执行日期：2026-08-29。本文只记录实际运行、静态契约检查和明确限制；“静态通过”不等同于真实模型或跨平台运行通过。后半部分保留 2.1 与 2.0 的历史评测。

## 2.2 纠偏结果

| 评测 | 实际结果 | 证据性质 |
|---|---|---|
| 官方 `quick_validate.py`（UTF-8） | Pass：`Skill is valid!` | 2026-08-29 实际执行 |
| 2.2 发布校验 | Pass | Frontmatter、YAML、链接、JSON/CSV/JSONL、manifest、ZIP 安全与字节一致性 |
| 构建确定性 | Pass | 连续构建 ZIP SHA-256 均为 `c27144cfb7b450fbce37d3e0e6a2335eb6a03b6e6b34c54d4b6557a1adce3f47` |
| 触发集 | 17 正向 + 9 负向 | 26 条静态契约覆盖；非宿主真实触发率 |
| 行为集 | 28 条唯一场景 | 格式与观测契约通过；其中 B21–B28 专测持续追问与主流程 |
| PowerShell 临时安装 | Pass | dry-run、首次安装与幂等实际执行 |
| Bash 临时安装 | Pass | 语法、dry-run、首次安装与幂等在 Windows Bash 实际执行 |
| 独立多轮前向测试 | Pass（4 个连续回合） | 独立 Agent 使用源 Skill 和隔离目录实际执行 |
| 全局升级 | Pass：2.1.0 → 2.2.0 | 实际安装到 `%USERPROFILE%\.agents\skills\vibe-product-director`；源/目标 manifest 哈希一致 |

2.2 包含 40 个文件，其中 manifest 登记其余 39 个；ZIP 只有 `vibe-product-director/` 一个顶层目录。ZIP 为 81,141 bytes；独立入口为 13,931 bytes。

### 独立前向测试

独立 Agent 没有读取本报告、融合审计、旧版本或预期修复结论。它只获得 2.2 源 Skill、隔离工作目录和真实请求：“规划一个同小区居民交换摄影/烘焙技能的微信小程序；按建议推进；开始开发前不写生产代码。”

实际轨迹：

1. **第 1 轮**：提出 3 个上游问题（首批用户、可观察成功、交换机制），创建 `PROJECT_STATE.md`，并明确回答后会继续居民核验、旅程与安全边界。
2. 用户说“这一轮全按推荐”后，Agent 只批准当前 3 个 nodes；**第 2 轮**继续 4 个新 frontier（居民核验、身份可见性、双清单、线上/线下），没有把授权扩展到未来分支。
3. 用户批准第 2 轮后，**第 3 轮**继续 4 个 child decisions（运营 owner、技能卡字段、结构化邀约、单方完成确认），并同步更新状态和权威蓝图。
4. 用户批准并要求“直接给最终蓝图”后，Agent 没有提前收尾；它记录“用户要求加速”，安全默认低风险项，同时指出仍有 4 个 Blocking，并进入**第 4 轮**处理邀请生命周期、联系方式披露、取消/爽约/举报和视觉方向。

第 4 轮时隔离目录已有 10 份实际文档、71,712 bytes；`PROJECT_STATE.md` 显示 `round: 4 / Discovery: Active`，并保留 Asked、Authorized Default、Unvisited 和当前 frontier。全程没有生产代码。

这次测试直接覆盖了用户报告的失败模式：Skill 不再把每轮 3–4 个问题理解成总问题量，也不会因“按推荐”或“现在出最终蓝图”而跳过尚未关闭的高影响分支。

全局替换前，安装脚本把 2.1.0 完整备份到 `%USERPROFILE%\.agents\skills\vibe-product-director.backup-20260829-214307`，本次未删除。

### 2.2 限制

- 前向测试执行到第 4 轮，验证了持续访谈和拒绝提前收尾；没有为了评测继续代替用户完成整棵树，因此未在该案例中实际跑到共同理解确认、ticket map 和开发阶段。
- 测试使用模拟项目和合理用户回答，不代表真实社区、法律、微信审核或运营批准。
- 未在 macOS 原生 runner 执行安装，也未测真实宿主的隐式触发 precision/recall。

## 2.1 增量结果（历史）

| 评测 | 实际结果 | 证据性质 |
|---|---|---|
| 官方 `quick_validate.py`（UTF-8） | Pass：`Skill is valid!` | 2026-08-29 实际执行 |
| 2.1 发布校验 | Pass | 实际执行：Frontmatter、YAML、链接、JSON/CSV/JSONL、manifest、ZIP 安全与字节一致性 |
| 构建确定性 | Pass | 相同源目录连续构建的 ZIP SHA-256 均为 `f861a57b6abc9aa8ed7fa64a1830dbd8571a035005ca84b441dbe2f95aa25aba` |
| 触发集 | 16 正向 + 9 负向 | 25 条静态契约覆盖；非宿主真实触发率 |
| 行为集 | 20 条唯一场景，格式与观测契约通过 | 静态契约检查；未执行 20 组真实模型多轮会话 |
| PowerShell 临时安装 | Pass | dry-run、首次安装、幂等、不同版本拒绝、force 备份均实际执行 |
| Bash 临时安装 | Pass | 语法、首次安装、幂等、不同版本拒绝、force 备份均在 Windows Bash 实际执行 |
| 全局升级 | Pass：2.0.0 → 2.1.0 | 实际安装到 `%USERPROFILE%\.agents\skills\vibe-product-director`；源/目标 manifest 哈希一致 |

2.1 包含 38 个文件，其中 manifest 登记其余 37 个；ZIP 只有 `vibe-product-director/` 一个顶层目录。独立 `SKILL.md` 与包内入口逐字节一致。2.1 ZIP 为 68,687 bytes；独立入口为 12,118 bytes。

### 2.1 契约回归重点

新增 B17–B20 覆盖：复杂决定图与 Fog、用户授权的隔离证据原型、外部知情人问卷、宽迁移与 Human Gates。量表新增“决策证据”和“开发可执行性”两维，并把“未授权原型写入生产路径”以及“证据没有关闭/缩小/停止任何分支”设为必须失败条件。

当前检查能证明文件结构、发布完整性和规则自洽，不能证明真实模型每次都能正确控制问题数、准确选择 frontier 或产出高质量原型。未重新执行 20 组真实多轮模型会话，也未在真实项目上做 2.0/2.1 A/B；这些限制不能表述为 Pass。

全局替换前，安装脚本把 2.0.0 完整备份到 `%USERPROFILE%\.agents\skills\vibe-product-director.backup-20260829-124143`。该备份可用于人工回滚，本次未删除。

## 2.0 基线环境（历史）

## 环境

- Windows NT 10.0.26200.0
- PowerShell 7.6.3
- Python 3.12.6
- 当前可用 shell：STM32CubeCLT 随附的 POSIX shell（Windows）
- 无 macOS 原生 runner；未在 macOS 原生执行安装。
- 未安装到用户全局 Skill 目录；安装测试全部使用系统临时目录。

## 2.0 结果总览（历史）

| 评测 | 实际结果 | 证据性质 |
|---|---|---|
| 官方 `quick_validate.py`（UTF-8 模式） | Pass | 实际执行 |
| 自定义发布校验 | Pass | 实际执行 |
| 触发集 | 14 正向 + 8 负向，格式/边界契约 22/22 覆盖 | 静态契约检查；非宿主真实触发率 |
| 16 个行为场景 | 初次 12 Pass / 4 Conditional / 0 Fail；修复后 16 Pass / 0 Conditional / 0 Fail | 独立 Agent 规则桌面模拟；非真实多轮 runner |
| v1/v2 同输入回归 | 9 个代表场景完成 | 独立 Agent 文本模拟 |
| PowerShell 安装 | Pass | 临时目标实际执行 |
| POSIX shell 安装 | Pass | Windows 随附 shell + 临时目标实际执行 |
| 三个端到端蓝图 | 3/3 生成，六核心齐全 | 独立 Agent 实际生成 |
| Blind-Handoff | 首轮 2 Pass / 1 Fail；修复后 3 Pass / 0 Fail | 独立 Agent 只读蓝图 |

## 1. 静态与发布验证

### 实际执行

```text
python -X utf8 .../skill-creator/scripts/quick_validate.py vibe-product-director
Skill is valid!
```

```text
python -X utf8 vibe-product-director/scripts/validate_release.py \
  --skill-dir vibe-product-director \
  --zip vibe-product-director-v2.0.0.zip \
  --standalone vibe-product-director-v2.0.0-SKILL.md
Validation passed
```

自定义验证实际覆盖：

- UTF-8 Frontmatter、Skill 名称与 description。
- `agents/openai.yaml` 可解析且隐式调用开启。
- JSON、CSV、JSONL 可解析；行为场景恰为 16 条唯一 ID。
- Markdown 相对链接存在。
- 顶层白名单，无缓存、临时文件或外部报告入包。
- Manifest 覆盖除自身外的全部发布文件，字节数与 SHA-256 相符。
- ZIP 无绝对路径或 `..`，且只有 `vibe-product-director/` 一个顶层目录。
- ZIP 内容与源目录逐字节一致；独立 SKILL 与包内 `SKILL.md` 逐字节一致。

发布包共 34 个文件（Manifest 登记另外 33 个文件）。构建脚本给脚本文件写入 Unix executable mode，并使用固定时间戳以减少无意义构建差异。

### 限制

`quick_validate.py` 主要验证 Skill 入口格式，不等同于完整发布验证；因此同时运行了包内验证器。没有在真实 Codex 宿主上测量隐式调用的 precision/recall。

## 2. 触发评测

`evals/trigger-cases.csv` 包含 14 类正向与 8 类负向：Greenfield 网站、React/Web App、移动、桌面、小程序、多端、Existing、v2 Resume、v1 Resume、Revision、Visual-First、Express、Deep、模糊产品；以及局部 UI、Bug、单组件、单 API、PR、已批准 ticket、仅文案、依赖升级。

解析、唯一 ID 和数量检查通过。逐条对照 Frontmatter 与 `SKILL.md` 边界，22 条均有明确契约结论。该结果是定义覆盖，不是宿主自动触发实测；真实误触发/漏触发率尚未测量。

## 3. 16 个多轮行为场景

独立评测 Agent 只读取 `SKILL.md`、场景文件和实际触发的 references，没有读取本报告、升级审计或 rubric。它逐项模拟问题量、重复提问、文档触发、停止时机和前后端闭环。

### 首轮

- Pass：12
- Conditional：4（B01、B05、B06、B13）
- Fail：0

发现并修复：

1. B01：明确首轮 `PROJECT_STATE.md` 落盘时机。
2. B05：会妨碍核心任务的已知无障碍失败必须 Blocking，用户坚持不能降级门禁。
3. B06：Existing Product 强制建立“保留行为 → 证据 → 回归测试”基线。
4. B13：有期限/容量约束时重复 Remove-One 并缩小切片，直到容量证据通过；关键容量证据缺失为 Blocking。

### 修复后复核

- Pass：16
- Conditional：0
- Fail：0

关键行为证据包括：复杂问题可单问、通常 2–4 问；“按推荐”形成 Authorized Default 且不重复确认；v1/v2 Resume 不重问已批准决定；Revision 废弃旧决定并沿依赖传播；Blocking 时“开始开发”不写生产代码；仅 Conditional/Later 时冻结默认并交接；支付、退款、第三方异步和删除恢复均需端到端闭环。

### 限制

这是独立规则桌面模拟，不是 16 组真实模型多轮会话。它证明规则覆盖和内部一致性，不能证明模型每次都遵守问题预算、更新顺序或不重复。场景未附真实生产仓库和平台账号，无法验证事实发现质量和官方平台规则新鲜度。

## 4. v1 / v2 回归

独立评测 Agent 使用 9 个相同输入比较两份入口 Skill，覆盖模糊 Greenfield、Visual-First、Existing 多角色改版、Resume、已批决定变更、小程序登录支付、提前开始开发、负向局部 UI 和 MVP 膨胀。

| 指标 | v1 | v2 | 观察 |
|---|---:|---:|---|
| 入口行数 | 258 | 141（最终修正后） | 高频入口更短，细节路由到 references |
| 常规单轮问题 | 3–6 | 通常 2–4，简单独立最多 5 | 降低决策疲劳 |
| 六个普通场景问题范围合计 | 18–36 | 10–22 | 文本模拟，不是实测均值 |
| 默认命名文档 | 21；Existing 常为 22 | 6；重要决定后通常 7 | 核心基线减少约 67%–71% |
| Resume | 旧索引 | v1/v2 索引兼容 | 迁移证据与新权威分离 |
| 决定变更 | 有更新但失效/依赖遍历较弱 | Superseded + In Review + 依赖传播 | 降低双重真相风险 |
| 追踪 | 业务链较完整，易把所有控件硬套后端 | 增加状态机、外部副作用、恢复、ticket 与 `local-only` | 更贴近纵向实现 |

v2 的视觉具体字段已下沉 reference；入口文件比较不能单独证明视觉输出优于 v1。包内视觉 reference 与模板确实覆盖字体、色彩、材质、组件、动效中断、触摸/键盘、reduced-motion 和低性能降级，但仍需真实生成质量评测。

## 5. 安装安全实测

PowerShell 与 POSIX shell 分别在唯一临时目录执行：

1. dry-run 不写目标。
2. 首次安装成功。
3. 同 Manifest 再安装返回 Already installed。
4. 将目标伪装为不同版本后，无 force 明确拒绝。
5. force 创建一个时间戳备份，再用经验证的暂存目录替换。

两套流程均通过。PowerShell 使用 Windows 原生路径和文件操作；shell 脚本不依赖 Python。测试没有触碰 `$HOME/.agents/skills`。

### 跨平台限制

- Shell 语法与安装流程在 Windows 随附 POSIX shell 实际执行通过。
- 未在 Linux runner 执行。
- 未在 macOS 原生执行。
- 文件权限、不同 `cp/mv/grep` 实现及 macOS 安全策略仍属于环境差异风险。

## 6. 三个端到端蓝图与 Blind-Handoff

独立生成 Agent 只使用发布 Skill 的入口、按需 references 和 templates，在临时目录生成：

| 案例 | 文档数 | 状态 | Blocking | Conditional/Later 摘要 |
|---|---:|---|---|---|
| 旅游地图 | 8 | Ready（Conditional） | 无 | 供应商/缓存许可/API key/存储预算；账号同步和实时导航 Later |
| 已有多角色平台改版 | 10 | Blocked | 缺真实仓库、权限矩阵、旧 API/schema/状态证据 | 增量迁移与 PII 边界 Conditional；AI 分派等 Later |
| 小程序登录支付 | 8 | Ready（Conditional） | 无，可先 mock/sandbox | 生产凭据、退款权限、最新平台规则与政策 Conditional；分账等 Later |

三个案例六核心文档均齐全，条件模块只按需要出现；没有模板占位符或失效本地引用。Existing 案没有为了“完成评测”伪造现状事实，而是正确保持 Evidence Gate Blocking。

### 独立 Blind-Handoff 结果

独立实现 Agent 只读取三个蓝图目录，没有读取 Skill、评测集、审计报告或生成意图。

首轮结果：

- **旅游地图：Pass。** 可直接实现 fixture 驱动的离线 TripPack 纵向切片：分片下载、中断恢复、checksum 后原子 Ready、飞行模式冷启动、损坏/空间不足/删除恢复与浏览器 E2E。无需重问产品决定；供应商许可和 API key 是后续外部证据。
- **已有多角色平台：Pass（正确 Blocked）。** 蓝图一致阻止在缺真实仓库、IAM、API/schema、状态与测试账号时写生产状态；独立 Agent 能直接执行 E0 只读证据审计，建立行为→证据→characterization test 基线。需要索取的是外部事实，不是重问产品选择。
- **小程序登录支付：Fail。** 首版遗漏 canonical principal、OpenID/UnionID/手机号唯一性、撞号拒绝/换绑/合并、历史订单归属、会话撤销和审计决定。这些会改变唯一约束、ownership、账号恢复和首切片测试，不能留给开发 Agent。

针对 Fail，更新 Skill 的 `system-integrity.md`、readiness 和 System/Build 模板：多身份因子场景必须在首个身份切片前冻结上述契约，未知时为 Blocking。随后只重算小程序案例的 State、Decisions、System、Build 和 Index，采用明确默认：内部不可变 `User.id` 为 canonical；OpenID 按环境/AppID 唯一，UnionID 仅在对应开放平台范围使用，ACTIVE 手机号绑定全局唯一；撞号不自动合并/换绑；历史订单不迁移；身份变化撤销相关会话并写不可变审计；并发由事务锁、唯一约束和幂等收敛。

修复后，独立 Agent 只重读小程序蓝图并判定 **Pass**：首个 mock/sandbox 身份与支付纵向切片可直接实施，首次/重复登录、撞号、并发、换绑、合并、历史订单、会话撤销、Webhook 重放和查单恢复都有可测试结论，无需重新询问关键产品决定。

最终 Blind-Handoff：**3 Pass / 0 Fail**。其中 Existing 案的 Pass 意味着“正确识别并遵守 Blocking，只做 E0”，不等于在缺证据时可实施生产功能。

## 7. 未覆盖与后续建议

- 未进行真实 Codex 宿主隐式触发 A/B。
- 未执行 16 组真实多轮模型会话；当前是独立规则模拟。
- 三个案例使用合理模拟默认，不代表真实用户、业务、法律或平台批准。
- 未使用真实微信商户、地图供应商、生产数据或现有多角色仓库。
- 未在 macOS/Linux 原生 runner 执行安装。
- v2 的真实优势应在后续项目中继续采集：实际问题数、重复率、文档使用率、实现返问、返工和验收失败。
