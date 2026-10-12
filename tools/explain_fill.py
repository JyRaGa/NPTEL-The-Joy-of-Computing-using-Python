"""Batch-edit wrong-option lines: python tools/explain_fill.py WEEK FILE.json  (FILE = {id: {letter: text}})."""
import json, sys
w, src = sys.argv[1], sys.argv[2]
fills = json.load(open(src, encoding="utf-8"))
p = f"index/explain/week-{int(w):02d}.jsonl"
rows = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
by = {r["id"]: r for r in rows}
for i, opts in fills.items():
    for k, t in opts.items():
        assert i in by and k in by[i]["options"], (i, k)
        by[i]["options"][k] = t
open(p, "w", encoding="utf-8", newline="\n").write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
print("filled", sum(len(o) for o in fills.values()), "in", p)
