#!/usr/bin/env python3
"""Refresh data/scholar.json from official, keyless scholarly APIs.

Primary source:  OpenAlex        (lookup by ORCID — reliable, no rate issues)
Fallback source: Semantic Scholar (name search)

Both are free public APIs, so unlike Google Scholar scraping this works
consistently from GitHub Actions runners. The output format is unchanged,
so index.html needs no modification. Citation counts differ slightly from
Google Scholar (Scholar indexes more grey literature); the site still links
to the Scholar profile for canonical figures.

Run locally:  python scripts/fetch_scholar.py   (no dependencies)
In CI:        .github/workflows/update-scholar.yml (weekly)
"""

import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ORCID = "0000-0001-8286-9997"
AUTHOR_NAME = "Ignatius Ezeani"
SCHOLAR_PROFILE = "https://scholar.google.com/citations?user=flSvPiMAAAAJ"
MAX_PUBLICATIONS = 12
OUT_PATH = Path(__file__).resolve().parent.parent / "data" / "scholar.json"

# Identifying ourselves politely gets us OpenAlex's faster "polite pool".
HEADERS = {"User-Agent": f"ignatiusezeani.github.io publication sync (mailto:i.ezeani@lancaster.ac.uk)"}


def get_json(url: str) -> dict:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def clean_title(title: str) -> str:
    return " ".join((title or "Untitled").split())


def format_authors(names: list[str], max_names: int = 6) -> str:
    names = [n for n in names if n]
    if len(names) > max_names:
        return ", ".join(names[:max_names]) + ", et al."
    return ", ".join(names)


def from_openalex() -> dict:
    author = get_json(f"https://api.openalex.org/authors/orcid:{ORCID}")
    stats = author.get("summary_stats", {}) or {}

    works_url = (
        "https://api.openalex.org/works?"
        + urllib.parse.urlencode(
            {
                "filter": f"author.orcid:{ORCID}",
                "sort": "publication_date:desc",
                "per-page": MAX_PUBLICATIONS,
            }
        )
    )
    works = get_json(works_url).get("results", [])

    pubs = []
    for w in works:
        loc = (w.get("primary_location") or {}).get("source") or {}
        doi = w.get("doi")  # already a full https://doi.org/... URL in OpenAlex
        pubs.append(
            {
                "title": clean_title(w.get("display_name")),
                "authors": format_authors(
                    [a.get("author", {}).get("display_name") for a in w.get("authorships", [])]
                ),
                "venue": loc.get("display_name") or "",
                "year": w.get("publication_year"),
                "citations": w.get("cited_by_count") or 0,
                "url": doi or w.get("id") or SCHOLAR_PROFILE,
            }
        )

    return {
        "source": "OpenAlex",
        "metrics": {
            "citations": author.get("cited_by_count"),
            "h_index": stats.get("h_index"),
            "i10_index": stats.get("i10_index"),
        },
        "publications": pubs,
    }


def from_semantic_scholar() -> dict:
    base = "https://api.semanticscholar.org/graph/v1"
    search = get_json(
        f"{base}/author/search?"
        + urllib.parse.urlencode({"query": AUTHOR_NAME, "fields": "name,hIndex,citationCount,paperCount"})
    )
    candidates = search.get("data", [])
    if not candidates:
        raise RuntimeError("Semantic Scholar: no author match")
    # Pick the candidate with the most papers (disambiguates common names).
    author = max(candidates, key=lambda a: a.get("paperCount") or 0)

    papers = get_json(
        f"{base}/author/{author['authorId']}/papers?"
        + urllib.parse.urlencode(
            {
                "fields": "title,year,venue,citationCount,externalIds,authors",
                "limit": 50,
            }
        )
    ).get("data", [])
    papers.sort(key=lambda p: (p.get("year") or 0, p.get("citationCount") or 0), reverse=True)

    pubs = []
    for p in papers[:MAX_PUBLICATIONS]:
        doi = (p.get("externalIds") or {}).get("DOI")
        pubs.append(
            {
                "title": clean_title(p.get("title")),
                "authors": format_authors([a.get("name") for a in p.get("authors", [])]),
                "venue": p.get("venue") or "",
                "year": p.get("year"),
                "citations": p.get("citationCount") or 0,
                "url": f"https://doi.org/{doi}" if doi else SCHOLAR_PROFILE,
            }
        )

    return {
        "source": "Semantic Scholar",
        "metrics": {
            "citations": author.get("citationCount"),
            "h_index": author.get("hIndex"),
            "i10_index": None,  # not provided by Semantic Scholar
        },
        "publications": pubs,
    }


def main() -> int:
    result = None
    for fetch in (from_openalex, from_semantic_scholar):
        try:
            result = fetch()
            break
        except Exception as exc:
            print(f"{fetch.__name__} failed: {exc}", file=sys.stderr)

    if result is None or not result["publications"]:
        # Non-destructive exit: keep the previous scholar.json in place.
        print("All sources failed; keeping previous data.", file=sys.stderr)
        return 0

    data = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "source": result["source"],
        "profile": SCHOLAR_PROFILE,
        "metrics": result["metrics"],
        "publications": result["publications"],
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    m = data["metrics"]
    print(
        f"Wrote {OUT_PATH} from {data['source']} — "
        f"{len(data['publications'])} publications, "
        f"{m['citations']} citations, h={m['h_index']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
