# Brief: show the missing code/figure on "following code" cards (Weeks 0–12)

Paste this as the task for a fresh session (Sonnet, high effort). Work in the repo root (`JRG JOC/`). Week 1 is already done and checked; use it as the reference for what "right" looks like.

## The problem

Many cards say "What is the output of the following code?", "the following instructions", "the block below", "the given graph", but show **no code and no picture**. The text was parsed from NPTEL portal printouts, and the code/Scratch blocks/graphs were images on the page, so they were lost. The full page image of each question exists (`crops` in the card, e.g. `quizzes/2020-jan/img/w02-q05-p4.png`), but it is only shown collapsed under "Original portal page" **after the options**, and it also prints the **Accepted Answer**, so it cannot simply be shown as-is.

Known affected: Week 2 Q40, Q41, Q42, Q44, Q45 and onwards (mostly Jan 2020, Sep 2020, Jan 2021, Jan 2025, Jul 2024), and the same pattern in every other week.

## What already exists (do not rebuild it)

- `tools/stem_crops.py` finds such cards and writes `<crop>-stem.png` next to each crop: the page cut **below the question's own figure and above the options**, so no answer is visible. It runs over all weeks.
- `tools/cluster.py` attaches existing `-stem.png` files to the card as `g["stem"]`; `site/app.js` shows `g.stem` inline right under the question text (and then hides the collapsed full-page copy).
- Pipeline after any change: `python tools/stem_crops.py` → `python tools/cluster.py` → `python tools/audit.py`. If you edit a source `.md`, run `python tools/build_dataset.py` and `python tools/run_check.py` first.

The script is a heuristic (cuts after the first tall ink block, or above the first option radio). It is right for most cards but fails on some layouts. **Do not keep tuning the global heuristic**: every tweak broke other cards in Week 1. Fix the leftovers per card instead (see "Manual overrides").

## What "right" looks like for each card

1. Under the question text: the question title line plus the code / Scratch blocks / graph / figure the stem refers to, and **nothing below it**: no option radios, no option text, no "Yes/No, the answer is…", no "Score", no "Accepted Answers".
2. No blank or near-blank images (a page tail with only a footer line, or an empty continuation page).
3. No PDF running header ("The Joy of Computing using Python - - Unit N - Week N") at the top of a continuation picture.
4. **Cards whose pictures ARE the answer options** ("Which of the following blocks…", graph options, flowchart options) must get **no** stem picture: the options are pictures, and showing the first one as "the code" is wrong. Leave those as they are.
5. Cards whose stem is complete as text ("Which of the following is true?") get nothing.
6. When a question's code was printed as text (not an image), the stem picture may be just the title plus code lines; that is fine as long as no options or answer show.

## Manual overrides (add this first)

Add `index/stem_overrides.json`, read by `tools/stem_crops.py` before its heuristic:

```json
{
  "quizzes/2024-jul/img/w01-q10-p17.png": 684,
  "quizzes/2020-jan/img/w01-q07-p4.png": null
}
```

- a number = cut that crop at this y (pixels from the top) and use it as the stem;
- `null` = never make a stem from this crop.

Measure y by opening the crop with PIL and checking where the figure ends and the options begin (draw a line at the y, save to the scratchpad, and look at it). Known Week 1 leftover: Q117 (`2024-jul/w01/q10`) shows nothing because a ring inside its Scratch picture fooled the radio check; give it an override.

## How to work

Go week by week, Week 0 and 2 → 12 (Week 1 only needs Q117).

1. List the week's affected cards and their stems:
   ```bash
   python -c "import json;gs=json.load(open('site/data/week-02.json',encoding='utf-8'));[print(n+1,g['id'],g['text'][-70:].replace(chr(10),' '),g['stem'],len(g['crops'])) for n,g in enumerate(gs) if g['crops'] and not (g['code'] or g['images'])]"
   ```
2. Look at the `-stem.png` images in one side-by-side montage (PIL, saved to your scratchpad, then Read it). This is the fast check; do it for every week.
3. **Inspect in the browser pane before editing.** The local server is `http://localhost:8765/site/#w2` (use `preview_start` with the `joc-site` config if it is not running). After data changes, bust the cache: `await fetch('data/week-02.json',{cache:'reload'}); location.reload()`. Scroll to a card with `javascript_tool` (find the `.q` whose `.q-id` text is `Q40¶`, `scrollIntoView()`, then `scrollBy(0,-60)`), wait ~800 ms for lazy images, then take a `computer` screenshot. Screenshot every affected card.
4. Fix each wrong card with an override (or by editing the source `.md` when the problem is parsing junk, see below), rerun the pipeline.
5. **Screenshot every affected card again in the browser pane after the edits** and confirm each one meets the "right" list above. Do not report a week as done without this second look.
6. Commit per week or two: `git add -A quizzes tools site index docs`, a message saying which weeks, and push. End commit messages with the attribution line from the session's system reminder.

## Also fix: page-break junk options

Portal printouts sometimes glue page-break letters onto the options: a trailing ` N` on the last real option and extra options `h` and `i i` (Jan 2020 Weeks 1, 8, 9, 10 are already fixed). If you see options that are clearly page junk (single stray letters that are not real answers), remove them in the session's source `quizzes/<session>/week-NN.md`, keep the `[x]` tick on the right option, rebuild the whole pipeline, and confirm the answer did not move. Real short options (`n`, `def`, `wav`, `py`, `if`) are fine.

## Hard rules

- Verbatim only: never retype or reword a question, option or code. The picture is the source.
- Never invent a stem: if the page has no figure for the stem (lost entirely), leave the card and list it.
- After any rebuild, check that no official answer was lost:
  ```bash
  python -c "import json,subprocess;L=lambda r:{m:(g['answer_source'],bool(g['answer'])) for w in range(13) for g in json.loads(subprocess.run(['git','show',f'{r}:site/data/week-{w:02d}.json'],capture_output=True,text=True,encoding='utf-8').stdout if r else open(f'site/data/week-{w:02d}.json',encoding='utf-8').read()) for m in g['members']};a,b=L('HEAD'),L(None);print('official lost',[k for k in a if a[k]==('official',True) and b.get(k)!=('official',True)])"
  ```
  It must print `official lost []`.
- `stem_crops.py` deletes and rewrites every `-stem.png` on each run, so hand-cropped files are lost unless they come from an override.
- Keep runs cheap: `stem_crops.py` scans every crop and takes several minutes; when testing a change, test it on the few crops in question first (import the module and call `cut_at` on them) before the full run.

## Report back

Per week: cards fixed (card number, session id, what was wrong), cards left and why, overrides added, and confirmation that you checked each fixed card in the browser pane before and after.
