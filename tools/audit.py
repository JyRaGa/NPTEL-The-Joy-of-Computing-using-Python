"""Flag suspect quiz cards in site/data/week-NN.json; writes docs/AUDIT.md.

Run after cluster.py. Every check is a heuristic: a flagged card is a candidate to look at, not a proven error.
Card numbers (Q1, Q2 ...) are positions in the site's default order ("Most repeated first", all sessions).
"""
import json, re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site" / "data"

IMAGE_WORD = re.compile(r"\b(images?|screenshots?)\b", re.I)
VISUAL_REF = re.compile(r"\b(figure|picture|diagram|shown (?:below|above)|given (?:below|image)|following (?:image|figure|output|graph|plot))\b", re.I)
PLACEHOLDER = re.compile(r"^\(?(question text in image|image|see image|no text)\)?\.?$", re.I)
JUNK_OPT = re.compile(r"funded by|swayam|nptel|1 point|accepted answers?|score:|unit\?|lesson=", re.I)
DANGLING = re.compile(r"(\b(the|of|a|an|to|and|or|is|in|for|with|by)|[,(\[{-])$", re.I)


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def base_id(i):
    return i.split("@")[0]


def has_visual(g):
    return bool(g["images"] or g["crops"] or g["code"] or any(o.get("img") for o in g["options"]))


def check(g):
    out = []
    text = g["text"] or ""
    t = text.strip()
    opts = g["options"]
    otexts = [norm(o["text"]) for o in opts]

    if PLACEHOLDER.match(t) or len(norm(t)) < 15:
        out.append(("high", "question text missing or a placeholder" + ("" if has_visual(g) else ", and no image or crop")))
    elif DANGLING.search(t) and not g["code"] and not g["images"] and not opts:
        out.append(("med", f"text looks cut off: ends with “…{t[-30:]}”"))
    if t.endswith(":") and not g["code"] and not g["images"] and not opts:
        out.append(("med", "text ends with ':' but nothing follows"))

    if IMAGE_WORD.search(text):
        out.append(("high" if not has_visual(g) else "low",
                    f"text mentions “{IMAGE_WORD.search(text).group(0)}”" + ("; no image, crop or code on the card" if not has_visual(g) else "; card has an image/crop, check it shows what the text describes")))
    elif VISUAL_REF.search(text) and not has_visual(g):
        out.append(("med", f"text refers to “{VISUAL_REF.search(text).group(0)}” but the card has no image, crop or code"))

    if g["type"] in ("single", "multi"):
        if len(opts) < 2:
            out.append(("high", f"{len(opts)} option(s) on a choice question"))
        if len(opts) > 6:
            out.append(("med", f"{len(opts)} options; probably merged or stray lines"))
        if any(not (opts[i]["text"] or "").strip() and not opts[i].get("img") and not opts[i].get("code") for i in range(len(opts))):  # raw text: "_" or "**" are real options
            out.append(("high", "an option is empty"))
        exact = [re.sub(r"\s+", " ", (o["text"] or "") + "|" + (o.get("code") or "") + "|" + (o.get("img") or "")).strip() for o in opts]  # case matters: %c vs %C
        dup = {o.strip("|") for o in exact if o.strip("|") and exact.count(o) > 1}
        if dup:
            out.append(("high", f"identical options: {', '.join(sorted(dup))[:60]}"))
        ph = [i for i, o in enumerate(opts) if re.fullmatch(r"option \d+", otexts[i]) and not o.get("img") and not o.get("code")]
        if ph and not g["images"] and not g["crops"]:
            out.append(("high", "options are 'Option N' placeholders with no picture, code or crop"))
        junk = [o["text"][:40] for o in opts if JUNK_OPT.search(o["text"]) or (len(o["text"]) > 300 and chr(10) not in o["text"])]  # multi-line options are code blocks
        if junk:
            out.append(("high", f"option looks like stray page text: “{junk[0]}”"))
        ans = g["answer"] if isinstance(g["answer"], list) else []
        if not ans:
            out.append(("low", "no answer"))
    if g.get("broken_image") and not g["images"] and not g["crops"]:  # a screenshot on the card replaces the lost embed
        out.append(("high", "source image link is broken"))
    return out


def main():
    rows = defaultdict(list)
    for f in sorted(DATA.glob("week-*.json")):
        w = int(f.stem[-2:])
        gs = json.loads(f.read_text(encoding="utf-8"))
        pos = {g["gid"]: i + 1 for i, g in enumerate(gs)}
        for g in gs:
            for sev, msg in check(g):
                rows[w].append((sev, pos[g["gid"]], g, msg))
        # duplicates that cluster.py kept apart
        for i, a in enumerate(gs):
            na = norm(a["text"])
            for b in gs[i + 1:]:
                nb = norm(b["text"])
                same_src = {base_id(m) for m in a["members"]} & {base_id(m) for m in b["members"]}
                if same_src:
                    rows[w].append(("high", pos[b["gid"]], b, f"same source question as Q{pos[a['gid']]} (`{sorted(same_src)[0]}`): two copies of one question"))
                    continue
                if len(na) < 20 or len(nb) < 20 or (a["code"] or "") != (b["code"] or "") or a["images"] != b["images"] or a["crops"] != b["crops"]:
                    continue  # same stem over different code or pictures is a different question
                contained = na in nb or nb in na
                if contained or SequenceMatcher(None, na, nb, autojunk=False).ratio() >= 0.9:
                    same_opts = sorted(norm(o["text"]) for o in a["options"]) == sorted(norm(o["text"]) for o in b["options"])
                    if same_opts:
                        rows[w].append(("high", pos[b["gid"]], b, f"duplicate of Q{pos[a['gid']]}: same options, text {'contained in the other' if contained else '≥90% similar'}"))
                    elif contained and min(len(na), len(nb)) >= 60:
                        rows[w].append(("low", pos[b["gid"]], b, f"text overlaps Q{pos[a['gid']]} with different options: repeat with changed options, or a mis-merge"))

    order = {"high": 0, "med": 1, "low": 2}
    total = {s: sum(1 for r in rows.values() for x in r if x[0] == s) for s in order}
    md = ["# Content audit of the quiz cards", "",
          "Generated by `python tools/audit.py` from `site/data/week-NN.json`. Re-run it after every fix. How to fix each kind of flag: [AUDIT_BRIEF.md](AUDIT_BRIEF.md).",
          "",
          "Each line: severity, card number in the site's default view (all sessions, most repeated first), what looks wrong, the card's first source id and source file.",
          "These are heuristics: a flag means \"look at this\", not \"this is wrong\".",
          "",
          f"**{total['high']} high · {total['med']} medium · {total['low']} low**",
          ""]
    for w in sorted(rows):
        items = sorted(rows[w], key=lambda r: (order[r[0]], r[1]))
        md += [f"## Week {w}", ""]
        for sev, n, g, msg in items:
            md.append(f"- **{sev}** · Q{n} · {msg} · `{g['id']}` · `{g['file']}`")
        md.append("")
    (ROOT / "docs" / "AUDIT.md").write_text("\n".join(md), encoding="utf-8")
    print(f"docs/AUDIT.md: {total}")


if __name__ == "__main__":
    main()
