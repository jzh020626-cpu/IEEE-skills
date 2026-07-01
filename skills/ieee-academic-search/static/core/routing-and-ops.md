# Source routing and operations

## Source routing

See [Source Tiers & Reliability](../../references/source-tiers.md) for the complete reliability classification and fallback routing rules. IEEE-first routing is the default across all workflows.

Quick guide:

| User need | Primary | Secondary | Last Resort |
|-----------|---------|-----------|-------------|
| Target-venue rules | IEEE society / Author Center pages | IEEE Xplore journal pages | Current journal submission system |
| IEEE Transactions related work | IEEE Xplore / CrossRef DOI | OpenAlex / Semantic Scholar | Scopus / Web of Science |
| Control theory | TAC/TCST/TCNS pages + CrossRef | Semantic Scholar | arXiv for preprint discovery |
| Robotics / automation | T-ASE / T-RO / RA-L / ICRA/IROS/CASE metadata | Semantic Scholar | Google Scholar |
| Communications / networks | TWC / TCOM / IoT-J / INFOCOM metadata | Semantic Scholar | Google Scholar |
| Industrial informatics | TII / TIE / industrial CPS venues | Scopus / Web of Science | Google Scholar |
| Chinese literature | CNKI / 万方 manual check | Google Scholar | user-provided PDFs |

## Environment setup

### API keys (optional)

| Service | Env Var | Register At | Notes |
|---------|---------|-------------|-------|
| Semantic Scholar | `SEMANTIC_SCHOLAR_API_KEY` | `https://api.semanticscholar.org/` | Higher rate limits with key |
| Elsevier / Scopus / ScienceDirect | pybliometrics config | `https://dev.elsevier.com/` | Depends on API entitlement |

Do not copy API keys into this plugin. Use environment variables or local config files.

### Proxy (if behind firewall)

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

### Pre-flight check

```bash
python scripts/preflight.py
```

Run before batch operations to verify core endpoints are reachable.

### No-MCP fallback

When the MCP server is not mounted, use the stdlib-only scripts:

- `scripts/academic_search.py` queries OpenAlex for engineering-paper discovery with relevance reranking and optional author disambiguation.
- `scripts/format-converter.py` exports known DOI/arXiv/identifier records to `.ris`, `.bib`, or `.enw`.

```bash
python scripts/academic_search.py "networked control packet loss stability" --limit 10 --sort cited_by_count --mailto you@example.com
python scripts/format-converter.py --doi 10.1109/TAC.2024.000000 --format ris
```

Be polite to public APIs: pass `--mailto` or set `OPENALEX_MAILTO` / `CROSSREF_MAILTO` where supported.

## MCP server runtime

Use uv to start the MCP server in an isolated dependency environment:

```bash
uv run --no-project --directory <mcp-server> --with "mcp>=1.0.0,<2.0.0" --with "requests>=2.28.0,<3.0.0" --with "toml>=0.10.2,<2.0.0" --with "lxml>=4.9.0,<6.0.0" --with "pybliometrics>=4.4.1,<5.0.0" python academic_search_server.py
```

Scopus / ScienceDirect are opt-in providers: include them only when configured and relevant. They may consume institutional API quota.

## Error handling

- MCP tool unavailable: report the specific failure and continue with remaining tools.
- No results: broaden IEEE venue names, use accepted abbreviations, and split the query into method/task/system terms.
- Script failure twice: fall back to manual DOI/title verification from official pages or CrossRef.

## Limitations

- Google Scholar is not API-backed; results may vary.
- Chinese literature often requires manual CNKI / 万方 checks.
- Citation counts can lag behind publisher metadata.
