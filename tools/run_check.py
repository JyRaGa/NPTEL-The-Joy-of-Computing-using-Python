"""Run each code question's snippet and match its output to exactly one option.

Writes index/run_results.tsv (gid, week, matched option index, output, stored answer).
Only snippets without input()/files/network/randomness are run, each in its own subprocess with a timeout.
Usage: python tools/run_check.py [week ...]
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "site" / "data"
SKIP = re.compile(r"\binput\s*\(|open\s*\(|import\s+(os|sys|subprocess|socket|requests|urllib|selenium|turtle|random|time|tkinter|cv2|PIL|matplotlib|speech|nltk|networkx|gmplot)|from\s+(os|random|turtle|selenium|PIL)\b|while\s+True", re.I)


def squash(s):
    return re.sub(r"[\s'\"]+", "", s).lower()


def run(code):
    try:
        p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True, timeout=5)
    except subprocess.TimeoutExpired:
        return None, "timeout"
    if p.returncode:
        return p.stdout, "error: " + (p.stderr.strip().splitlines() or ["?"])[-1]
    return p.stdout, "ok"


def main():
    weeks = [int(w) for w in sys.argv[1:]] or range(13)
    rows = ["gid\tweek\tmatch\tstatus\tstored\toutput"]
    hit = 0
    for w in weeks:
        f = DATA / f"week-{w:02d}.json"
        if not f.exists():
            continue
        for g in json.loads(f.read_text(encoding="utf-8")):
            code = g["code"] or (g["context"] or {}).get("code")
            if not code or g["type"] not in ("single", "multi") or SKIP.search(code):
                continue
            out, status = run(code)
            match = ""
            if status.startswith("error"):
                # "Error" options are the answer when the snippet raises
                errs = [i for i, o in enumerate(g["options"]) if re.search(r"\berror\b|exception", o["text"], re.I)]
                if len(errs) == 1 and not (out or "").strip():
                    match = str(errs[0])
            elif out is not None and out.strip():
                so = squash(out)
                cand = [i for i, o in enumerate(g["options"]) if o["text"] and squash(o["text"]) == so]
                if len(cand) == 1:
                    match = str(cand[0])
            if match:
                hit += 1
            rows.append("\t".join([g["gid"], str(w), match, status, ",".join(map(str, g["answer"])) if isinstance(g["answer"], list) else str(g["answer"]),
                                   (out or "").strip().replace("\n", "\\n").replace("\t", " ")[:200]]))
    (ROOT / "index" / "run_results.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"ran {len(rows) - 1} snippets, {hit} matched exactly one option")


if __name__ == "__main__":
    main()
