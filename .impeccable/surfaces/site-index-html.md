---
version: 1
slug: "site-index-html"
primary_target: "site/index.html"
related_targets: []
---

Scope: site/index.html, the whole practice app (Operate mode). Audience/job: JOC students drilling past weekly quizzes by week, filtered by year; instant grading; progress in browser.

## Direction contract

THESIS: The bank is an edition of the Python documentation, not a quiz app: questions are doc entries, answering is evaluating. Refuses the rounded-card study-app grid with confetti and score rings.

OWN-WORLD: Python docs world. White page, near-black body text, Python blue (#306998 family) for ink, links and the index; Python yellow (#FFD43B family) reserved only for "you are here" (current week, focused question). Code in pale docs panels (classic Sphinx green-grey tint), custom Pygments token palette, a proportional docs sans for body, a refined monospace (JetBrains Mono, ligatures off) for code and output options. 1px hairline rules, no shadows, small radius 3px. Correct = one green, wrong = one red, always with an icon. Dark theme = docs dark mode (deep blue-black, same roles). Raises: one colour reserved for one job (from the terminal-yellow wayfinding challenger); three ink values plus one rubric accent, all rules at 1px (from the centre-rail reference-setting challenger).

STORY: A student opens Week N, sees every year's questions in order of how often they were asked, answers, sees right/wrong and the official note, and can retry the wrong ones later.

FIRST VIEWPORT: Desktop: left sidebar = table of contents "Weeks 0–12" with progress counts, current week marked yellow; top bar = site title, search, text size, theme; under it a row of year chips and a status filter. Main column (max ~760px): "Week 3: Lists, conditionals, loops" heading, one-line progress, then the first question entry. Phone: the sidebar becomes a week picker in the top bar; chips scroll horizontally.

FORM: Python documentation edition; position 4 of the grounded list; seed key 29d82a49. Signature interaction: answering prints a REPL-style result line under the question (">>> answer(B)" then a check or cross with the correct option), with an expanding note/explanation like a docs admonition.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
