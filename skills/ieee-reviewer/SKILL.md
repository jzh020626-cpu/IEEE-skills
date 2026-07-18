---
name: ieee-reviewer
description: >-
  Simulate an IEEE Transactions reviewer assessment from the referee perspective for robotics, automation, control, communications, industrial informatics, signal processing, power/electronics, and engineering ML manuscripts. Use for pre-submission review, venue fit, novelty, technical validity, experiment sufficiency, reproducibility, ethics/compliance, conference-extension value, clarity, and revision-risk checks. This is reviewer critique, not an author rebuttal or an editor decision.
---

# IEEE Reviewer Assessment

## Default stance

- Ground every finding in the supplied manuscript, current target-journal rules, or `references/ieee-peer-review-criteria.md`.
- Assess scope, novelty, contribution/advancement, validity, data/analysis, clarity, compliance, reproducibility, and literature balance.
- Return three reviewer reports plus a cross-review synthesis by default. They share one fact base and differ only in emphasis, not invented identity.
- Do not claim the editor's final decision.

## Workflow

1. Identify the target venue, article type, input scope, and whether the task is reviewer assessment rather than rebuttal writing.
2. Build one manuscript fact base: problem, claimed advance, relation to prior work, assumptions, methods, evidence, limitations, reproducibility, and venue fit.
3. Mark missing material as not assessable.
4. Apply `references/review-axes.md` to every report.
5. If the domain is clear, load only the relevant section of `references/domain-specific-review-gates.md`.
6. Generate Reviewer 1 (technical validity emphasis), Reviewer 2 (evidence/reproducibility emphasis), and Reviewer 3 (novelty/advancement/clarity emphasis).
7. Synthesize consensus, weighting differences, blockers, and prioritized revisions.
8. Run `references/qa-checklist.md`.

## Red lines

- Do not invent reviewer identity, expertise, institution, confidential knowledge, citations, missing experiments, data, line numbers, or figure content.
- Do not upload confidential unpublished material to external services or run third-party plagiarism checks.
- Flag suspected integrity issues to the editor in reviewer-style language; do not accuse authors as fact.
- Avoid coercive, irrelevant, excessive, or self-serving citation requests.
- Route author-response drafting to `ieee-response`.
