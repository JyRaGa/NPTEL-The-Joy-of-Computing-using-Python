# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

delegated: static HTML/CSS/vanilla JS on Vercel (free). A Python script in `tools/` generates `questions.json` from the week files; the page renders it client-side. Chosen because the owner's ITNS PYQ app already works this way and nothing here (filter, select, check, save progress) needs a framework or a Node build. Revisit Astro only if per-week static pages for SEO become a goal.

## Users

The owner first: an NPTEL "The Joy of Computing using Python" (IIT Ropar) student practising past weekly quizzes, for weekly assignments and final-exam revision. Later shared publicly with other JOC students. Expect phone use as well as desktop.

## Product Purpose

Every past JOC weekly-quiz question (2018 to 2026, Jan and Jul sessions) in one place, answerable in place: pick an option and immediately see if it was right; multi-answer questions have a Submit button. Success: a student can drill a week across all years and know which answers to trust.

## Positioning

The only bank that merges every source (portal prints with NPTEL Accepted Answers, YouTube transcriptions, other repos, the owner's 2026 PDFs) and says where each answer comes from, instead of copying one uploader's ticks, which are sometimes wrong.

## Operating Context

- Navigation by **Week** (0–12) and **Year/session** filter chips (reference: the owner's ITNS app at jrgsemv.vercel.app/ITNS_Study_App/ITNS_PYQ_Study_App, using Weeks instead of Units).
- Repeated questions across sessions are merged and show which sessions they appeared in.
- No marks or due-date tags.

## Capabilities and Constraints

- Question text, all options and code are verbatim from sources; never summarised or rewritten.
- Answer source shown as a badge: Official (NPTEL Accepted Answer), Verified by running (code executed), Reviewed (answer worked out by Claude; uploader ticks are only a hint and a wrong one is never mentioned). The only answer note on the site: when an official answer is wrong or ambiguous, explaining why.
- Code blocks are a first-class, elegant element: syntax-highlighted, exact whitespace, readable on phones.
- Image-only questions/options show the image (crops in `quizzes/*/img/`).
- Progress (answered, right/wrong, retry-wrong list) saved in the browser only; no accounts.
- Open: licence of quiz content (NPTEL course material) before going public.

## Evidence on Hand

`quizzes/<term>/week-NN.md` (214 files indexed in `inventory.tsv`), page crops and figures in `img/`. No testimonials, user counts or endorsements exist; do not invent any.

## Product Principles

1. Verbatim content; trust is labelled, never implied.
2. Instant feedback is the core loop: tap, see right/wrong, move on.
3. Drill by week, filter by year; repeats are a signal of exam importance.
4. Phone-first readability, including code blocks.

## Accessibility & Inclusion

Right/wrong must not rely on colour alone; keyboard-operable options; readable code at small widths; adjustable text size (as in the reference app).
