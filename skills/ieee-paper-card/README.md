# `ieee-paper-card`

对单篇机器人、控制、通信网络、工业信息学或相邻工程论文进行有来源约束的深度精读，输出固定 01–16 节 Paper Card。它强调问题—方法—证据链、公式与假设、实验边界、批判性分析和可检验研究想法，不把摘要翻译冒充精读。

支持 PDF、DOI、arXiv、出版社页面、粘贴文本或 `ieee-reader` source map。按论文主贡献选择 `algorithm`、`system`、`theory`、`benchmark`、`application` 或 `review` 视角；来源不足时明确标记 `Not assessable`。

示例：

```text
使用 ieee-paper-card 精读这篇机器人论文，核对每个方法模块、假设、消融实验和结论边界，并提出只能作为假设的后续研究方向。
```

生成后必须运行自带的来源定位与卡片审计脚本。需要全文双语材料用 `ieee-reader`；需要正式审稿用 `ieee-reviewer`；需要外部新颖性检索用 `ieee-academic-search`。
