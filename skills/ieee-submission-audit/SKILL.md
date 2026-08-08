---
name: ieee-submission-audit
description: >-
  Run a strict IEEE Transactions pre-submission audit for robotics, automation, control, communications, and industrial informatics manuscripts. Use before journal submission or resubmission, especially for T-ASE, TII, TAC, TCST, TCNS, T-RO/RA-L, and related IEEE Transactions targets, to check IEEEtran format, Abstract/Index Terms, numeric references, page limits, figures, reproducibility, Note to Practitioners, conference-extension value, and venue-specific hard constraints.
---

# IEEE Submission Audit

## Trigger

Use this skill when the user asks for:

- strict IEEE / IEEE Transactions hardening
- pre-submission, final submission, or resubmission audit
- T-ASE, TII, TAC, TCST, TCNS, T-RO, RA-L, TIE, TWC, TCOM, IoT-J readiness
- IEEEtran, page-limit, figure/table, reference, Note to Practitioners, or supplementary-material checks

## Workflow

1. Identify the target venue, article type, stage, and official rules checked. If missing, use `generic-ieee` and mark venue-specific items as manual.
2. Verify the current journal Information for Authors when online access is available; record URL and date.
3. Load `references/strict-ieee-checklist.md`, `../ieee-shared/core/ieee-transactions-contract.md`, and `../ieee-shared/core/consistency-sweep.md`. When human/HRI, autonomous deployment, spectrum, cybersecurity, sensitive traces, safety-critical systems, or dual-use issues apply, also load `../ieee-shared/core/research-compliance.md`; unknown administrative facts are `AUTHOR_INPUT_NEEDED`.
4. If the user supplied manuscript text/LaTeX, run `scripts/ieee_submission_audit.py` with the closest `--venue` and `--paper-type`. Use `--page-limit` when a current authoritative limit has been verified.
5. Report only evidence-backed results. If a check cannot be confirmed from the provided material, mark it `manual`, not pass.
6. Return a gate: `Go`, `Conditional Go`, or `No-Go`.

## Audit Categories

- IEEE template and front matter: IEEEtran/double-column, Abstract, Index Terms, abstract restrictions.
- Venue hard constraints: T-ASE NtP/Abstract/order, TII page/anonymity/email rules, TAC/TCST/TCNS page/type rules, and ORCID for all authors.
- Argument and evidence: problem definition, novelty, assumptions, theorem/proof, baselines, ablations, complexity, stability/convergence/reliability, limitations.
- Citations: numeric IEEE style, first-appearance ordering, archival IEEE-first support, conference-extension disclosure.
- Figures and tables: one claim per figure, final-width readability, captions, subfigure labels, vector/raster export format, black-and-white robustness.
- Reproducibility: code/data/logs/seeds/configs/weights/ROS bags/hardware/simulation settings and exact reproduction commands.

## Output

Keep the response concise and gate-oriented:

```text
GATE:
- Go / Conditional Go / No-Go

BLOCKERS:
- [blocking item or None]

FIX BEFORE SUBMISSION:
- [actionable item]

MANUAL CONFIRMATION:
- [item that requires compiled PDF, submission-system view, or author confirmation]
```

Do not rewrite the manuscript unless the user asks. For audit tasks, findings and gates come first.
