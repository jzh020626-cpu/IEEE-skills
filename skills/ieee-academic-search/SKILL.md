---
name: ieee-academic-search
description: >-
  Multi-source literature search, citation verification, DOI/arXiv/IEEE Xplore-oriented reference management, and BibTeX/RIS/ENW conversion for robotics, automation, control, communications, and industrial informatics papers. Use when the user asks to search papers, verify citations, build related work, manage references, or find support for IEEE Transactions manuscripts.
---

# IEEE Academic Search

## Workflow

- Prefer archival IEEE Transactions/Letters, major robotics/control/communications venues, and high-quality recent surveys.
- Track DOI, venue, year, contribution type, method family, baselines, metrics, and relevance to the target claim.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
