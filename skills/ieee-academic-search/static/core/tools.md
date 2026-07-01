# MCP tools and shared modules

Multi-source literature search, citation verification, citation format conversion, and reference management for IEEE Transactions manuscripts.

## Core search

| Tool | Source | Best For |
|------|--------|----------|
| `search_papers` | academic-search MCP | Concurrent engineering-paper discovery across CrossRef/OpenAlex/arXiv and configured providers |
| `get_paper_by_id` | academic-search MCP | DOI / arXiv ID / known identifier details |
| `get_citation` | academic-search MCP | DOI-based formatted citation |
| `search_scopus` | academic-search MCP | Broad scholarly database search when configured |
| `search_webofscience` | paper-search MCP | Curated index and citation reports when available |
| `search_semantic_scholar` | paper-search MCP | Citation graph and field-of-study filters |
| `search_google_scholar` | paper-search MCP | Last-resort broad academic search |

## IEEE-first provider order

1. IEEE Xplore / official IEEE society pages for target-venue identity and author instructions.
2. CrossRef / DOI metadata for bibliographic verification.
3. OpenAlex / Semantic Scholar for discovery and citation graph expansion.
4. Scopus / Web of Science when institutional access or API credentials are configured.
5. arXiv only for preprint discovery, never as a replacement for archival IEEE references.

## Optional non-default utilities

The underlying MCP server may expose additional biomedical or publisher-specific utilities inherited from the source template. Do not use them for IEEE Transactions work unless the user explicitly asks for that source family.

## Shared modules

| Module | Purpose |
|--------|---------|
| [Dedup Engine](../../references/dedup-engine.md) | Unified deduplication |
| [Citation Parser](../../references/citation-parser.md) | Extract citations from documents |
| [Search Strategy](../../references/search-strategy.md) | Query construction, source selection, ranking |
| [RIS/BibTeX Format](../../references/ris-bibtex-format.md) | Format specifications and field mappings |
| [Format Converter](../../scripts/format-converter.py) | DOI/arXiv/known-ID citation export |
