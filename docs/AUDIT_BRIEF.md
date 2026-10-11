# Brief: fix the cards flagged in AUDIT.md

Paste this as the task for a fresh session. Work inside the repo root (`JRG JOC/`). The list of suspect cards is [AUDIT.md](AUDIT.md); regenerate it with `python tools/audit.py`.

## How the data flows

`quizzes/<session>/week-NN.md` (sources) → `python tools/build_dataset.py` → `site/data/questions.json` → `python tools/run_check.py` → `python tools/cluster.py` → `site/data/week-NN.json` (what the site shows).

Each card is a group of source questions (`members`). An id like `2018-jul/w01/q03@portal` is question 3 of the Jul-2018 Week 1 portal print; `@gpt` = ChatGPT-converted md; no suffix = the main week file. The audit line names the card's first source id and file.

## Hard rules (from the owner)

- **Verbatim only.** Never rewrite, summarise or "fix the wording" of question text, options or code. Copy what the source image/page shows. If the text cannot be recovered, leave the card and say so.
- The only note allowed on the site is for an official answer that is wrong or ambiguous. Never mention a wrong uploader tick.
- Badges: `official` only from an NPTEL key; `reviewed` only when exactly one answer is defensible.
- Work in batches by week; rebuild and re-run the audit after each batch. Report what you fixed, what you left and why.

## Where to fix what

| Problem | Fix |
|---|---|
| **Two copies of one question** ("same source question as Qn", usually a video transcription + a `@portal` print of the same session) | The portal print is authoritative. If the texts differ only by a prefix line like "(Scratch blocks: …)", the two failed to merge: make the main week file's text match the portal print, or put the missing context into the portal record via a fix (`index/fixes/*.jsonl`, keyed by the source id, field `text`). After a rebuild they must merge into one card. |
| **Duplicate of Qn, same options** | Same as above: find the textual difference that blocked the merge (`tools/cluster.py` merges on normalised text + option set) and fix the source that is wrong. |
| **Placeholder text / "question text in image"** | Read the page crop (`quizzes/<session>/img/wNN-qNN-pP.png`, listed in the card's `crops`) and transcribe the question verbatim into a fix `text`. |
| **Option looks like stray page text** ("Funded by", "1 point", a question line inside the options, 7+ options) | A portal-print parse error. Read the crop and give the correct `options` list in a fix (with `answer` as 0-based indices if the options change). |
| **Identical options / empty option** | Compare with the crop, PDF or video; an option was mis-transcribed (often `**` vs `*`, `<` vs `<=`, lost spaces). Fix the source md if it is a transcription you own; otherwise a fix `options`. If the source really shows two identical options, leave it. |
| **Text mentions image/screenshot, no image on the card** | Find the image in the session's `img/` folder or the source page/video and add it via a fix (`images` or `crops`, repo-relative paths). If it does not exist anywhere, leave it and list it. |
| **Source image link is broken** (Jul-2023 `@gpt`) | The original Obsidian images were never committed. Prefer the non-`@gpt` record of the same question if one exists; otherwise the screenshot in `quizzes/2023-jul/notebooks/` (extract with Python). |
| **Text looks cut off** | Check the source; fill-in-the-blank stems are fine. |
| **Text overlaps Qn with different options** (low) | Usually a real repeat with changed options: leave it. Only act if one is clearly a broken copy of the other. |
| **No answer** (low) | Only fill it from an official key or a run; never guess. |

## Traps

- A bold numbered line `**N) …**` inside a question is parsed as question N when N is the next expected number. That splits a question and glues its tail onto the next one. Fix it in the source md by writing `**Step N)`, then check the following question too.
- Fix files are JSONL, UTF-8, **no BOM**. Write them with Python or bash, never PowerShell `Set-Content`.
- After editing a source md, run all three: `build_dataset.py` → `run_check.py` → `cluster.py`. Overlay-only changes need just `cluster.py`. Then `python tools/audit.py`.
- Check that the question count in the `cluster.py` output only drops by the duplicates you merged.
