# Audit: session duplicates, unsolvable cards, >4 options (2026-10-20)

Data checked: `site/data/questions.json` (2334 source questions) and `site/data/week-NN.json` (1952 site cards).

## 1. Sessions wrongly copied as other sessions — none found

- No two `quizzes/*/week-NN.md` files are byte-identical, and no image/crop is shared between two terms (md5 of every png/jpg).
- Same-week overlap (question text ≥90% similar) between any two terms tops out around 50–70%, which is normal NPTEL reuse. The high ones were checked:
  - **2020-jan vs 2020-sep, week 10 (5/10)**: false alarm. The matches are generic stems ("Predict the output") with different code and answers; the site does not merge those.
  - **2022-jul vs 2024-jul, week 0 (10/10, same order, same answers)**: genuine reuse. Two independent sources (YouTube 2022-07-12, `noc22_cs122` vs the 2024 portal-print PDF).
  - **2022-jan vs 2024-jan, week 0 (9/10)**: likely genuine, but `quizzes/2022-jan/week-00.md` has **no source/portal header**, so its Jan-2022 tag can't be verified from the file.
- Inside one term, repeats are expected copies (`@portal` = portal print of the same quiz, `@gpt` = 2023-jul ChatGPT-converted version). Same-text pairs like `2020-jan/w04/q08` / `q09` differ only in the code image and different answers: real distinct questions, kept separate on the site.

### Same-week duplicate cards on the site (flagged in AUDIT.md)
- Merged via `index/merges.tsv`: Binary search (2022-jan/w06/q07 + 2023-jul/w06/q07@gpt), hexagon (2022-jan/w07/q04 + 2023-jul/w07/q04), `time.time()` (2022-jan/w11/q02 + 2023-jan/w11/q03), 3n+1 (2019-jul/w12/q05 + 2021-jul/w12/q06, whose text was cut off). The two blank-option cards from section 2 are now solvable.
- Not duplicates, kept apart: Monty Hall switch vs don't switch (w5), `f(10000)` vs `f(-8)` (w6), star vs hexagon (w7).

### Full pairwise check (every card against every other card in the same week)
- 360 candidate pairs. About 265 were generic stems ("What is the output of the following code?") with different code and options, so they are different questions.
- The other ~95 were read by hand: **48 more real repeats were merged** (all listed in `index/merges.tsv`), taking the site from 1952 to **1900 cards**. Each merged card gets every session in its "Asked N×" tag. Mostly 2022-jan questions reused in 2023-jan, 2023-jul and 2025-jan, plus a few 2018/2019/2020 ones.
- Merges are hand-checked, so they override the official-key guard. One case needed it: "All of the above" vs "All the above".
- Kept apart on purpose: **repeats whose options were changed**, where merging would show the wrong option set for one session. Examples: dice 1/12 vs 1/3 (w0), numpy 10–13 vs 11–14 (w10), `break` question with leave vs try (w11), birthday "None of the above" vs 13 (w4), magic square 15 vs 16 (w4), tic-tac-toe, VADER, recursion statements, functions. Also kept apart: same stem with different code in the image and different answers (2024-jul vs 2025-jan cards, 2020-jan w04 q08/q09, w06 q08–q10, w08 q08/q09).
- **Across weeks** (the same question asked in a different week in another session): every card was also compared with every card in other weeks, needing shared options. That gave 141 hits, mostly placeholder options ("Option 1…4"). 17 were read by hand and **9 merged**, e.g. 2020-sep w3 ↔ 2020-jan w9 and 2022-jul w12 ↔ 2023-jan w11. The 2020-sep "scenario" code was checked against the 2020-jan crops. A merged card is listed under one week only (its main copy's). Total now **1891 cards**.
- Data problems noticed, not fixed: the page-rank card `2019-jul/w12/q03` official key ticks two options; `2021-jul/w12/q08` has two "Statement b is correct" options; `2023-jul/w09/q10@gpt` and `2023-jul/w12/q11@gpt` carry programming-assignment code by mistake (the w12 one is merged into its proper card, w09 is not).

## 2. Unsolvable / incomplete cards (text needs code or a figure, card shows none)

| Card | Problem | Source |
|---|---|---|
| 2021-jul/w02/q08 | "output of the following program", no code | quizzes/2021-jul/week-02.md |
| 2022-jul/w02/q08 | "which blocks of code are correct", no code | quizzes/2022-jul/week-02.md |
| 2022-jul/w02/q09 | "regarding the following code", no code | quizzes/2022-jul/week-02.md |
| 2023-jul/w02/q08@gpt | "below code", code missing | quizzes/2023-jul/chatgpt-converted-md/week-02.md |
| 2019-jan/w04/q03 | refers to code, none attached | quizzes/2019-jan/week-04.md |
| 2023-jul/w04/q06@gpt | all 4 options blank (options were code) | quizzes/2023-jul/chatgpt-converted-md/week-04.md |
| 2024-jan/w04/q05 | "Masked Gun" code missing | quizzes/2024-jan/week-04.md |
| 2024-jan/w05/q03 | RPSLS code missing | quizzes/2024-jan/week-05.md |
| 2023-jul/w06/q07@gpt | all options blank (options were code) | quizzes/2023-jul/chatgpt-converted-md/week-06.md |
| 2023-jan/w07/q07 | "which code snippet", check options hold the code | quizzes/2023-jan/week-07.md |
| 2023-jul/w07/q04 | hexagon programs: no code, all options blank | quizzes/2023-jul/week-07.md |
| 2022-jul/w08/q03 | "which programs print…", no programs | quizzes/2022-jul/week-08.md |
| 2024-jan/w10/q04 | refers to code, none attached | quizzes/2024-jan/week-10.md |
| 2019-jul/w11/q03 | "in the question above": depends on previous question's code | quizzes/2019-jul/week-11.md |
| 2023-jul/w12/q06 | flagged by pattern; check | quizzes/2023-jul/week-12.md |

Probably fine (pattern false hits, check quickly): 2023-jul/w01/q08@gpt, 2024-jan/w01/q04, 2022-jul/w11/q08.

Also **86 questions have 0 options** (mostly `reveal`/`numeric` types, by design) and ~250 have no answer key; those are already tracked by `tools/audit.py` / `docs/AUDIT.md` and not repeated here.

## 3. Questions with more than 4 options (49)

### Genuine 5–6 option questions (source really has them) — OK
2023-jan/w01/q07, 2022-jul/w02/q06, 2023-jan/w02/q01, 2023-jan/w07/q01, 2023-jan/w07/q05, 2023-jan/w08/q04, 2023-jan/w08/q05, 2021-jan/w09/q05 (+@portal), 2022-jul/w09/q04, 2023-jan/w09/q06, 2024-jul/w10/q05 (FLAMES: 6), 2023-jan/w11/q06, 2022-jan/w12/q03, 2023-jul/w12/q03, 2024-jan/w12/q04, 2020-sep/w08/q09 (5th "None of the above" OK, but option 1 is split: "…otherwise" is a wrapped line — see below).

### Broken: options built wrongly from PDF text — need rebuilding from the crop
Cause in each case: when the portal PDF was parsed, a wrapped option line, a duplicated text layer, or part of the question became its own option. On the site these show fragments as choices and the tick lands on fragments (e.g. 2020-jan/w04/q10 ticks 9 of 19), so the card can't be answered properly.

| Card | Count | What went wrong |
|---|---|---|
| 2024-jul/w04/q04 | 76 | matrix options exploded into one option per glyph |
| 2020-jan/w04/q10 | 19 | code options split per line |
| 2020-sep/w06/q01 | 19 | code options split per line |
| 2020-sep/w07/q01, q03 | 12 | long options wrapped into 3 lines each |
| 2023-jul/w05/q10@gpt | 13 | next question's text + "Explanation" leaked into options |
| 2024-jul/w04/q01 | 11 | formula options split (n², n(n+1)/2 …) |
| 2020-jan/w04/q05 | 10 | code options split per line |
| 2020-sep/w02/q08 | 10 | text layer printed twice + lines split |
| 2020-sep/w02/q04, 2020-jan/w06/q04 | 8 / 6 | each option duplicated (spaced and unspaced text layer) |
| 2020-sep/w05/q07, w08/q03 | 8 | each option wrapped into 2 lines |
| 2018-jul/w03/q03 | 8 | code lines of the question became options |
| 2020-sep/w03/q01 | 7 | list options split |
| 2020-sep/w10/q04 | 7 | wrapped options |
| 2018-jul/w06/q08, q09 | 7 | question's code lines became options |
| 2018-jul/w03/q01 | 6 | question's code lines became options |
| 2020-sep/w04/q08, 2020-sep/w06/q03 | 6 | wrapped options / matrix rows |
| 2025-jan/w05/q03 | 6 | code split + garbage glyphs |
| 2018-jul/w03/q05 | 5 | jumbled word + date stamp merged into option a |
| 2025-jan/w01/q10, 2025-jan/w04/q07 | 5 | question text ("What task does…") parsed as option a |
| 2020-sep/w03/q08, 2020-sep/w04/q04 | 5 | one option duplicated / split |
| 2020-sep/w08/q09 | 5 | wrapped line "otherwise" became an option |
| 2023-jul/w06/q08@gpt | 5 | "Correct Answer: …" line became an option |

**Status (same day):** this table came from the raw `questions.json`. Most of these were already fixed on the site by `index/fixes/local.jsonl`. The 7 that were still broken on the site are now fixed in `index/fixes/options.jsonl`, rebuilt from the crops: 2018-jul/w03/q01, 2018-jul/w03/q05, 2020-sep/w03/q08, 2020-sep/w04/q04, 2020-sep/w08/q09, 2025-jan/w05/q03 and 2023-jul/w06/q08@gpt. Every site card now has at most 4 options, apart from the genuine 5–6 option ones listed above.

Fix for each: rebuild the options from the page crop (`quizzes/<term>/img/…`), then re-tick the accepted answer by its text, not by its old index.
