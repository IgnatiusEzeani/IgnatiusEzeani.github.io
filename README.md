# ignatiusezeani.github.io

Personal academic website of **Dr Ignatius M. Ezeani** — Research Fellow at the UCREL Research Centre, Lancaster University, and Visiting Researcher at Microsoft Research Lab Africa. Research in NLP for low-resource and African languages, cross-lingual model adaptation, and digital & spatial humanities.

**Live site:** https://ignatiusezeani.github.io/

## Structure

```
├── index.html                        # The entire site (no build step)
├── assets/
│   └── profile.jpg                   # Profile photo shown in the hero
├── data/
│   └── scholar.json                  # Publications + citation metrics (auto-updated)
├── scripts/
│   └── fetch_scholar.py              # Pulls fresh data from Google Scholar
└── .github/workflows/
    └── update-scholar.yml            # Weekly sync (Mondays 06:00 UTC)
```

## How the Google Scholar sync works

Google Scholar has no official API, so a scheduled GitHub Action runs
`scripts/fetch_scholar.py` (via the [`scholarly`](https://pypi.org/project/scholarly/)
package) against the public profile and rewrites `data/scholar.json` with current
citation counts, h-index, i10-index, and recent publications. `index.html`
fetches that file at page load; if the file is missing or a sync fails, the page
falls back to a curated publication list.

- **Manual sync:** repo **Actions → Update Google Scholar data → Run workflow**
- **Requirement:** Settings → Actions → General → Workflow permissions must be
  set to *Read and write* so the Action can commit the updated JSON.
- **Local run:** `pip install scholarly && python scripts/fetch_scholar.py`

## Social feeds

- **X (@igezeani):** timeline embedded via X's official widget, with a
  follow-link fallback when embeds are blocked.
- **LinkedIn:** profile link only — LinkedIn's API does not permit displaying a
  personal feed on third-party sites.

## Local preview

```bash
python -m http.server 8000
# open http://localhost:8000
```

Serve over HTTP (rather than opening `index.html` directly) so the
`data/scholar.json` fetch works.

## Customising

- **Photo:** replace `assets/profile.jpg` (portrait orientation, ~4:5, ≥600px
  wide works best). Until a photo is present, the page shows a monogram
  placeholder.
- **Colours & type:** all design tokens are CSS variables in `:root` at the top
  of `index.html`.
- **Greeting languages:** edit the `greetings` array in the script block.
- **Publications seed list:** edit `data/scholar.json` (overwritten by the next
  scheduled sync) or the `FALLBACK` object in `index.html` (permanent fallback).

## License

Content © Ignatius M. Ezeani. Code may be reused freely.
