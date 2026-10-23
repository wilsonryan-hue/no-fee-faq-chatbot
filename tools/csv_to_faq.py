#!/usr/bin/env python3
"""Turn a simple 3-column CSV (question, answer, keywords) into the faq.json the widget reads.

Usage:
  python3 tools/csv_to_faq.py faqs.csv faq.json --name "Hollybank Bakery" --colour "#7a3e12" \
      --email hello@your-site.co.uk

keywords: optional, separated by ; (e.g. "open;hours;times"). Answers may contain
[link text](https://...) or [link text](/page) links. Standard library only.
"""
import argparse, csv, json, sys

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("csv"); p.add_argument("out")
    p.add_argument("--name", default="Questions? Ask us")
    p.add_argument("--colour", default="#1f3fbf")
    p.add_argument("--email", default="")
    p.add_argument("--threshold", type=float, default=0.34)
    a = p.parse_args()
    faqs = []
    with open(a.csv, newline="", encoding="utf-8-sig") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            q = (row.get("question") or "").strip(); ans = (row.get("answer") or "").strip()
            if not q or not ans:
                sys.exit(f"Row {i}: question and answer are both required")
            kw = [k.strip() for k in (row.get("keywords") or "").split(";") if k.strip()]
            faqs.append({"q": q, "keywords": kw, "a": ans})
    if not faqs:
        sys.exit("No rows found. The CSV needs a header row: question,answer,keywords")
    contact = f" Email [{a.email}](mailto:{a.email}) and we'll reply." if a.email else ""
    cfg = {
        "name": a.name, "colour": a.colour, "button": "Questions? Ask us",
        "greeting": "Hi! Ask me a question, or tap one below.",
        "fallback": "Sorry, I don't have an answer for that one, so I won't guess." + contact,
        "threshold": a.threshold,
        "suggest": list(range(min(4, len(faqs)))),
        "synonyms": {"price": ["cost", "costs", "much", "charge", "fee", "fees", "gbp", "pound", "pounds"],
                     "time": ["long", "quick", "fast", "when", "days"],
                     "open": ["opening", "hours", "times"]},
        "faqs": faqs,
    }
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=1)
    print(f"Wrote {len(faqs)} Q&As to {a.out}")

if __name__ == "__main__":
    main()
