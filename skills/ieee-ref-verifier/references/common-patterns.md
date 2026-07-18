# Common IEEE reference problems

## DOI year versus publication year

The year embedded in a DOI may reflect registration or manuscript numbering. Use the official volume/issue year for an assigned issue; otherwise report the authoritative early-access year and identify the metadata state.

## Early access versus issue assignment

An IEEE article may first appear as Early Access and later receive volume, issue, page range, or article number metadata. Prefer the current version-of-record fields and avoid combining obsolete early-access fields with final issue metadata.

## Pages versus article numbers

Do not force an article number into a page range. Preserve the identifier type used by the official record.

## Author problems

- Compare the full ordered list when available.
- Treat a different first author or unrelated author set as a high-severity identity mismatch.
- Preserve compound surnames and diacritics.
- Do not use `et al.` to hide a supplied author-order conflict during verification.

## Conference and journal versions

Related titles may represent a preliminary conference paper and a substantively extended journal article. Verify venue, year, DOI, and title separately. Mark duplicate versions only when both entries identify the same work, not merely the same research line.

## Legacy IEEE records

Older IEEE/IET/IEE records may have incomplete Crossref metadata. Search IEEE Xplore or the official archive before marking the reference missing. Preserve the historical publisher or society name used by the record.

## DOI points to another work

A syntactically valid DOI can still be wrong by one character. Resolve it and compare normalized title and first author. If they disagree materially, classify `metadata_conflict` or `likely_fabricated` rather than silently replacing the DOI.
