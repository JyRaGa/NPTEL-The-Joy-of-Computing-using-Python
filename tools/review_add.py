"""Append review decisions to index/answers_review.tsv.

Usage: python tools/review_add.py gid=B gid=A,C gid=n:42 gid=type:multi:A,B gid=note:text ...
  letters -> option answer (badge reviewed); n:VALUE -> numeric answer; type:T:ANS sets the type too;
  note:TEXT -> note on an official answer (kept with its existing answer).
"""
import sys
from pathlib import Path

TSV = Path(__file__).resolve().parent.parent / "index" / "answers_review.tsv"
L = "ABCDEFGH"
args = sys.argv[1:]
if args and args[0].startswith("--week="):
    # one file per week so parallel reviewers never write the same file
    TSV = TSV.parent / "review" / f"week-{int(args.pop(0)[7:]):02d}.tsv"
    TSV.parent.mkdir(exist_ok=True)
    if not TSV.exists():
        TSV.write_text("id\tanswer\tbadge\tnote\ttype\n", encoding="utf-8")
rows = []
for arg in args:
    gid, val = arg.split("=", 1)
    typ, note, ans = "", "", val
    if val.startswith("note:"):
        rows.append(f"{gid}\t\t\t{val[5:]}\t")
        continue
    if val.startswith("type:"):
        _, typ, ans = val.split(":", 2)
    if ans.startswith("n:"):
        ans, typ = ans[2:], typ or "numeric"
    else:
        ans = ",".join(str(L.index(c)) for c in ans.split(","))
    rows.append(f"{gid}\t{ans}\treviewed\t{note}\t{typ}")
with open(TSV, "a", encoding="utf-8") as f:
    f.write("\n".join(rows) + "\n")
print(f"added {len(rows)}")
