# Workflow 4: Citation File Management

**Purpose:** Download, convert, and clean citation files for IEEE manuscripts.

**Uses:** `scripts/format-converter.py` for DOI/arXiv/known-ID export to `.ris`, `.bib`, or `.enw`.

## Procedure

1. Identify papers by DOI, arXiv ID, title, or a user-provided reference list.
2. Download/convert with format-converter:

```bash
# CrossRef DOI
python scripts/format-converter.py --doi 10.1109/TAC.2024.000000 --format ris

# arXiv preprint metadata
python scripts/format-converter.py --arxiv 2401.00000 --format bib

# Batch from file
python scripts/format-converter.py --input refs.txt --format ris
```

3. Convert format as needed: `.ris` for EndNote/Zotero, `.bib` for LaTeX, `.enw` for EndNote tagged export.
4. Save to a references directory or the user's requested output path.
5. Verify output count matches input and flag missing DOI/venue/year fields.

## refs.txt Format

```text
DOI:10.1109/TAC.2024.000000
DOI:10.1109/TII.2025.000000
ARXIV:2401.00000
QUERY:networked control packet loss stability
# Lines starting with # are comments
```

## Error Modes

- Script failure twice: fall back to manual `.ris`/`.bib` generation from verified metadata.
- DOI not found in CrossRef: verify DOI spelling and publisher page.
- arXiv ID not found: check version suffix and whether an archival version exists.
