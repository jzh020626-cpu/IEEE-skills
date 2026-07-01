# Workflow

Run these steps for any IEEE citation job. For more than about 10 claim segments, switch to the batched strategy in `references/script-usage.md`.

## 1. Segment the text

- Split long text into citable segments. Prefer paragraph boundaries, then sentence boundaries.
- Keep one citable idea per segment when possible.
- Preserve original order and stable IDs such as `S001`, `S002`, `S003`.
- Skip purely connective sentences unless the user asks to cite every sentence.

## 2. Parse each segment

For each segment:

- Extract the core claim in one sentence.
- Identify claim type: `method`, `theory`, `system`, `experiment`, `benchmark`, `survey-context`, `definition`, or `engineering-background`.
- Identify task, system model, assumptions, variables, performance metric, platform, and boundary conditions.
- Convert the claim into 2-4 English search queries: precise method query, synonym query, venue-target query, and broader background query.

## 3. Search candidate papers

Prefer `scripts/ieee_citation.py` when internet access is available:

```bash
python scripts/ieee_citation.py \
  manuscript.txt \
  --scope tase \
  --output ieee_references.enw \
  --report ieee_citation_report.md
```

Use strict scopes (`tase`, `tii`, `tac`, `tcst`, `tro`, `ral`, `tie`, `twc`, `tcom`, `iotj`) when the target journal is known. Use `all` only for early discovery across the IEEE-first set.

## 4. Evaluate support

Use a conservative scale:

- `strong support`: same task/system/claim and direct evidence.
- `partial support`: related system or narrower condition.
- `background support`: field context only.
- `contradictory/limiting`: conflicts with or narrows the claim.
- `metadata-only candidate`: bibliographic fields suggest relevance but abstract/full text has not been checked.

Never cite a `metadata-only candidate` as support without checking the abstract or publisher page.

## 5. Export references

Default export is `ieee_references.enw`. Use RIS or Zotero RDF only when requested. Do not invent missing DOI, volume, issue, page, article number, or author fields.

## 6. Report results

Unless the user asks otherwise, return:

```text
检索范围
- [target venue/scope and search date]

分段引用对应关系
S001: [source segment]
  - [Author, year, title, journal, DOI]
  - 支撑等级: [strong/partial/background/limiting/metadata-only]
  - 插入建议: IEEE numeric citation placeholder [n] after the supported claim

导出文件
- [absolute path to .enw/.ris/.rdf]

风险和缺口
- [missing full-text check, no direct IEEE support, contradictory evidence, etc.]
```

If no suitable IEEE-first paper exists, say so directly and ask before broadening to non-IEEE sources.
