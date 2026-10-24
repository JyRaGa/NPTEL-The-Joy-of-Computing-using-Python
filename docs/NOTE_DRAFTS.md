# Draft notes for disputed answers

> **Applied** (index/fixes/notes.jsonl), except 2020-jan/w12/q04 (key correct for NetworkX 2+). Edited before applying: 2021-jan/w04/q09@portal, 2022-jul/w12/q07, 2026-jan/w08/q10.
Each note says what the key says and why another option is also right, or why the key is wrong, in the style of the note on `2021-jan/w02/q10@portal`. Code was run where it could be (NumPy, `datetime`, the `for`/`continue` loop, the magic-square sums, the Collatz and FLAMES checks); picture-only cards were read from the images.

| Card id | Week | Current answer | Draft note |
|---|---|---|---|
| 2024-jan/w02/q07 | 2 | A | The code as shown has `i += 1` indented deeper than `print`, which raises an IndentationError when run. The key describes the code as intended, with both lines at the same level. |
| 2023-jul/w04/q04@gpt | 4 | B | This question mixes two Week 4 projects. The code is Dobble code: like the lecture's `SameLetterCards.py`, it picks random letters from `string.ascii_letters` with `random.choice`, and here it prints them as an n × n grid. The options come from the magic-square project, but nothing in the code adds numbers or checks that rows, columns and diagonals have equal sums, so it does not make a magic square. The key says B, probably because the grid is n × n; in the exam, pick B. |
| 2020-jan/w04/q05 | 4 | A | The key accepts only A, but option C (`for ch in range(len(ch))`) also prints one dash per letter: `range(len(ch))` is worked out once, before the loop variable `ch` replaces the movie name. |
| 2020-sep/w04/q03 | 4 | B | The key accepts only B, but D (`random.choice(string.ascii_uppercase)`) also picks a random letter from A to Z: `random.choice` works on a string, so `list(...)` is not needed. |
| 2021-jan/w04/q09@portal | 4 | A | The key says 53,130, which is the number of ways to choose 5 letters out of 25, but nothing in the game uses that count. The guesses are single letters from a set of 26, so the number of guesses can never be that large. |
| 2022-jan/w04/q02 | 4 | D | The key picks D because it prints exactly one message for every year. D still reports 1900 and 2100 as leap years, since `year % 4 == 0` is true for them and nothing excludes multiples of 100. D is the best of the four, but no option is a full leap-year test. |
| 2023-jan/w04/q02 | 4 | B | The key says N must be odd, but magic squares of even order exist, such as the 4 × 4 square in the Jan-2024 Week 4 Q10. Odd N is a limit of the lecture's construction method only, so C (even or odd) is also defensible. |
| 2024-jul/w05/q01 | 5 | D | The key accepts only D, but C (the same assignment with a semicolon at the end) is also valid Python, because a semicolon may end a statement. |
| 2023-jul/w06/q04@gpt | 6 | B | The key says the function calculates the product of the first n terms, but it returns only `num * (num - 1)` with no recursive call. For 5 it gives 5 × 4 = 20, so it multiplies the last two terms and does not build a product of n terms. |
| 2020-sep/w06/q06 | 6 | A | The key says a missing base case gives an infinite loop. In Python the recursion stops with a `RecursionError`, which is a subclass of `RuntimeError`, so B is also right; the program does not run forever. |
| 2022-jan/w06/q06 | 6 | B | The key says the program runs into an infinite loop, but `recursive` has no base case. It calls itself on shorter lists until `L` is empty, and then `L[-1]` raises an `IndexError`, so the program stops with an error. |
| 2023-jul/w06/q06@gpt | 6 | B | The key says the program runs into an infinite loop, but `recursive` has no base case. It calls itself on shorter lists until `L` is empty, and then `L[-1]` raises an `IndexError`, so the program stops with an error. |
| 2022-jul/w06/q05 | 6 | C | Options C and D show the same binary search code, so D is correct as well as C. |
| 2026-jan/w06/q10 | 6 | A | The key says the list is still reversed but `None` is returned. Without the recursive return, only the first swap (first and last items) happens and the function stops, so the list is not fully reversed. D describes this. |
| 2026-jan/w06/q14 | 6 | B | The key says the game stops only when a winning condition is detected, but it also ends after nine turns, when the board is full, so A is also true. |
| 2019-jul/w07/q06 | 7 | B | The key lists (1,1), (1,2), (1,3), (1,4), (2,4), but a spiral over a 5 × 5 matrix goes on along the top row to (1,5) before it turns down, so (2,4) cannot follow (1,4). No option is a correct start of the spiral. |
| 2026-jul/w07/q20 | 7 | B, C | The key accepts B and C, but D is also true: the map markers are placed with an attraction's latitude and longitude, as the map questions in the same set show. |
| 2022-jul/w08/q04 | 8 | B, C | The key accepts B and C, but only compression (B) lets you store more images in small storage. Enhancement (C) changes how an image looks and does not make the file smaller. |
| 2026-jan/w08/q10 | 8 | B | The key says the simulation tends to show losses, but the game is fair: the expected change is 0.1 × 900 − 0.9 × 100 = 0 per day. Over 30 days about 41% of months end below zero, 24% at exactly zero and 35% above, so B is only the best of the four options. |
| 2026-jul/w08/q20 | 8 | A, B, C, D | The key marks all four statements correct, but the `Review` column is never changed (A is false) and the label comes from the compound score, not the length of the review (D is false). Only B and C are correct. |
| 2026-jul/w09/q05 | 9 | A, C, D | A is false: `len(tokens)` is the total number of tokens (20 in the program), while `len(freq)` gives the number of unique tokens (9). Only C and D are correct. |
| 2026-jul/w09/q10 | 9 | A, C, D | A is false: not every node has to be connected to every other node. In the program `Cloud` is joined only to `Data`. Only C and D are correct. |
| 2026-jul/w09/q15 | 9 | A, C, D | A is false: a path can pass through other users, so Alice and Carol are connected through Bob without a direct friendship. Only C and D are correct. |
| 2026-jul/w09/q20 | 9 | A, B, D | A is false: `getpixel()` only reads a colour, while `putpixel()` changes it. Only B and D are correct, which is also what the PDF explanation says. |
| 2018-jul/w10/q06 | 10 | B | `np.zeros(3,3)` raises a `TypeError`, because the second argument is the data type and 3 is not one. The 3 × 3 matrix of zeros in the key needs `np.zeros((3,3))`. |
| 2018-jul/w10/q07 | 10 | C | `shape` is an attribute that already holds the tuple `(2, 3)`, so `a.shape()` raises `TypeError: 'tuple' object is not callable`. The key is right for `a.shape`, not for `a.shape()`. |
| 2022-jul/w10/q04 | 10 | B | As shown, `b` is a tuple of a 1 × 2 array and a list, and `np.sum(b)` raises a `ValueError`. For the intended 2 × 2 array `np.sum(b)` is 10, and `[[4, 6]]` would be the column sums, `np.sum(b, axis=0)`. |
| 2024-jan/w10/q09 | 10 | C | The key accepts only `np.random.rand()`, but `np.random.random((rows, cols))` also makes a matrix of values between 0 and 1; it takes the shape as one tuple. |
| 2022-jul/w11/q04 | 11 | B | The key says `now()`, but `datetime.today()` (option C) also returns the current date and time. |
| 2021-jul/w11/q05 | 11 | C | The key says `now()`, but `datetime.today()` (option A, `today()`) also returns the current date and time, though `date.today()` gives only the date. |
| 2025-jan/w11/q05 | 11 | D | The key says the output is only `Found at index 3`, but running the loop prints `Checking 3` and `Checking 1` first (8 is skipped by `continue`), and then `Found at index 3`. That is option B. |
| 2024-jul/w11/q04 | 11 | C | The key accepts only `Keys.RETURN`, but `send_keys(Keys.ENTER)` (option A) also presses Enter. |
| 2019-jul/w12/q03 | 12 | C, D | The key says the rank depends on the rank of the pages the page refers to (C), but PageRank depends on the pages that refer to it. B and D are right and C is wrong. |
| 2020-jan/w12/q04 | 12 | D | `random.choice(G.nodes())` works only with old NetworkX, where `G.nodes()` was a list. In current versions it is a view indexed by node name, so `list(G.nodes())` is needed and D is right. The Jul-2022 card keys the opposite, so the two keys depend on the version. |
| 2022-jul/w12/q07 | 12 | C | `random.choice(A.nodes())` works only with old NetworkX, where `A.nodes()` was a list. In current versions it is a view indexed by node name, so `list(A.nodes())` is needed. The Jan-2020 card keys the opposite, so the key depends on the version. |
| 2022-jul/w12/q08 | 12 | A, C | B is also not true: the number of Collatz steps depends on the starting number (10 takes 6 steps, 75 takes 14). |

## Cards that already have a note (no draft)

- `2025-jan/w01/q10`: already notes the key (18) against the simulation (17).
- `2025-jan/w02/q03`: already notes that D is not a way to read a decimal either.
- `2019-jul/w12/q06`: already notes that NPTEL zero-weighted the question. Options A and D list the same sequence, which the note could mention.

## Cards on the skip list with no draft

- `2025-jan/w02/q08`: the code in the picture has no `if` inside the `while` loop that the options refer to, so I cannot say which option is right.
- `2025-jan/w05/q03`: the options in the card are garbled (the portal accepts two answers, only one is recorded).
- `2019-jul/w12/q07`: nothing in the card shows which method needs fewer iterations, so I cannot say the key is wrong.

## Noticed while filling option lines (not on the skip list)

| Card id | Week | Current answer | Draft note |
|---|---|---|---|
| 2024-jan/w03/q10 | 3 | A | The key accepts only A, but B describes the same behaviour in a different order (multiples of both 3 and 5 give "FizzBuzz", multiples of 3 give "Fizz", multiples of 5 give "Buzz"), so B is also correct. |
