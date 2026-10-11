"""Helper for index/explain/week-NN.jsonl (see docs/EXPLAIN_BRIEF.md).

  python tools/explain_dump.py WEEK [START [COUNT]]   print pending trusted cards (those without an entry yet)
  python tools/explain_dump.py --check [WEEK]          validate the overlay against site/data (all weeks if omitted)
  python tools/explain_dump.py --write WEEK FILE       append the JSON-lines in FILE to the week's overlay (after checking them)

Snippets in a card's code are run with `python -I` (stdin closed, 5 s limit) and the output is printed next to the
card; a line "RUN MATCHES OPTION X" is added when stdout equals an option text.
"""
import json, subprocess, sys, tempfile
from urllib.parse import unquote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LET = "ABCDEFGH"
TRUSTED = ("official", "run", "reviewed")


def week(w):
    return json.loads((ROOT / "site" / "data" / f"week-{w:02d}.json").read_text(encoding="utf-8"))


def overlay(w):
    f = ROOT / "index" / "explain" / f"week-{w:02d}.jsonl"
    return [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()] if f.exists() else []


def eligible(g):
    return g["type"] != "reveal" and bool(g["answer"]) and g["answer_source"] in TRUSTED


def run(code):
    with tempfile.TemporaryDirectory() as d:
        try:
            p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=5, cwd=d, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            return None, "TIMEOUT"
        return p.stdout, p.stderr.strip().splitlines()[-1] if p.stderr.strip() else ""


_ctx = [None]


def show(n, g):
    print(f"=== Q{n} id={g['id']} type={g['type']} src={g['answer_source']} terms={len(g['terms'])}")
    c = g.get("context")
    if c and c == _ctx[0]:
        print("[ctx: same as the previous card]")
    elif c:
        _ctx[0] = c
        if c.get("text"):
            print("[ctx]", c["text"])
        if c.get("code"):
            print("[ctx code]\n" + c["code"])
        if c.get("images"):
            print("[ctx images]", c["images"])
    print("Q:", g["text"])
    if g["code"]:
        print("[code]\n" + g["code"])
    if g["images"]:
        print("[images]", g["images"])
    if g["stem"] or g["crops"]:
        print("[stem/crops]", g["stem"] or g["crops"])
    for i, o in enumerate(g["options"]):
        extra = (" [code] " + o["code"].replace("\n", "\\n")) if o.get("code") else ""
        extra += f" [img {unquote(o['img'])}]" if o.get("img") else ""
        print(f"  {LET[i]}. {o['text']}{extra}")
    ans = g["answer"]
    print("ANSWER:", ans if g["type"] == "numeric" else ",".join(LET[i] for i in ans))
    if g.get("note"):
        print("NOTE:", g["note"])
    if g.get("explanation"):
        print("PDF-EXPL:", g["explanation"])
    code = g["code"] or (c or {}).get("code")
    if code:
        out, err = run(code)
        if out is None:
            print("RUN: timeout")
        else:
            print("RUN stdout:", repr(out[:300]), "| err:", err[:200])
            norm = lambda s: " ".join(s.split())
            hit = [LET[i] for i, o in enumerate(g["options"]) if o["text"].strip("`' ") and norm(o["text"].strip("` ")) == norm(out)]
            if hit:
                print("RUN MATCHES OPTION", ",".join(hit), "(card answer", ",".join(LET[i] for i in ans) + ")" if g["type"] != "numeric" else ")")
    print()


def check(w, extra=None):
    cards = week(w)
    by = {}
    for g in cards:
        for m in g["members"]:
            by[m] = g
    errs, seen = [], set()
    for k, d in enumerate((extra if extra is not None else overlay(w)), 1):
        tag = f"w{w} #{k} {d.get('id')}"
        g = by.get(d.get("id"))
        if g is None:
            errs.append(f"{tag}: no such card"); continue
        if g["gid"] in seen:
            errs.append(f"{tag}: duplicate entry for card {g['gid']}")
        seen.add(g["gid"])
        if not eligible(g):
            errs.append(f"{tag}: card not eligible ({g['type']}, {g['answer_source']})")
        if not isinstance(d.get("why"), str) or not d["why"].strip():
            errs.append(f"{tag}: empty why")
        elif len(d["why"].split()) > 60:
            errs.append(f"{tag}: why has {len(d['why'].split())} words")
        ops = d.get("options", {})
        if g["type"] == "numeric" and ops:
            errs.append(f"{tag}: numeric card with options")
        right = {LET[i] for i in g["answer"]} if g["type"] != "numeric" else set()
        have = {LET[i] for i in range(len(g["options"]))}
        for l, t in ops.items():
            if l not in have:
                errs.append(f"{tag}: option {l} does not exist")
            elif l in right:
                errs.append(f"{tag}: option {l} is a correct answer")
            elif t is not None and (not isinstance(t, str) or len(t.split()) > 25):
                errs.append(f"{tag}: option {l} line too long/invalid ({len(str(t).split())} words)")
        if g["type"] != "numeric" and g["options"]:
            missing = have - right - set(ops)
            if missing:
                errs.append(f"{tag}: wrong options without a key (use null): {sorted(missing)}")
    return errs


def main():
    a = sys.argv[1:]
    if a and a[0] == "--check":
        ws = [int(a[1])] if len(a) > 1 else range(13)
        errs = [e for w in ws for e in check(w)]
        print("\n".join(errs) or "ok")
        sys.exit(1 if errs else 0)
    if a and a[0] == "--write":
        w = int(a[1])
        lines = [json.loads(l) for l in Path(a[2]).read_text(encoding="utf-8").splitlines() if l.strip()]
        done = {d["id"] for d in overlay(w)}
        errs = check(w, lines) + [f"{d['id']}: already has an entry" for d in lines if d["id"] in done]
        if errs:
            print("\n".join(errs)); sys.exit(1)
        f = ROOT / "index" / "explain" / f"week-{w:02d}.jsonl"
        f.parent.mkdir(exist_ok=True)
        with open(f, "a", encoding="utf-8", newline="\n") as fh:
            for d in lines:
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
        print(f"appended {len(lines)} to {f.name}")
        return
    w = int(a[0])
    start = int(a[1]) if len(a) > 1 else 1
    count = int(a[2]) if len(a) > 2 else 20
    sk = ROOT / "index" / "explain" / "skipped.tsv"  # id<TAB>reason: cards left unexplained on purpose (disagreements etc.)
    have = {d["id"] for d in overlay(w)} | ({l.split("	")[0] for l in sk.read_text(encoding="utf-8").splitlines()} if sk.exists() else set())
    cards = week(w)
    pending = [(n, g) for n, g in enumerate(cards, 1) if eligible(g) and not (set(g["members"]) & have)]
    skipped = [(n, g) for n, g in enumerate(cards, 1) if not eligible(g)]
    pending = [p for p in pending if p[0] >= start]
    print(f"# week {w}: {len(cards)} cards, {len(skipped)} skipped by rule, pending from Q{start}: {len(pending)}\n")
    for n, g in pending[:count]:
        show(n, g)


if __name__ == "__main__":
    main()
