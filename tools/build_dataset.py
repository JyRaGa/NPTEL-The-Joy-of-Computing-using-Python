"""Parse every quiz file in sources/inventory.tsv into site/data/questions.json.

Text, options and code are kept verbatim; only `norm` (used for matching) is normalised.
Writes index/mismatch_report.md for files whose question count looks wrong.
Run from anywhere: python tools/build_dataset.py
"""
import unicodedata
import csv, json, re, posixpath, textwrap
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "data"
REPORT = ROOT / "index" / "mismatch_report.md"

HEAD = {
    "portal_print_parsed": re.compile(r"^###\s*Q(\d+)\.\s*(.*)"),
    "youtube_transcription": re.compile(r"^\*\*(\d+)\)\s*(.*)"),
    "second_repo_md": re.compile(r"^\*\*(\d+)\.\s*(.*)"),
    "chatgpt_converted_md": re.compile(r"^(\d+)\.\s+(.*)"),
    "case_study_pdf_md": re.compile(r"^###\s*(?:Q|Question\s*|MCQ\s*|MSQ\s*)(\d+)\.?\s*(.*)"),
}
TICK = re.compile(r"^\s*- \[( |x|X)\]\s?(.*)")
PLAIN_OPT = re.compile(r"^\s*- (.*)")
LETTER_OPT = re.compile(r"^\s*-\s*([A-H])[.)]\s*(.*)")
MD_IMG = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_IMG = re.compile(r"<img[^>]*src=\"([^\"]+)\"", re.I)
NUMERIC = re.compile(r"^Accepted answer\(s\):\s*\(Type:\s*(\w+)\)\s*(.*)", re.I)
ANSWER = re.compile(r"^\*\*(?:Correct\s+)?Answers?:\s*([A-H](?:\s*[,&and ]+\s*[A-H])*)\*\*", re.I)
PAGE_STAMP = re.compile(r"^\w+day \d+ \w+ \d{4} \d+:\d+ [AP]M\s*")
MARK = re.compile(r"\s*(✅|✓|✔)\s*$")


def strip_md(s):
    s = re.sub(r"\*\*$", "", s.strip())
    return s.strip()


def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()  # fold ligatures (ﬁ) so portal prints match typed copies
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def img_path(src, md_file):
    if src.startswith("http"):
        return src
    return posixpath.normpath(posixpath.join(posixpath.dirname(md_file), src))


def parse_file(rel, kind):
    lines = (ROOT / rel).read_text(encoding="utf-8").splitlines()
    head = HEAD[kind]
    qs, cur, in_code, context, sink = [], None, False, None, None
    # YouTube files put shared scenario text / "Code for question 5 & 6" between questions
    pending = {"text": [], "code": []}
    yt = kind == "youtube_transcription"
    for raw in lines:
        line = raw.rstrip()
        between = yt and (cur is None or cur["options"])
        if in_code:
            if line.lstrip().startswith("```"):
                in_code = False
            elif sink is not None:
                sink.append(raw)
            continue
        if line.lstrip().startswith("```"):
            in_code = True
            if cur and cur["options"] and raw[:1] in " 	":
                sink = cur["options"][-1].setdefault("code", [])  # code block indented under an option
            else:
                sink = pending["code"] if between else (cur["code"] if cur else None)
            if sink:
                sink.append("")  # second code block in one question
            continue
        # Jul-2019 style files: only the first section is the question list
        if yt and line.startswith("## ") and qs:
            break
        if kind == "case_study_pdf_md" and line.startswith(("## Scenario", "## Case Study")):
            context = {"text": re.sub(r"^## (?:Scenario|Case Study):?\s*", "", line).strip(), "code": None, "only": None}
            cur = None
            continue
        m = head.match(line)
        # numbered sub-steps inside a question body ("1) Implement Game Loop") are not new questions
        if m and kind != "case_study_pdf_md" and cur and not cur["options"] and int(m.group(1)) != cur["num"] + 1:
            m = None
        if m and not (kind == "chatgpt_converted_md" and raw.startswith(" ")):
            num = len(qs) + 1 if kind == "case_study_pdf_md" else int(m.group(1))
            if pending["text"] or pending["code"]:
                t = "\n".join(pending["text"])
                only = re.search(r"questions?\s+([\d\s,&and-]+)", t, re.I)
                context = {"text": t, "code": textwrap.dedent("\n".join(pending["code"])).strip("\n") or None,
                           "only": [int(n) for n in re.findall(r"\d+", only.group(1))] if only else None}
                if pending.get("images"):
                    context["images"] = pending["images"]
                pending = {"text": [], "code": []}
            ctx = context if context and (context["only"] is None or num in context["only"]) else None
            cur = {"num": num, "text": [re.sub(r"^\(M[CS]Q\)\s*", "", strip_md(m.group(2)))], "code": [], "options": [],
                   "answer": [], "images": [], "crops": [], "numeric": None, "explanation": None,
                   "context": ctx, "open_bold": kind in ("youtube_transcription", "second_repo_md") and not m.group(2).rstrip().endswith("**")}
            qs.append(cur)
            continue
        if between and line.startswith("**") and line.endswith("**") and len(line) > 4:
            pending["text"].append(line.strip("*").strip())
            continue
        # 2024-jan: the scene picture under a "Problem Introduction" header belongs to the scenario, not the question above it
        if between and pending["text"] and MD_IMG.search(line):
            pending.setdefault("images", []).extend(img_path(p, rel) for p in MD_IMG.findall(line))
            continue
        if cur is None:
            # 2026-jul: the scenario's program is an image placed before Q1
            if context is not None and MD_IMG.search(line):
                context.setdefault("images", []).extend(img_path(p, rel) for p in MD_IMG.findall(line))
            continue
        s = line.strip()
        if not s or s.startswith("> Yes") or s.startswith("> No") or s.startswith("Score:"):
            continue
        if "[[Pasted image" in s:  # broken Obsidian embed from the ChatGPT conversion
            cur["broken_image"] = True
            continue
        imgs = [img_path(p, rel) for p in MD_IMG.findall(s) + HTML_IMG.findall(s)]
        if s.startswith("![page crop]"):
            cur["crops"] += imgs
            continue
        nm = NUMERIC.match(s)
        if nm:
            cur["numeric"] = nm.group(2).strip()
            continue
        am = ANSWER.match(s)
        if am:
            cur["answer"] = ["ABCDEFGH".index(c) for c in re.findall(r"\b[A-H]\b", am.group(1).upper())]  # "C and D": the A of "AND" is not an option
            continue
        if s.startswith("> Justification:") or s.startswith("> Explanation:"):
            cur["explanation"] = re.sub(r"^> \w+:\s*", "", s)
            continue
        if s.startswith(">") and cur["explanation"] is not None:
            cur["explanation"] += "\n" + s.lstrip("> ")
            continue
        opt = None
        if kind in ("portal_print_parsed", "youtube_transcription"):
            t = TICK.match(line)
            if t:
                opt = (t.group(2), t.group(1) != " ")
        elif kind == "second_repo_md":
            p = PLAIN_OPT.match(line)
            if p and not line.startswith("  "):
                body = p.group(1)
                opt = (MARK.sub("", body), bool(MARK.search(body)))
        elif kind == "chatgpt_converted_md":
            p = LETTER_OPT.match(line) or PLAIN_OPT.match(line)  # "- A) text ✓" or "- text ✓"
            if p:
                body = p.group(p.lastindex)
                opt = (MARK.sub("", body), bool(MARK.search(body)))
            elif s.lower().startswith("correct answer"):
                letters = re.findall(r"\b([A-H])\)", s)
                if letters:
                    cur["answer"] = ["ABCDEFGH".index(c) for c in letters]
                continue
        elif kind == "case_study_pdf_md":
            p = LETTER_OPT.match(line)
            if p:
                opt = (p.group(2), False)
        if opt is not None:
            text, ticked = opt
            text = PAGE_STAMP.sub("", text)  # 2018 portal printout page header leaks into options
            if not text.strip():
                continue
            o_imgs = [img_path(p, rel) for p in MD_IMG.findall(text) + HTML_IMG.findall(text)]
            text = re.sub(r"<img[^>]*>", "", MD_IMG.sub("", text)).strip()
            cur["options"].append({"text": text.rstrip("\\").rstrip(), "img": o_imgs[0] if o_imgs else None})
            if ticked:
                cur["answer"].append(len(cur["options"]) - 1)
            cur["open_bold"] = False
            continue
        if cur["options"] and raw.startswith("  ") and not imgs:
            # continuation of a multi-line option (second repo uses trailing "\")
            o = cur["options"][-1]
            o["text"] = (o["text"] + "\n" + s.rstrip("\\").rstrip()).strip()
            m2 = MARK.search(s)
            if m2:
                o["text"] = MARK.sub("", o["text"])
                cur["answer"].append(len(cur["options"]) - 1)
            continue
        if imgs:
            if "Pasted image" in s:
                cur["broken_image"] = True
            else:
                cur["images"] += imgs
            continue
        if "[[Pasted image" in s:
            cur["broken_image"] = True
            continue
        if not cur["options"]:
            cur["text"].append(s.strip("*").strip() if s.startswith("**") and s.endswith("**") else (strip_md(s) if cur["open_bold"] else s))
            if s.endswith("**"):
                cur["open_bold"] = False
    return qs


def finish(q, row):
    text = "\n".join(t for t in q["text"] if t).strip()
    code = textwrap.dedent("\n".join(q["code"])).strip("\n") or None
    answer = sorted(set(q["answer"]))
    if q["numeric"]:
        qtype = "numeric"
    elif not q["options"]:
        qtype = "reveal"
    elif len(answer) > 1:
        qtype = "multi"
    else:
        qtype = "single"
    for o in q["options"]:
        if "code" in o:
            o["code"] = textwrap.dedent("\n".join(o["code"])).strip("\n")
    term, week = row["term"], int(row["week"])
    src = "portal" if row["path"].endswith("-portal-print.md") else "main"
    rec = {
        "id": f"{term}/w{week:02d}/q{q['num']:02d}" + ("@portal" if src == "portal" else "@gpt" if row["kind"] == "chatgpt_converted_md" else ""),
        "term": term, "week": week, "num": q["num"], "file": row["path"], "kind": row["kind"],
        "type": qtype, "context": {k: v for k, v in q["context"].items() if k != "only"} if q["context"] else None, "text": text, "code": code,
        "images": q["images"], "crops": q["crops"], "options": q["options"],
        "answer": q["numeric"] if qtype == "numeric" else answer,
        "answer_source": "official" if row["kind"] == "portal_print_parsed" or (row["kind"] == "case_study_pdf_md" and week <= 10)
                         else "reviewed" if row["kind"] == "case_study_pdf_md" else "uploader",  # Jul-2026 PDFs: weeks 1-10 carry the official key, 11-12 the owner's answers
        "explanation": q["explanation"],
        "norm": norm(text + " " + (code or "")),
        "norm_options": sorted(norm(o["text"]) for o in q["options"]),
    }
    if q.get("broken_image"):
        rec["broken_image"] = True
    # Jul-2019: the files' "Official accepted answers" sections confirm every tick except these
    if term == "2019-jul" and row["kind"] == "youtube_transcription" and (week, q["num"]) not in JUL19_NOT_SHOWN:
        fix = JUL19_FIX.get((week, q["num"]))
        if fix:
            rec["answer"] = [i for i, o in enumerate(q["options"]) if o["text"].strip().startswith(fix)]
        if rec["answer"]:
            rec["answer_source"] = "official"
        if (week, q["num"]) in JUL19_ZERO:
            rec["note"] = "NPTEL scored this question 0 for everyone (zero-weighted), most likely because the question as set was broken."
    return rec


JUL19_NOT_SHOWN = {(2, 9), (2, 10), (4, 8), (4, 9), (7, 8), (11, 9), (11, 10)}
JUL19_FIX = {(1, 2): "False", (5, 1): "Divide and conquer", (12, 3): "Rank of pages"}
JUL19_ZERO = {(6, 5), (12, 6)}


def main():
    rows = list(csv.DictReader(open(ROOT / "sources" / "inventory.tsv", encoding="utf-8"), delimiter="\t"))
    records, problems = [], []
    for row in rows:
        qs = parse_file(row["path"], row["kind"])
        recs = [finish(q, row) for q in qs]
        expected = {"portal_print_parsed": 10, "case_study_pdf_md": 20}.get(row["kind"])
        nums = [r["num"] for r in recs]
        issues = []
        if not recs:
            issues.append("no questions parsed")
        elif not expected and len(recs) < 8:
            issues.append(f"only {len(recs)} questions")
        elif expected and len(recs) != expected:
            issues.append(f"{len(recs)} questions, expected {expected}")
        dup = [n for n, c in Counter(nums).items() if c > 1]
        if dup:
            issues.append(f"duplicate numbers {dup}")
        no_ans = [r["num"] for r in recs if r["type"] != "reveal" and not r["answer"]]
        if no_ans:
            issues.append(f"no answer: Q{', Q'.join(map(str, no_ans))}")
        reveal = [r["num"] for r in recs if r["type"] == "reveal"]
        if reveal:
            issues.append(f"no parsed options (reveal): Q{', Q'.join(map(str, reveal))}")
        if issues:
            problems.append((row["path"], issues))
        records += recs
    records.sort(key=lambda r: (r["week"], r["term"], r["id"]))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "questions.json").write_text(json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8")
    REPORT.parent.mkdir(exist_ok=True)
    types = Counter(r["type"] for r in records)
    srcs = Counter(r["answer_source"] for r in records)
    out = ["# Parse mismatch report", "", f"{len(records)} questions from {len(rows)} files. Types: {dict(types)}. Answer sources: {dict(srcs)}.", "",
           f"{len(problems)} files with issues:", ""]
    for path, issues in problems:
        out.append(f"- `{path}`: " + "; ".join(issues))
    REPORT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(out[2])
    print(f"{len(problems)} files with issues -> {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
