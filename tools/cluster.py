"""Merge repeated questions across sessions into groups; write site/data/week-NN.json.

Input: site/data/questions.json (from build_dataset.py) and index/answers_review.tsv (optional overlay).
Same group = same normalised text+code AND same option set (order ignored); fuzzy text match >= RATIO
is allowed only when the option sets are identical. Text match with different options -> near_duplicates.md.
"""
import csv, hashlib, json, re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

from build_dataset import norm

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site" / "data"
RATIO = 0.9
LEXER = PythonLexer(stripnl=False)
FMT = HtmlFormatter(nowrap=True)


def hl(code):
    # build-time syntax highlighting: the site ships plain HTML spans, no runtime library
    return highlight(code, LEXER, FMT).rstrip("\n") if code else None


RANK = {"official": 0, "pdf": 1, "uploader": 2}


def mergeable(r):
    # code shown only as an image: identical text + options proves nothing unless the options are distinctive
    if r["images"] and not r["code"]:
        opts = r["norm_options"]
        return len(opts) >= 3 and sum(map(len, opts)) / len(opts) >= 6
    return bool(r["norm"]) and (len(r["norm"]) >= 12 or r["norm_options"])


def key(r):
    return r["norm"] + " || " + " | ".join(r["norm_options"])


def main():
    recs = json.loads((DATA / "questions.json").read_text(encoding="utf-8"))
    parent = list(range(len(recs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def union(a, b):
        parent[find(a)] = find(b)

    exact = {}
    for i, r in enumerate(recs):
        if not mergeable(r):
            continue
        k = key(r)
        if k in exact:
            union(i, exact[k])
        else:
            exact[k] = i

    # a ChatGPT copy and a video transcription of the same session question are one question by construction
    pos = {r["id"]: i for i, r in enumerate(recs)}
    for i, r in enumerate(recs):
        if r["id"].endswith("@gpt") and r["id"][:-4] in pos:
            union(i, pos[r["id"][:-4]])

    near = []
    by_week = defaultdict(list)
    for i, r in enumerate(recs):
        by_week[r["week"]].append(i)
    for w, ids in by_week.items():
        pool = ids + by_week.get(w + 1, [])
        for a_pos, a in enumerate(ids):
            ra = recs[a]
            if not mergeable(ra):
                continue
            for b in pool[a_pos + 1:]:
                if find(a) == find(b) or recs[b]["term"] == ra["term"] or not mergeable(recs[b]):
                    continue
                rb = recs[b]
                sm = SequenceMatcher(None, ra["norm"], rb["norm"], autojunk=False)
                if sm.real_quick_ratio() < RATIO or sm.quick_ratio() < RATIO or sm.ratio() < RATIO:
                    continue
                if ra["norm_options"] == rb["norm_options"]:
                    union(a, b)
                elif ra["norm_options"] and rb["norm_options"]:
                    shared = len(set(ra["norm_options"]) & set(rb["norm_options"]))
                    if shared * 2 >= max(len(ra["norm_options"]), len(rb["norm_options"])):
                        near.append((ra["id"], rb["id"]))

    review = {}
    rv = ROOT / "index" / "answers_review.tsv"
    for f in [rv, *sorted((ROOT / "index" / "review").glob("*.tsv"))]:
        if f.exists():
            for row in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
                review[row["id"]] = row

    fixes = {}
    for f in sorted((ROOT / "index" / "fixes").glob("*.jsonl")):
        for line in open(f, encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                fixes.setdefault(d["gid"], {}).update(d)
    runs, flags = {}, []
    rr = ROOT / "index" / "run_results.tsv"
    if rr.exists():
        for row in csv.DictReader(open(rr, encoding="utf-8"), delimiter="\t"):
            if row["match"] and row["status"] == "ok":
                runs[row["gid"]] = int(row["match"])

    groups = defaultdict(list)
    for i, r in enumerate(recs):
        groups[find(i)].append(r)

    out = defaultdict(list)
    sizes = []
    used = set()
    for members in groups.values():
        members.sort(key=lambda r: (RANK[r["answer_source"]], r["type"] == "reveal", -int(r["term"][:4]), r["id"]))
        rep = members[0]
        gid = hashlib.sha1(key(rep).encode()).hexdigest()[:10] if rep["norm"] else hashlib.sha1(rep["id"].encode()).hexdigest()[:10]
        if gid in used:  # unmergeable twins (same text, image-only code) need their own id
            gid = hashlib.sha1(rep["id"].encode()).hexdigest()[:10]
        used.add(gid)
        g = {k: rep[k] for k in ("id", "week", "type", "context", "text", "code", "images", "crops", "options", "answer", "answer_source", "explanation", "file")}
        if rep.get("broken_image"):
            g["broken_image"] = True
        if rep.get("note"):
            g["note"] = rep["note"]
        g["gid"] = gid
        g["terms"] = sorted({m["term"] for m in members})
        g["members"] = [m["id"] for m in members]
        # review overlay: Claude's answer for unofficial groups, or a note on an official answer
        # reviews and fixes are keyed by a member's source id (stable) or, for older rows, by gid
        by_id = {m["id"]: m for m in members}

        def remap(idx, key):
            # answers were recorded against that member's option order; repeats can shuffle options
            src = by_id.get(key)
            if src is None or src is rep or not src["options"]:
                return idx
            pos = {norm(o["text"]): i for i, o in enumerate(rep["options"])}
            out = [pos.get(norm(src["options"][i]["text"])) for i in idx if i < len(src["options"])]
            return out if out and None not in out else idx

        rk = next((k for k in [gid, *g["members"]] if k in review), None)
        rw = review.get(rk)
        if rw:
            if rw.get("type"):
                g["type"] = rw["type"]
            if rw.get("answer") and g["answer_source"] != "official":
                g["answer"] = rw["answer"] if g["type"] == "numeric" else remap([int(x) for x in rw["answer"].split(",")], rk)
            if rw.get("badge") and g["answer_source"] != "official":
                g["answer_source"] = rw["badge"]
            if rw.get("note"):
                g["note"] = rw["note"]
            if g["type"] == "single" and isinstance(g["answer"], list) and len(g["answer"]) > 1:
                g["type"] = "multi"
        # fixes overlay: code/options/images recovered from screenshots or videos (source files stay untouched)
        fk = next((k for k in [gid, *g["members"]] if k in fixes), None)
        fx = fixes.get(fk)
        if fx:
            for k in ("text", "code", "images", "crops", "type", "note", "explanation"):
                if k in fx:
                    g[k] = fx[k]
            if "options" in fx:
                old = g["options"]
                # an option that is a picture keeps its picture; a recovered text description never replaces it
                g["options"] = [old[i] if i < len(old) and old[i].get("img") else {"text": t, "img": None}
                                for i, t in enumerate(fx["options"])]
            if "answer" in fx:
                g["answer"] = fx["answer"] if "options" in fx or not isinstance(fx["answer"], list) else remap(fx["answer"], fk)
                g["answer_source"] = fx.get("badge", "reviewed")
        if isinstance(g["answer"], list) and g["answer"] and (not g["options"] or max(g["answer"]) >= len(g["options"])):
            g["answer"], g["answer_source"] = [], "uploader"  # an option answer with no matching option is unusable
            if isinstance(g["answer"], list) and len(g["answer"]) > 1 and g["type"] == "single":
                g["type"] = "multi"
        # a clean run that matches exactly one option beats any unofficial answer; never overrides an official one
        run = runs.get(gid)
        if run is not None and g["type"] == "single":
            if g["answer_source"] in ("official", "pdf"):
                if g["answer"] != [run]:
                    flags.append(f"- `{gid}` ({rep['id']}): {g['answer_source']} answer {g['answer']} but running the code matches option {run}")
            else:
                if g["answer"] and g["answer"] != [run] and g["answer_source"] == "reviewed":
                    flags.append(f"- `{gid}` ({rep['id']}): reviewed answer {g['answer']} but running the code matches option {run}")
                g["answer"], g["answer_source"] = [run], "run"
        if g["type"] == "numeric" and g["text"]:
            # the uploader's typed entry would give the answer away once the card is answerable
            g["text"] = re.sub(r"\n?Answer (?:entered|box)[^\n]*", "", g["text"]).strip()
        g["code_html"] = hl(g["code"])
        if g["context"] and g["context"].get("code"):
            g["context"] = dict(g["context"], code_html=hl(g["context"]["code"]))
        g["options"] = [dict(o, code_html=hl(o["code"])) if o.get("code") else o for o in g["options"]]
        sizes.append(len(g["terms"]))
        out[g["week"]].append(g)

    for w, gs in out.items():
        gs.sort(key=lambda g: (-len(g["terms"]), g["id"]))
        (DATA / f"week-{w:02d}.json").write_text(json.dumps(gs, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    meta = {"weeks": {w: len(gs) for w, gs in sorted(out.items())}, "terms": sorted({r["term"] for r in recs})}
    (DATA / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    (ROOT / "index" / "official_notes.md").write_text(
        "# Answers to check: run result disagrees with the stored answer\n\n" + "\n".join(flags) + "\n", encoding="utf-8")

    nd = ["# Near-duplicates (same question text, different options) — kept separate", ""]
    nd += [f"- `{a}` vs `{b}`" for a, b in sorted(near)]
    (ROOT / "index" / "near_duplicates.md").write_text("\n".join(nd) + "\n", encoding="utf-8")
    multi = sum(1 for s in sizes if s > 1)
    print(f"{len(recs)} questions -> {len(sizes)} groups; {multi} groups appear in 2+ sessions; max {max(sizes)}; {len(near)} near-duplicate pairs")


if __name__ == "__main__":
    main()
