# RIS, BibTeX, and ENW Format Specifications

Use this reference for IEEE manuscript reference-management exports.

## RIS Format

RIS is a standard import format for EndNote, Zotero, and most reference managers.

```text
TY  - JOUR
AU  - Last, First
AU  - Last2, First2
TI  - Article Title
JO  - IEEE Transactions on Example
PY  - 2024
VL  - 10
IS  - 3
SP  - 123
EP  - 145
DO  - 10.1109/example
UR  - https://doi.org/10.1109/example
ER  -
```

Each RIS record must end with `ER  -` followed by a blank line.

## BibTeX Format

```bibtex
@article{smith2024example,
  author  = {Smith, First and Doe, Second},
  title   = {Article Title},
  journal = {IEEE Transactions on Example},
  year    = {2024},
  volume  = {10},
  number  = {3},
  pages   = {123--145},
  doi     = {10.1109/example},
  url     = {https://doi.org/10.1109/example}
}
```

Required fields for journal articles: author, title, journal, year. DOI is strongly preferred.

## ENW (EndNote Tagged) Format

```text
%0 Journal Article
%T Article Title
%A Last, First
%A Last2, First2
%J IEEE Transactions on Example
%V 10
%N 3
%P 123-145
%D 2024
%R 10.1109/example
%U https://doi.org/10.1109/example
```

## IEEE cleaning rules

- Preserve DOI exactly.
- Preserve IEEE journal title and abbreviation consistently.
- Remove HTML tags from abstracts and titles.
- Normalize whitespace.
- Use one citation key convention per `.bib` file.
- Flag preprint-only entries when the user asked for archival IEEE references.
- Do not fabricate volume, issue, page, article number, or DOI fields.

## Format selection guide

| User says | Use format |
|---|---|
| "EndNote", ".enw" | ENW or RIS |
| "Zotero" | RIS |
| "LaTeX", "BibTeX", "Bib" | BibTeX |
| "reference manager import" | RIS |
