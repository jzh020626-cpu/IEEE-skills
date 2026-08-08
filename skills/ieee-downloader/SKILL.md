---
name: ieee-downloader
description: >-
  Configure lawful academic full-text retrieval through open access, publisher APIs, CNKI, or user-authorized institutional browser sessions; download PDFs or supported native full-text formats; collect optional supplementary information; validate files; and write provenance manifests for IEEE and engineering literature workflows. Use only when the user requests retrieval, authorized download, or supplementary-material collection.
---

# IEEE Literature Downloader

Route every item through lawful access. `scripts/batch_download.mjs` is the orchestration entry point.

## Intake gate

Before creating output files, resolve the requested papers and determine whether Supporting Information (SI) is wanted. An explicit SI request counts as yes; an explicit “main text only” request counts as no. Otherwise ask once for the batch. Invoke the CLI with exactly one of `--si` or `--no-si`.

## Routing

1. Normalize DOI/title and identify language, publisher, requested format, and any supplied source URL.
2. Chinese literature or an explicit CNKI source uses the CNKI route.
3. For Elsevier, Springer Nature, or IEEE content with a configured publisher credential, try the publisher API first.
4. After an API failure, or for other English publishers, try legitimate article-level open-access sources.
5. Use institutional Web Access only with the user's authorization and active authenticated browser state. Do not assume a new browser profile has the same session.
6. Do not substitute HTML, CAJ, a login page, or an error page when the user requested PDF.
7. Validate signature/content type, size, and readability; write a per-item manifest with source URL, access route, status, filename, checksum when available, and retrieval time.
8. Load `references/institutional-browser-workflow.md` only when OA and applicable publisher APIs are exhausted and authorized browser access is needed. Load `references/delivery-verification-and-failures.md` for SI, final file verification, naming, or typed failures.

## Configuration and references

Read `manifest.yaml` and load only the relevant module:

- first-run institution setup: `scripts/configure_school.py`
- publisher credentials: `scripts/configure_credentials.py`
- route planning and batch retrieval: `scripts/batch_download.mjs`
- browser-authenticated PDF retrieval: `scripts/browser_pdf_downloader.mjs`
- canonical statuses: `scripts/lib/status-codes.mjs`

## Safety and authorization

- Never bypass a paywall, access control, rate limit, CAPTCHA, Cloudflare page, or institutional restriction.
- Never automate a CAPTCHA or slider challenge. Pause and hand the controlled browser to the user, then continue only after the user completes verification.
- Never export cookies, collect an institutional password, commit API keys, or print secrets in logs.
- An API key does not prove full-text entitlement. A successful HTTP response does not prove a valid paper file.
- Do not use unauthorized mirrors or redistribute non-open content.
