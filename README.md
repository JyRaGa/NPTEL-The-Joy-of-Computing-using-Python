# Joy of Computing — past quizzes

Every past weekly quiz of NPTEL's **The Joy of Computing using Python** (IIT Ropar), 2018–2026, as one practice site. Questions are grouped by course week; pick an option and see right or wrong at once.

**Live site: [joc-jrg.vercel.app](https://joc-jrg.vercel.app)**

## Features

- **2,135 questions** from 17 sessions, merged into 1,953 cards. A question asked in several sessions appears once, tagged with each session and an "Asked N×" count.
- **Instant feedback.** Single-answer questions check on click; multi-answer questions have a Submit button; typed answers have a Check button.
- **Every answer says where it came from:** official NPTEL key, course PDF, verified by running the code, reviewed, or unverified.
- **Filters and order:** by session; all, unanswered, wrong or saved; most repeated, newest or oldest first. Search covers every week.
- **Progress stays in your browser,** with export and import. Keyboard shortcuts, dark mode and adjustable text size.
- Code is shown verbatim with syntax highlighting; questions that were images keep the original page crop.

## Coverage

| Session | Weeks | Questions | Official answer | Other answers |
|---|---|--:|--:|---|
| 2018 Jul–Oct | 1–6, 8–10 | 90 | 100% | — |
| 2019 Jan–Apr | 3–12 | 94 | 32% | 2 verified by running, 62 reviewed |
| 2019 Jul–Oct | 1–12 | 109 | 93% | 8 reviewed |
| 2020 Jan–Apr | 1–12 | 119 | 97% | 4 no answer |
| 2020 Sep–Dec | 1–12 | 120 | 94% | 2 reviewed, 5 no answer |
| 2021 Jan–Apr | 0–12 | 130 | 84% | 20 reviewed, 1 unverified |
| 2021 Jul–Oct | 0–12 | 130 | 7% | 113 reviewed, 8 unverified |
| 2022 Jan–Apr | 0–12 | 130 | 35% | 85 reviewed |
| 2022 Jul–Oct | 0–12 | 130 | 100% | — |
| 2023 Jan–Apr | 0–12 | 130 | 31% | 8 verified by running, 82 reviewed |
| 2023 Jul–Oct | 1–12 | 122 | 93% | 3 verified by running, 4 reviewed, 1 unverified, 1 no answer |
| 2024 Jan–Apr | 0–12 | 131 | 1% | 7 verified by running, 115 reviewed, 8 unverified |
| 2024 Jul–Oct | 0–12 | 130 | 100% | — |
| 2025 Jan–Apr | 1–12 | 120 | 99% | 1 no answer |
| 2025 Jul–Oct | 5 | 30 | 0% | 5 verified by running, 25 reviewed |
| 2026 Jan–Apr | 1–12 | 180 | 0% | 23 verified by running, 156 reviewed, 1 unverified |
| 2026 Jul–Oct | 1–12 | 240 | 83% | 40 reviewed |
| **All** | | **2135** | **63%** | |

Counts are per session; when a repeated question has an official key from any session, every copy uses it. "Reviewed" answers were worked out from the question, and "unverified" ones are only a video uploader's pick. Missing sessions and weeks had no source we could find.

## Also in this repo

- [`notes/`](notes/): week-by-week lecture notes (Markdown, written in Obsidian; `excalidraw/` drawings open in Obsidian's Excalidraw plugin).
- [`exams/`](exams/): a recollection of 34 final-exam questions, exam-pattern notes, and online programming test solutions (Jan and Jul 2021).
- [`programming-assignments/`](programming-assignments/): weekly programming-assignment solutions for 2021–2022.
- [`lecture-code/`](lecture-code/): the programs written in the lectures (FLAMES, Monty Hall, PageRank, Snakes and Ladders and more).
- [`practice/`](practice/): important-question sets and small MCQ banks.
- Each session's whole-term PDFs and printouts sit next to its week files in `quizzes/<session>/`.

## Run it locally

The site is static (HTML, CSS and plain JavaScript; no build step to view it).

```bash
python -m http.server 8765
```

Then open <http://localhost:8765/site/>.

## Rebuild the data

Needs Python 3 and Pygments.

```bash
python tools/build_dataset.py && python tools/run_check.py && python tools/cluster.py
```

- `quizzes/<session>/week-NN.md`: the transcribed quizzes, text kept verbatim.
- `index/review/`, `index/answers_review.tsv`: answer overlays (official keys and reviewed answers).
- `index/fixes/`: text, code and images recovered from videos and screenshots.
- `site/`: the website; `site/data/` is generated.

Source notes and conventions are in [docs/SOURCES.md](docs/SOURCES.md).

## Sources and credits

Quiz questions, options and official answers are course material of NPTEL / IIT Ropar, reproduced for study.

**YouTube first.** Most sessions survive only as solved-assignment videos, so the quizzes were rebuilt from 93 videos by 17 YouTube channels (each credited in its week file's header). Questions, options and code were transcribed frame by frame, sometimes stepping through phone recordings at quarter speed, skipping ads and catching code that scrolls past in under a second. Then every answer was checked again, because an uploader's tick is not an answer key. Code questions were run; the rest were reasoned out or matched against official keys. Over 60 code screenshots were recovered this way.

The rest came from these repositories:

- [kishanrajput23/NPTEL-The-Joy-of-Computing-using-Python](https://github.com/kishanrajput23/NPTEL-The-Joy-of-Computing-using-Python) by Kishan Kumar Rai (MIT): 2021–2022 quizzes, programming assignments, online test solutions and lecture code.
- [gxuxhxm/NPTEL-The-Joy-of-Computing-using-Python](https://github.com/gxuxhxm/NPTEL-The-Joy-of-Computing-using-Python) by Goutham S K (MIT): lecture notes and the Jul-2023 quiz notes.
- [avinashyadav16/The-Joy-of-Computing-Using-Pyhton](https://github.com/avinashyadav16/The-Joy-of-Computing-Using-Pyhton): Jul-2023 Jupyter notebooks whose screenshots supplied that term's official answers.
- [tdishant/NPTEL-Joy-of-Computing-Using-Python](https://github.com/tdishant/NPTEL-Joy-of-Computing-Using-Python): 2020–2021 quiz PDFs, including the text PDF of Jan-2021.
- [progiez/nptel-assignment-answers](https://github.com/progiez/nptel-assignment-answers) (the Joy of Computing part): kept for reference only, unverified.

Scribd uploads and NPTEL portal printouts filled the remaining gaps; the URL of each is in [sources/](sources/). Licences of the MIT sources are in [licenses/](licenses/).
