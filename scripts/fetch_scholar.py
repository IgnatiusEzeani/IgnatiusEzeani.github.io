#!/usr/bin/env python3
"""Fetch Google Scholar metrics and publications for the site.

Writes data/scholar.json, which index.html reads at page load.
Run locally:  pip install scholarly && python scripts/fetch_scholar.py
In CI:        triggered weekly by .github/workflows/update-scholar.yml

Note: Google Scholar has no official API; the `scholarly` package scrapes
public profile pages. If Scholar rate-limits the runner, the script exits
non-destructively and the previous scholar.json is kept.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHOLAR_USER_ID = "flSvPiMAAAAJ"  # Dr Ignatius Ezeani
MAX_PUBLICATIONS = 12
OUT_PATH = Path(__file__).resolve().parent.parent / "data" / "scholar.json"


def main() -> int:
    try:
        from scholarly import scholarly
    except ImportError:
        print("Install dependency first: pip install scholarly", file=sys.stderr)
        return 1

    try:
        author = scholarly.search_author_id(SCHOLAR_USER_ID)
        author = scholarly.fill(author, sections=["basics", "indices", "publications"])
    except Exception as exc:  # rate-limited or blocked — keep old data
        print(f"Scholar fetch failed, keeping previous data: {exc}", file=sys.stderr)
        return 0

    pubs = []
    # Sort newest first, then by citations within a year
    raw = sorted(
        author.get("publications", []),
        key=lambda p: (
            int(p.get("bib", {}).get("pub_year") or 0),
            int(p.get("num_citations") or 0),
        ),
        reverse=True,
    )
    for p in raw[:MAX_PUBLICATIONS]:
        bib = p.get("bib", {})
        pub_id = p.get("author_pub_id", "")
        pubs.append(
            {
                "title": bib.get("title", "Untitled"),
                "authors": bib.get("author", "").replace(" and ", ", "),
                "venue": bib.get("citation", ""),
                "year": int(bib["pub_year"]) if bib.get("pub_year") else None,
                "citations": p.get("num_citations") or 0,
                "url": (
                    "https://scholar.google.com/citations?"
                    f"view_op=view_citation&hl=en&user={SCHOLAR_USER_ID}"
                    f"&citation_for_view={pub_id}"
                )
                if pub_id
                else f"https://scholar.google.com/citations?user={SCHOLAR_USER_ID}",
            }
        )

    data = {
        "updated": datetime.now(timezone.utc).isoformat(),
        "profile": f"https://scholar.google.com/citations?user={SCHOLAR_USER_ID}",
        "metrics": {
            "citations": author.get("citedby"),
            "h_index": author.get("hindex"),
            "i10_index": author.get("i10index"),
        },
        "publications": pubs,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT_PATH} — {len(pubs)} publications, "
        f"{data['metrics']['citations']} citations, h={data['metrics']['h_index']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
