---
name: ieee-writing
description: >-
  Draft, restructure, or plan IEEE Transactions manuscript sections from author-provided claims, results, figures, notes, or Chinese drafts. Use for abstracts, introductions, related work, method, experiments, discussion, conclusion, title, T-ASE Note to Practitioners, or full manuscript argument in robotics, automation, control, communications, and industrial informatics.
---

# IEEE Transactions Writing Router

## Workflow

- Use a problem-gap-method-evidence-contribution structure, not broad-audience editorial storytelling.
- For T-ASE front matter, include a Note to Practitioners section when requested or when building a full submission package.
- For control papers, include assumptions, theorem/proof, stability/convergence, and robustness checks when supported by the source.
- For robotics/communications papers, include system model, scenario, constraints, latency/throughput/reliability, baselines, ablations, and reproducibility details.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
