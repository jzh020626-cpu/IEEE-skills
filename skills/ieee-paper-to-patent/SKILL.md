---
name: ieee-paper-to-patent
description: >-
  Convert engineering papers, theses, technical reports, source code, figures, or research manuscripts into evidence-grounded Chinese invention patent drafts. Use when extracting patentable technical contributions from robotics, control, communication, algorithm, or system papers.
---

# IEEE Paper To Patent

## Workflow

- Preserve evidence links from the source paper to each claim element.
- Separate method, apparatus/system, and software/process claims when appropriate.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
