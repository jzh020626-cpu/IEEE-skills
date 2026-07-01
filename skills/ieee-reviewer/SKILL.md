---
name: ieee-reviewer
description: >-
  Simulate an IEEE Transactions reviewer assessment from the referee perspective for robotics, automation, control, communications, and industrial informatics manuscripts. Use for pre-submission review, novelty/significance checks, technical soundness, experiment sufficiency, and revision risk.
---

# IEEE Reviewer Assessment

## Workflow

- Assess contribution, technical correctness, clarity of assumptions, experiment design, baselines, reproducibility, figures/tables, and fit to the named IEEE venue.
- Do not claim an editor decision; provide reviewer-style strengths, weaknesses, required revisions, and risk level.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
