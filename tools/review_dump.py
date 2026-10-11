"""Print the groups of one week that still need an answer review (not official/pdf/run, not in answers_review.tsv).

Usage: python tools/review_dump.py WEEK
"""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
L = "ABCDEFGH"
done = {r["id"] for f in [ROOT / "index" / "answers_review.tsv", *sorted((ROOT / "index" / "review").glob("*.tsv"))]
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t")}
w = int(sys.argv[1])
for g in json.loads((ROOT / "site" / "data" / f"week-{w:02d}.json").read_text(encoding="utf-8")):
    if g["answer_source"] in ("official", "pdf", "run") or g["gid"] in done:
        continue
    a = g["answer"]
    a = ",".join(L[i] for i in a) if isinstance(a, list) else a
    print(f"## {g['gid']} {g['type']} ans={a or '-'}")
    ctx = g["context"] or {}
    if ctx.get("code"):
        print("CTXCODE:", ctx["code"][:600])
    for p in ctx.get("images", []) + g["images"]:
        print("IMG:", p)
    print(g["text"][:500])
    if g["code"]:
        print("CODE:", g["code"])
    for i, o in enumerate(g["options"]):
        extra = (" IMG:" + o["img"]) if o["img"] else ""
        extra += (" CODE:" + o["code"].replace("\n", " / ")) if o.get("code") else ""
        print(f"  {L[i]}) {o['text'][:160].replace(chr(10), ' / ')}{extra}")
    if g["type"] == "reveal" and g["crops"]:
        print("CROPS:", " ".join(g["crops"]))
