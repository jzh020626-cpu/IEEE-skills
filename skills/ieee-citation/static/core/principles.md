# Core principles (IEEE citation)

Use this skill to turn manuscript text into defensible IEEE-style citation support:

- segment manuscript claims into stable claim IDs
- search IEEE-first archival sources for each claim
- rank candidates conservatively and label support strength
- export `.enw`, `.ris`, or Zotero `.rdf` without fabricating missing metadata

## Default Scope

Default is IEEE-first archival coverage for robotics, automation, control, communications, industrial informatics, and networked systems.

Supported strict scopes:

- `tase`: IEEE Transactions on Automation Science and Engineering
- `tii`: IEEE Transactions on Industrial Informatics
- `tac`: IEEE Transactions on Automatic Control
- `tcst`: IEEE Transactions on Control Systems Technology
- `tro`: IEEE Transactions on Robotics
- `ral`: IEEE Robotics and Automation Letters
- `tie`: IEEE Transactions on Industrial Electronics
- `twc`: IEEE Transactions on Wireless Communications
- `tcom`: IEEE Transactions on Communications
- `iotj`: IEEE Internet of Things Journal
- `robotics`, `control`, `communications`, `industrial`, `ieee`, `all`: broader IEEE-first sets

Do not broaden beyond the IEEE-first scope unless the user explicitly asks or the audit finds no IEEE-first support. If broadening is necessary, label the result as non-IEEE support and keep it separate from strict IEEE coverage.

## Source Hierarchy

Use sources in this order:

1. IEEE Xplore and official IEEE society/journal pages for venue identity and publication status.
2. Crossref DOI metadata for bibliographic fields and DOI resolution.
3. Publisher pages or accessible abstracts/full text for support verification.
4. Semantic Scholar, Google Scholar, Scopus, Web of Science, OpenAlex, or arXiv only as discovery aids or fallback metadata sources.

Metadata is not evidence. A paper supports a claim only after the title/abstract/full text clearly matches the claim.

## Search Quality Rules

- Prefer 3-8 high-precision candidates per segment over long loosely related lists.
- Use exact phrase searches for distinctive method names; otherwise use concept terms and accepted venue abbreviations.
- Check venue identity; not every title containing "IEEE" is a Transactions/Letters venue.
- Prefer archival journal versions over conference versions when both exist.
- Treat citation count as a tie-breaker, not support evidence.
- Capture retractions, corrections, and publication-status ambiguity when visible.
- Date-sensitive target-venue advice requires a current source check and a search date.

## Source Notes

This skill uses public bibliographic APIs and official publisher/import documentation: Crossref REST API, IEEE Xplore/journal pages, IEEE Author Center reference guidance, and ENW/RIS/Zotero import formats. Verify official journal pages when exact venue coverage or page-policy currency matters.
