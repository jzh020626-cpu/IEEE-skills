---
name: ieee-academic-search
description: >-
  Multi-source literature search, citation verification, DOI/arXiv/IEEE Xplore-oriented reference management, strict independent-citation audits, article-level citation metrics, influential-citer profiling, citation-context extraction, and BibTeX/RIS/ENW conversion for robotics, automation, control, communications, and industrial informatics papers. Use when the user asks to search papers, verify citations, build related work, manage references, audit self-citation-independent impact, or find support for IEEE Transactions manuscripts.
---

# IEEE Academic Search Router

Use the static/dynamic routing declared in `manifest.yaml`; do not load every workflow.

## Routing protocol

1. Read `manifest.yaml` and every file under `always_load`.
2. Detect one or more workflow values:
   - `multi-source-search`
   - `citation-verification`
   - `venue-compliance`
   - `citation-file-mgmt`
   - `reference-mgmt`
   - `strict-other-citation-impact-audit`
3. State the detected workflow(s) in one short line.
4. Load only the mapped workflow fragment(s), then load linked references or scripts on demand.
5. Run the declared T1→T2→T3 source fallback. Report a source failure and continue with the remaining routes.

## IEEE operating rules

- Prefer archival IEEE journals and major engineering venues when they directly support the claim; do not exclude a stronger authoritative non-IEEE source merely because of branding.
- Treat conference and journal versions as related but distinct records. Preserve prior-version and extension relationships.
- Track DOI, exact venue, year, version, contribution type, method family, baselines, metrics, evidence strength, and claim relevance.
- For current venue rules, use official journal author pages and record the retrieval date.
- For strict independent-citation audits, define self-citation and institutional-overlap rules before counting, separate raw citation count from verified independent citations, and label uncertain identities.
- Do not invent citations, metadata, citation contexts, author affiliations, influence labels, metrics, or access results.
- Use `ieee-ref-verifier` for field-level correction of a supplied reference list and `ieee-citation` when the main job is inserting claim-linked sources into manuscript text.
