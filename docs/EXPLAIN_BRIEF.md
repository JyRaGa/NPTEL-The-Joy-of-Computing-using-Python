# Brief: explain every answer after the user responds

Paste this as the task for a fresh session (Sonnet, high effort). It is a long, overnight job: work in the repo root (`JRG JOC/`), commit and push after every week, and keep going until all weeks are done or you run out of budget. It must be resumable: a later session continues where you stopped.

## Goal

Today, after a user picks an option (or submits), the card shows:

```
>>> answer("C")
✗ Not quite. Answer: B   [Official answer]   Try again
```

and nothing else (except a few notes on disputed official answers, and 200 Jul-2026 cards that carry the PDF's justification).

Add, below that line, a short teaching block for every card:

1. **Why the right answer is right**: 1–3 plain sentences a first-year student understands. For code questions, trace the code briefly (what each step does, what gets printed). For theory questions, state the fact and why it holds.
2. **The other options**: for each wrong option, one line that turns it into something useful: the question it *would* be the right answer to, or the small change to the code/question that would make it correct. Example: for "What does `len('hello')` return?" with wrong option `4`, write "Would be the answer for `len('hell')`." If a wrong option has nothing to do with Python or programming (a distractor like "None of the above", "Cannot say", an unrelated word or a joke option), give it no line (`null`). Do not write "this is wrong because…" filler.

## Where the data goes

**Do not edit the generated `site/data/week-NN.json` by hand.** It is rebuilt from sources and overlays.

- New overlay files: `index/explain/week-NN.jsonl`, one JSON object per line, UTF-8, no BOM (write with Python, never PowerShell):
  ```json
  {"id": "2021-jan/w02/q10@portal", "why": "…", "options": {"B": "…", "C": "…", "D": null}}
  ```
  - `id`: the card's `id` field (its first source id). Any of the card's `members` ids also works, the same way `index/fixes/*.jsonl` is keyed; use `id`.
  - `why`: string.
  - `options`: letters as shown on the card (A, B, C…) for the **wrong** options only; value is the one-line string or `null`.
- `tools/cluster.py`: load all `index/explain/*.jsonl` (like it loads `index/fixes/*.jsonl`) and attach the entry to the matching card as `g["explain"]` (match on the card id or any member id). If a card has both an old `explanation` (Jul-2026 PDF justification) and an `explain`, keep both in the data.
- `site/app.js`, function `paint()` (around the `g.note` / `g.explanation` lines): after the note, render `g.explain` as one block in the existing admonition style (`<div class="adm">…`):
  - heading `Why <correct letters>` with the `why` text;
  - then a compact list `<ul class="why-opts">` with one `<li><b>A</b> text</li>` per non-null option line;
  - when `g.explain` exists, do not also show the old `Explanation` block (the new one replaces it); otherwise keep the old behaviour;
  - run all text through the existing `rich()` helper (it already renders `` `code` `` and `**bold**`) after `esc()`-safe handling: check how `rich()` escapes before using it, and never inject raw HTML from the data;
  - add the minimal CSS to `site/style.css` (list spacing only, reuse existing tokens; no new colours).
  Do this code part first, test it on two or three cards, commit, then start writing explanations.

## Which cards

All weeks 0–12, every card with a **trusted answer**: `answer_source` in `official`, `run`, `reviewed` and a non-empty `answer`.

- Skip `uploader` (Unverified) cards and cards with no answer: explaining an unchecked answer would teach a possibly wrong fact.
- `numeric` cards: write `why` only (no options).
- `reveal` cards: skip.
- `multi` cards: `why` covers every correct option; `options` covers the wrong ones.
- Cards with a `note` (a disputed official answer, e.g. Week 2 Q55 var-1, Week 10 transpose): the `why` must agree with the note, never contradict it.
- Cards that repeat across sessions are one card: write one entry.

## How to write them (accuracy first)

- **Read the whole card**: `text`, `code`, `context` (scenario text/code), `images`, `stem` pictures, option `img`/`code`. If the code is only in a picture (`stem`, `images` or `crops`), open the picture with the Read tool before writing. Never explain code you have not seen.
- **Run the code whenever it is runnable** (plain Python snippets): put it in a scratch file in your scratchpad and run it with `python -I`. If your run disagrees with the card's answer, do not write an entry: list the card in your report instead (`id`, card answer, your run's output). Turtle, Scratch, file and network code: trace by reading.
- Verbatim stays verbatim: never change question text, options or answers. The overlay only adds explanation text.
- Never mention video uploaders, ticks, other answer sources, or "the official key is wrong" (that is what `note` is for).
- Style: plain English, short sentences, present tense, no "Great question", no "Option B is incorrect because" padding, no hedging ("might", "probably") unless the topic is genuinely uncertain. Use `` `backticks` `` for code, names and outputs. `why` ≤ 60 words; each option line ≤ 25 words.
- Theory questions about the course's own material (Scratch, Monty Hall, magic squares, PageRank, FLAMES, Dobble, etc.): explain from the concept, not "as said in the lecture".

Examples (real cards):

```json
{"id": "2021-jan/w02/q10@portal", "why": "`var-1` is read as `var` minus `1`, so `var-1 = 5` is a SyntaxError: a name may only contain letters, digits and `_`, and cannot start with a digit.", "options": {"B": "`var1` is a valid name: letters then a digit.", "C": "`Var1` is valid too; names are case-sensitive, so it differs from `var1`.", "D": "`var 1` also breaks the rule (no spaces allowed); see the note above."}}
{"id": "2020-jan/w01/q03", "why": "`t` starts at 0 and `change t by -1` runs 10 times, so `t` ends at 0 − 10 = `-10`.", "options": {"A": "Would be the answer if the loop ran 0 times (`repeat 0`).", "B": "Would be the answer for `change t by 1`.", "D": null}}
```

(Option lines may describe valid alternatives, as for B and C above, when that is the most useful thing to say.)

## Workflow (per week, resumable)

1. Dump the week's pending cards compactly (write a small helper `tools/explain_dump.py WEEK` that prints, for each trusted card without an entry yet: card number, id, type, text, code/context code, options with letters, answer letters, note, and the paths of any images/stems). Read it in chunks of ~20 cards.
2. Write entries for the chunk, appending to `index/explain/week-NN.jsonl` (one Python write per chunk).
3. Validate with a small checker (add it to the dump helper or `tools/audit.py`): every line parses, every `id` matches a card, every option letter exists on that card and is not a correct answer, no entry for skipped card types, length limits respected.
4. After the week: `python tools/cluster.py`, then the official-answer check below (must print `official lost []`).
5. **Browser pane check** (the local server is `http://localhost:8765/site/#wN`; start it with `preview_start` config `joc-site` if needed; bust cache with `await fetch('data/week-NN.json',{cache:'reload'}); location.reload()`): answer at least 5 cards of that week (one wrong pick, one right pick, one multi, one with code, one with a note if any), screenshot each result block, and confirm the text renders (code formatting, no raw `**` or HTML, no layout overflow on a 375px mobile viewport via `resize_window`). Reset the viewport to desktop and clear the answers you made (`localStorage.removeItem` of the site's progress key, or "Try again").
6. Commit `index/explain/week-NN.jsonl` + rebuilt `site/data` and push. Message: `Explanations: Week N (X cards)`. End commit messages with the attribution line from the session's system reminder.

Order: Week 1, 2, 3 … 12, then Week 0. Week sizes: 100–200 cards each, ~1,900 cards in all; budget your effort so quality stays constant (do not get terser later in the night).

Official-answer check (run from the repo root after every rebuild):

```bash
python -c "import json,subprocess;L=lambda r:{m:(g['answer_source'],bool(g['answer'])) for w in range(13) for g in json.loads(subprocess.run(['git','show',f'{r}:site/data/week-{w:02d}.json'],capture_output=True,text=True,encoding='utf-8').stdout if r else open(f'site/data/week-{w:02d}.json',encoding='utf-8').read()) for m in g['members']};a,b=L('HEAD'),L(None);print('official lost',[k for k in a if a[k]==('official',True) and b.get(k)!=('official',True)])"
```

## Using the site in the browser pane

The tools are `mcp__Claude_Browser__*`. Prefer `javascript_tool` to drive the page and read state (cheap, exact), and take a `computer` screenshot only to judge how something looks. Screenshots at `scale: 0.5` are enough; zoom with the `zoom` action if text is small.

**Open it.** Local server: `http://localhost:8765/site/` (if it is not running, `preview_start` with name `joc-site`). The live site (https://joc-jrg.vercel.app/site/) only updates after a push and Vercel deploy; check local first.

**Fresh data after a rebuild.** The browser caches `data/week-NN.json` and `app.js`. After every rebuild or code edit:
```js
for (const f of ['app.js', 'style.css', 'data/week-05.json']) await fetch(f, {cache: 'reload'}); location.reload();
```
Then wait ~1.5 s in the next call (`await new Promise(r => setTimeout(r, 1500))`) before touching the page. If a script returns "the page navigated", that is the reload; just continue in a new call.

**Page layout and URL.** The URL hash holds the view: `#w5` (Week 5), `#w5?f=wrong` (filter), `&y=2024-jul` (sessions), `&s=new|old` (order), `?g=<gid>` (jump to one card). Set it with `location.hash = '#w5'`. Top bar: `#menu` (week drawer `#toc`, links `#weeks a`), `#q` (search all weeks), `#theme` (light/dark), `#smaller` / `#larger` (text size). Under the week title: `#summary`, the "Sessions: …" dropdown (`.sess-pick`, chips `#years [data-year]`; `data-year=""` is All), the filter buttons `#status [data-f="all|todo|wrong|saved"]` (selected one has `aria-pressed="true"`), the order `<select id="sort">`. Cards are in `#list`; the bottom has the answer-label legend `.legend`.

**A card** is `article.q` with `data-gid`. Inside: `.q-id` (text like `Q12¶`; the number is the card's position in the current order), `.q-text`, optional `details.ctx` (Scenario), `.q-imgs img` (figures and stem pictures), `.code` panels, `ol.opts` with `button.opt[data-i="0..n"]` (A = 0), `.actions` (buttons below), `.result` (the answer block you are adding to), `.save` (bookmark), `details.src` (Original portal page).

Find and show a card by its number:
```js
const card = n => [...document.querySelectorAll('.q')].find(q => q.querySelector('.q-id').textContent.replace('¶','') === 'Q' + n);
const q = card(12); q.scrollIntoView(); scrollBy(0, -60);
```
Or by source id: read `data/week-NN.json`, find the card with that `id`, then `document.querySelector('.q[data-gid="' + g.gid + '"]')`.

**Answering** (what a user does):
- single choice: `q.querySelector('.opt[data-i="2"]').click()` grades at once;
- multi choice: click each option, then `q.querySelector('[data-submit]').click()`;
- numeric: `const i = q.querySelector('[data-num]'); i.value = '42'; i.dispatchEvent(new Event('input', {bubbles: true})); q.querySelector('[data-check]').click()`;
- reveal: `q.querySelector('[data-reveal]').click()`.
Then read the result: `q.querySelector('.result').innerText` (the `>>> answer("C")` line, verdict, your explanation block). Images load lazily: after scrolling, wait ~800 ms before a screenshot.
- Undo: `q.querySelector('[data-again]').click()` ("Try again").
- Keyboard (focus a card first by clicking its text): `j`/`k` next/previous card, `1`–`8` pick an option, `Enter` submits a multi.

**Several cards in one screenshot** (saves tokens): hide every other card, then screenshot:
```js
const keep = new Set(['Q3','Q12','Q40']);
document.querySelectorAll('.q').forEach(q => q.style.display = keep.has(q.querySelector('.q-id').textContent.replace('¶','')) ? '' : 'none');
document.querySelectorAll('.q img').forEach(i => i.loading = 'eager'); document.querySelector('#list').scrollIntoView();
```
A reload restores the page.

**Mobile.** `resize_window` with `preset: 'mobile'` (375×812, emulates touch), reload, check, then `preset: 'desktop'` before you finish. Look for text overflowing the card and code panels wider than the screen (`document.documentElement.scrollWidth > innerWidth` must be `false`).

**Dark theme.** `#theme` toggles it (stored in `localStorage['joc:theme']`); check one result block in both themes.

**Clean up your test answers.** Progress lives in `localStorage['joc:v1']` (`{a: answers, s: saved}`). After testing, `localStorage.removeItem('joc:v1'); location.reload()` so the owner's browser is not left with your clicks. Never touch other keys.

**Errors.** `read_console_messages` with `onlyErrors: true` after each week; a JS error in `paint()` silently breaks every card's result block.

## Report back (at the end, or when stopping)

- Weeks done, cards explained per week, cards skipped by rule (uploader / no answer / reveal).
- **Disagreements**: every card where running or tracing the code gave a different answer from the card's answer (`id`, card answer, what you got, one line why). Do not "fix" answers yourself.
- Cards you could not explain (code unreadable, figure missing) with ids.
- Where to resume.
