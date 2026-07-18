# Reviewer workflow

## Default execution order

1. Identify the input package.
   - Determine whether the user supplied a full manuscript, abstract-only draft, selected sections, figures, notes, or a pre-submission concept summary.
2. Build a manuscript fact base.
   - Extract the central claim, key evidence, stated significance, implied audience, and visible limitations.
3. Check assessment readiness.
   - Mark what can be assessed versus what remains missing.
   - If evidence is incomplete, preserve momentum but label uncertainty instead of blocking unless the gap is total.
4. Review the manuscript across the source-grounded axes.
   - Apply scope, novelty/advancement, technical validity, experimental evidence, reproducibility, literature, clarity, and ethics/compliance.
   - Load only the matching section of `domain-specific-review-gates.md`.
5. Generate `3` reviewer reports with different emphasis.
   - Use the same fact base for all three reports.
   - Do not invent different reviewer identities or hidden information.
6. Generate a cross-review synthesis.
   - Summarize consensus, points of emphasis divergence, and the most decision-relevant technical and significance risks.
7. Run final QA.
   - Check groundedness, consistency, coverage, and non-invention.

## Input handling

- Acceptable inputs include:
  - manuscript draft
  - abstract or summary paragraph
  - introduction, results, discussion, or methods excerpts
  - figure legends or selected figures
  - author notes describing the claimed contribution
- If the input is thin, the skill should still provide a bounded review, but it must clearly state the assessment boundary.

## Fact-base extraction checklist

- Extract these items before writing the reports:
  - `manuscript type or apparent submission posture`
  - `main claim`
  - `key evidence presented`
  - `claimed advancement and venue fit`
  - `domain and article type`
  - `visible technical gaps`
  - `experimental/reproducibility gaps`
  - `clarity or compliance issues`

## Cross-review generation rule

- The cross-review synthesis should consolidate, not average away, reviewer differences.
- It must separate:
  - shared strengths
  - shared technical concerns
  - differences in significance weighting
  - differences in readership/readability judgment

## Failure-safe behaviour

- When evidence is absent, say the case is not yet established from the supplied material.
- When advancement is unclear, distinguish potential engineering value from demonstrated contribution.
- When clarity is weak, identify the evaluation barrier instead of rewriting unless asked.
