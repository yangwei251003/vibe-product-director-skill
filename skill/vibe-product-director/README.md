# Vibe Product Director 2.2

面向 Vibe Coding 用户的产品总导演型 Skill。它在正式编码前，通过持续、多轮、边问边落盘的 Stateful Grilling，把网站、Web App、React 应用、移动/桌面 App、小程序、多端产品或重大改版的模糊想法，收敛成可独立交给开发 Agent 的正式蓝图。

核心优先级：

1. 视觉、UI、交互与动效。
2. 真实用户价值、功能完整性与 MVP 范围。
3. 前端、权限、领域、数据、接口、失败恢复和测试闭环。
4. 用研究、真实知情人和隔离证据原型关闭高影响未知。
5. 设计树全部适用分支关闭后，再合成蓝图、审阅 tickets 并进入开发。
6. 可恢复、低认知负担、不过度设计的交付。

## 调用

```text
使用 $vibe-product-director，从零帮我规划这个产品。我不熟悉专业术语，请给出解释和明确推荐；在我说“开始开发”前不要写生产代码。
```

内置 Director Router 会自动选择 Stateful Grilling、Wayfinding、Evidence Detour、Blueprint Synthesis、Tickets 或 Development Bridge，无需用户记忆多个 Skill。用户回答一轮后，系统会更新 State、领域语言和决定，再继续下一 frontier；每轮最多 4 个问题，但总轮数不设上限。复杂项目维护 design tree、Fog 与 frontier；讨论不足以关闭关键决定时，才请求用户授权制作隔离、可丢弃的证据原型。

“按推荐”只批准当前展示的问题，不会静默批准尚未出现的后续分支。Express 会增加安全默认，但不会把访谈缩成一轮。

## 安装

当前 OpenAI 官方文档列出的个人 Skill 目录是 `$HOME/.agents/skills`，仓库级目录是 `<repo>/.agents/skills`。

Windows PowerShell：

```powershell
.\vibe-product-director\scripts\install.ps1
```

macOS / Linux：

```bash
sh ./vibe-product-director/scripts/install.sh
```

安装脚本默认不覆盖已有不同版本。使用 `-DryRun` / `--dry-run` 预览；确认替换时使用 `-Force` / `--force`，原目录会先备份为带时间戳的同级目录。也可显式传入项目级或兼容目录。

## 包结构

- `SKILL.md`：高频决策循环、边界、停止条件和 reference 路由。
- `references/`：Director Router 与 Stateful Grilling 为默认主流程；其他模式、证据、领域和交接细节按需加载。
- `assets/templates/`：六个核心蓝图和条件模块模板。
- `evals/`：触发、多轮行为和质量评测材料。
- `scripts/`：安全安装、确定性验证与发布打包。
- `manifest.json`：2.2.0 安装包内容与 SHA-256 完整性记录。

## 默认蓝图位置

- 代码仓库：`docs/product-blueprint/`
- 非代码目录：`product-blueprint/<project-slug>/`

六个核心文件是 Index、Project State、Product、Experience、System、Build & Acceptance；只在确有需要时增加现状审计、视觉探索、平台约束、研究证据、数据/API、安全合规、迁移、内容文案、领域语言、利益相关者问卷或证据原型模块。

## 验证和发布

```text
python -X utf8 vibe-product-director/scripts/validate_release.py --skill-dir vibe-product-director
python -X utf8 vibe-product-director/scripts/build_release.py --skill-dir vibe-product-director --output-dir .
```

构建脚本使用严格白名单，不会把工作区缓存、报告或临时文件打入 ZIP。
