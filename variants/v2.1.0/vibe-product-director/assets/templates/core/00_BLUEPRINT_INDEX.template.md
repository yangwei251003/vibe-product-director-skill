# {{PRODUCT_NAME}} · Blueprint Index

> 状态：{{Draft|In Review|Ready}}  
> 最后更新：{{YYYY-MM-DD}}  
> 当前工作边界：{{decision cluster|research|evidence prototype|handoff|development}}  
> 当前 frontier：{{NEXT_DECISION_OR_HANDOFF}}

## 阅读入口

- 新开发 Agent：本索引 → `BUILD_AND_ACCEPTANCE.md` → 首切片引用的 Product / Experience / System / Decisions 章节。
- 产品决定：`PROJECT_STATE.md` 的 Decision Map → 对应唯一权威来源。
- 恢复工作：先读当前工作边界、frontier、Fog、Blocking 与最近变更，不依赖原始聊天。

## 权威来源

| 主题 | 唯一权威文档 | 状态 | 依赖/备注 |
|---|---|---|---|
| 项目事实、决定、未决项 | `PROJECT_STATE.md` | {{status}} | — |
| 产品范围与旅程 | `PRODUCT_BLUEPRINT.md` | {{status}} | {{deps}} |
| 体验与视觉契约 | `EXPERIENCE_BLUEPRINT.md` | {{status}} | {{deps}} |
| 系统、数据与集成 | `SYSTEM_BLUEPRINT.md` | {{status}} | {{deps}} |
| 构建切片与验收 | `BUILD_AND_ACCEPTANCE.md` | {{status}} | {{deps}} |

## 条件模块

仅列出已触发并实际创建的模块。未创建不代表遗漏。

| 模块 | 触发原因 | 状态 | 权威范围 |
|---|---|---|---|
| {{FILE}} | {{WHY}} | {{status}} | {{scope}} |

## 版本迁移

{{若从 v1 的 00_INDEX.md 迁移：列出读取过的旧文档、被继承/废弃的结论，并声明本索引指向的新权威来源。否则删除本节。}}

## Ready 摘要

- Blocking：{{none_or_items}}
- Conditional：{{items}}
- Later：{{items}}
- Human Gates：{{owner + returned evidence + blocks}}
- 首个纵向切片：{{slice}}
- 三重审查：Skeptic {{result}} / Simplifier {{result}} / Blind-Handoff {{result}}
