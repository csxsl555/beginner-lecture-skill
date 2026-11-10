# beginner-lecture

为领域初学者编写深入浅出的中文讲义。**正文各章先给摘要思维导图，每个新专业名词首次出现后立即解释，关键推理不跳步，内容覆盖有依据。**

这是一个 Agent Skill，即供 AI 助手按需读取的一组任务指令。它面向讲义、课程章节和学习材料的编写、改写与检查，不是一个独立运行的应用。

A Chinese-first skill for beginner-friendly learning materials: open each teaching chapter with a summary mind map, explain new terms in place, preserve reasoning steps, and check coverage against a defined scope.

## 它要求 AI 做什么

- **正文各章先给摘要图。** 在每个正文章开头绘制本章思维导图，展示实际讲解的主要内容及分支关系。导读、自测题、答案等辅助部分不加图，章内普通小节也不重复加图。
- **就地解释新名词。** 中文术语、英文名称、缩写、数学符号和代码标识符都要在首次出现后说明含义；解释中新引入的术语也必须说明。
- **补齐理解所需的基础。** 根据读者真正已知的内容安排顺序，不默认“大学生”就懂当前学科。
- **讲清过程。** 从具体问题出发，说明概念、机制、中间推导、完整例子及影响结论的条件。
- **核对遗漏。** 对照指定教材或知识范围检查，不能把出现在目录、公式或代码里的名字当作已经讲清。
- **先修复再交付。** 顺序检查术语、覆盖、跳步、事实与理解题；只要求审稿时才单独交付修改建议。

术语表可以帮助复习，但不能代替首次出现处的解释。同一学习单元中已经解释过的词不机械重复；可独立阅读的新章节会给出简短回顾。

章首图也遵守同样的术语规则：优先使用通俗短句，新术语在图前或节点中就地解释。支持 Mermaid（用文本描述绘图的工具）的 Markdown 使用 `mindmap` 图；不支持时改用可见的层次图。导图概括正文，不替代正文中的详细解释。

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills) 安装。CLI 是命令行工具，即通过输入命令完成操作的程序；当前安装工具需要 Node.js 22.20 或更新版本，具体要求以其官方说明为准。

在目标项目目录运行：

```sh
npx skills add csxsl555/beginner-lecture-skill --skill beginner-lecture
```

按提示选择使用的 AI 助手。该命令默认安装到当前项目；其他安装范围与选项见 [Skills CLI 文档](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)。

仓库名是 `beginner-lecture-skill`，实际调用的技能名是 `beginner-lecture`。也可以直接阅读 [SKILL.md](SKILL.md)，并在支持该格式的助手中加载它。

## 使用

尽量说明主题、已知基础、希望覆盖的范围，以及是否有指定材料。信息已经足够时，技能会直接编写正文。

从一个主题开始：

```text
$beginner-lecture 请给我写一份动态规划入门讲义。
我会基础 Python，但没学过算法。请讲清为什么需要它、每一步怎样推出来，
所有新名词首次出现后立即解释，并用一个完整例子带我走完。
```

根据现有教材编写：

```text
$beginner-lecture 根据我提供的这一章教材写讲义。
读者只会基础代数。保留本章的结论、成立条件、关键推导和重要例外，
不要把必要解释留到“拓展阅读”，最后核对有没有漏讲。
```

检查已经写好的内容：

```text
$beginner-lecture 检查下面的讲义。
重点找突然出现的新术语、推导跳步和只提名字没有解释的内容。
直接修复这些问题，保留其他章节和原有结论；材料不足的地方明确指出。
```

## 讲义示例

| 示例 | 重点 |
| --- | --- |
| [缓存](examples/cache-lesson.md) | 中文与英文名称就地解释；命中率计算；过期与内容变旧的区别 |
| [条件概率](examples/probability-lesson.md) | 为什么比较范围改变；符号的含义；材料不足时不能倒推结论 |
| [二分查找](examples/binary-search-lesson.md) | 新语法说明；逐轮追踪；为什么结束；空列表和重复值 |
| [两章讲义的结构](examples/chapter-structure-lesson.md) | 两章正文各有章首图；导读、自测题、答案没有图 |

这些示例展示解释方式，不是每个学科都必须套用的固定模板。示例中的价格和读取记录为虚构数据，卡片与查找问题使用文中明确给出的条件。

## 内容与验证

主要文件：

```text
SKILL.md
agents/openai.yaml
references/
  explanation-patterns.md
  evaluation-cases.md
examples/
  cache-lesson.md
  probability-lesson.md
  binary-search-lesson.md
  chapter-structure-lesson.md
tests/verify_examples.py
```

使用 Python 3.9 或更新版本，在仓库根目录运行：

```sh
python tests/verify_examples.py
```

检查只使用 Python 标准库，会读取讲义中实际展示的代码，验证二分查找的 1,260 个输入与目标组合、示例运算和内部文件链接。它不会替代术语、推理与教学质量的逐段审查。

修改教学规则时，参考 [行为检查请求](references/evaluation-cases.md) 生成小样，再按相应要求检查。维护约定见 [AGENTS.md](AGENTS.md)。

## 适用边界

“完整”需要明确参照：指定教材、章节或事先界定的知识范围。没有拿到材料时，技能不能声称逐项覆盖了它；没有进行真实学习者试读时，也不能声称已经证明“所有初学者都能懂”。

本仓库包含作者审查过的示例与可运行的一致性检查，尚未提供真实学习者教学效果评测。未来生成的事实、公式与代码仍需要按材料和运行结果核验。

欢迎通过 Issue 或 Pull Request 提供具体改进：指出难懂的段落、读者已知基础，以及缺失的解释或推理步骤。

## 许可证

[MIT](LICENSE)。
