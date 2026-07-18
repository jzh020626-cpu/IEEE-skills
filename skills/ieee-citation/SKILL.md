---
name: ieee-citation
description: >-
  Add IEEE Transactions-style citations to manuscript text by segmenting claims, searching IEEE-first archival sources, ranking support strength, and exporting ENW/RIS/Zotero RDF. Use for T-ASE, TII, T-RO/RA-L, TAC, TCST, TIE, TWC, TCOM, IoT-J, and related robotics, automation, control, and communications citation tasks.
---

# IEEE Citation Router

Use the static/dynamic routing in `manifest.yaml`.

## Routing protocol

1. Read `manifest.yaml` and all files under `always_load`.
2. Confirm the target venue, date boundary, source scope, and output format. Use the manuscript's language for notes, but search with precise English technical terms when useful.
3. Segment the text into atomic, citable claims; group only claims that need the same evidence.
4. Search and grade support conservatively. A topical title is not enough: inspect an abstract, publisher record, or full text when accessible.
5. Prefer the version of record and archival engineering sources. Use conference papers when they are the original or most relevant evidence and label their status.
6. Suggest IEEE numeric citation positions without inventing final reference numbers. Let the manuscript's citation manager assign ordering.
7. Export one requested reference-manager format by default. Use `scripts/ieee_citation.py` when executing the segmented search/export workflow.
8. For more than about ten segments, load `references/script-usage.md` and use the batched strategy.

## Red lines

- Never present a metadata-only candidate as verified claim support.
- Never fabricate DOI, author order, venue, year, pages, abstract content, citation number, or support strength.
- Do not force an IEEE-only bibliography when the best primary evidence is from another authoritative archival venue.
- Use `ieee-ref-verifier` for a field-by-field bibliography audit and `ieee-academic-search` for broader discovery or citation-impact analysis.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.

## Script

Run `scripts/ieee_citation.py --help` for export options. Use `--scope tase|tii|tac|tcst|tro|ral|tie|twc|tcom|iotj|robotics|control|communications|industrial|ieee|all` to tune journal filtering.
