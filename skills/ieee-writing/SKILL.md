---
name: ieee-writing
description: >-
  Draft, restructure, or plan IEEE Transactions manuscript sections and initial-submission materials from author-provided claims, results, figures, notes, or Chinese drafts. Use for titles, abstracts, introductions, related work, methods, experiments/results, discussions, conclusions, T-ASE Note to Practitioners, full argument maps, initial cover letters, title pages, author/declaration text, conference-version disclosure, reviewer suggestions, graphical-abstract routing, or complete first-submission packages in robotics, automation, control, communications, and industrial informatics.
---

# IEEE Transactions Writing Router

Use the axes and paths in `manifest.yaml`; do not load every fragment.

## Routing protocol

1. Read `manifest.yaml` and all `always_load` paths.
2. Detect and briefly state `task`, `paper_type`, `section`, `language`, and `venue`.
3. Use `task=manuscript` for manuscript argument/sections. Use `task=submission-package` for materials prepared before the first editorial decision. Post-decision correspondence belongs to `ieee-response`.
4. Load only the selected fragments. Skip section fragments for a pure submission-package task.
5. For manuscript work, follow the core workflow: one-sentence argument, terminology ledger, section architecture, paragraph jobs, confirmation gate when ambiguity is material, evidence-outward drafting, claim calibration, flow check, and targeted revision.
6. For submission packages, load `static/fragments/task/submission-package.md` and `references/submission-package.md`, verify the named journal's current instructions, build a deliverable matrix, and draft only required items.
7. Use visible placeholders or `AUTHOR_INPUT_NEEDED` when facts are absent.

## IEEE boundaries

- Use a problem-gap-method-evidence-contribution structure and numeric-citation awareness.
- The exact journal's current Information for Authors overrides generic IEEE guidance.
- T-ASE Note to Practitioners is distinct from the abstract and is placed according to current T-ASE instructions.
- For control papers, expose assumptions, theorem/proof logic, stability/convergence, robustness, and boundaries when supported.
- For robotics/communications papers, expose system/scenario constraints, baselines, ablations, failure cases, latency/throughput/reliability, and reproducibility as applicable.
- Never invent results, equations, citations, novelty, author metadata, ORCIDs, funding, ethics, repositories, permissions, reviewer identities, or conference-extension differences.
- Route figures/graphical abstracts to `ieee-figure`, reproducibility packages to `ieee-data`, and simulated review to `ieee-reviewer`.
- Read `../ieee-shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
- For a full manuscript or multi-round revision, load `../ieee-shared/core/consistency-sweep.md` and reconcile numbers, terminology, assumptions, scenarios, units, and claims before delivery.
