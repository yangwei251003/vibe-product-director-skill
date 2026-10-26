# Experience Blueprint

## 体验原则

| 原则 | 可观察行为 | 禁止模式 |
|---|---|---|
| {{principle}} | {{observable implementation}} | {{anti-pattern}} |

## 信息架构与关键界面

| 界面/状态 | 用户目标 | 主要信息 | 主动作 | 次动作 | 空/错/加载/离线状态 |
|---|---|---|---|---|---|
| {{screen}} | {{goal}} | {{content}} | {{primary}} | {{secondary}} | {{states}} |

## 视觉契约

- 审美词 → 可实现属性：{{translation}}
- 字体：{{families, weights, scale, fallback}}
- 色彩：{{roles, contrast, dark/light behavior}}
- 材质：{{surface, border, elevation, texture}}
- 间距与布局：{{grid, rhythm, density, breakpoints}}
- 组件：{{states, variants, consistency rules}}
- 反 AI 模板检查：{{generic patterns rejected + corrective rules}}

## 交互与动效

| 触发 | 动画/反馈 | 时长/曲线 | 可中断 | 触摸/键盘 | reduced-motion | 低性能降级 |
|---|---|---|---|---|---|---|
| {{trigger}} | {{behavior}} | {{timing}} | {{yes/how}} | {{equivalence}} | {{alternative}} | {{fallback}} |

## 无障碍与适配

{{焦点顺序、语义、对比度、文字缩放、触控目标、键盘、屏幕阅读器、响应式与平台差异。}}

## 体验验收

{{用可观察、可测试的 Given/When/Then 描述关键状态；引用 ACT/DEC/RISK ID。}}

