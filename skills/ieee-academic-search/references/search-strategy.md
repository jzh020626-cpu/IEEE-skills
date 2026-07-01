# IEEE Search Strategy

Use this file to construct precise searches for IEEE Transactions manuscripts.

## Query construction

1. Split the topic into `task`, `method`, `system`, `constraint`, and `metric`.
2. Add target venue names or abbreviations only when strict venue scope matters.
3. Search archival terms first: `IEEE Transactions on ...`, `T-ASE`, `TII`, `TAC`, `TCST`, `TRO`, `RA-L`, `TWC`, `TCOM`, `IoT-J`.
4. Use conference names only to trace conference-extension history or early versions: ICRA, IROS, CASE, CDC, ACC, INFOCOM.
5. Use arXiv only to discover recent work; verify whether an archival version exists.

## Example query patterns

| Need | Query pattern |
|---|---|
| Robotics/automation | `"multi-robot" "automation" "IEEE Transactions on Automation Science and Engineering"` |
| Control theory | `"packet loss" "stability" "IEEE Transactions on Automatic Control"` |
| Control technology | `"model predictive control" "implementation" "IEEE Transactions on Control Systems Technology"` |
| Industrial informatics | `"industrial edge" "fault detection" "IEEE Transactions on Industrial Informatics"` |
| Communications | `"latency" "throughput" "IEEE Transactions on Wireless Communications"` |

## Decision tree

```text
Known target venue?
├─ Yes → search official venue page + strict CrossRef/IEEE Xplore metadata
└─ No
   ├─ robotics/automation → T-ASE/T-RO/RA-L plus major robotics conferences
   ├─ control theory → TAC/TCST/TCNS/L-CSS plus CDC/ACC for prior versions
   ├─ communications → TWC/TCOM/IoT-J/TMC plus INFOCOM for prior versions
   └─ industrial systems → TII/TIE/IoT-J/Smart Grid
```

## Edge cases

- Chinese journals: CNKI/万方 require manual check.
- Preprints only: mark as non-archival until an accepted journal/conference version is found.
- Same title in conference and journal: compare abstracts, figures, theorem statements, and experiment sets for added archival value.
