# Workflow 5: Reference Management

**Purpose:** Manage, enrich, and audit IEEE manuscript reference collections.

**Uses:** [Dedup Engine](../dedup-engine.md).

## 5a. Find related papers

1. Start from a seed DOI, title, or known IEEE venue paper.
2. Search CrossRef, IEEE Xplore/official pages, OpenAlex, and Semantic Scholar.
3. Filter by venue, year, method family, task, system, and metric.
4. Deduplicate against the seed set.
5. Present with context notes and support type.

## 5b. BibTeX generation

1. DOI -> CrossRef -> BibTeX/RIS/ENW.
2. arXiv ID -> arXiv metadata -> mark as preprint unless an archival DOI exists.
3. Batch: process multiple IDs via `scripts/format-converter.py`.
4. Clean: deduplicate by citation key, sort, validate required fields, and preserve DOI.

## 5c. Venue abbreviation and IEEE style audit

1. Check journal titles and abbreviations against IEEE reference style expectations.
2. Flag author-year citations in manuscript text.
3. Flag references not cited in order of appearance when a compiled/reference list is available.
4. Flag preprint-only entries when strict archival support is required.

## 5d. Conference-extension audit

1. Identify prior conference versions by title, authors, DOI, and venue.
2. Compare journal and conference records for new proofs, experiments, figures, datasets, or technical depth.
3. Mark as manual if the full prior version is unavailable.
