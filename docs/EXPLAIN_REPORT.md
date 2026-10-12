# Explain overlay: running report

Resume with `python tools/explain_dump.py WEEK 1 30` (prints pending trusted cards). Cards left on purpose are in `index/explain/skipped.tsv` (one line each, with the reason).

## Progress

| Week | Explained | Skipped by rule (uploader / no answer / reveal) | Left on skipped.tsv |
|---|---|---|---|
| 1 | 152 | 9 | 1 |
| 2 | 151 | 6 | 3 |
| 3 | 160 | 5 | 0 |

## skipped.tsv: disagreements and unreadable cards (no entry written)

- `2025-jan/w01/q10`: card A (18 away in x); simulating the script ends at x = 17 (option D). The card now carries a note disputing the key.
- `2024-jan/w02/q07`: card A; the code as shown has `i += 1` indented deeper than `print`, an IndentationError when run.
- `2025-jan/w02/q03`: card A,C; option D (`a = int(a)`) is not a way to read a decimal either. The card carries a note.
- `2025-jan/w02/q08`: could not explain: the picture shows a different program from the options (no `if` inside the `while`).

## Doubtful but explained (no contradiction with a note)

- `2018-jul/w01/q09@portal`: official `repeat until <key any pressed?>` for "as long as a key is pressed" (it actually loops until pressed).
- `2022-jul/w01/q07`: official `if` for "not related to the motion section"; `wait` is not a Motion block either.
- `2024-jan/w03/q05`: output is random; "some 1s and some 0s" is the usual result, not a certainty.
- `2023-jul/w03/q06@gpt`: options A–C each describe only part of the FizzBuzz output.

## To do after the last week

Weeks 1–3 were written before the rule "a wrong option that is a real Python output or code gets a line saying what code produces it". Some of their options are `null` where a line could be written; revisit them.
