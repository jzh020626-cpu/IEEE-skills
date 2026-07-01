# Workflow 1: IEEE-First Multi-Source Literature Search

**Purpose:** Search IEEE-first engineering literature, deduplicate, merge, and rank results.

**Uses:** [Dedup Engine](../dedup-engine.md) and [Source Tiers](../source-tiers.md).

## Procedure

1. Analyze the topic into task, method, system, constraint, and metric.
2. Select sources by the IEEE-first routing table. Use official IEEE pages for venue rules, CrossRef/IEEE Xplore for metadata, and OpenAlex/Semantic Scholar for expansion.
3. Search strict venues first when known: T-ASE, TII, TAC, TCST, TCNS, T-RO, RA-L, TIE, TWC, TCOM, IoT-J.
4. Search major conference versions only for historical context or conference-extension checks.
5. Deduplicate by DOI, title, and venue.
6. Rank by relevance to the claim, venue fit, recency, and evidence type; citation count is only a tie-breaker.
7. Present results with DOI, venue, year, contribution type, method family, baselines, metrics, and why the paper is relevant.

## Output Format

```text
Title:
Authors:
Venue:
Year:
DOI:
IEEE scope:
Why relevant:
Support type: [direct / partial / background / metadata-only]
```

## Error Modes

- MCP tool unavailable: report specific failure and continue with remaining tools.
- No IEEE-first results: broaden IEEE venue names and abbreviations before asking whether to include non-IEEE sources.
- All sources empty: ask for narrower task/method/system terms or a seed paper.
