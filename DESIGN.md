---
name: JOC Past Quizzes
description: A Python-documentation edition of the NPTEL Joy of Computing past-quiz bank.
colors:
  page: "#ffffff"
  page-2: "#f6f8fa"
  ink: "#1d232b"
  ink-2: "#4c5663"
  ink-3: "#6b7480"
  rule: "#dde3ea"
  rule-2: "#c7d0da"
  python-blue: "#306998"
  blue-ink: "#234e74"
  blue-wash: "#e9f1f8"
  here-yellow: "#ffd43b"
  here-wash: "#fff8d6"
  ok: "#1a7f37"
  ok-wash: "#e7f5ea"
  bad: "#c4282f"
  bad-wash: "#fdeced"
  warn: "#a35200"
  warn-wash: "#fdf1e6"
  code-bg: "#f3fbe4"
  code-rule: "#d2e5b0"
  code-gutter: "#8a9a6e"
  dark-page: "#12171d"
  dark-page-2: "#181e26"
  dark-ink: "#e4e8ec"
  dark-ink-2: "#b2bbc5"
  dark-ink-3: "#8a94a0"
  dark-rule: "#26303b"
  dark-rule-2: "#34404d"
  dark-blue: "#7fb0dc"
  dark-blue-ink: "#a9cbea"
  dark-blue-wash: "#18283a"
  dark-here-wash: "#2c2810"
  dark-ok: "#5cc27a"
  dark-ok-wash: "#11281a"
  dark-bad: "#f2777c"
  dark-bad-wash: "#2f1517"
  dark-warn: "#f0a85a"
  dark-warn-wash: "#2a1f12"
  dark-code-bg: "#161f19"
  dark-code-rule: "#2b3b2f"
  dark-code-gutter: "#5e7262"
typography:
  headline:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.85rem"
    fontWeight: 650
    lineHeight: 1.2
    letterSpacing: "-0.015em"
  title:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 650
    letterSpacing: "0.04em"
  code:
    fontFamily: "JetBrains Mono, ui-monospace, Cascadia Mono, Consolas, monospace"
    fontSize: "0.86rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  sm: "3px"
  pill: "15px"
spacing:
  xs: "0.35rem"
  sm: "0.6rem"
  md: "1rem"
  lg: "1.6rem"
  topbar: "60px"
  toc: "250px"
  measure: "780px"
components:
  top-bar:
    backgroundColor: "{colors.page}"
    height: "60px"
    padding: "0 16px"
  toc-link:
    textColor: "{colors.ink-2}"
    rounded: "{rounded.sm}"
    padding: "0.42rem 0.5rem"
  toc-link-current:
    backgroundColor: "{colors.here-wash}"
    textColor: "{colors.ink}"
  chip:
    backgroundColor: "{colors.page}"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    height: "30px"
    padding: "0 0.65rem"
  chip-pressed:
    backgroundColor: "{colors.python-blue}"
    textColor: "#ffffff"
  segmented-selected:
    backgroundColor: "{colors.blue-wash}"
    textColor: "{colors.blue-ink}"
    rounded: "{rounded.sm}"
  option:
    backgroundColor: "{colors.page}"
    rounded: "{rounded.sm}"
    padding: "0.55rem 0.7rem"
  option-selected:
    backgroundColor: "{colors.blue-wash}"
  option-correct:
    backgroundColor: "{colors.ok-wash}"
  option-wrong:
    backgroundColor: "{colors.bad-wash}"
  button-primary:
    backgroundColor: "{colors.python-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    height: "36px"
    padding: "0 1rem"
  code-panel:
    backgroundColor: "{colors.code-bg}"
    rounded: "{rounded.sm}"
    typography: "{typography.code}"
  admonition:
    backgroundColor: "{colors.blue-wash}"
    rounded: "{rounded.sm}"
  admonition-warn:
    backgroundColor: "{colors.warn-wash}"
---

# Design System: JOC Past Quizzes

## Overview

**Creative North Star: "The Docs Edition"**

The question bank reads as an edition of the Python documentation: questions are entries, answering is evaluating. White page, near-black text, Python blue for ink, links and the index, hairline rules, a 3px radius, no shadows in the page itself. It refuses the rounded-card study-app look with confetti and score rings.

Dark theme is docs dark mode: deep blue-black, same roles, same structure. Theme follows the OS and can be overridden by a data-theme attribute.

**Key Characteristics:**
- Flat, ruled, document-like; depth comes from 1px rules and tonal washes.
- Proportional system sans for prose, JetBrains Mono for code and code-like options.
- Yellow is wayfinding only; green and red are verdicts only.

## Colors

Cool white and slate neutrals, one blue voice, one yellow marker, one green, one red. Dark values are the same roles remapped (dark-* keys).

### Primary
- **Python Blue** (python-blue): links, week numbers, question ids, selected state, primary button, pressed chip. Dark: dark-blue.
- **Blue Ink** (blue-ink) and **Blue Wash** (blue-wash): selected segment, hover and selected option, explanation admonition, repeat pill.

### Secondary
- **Here Yellow** (here-yellow, here-wash): the current week in the TOC (inset 3px left bar), the focused-question bar, text selection, and the second half of the logo mark. Nothing else.

### Neutral
- **Page / Page 2 / Ink / Ink 2 / Ink 3**: page, recessed panels and inputs, body text, secondary text, metadata. **Rule / Rule 2**: hairline dividers and control borders.
- **Code Panel** (code-bg, code-rule, code-gutter): pale Sphinx green-grey tint.
- **Semantic**: ok / bad (verdicts, option states, progress bar), warn (official-answer caveat).

### Pygments tokens (light / dark)
keyword and builtin #007020 / #6fcf8a; string #4070a0 / #8fb8e6; number #208050 / #7fd6b0; comment #408090 / #7fa4b0 italic; function #06287e / #b8c8ff; class/namespace #0e84b5 / #6cc7e8 bold; operator and decorator #666666 / #a5adb5; error uses bad.

### Named Rules
**The One Job Rule.** Each hue has one job: blue for ink and selection, yellow for "you are here", green for correct, red for wrong. Verdicts always pair color with an icon.

## Typography

**Body Font:** system-ui stack. **Code Font:** JetBrains Mono (with ui-monospace, Cascadia Mono, Consolas), ligatures disabled.

**Character:** a documentation page: neutral sans for reading, precise mono for anything the interpreter would see.

### Hierarchy
- **Headline** (650, 1.85rem, 1.2, -0.015em; 1.45rem on phones): week title; the week number is blue.
- **Title** (400, 1.05rem, 1.55): question text.
- **Body** (400, 1rem, 1.6): default; admonitions 0.92rem; metadata 0.8rem.
- **Label** (650, 0.78rem, +0.04em, uppercase): TOC heading only.
- **Code** (400, 0.86rem, 1.6): code panels, option text in mono, REPL result line, week numbers and ids at 600 0.82rem.

### Named Rules
**The No-Ligature Rule.** Code never uses ligatures; students must see exactly the characters typed.

## Layout

Two-column grid, max 1180px: 250px sticky TOC plus a main column capped at 780px, under a 60px sticky top bar (scroll-padding 76px). Rhythm in rem steps of about .35 / .6 / 1 / 1.6; question entries are separated by a 1px rule with 1.6rem padding, not boxed. Below 960px the TOC becomes a fixed off-canvas drawer (min(84vw, 320px)); below 640px the chip row scrolls horizontally, the brand subtitle and hints hide, and the headline shrinks. A user text-size control scales the root font size.

## Elevation & Depth

Flat. Hierarchy is carried by 1px rules and tonal washes. The only shadow is the mobile TOC drawer (`6px 0 24px rgb(0 0 0 / .12)`), and the zoom dialog backdrop is a 60% dark scrim.

### Named Rules
**The Hairline Rule.** All rules are 1px; no shadows on in-page surfaces.

## Shapes

3px radius on every control, panel and option; pill radius (15px) only for chips, with 9px mini-pills for the repeat count and badges. Dashed border marks "missed correct answer" and the clear-filter chip.

## Components

### Top bar
Sticky, page background, bottom hairline. Logo mark (blue and yellow), brand, search field (page-2 fill, blue border on focus-within), icon buttons 36px (transparent; hover page-2 plus hairline).

### Week TOC
Grid rows: mono blue week number, topic, small tabular count. Hover page-2. Current week: here-wash with inset 3px yellow bar. Bottom links are blue underlined text buttons.

### Chips and segmented control
Chip: 30px pill, hairline border, hover blue border; pressed is solid blue with white (dark: #0d1620) text. Segmented control: bordered 3px group, selected segment blue-wash with blue-ink semibold text.

### Option buttons
Full-width grid: mono letter tile, text, mark slot. States: hover blue border and wash; selected blue border, wash, blue letter tile; correct green border, wash, tile; wrong red equivalents; missed-correct green dashed border. Marks carry icons.

### Primary button
36px solid blue, white text (dark text on dark theme), 600 weight; ghost variant is transparent with blue text; disabled 45% opacity.

### Code panel
Two-column grid: right-aligned line-number gutter (not selectable) and scrollable pre, on the Sphinx tint with a right-edge fade when it scrolls; copy button appears on hover or focus.

### REPL result line
Mono. A grey `>>>` prompt followed by `answer("B")`, then the verdict row (icon plus Correct, or Not quite with the answer), an optional official/other badge, and a Try again link.

### Admonitions
Hairline-bordered 3px box; explanation is blue-wash with blue-ink bold title; "About the official answer" uses warn-wash and warn title. Scenario context is a collapsible details with page-2 fill.

## Do's and Don'ts

### Do:
- **Do** reserve yellow for current-week and focused-question markers.
- **Do** pair every correct or wrong state with an icon and color.
- **Do** keep controls at 3px radius and borders at 1px.
- **Do** define new colors as light and dark pairs that keep their role.

### Don't:
- **Don't** add card grids, score rings, confetti or celebratory motion.
- **Don't** use yellow, green or red as decoration.
- **Don't** add shadows to in-page surfaces.
- **Don't** enable ligatures in code.
