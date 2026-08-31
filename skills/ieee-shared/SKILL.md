---
name: ieee-shared
description: Internal shared-reference support package for installed IEEE Transactions skills. Do not invoke it as a standalone user workflow. Load only the exact shared core or journal-format file requested by another ieee-* skill.
---

# IEEE Shared References

Use this package only as a dependency of another IEEE skill.

- Load the exact referenced file; do not preload the whole package.
- Treat `core/` and `journal-formats/` as shared definitions, not standalone workflows.
- Use `core/ieee-transactions-contract.md` for suite-wide IEEE constraints.
- Use `core/claim-centered-writing.md` for the evidence-calibrated press-release
  principle: organize the main manuscript around its strongest supported value,
  separate the main argument from the complete supplementary record, and remove
  repeated self-defense without softening independent review or statistical findings.
- Use `core/main-text-discipline.md` when allocating core results, qualifications,
  robustness checks, failure cases, configuration detail, and statistics across
  the main text, captions, Supplementary Material, and artifact repositories.
- Use `core/discussion-argument-language.md` when a Discussion needs a clear
  finding-to-interpretation progression, evidence-calibrated modality,
  claim-specific limitations, or uncertainty-resolving future work.
- Use `core/engineering-evidence-chain.md` when Abstract, Introduction,
  Results/Experiments, Discussion, and Conclusion must follow one paper-type-
  appropriate claim–evidence route.
- Use `core/consistency-sweep.md` for cross-section terminology, numeric, assumption, and claim consistency after iterative edits.
- Use `core/research-compliance.md` only when human subjects, autonomous deployment, spectrum use, cybersecurity, sensitive traces, safety-critical systems, or dual-use concerns apply.
- Use `journal-formats/ieee-transactions.md` for stable generic format facts, then verify the named journal's current Information for Authors when exact limits matter.
- Return to the requesting skill for task logic, output format, and final QA.
