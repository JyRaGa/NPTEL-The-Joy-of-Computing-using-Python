"""List still-unverified questions (uploader-only answer, or no answer at all) for some sessions.

Usage: python tools/gaps.py TERM [TERM ...]      e.g. python tools/gaps.py 2023-jul
Prints gid, week, type, source file:line hint, current text/code/options, images and portal crops.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
L = "ABCDEFGH"
terms = set(sys.argv[1:])
for f in sorted((ROOT / "site" / "data").glob("week-*.json")):
    for g in json.loads(f.read_text(encoding="utf-8")):
        if g["id"].split("/")[0] not in terms:
            continue
        if not (g["answer_source"] == "uploader" or not g["answer"]):
            continue
        a = g["answer"]
        a = ",".join(L[i] for i in a) if isinstance(a, list) else a
        print(f"## {g['gid']} week={g['week']} {g['type']} ans={a or '-'} src={g['id']} file={g['file']}")
        print(g["text"][:400])
        if g["code"]:
            print("CODE:", g["code"][:500])
        for p in g["images"] + g["crops"]:
            print("IMG:", p)
        for i, o in enumerate(g["options"]):
            print(f"  {L[i]}) {o['text'][:140]}" + (f" IMG:{o['img']}" if o["img"] else ""))
