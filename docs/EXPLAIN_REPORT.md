# Explain overlay: running report

Resume with `python tools/explain_dump.py WEEK 1 30` (prints pending trusted cards). Cards left on purpose are in `index/explain/skipped.tsv` (one line each, with the reason).

## Progress

| Week | Explained | Skipped by rule (uploader / no answer / reveal) | Left on skipped.tsv |
|---|---|---|---|
| 1 | 152 | 9 | 1 |
| 2 | 151 | 6 | 3 |
| 3 | 160 | 5 | 0 |
| 4 | 156 | 3 | 7 |
| 5 | 186 | 6 | 2 |
| 6 | 149 | 1 | 7 |

## skipped.tsv: disagreements and unreadable cards (no entry written)

- `2025-jan/w01/q10`: card A (18 away in x); simulating the script ends at x = 17 (option D). The card now carries a note disputing the key.
- `2024-jan/w02/q07`: card A; the code as shown has `i += 1` indented deeper than `print`, an IndentationError when run.
- `2025-jan/w02/q03`: card A,C; option D (`a = int(a)`) is not a way to read a decimal either. The card carries a note.
- `2025-jan/w02/q08`: could not explain: the picture shows a different program from the options (no `if` inside the `while`).

- `2023-jul/w04/q04@gpt`: card B (a magic square of size n); the code prints an n x n grid of random letters, not a magic square.
- `2020-jan/w04/q05`: card A only; option C (`for ch in range(len(ch))`) also prints one dash per letter.
- `2020-sep/w04/q03`: card B; option D `random.choice(string.ascii_uppercase)` gives the same result.
- `2021-jan/w04/q09@portal`: card 53,130; tracing gives at most 22 letter guesses; 53,130 = C(25,5) has no clear basis.
- `2022-jan/w04/q02`: card D; all four leap-year programs mishandle century years such as 1900.
- `2023-jan/w04/q02`: card B (N should be odd); 4 x 4 magic squares exist, odd N is only the lecture method.
- `2025-jan/w04/q04`: card A,C; option D (the first square times pi) is also a magic square, and the Jul-2024 copy accepts it.

- `2024-jul/w05/q01`: card D; option C (the same line ending in a semicolon) is also valid Python.
- `2025-jan/w05/q03`: could not explain: the card options are garbled (the portal accepts two answers, only one is recorded).

- `2023-jul/w06/q04@gpt`: card B (product of first n terms); the function returns only num*(num-1), with no recursion.
- `2020-sep/w06/q06`: card A (infinite loop); a missing base case raises RecursionError, a subclass of RuntimeError (option B).
- `2022-jan/w06/q06` and `2023-jul/w06/q06@gpt`: card B (infinite loop); recursive(L) with no base case raises IndexError on the empty list.
- `2022-jul/w06/q05`: could not explain: options C and D read identically in the card.
- `2026-jan/w06/q10`: card A; removing the recursive return line leaves only the first swap (option D).
- `2026-jan/w06/q14`: card B; reaching nine turns also ends the loop (option A).

## Doubtful but explained (no contradiction with a note)

- `2018-jul/w01/q09@portal`: official `repeat until <key any pressed?>` for "as long as a key is pressed" (it actually loops until pressed).
- `2022-jul/w01/q07`: official `if` for "not related to the motion section"; `wait` is not a Motion block either.
- `2024-jan/w03/q05`: output is random; "some 1s and some 0s" is the usual result, not a certainty.
- `2023-jul/w03/q06@gpt`: options A–C each describe only part of the FizzBuzz output.

## To do after the last week

Weeks 1–3 were written before the rule "a wrong option that is a real Python output or code gets a line saying what code produces it". Some of their options are `null` where a line could be written; revisit them.
