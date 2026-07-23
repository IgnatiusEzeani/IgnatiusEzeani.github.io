# ignatiusezeani.github.io

Personal academic website for **Dr Ignatius M. Ezeani** — Research Fellow, UCREL Research Centre, Lancaster University; Visiting Researcher, Microsoft Research Lab Africa.

## What's here

| Path | Purpose |
|---|---|
| `index.html` | The entire site — self-contained HTML/CSS/JS, no build step |
| `data/scholar.json` | Publications + citation metrics the page reads at load |
| `scripts/fetch_scholar.py` | Pulls fresh data from Google Scholar |
| `.github/workflows/update-scholar.yml` | Runs the script every Monday and commits the result |

## Deploy (replaces the current site)

Since the repo is already named `ignatiusezeani.github.io`, GitHub Pages serves it automatically:

```bash
git clone https://github.com/IgnatiusEzeani/ignatiusezeani.github.io.git
cd ignatiusezeani.github.io
# back up the old site first if you want it:  git checkout -b legacy-site && git push -u origin legacy-site && git checkout main
# copy the new files in, then:
git add -A
git commit -m "New site: redesign with automated Scholar sync"
git push
```

If the old site used Jekyll themes, delete leftover `_config.yml` / theme files, or add an empty `.nojekyll` file to be safe.

## Automatic updates — what works and what doesn't

**Google Scholar — automated.** Scholar has no official API, so the weekly GitHub Action uses the `scholarly` package to scrape your public profile (`flSvPiMAAAAJ`) and rewrite `data/scholar.json` (citations, h-index, i10, latest publications with per-paper citation counts). The page falls back to the curated seed list if the file is missing or a sync fails. You can also trigger a sync any time from the repo's **Actions → Update Google Scholar data → Run workflow**. If Scholar rate-limits the runner occasionally, the previous data is simply kept.

**X / Twitter — embedded, best-effort.** The page embeds your `@igezeani` timeline via X's official widget. X has increasingly restricted these embeds (and some browsers block them), so the page detects a failed load and shows a "Follow on X" fallback instead. There is no free API tier that would let a static site reliably pull posts, tags, or mentions.

**LinkedIn — link only.** LinkedIn's API does not allow reading a personal feed for third-party display, full stop. The site links prominently to your profile instead. If you ever want post highlights on the page, the pragmatic route is a small `data/linkedin.json` you update by hand (happy to wire that up).

## Local preview

```bash
python -m http.server 8000
# open http://localhost:8000
```

(Serving over HTTP rather than opening the file directly is needed for the `scholar.json` fetch to work.)

## Customising

- Colours, fonts, and spacing are all CSS variables at the top of `index.html` (`:root`).
- The rotating greeting languages live in the `greetings` array in the script block.
- The hero's NER-style annotations are plain `<span class="ent ent-…">` elements — edit freely.
