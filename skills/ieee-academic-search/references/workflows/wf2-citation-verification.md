# Workflow 2: Citation Verification

**Purpose:** Verify references in a document (`.docx`, `.tex`, `.txt`) against IEEE-style metadata and target-venue expectations.

**Uses:**

- [Citation Parser](../citation-parser.md)
- [Dedup Engine](../dedup-engine.md)
- [Source Tiers](../source-tiers.md)

## Procedure

1. Extract citations from the document.
2. Resolve each citation:
   - DOI -> CrossRef / IEEE Xplore / publisher page
   - arXiv ID -> arXiv metadata, then search for an archival version
   - Title + first author -> CrossRef, IEEE Xplore, OpenAlex, or Semantic Scholar
3. Compare retrieved metadata vs. manuscript metadata: title, authors, venue, year, DOI, volume/issue/pages.
4. Classify each reference: `verified`, `mismatch`, `not_found`, `suspicious`, or `manual_needed`.
5. Flag non-IEEE or preprint-only references when the user requested strict IEEE-first support.
6. Generate a compact report: total / verified / mismatched / not_found / suspicious / manual_needed.

## Error Modes

- Unsupported document format: request `.docx`, `.tex`, `.bib`, `.ris`, or `.txt`.
- Many references lack identifiers: suggest adding DOI or official landing-page URLs.
- Target venue has a self-citation or conference-extension policy: mark those checks manual unless author identity and prior version are available.
