# Next steps — JOC past-quiz practice site

State as of 2026-10-11. The site works locally: `.claude/launch.json` config **joc-site**, then open http://localhost:8765/site/.

## Where things stand
- **2001 question cards** across W0–W12.

  | Answer label | About |
  |---|---|
  | Official answer | ~796 |
  | Reviewed answer | ~880 |
  | Course PDF answer | 220 |
  | Verified by running | ~52 |
  | Unverified (only the YouTuber's tick) | ~22 in the terms below |
  | No answer | a few |

- **Week titles and descriptions** come from the official course outline. They are the `WEEKS` and `DESC` arrays at the top of `site/app.js`. W0 is the pre-course warm-up.
- **Rebuilding:** run `python tools/build_dataset.py` → `python tools/cluster.py` → `python tools/run_check.py` → `python tools/cluster.py`. Only `cluster.py` is needed after editing review or fix files.
- **Answer overlays** live in two places:
  - `index/answers_review.tsv` and `index/review/week-NN.tsv`, added with `python tools/review_add.py <member-id>=B`;
  - `index/fixes/*.jsonl`.

  Both are keyed by a member source id such as `2024-jan/w05/q04`. Answers are 0-based option indices in that member's option order.
- **Last session's YouTube recovery** went into `index/fixes/youtube3.jsonl`. Crops are saved in `quizzes/<term>/img/recovered/`.

## 1. Remaining gaps (optional, low value)
Solved later by reasoning: 2024-jan w07 q02 = C (step III also names 100, so a 200-tile board changes steps I and III) and 2024-jan w09 q09 = -1 (the code is correct). Then recovered from the Jan-2024 videos and reasoning: w06 q09/q10 = 7 and 5 (code read from the Week 6 video, verified by running), w05 q03 (the bold step lines were mis-parsed; the md step lines were renamed `Step 4)`/`Step 5)` so q03 keeps its four options, answer D), w04 q05 (typed answer 321645, unverified), w07 q01 = 213 and w08 q04 = C. 14 gaps remain; the ones below are ambiguous, broken, or need code that is not in the data (w06 q09/q10, 2019-jan w05 q09, 2022-jul w07 q07, 2024-jan w05 q08, w11 q08, w12 q04/q10).
Run `python tools/gaps.py 2024-jan 2022-jul 2023-jan 2019-jan 2019-jul 2026-jan` to list them. What's left:

- **Questions that are broken or ambiguous at the source.** A video cannot fix these; leave them Unverified unless an official key turns up.
  - 2024-jan w05 q01: 4-door Monty Hall. The correct answer is 3/8, which is not among the options.
  - 2024-jan w04 q07: the Tuesday-birthday count. The transcribed dataset gives 17, but the options are 8–11, so the dataset is probably mistranscribed. Re-check the dataset against the portal image.
  - 2022-jul w06 q05: options 3 and 4 are identical in every frame.
  - 2026-jan w02 q03: both C and D describe real faults.
  - 2022-jul w01 q07: "if" and "wait" are both non-motion blocks.
- **2022-jul w10 q04:** the code as transcribed doesn't fit the options. Every frame of the source video (A2p4zimg5lE) is blurred, so another uploader's video of the Jul-2022 Week 10 quiz is needed.
- **Others that need a careful look:**
  - 2024-jan "arrange the steps" and typed-answer items (w04 q05, w05 q03/q04, w06 q09/q10 need the `f` code, w07 q01, w09 q09, w11 q08, w12 q10);
  - 2024-jan w01 q04 (open-source languages);
  - 2024-jan w05 q08;
  - 2024-jan w07 q02;
  - 2024-jan w08 q04 (options are pictures);
  - 2024-jan w12 q04;
  - 2019-jan w05 q09;
  - 2022-jul w07 q07.
- **YouTube technique that works in the in-app browser:**
  1. Navigate to `watch?v=ID&t=Ns`.
  2. Skip ads with JS (`video.currentTime=1e4` while `.ad-showing`).
  3. Hide `.ytp-chrome-bottom`.
  4. Play for 1–5 s, pause, then zoom to the region `[0,80,780,530]`.
  5. For fast-scrolling phone recordings, set `playbackRate=0.25` and step `currentTime` by about 1 s.

  Screenshots are saved under the session's `tool-results` folder; copy one to `img/recovered/` to use it as a crop.

## 2. Design finish review (Impeccable)
- Take desktop (1280 px) and mobile (375 px) screenshots, in light and dark mode, into `.impeccable/review/`.
- Run the `impeccable:impeccable-finish-reviewer` agent against `.impeccable/surfaces/site-index-html.md` and `DESIGN.md`.
- Apply its fixes in one batch, then do at most one confirmation pass.
- Check the new `.week-desc` line under each week title for spacing on mobile.

## 3. Decisions for the owner
- **Licence** for the repo and site content. The quiz content belongs to NPTEL; say so in a footer or README.
- **Git:** nothing is committed yet (branch `main`; `JRG JOC/`, `2026 Assignments/`, `_incoming/` and `structure.md` are untracked). Decide which branch to use and whether `quizzes/**` images and notebooks belong in the repo.
- **Deploy:** `vercel.json` and `.vercelignore` are ready. Create a Vercel project with root directory `JRG JOC`, deploy, and check that `/` redirects to `/site/` and that images load from `/quizzes/...`.

## 4. Nice-to-haves (only if wanted)
- Per-week progress shown in the sidebar table of contents.
- A "random question" or exam-mode drill across weeks.
- A link back to each card's source video or portal file, already present as `file` in the data.

## Rules for whoever continues (from the Opus review, 2026-10-11)
- **Parser trap:** a bold numbered line `**N) …**` inside a question is read as question N when N is the next expected number. That swallowed a step and glued it onto the next question (2024-jan w05 q03/q04, w04 q05/q06). Fix it in the source md by writing `**Step N)`, then run the full rebuild. Afterwards, check the following question's text, not just the one you fixed.
- **After any md edit,** run all four steps: `build_dataset` → `run_check` → `cluster`. Then confirm `python tools/gaps.py …` and that the question count did not drop unexpectedly.
- **Typed answers:** `cluster.py` now removes the "Answer entered…" line when a card becomes numeric, so the answer is not given away. Don't put that line into fix `text` either.
- **Badges:** use `reviewed` only when the reasoning has exactly one defensible answer. Otherwise leave the card Unverified. The 13 remaining gaps are all in that state; don't force them.
- **YouTube search** for older terms (2019–2023) returns mostly new uploads. Search by the original uploader's channel name, as listed in the `Source:` line of each week md, instead of keyword queries.
