# JOC practice site: plan

This replaces the topic-index / stats parts of [STEP3_INSTRUCTIONS.md](STEP3_INSTRUCTIONS.md). Product facts: [PRODUCT.md](PRODUCT.md).

## What the data looks like (measured 2026-10-11)

| Fact | Number | Consequence |
|---|---|---|
| Question records across `quizzes/*/week-*.md` | ~1,780 | ~150 per week across all years; render one week at a time |
| Questions with more than one correct option | ~90 | Multi-select with Submit is a real case, not an edge |
| Numeric / typed-answer questions (portal `Type: Numeric`) | 11+ | Need a text input + Check, not option buttons |
| Image files in `quizzes/*/img/` | 1,379 (~38 MB) | Lazy-load; fine for Vercel |
| Files carrying explanations/justifications | 26 (2026-jul, 2025-jul Scribd) | Show after answering |
| Official answers (portal prints) | ~700 records | Grade directly |
| Owner's PDF answers (2026-jul) | 240 | Grade directly, badge "From course PDF" |
| Everything else (YouTube, second repo, ChatGPT md) | ~840 records | Needs answer review (fewer after merging repeats) |

## Phase 0: Design direction (impeccable new-work) → **owner approves a mock**

- Mode: Operate (study tool). Phone-first, dark and light.
- Screens to mock: week view with question cards in every state (unanswered, correct, wrong, multi-select pending, numeric, image-only), filter bar, progress strip.
- Fixes over the ITNS app: instant check instead of "Show answer"; no marks/CO/due-date chips; question number not cluttered with source numbering; no blank page when a filter is applied.

## Phase 1: Dataset (`tools/build_dataset.py` → `site/data/`)

1. One parser per `kind` in `inventory.tsv`:
   - `portal_print_parsed`: `### Qn.`, `- [x]`, `Accepted answer(s): (Type: Numeric) 7`, crop images.
   - `youtube_transcription`: `**N) ...**`, `- [x]`, fenced code; Jul-2019 reads only the first section and applies its "Official accepted answers" section.
   - `second_repo_md`: `**N. ...**`, plain `- ` options, `✅` marks the author answer, `<img>` question images.
   - `chatgpt_converted_md`: `Correct Answer:` lines; broken `![[Pasted image]]` embeds are dropped and the question is flagged.
   - `case_study_pdf_md`: shared scenario becomes `context`, `**Answer: B**`, `> Justification:` becomes `explanation`.
2. Record fields: `id`, `term`, `week`, `num`, `src` (file + line), `kind`, `type` (`single` | `multi` | `numeric` | `reveal`), `context`, `text`, `code`, `images`, `options`, `answer`, `explanation`. Text is verbatim; normalised copies (`norm`) are used only for matching.
3. `reveal` type: options exist only inside an image and could not be transcribed. The card shows the image with a "Show answer" button instead of clickable options. Phase 3 shrinks this list by reading the crops.
4. Count checks per file (10 per portal week, 20 per 2026-jul week, header count otherwise). A `mismatch_report.md` lists every file whose count does not match, plus questions with no answer.
5. Output: `site/data/week-00.json` … `week-12.json` (lazy-loaded per week) plus a small `site/data/meta.json` (terms, counts). Deterministic: re-running gives identical files.
6. **Checkpoint:** the owner sees the mismatch report and two sample weeks rendered raw.

## Phase 2: Merge repeats (`tools/cluster.py`)

- Match key: normalised text + normalised code + sorted normalised options (option order changes between years, so the key ignores order).
- Exact match first, then fuzzy (rapidfuzz). The cut-off is set by eyeballing pairs scored 0.85–0.98, not fixed in advance.
- Near-duplicates (one number, one option or a `range()` bound differs) are never merged; they are listed in `index/near_duplicates.md`, and the site shows "similar question in 2022" links.
- Each merged group gets a stable id: a hash of its key, so saved progress survives rebuilds. The site shows the group once; the text comes from the best source (official > PDF > others); badges list every term it appeared in ("Asked 4×: 2019 Jul, 2021 Jan, …"); the answer comes from the highest-trust member.
- **Checkpoint:** at least 20 merged groups spot-checked against both sources.

## Phase 3: Answer review → `index/answers_review.tsv`

The review is kept in a separate file (`id, answer, badge, note`) that `build_dataset.py` applies last, so rebuilding never loses review work.

Badges, highest to lowest:
1. **Official**: NPTEL Accepted Answer (portal print, or the Jul-2019 official section), including when it comes from another year's copy of the same question.
2. **From course PDF**: 2026-jul answers as printed.
3. **Verified by running**: short pure-Python snippets executed in a subprocess with a timeout and stubbed `input()`; the output is stored and shown.
4. **Reviewed**: Claude's answer to the question. Uploader ticks are only a hint; a wrong one is silently replaced and never mentioned on the site.

Official answers are checked too (by running the code, or by reasoning). When an official answer is wrong or ambiguous (e.g. two options defensible, NPTEL accepted only one, or a question zero-weighted as in Jul-2019 Wk6 Q5), the card keeps grading with the official answer and shows a short **note** saying why it is wrong or ambiguous and what the correct reading is. This is the only kind of answer note on the site.

Work order: run all code questions first (cheap, objective), then review the remaining unofficial groups week by week, reading crops for `reveal` questions. **Checkpoint:** `index/official_notes.md` lists every official answer flagged as wrong or ambiguous (and official answers that differ between years) for the owner to approve before notes go live.

## Phase 4: Site (`site/`: static HTML, CSS, vanilla JS)

- **Navigation:** week rail (0–12) in a sidebar on desktop and a top bar on phones; year/session chips (multi-select); status filter (All / Unanswered / Wrong / Bookmarked); text search over the loaded week; sort (most repeated first by default, or newest first).
- **Cards:** scenario context collapsed above 2026-jul groups; images lazy-loaded with tap-to-zoom.
- **Code blocks** (a first-class element, designed in the Phase 0 mock):
  - Python syntax highlighting with a custom theme drawn from the site palette (light and dark), not a stock library theme. Highlighting runs at build time in `build_dataset.py` (Pygments emits class names), so there is no runtime library and nothing flashes in.
  - A good monospace font with ligatures off (so `==`, `!=`, `<=` read exactly as typed), tuned line height, and a line-number gutter that is not selectable.
  - Whitespace preserved exactly, since indentation is meaningful. Long lines scroll horizontally inside the block with a soft edge fade; the page itself never scrolls sideways on phones.
  - A Copy button (copies the code without line numbers).
  - Code that appears inside options (e.g. output choices) uses the same font inline, so expected output reads like terminal output.
  - Code that exists only as an image (second-repo questions) is transcribed into real code blocks during review where legible; otherwise the image is shown.
- **Interaction:**
  - `single`: tapping an option locks it, marks it right/wrong with an icon plus colour, and reveals the correct one.
  - `multi`: options toggle, "Select all that apply" is shown, and Submit grades each option (correct, missed, wrong pick).
  - `numeric`: input + Check.
  - `reveal`: Show answer.
  - After answering: badge, explanation or run output, the official-answer note when one exists, and source link.
  - "Try again" resets the card.
- **Progress:** localStorage keyed by group id holds the last answer, whether it was right, and the attempt count, all in try/catch. A per-week progress bar, a "Retry wrong" mode, and export/import as a JSON file (so progress can move between phone and laptop without accounts).
- **URL state:** `#w3?y=2024-jul,2025-jan&f=wrong` so links reopen the same view.
- **Accessibility:** options are real buttons/checkboxes, keyboard 1–4 to pick, Enter to submit, J/K for next/previous question; right/wrong never shown by colour alone; text-size control.
- **Performance:** only the current week's JSON is loaded, so ~150 cards render without virtualisation.

## Phase 5: Verify and ship

- Browser pass on desktop and phone widths: every question type, filters, retry mode, reload keeps progress, and a year filter never blanks the page.
- Run the impeccable detector and `impeccable audit` once.
- Deploy to Vercel with the root directory set to `JRG JOC/site`. Copy images into `site/img/` at build time (`build_dataset.py`), so the site folder is self-contained.

## Open decisions for the owner

- Licence / attribution before going public (quiz content is NPTEL course material; credit sources in an About page).
- Whether this lives in the current fork or the fresh repo planned in the README.
- Practice-exam mode (random 20 questions across weeks, timed): later, if wanted.

## Not doing

Topic tags, the stats report, programming assignments, OCR-only sources (Jul-2022 scanned print, exams), accounts or sync.
