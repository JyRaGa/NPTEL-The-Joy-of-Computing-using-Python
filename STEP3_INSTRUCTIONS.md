# Step 3 brief: topic index, repeat frequency, verified flag

Paste this file (or point the new chat at it) as the task. Work inside `JRG JOC/`. Read `README.md`, `structure.md` §5 and `inventory.tsv` first.

## Goal

Add three things no source repo has, on top of the per-week files already in `JRG JOC/quizzes/`:

1. **Topic index**: every question tagged with one or more course topics, so "all turtle-output questions across years" is one page.
2. **Repeat frequency**: which questions recur across sessions (the course reuses questions heavily), and how many sessions each appears in.
3. **Verified / unverified flag per answer**, with a trust level and a note where sources disagree.

## Hard rules (from the owner)

- **Never summarise or rewrite question text, options or code.** Index files may quote or link, but source `week-*.md` files stay untouched. Put all new output in new folders: `index/` (data) and `index/topics/` (pages). Scripts go in `tools/`.
- Quiz questions and options are the product; programming assignments are low priority (index them only if cheap).
- A `[x]` tick is **not** an answer key unless the file says it is official (see trust levels). Ticks in video transcriptions are the uploader's own pick and can be wrong; some are known wrong and already noted in the file (Jul-2019 has a corrections list).
- Do not write "assignment not submitted" or similar submission-status remarks anywhere.
- Report outcomes plainly; flag suspicious answers; do not pad.

## What is in the tree (2026-10-11)

`inventory.tsv` lists 215 markdown files with `term, week, path, kind, trust`. Term folders are `quizzes/<year>-<jan|jul>/`; session rule: Week 1 in Dec/Jan = Jan session, Jul/Aug = Jul session. Folder `2026-jul` is the second 2026 session.

| kind | terms | format | trust |
|---|---|---|---|
| `portal_print_parsed` | 2018-jul (Wk1–6, 8–10), 2020-jan, 2020-sep, 2021-jan (`*-portal-print.md`), 2024-jul, 2025-jan | `### Qn. text`, options `- [ ]`/`- [x]`, then `> Yes, the answer is correct. Score: 1`, then `![page crop](img/wNN-qNN-pP.png)` | **official**: `[x]` = NPTEL "Accepted Answer". Text parse can be noisy (stray spaces such as "cor rect", options lost when they are images). **The PNG crop is authoritative.** |
| `youtube_transcription` | 2018-jul Wk1–2, 2019-jan Wk3–12, 2019-jul Wk1–12, 2022-jul, 2023-jan, 2023-jul Wk7–12, 2024-jan, 2025-jul Wk5, 2026-jan | `**N) question**` then `- [x]` / `- [ ]` options, fenced code, header with source URL and portal due date | ticks = uploader's own pick, unverified. Jul-2019 files end with an "Official accepted answers" section from the NPTEL review page: **that overrides the ticks**. A few weeks (e.g. Jul-2022 Wk0 and Wk2, Jan-2023 Wk0, Jan-2024 Wk0) were checked against a score page; grep the files for "10/10" or "score page" to find them ("unverified" also contains "verified", so do not grep for that). |
| `second_repo_md` | 2021-jan, 2021-jul, 2022-jan | markdown with `<img src="img/noc../...">` for image questions, `✅` after the author's answer | author-marked, unverified. Images are mirrored under `img/`. |
| `chatgpt_converted_md` | 2023-jul Wk1–12 | ChatGPT-converted, "Correct Answer:" lines, broken `![[Pasted image]]` embeds | unverified; same questions as `notebooks/` screenshots (which show NPTEL Accepted Answers but are images) |
| `case_study_pdf_md` | 2026-jul Wk1–12 | scenario + 20 questions per week (`### Q1.` or `### Question 1` / `### MCQ 1`), `**Answer: B**`, `> Justification:`; Wk11–12 are scanned pages with an OCR layer | answers as printed in the owner's PDFs; treat as "provided", not NPTEL-verified |

Image-only/OCR text lives next to the PDFs as `*.ocr.txt` (RapidOCR, machine-read). Not parsed into md yet: `quizzes/2022-jul/JOC_2022_APRIL_DEC… .ocr.txt` (a portal print of Jul-2022, second source for that term), `exams/34 questions… .ocr.txt`, and the Jan-2022 Wk1, Jan-2024 Wk3, Jan-2026 Wk2/Wk7, Jul-2025 Wk4 extras.

Not in `quizzes/*.md` (PDF only, searchable text layer): the Scribd printouts in `quizzes/<term>/extra-sources/`, `quizzes/2025-jan/*.pdf` typed sheet, `practice/`, `exams/`.

## Suggested plan

### A. Normalise to one dataset

Write `tools/build_dataset.py` that parses every file in `inventory.tsv` (one small parser per `kind`) into `index/questions.jsonl`, one record per question:

```
{"id": "2024-jul/w03/q04", "term": "2024-jul", "week": 3, "num": 4, "file": "quizzes/2024-jul/week-03.md",
 "text": "...verbatim...", "code": "...or null", "options": ["..."], "ticked": [2], "has_image": true,
 "kind": "portal_print_parsed", "trust": "official", "crop": "quizzes/2024-jul/img/w03-q04-p29.png"}
```

Notes: keep text verbatim; normalise only in separate fields (`norm_text`, `norm_options`). Questions whose options exist only as an image: keep `options: []`, `has_image: true`. Include 2026-jul questions (scenario text is shared by 5 questions: store it as `context`). Assert counts per file (e.g. 10 questions per portal-print week; 20 per 2026-jul week) and print a mismatch report.

### B. Topic tags

Course topics by week (use them as the taxonomy, add finer tags as needed): Wk0 aptitude/maths warm-up; Wk1 programming basics, Scratch (loops, broadcast, motion/sound blocks); Wk2 Python basics (variables, input(), operators, loops, `range`, string multiplication); Wk3 lists, conditionals, loops, counting candies, FizzBuzz; Wk4 magic square, Birthday paradox, Google Translate/guess-the-word, currency converter, dictionaries; Wk5 Monty Hall, searching (linear/binary), sorting (bubble), Rock-Paper-Scissors, speech recognition; Wk6 recursion, ciphers (Caesar/substitution), Tic-Tac-Toe, Min-Max; Wk7 Snakes & Ladders, turtle, spiral traversal, matplotlib/GPS/gmplot, PIL; Wk8 tuples, lottery simulation, image processing (CLAHE), anagrams, sentiment analysis (NLTK/VADER), matrices/transpose; Wk9 networkx/graphs, Six degrees of separation, area calculation (Monte Carlo), stylometry/NLP; Wk10 FLAMES, data compression (lossy/lossless), strings, numpy; Wk11 Selenium, datetime/calendar, string methods; Wk12 PageRank, sinks, Collatz/3n+1.

Implementation: rule-based keyword/regex tagger first (e.g. `turtle`, `pen.forward` → turtle; `nx.`, `networkx` → graphs; `np.`/`numpy` → numpy; `calendar`, `datetime` → date-time; `selenium`; `def ...(` recursion detection; `sorted`, `bubble`; `Monty`, `FLAMES`, `PageRank`, `Collatz`...). Allow multiple tags. Anything untagged goes to `index/topics/_untagged.md` for review. Do not use an LLM to rewrite text; an LLM may only assign tags, and the tag list and decisions must be written to `index/tag_rules.md`.

Outputs: `index/topics/INDEX.md` (topic → count, list of terms) and one `index/topics/<topic>.md` per topic listing, per question: id, term/week, link to the source file and anchor/line, the first line of the question (quoted verbatim), whether options are images, repeat count, trust level. No answers inlined unless trust is official.

### C. Repeat frequency

Cluster questions across terms:

1. exact match on `norm_text + sorted(norm_options)` (lowercase, collapse whitespace/punctuation, strip `1)`/`Q1.` prefixes, strip code line numbers);
2. then fuzzy match (e.g. `rapidfuzz` ratio ≥ 0.92 on the normalised text; require same option set when options exist);
3. for image-only questions, use the filename/crop only if identical; otherwise leave as singletons and say so.

Outputs: `index/repeats.tsv` (cluster id, size, number of distinct terms, member ids), `index/REPEATS.md` (top clusters by number of terms, with the verbatim question once and the list of terms/weeks it appears in), and write `repeat_count` / `terms` into `questions.jsonl`. Watch for false merges between versions of a question that differ in one number or one option (e.g. 2D matrix size, `range(1,5)` vs `range(1,6)`): such near-duplicates must not be merged; list them separately in `index/near_duplicates.md`.

### D. Verified flag

Per question, set `verified` to one of:

- `official`: from `portal_print_parsed` (NPTEL Accepted Answer) or from a Jul-2019 "Official accepted answers" section;
- `scored`: video/screenshot shows a green score box for that quiz (the file header says so; grep for "10/10" or "score page");
- `agreed`: two or more independent unscored sources give the same answer (cluster members from different `kind`s);
- `single_source`: one author tick, nothing else;
- `unknown`: no ticked option (e.g. image-only, or unsubmitted page).

Add `answer_conflicts`: when members of the same cluster disagree on the ticked option, list them in `index/conflicts.md`, with the official answer first if one exists. Known official corrections to seed this (Jul-2019): Wk1 Q2 = False; Wk3 Q6 = 5; Wk5 Q1 = Divide and conquer method; Wk12 Q3 = Rank of pages referring to it; Wk6 Q5 and Wk12 Q6 were zero-weighted; Wk9 Q5 and Q8 accepted answers are the ticked ones. Also flag likely-wrong ticks you can justify by running the code (cheap check: execute short pure-Python snippets), clearly labelled as "checked by running", never silently overwritten.

### E. Report

Write `index/QA_STATS.md`: questions per term and week, how many per `verified` level, how many tagged/untagged, number of repeat clusters, top 20 repeating questions, list of parse mismatches. Tell the owner plainly what is incomplete.

## Pitfalls seen so far

- The Bash tool on this Windows machine mangles backslashes inside heredocs; create scripts with the file Write/Edit tools. Paths contain spaces ("JRG JOC", "second repo"); quote everything. A deep venv path breaks DLL loading ("filename too long"); create venvs near the drive root (a working one is `C:\Users\rajes\AppData\Local\Temp\jocenv`: `pymupdf`, `rapidocr-onnxruntime`, `pillow`). Tesseract is **not** installed.
- `-portal-print.md` files sit next to another source for the same week (2018-jul Wk1–2, 2021-jan Wk1–12): they are second sources; do not drop either.
- 2018-jul portal print has Wk1–6, 8–10 only (88 accepted answers); Jan-2020 Wk8 parsed 9 of 10 questions; Jul-2023 has no per-week file for Wk1–6 except the ChatGPT md and notebooks.
- Jan-2019 programming-assignment text lives inside the same week file (low priority).
- The Jul-2019 files contain extra sections (second source, official answers). Only the first quiz section (up to the first `---`) is the question list; later sections repeat answers.
- Portal-print text can place an option under the wrong question when the layout breaks across pages; spot-check against the crop PNG before trusting an option list, and report parse mismatches instead of hiding them.

## Acceptance checks

- Re-running `tools/build_dataset.py` reproduces `index/questions.jsonl` identically.
- Every file in `inventory.tsv` contributes records or is listed in the mismatch report.
- No source `week-*.md` was modified (`git status` shows only new files under `JRG JOC/index/` and `JRG JOC/tools/`).
- At least 20 clusters spot-checked by hand (open the two source locations and confirm they are the same question).
