"""Cut picture options out of portal page crops, for cards whose options were pictures but were typed up as summaries.

Boxes were measured by hand on each page (left, top, right, bottom in crop pixels). Writes quizzes/<term>/img/opts/<card>-<letter>.png
and index/fixes/optimg.jsonl, which cluster.py lays over the typed options (an option given as a string stays text).
"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
BOXES = {
    "2018-jul/w01/q09@portal": [("w01-q09-p3", (66, 56, 602, 212)), ("w01-q09-p3", (66, 210, 568, 310)), ("w01-q09-p3", (66, 310, 550, 459)), "None of the above"],
    "2020-jan/w01/q01": [("w01-q01-p1", (66, 93, 277, 184)), ("w01-q01-p1", (64, 196, 274, 327)), ("w01-q01-p1", (64, 336, 274, 485)), ("w01-q01-p2", (58, 56, 268, 320))],
    "2020-jan/w01/q07": [("w01-q07-p4", (64, 86, 337, 400)), ("w01-q07-p4", (56, 400, 334, 714)), ("w01-q07-p4", (62, 716, 340, 1030)), ("w01-q07-p5", (60, 56, 336, 374))],
    "2020-sep/w01/q05": [("w01-q05-p3", (68, 56, 580, 524)), ("w01-q05-p3", (72, 532, 586, 1020)), ("w01-q05-p4", (78, 72, 590, 512)), ("w01-q05-p4", (62, 526, 576, 1034))],
    "2020-sep/w01/q07": [("w01-q07-p6", (76, 92, 588, 660)), ("w01-q07-p7", (80, 58, 590, 640)), ("w01-q07-p7", (58, 642, 570, 1240)), ("w01-q07-p8", (64, 66, 580, 640))],
    "2024-jul/w01/q02": [("w01-q02-p7", (50, 60, 310, 340)), ("w01-q02-p7", (50, 360, 310, 635)), ("w01-q02-p8", (70, 50, 330, 305)), ("w01-q02-p8", (70, 368, 330, 500))],
    "2024-jul/w01/q09": [("w01-q09-p13", (45, 55, 905, 405)), ("w01-q09-p14", (45, 55, 650, 795)), ("w01-q09-p15", (45, 45, 905, 365)), ("w01-q09-p15", (60, 405, 905, 715))],
    "2025-jan/w01/q02": [("w01-q02-p1", (70, 42, 330, 220)), ("w01-q02-p1", (66, 230, 320, 388)), ("w01-q02-p2", (73, 82, 320, 262)), ("w01-q02-p2", (73, 262, 320, 438))],
    "2025-jan/w01/q09": [("w01-q09-p5", (40, 110, 928, 630)), ("w01-q09-p5", (40, 652, 928, 1176)), ("w01-q09-p5", (40, 1192, 928, 1712)), ("w01-q09-p6", (24, 110, 928, 628))],
    "2020-sep/w02/q04": [("w02-q04-p13", (47, 255, 108, 275)), ("w02-q04-p13", (47, 292, 108, 317)), ("w02-q04-p13", (47, 339, 100, 366)), ("w02-q04-p13", (47, 384, 93, 412))],
    "2020-sep/w02/q06": [("w02-q06-p14", (80, 315, 410, 377)), ("w02-q06-p14", (80, 389, 410, 452)), ("w02-q06-p14", (80, 487, 410, 550)), ("w02-q06-p14", (72, 572, 410, 634))],
    "2020-jan/w08/q05": [("w08-q05-p51", (62, 710, 222, 829)), ("w08-q05-p51", (60, 846, 218, 964)), ("w08-q05-p52", (62, 61, 219, 179)), ("w08-q05-p52", (62, 188, 220, 306))],
    "2020-jan/w08/q06": [("w08-q06-p52", (70, 668, 228, 784)), ("w08-q06-p53", (64, 64, 222, 180)), ("w08-q06-p53", (58, 194, 214, 310)), ("w08-q06-p53", (64, 324, 216, 441))],
}
# cards that had no options parsed at all also need the key from the page's "Accepted Answers"
EXTRA = {
    "2020-sep/w02/q04": {"type": "single"},  # the source lists every option twice and ticks both copies
    "2020-sep/w02/q06": {"type": "single", "answer": [2], "badge": "official"},
    "2020-jan/w08/q05": {"type": "single", "answer": [1], "badge": "official"},
    "2020-jan/w08/q06": {"type": "single", "answer": [3], "badge": "official"},
}


def main():
    rows = []
    for card, opts in BOXES.items():
        term = card.split("/")[0]
        out = []
        for letter, o in zip("ABCD", opts):
            if isinstance(o, str):
                out.append(o)
                continue
            page, box = o
            dst = ROOT / "quizzes" / term / "img" / "opts" / f"{card.split('/', 1)[1].replace('/', '-').replace('@portal', '')}-{letter}.png"
            dst.parent.mkdir(exist_ok=True)
            Image.open(ROOT / "quizzes" / term / "img" / f"{page}.png").crop(box).save(dst)
            out.append({"text": "", "img": dst.relative_to(ROOT).as_posix()})
        rows.append({"gid": card, "options": out, **EXTRA.get(card, {})})
    (ROOT / "index" / "fixes" / "optimg.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    print(f"{sum(isinstance(o, dict) for r in rows for o in r['options'])} option pictures for {len(rows)} cards")


if __name__ == "__main__":
    main()
