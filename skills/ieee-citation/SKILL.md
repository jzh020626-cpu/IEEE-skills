---
name: ieee-citation
description: >-
  Add IEEE Transactions-style citations to manuscript text by segmenting claims, searching IEEE-first archival sources, ranking support strength, and exporting ENW/RIS/Zotero RDF. Use for T-ASE, TII, T-RO/RA-L, TAC, TCST, TIE, TWC, TCOM, IoT-J, and related robotics, automation, control, and communications citation tasks.
---

# IEEE Citation Router

## Workflow

- Use numbered citation logic: suggest where `[n]`-style citations belong without fabricating reference numbers.
- Default scope is IEEE-first archival sources; broaden to non-IEEE or conference coverage only when the user explicitly asks or strict IEEE coverage is unavailable.
- Use `scripts/ieee_citation.py` for segmented search/export when the user asks to generate references or files.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.

## Script

Run `scripts/ieee_citation.py --help` for export options. Use `--scope tase|tii|tac|tcst|tro|ral|tie|twc|tcom|iotj|robotics|control|communications|industrial|ieee|all` to tune journal filtering.
