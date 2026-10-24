# JOC deck audit: knowledge lost in compression

One line per loss: file | card or lesson | lost point | suggested fix

## audit_p1a.txt

- p1a.md | 2024-jul/w05/q03 | Monty Hall: `3*((3**89)+3) % 3 == 0` and `(2**90) % 3 == 1` are also true switch conditions (bullet lists only some). | Add both to the Truthiness Monty Hall bullet.
- p1a.md | 2025-jan/w05/q03 | Reason: switching wins 2 in 3 because the first pick is right only 1 in 3; `2*(2**89+7) % 2 == 0` is true (even product); `(2**90) % len(doors) != 1` is false. | Extend the Monty Hall bullet with the 1-in-3 reason and these two expressions.
- p1a.md | 2026-jan/w06/q12 | Tic-Tac-Toe: input `2` (no comma) gives a one-item list from `.split(',')`, so `len(move) != 2` prints `Invalid input.` and `continue` asks again. | Set `fact:` on the card or add to the map/split bullet.
- p1a.md | 2019-jul/w02/q02 | Two loops using `end=""` (0,1 then 4,5) print `0145` on one line. | fact: Two loops with `end=""` print `0145` on one line.
- p1a.md | 2022-jan/w01/q04 | Off-by-one: `while t <= 5` with print then `t += 1` prints 0..5 and stops once t is 6. | Add to Counting loop passes bullet.
- p1a.md | 2018-jul/w02/q06@portal | Doubling `answer` from 1 over 5 passes gives 2,4,8,16,32 (baseline: same as starting 2 and doubling 4 times). | Add to accumulator bullet.
- p1a.md | 2021-jan/w08/q04@portal | A `while x != random_number` guessing loop stops exactly when the input matches the random number. | Add to the break/loop-condition bullet.
- p1a.md | 2020-sep/w03/q01 | A loop that prints each item but substitutes `jaggery` for `sugar` outputs coffee, jaggery, cheese, butter. | Low value; fact: or leave.
- p1a.md | 2025-jan/w01/q04 | Trace: `myNum` starts at 7 and drops 1 per pass over 7 passes, ending at 0. | Low value; leave unless counting-loop trace wanted.
- p1a.md | 2023-jul/w02/q07@gpt | Sum of i = 0..9 added to b starting at 0 gives 45. | Low value; add to accumulator bullet if desired.
- p1a.md | 2024-jul/w01/q06 | Variables store/retrieve values; saving to disk needs files, repeating needs loops, parallel work needs threads. | Low value; add a half-clause to the uses bullet.

## audit_p1b_p4_p8.txt

- p1b | 2023-jan/w12/q02 | The subtract-32 loop converts only lowercase letters and drops every other character (contrast with 2021-jan/w08/q08 which keeps them); card has no fact line so its why is not shown. | add fact: `-32` inside an `'a'<=c<='z'` test uppercases letters and drops all other characters.
- p1b | 2019-jul/w06/q05 | A recursive palindrome check compares `s[0] != s[-1]` (first vs last character); card has no fact line and no code so nothing renders. | add fact: recursive palindrome test compares `s[0]` with `s[-1]`; other indexes overrun or miss the first character.
- p1b | 2023-jul/w02/q04@gpt | Text to print needs quotes and the call needs brackets: `print('The joy of computing')`; dashed and not in any lesson bullet. | add to Writing a string: printed text needs quotes and `print(...)` needs brackets.
- p1b | 2025-jan/w03/q01 + 2024-jul/w03/q01 | Lists have no 1024-item limit and a `for` loop can iterate over a list. | add to What a list is: no size limit (not 1024); `for` can loop over it.
- p1b | 2026-jul/w03/q05 | `len(L)` is the total items; `count(x)` only gives copies of one value. | add to builtin bullet: `len` = all items, `count(x)` = copies of x only.
- p1b | 2019-jul/w06/q03 | The split('a') loop prints pieces each followed by a space: `Wh t will h ve so will`. | add to split bullet the printed form `Wh t will h ve so will`.
- p1b | lesson: Slices | Step example positions: `s[2:15:3]` takes positions 2,5,8,11,14; `'abcdef'[::2]` is `ace`. | minor: add positions list to the table row.
- p1b | 2022-jul/w03/q06 | `total()` and `numberof()` do not exist; use `count`/`sum`. | minor: add to list builtin bullet.
- p4 | lesson: Tuple traps | `((1), (2))` is `(1, 2)` (brackets alone make no tuple), and `del t` (whole name) is allowed while `del t[2]` is TypeError. | add both to Tuple traps bullets.
- p4 | lesson: Loop traps | Why `while n != 0: n //= 10` never ends for negative n (`-1 // 10` stays -1) and why `while n >= 0` never ends (n reaches 0 and stays). | add reasons in a few words each.
- p4 | lesson: Recursion and empty lists | Quiz options may call a missing base case an "infinite loop"; correct term is RecursionError. | add: options may say "infinite loop"; answer is RecursionError.
- p4 | lesson: NetworkX traps | `import network as nx`, `G.add node(1)` (space) and `nx.draw()` with no graph all raise errors. | add one bullet listing these three.
- p4 | lesson: Turtle near misses | Wrong variants: `range(3)` with `right(60)` draws half a hexagon; `range(6)` with `right(30)` turns only 180 degrees so the shape does not close. | add the two wrong variants to Turtle bullet.
- p4 | lesson: Prime and perfect-number near misses | Swapping `True`/`False` or writing `!=` inverts a perfect-number test; only `range(2, i)` with `i` from 2 is a correct prime loop. | add to the perfect/prime bullets.
- p4 | lesson: Writing a pattern file | Looping `range(len(letters))` writes 26 lines instead of 13; writing to a file opened with `'r'` errors. | add to Writing a pattern file.
- p4 | lesson: Star patterns | Rows going up only form a triangle; up then down forms a diamond. | add "up only = triangle".
- p4 | lesson: Bounds of random functions | `random.shuffle` may leave the same order; `random.choice(0, len(movies))` is a wrong call (needs one sequence). | add "may leave same order".
- p4 | lesson: Strings cannot be changed | Strings have no `append` or `insert` method (only `upper`, not `uppercase`). | minor: add `append`/`insert` to the AttributeError bullet.
- p4 | lesson: Dictionary traps | `d.values().count(x)` also fails (view), and `1` stays as the kept key spelling. | minor.
- p8 | lesson: Searching and sorting | Bubble-sort swaps equal inversions = pairs in the wrong order (definition dropped). | add "(pairs out of order)".
- p8 | lesson: Counting arrangements | Jumbled-word `n! - 1` means all orders except the real word. | add "(all orders but the real word)".
- p8 | lesson: Calendar results | `monthrange(2024, 2)` is `(3, 29)` because 1 Feb 2024 is a Thursday; `monthcalendar` index 4 Fri, 5 Sat. | minor: add "1st is Thursday".

## audit_p1c.txt

- p1c.md | 2021-jul/w08/q08 -> 2021-jul/w05/q08 | Binary search takes about log2(n) steps whether the list is ascending or descending; sort direction only changes which half is kept. | Add to Binary search bullet: "works on ascending or descending order alike".
- p1c.md | 2019-jan/w08/q07 | On a tuple `t`, any `t[i] = x` is a TypeError (including `t[len(t)-1]`), and an index past the end (`t[4]` on 4 items) does not exist (IndexError). The card sits in the dictionary section with fact `-`. | In "Tuples cannot be changed" add: "any index assignment fails, even the last item; an index past the end is IndexError".
- p1c.md | 2020-sep/w08/q01 | `t1 + t1` on two 5-item tuples gives a new 10-item tuple (len 10); brief and fact are both `-`. | Set `brief: t1 + t1 builds a new tuple of 10 items; len works on tuples.`
- p1c.md | 2024-jul/w06/q03 and 2025-jan/w06/q03 | Worked results of the redefined-function cards (func(5) = 8 with x + y, y = 3; func(5) = 26 with 5**2 + 1) are not shown; only the generic "later def replaces" rule survives, and that rule sits in 1.12 not in the recursion-on-lists section. | Set `brief: The second def func replaces the first, so func(5) is 8 (x + y, y = 3)` / `... is 26 (5**2 + 1).`
- p1c.md | 2025-jan/w06/q01 | `mystery(n) = n + mystery(n-1)` stopping at 0 is the sum 1..n (for any n); table row only shows `recursive(a-1)` and 55. | Fine if table row is generalised to "1 + 2 + ... + n (10 gives 55)"; low priority.
- p1c.md | practice (1.14, f.read() after open 'w') | Python raises `io.UnsupportedOperation` (not just "an error"); use `'r+'` to read and write. Card has no code and fact `-`, so nothing renders. | Add to table row `'w'`: "`read` raises UnsupportedOperation; use `'r+'` for both".
- p1c.md | 2026-jul/w08/q02 | A tuple keeps item order but does not sort its items. | Add "ordered does not mean sorted" to "What a tuple is" bullet 1.
- p1c.md | 2019-jul/w08/q01 | `print(t[i])`, `max(t)`, `len(t)` only read a tuple and never raise errors (only `t[3] = 45` fails); fact `-`. | Already implied by "Reading works as for lists"; optional: add "reading never errors".
- p1c.md | 2023-jul/w05/q01@gpt | Quick sort beats bubble AND insertion sort (both quadratic); insertion sort is not named in the lesson. | Add "insertion sort is also about n squared" to the Fastest sort bullet.
- p1c.md | 2018-jul/w08/q09 | `[]` is the empty list as well as `{}` empty dict (and `()` empty tuple); only `{}` and `()` appear. | Add "`[]` is the empty list" to the "Empty and one-item tuples" first bullet or the bracket-types bullet.

## audit_p2a.txt

- p2a.md | 2026-jul/w11/q20 | A program prints the last Friday (`fridays[-1]`) only if `len(fridays) >= 4`, otherwise prints `Insufficient Fridays`; only `fridays[-1]` is taught. | In monthcalendar bullets add: a guard like `len(fridays) >= 4` decides whether a last Friday is printed.
- p2a.md | 2024-jul/w11/q09 | Leap year rule for 2024: divisible by 4 and not by 100; lesson only states the 100/400 exception for 2100. | In Leap years bullet: "leap if divisible by 4, except centuries unless divisible by 400".
- p2a.md | 2023-jul/w11/q04 | `now()` prints year-month-day hours:minutes:seconds.microseconds (e.g. 2026-10-12 23:34:33.760029); the output format is no longer shown. | Today and now bullet: add "prints like `2026-10-12 23:34:33.760029`".
- p2a.md | 2021-jul/w11/q09 | `calendar.month` needs numeric arguments; a month name like `Oct` is invalid. | Calendar table note: "month is a number, not a name".
- p2a.md | lesson: UTC and local time | `utcnow()` is replaced in new code by `datetime.now(timezone.utc)`. | Append "(newer: `datetime.now(timezone.utc)`)" to the utcnow bullet.
- p2a.md | lesson: Mean, median and trimmed mean | Plain definitions of mean (sum divided by count) and median (middle of sorted data) were dropped, only examples remain. | Add "mean = sum / count; median = middle of sorted data" to the first bullet.
- p2a.md | 2020-sep/w04/q03 | `ascii_lowercase` has only lowercase letters (only `ascii_letters` is mentioned). | Extend the choice string bullet: "`ascii_lowercase` is a-z only".

## audit_p2b.txt

- p2b.md | 2021-jan/w10/q09 | Wrong column-sum names `a.col` and `np.colsum` do not exist (only `np.sum(a, axis=0)`). | Add "`a.col` and `np.colsum` do not exist" to the sum-axis lesson line.
- p2b.md | 2023-jul/w07/q04 | A hexagon can also be drawn by a loop of 3 passes each doing two forward(60)+right(60) pairs (6 sides, 60 degree turns). | Give it `brief: Three passes of two forward 60 + right 60 steps still draw six sides: a hexagon.`
- p2b.md | 2022-jul/w07/q07 | The GPS program tracks the user's path/route (what the route drawing is for). | Add "it tracks the user's route" to the GPS route lesson sentence.
- p2b.md | 2021-jul/w07/q01 | Renaming a file would need `os.rename`; `save` never renames. | Append "renaming needs `os.rename`" to the save sentence.
- p2b.md | lesson: Making an array / asarray | Baseline example: `np.asarray([(1, 2), (3, 4)])` gives a 2 x 2 array from a list of tuples (output no longer shown). | Add output `[[1 2] [3 4]]` to the asarray lesson line.
- p2b.md | lesson: What turtle is | `turtle.done()` keeps the window open at the end (the lesson now only says it ends the program). | Say "`turtle.done()` keeps the window open".
- p2b.md | 2026-jul/w09/q02 | Worked example showed both `len(tokens)` and `len(freq)` on the review text; the brief gives only unique count 9 (total token count not stated). | Add "`len(tokens)` counts all tokens (here more than 9)" to brief, or compute the number.
- p2b.md | 2026-jul/w08/q18 | The `apply` step leaves the review text unchanged and only adds a new `Sentiment` column. | Add "the original column is unchanged" to the apply lesson line.
- p2b.md | 2020-sep/w08/q08 | VADER lives in `nltk.sentiment` (import path). | Add "from `nltk.sentiment.vader`" to the VADER lesson.
- p2b.md | 2024-jan/w09/q11 | PIL is sometimes written "Image" for Python Imaging Library (all three statements true). | Optional: mention in What PIL is.

## audit_p2c_p3a_p3b.txt

- p2c | 2019-jan/w09/q09 | A graph where node 1 has edges to 2, 3, 4, 7, 9 and every node has an edge is connected (reach all from one node). | Add to "Random graphs and connectivity": "if one node reaches all others, it is connected."
- p2c | 2024-jan/w09/q05 | Nodes come from `range(1, 6)` (1 to 5), and 5 nodes have 10 possible pairs. | Extend its brief: "`range(1, 6)` gives nodes 1-5; 10 edges = all pairs."
- p2c | lesson: Picking a random node | Older code wrote `random.choice(A.nodes())`; newer needs `list(...)` first. | Add "(older `A.nodes()` form)" to the random-node bullet.
- p2c | 2019-jan/w09/q03 | `G.nodes()` returns the nodes, not a count (count is `len(G.nodes)` / `number_of_nodes()`). | Lesson bullet "Counting" already near; add "`G.nodes()` is not a count".
- p3a | 2021-jan/w02/q09@portal | Natural numbers in decreasing order from 7 (sequence card, `fact: -`, why generic). | Misfiled programming card; confirm it is taught in its own week part, else add a fact.
- p3a | 2020-sep/w02/q10 | A `while` body that never runs while an `if` branch prints 20 (loop never-executes trap). | Misfiled; confirm covered in the while-loop part, else add `fact:`.
- p3a | 2025-jan/w02/q02 | Option D lacks a space after `to`: `Ramesh talks toSuresh and Kamlesh` (print spacing trap). | Misfiled; confirm covered in the print/string part.
- p3a | 2020-jan/w05/q09 | Loop `break` condition is an even roll (dice loop). | Misfiled; confirm covered in the break part.
- p3a | 2026-jul/w03/q14 | A loop repeats the same instructions for each number 1 to 30 (loop-vs-primes). | Misfiled; low value, may drop.
- p3b | 2021-jan/w01/q10@portal | Nested multiplication table: `i` = 2, `j` from 1 adding 1 each pass, `x = i*j` shows 2, 4, ..., 20 (table of 2). | Add to "Order of blocks inside a loop": "`x = i*j` with j counting 1..10 gives a table: 2, 4, ..., 20."
- p3b | 2025-jan/w01/q03 | `myNum` = 7, says myNum then subtracts 1 for 7 passes: says 7, 6, ..., 1 (countdown). | Add to "Saying a sequence": "step -1 from 7 says 7, 6, ..., 1."
- p3b | 2026-jan/w01/q02 | `score` 20 plus `repeat 5` of +4 is 40 after the first loop. | Add to "Counting with two loops": "20 + 5x4 = 40 after loop 1."
- p3b | 2026-jan/w01/q03 | Second loop subtracts 6 three times (-18) from 40, so sprite says 22. | Same bullet: "then 40 - 3x6 = 22."
- p3b | 2026-jan/w01/q04 | `change counter by 1` is inside both loops, executing 5 + 3 = 8 times (stated in lesson only via counter value). | Fine if the "How to trace a loop" line stays; optional to add "executions = 5 + 3".
- p3b | 2023-jan/w01/q06 | 100 with `change num by -2` x10 = 80, which is "none of the above" in that option set. | Optional; q06@portal brief already gives 80.
- p3b | 2021-jul/w01/q06 | `wait (n) secs` pauses the script (heading "Adding in a loop makes a product" has no text of its own). | Covered under Control table; none needed.

## audit_p3c_p10_p11.txt

- p3c.md | lesson: Wisdom of crowds / trimmed mean | The trimmed-mean worked example (sorted [2,4,4,5,5,5,6,6,7,90] -> trim 10% each end -> [4,4,5,5,5,6,6,7], mean 5.25) and its purpose (a few wild values drag an ordinary mean; trimming both ends reduces outlier influence) were dropped; only "sort, drop top/bottom 10%" remains | add bullet: "Trimmed mean resists outliers: [2,4,4,5,5,5,6,6,7,90] drops 2 and 90, mean 5.25."
- p3c.md | 2024-jan/w04/q06 | Matrices can be stored as nested lists or with NumPy (NumPy is the standard matrix library); lists are not the only way. Dashed, so nothing renders | add to "Building an odd square": "A matrix is nested lists, or NumPy arrays."
- p3c.md | 2026-jul/w04/q14 | The magic-square prototype only creates the matrix and places 1; it has no movement rules to place 2, 3, ..., so it is not yet a magic square. Dashed | add a bullet after step 3: "A prototype that only places 1 lacks the movement rules for 2, 3, ..."
- p3c.md | 2020-sep/w03/q02 | Accumulator pattern: `sum=0; for w in weights: sum=sum+w` is correct; `range(len(...))` would add indices, `sum=w` keeps only the last. Dashed | add to "Digit sums" or a new bullet: "Total with `total = total + w` per item; not `total = w` (keeps last) or looping over indexes."
- p3c.md | 2022-jan/w04/q07 | Lesson rule says spaces and digits stay visible, but the card's code prints `*` for letters AND digits and leaves other characters unchanged; the lesson contradicts it (the last Rules bullet also says digit) | reword first Rules bullet: "spaces and symbols stay visible" and keep the digit remark only for the one-line `*` code.
- p3c.md | 2026-jul/w05/q07 | Score trace: A wins rounds 1-3 (Rock>Scissors, Paper>Rock, Scissors>Paper), round 4 Rock/Rock is a draw, round 5 Paper vs Scissors goes to B; final {"Player A": 3, "Player B": 1}. Dashed, only "round 4 is a draw" partially kept | add bullet: "After five rounds incl. one draw the score is A 3, B 1."
- p3c.md | 2026-jul/w05/q09 | Because score A (3) > score B (1), the program prints "Player A Wins" | fold into the q07 bullet above.
- p3c.md | 2026-jul/w05/q13 | Binary search gate list of 8 items: first mid = (0+7)//2 = 3 (lesson only has 8 items -> 3, 10 -> 4; ok) | kept; no action.
- p3c.md | 2026-jul/w05/q16-q18 | Gate example (10 gates): linear search finds 126 after 7 comparisons; first binary-search comparison is index 4 = 117; since 126 > 117 the left half is dropped and [121, 126, 130, 135, 140] is searched next. All dashed | add bullet in Binary search: "10 sorted gates: first mid = index 4 (117); 126 > 117 keeps the right half [121..140]; linear search needs 7 checks for 126."
- p3c.md | 2025-jul/w05/q13 | binary_search([1,3,5,7,9], 7) trace: mid 2 (5 < 7) -> low 3; mid 4 (9 > 7) -> high 3; mid 3 -> returns 3. Dashed | add a one-line worked trace or brief to the Binary search section.
- p3c.md | 2024-jul/w05/q09, 2024-jul/w05/q10, 2025-jan/w05/q10, 2019-jul/w05/q03 | Pass-by-pass bubble traces lost: [5,3,8,4,2] -> [3,5,4,2,8] -> [3,4,2,5,8]; [4,3,2,1] passes make 3,2,1 swaps; [5,4,3,2,1] passes make 4,3,2 swaps (swaps per pass fall by 1); [2,9,5,4,8,1] pass 1 -> [2,5,4,8,1,9]. Only final pass-3 results kept | add: "Swaps per pass on a reversed list of n items: n-1, n-2, ... ; first pass of [2,9,5,4,8,1] gives [2,5,4,8,1,9]."
- p3c.md | 2024-jan/w05/q08 | Official-key dispute (key says Step 4, correct is Step 3, the comparison step, not among options) lives only in a dashed card's `note:`; renders only if notes render | confirm notes render, else add lesson bullet: "Binary-search step-order question: official key says Step 4, correct is Step 3 (comparison)."
- p3c.md | 2020-jan/w03/q01 | Official-key dispute note (A prints fizzbuzz whenever b does not divide; C and D mis-attach else) lives only in a dashed card's `note:` | same: confirm notes render, otherwise add a bullet.
- p3c.md | 2020-jan/w05/q10 | Detail lost: with a list instead of a view, x would be the ball counts and y the number of bins with that count (it is a `why:` on a no-code card) | optional: append "(a list would give x = ball counts, y = bins per count)" to the fact.
- p10.md | lesson: Why these questions catch people | Whole intro section removed; its points (each case hinges on one specific rule, predict first) are in the one-line intro | none needed
- p10.md | 2022 loop-removal card (remove inside for loop) | Detail lost that items 4 and 8 are the ones never checked | optional: restore "(4 and 8 are never checked)" in the why.

## audit_p3d_p5.txt

- p3d.md | lesson: Week 9 Area by random points (2024-jan/w09/q10) | Monte Carlo is not efficient in every scenario (the "always efficient" option is false). | Add "not efficient in every scenario" to the 'More points, more stable' bullet.
- p3d.md | 2026-jul/w07/q07 | Position 16 is a snake head (elif position == 16: position = 7), slide to 7; not in lesson. | Set fact: Position 16 is a snake head and moves the player to 7.
- p3d.md | 2026-jul/w07/q10 | Move skipped if it would pass 25 and ladder/snake squares change position at once; lesson only states the rule generically. | Optional: add "target 25 in the code; snake/ladder applied at once" to the Variants skip bullet.
- p3d.md | 2026-jan/w09/q04 | Longer average words move the word-length curve peak right and spread it wider. | Add to Federalist bullets: longer words, peak further right and wider.
- p3d.md | lesson: Other chance simulations (week 8 lottery) | Dropped: plot that goes up on a mismatch and down on a match; guessing a number daily for a year. | Add one line to the lottery bullets.
- p3d.md | 2021-jan/w06/q03@portal, 2023-jul/w08/q05... (minimax) | Minimax = maximise own winning chances while minimising the opponent's; lesson gives only worst-case wording. | Add "maximise yours, minimise the opponent's" to the Minimax bullet.
- p3d.md | lesson: Week 7 Snakes rules / 2019-jul/w07/q07 | Win is reaching the last cell only; climbing a ladder or rolling a six does not end the game; program also ends if the player quits. | Add to the Win-at-100 bullet.
- p3d.md | 2022-jul/w07/q06 | The spiral problem is broken down into a 2-D table (matrix). | Add "matrix = 2-D table" to the spiral bullet.
- p3d.md | lesson: Graph basics | Dropped: 4-cycle degree total is 8; complete graph on 5 nodes has 10 edges; two friends of one person are connected via that person. | Add these as short clauses.
- p3d.md | lesson: Contrast and CLAHE | CLAHE handles noise better than plain AHE; enhancement reveals hidden detail. | Add "better with noise than AHE".
- p3d.md | lesson: Substitution cipher | Worked dict/reverse-dict code and its output (eqw cab) dropped; GOLD to FNKC and SOUJANYA to RNTIZMXZ examples only in unrendered why. | Optional: keep code example.
- p5.md | 2026-jul/w08/q17 | Review labelled Positive when compound score is above 0 (compound is the score used). | Table row: add "Positive if > 0".
- p5.md | 2026-jul/w05/q04 | max_books holds the largest count, highest holds its category, category/count are loop variables for the current pair only. | Set fact with that sentence.
- p5.md | lesson: Worked case Library Book Tracker | Line-role table (lines 1-11 init, 12-16 update loop, 13 condition, 17-18 running best, 19-22 max loop) dropped; "which line does X" questions need it. | Add one-line role summary under the program.
- p5.md | lesson: Worked case Pixel Inspector | Line-role table (2-4 input, 5-6 counters, 7-8 loop headers, 9-10 average, 11-14 condition/updates) dropped. | Add one-line role summary under the program.
- p5.md | lesson: Missing update/loop (Scratch) 2026-jul/w01/q19 | Scratch scoring program (score 12, 6 rounds +5, bonus 3 even/1 odd, final change by bonus, thresholds 50 Excellent, 40 Level Cleared) is not shown; only the moved-inside fact. | Optional: add program/thresholds as a text block.
- p5.md | 2026-jul/w08/q14 | Loop breaks only when candidate != keyword, so it keeps shuffling until different. | Fold into the one-letter-word bullet.
- p5.md | 2026-jul/w04/q06, q10 | Dobble program builds two five-symbol cards sharing one symbol, then asks the player to enter it and checks. | Optional fold into Dobble fact.
- p5.md | lesson: Case families | Specific story list shortened (Scratch battery counter, kiosks registration/cafeteria, grocery list ops, tuples vs sets, movie guessing, gmplot, TextBlob, PageRank detail, shift/training planners). | Optional restore compact list.

## audit_p3e.txt

- p3e.md | 2024-jan/w12/q01 + 2024-jan/w12/q06 | Google ranks with PageRank plus content relevance and user experience; PageRank is not the only search factor (only in a hidden why). | Add lesson bullet in "What PageRank is": "Google also uses content relevance and user experience; PageRank is one factor."
- p3e.md | 2022-jul/w12/q07 | `random.choice` picks one item, `random.choices` returns a list (only in hidden why; the note covers the key/KeyError only). | Add to the "Pick a random node" sentence: "`choice` returns one item, `choices` a list."
- p3e.md | 2024-jul/w10/q01 | `s[7:12]` of `Hello, World!` takes positions 7 to 11 and gives `World` (card has no fact, so nothing is shown; options B/C/D wrong via s[7:13], s[7:11], s[8:12]). | Add `fact: `s[7:12]` of `Hello, World!` is `World` (positions 7 to 11).`
- p3e.md | 2026-jan/w12/q12 | A node's own outgoing edges give points away and do not raise its rank; only important in-links do. | Add to "main idea" bullet: "Outgoing links do not raise a page's own rank."
- p3e.md | 2026-jan/w12/q07 | A node with no incoming edges only gives points away (not trapped); only sinks trap points. | Add to "Sinks trap points": "A node with no in-links just gives its points away."
- p3e.md | 2026-jul/w12/q02 | A link from a top-ranked page helps a new page but does not make it first at once, and the linker keeps its rank. | Extend fact: "...it does not make the page first, and the linking page keeps its rank."
- p3e.md | 2026-jul/w12/q20 option B | For an odd n the next value 3n + 1 is always larger, not smaller. | Add to Collatz rules: "An odd step always makes the number bigger."
- p3e.md | 2026-jan/w12/q11 | PageRank is reliable because iterations converge mathematically (hidden why). | Add "reliable" to the convergence paragraph.
- p3e.md | 2025-jan/w12/q09 | Hyperlink analysis only names the data; the technique is random walk. | Optional: add to Random walk lesson.
- p3e.md | 2022-jan/w10/q04 | Wrong vowel-replace options: `replace('_','a')` is reversed; unassigned `replace` discards its result (reversed case lost; unassigned kept). | Add "args order: old then new" to Replacing vowels.
- p3e.md | 2018-jul/w10/q01, q03, 2019-jul/w10/q01, 2019-jan/w10/q04, q05, 2024-jul/w10/q05 | Which letters cancel for each name pair (A K S H; A I; A E E; A A N K) no longer shown, only counts in table. | Optional: add a "Cancelled" column to the table.
- p3e.md | 2020-sep/w12/q08 | 75 reaches 1 via 75, 226, 113, 340, 170, 85, 256, 128, 64, 32, 16, 8, 4, 2, 1 (sequence lost, count 14 kept). | Optional.
- p3e.md | 2025-jan/w12/q04 | `cycle_graph(4)` is undirected. | Optional: add "undirected" in the graph types table header.
- p3e.md | lesson: The problem (What PageRank is) | Why keyword or plain link counting fails to rank millions of matching pages. | Optional one sentence.
- p3e.md | 2024-jan/w10/q10 | Mode `'r'` write fails, no-newline puts all on one line, 26 passes repeat pairs in reverse; shown only if notes render with a brief. | Check note renders with brief.

## audit_p6_p7_p9.txt

- p6.md | 2026-jul/w07/q20 | Binary search needs a sorted list (option A false) is only in why of a no-code card, so not rendered in the weeks 7-8 section (only 2026-jul/w06/q20 says it elsewhere). | Add "binary search needs sorted data" to the fact.
- p6.md | 2025-jan/w01/q10 | y ends at -18 after the 18 passes (trace result) is gone. | Add "(y ends at -18)" to the brief.
- p6.md | 2026-jul/w08/q20 | The original Review column is left unchanged; labels go only into the new Sentiment column. | Add "Review stays unchanged" to the lesson line.
- p6.md | 2026-jul/w09/q10 | An edge needs two nodes; not every node must link to every other (only the second half survives in lesson). | Add "an edge joins two nodes" to the fact.
- p6.md | 2024-jan/w05/q01 | Four doors: staying wins 1/4 (baseline lesson) is not rendered. | Add "staying wins 1/4" to the fact.
- p7a.md | 2019-jul/w05/q02 | Bubble sort swaps equal the number of out-of-order pairs; [8,22,7,9,31,5,13] needs 10 swaps. | Add to Bubble sort bullets: "swaps = inversions; [8,22,7,9,31,5,13] gives 10".
- p7a.md | 2020-jan/w07/q08 | Snakes and ladders ambiguity: ladder start equal to snake start (same square) is the real conflict; snake_begin=snake_end is already excluded by the loops. | Add one bullet to the Snakes and ladders lesson.
- p7a.md | 2021-jan/w07/q03@portal | Game ends when a player reaches the end square or quits (both). | Add to the lesson: "ends at square 30 or when a player quits".
- p7a.md | 2025-jan/w07/q10 | Snakes/ladders can be tracked with a dictionary keyed by square or with an if test on each position; both valid. | Add "or a dict keyed by square" to the lesson.
- p7a.md | 2024-jul/w07/q04 | From 96 with a snake at 99, roll 4 lands exactly on 100 (3 would hit the snake). | Optional one-line fact; low value.
- p7a.md | 2026-jul/w04/q15 | The magic square prototype never verifies row/column/diagonal sums; it only builds the matrix and places the first number. | Add to the Magic square lesson: "the program builds, it does not check sums".
- p7a.md | 2024-jan/w04/q02 | Checker function (square, rows, columns, anti-diagonal equal first-row sum) returns True for all four sample grids (sum 15). | Optional bullet describing the checker.
- p7a.md | 2026-jul/w07/q02 | In the spiral, `k += 1` after the top row moves the start row down. | Add to the lesson or p6 spiral note.
- p7a.md | 2021-jul/w08/q05 | CLAHE combines neighbouring tiles by bilinear interpolation to remove tile boundaries (the false statement said it includes them). | Add a CLAHE bullet: "tiles on small regions, joined by bilinear interpolation".
- p7a.md | 2024-jan/w08/q09 | CLAHE limits contrast amplification, so it handles noise better than plain AHE. | Add to the CLAHE lesson.
- p7a.md | 2026-jan/w11/q04 | Removing `time.sleep` between 50 messages can cause UI failures or platform restrictions. | Add to the Browser automation lesson.
- p7a.md | 2021-jul/w11/q07 | `calendar.weekday(2021,10,9)` is 5 (Saturday). | Add the worked value to the Timezones/calendar bullet.
- p7a.md | 2026-jan/w03/q13 | `tuple(list)` converts a list to a tuple. | Add to the Tuples lesson.
- p7a.md | 2025-jan/w08/q08 | `sorted('hey!there')` gives a list with `!` first, then `reverse()` flips it in place. | Optional bullet in the sorted lesson.
- p7a.md | lesson: Magic square (the code) | The full lecture program code and its `'%2d '` loop are removed; only the rules and the n=3 output remain. | Optional; rules and output carry it.
- p7a.md | lesson: FLAMES | `remove_matching_letter` returns list1 + ["*"] + list2 and the caller splits at "*" again. | Add the "*" separator note.
- p7a.md | lesson: Browser automation / Compression | `find_element_by_class_name` finds the message box; `ig.new(img.mode, img.size)` makes the blank output image. | Optional one-clause additions.
- p7b.md | 2024-jan/w10/q01 | Josephus recursion J(n) = (J(n-1)+k-1) % n + 1, J(1)=1; 25 soldiers every 3rd gives 14. The card has no fact so its why is not rendered. | Add a fact: "J(n)=(J(n-1)+k-1)%n+1, J(1)=1; 25 soldiers, every 3rd: 14".
- p7b.md | lesson: Tuple and dict functions | `count_letters("banana")` giving {'b':1,'a':3,'n':2} (counting letters with a dict) is removed. | Add `count_letters` to the sentence.
- p7b.md | lesson: Snakes and ladders | Position trace 4->14, 20, 26, 31, 34, 38, 44 (jump only on an exact start square, repeated) is gone; only 44 No remains. | Add the trace as one bullet.
- p7b.md | lesson: Number patterns | Square-number pattern `[count*count ...]` giving 1,4,9,16 is removed. | Add to the pyramid bullet.
- p7b.md | lesson: Fill a matrix | A table `R*row + col` printed with nested generators inside `'\n'.join` is removed. | Optional bullet.
- p7b.md | lesson: Week 11 | Worked outputs removed (review count `good` -> 2; stay duration 4 days; March 2026 has 5 Sundays). | Add the three results as examples.
- p9.md | (none) | Only the intro/how-to-use lines were cut; every drill card is intact. | no change

