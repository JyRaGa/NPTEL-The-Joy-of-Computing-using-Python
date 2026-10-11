"""Rewrite the README coverage table from site/data/week-NN.json. Run after cluster.py."""
import json, re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPAN = {"jan": "Jan–Apr", "jul": "Jul–Oct", "sep": "Sep–Dec"}
OTHER = [("run", "verified by running"), ("reviewed", "reviewed"), ("uploader", "unverified"), ("none", "no answer")]


def weeks(ws):
    ws, out, i = sorted(ws), [], 0
    while i < len(ws):
        j = i
        while j + 1 < len(ws) and ws[j + 1] == ws[j] + 1:
            j += 1
        out.append(f"{ws[i]}" if i == j else f"{ws[i]}–{ws[j]}")
        i = j + 1
    return ", ".join(out)


src, wk = defaultdict(dict), defaultdict(set)  # session -> base question id -> answer source
for f in sorted((ROOT / "site" / "data").glob("week-*.json")):
    for g in json.loads(f.read_text(encoding="utf-8")):
        s = g["answer_source"] if g["answer"] not in (None, [], "") else "none"
        for m in g["members"]:
            b = m.split("@")[0]
            term = b.split("/")[0]
            src[term][b] = s
            wk[term].add(int(b.split("/")[1][1:]))

rows, tot, off = [], 0, 0
for term in sorted(src):
    c = Counter(src[term].values())
    n = sum(c.values())
    tot, off = tot + n, off + c["official"]
    other = ", ".join(f"{c[k]} {label}" for k, label in OTHER if c[k]) or "—"
    y, s = term.split("-")
    rows.append(f"| {y} {SPAN[s]} | {weeks(wk[term])} | {n} | {round(100 * c['official'] / n)}% | {other} |")
rows.append(f"| **All** | | **{tot}** | **{round(100 * off / tot)}%** | |")

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
new = re.sub(r"(\|---\|---\|--:\|--:\|---\|\n)(?:\|.*\|\n)+", lambda m: m.group(1) + "\n".join(rows) + "\n", text, count=1)
assert new != text or "\n".join(rows) in text, "coverage table not found in README.md"
readme.write_text(new, encoding="utf-8")
print("\n".join(rows[-3:]))
