# QA checklist

## Grounding checks

- Every substantive evaluation should be traceable to either:
  - `references/ieee-peer-review-criteria.md`,
  - the named journal's current reviewer/author instructions, or
  - manuscript facts explicitly supplied by the user.
- No reviewer persona detail should appear beyond allowed `emphasis` labels.
- Domain gates are prompts only; no failing should be asserted when the supplied material does not show it.

## Coverage checks

- Confirm all three reviewer reports exist.
- Confirm the three reports differ in `emphasis` only.
- Confirm each reviewer still addresses all core axes, even if briefly.
- Confirm a `Cross-review synthesis` section exists.
- Confirm a `Risk / unsupported claims` section exists.

## Boundary checks

- Confirm the output stays in reviewer-assessment mode, not author-response mode.
- Confirm the output does not claim a final editorial decision.
- Confirm the output does not claim an editor decision.
- Confirm any actual confidential-review case was handled under the journal's AI/confidentiality policy.

## Non-invention checks

- No invented reviewer identity, specialty, institution, or selection history.
- No invented experiments, controls, analyses, line numbers, citations, prior-work details, or figure-specific content absent from the input.
- If evidence is partial, mark `AUTHOR_INPUT_NEEDED` or `Not assessable from provided material`.

## Consistency checks

- Shared manuscript facts should stay consistent across all three reviewers.
- Divergence across reviewers should reflect weighting differences, not contradictory factual claims.
- Technical failings listed in the synthesis should match issues already raised in at least one individual report.

## Final release rule

- If the skill cannot produce a grounded three-reviewer package without major invention, it should return a bounded draft review with explicit missing-information flags rather than pretending certainty.
