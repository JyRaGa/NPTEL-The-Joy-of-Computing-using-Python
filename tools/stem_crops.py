"""Cut portal-page crops above the first option radio, for cards whose stem says "the following code" but carry no code.

The full crop also prints "Accepted Answers", so it cannot be shown before the user answers. Writes <crop>-stem.png next to
each crop; cluster.py attaches them as g["stem"]. Run after cluster.py, then run cluster.py again.
"""
import json, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
POINTS_AT = re.compile(r"\b(following|below|given|above)\b", re.I)
GREY = range(110, 230)
OVERRIDES = ROOT / "index" / "stem_overrides.json"  # {crop path: y to cut at | [top, bottom] | null = no stem from this crop}, checked before the heuristic


def first_radio(im):
    """(y, x) of radio rings: grey left/right edges d px apart (11-22, portal styles differ), white centre, for 7+ rows."""
    W, H = im.size
    px = im.load()
    for d in range(11, 23):
        for x0 in range(5, min(160, W - d - 5)):
            run = 0
            for y in range(H):
                ring = (px[x0, y] in GREY or px[x0 + 1, y] in GREY) and (px[x0 + d, y] in GREY or px[x0 + d - 1, y] in GREY)                     and px[x0 - 3, y] > 235 and px[x0 + d + 3, y] > 235
                run = run + 1 if ring else 0
                if run >= 6:
                    yield y - run - 5, x0
                    break


def ink_rows(im):
    """rows holding anything darker than light grey: a question's own text is a few lines, a code block or figure is many"""
    px, W = im.load(), im.width
    return sum(1 for y in range(im.height) if any(px[x, y] < 200 for x in range(0, W, 2)))


def tidy(im, top=False):
    """trim blank space at the bottom, a stray footer line, and (on continuation pages, top=True) the PDF running header"""
    g = im.convert("L"); px = g.load()
    rows = [y for y in range(g.height) if any(px[x, y] < 200 for x in range(0, g.width, 2))]
    if not rows:
        return im.crop((0, 0, im.width, 1))
    bands, start = [], rows[0]
    for a, b in zip(rows, rows[1:] + [None]):
        if b is None or b - a > 1:
            bands.append((start, a)); start = b
    if len(bands) > 1 and bands[-1][1] - bands[-1][0] < 16 and bands[-1][0] - bands[-2][1] > 30:
        bands.pop()
    y0 = 0
    if top and len(bands) > 1 and bands[0][1] - bands[0][0] < 16 and bands[1][0] - bands[0][1] > 30:
        y0 = bands[1][0] - 8
    return im.crop((0, y0, im.width, min(im.height, bands[-1][1] + 8)))


FIGURE = 80  # ink rows; 3 wrapped text lines at 130 dpi are ~45


def bands(g):
    px = g.load()
    rows = [y for y in range(g.height) if any(px[x, y] < 200 for x in range(0, g.width, 2))]
    out = []
    for y in rows:
        if out and y - out[-1][1] <= 2:
            out[-1][1] = y
        else:
            out.append([y, y])
    return out


def radio_y(im):
    hits = [(y, x) for y, x in first_radio(im) if 20 < y < im.height - 25]  # letters in the title line and rings cut by the page edge are not radios
    if not hits:
        return None
    left = min(x for _, x in hits)  # option radios sit in the left-most column; rings inside figures are further right
    return min(y for y, x in hits if x <= left + 3)


def cut_at(im):
    """(cut y, options reached?): below the question's own figure, else just above the first option.
    A figure beside the first radio is an option picture, so the cut goes above it."""
    r = radio_y(im)
    tall = [b for b in bands(im) if b[1] - b[0] >= 50]
    before = [b for b in tall if r is None or b[1] < r]
    if before:
        return before[0][1] + 8, True
    if r is None:
        return None, False
    beside = [b for b in tall if b[0] <= r <= b[1]]
    return (beside[0][0] - 4 if beside else r), True


def bare(g):
    c = g.get("context") or {}
    return not (g["code"] or g["images"] or c.get("code") or c.get("images") or any(o.get("img") or o.get("code") for o in g["options"]))


def main(weeks=None):
    """weeks: optional list of week numbers; only those are deleted and rewritten (a full run takes minutes)"""
    ov = json.loads(OVERRIDES.read_text(encoding="utf-8")) if OVERRIDES.exists() else {}
    tag = [f"w{w:02d}-" for w in weeks] if weeks is not None else None
    for old in ROOT.glob("quizzes/*/img/**/*-stem.png"):
        if tag is None or old.name.startswith(tuple(tag)):
            old.unlink()
    made, missed, text_only = 0, [], 0
    for f in sorted((ROOT / "site" / "data").glob("week-*.json")):
        if weeks is not None and int(f.stem[5:]) not in weeks:
            continue
        for g in json.loads(f.read_text(encoding="utf-8")):
            forced = any(isinstance(ov.get(p), (int, list)) for p in g["crops"])
            if not (bare(g) and g["crops"] and (forced or POINTS_AT.search(g["text"] or ""))):
                continue
            stems, skipped = [], False  # (path, image) of everything above the first option radio
            for p in g["crops"]:
                im = Image.open(ROOT / p)
                if p in ov and ov[p] is None:
                    skipped = True
                    continue
                top, cut = ov[p] if isinstance(ov.get(p), list) else (0, ov.get(p))  # [top, bottom]: keep only that band (a figure under a page header)
                y, done = (cut, cut < im.height) if p in ov else cut_at(im.convert("L"))  # cutting at the full height = the stem goes on onto the next crop
                stems.append((p, im if y is None else im.crop((0, top, im.width, max(y, top)))))
                if done:
                    break
            else:
                if not skipped:
                    missed.append(g["id"])
                    continue
            stems = [(p, tidy(im, top=k > 0)) for k, (p, im) in enumerate(stems)]
            stems = [(p, im) for p, im in stems if im.height > 20 and (ink_rows(im.convert("L")) > 10 or isinstance(ov.get(p), list))]  # drop blank page tails
            if not any(b[1] - b[0] >= 50 for _, im in stems for b in bands(im.convert("L"))) and not forced:
                text_only += 1  # the stem is just the question's own words
                continue
            for p, im in stems:
                src = ROOT / p
                im.save(src.with_name(src.stem + "-stem.png"))
                made += 1
    print(f"{made} stem crops written; {text_only} cards are text only; no option radio found for {len(missed)}: {missed}")


if __name__ == "__main__":
    main([int(a) for a in sys.argv[1:]] or None)  # python tools/stem_crops.py 2 3
