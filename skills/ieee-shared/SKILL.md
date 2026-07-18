---
name: ieee-shared
description: Internal shared-reference support package for installed IEEE Transactions skills. Do not invoke it as a standalone user workflow. Load only the exact shared core or journal-format file requested by another ieee-* skill.
---

# IEEE Shared References

Use this package only as a dependency of another IEEE skill.

- Load the exact referenced file; do not preload the whole package.
- Treat `core/` and `journal-formats/` as shared definitions, not standalone workflows.
- Use `core/ieee-transactions-contract.md` for suite-wide IEEE constraints.
- Use `journal-formats/ieee-transactions.md` for stable generic format facts, then verify the named journal's current Information for Authors when exact limits matter.
- Return to the requesting skill for task logic, output format, and final QA.
