---
name: ieee-ref-verifier
description: Verify IEEE and engineering references field by field across authoritative sources, including author order, title, venue, year, volume, issue, pages or article number, DOI, preprint-to-version-of-record status, and conference-versus-journal identity. Use for single citations or full reference lists, hallucinated-reference checks, DOI/title conflicts, early-access versus issue metadata, duplicate-version cleanup, IEEE numbered-reference audits, BibTeX/RIS cleanup, Zotero correction plans, or Chinese requests such as 参考文献核验、逐条查引用、DOI核对、作者顺序检查、卷期页码检查、查假文献.
---

# IEEE Reference Verifier

Verify identity before formatting. A reference that looks syntactically correct is not verified until its bibliographic fields point to the same work.

## Workflow

1. Parse each entry into authors, title, venue, year, volume, issue, pages/article number, DOI, URL, and version type.
2. Resolve the candidate by DOI when present, then cross-check title and first author.
3. When DOI is absent or wrong, search exact title plus author and year.
4. Prefer the version of record. Keep a preprint only when it is the intended cited object or no archival version exists.
5. Compare fields using the source hierarchy in `references/source-hierarchy.md`.
6. Classify the entry:
   - `verified`
   - `verified_with_format_fix`
   - `metadata_conflict`
   - `wrong_version`
   - `duplicate_version`
   - `not_found`
   - `likely_fabricated`
7. Return corrected IEEE-style metadata separately from the evidence report.
8. Never overwrite Zotero or manuscript files unless the user explicitly asks for the edit.

Read `references/common-patterns.md` for recurring DOI-year, author-order, page/article-number, early-access, conference/journal, and legacy IEEE cases.

## Output

```text
Reference verification summary
- entries checked:
- verified:
- corrected:
- unresolved:
- likely fabricated:

| # | Status | Supplied identity | Verified identity | Field differences | Evidence sources | Recommended action |
|---:|---|---|---|---|---|---|

Corrected IEEE references
[numbered entries or BibTeX/RIS fields]

Unresolved checks
- [specific missing source or ambiguity]
```

## Rules

- Do not infer that a DOI is correct from its syntax.
- Do not use DOI-embedded years as the publication year.
- Preserve official author order and diacritics when supported.
- Distinguish online publication date, issue year, conference year, and proceedings year.
- Do not merge a conference paper and journal extension as duplicates merely because titles overlap.
- For early-access IEEE articles, report the currently authoritative metadata and flag fields that may change after issue assignment.
- Cite the source checked for every material correction.
