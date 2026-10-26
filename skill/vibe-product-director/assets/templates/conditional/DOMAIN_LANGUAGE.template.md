# Domain Language

> 仅在多角色、多上下文或大量术语重载使 `SYSTEM_BLUEPRINT.md` 难读时创建。这里是详细词表权威；System 只保留关键词和链接。

## Bounded Contexts

| Context | 责任边界 | 共享/不共享的概念 | 上下游关系 |
|---|---|---|---|
| {{context}} | {{responsibility}} | {{terms}} | {{relationship}} |

## Canonical Terms

| Preferred term | 通俗含义 | 类型 | Context | Avoid aliases | 正例 | 反例/边界 | 代码/接口映射 |
|---|---|---|---|---|---|---|---|
| {{term}} | {{meaning}} | {{Actor/Role/Entity/Value/Policy/Event}} | {{context}} | {{aliases}} | {{scenario}} | {{non-example}} | {{mapping or conflict}} |

## 场景压力测试

| 场景 | 使用的术语 | 是否歧义 | 发现的冲突 | 决定/修正 |
|---|---|---|---|---|
| {{real scenario}} | {{terms}} | {{yes/no}} | {{product/code/data mismatch}} | {{DEC/section}} |
