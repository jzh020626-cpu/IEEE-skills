# IEEE Transactions Skills 中文说明

[English README](README.md)

IEEE Transactions Skills 是一套面向 Codex 的学术写作与投稿辅助技能集合，主要服务于机器人、自动化、控制、通信、工业信息学和网络化智能系统方向的博士研究工作。它的目标不是泛泛的科学写作，也不是生命科学或 Nature 风格写作，而是面向 IEEE Transactions 系列期刊的论文准备、润色、引用、图表、复现和投稿前审查。

这套 skills 主要覆盖 T-ASE、TII、T-RO、RA-L、TAC、TCST、TIE、TWC、TCOM、IoT-J 等 IEEE 期刊或相近工程类期刊。核心关注点包括 IEEEtran 结构、编号引用、双栏可读性、可复现实验、baseline、ablation、稳定性或收敛性论证、通信约束、延迟、鲁棒性，以及分刊投稿 checklist。

## 仓库内容

```text
.
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
|-- scripts/
|   |-- update-codex-skills.sh
|   `-- check-nature-upstream.sh
`-- skills/
    |-- _ieee_shared/
    |-- ieee-writing/
    |-- ieee-polishing/
    |-- ieee-citation/
    |-- ieee-figure/
    |-- ieee-data/
    |-- ieee-response/
    |-- ieee-reviewer/
    |-- ieee-submission-audit/
    |-- ieee-academic-search/
    |-- ieee-literature-pipeline/
    |-- ieee-reader/
    |-- ieee-downloader/
    |-- ieee-paper2ppt/
    |-- ieee-paper-to-patent/
    `-- ieee-proposal-writer/
```

每个 skill 基本遵循 Codex skill 的标准结构：

- `SKILL.md`：触发说明与核心操作规则。
- `manifest.yaml`：skill 元数据，部分 skill 提供。
- `static/`：skill 执行时会加载的固定片段。
- `references/`：更细的写作规则、checklist、示例或来源说明。
- `scripts/`：该 skill 使用的本地辅助脚本。
- `assets/`：必要时提供的示例图、演示资源或可复用素材。

以下内容不应提交到仓库：`.upstream/`、`__pycache__/`、`.pytest_cache/`、`.env`、虚拟环境、运行日志、浏览器会话、私有凭据和下载的论文 PDF。

## 设计目标

本仓库遵循 IEEE-first 原则：

- 使用 IEEE 编号引用格式，例如 `[1]`、`[2]`，不默认使用 author-year 格式。
- 引用优先面向 IEEE 档案论文和工程类权威来源。
- 图、表、caption 和正文密度都要考虑 IEEE 双栏排版约束。
- 技术 novelty 应落在系统、算法、控制、通信或工程实现贡献上，而不是生命科学发现式表述。
- 要求明确的问题定义、assumptions、baseline、ablation、复现材料和 limitation。
- 支持 T-ASE 的 `Note to Practitioners` 撰写与审查。
- 支持控制类论文的 assumptions、theorem/proof、stability、convergence、feasibility 和 conference-extension value 检查。
- 支持机器人和通信类论文的硬件/仿真设置、任务场景、延迟、吞吐、丢包、鲁棒性和统计显著性检查。

## 安装到 Codex

进入仓库目录后运行：

```bash
cd /path/to/IEEE-skills
scripts/update-codex-skills.sh
scripts/update-codex-skills.sh --check
```

默认安装脚本只会同步以下目录：

- `skills/ieee-*`
- `skills/_ieee_shared`

目标位置是：

```text
~/.codex/skills
```

安装脚本不会删除或覆盖其他无关 skills。它还会写入一个本地安装清单：

```text
~/.codex/skills/.ieee-trans-skills-install.txt
```

常用参数：

```bash
scripts/update-codex-skills.sh --check
scripts/update-codex-skills.sh --dest /tmp/skills-check
scripts/update-codex-skills.sh --pull
scripts/update-codex-skills.sh --prune
```

`--prune` 只会删除此前由本安装脚本管理、但当前仓库不再提供的目录，不会清理其他个人 skills。

## Skill 索引

| Skill | 主要用途 |
|---|---|
| [`ieee-writing`](skills/ieee-writing/README.md) | 根据 claims、实验结果、图表、笔记或中文草稿，起草或重构 IEEE Transactions 论文段落和章节。 |
| [`ieee-polishing`](skills/ieee-polishing/README.md) | 将英文或中文草稿润色、翻译并收紧为 IEEE Transactions 风格英文。 |
| [`ieee-citation`](skills/ieee-citation/README.md) | 添加 IEEE 编号引用，检查 claim 支撑强度，并处理 RIS、ENW、BibTeX 等引用工作流。 |
| [`ieee-figure`](skills/ieee-figure/README.md) | 创建、修改或审查 IEEE 单栏/双栏论文图。 |
| [`ieee-data`](skills/ieee-data/README.md) | 准备复现包、代码/数据可用性说明、随机种子、日志、参数和硬件/仿真元数据。 |
| [`ieee-response`](skills/ieee-response/README.md) | 起草或审查 IEEE 期刊逐点审稿回复。 |
| [`ieee-reviewer`](skills/ieee-reviewer/README.md) | 从 IEEE Transactions 审稿人视角模拟预审。 |
| [`ieee-submission-audit`](skills/ieee-submission-audit/SKILL.md) | 严格投稿前审查，覆盖 IEEEtran、页数、图表、参考文献、NtP、复现和分刊硬约束。 |
| [`ieee-academic-search`](skills/ieee-academic-search/README.md) | 多源文献搜索、引用核查、DOI/arXiv/IEEE 取向的参考文献管理，以及可选 MCP dispatch。 |
| [`ieee-literature-pipeline`](skills/ieee-literature-pipeline/README.md) | 面向工程论文的自动化文献发现、打分、聚类和精读流程。 |
| [`ieee-reader`](skills/ieee-reader/README.md) | 为 IEEE 或工程论文构建图表感知的中英双语阅读材料。 |
| [`ieee-downloader`](skills/ieee-downloader/README.md) | 配置合法的机构访问或开放获取论文下载，并整理授权 PDF。 |
| [`ieee-paper2ppt`](skills/ieee-paper2ppt/README.md) | 从机器人、自动化、控制、通信或工业信息学论文构建 IEEE 风格中文汇报 PPT。 |
| [`ieee-paper-to-patent`](skills/ieee-paper-to-patent/README.md) | 将工程论文、学位论文、技术报告、源码或图表转换为中文发明专利草案。 |
| [`ieee-proposal-writer`](skills/ieee-proposal-writer/README.md) | 运行 proposal-first 的 IEEE Transactions 论文构思与写作流程。 |

## 常见触发方式

安装后，Codex 可以通过自然语言或显式 skill 名触发这些功能。

示例：

```text
Use ieee-writing to rewrite my T-ASE introduction.
Use ieee-polishing to polish this Chinese draft into IEEE Transactions English.
Use ieee-citation to add numbered IEEE references for these claims.
Use ieee-figure to audit whether this figure works in a double-column paper.
Use ieee-data to prepare a reproducibility package checklist.
Use ieee-response to draft replies to TII reviewer comments.
Use ieee-submission-audit to run a strict pre-submission check for T-ASE.
```

如果希望触发更稳定，可以显式写 skill 名：

```text
$ieee-submission-audit
```

## 严格 IEEE 投稿审查

`ieee-submission-audit` 是最终投稿前的 strict mode，适合论文接近投稿或返修提交时使用。

它会检查：

- IEEEtran 兼容性和 front matter 结构。
- 标题、摘要、关键词和贡献陈述。
- T-ASE `Note to Practitioners` 是否与 abstract 区分清楚。
- 编号引用格式和参考文献完整性。
- 图在 IEEE 单栏/双栏条件下的可读性。
- 表格密度、caption 自足性和交叉引用卫生。
- 页数预算、appendix 放置和 supplementary material 边界。
- baselines、ablations、统计证据和鲁棒性证据。
- 控制类论文的 assumptions、theorems、proofs、stability 和 convergence。
- 机器人和自动化实验设置：任务场景、硬件/仿真、安全边界、延迟、吞吐和可靠性。
- 复现包准备情况：代码、数据集、随机种子、日志、模型权重、必要时的 ROS bag、参数和运行命令。

## 可选依赖

大多数 skills 是提示词/指令型 skill，不需要额外安装包。少数辅助脚本有可选依赖：

```bash
python -m pip install -r skills/ieee-paper-to-patent/requirements.txt
python -m pip install -r skills/ieee-academic-search/mcp-server/requirements.txt
```

只有在使用对应脚本时才需要安装。

## IEEE academic search MCP

`ieee-academic-search` 包含一个可选 MCP server：

```text
skills/ieee-academic-search/mcp-server
```

默认行为是 IEEE-first 且低风险：

- CrossRef/OpenAlex 风格 DOI 元数据。
- arXiv 预印本发现。
- 可用时优先使用 IEEE Xplore 或官方出版商页面。
- Scopus 和 ScienceDirect 只在显式配置且用户要求时使用。

可选 Elsevier/Scopus 凭据不会保存在本仓库。请通过环境变量或 `pybliometrics` 本地配置提供：

```bash
export ELSEVIER_API_KEY=...
export SCOPUS_API_KEY=...
export IEEE_ACADEMIC_SEARCH_LIVE_ELSEVIER=1
```

只有在具备凭据和 API quota 时才应运行 live API 测试。

## 上游同步

本仓库可以跟踪上游 `nature-skills` checkout 中可复用的架构变化，同时保持 IEEE 行为不变。

脚本：

```bash
scripts/check-nature-upstream.sh
```

该脚本会比较上游 `nature-skills` HEAD 和最近一次完成 IEEE 适配的 commit。当发现上游更新时，它会创建 pending 状态，但不会自动标记为已完成。只有在人或 Codex 自动化把可复用结构迁移为 IEEE 形式并通过验证后，才应标记：

```bash
scripts/check-nature-upstream.sh --mark <commit>
```

重要边界：

- 上游 `nature-*` 内容只能作为架构 diff 的来源。
- 主动 skill 行为必须保持为 `ieee-*`。
- 不要把生命科学、临床、基因组学、Nature Portfolio、Nat Commun、CNS 或 Cell Press 假设复制到默认 IEEE 指令中。

## 验证 checklist

发布或安装更新版本前建议运行：

```bash
scripts/update-codex-skills.sh --check
```

推荐的额外检查：

```bash
rg -n "__pycache__|\\.pytest_cache|\\.upstream" .
rg -i "Nature|Nat Commun|CNS|Cell Press|biolog|clinical|genomic|single-cell" skills README.md README.zh-CN.md
rg -i "IEEE|T-ASE|TII|Transactions|Note to Practitioners|double-column|baselines|ablation|stability|latency" skills README.md README.zh-CN.md
```

部分 legacy assets 或来源说明可能会提到非 IEEE 起源；它们不应作为 IEEE 投稿的默认写作行为、主动路由或推荐示例出现。

## 仓库维护建议

建议遵循以下发布习惯：

- 将 source skills、references、scripts 和必要的小型可复用 assets 保留在 Git 中。
- 不要提交运行缓存、本地凭据、下载的 PDF、浏览器会话、`.env`、虚拟环境或本地 `.upstream` 状态。
- 大型 legacy demo assets 只有在 skill 或测试仍依赖时才保留；后续可逐步替换为更小、更符合 IEEE 场景的示例。
- 尽量用聚焦的 commit 分离 README/文档变更和 skill 行为变更。

## License

见 [`LICENSE`](LICENSE)。
