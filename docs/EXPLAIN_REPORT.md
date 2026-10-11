# Explain overlay: running report

Resume with `python tools/explain_dump.py WEEK 1 30` (prints pending trusted cards). Cards left on purpose are in `index/explain/skipped.tsv`.

## Progress

| Week | Entries | Skipped by rule (uploader / no answer / reveal) | Left unexplained (disagreement) |
|---|---|---|---|
| 1 | 151 | 9 | 2 |
| 2 | 151 | 6 | 3 |

## Disagreements (card answer vs. my run/trace; no entry written)

- `2024-jan/w01/q09` — card B (Two); the code shows one loop block (`repeat 2`), so I count One.
- `2025-jan/w01/q10` — card A (stops 18 away in x); simulating the script ends at x = 17 (option D). Same script as `2024-jul/w01/q10` (card D, 20 for `repeat 21`) shifted by one.

- `2024-jan/w02/q07` — card A; the code as shown has `i += 1` indented deeper than `print`, which is an IndentationError when run.
- `2025-jan/w02/q03` — card A,C ("not correct ways to read a decimal"); option D (`a = int(a)`) is not a way to read a decimal either.
- `2025-jan/w02/q08` — could not explain: the picture shows a different program from the options (no `if` inside the `while`).

## Doubtful but explained (no contradiction with a note, flagged for a human look)

- `2018-jul/w01/q09@portal` — official answer `repeat until <key any pressed?>` for "as long as a key is pressed" (it actually loops until pressed).
- `2022-jul/w01/q07` — official `if` for "not related to the motion section"; `wait` is not a Motion block either.
