# IEEE academic-search MCP server

This MCP server supports engineering literature discovery and reference metadata workflows for IEEE Transactions manuscripts. Default use should stay IEEE-first: CrossRef/OpenAlex, IEEE pages, arXiv for preprint discovery, and configured Scopus/Web of Science-style providers when available.

## Tools

| Tool | Purpose |
|---|---|
| `search_papers` | Unified search across configured engineering metadata sources |
| `get_paper_by_id` | DOI or arXiv identifier lookup |
| `get_citation` | Format citation metadata |
| `search_scopus` | Scopus advanced search when configured |
| `get_scopus_abstract` | Scopus abstract and metadata |
| `get_scopus_citation_overview` | Scopus citation overview |
| `search_scopus_authors` / `get_scopus_author` | Author search and retrieval |
| `search_scopus_affiliations` / `get_scopus_affiliation` | Affiliation search and retrieval |
| `search_scopus_serial_titles` / `get_scopus_serial_title` | Journal/source metadata |
| `search_sciencedirect` | Optional publisher metadata search |
| `get_sciencedirect_article_metadata` | Optional publisher metadata retrieval |

## Configuration

- Elsevier / Scopus / ScienceDirect use the local `pybliometrics` configuration, normally `~/.config/pybliometrics.cfg`.
- Optional inherited metadata providers may require their own credentials, but they are not part of the IEEE-first default route.

Scopus / ScienceDirect are opt-in providers. Use them only when `sources` explicitly includes the provider or the user asks for it, because they may consume institutional API quota.
