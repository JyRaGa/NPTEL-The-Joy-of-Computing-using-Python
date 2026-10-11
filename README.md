# Joy of Computing — past quizzes

Every past weekly quiz of NPTEL's **The Joy of Computing using Python** (IIT Ropar), 2018–2026, as one practice site. Questions are grouped by course week; pick an option and see right or wrong at once.

## Features

- **2,334 questions** from 17 sessions, merged into 1,999 cards. A question asked in several sessions appears once, tagged with each session and an "Asked N×" count.
- **Instant feedback.** Single-answer questions check on click; multi-answer questions have a Submit button; typed answers have a Check button.
- **Every answer says where it came from:** official NPTEL key, course PDF, verified by running the code, reviewed, or unverified.
- **Filters and order:** by session; all, unanswered, wrong or saved; most repeated, newest or oldest first. Search covers every week.
- **Progress stays in your browser,** with export and import. Keyboard shortcuts, dark mode and adjustable text size.
- Code is shown verbatim with syntax highlighting; questions that were images keep the original page crop.

## Coverage

| Session | Weeks | Questions | Official answer | Other answers |
|---|---|--:|--:|---|
| 2018 Jul–Oct | 1–6, 8–10 | 109 | 94% | 1 verified by running, 5 reviewed, 1 no answer |
| 2019 Jan–Apr | 3–12 | 94 | 30% | 2 verified by running, 63 reviewed, 1 unverified |
| 2019 Jul–Oct | 1–12 | 109 | 93% | 8 reviewed |
| 2020 Jan–Apr | 1–12 | 119 | 100% | — |
| 2020 Sep–Dec | 1–12 | 120 | 97% | 2 reviewed, 2 no answer |
| 2021 Jan–Apr | 0–12 | 250 | 70% | 1 verified by running, 64 reviewed, 3 unverified, 6 no answer |
| 2021 Jul–Oct | 0–12 | 130 | 5% | 114 reviewed, 9 unverified |
| 2022 Jan–Apr | 0–12 | 130 | 35% | 82 reviewed, 3 unverified |
| 2022 Jul–Oct | 0–12 | 130 | 99% | 1 reviewed |
| 2023 Jan–Apr | 0–12 | 130 | 30% | 8 verified by running, 83 reviewed |
| 2023 Jul–Oct | 1–12 | 182 | 93% | 6 reviewed, 2 unverified, 4 no answer |
| 2024 Jan–Apr | 0–12 | 131 | 1% | 7 verified by running, 115 reviewed, 6 unverified, 2 no answer |
| 2024 Jul–Oct | 0–12 | 130 | 100% | — |
| 2025 Jan–Apr | 1–12 | 120 | 100% | — |
| 2025 Jul–Oct | 5 | 30 | 0% | 4 verified by running, 26 reviewed |
| 2026 Jan–Apr | 1–12 | 180 | 0% | 23 verified by running, 156 reviewed, 1 unverified |
| 2026 Jul–Oct | 1–12 | 240 | 0% | 220 course PDF, 20 reviewed |
| **All** | | **2334** | **55%** | |

Counts are per session; when a repeated question has an official key from any session, every copy uses it. "Reviewed" answers were worked out from the question, and "unverified" ones are only a video uploader's pick. Missing sessions and weeks had no source we could find.

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

## Credits

Quiz questions, options and official answers are course material of NPTEL / IIT Ropar, reproduced for study. Parts of the source material came from public repositories under the MIT licence; see [licenses/](licenses/).
