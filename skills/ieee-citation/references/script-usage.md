# Script usage and long-article strategy

Open this reference when running `scripts/ieee_citation.py` or when the input is long enough to need batching.

## Running the script

```bash
python scripts/ieee_citation.py \
  manuscript.txt \
  --scope all \
  --format ris \
  --output ieee_references.ris \
  --report ieee_citation_report.md
```

## Useful options

- `--scope tase|tii|tac|tcst|tro|ral|tie|twc|tcom|iotj`: strict venue scope.
- `--scope robotics|control|communications|industrial`: field bundle.
- `--scope ieee|all`: broad IEEE-first archival set.
- `--format enw|ris|zotero-rdf`: export format.
- `--allow-incomplete-authors`: explicit unsafe override when source author metadata cannot first be verified.
- `--rows 40`: raise for broad searches; keep top candidates manageable.
- `--top-k 3`: number of candidates to keep per segment.
- `--polite-delay 0.5`: seconds between Crossref requests.
- `--no-report` / `--no-json`: suppress sidecar artifacts.

## Long-Article Strategy

When the input has more than about 10 citable segments:

1. Split by section (`Introduction`, `Related Work`, `Experiments`, etc.).
2. Run one search per section with the same strict scope.
3. Merge outputs by DOI and remove duplicates.
4. Report a compact table: segment ID, best candidate, support grade, missing evidence.
5. Avoid long inline discussion for every segment; reserve detail for segments with no direct IEEE support.

## Strictness Rules

- Do not use non-IEEE sources to satisfy a strict IEEE scope unless the user explicitly broadens the task.
- Do not treat preprints as replacements for archival IEEE references.
- Do not infer support from title alone.
- For target-venue submission advice, verify current official journal pages outside the script; Crossref metadata is not a style-authority source.
