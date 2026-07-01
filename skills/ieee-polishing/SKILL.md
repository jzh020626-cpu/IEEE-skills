---
name: ieee-polishing
description: >-
  Polish, restructure, or translate academic prose into IEEE Transactions-style English for robotics, automation, control, communications, and industrial informatics papers. Use for abstracts, introductions, related work, methods, experiments, discussions, conclusions, titles, and LaTeX layout fixes.
---

# IEEE Transactions Polishing Router

## Workflow

- Preserve technical meaning, equations, variables, and claim strength.
- Use IEEE style: concise technical prose, numbered-citation awareness, contribution clarity, double-column economy, and evidence-calibrated claims.
- Route T-ASE/TII/TAC/TCST-specific requests through `manifest.yaml` journal fragments.

## Resources

- If `manifest.yaml` exists, load only the fragments needed for the requested section, paper type, language, or venue.
- Read `../_ieee_shared/core/ieee-transactions-contract.md` for shared IEEE Transactions constraints when producing manuscript-facing output.
- Keep outputs source-grounded: do not invent citations, metrics, theorem guarantees, hardware details, or experimental results.
