# ieee-downloader

Lawful academic full-text and supplementary-information retrieval for IEEE and engineering literature.

## Routes

- publisher APIs for configured Elsevier, Springer Nature, and IEEE credentials;
- legitimate article-level open access;
- CNKI through the user's authorized institutional session;
- institutional Web Access through the user's active authenticated browser;
- supplementary-information discovery and download when requested.

The downloader validates content rather than trusting HTTP success and writes per-item provenance/status manifests.

## First-run configuration

```bash
python scripts/configure_school.py --help
python scripts/configure_credentials.py --help
node scripts/batch_download.mjs --help
```

Before a batch, choose exactly one SI mode:

```bash
node scripts/batch_download.mjs --dois 10.x/a,10.y/b --out downloads --si
node scripts/batch_download.mjs --topic "networked control" --count 10 --out downloads --no-si
```

Use environment variables or local ignored configuration for credentials. Never commit API keys, cookies, passwords, downloaded papers, or browser state.

## Safety

- No paywall, access-control, rate-limit, CAPTCHA, slider, or anti-bot bypass.
- Verification challenges are handed to the user in the authenticated browser.
- No unauthorized mirrors or redistribution of non-open content.
- A configured key does not imply full-text entitlement.
- PDF-only requests require a real PDF signature; HTML, CAJ, login pages, and error documents are not silently renamed.

See `SKILL.md` for routing rules and `manifest.yaml` for on-demand modules.
