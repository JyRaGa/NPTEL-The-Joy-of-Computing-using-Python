"""Edit one option line (or `why`) of an existing explain entry: explain_fix.py WEEK ID LETTER|why TEXT|null"""
import json, sys
from pathlib import Path

w, id_, key, text = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
f = Path(__file__).resolve().parent.parent / "index" / "explain" / f"week-{w:02d}.jsonl"
rows = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
for d in rows:
    if d["id"] == id_:
        if key == "why":
            d["why"] = text
        else:
            d["options"][key] = None if text == "null" else text
        break
else:
    sys.exit("no such id")
f.write_text("".join(json.dumps(d, ensure_ascii=False) + "\n" for d in rows), encoding="utf-8", newline="\n")
