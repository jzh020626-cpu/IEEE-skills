# Source Tiers and Reliability

Use this file to decide which source can support which claim in an IEEE Transactions literature workflow.

## Tier 1: authoritative for venue and metadata

| Source | Use |
|---|---|
| IEEE Author Center | Templates, editorial style, graphics, supplementary material |
| IEEE society/journal pages | Target-venue scope, page limits, checklist, special sections |
| IEEE Xplore journal pages | Venue identity, issue status, article landing pages |
| CrossRef DOI metadata | DOI, title, authors, journal, year, volume/issue/pages |

## Tier 2: discovery and cross-checking

| Source | Use |
|---|---|
| OpenAlex | Broad paper discovery and author disambiguation |
| Semantic Scholar | Citation graph, related papers, field filters |
| Scopus | Curated database search when configured |
| Web of Science | Citation reports and curated-index checks |
| arXiv | Preprint discovery only; verify archival status separately |

## Tier 3: manual or last-resort discovery

| Source | Use |
|---|---|
| Google Scholar | Broad fallback; verify everything elsewhere |
| CNKI / 万方 | Chinese literature manual check |
| Publisher pages outside IEEE | Broader related work only when user allows non-IEEE expansion |

## Routing by task

| Task | Primary | Secondary | Last resort |
|---|---|---|---|
| Target-venue compliance | IEEE society page | IEEE Author Center | submission-system screenshot |
| Citation verification | DOI/CrossRef | IEEE Xplore page | publisher page |
| Related work for T-ASE/TII/TAC/TCST | IEEE Xplore + CrossRef | OpenAlex/Semantic Scholar | Scopus/WoS |
| Conference-extension check | prior conference DOI/page | IEEE Xplore/CrossRef | author-provided PDF |
| Survey seed set | IEEE Transactions/Letters | top conference versions | broader publisher set only if requested |

## Support rule

Only official venue pages can establish style/page/submission rules. Bibliographic databases can establish metadata, but not author-instruction compliance.
