# Citation Parser

Strategy reference for extracting citations from documents. Used by Workflow 2 (Citation Verification).

## Extraction by Source Format

### .docx

**Method:** Use python-docx to iterate paragraphs. For each paragraph, apply regex patterns below in order.

**Preprocessing:**
- Skip paragraphs inside EndNote field codes: if paragraph text matches `ADDIN EN\.\w+`, skip entire paragraph.
- Skip Zotero field codes: if paragraph text matches `\{[|]?\|[^}]+\}`, skip.
- Strip inline Zotero markers: remove `\{citation:\d+\}` spans from text.

**Regex patterns** (apply to cleaned text):

| Pattern | Target | Example |
|---------|--------|---------|
| `10\.\d{4,}/[^\s]+` | DOI | `10.1038/ieee14539` |
| `arXiv:\s*\d{4}\.\d{4,}(v\d+)?` | arXiv ID | `arXiv: 1706.03762v7` |

### .tex / .bib

**Method:** Read file as text. Apply patterns:

| Pattern | Target |
|---------|--------|
| `\\cite\{([^}]+)\}` | Citation keys (comma-separated) |
| `\\bibitem\{([^}]+)\}` | Bibitem keys |
| `@article\{([^,]+),` | BibTeX entry keys |
| `doi\s*=\s*\{([^}]+)\}` | DOI in BibTeX |

**Resolution:** Citation keys → resolve via .bib file `@article` entries. If standalone .tex without .bib, flag as `manual_needed`.

**natbib/biblatex:** `\\citep`, `\\citet`, `\\textcite` all reduce to `\\cite` semantics for key extraction.

### .txt

**Method:** Line-by-line scan. Apply the same DOI/arXiv regex patterns as .docx.

**Edge cases:**
- Paste-imported references may have line-wrapping that splits DOIs. Before scanning, join lines where the previous line ends mid-DOI pattern (no terminal punctuation, next line starts with alphanumeric).
- References without identifiers: extract first line as candidate title, mark for title+author resolution via MCP search.

## Resolution Priority

For each extracted reference:
1. DOI → `get_paper_by_doi` or `search_crossref`
2. arXiv ID → `search_arxiv`, then search for an archival DOI
3. Title + first author → CrossRef, IEEE Xplore/official pages, OpenAlex, or Semantic Scholar
4. Venue/page rules → official IEEE society or Author Center page
5. Citation key only (unresolvable from .bib) → `manual_needed`

## Classification Labels

| Label | Condition |
|-------|-----------|
| `verified` | Retrieved metadata matches document metadata (title + journal + year all match) |
| `mismatch` | Retrieved metadata exists but conflicts with document |
| `not_found` | No match found in any database |
| `suspicious` | Match found but metadata incomplete (e.g., missing DOI, only partial title match) |
| `manual_needed` | Cannot resolve to a database query (no DOI, title too generic, or official venue page required) |
