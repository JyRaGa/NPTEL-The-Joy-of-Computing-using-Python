# Joy of Computing using Python: Guidebook

This guide covers every concept that the 1,891 quiz cards on the site test (all sessions from 2018-jul to 2026-jul, weeks 0–12). It was written by reading every card. Nothing has been dropped or ranked by how often it appears. Each fact here is something at least one card asks about.

How to use it:
- **Part 1–3** hold the facts you must *know*: the language, the libraries and the course topics. Questions that do not come with code ("independent" questions) are answered from these.
- **Part 4** lists the traps and edge cases: questions whose code looks fine but errors, or prints something unexpected.
- **Part 5** is the method for case/scenario questions, which give you the code or story in the exam.
- **Part 6** lists cards whose stored answer key is doubtful, so you do not learn a wrong fact from them.
- **Part 7** covers the lecture code, the programming assignments, the 2021 online programming tests, a recalled final exam paper and the exam pattern.
- **Part 8** is the exam-day sheet: every number, formula and index convention on one screen.
- **Part 9** is a self-test drill of 46 predict-the-output and variant questions. Each answer comes from running the code and is hidden until you open it.
- **Part 10** is 36 examiner's oddities: corner cases where the intuitive answer is wrong (floats, rounding, precedence, aliasing, scope). Answers come from running the code.
- **Part 11** is 30 plain ChatGPT-style concept MCQs, like the `@gpt` cards, with hidden answers.

Sources used:
- All the cards in `site/data/week-*.json`: question, code, options (including code inside options), case-study programs (`context.code`), key and explanation.
- `site/data/questions.json`: typed code from duplicate copies of image-only cards.
- `lecture-code/`, `programming-assignments/` and `exams/` (Part 7).
- The 2026-jul assignment solution PDFs in `JyRaGa/NPTELWhisperer` (Part 7.5).
- `index/explain/skipped.tsv` (answer-key disagreements).
- For the 738 cards whose code or figure exists only as a page image: their explanations, which were written by reading those crops. The 46 such cards with no explanation were read directly from their crops in `quizzes/<term>/img/`.

Week → topics → where to read (every week also uses Parts 4–9):

- **Week 0**: Aptitude maths (no Python). Read: [3.0 Week 0 aptitude maths](#30-week-0-aptitude-maths).
- **Week 1**: What programming is; Scratch. Read: [1.1 Programs, languages, tools](#11-programs-languages-tools), [3.1 Week 1: Scratch](#31-week-1-scratch).
- **Week 2**: Python basics: print, input, variables, operators, if/while/for, errors. Read: [1.2 print, input and type conversion](#12-print-input-and-type-conversion), [1.3 Names and keywords](#13-names-and-keywords), [1.4 Operators](#14-operators), [1.5 Control flow](#15-control-flow), [1.6 Errors you must recognise](#16-errors-you-must-recognise).
- **Week 3**: Lists, random, files, matplotlib, FizzBuzz, jumbled words, crowd computing / trimmed mean, genetic evolution. Read: [1.8 Lists](#18-lists), [1.14 Files](#114-files), [2.1 random](#21-random), [2.2 Statistics](#22-statistics), [2.3 matplotlib.pyplot (as plt)](#23-matplotlibpyplot-as-plt), [3.2 Week 3 projects](#32-week-3-projects).
- **Week 4**: Magic square, birthday paradox / pigeonhole, Dobble, Guess the Movie, leap years, datetime basics, list copies. Read: [3.3 Week 4 projects](#33-week-4-projects), [1.8 Lists](#18-lists), [2.4 datetime, time, calendar, pytz](#24-datetime-time-calendar-pytz).
- **Week 5**: Dictionaries, Monty Hall, Rock-Paper-Scissors (secure version), speech recognition, linear/binary search, bubble sort, functions. Read: [1.11 Dictionaries](#111-dictionaries), [1.12 Functions](#112-functions), [1.15 Complexity facts](#115-complexity-facts), [2.13 Speech recognition](#213-speech-recognition), [3.4 Week 5 projects](#34-week-5-projects).
- **Week 6**: Recursion, ciphers (Caesar/substitution), Tic-Tac-Toe / min-max, strings, recursive binary search. Read: [1.13 Recursion](#113-recursion), [1.7 Strings](#17-strings), [3.5 Week 6 projects](#35-week-6-projects).
- **Week 7**: Turtle, PIL basics, gmplot/GPS, csv, snakes and ladders, spiral traversal, sets vs tuples, functions. Read: [2.8 turtle](#28-turtle), [2.7 PIL / Pillow (from PIL import Image)](#27-pil--pillow-from-pil-import-image), [2.9 gmplot, csv](#29-gmplot-csv), [1.10 Sets](#110-sets), [3.6 Week 7 projects](#36-week-7-projects).
- **Week 8**: Tuples, gambling / lottery simulation, anagrams, ASCII, sentiment (NLTK/VADER), image enhancement (CLAHE, flip), isomorphic strings. Read: [1.9 Tuples](#19-tuples), [2.10 NLTK, VADER, TextBlob, pandas](#210-nltk-vader-textblob-pandas), [3.7 Week 8 projects](#37-week-8-projects).
- **Week 9**: Stylometry, NLTK tokenising, NetworkX basics, six degrees of separation, area estimation (Monte Carlo), image pixels. Read: [2.10 NLTK, VADER, TextBlob, pandas](#210-nltk-vader-textblob-pandas), [2.11 NetworkX (import networkx as nx)](#211-networkx-import-networkx-as-nx), [3.8 Week 9 projects](#38-week-9-projects).
- **Week 10**: Strings in depth, FLAMES / Josephus, NumPy, image compression, pixel processing / quantisation. Read: [1.7 Strings](#17-strings), [2.6 NumPy (import numpy as np)](#26-numpy-import-numpy-as-np), [2.7 PIL / Pillow (from PIL import Image)](#27-pil--pillow-from-pil-import-image), [3.9 Week 10 projects](#39-week-10-projects).
- **Week 11**: Selenium (browser / WhatsApp automation), datetime, calendar, pytz, time. Read: [2.4 datetime, time, calendar, pytz](#24-datetime-time-calendar-pytz), [2.12 Selenium (browser automation)](#212-selenium-browser-automation), [3.10 Week 11 topics](#310-week-11-topics).
- **Week 12**: PageRank (random walk, point distribution), directed graphs, graph types, Collatz conjecture. Read: [2.11 NetworkX (import networkx as nx)](#211-networkx-import-networkx-as-nx), [3.11 Week 12 topics](#311-week-12-topics).

## Contents

- [Part 1 — The Python language](#part-1--the-python-language)
  - [1.1 Programs, languages, tools](#11-programs-languages-tools)
  - [1.2 print, input and type conversion](#12-print-input-and-type-conversion)
  - [1.3 Names and keywords](#13-names-and-keywords)
  - [1.4 Operators](#14-operators)
  - [1.5 Control flow](#15-control-flow)
  - [1.6 Errors you must recognise](#16-errors-you-must-recognise)
  - [1.7 Strings](#17-strings)
  - [1.8 Lists](#18-lists)
  - [1.9 Tuples](#19-tuples)
  - [1.10 Sets](#110-sets)
  - [1.11 Dictionaries](#111-dictionaries)
  - [1.12 Functions](#112-functions)
  - [1.13 Recursion](#113-recursion)
  - [1.14 Files](#114-files)
  - [1.15 Complexity facts](#115-complexity-facts)
- [Part 2 — Libraries: what each part does](#part-2--libraries-what-each-part-does)
  - [2.1 random](#21-random)
  - [2.2 Statistics](#22-statistics)
  - [2.3 matplotlib.pyplot (as plt)](#23-matplotlibpyplot-as-plt)
  - [2.4 datetime, time, calendar, pytz](#24-datetime-time-calendar-pytz)
  - [2.5 copy and operator](#25-copy-and-operator)
  - [2.6 NumPy (import numpy as np)](#26-numpy-import-numpy-as-np)
  - [2.7 PIL / Pillow (from PIL import Image)](#27-pil--pillow-from-pil-import-image)
  - [2.8 turtle](#28-turtle)
  - [2.9 gmplot, csv](#29-gmplot-csv)
  - [2.10 NLTK, VADER, TextBlob, pandas](#210-nltk-vader-textblob-pandas)
  - [2.11 NetworkX (import networkx as nx)](#211-networkx-import-networkx-as-nx)
  - [2.12 Selenium (browser automation)](#212-selenium-browser-automation)
  - [2.13 Speech recognition](#213-speech-recognition)
- [Part 3 — Course topics and algorithms](#part-3--course-topics-and-algorithms)
  - [3.0 Week 0 aptitude maths](#30-week-0-aptitude-maths)
  - [3.1 Week 1: Scratch](#31-week-1-scratch)
  - [3.2 Week 3 projects](#32-week-3-projects)
  - [3.3 Week 4 projects](#33-week-4-projects)
  - [3.4 Week 5 projects](#34-week-5-projects)
  - [3.5 Week 6 projects](#35-week-6-projects)
  - [3.6 Week 7 projects](#36-week-7-projects)
  - [3.7 Week 8 projects](#37-week-8-projects)
  - [3.8 Week 9 projects](#38-week-9-projects)
  - [3.9 Week 10 projects](#39-week-10-projects)
  - [3.10 Week 11 topics](#310-week-11-topics)
  - [3.11 Week 12 topics](#311-week-12-topics)
- [Part 4 — Edge cases and traps (all found on the cards)](#part-4--edge-cases-and-traps-all-found-on-the-cards)
- [Part 5 — How to answer case/scenario questions](#part-5--how-to-answer-casescenario-questions)
- [Part 6 — Doubtful answer keys (don't learn these as facts)](#part-6--doubtful-answer-keys-dont-learn-these-as-facts)
- [Part 7 — Lecture code, programming assignments and the final exam](#part-7--lecture-code-programming-assignments-and-the-final-exam)
  - [7.1 Exam pattern](#71-exam-pattern)
  - [7.2 The recalled final exam (13 Dec, morning session, 34 questions)](#72-the-recalled-final-exam-13-dec-morning-session-34-questions)
  - [7.3 How the lectures wrote the course programs](#73-how-the-lectures-wrote-the-course-programs)
  - [7.4 Programming-assignment patterns (code you may be asked to trace)](#74-programming-assignment-patterns-code-you-may-be-asked-to-trace)
  - [7.5 Current session (2026-jul) programming assignments](#75-current-session-2026-jul-programming-assignments)
- [Part 8 — Exam-day sheet: numbers, formulas and conventions](#part-8--exam-day-sheet-numbers-formulas-and-conventions)
  - [Boundaries: included or excluded?](#boundaries-included-or-excluded)
  - [Index conventions](#index-conventions)
  - [Formulas](#formulas)
  - [Character codes and modules](#character-codes-and-modules)
  - [Full forms](#full-forms)
- [Part 9 — Self-test drill](#part-9--self-test-drill)
- [Part 10 — Examiner's oddities](#part-10--examiners-oddities)
- [Part 11 — ChatGPT-style questions](#part-11--chatgpt-style-questions)

---

## Part 1 — The Python language

### 1.1 Programs, languages, tools

- A **program** is a sequence of instructions that does a specific task, usually stored as an executable file. It cannot be written in plain English, which is ambiguous; it needs a programming language with strict rules.
- Programming languages exist so humans can give instructions to computers. Many languages were designed for different kinds of problems. BASIC, FORTRAN and LOGO are programming languages.
- **Programming logic** (the step-by-step thinking) is the same in every language. Python, C and C++ are languages, not logic.
- Python is a **high-level** language. HTML is a **front-end** language (it builds what the browser shows).
- Open source examples asked on the cards: Java, Python and FORTRAN (the key leaves out C#, although C#/.NET has been open source since 2014).
- Coding is useful in physics, mathematics, economics, small-scale business, healthcare and other fields, not only software engineering. The way to get good at it is regular practice in small steps.
- Programming is a problem-solving skill. Existing apps don't make it unnecessary: it lets you create, improve and customise solutions.
- The lecture's hand-gesture activity shows that programming = clear instructions using symbols everyone has agreed on.
- Polynomials and arithmetic expressions can be evaluated in a finite number of steps, with built-in operators (`+ - * /`) or libraries.
- A **string** stores a sequence of characters. Variables and arrays (lists) store data; loops and conditionals control flow, they do not store anything.
- Python was named after the TV show **Monty Python's Flying Circus**.
- Python files end in **`.py`** (not `.python`).
- **IDEs**: PyCharm, Spyder, VS Code. C# is a language, not an IDE.
- **Anaconda** is a Python *distribution* (Python plus scientific and data-science libraries).
- `pip install packagename` installs packages, including ones that are not on the conda channels.
- In the IPython console, `_` holds the last result.
- Applications of Python: image processing and graphics, enterprise and business software, operating-system tooling.
- Python is **case-sensitive** (`name` ≠ `Name`) and **dynamically typed**: a variable needs no declaration and can change type at run time.
- A **variable** is a named storage location whose value can change while the program runs. It always holds the **latest** value assigned to it. Reasons to store data in variables: reuse it without asking again, and change it in one place.
- A **loop** repeats instructions (write once, run many times, easier to change and maintain). A `for` loop suits a known number of repeats. A `while` loop repeats while a condition holds, for example when a user decides when to stop.

### 1.2 `print`, `input` and type conversion

- `print(a, b, c)` separates its items with a space and ends with a newline.
- `print(x, end="")` stays on the same line. `print()` alone prints just a newline, which is how nested-loop patterns move to the next row.
- `print('Hello Mr.', a, b+1)` with `a = 'Bond'`, `b = 34` → `Hello Mr. Bond 35`.
- Text must be in quotes: `print(Stay Safe Friends)` is an error, `print("Hurry Up!!")` is fine.
- `"Hi" + user1` joins strings without a space, while a comma adds one.
- **`input()` always returns a string.** `input("prompt")`, `input('42')` and `input()` are all valid. `input(Hello)` without quotes is an error (it reads `Hello` as a variable name).
  - Input `5`: `c*3` → `'555'`. Input `20`: `n*2` → `'2020'`.
  - `int(input())` gives an integer and `float(input())` a decimal number (use `float` for rates like 7.5). `in(input())` does not exist.
  - Comparing raw input with a number (`input() == 10`) is never `True`.
- Conversions:
  - `int(4.5)` → 4 and `int(3.79) + int(2.1)` → 5: `int` cuts off the decimal part.
  - `int("123abc")` → `ValueError`.
  - `int(s)` turns a string of digits into an int, and `str(n)` turns a number into a string.
  - `list("joc python")` gives a list of single characters, spaces included.
  - `tuple(L)` and `list(t)` convert between lists and tuples.
- Types:
  - `type(10)` and `type(9)` → `int`.
  - `type(np.array(...))` → `numpy.ndarray`.
  - `type((t, t))` → `tuple`.
  - Binary types: `bytes`, `bytearray`, `memoryview`.
  - Python has **no** separate `character` type; a character is a string of length 1.

### 1.3 Names and keywords

- A name may contain letters, digits and `_`, and cannot start with a digit.
  - Valid: `_a`, `__1`.
  - Invalid: `32asd`, and `var-1` (read as `var` minus `1`).
- `yield`, `global` and `elif` are keywords; `add` is not.
- The conditional keywords are `if`, `elif` and `else`. `else_if` and `switch` do not exist in Python.
- `def` declares a function: `def function_name():`.
  - Parameters have no types: `def add(int a, int b)` is invalid.
  - Literals cannot be parameters: `def add(2, 3)` is invalid.
  - `function add(a, b)` is not Python.
  - Correct: `def add(a, b): print(a+b)` then `add(2,3)`.

### 1.4 Operators

- **`/`**: true division, always a float. Examples: `30/4` → 7.5
- **`//`**: floor (integer) division. Examples: `30//4` → 7, `5//2` → 2
- **`%`**: remainder (modulo); the result takes the **sign of the divisor**. Examples: `100%90` → 10, `10%5` → 0, `17 % -5` → **-3**; `n % 2 == 0` tests even; `n % 5` is always 0–4
- **`**`**: power; binds tighter than `*`. Examples: `3*1**3` → 3
- **`^`**: bitwise XOR (not power). Examples: `a=a^b; b=a^b; a=a^b` swaps a and b
- **`==` vs `=`**: compare vs assign. Examples: `if (x = 0):` → SyntaxError
- **`+=`**: in-place add; no space inside. Examples: `i + = 1` → SyntaxError

More operator facts:

- `3 == 3.0` is `True`. `c = a > b` stores a bool (`False` for 3 > 4).
- `int + float` → float (`4.5 + 15` → 19.5).
- Strings support `+` (join) and `*` (repeat) only. There is no `++` and no `-` for strings.
- `a(b + c**2)` tries to **call** the integer `a` → `TypeError: 'int' object is not callable`. Write `a*(b + c**2)`.
- Swapping without a temp variable: `a, b = b, a`, or the XOR / add-subtract tricks.
- `pow(x, y)` = `x ** y`. `for i in range(1,6): print(pow(2,i))` prints 2, 4, 8, 16, 32, the same as doubling `n` from 2 four times.
- **Floor division of negatives rounds down**: `-1 // 10` is `-1`, so `while n != 0: n = n // 10` never ends for a negative `n`.
- **Truthiness**: `if 2:` is true, because any non-zero number or non-empty string/list is truthy and `0`, `""`, `[]`, `None` are falsy. In the Monty Hall card, `2`, `True`, `(2**90) % 2 == 0` and `2*(2**89+7) % 2 == 0` all make the "switch" branch run, while `2**1024 % 2 != 0` and `(2**90) % 3 != 1` are False.
- `;` separates statements on one line: `n=5;print(n+5);print(n+5)` prints `10` on separate lines.
- f-strings: `print(f"Found at index {i}")` puts the value of `i` into the text. `{x:.2f}` shows 2 decimals (`f"{switch_wins / trials * 100:.2f}%"`).
- Conditional expression: `current_player = "X" if current_player == "O" else "O"` (switches players).
- `all(cond for x in seq)`: True if every item passes. The Tic-Tac-Toe checks are `all(cell == symbol for cell in row)`, `all(row[col] == symbol for row in board)`, `all(board[i][i] == symbol …)` and `all(board[i][2-i] == symbol …)`.
- `map(int, move)` converts every item: `row, col = map(int, input().split(','))` unpacks two numbers typed as `2,3`.
- `sum(f() for _ in range(n))` with a function that returns True/False counts the Trues (True = 1).
- Type hints `def simulate_monty_hall(switch: bool) -> bool:` only document the types; Python does not enforce them.
- `\` at the end of a line continues a long condition on the next line.
- `_` as a loop variable means "value not used" (`for _ in range(3)`).

### 1.5 Control flow

- `if` / `while` take a condition that evaluates to `True` or `False`. When it is false, Python skips the block and carries on after it; the program does not stop.
- **Order of `if`/`elif` matters.** The first true branch wins and the rest are skipped.
  - FizzBuzz must test "divisible by 3 **and** 5" first, or 15 prints `Fizz` (or `Walk` in the traffic-signal version) instead of `FizzBuzz` (`WalkWait`).
  - In the Jack/Jill loop over 11–15, the `i%2==0 and i%3==0` branch comes after `i%2==0`, so it is never reached. The output is `Jill and Jack, Jack, Jill and Jack, Jack, Jill`.
- `range(n)` → 0…n-1. `range(a, b)` stops before `b`. `range(a, b, step)` uses a step, which can be negative.
  - `range(11)` prints 0–10.
  - `range(1,11)` → 1–10.
  - `range(0,20,2)` → evens 0–18.
  - `range(3,30,3)` → 3…27.
  - `range(10,0,-1)` → 10…1.
  - `range(-1, -len(t), -1)` → -1, -2, …, -(len-1).
  - `range` takes **integers only**.
  - `for i in range(a)`: `i` takes 0 to a-1.
- `for item in L` gives the items. `for i in range(len(L))` gives the **indexes** (printing `i` prints 0, 1, 2, 3, not the items).
- `break` leaves the **innermost** loop at once (also from `while True`); the outer loop carries on.
- `continue` skips the rest of the current pass and goes to the next one.
- **`for … else` / `while … else`**: the `else` block runs only if the loop finished **without `break`**.
  - Prime printing: `for i in range(2, num): if num % i == 0: break` / `else: print(num)`.
  - Tic-Tac-Toe: the `else` of the game loop prints "It's a draw!".
- Infinite loops:
  - `while i in x:` where `i` never changes.
  - `while n >= 0:` with `n //= 10` (n sticks at 0).
  - A `while True` that never reaches `break`.
  - A shuffle loop that waits for a different arrangement of a one-letter word.
- Loop-count reasoning:
  - Nested `for i in range(10): for j in range(5): count += i*j` → 450.
  - Pattern `1 / 22 / 333 …`: the inner loop runs `i` times with `print(i, end="")`, then `print()`.
  - A while loop that removes one digit per pass runs once per digit (`1001` → 4 passes).

### 1.6 Errors you must recognise

| Error | Typical cause on the cards |
|---|---|
| `SyntaxError` | missing `:` after `if`/`while`/`for`; `=` instead of `==` in a condition; `i + = 1`; unbalanced quotes `print( " "Hello" " )`; words without quotes in `print`; `var-1 = 5` |
| `IndentationError` | body not indented under `if`/`for`/`with`; uneven indentation inside a block |
| `NameError` | using a variable never assigned (`c = b ** 3`, `x = y`); `Numpy.array` (wrong case) |
| `TypeError` | `"a" + 1`; item assignment on a string or tuple; deleting a tuple item; calling a non-function (`int`, `str`, tuple from `.shape()`, shadowed function name); `tuple + str`; comparing a number with an RGB tuple |
| `ValueError` | `int("123babumoshai")`; `str.index` / `list.remove` of something not present |
| `IndexError` | list index past the end (`l[10]` in a 10-item list; `randint(0, 5)` used as an index into a 5-item list); `L[-1]` on an empty list |
| `KeyError` | `d[k]` or `d[k] += 1` for a key not yet in the dict |
| `AttributeError` | `tuple.append`; `"s".uppercase()`; `date.hour`; `dict.values().count` |
| `RecursionError` | a recursive function with no base case |
| `RuntimeError` | adding keys to a dict while looping over it |
| `ImportError` | `from PIL import image` (must be `Image`) |
| `AxisError` | `numpy.sum(p, axis=2)` on a 2-D array |
| `UnknownValueError` | the speech recogniser could not understand the audio |

A program with a syntax error prints **nothing**, because Python rejects it before running any line.

### 1.7 Strings

- Strings are created with single, double or triple quotes. Triple quotes can span lines. A bare `'''This is a sentence'''` on its own line produces **no output**.
- **Strings are immutable**: `s[0] = 'H'` and `word[2] = 'n'` → `TypeError`. Methods return a **new** string. `s.replace('a','z')` without assigning it back leaves `s` unchanged.
- Indexing and slicing (the end index is **excluded**; the defaults are 0 and len):
  - `'python'[1:4]` → `'yth'`.
  - `'The Joy of Computing'[3:12]` → `' Joy of C'` (leading space).
  - `'Cinderella'[2:5]` → `'nde'`.
  - `'AbraKaDabra'[1:6]` → `'braKa'`.
  - `'Hello, World!'[7:12]` → `'World'`.
  - `s[:]` → the whole string.
  - `s[::-1]` → reversed (`'hello'` → `'olleh'`, `'Python'` → `'nohtyP'`).
  - `'PythonProgramming'[::2]` → `'PtoPormig'`.
  - `'abcdef'[1:5:2]` → `'bd'`.
  - `s[2:15:3] + s[::-4]` on `'PythonProgramming'` → `'tnoaigmooP'`.
- Methods:

| Method | Does |
|---|---|
| `upper()` / `lower()` | all upper / all lower case (`'SImRan'` → `'SIMRAN'` / `'simran'`) |
| `casefold()` | aggressive lower case (`'hello PYTHON'` → `'hello python'`) |
| `capitalize()` | first letter upper, rest lower |
| `replace(old, new[, count])` | replaces all, or only the first `count` (`replace('Madras','Chennai',2)` replaces the first two only) |
| `index(sub[, start, end])` | first position; **`ValueError`** if not found (`'Hello'.index('ell')` → 1; `index('o',5,10)` searches only positions 5–9: on `'Python Programming'` it returns 9, on `'PythonProgramming'` it returns 8) |
| `find(sub)` | first position, or **-1** if not found |
| `split(sep)` | list of pieces; the separator is removed (`"What will have so will".split('a')` → `'Wh'`, `'t will h'`, `'ve so will'`) |
| `strip()` | removes leading/trailing whitespace |
| `sep.join(iterable)` | puts `sep` *between* items: `'#'.join('JOC')` → `J#O#C`, `"+".join("Hello")` → `H+e+l+l+o`; empty strings in the list give doubled separators (`'.'.join(['','h','e','l','','l','o'])` → `.h.e.l..l.o`) |
| `isalpha()` | True if every character is a letter (`'ab'` → True; `'100%'` → False) |
| `isalnum()` | True if every character is a letter or digit (`'9a'` → True) |
| `count(x)` | number of occurrences |

- Strings have **no** `append`, `insert`, `sort` or `uppercase` methods. `sorted(s)` works and returns a **list**.
- Two string literals side by side are joined: `print('new' 'line')` → `newline`.
- `x in s` tests for a substring (`subStr(s1, s2)` = `s2 in s1`).
- Pattern matching by hand: compare `text2` against `text1` at each start position `i`. If all `len2` characters match, print it. This finds **all** occurrences.
- Character codes:
  - `ord('A')` = 65, `ord('a')` = 97, `ord('f')` = 102, and `chr()` is the inverse.
  - Upper and lower case differ by **32** (`chr(ord(ch) - 32)` turns lowercase into uppercase).
  - Sort order by code: space < `!` < digits < UPPERCASE < lowercase, so `sorted("HI! Amitabh")` starts with `' '`, `'!'`, then the capitals.
- The `string` module:
  - `ascii_letters` is 52 letters (a–z then A–Z).
  - `ascii_lowercase`, `ascii_uppercase`, `digits` (`'0123456789'`).
  - "Which module supports string operations?" → `string`.
- Shifting letters:
  - `letters[(index + value) % 26]` shifts with wrap-around.
  - `((ord(w) + 26 - 97) % 26) + 97` returns the same letter (a shift of 26).

### 1.8 Lists

- Lists are ordered, changeable and **allow duplicates**. No size is given at creation, they grow freely, and they are indexed by integers. `[]` is empty (even if named `This_is_not_List`).
- Methods:
  - **`append(x)`**: adds **one** item at the end. `[1,2,3,4].append([5,6,7,8])` → length **5**
  - **`extend(list)`**: adds each item of the list, so the result stays flat
  - **`insert(i, x)`**: puts `x` at index `i`. 3rd item → `insert(2, x)`; `insert(-3, 999)` goes before the third-from-last; `insert(len(L), x)` = append; `insert(0, x)` in a loop builds a reversed list
  - **`remove(x)`**: deletes the first `x`. `ValueError` if absent
  - **`pop(i)`**: removes and **returns** the item at `i` (last by default).
  - **`clear()`**: empties the list.
  - **`count(x)`**: occurrences.
  - **`index(x)`**: first position. `[4,6,7,4,6,2,1].index(7)` → 2
  - **`sort()`**: ascending, **in place**, returns `None`; capitals before small letters. `['Practice','makes','man','perfect.','the']`
  - **`reverse()`**: reverses in place.
- `sorted(x)` returns a new list; `x.sorted()` does not exist.
- `len`, `sum`, `min`, `max` and `in` work on lists.
- Slices: `L[3:6]`, `L[2:4]`, `L[4:]` (from index 4 to the end; on a 5-item list that is just the last item, as a list), `L[::-1]`. `P[:-1]` = `P[:len(P)-1]` = `P[0:-1]` = all but the last item.
- `P + Q` concatenates. `[]*100` is still `[]`.
- List comprehensions:
  - `[m for m in marks if m >= 50]`.
  - `[min(m+5, 100) for m in L]`.
  - `[x for x in nums if x % 3 == 0 and x % 5 != 0]`.
  - `[i*i for i in range(10) if i%2==0]` → squares of evens.
  - Nested: `[[0 for j in range(n)] for i in range(n)]` builds an n×n matrix.
- Matrices as nested lists:
  - `A[1]` is a row.
  - `[A[r][1] for r in (0,1,2)]` is a column.
  - `A[i][i]` is the main diagonal and `A[i][n-1-i]` (or `M[i][-1-i]`) the anti-diagonal.
  - `len(matrix)` is the number of rows and `len(matrix[0])` the number of columns (a 4×3 matrix has 4 rows).
  - Boundary element: `i==0` or `i==m-1` or `j==0` or `j==n-1`.
  - Snake pattern: rows with even parity print left→right, odd parity right→left.
  - The transpose of an m×n matrix is n×m. Symmetric matrices (identity, zero) equal their transpose.
- **Copies (very common):**
  - `b = a` → the **same** list; changing `b` changes `a`.
  - `b = a.copy()` or `b = a[:]` → a **shallow** copy. Replacing `b[i]` does not touch `a`, but changing an **inner** list `b[i][j]` does change `a`.
  - `copy.deepcopy(a)` → fully independent.
  - Combined example:
    ```python
    b = a
    c = a.copy()
    d = copy.deepcopy(a)
    b[0][0] = 10
    c[1][1] = 20
    d[0][1] = 30
    ```
    `a` becomes `[[10,2],[3,20]]`.
  - `ref = data["nums"]; ref.append(4)` changes the dict's list.
  - A slice `student["marks"][:2]` is a new list, so appending to it leaves the original unchanged.
- In functions:
  - `x += [1,2]` on a list parameter changes the caller's list.
  - `y += (3,4)` on a tuple makes a new local tuple, so the caller's tuple is unchanged.
  - `d = {"x":100}` inside a function rebinds the local name, so the caller is unchanged.
- Code idioms on the cards:
  - Insertion sort.
  - Reverse in place with two pointers.
  - Removing all copies of `x`:
    ```python
    while len(L) > 0:
        L.remove(x)
        count += 1
    ```
    If `count` ends at 10, `L` held exactly 10 items, all equal to `x`.
  - "Is the average an element?": `x * len(L) == S`. For the list 1…n this holds exactly when n is **odd**.

### 1.9 Tuples

- Created with round brackets or just commas: `(1,2,3)`, `t = 1, 2, 3`, `Dates = (12,23,3,4)`.
- Empty `()`. A single item needs a comma: `('Poonam',)`.
- **`('purple')` is just a string**, so `colors + ('purple')` → `TypeError: can only concatenate tuple (not "str") to tuple`.
- `((1),(2),(3),(4))` is the same as `(1,2,3,4)`.
- **Immutable**:
  - `t[3] = 45` → `TypeError`.
  - `del t[2]` → `TypeError`.
  - `del t` (the whole name) is fine.
  - `t.append(...)` → `AttributeError`.
  - To "change" one, build a new tuple: `t = t + (4,)` is valid.
- They support indexing (`name[-1]`), slicing (`t[1:]` → `(2,3,4)`), `+` (two 5-tuples → length 10), `*`, `count()`, `index()`, nesting, mixed types `(1,'cool',True)` and **mutable items**: `tup[0].append(5)` works → `([1,2,5],[3,4])`.
- Unpacking: `(a, b, c) = t` → `1 2 3`.
- `[(1,1),(2,4),(3,9)]` is a list of tuples.
- Use tuples for fixed records (student details, course info) to protect them from accidental change. Lists are for data that changes.
- A string and a tuple both refuse item assignment; a list allows it.

### 1.10 Sets

- `{"ring","amulet","ring","scroll"}` stores `ring` once (duplicates are ignored).
- Sets are **unordered** (the print order is unpredictable), have **no indexing**, and are **mutable** (`add`, `remove`, `discard`).
- A set guarantees uniqueness. A tuple is ordered and immutable.

### 1.11 Dictionaries

- Created with `{}` or `{'a':10, 'b':20}` (text keys need quotes). Values can be dicts: `{'a': {'a': 10}, 'b': 10}`. `'a': 10` without braces as a value is a SyntaxError.
- Keys are **unique**. Assigning to an existing key **overwrites** its value. Values may repeat.
- Keys must be **immutable**, strictly *hashable* (str, number, a tuple of immutable items; a tuple containing a list cannot be a key, and neither can a list). `1`, `1.0` and `True` are the **same key**: assigning all three leaves `{1: "boolean one"}` with the last value.
- Adding: `courseData["CS101"] = "Web Programming"`. Reading a missing key → `KeyError`.
- Methods:

| Method | Does |
|---|---|
| `keys()` | all keys (a view) |
| `values()` | all values (a view; `20, '30'` keep their types) |
| `items()` | (key, value) pairs, shown as `dict_items([...])` |
| `pop(key)` | removes the key and returns its value |
| `del d[key]` | removes the key |
| `clear()` | empties the dict |
| `update(other)` | copies the other dict's items in |
| `get(key)` | value or `None` (`student.get("age")`); no KeyError |

- Views cannot be indexed or `.count()`-ed in Python 3 (`l = d.values(); l[0] = 90` → error).
- Looping `for k in d` gives the keys. Nested loops can print nested records.
- Counting pattern: `if each not in d: d[each] = 1 else: d[each] += 1` (or `d[k] = d.get(k, 0) + 1`). The card version `try: d[k] += 1 except KeyError: d[k] = 0` starts at 0, so it counts *repeats* (one less than the number of occurrences).
- Dict comprehension: `{x: x*x for x in range(11) if x%2==0}` → evens and their squares.
- `my_dict[my_dict[1]]` looks up twice.
- Two dicts with `"zzz"` vs `"ZZZ"` are not equal (case matters).
- Adding a key while looping over `d.keys()` → `RuntimeError: dictionary changed size during iteration`.
- Sorting by value: `sorted(p.items(), key=operator.itemgetter(1))`.
- The key with the largest value: `max(d.items(), key=operator.itemgetter(1))[0]`.
- Merging without overwriting: `for k in d2: if k not in d1: d1[k] = d2[k]`.

### 1.12 Functions

- Reasons to use functions: readability, reusing code, easier debugging, an overview of the task.
- `return` sends a value back. `return a, b` returns a tuple (`result[0][1]`, `result[1]`).
- Defaults and keywords: `weighted_sum(1, z=4)` with `y=2` → `1 + 2*4 = 9`.
- Composition: `add_three(double(4))` → 11.
- A function returning a constant (`return 5`) is a **many-to-one** function. `n % 2` returns only 0 or 1.
- A function is an object:
  - `print(identity)` shows the function object and `identity()` calls it.
  - `fun = len; fun(a)` works.
- **Redefining** a function replaces the earlier one (the second `def func` wins).
- Assigning a string to the function's name (`message = "..."`) and then calling `message()` → `TypeError: 'str' object is not callable`.
- **Mutable default argument**: in `def log_error(msg, log=[])` the list is created once and shared, so the second call prints `['E1','E2']`. Passing `[]` explicitly gives a fresh list.
- `if __name__ == "__main__":` runs only when the file is executed directly.

### 1.13 Recursion

- A function calling itself on a smaller instance is **recursion**.
- The **base case** (anchor) is required. Without it the function never stops: an infinite loop, which Python ends with `RecursionError`. A proper base case returns a fixed result and stops the recursion.
- Recursion vs iteration:
  - Anything recursive can be written with loops, and the reverse.
  - Recursion is usually **slower** and uses more memory (a stack frame per call, so the extra space is O(n)).
  - Recursive code is often shorter and reusable.
  - A problem does not have to be "recursively defined" to be written recursively.
- Results you should be able to trace:

| Code | Result |
|---|---|
| `fact(n) = n*fact(n-1)`, `fact(0)=1` (or `factorial(n-1)*n`) | n! |
| `mystry(n) = mystry(n-1)+mystry(n-2)`, n<2 → n | Fibonacci; `mystry(25)` = 75025 |
| `test(i,j)`: `i==0` → j, else `test(i-1, i+j)`; `test(4,7)` | 17 |
| `f(n) = 4 + f(n-1)`, `f(0)=0`; `f(8)` | 32 |
| `f(n) = f(n-1) + 2` | 2n (negatives via `-1*f(-n)`) |
| `mul(1) = -1`, `mul(n) = -1*mul(n-1)` | (−1)ⁿ |
| `fun(n)`: `n/3` while divisible, 0/1 base | 1 if n is a power of 3, else 0 |
| `fun(k, n) = k*fun(k, n-1)`, n==0 → 1 | kⁿ |
| `xyz(a, b) = a + xyz(a, b-1)` | a × b |
| `recursive(a) = a + recursive(a-1)`, 0 → 0 | sum 1..a (10 → 55) |
| `mystery(n) = 1 + mystery(n-1)` | n |
| first item + recursion on the rest | sum of the list (1..10 → 55) |
| `1 + func(L[1:])` if `L[0]` even | count of even elements |
| `L[-1] + func(L[:-1])` if `L[-1]` odd | sum of odd elements |
| product while more than 6 items, else last item | product from index 5 onwards |
| `rfun(4)` printing after the recursive call | prints 2, 6, 24 (prints happen while unwinding) |
| even num → print `'*'*num`, recurse; odd → recurse; `recursive(10)` | 10, 8, 6, 4, 2 stars, then one `*` |
| `abc(num)` calling `abc(num-1)` with no base case | `RecursionError` |
| recursion where `input()` (a string) is compared with 10 | never equal → infinite |
| `f(n)`: perfect square → sqrt, odd → 3n+1, even → n/2, n<1 → n²; `f(10000)`, `f(-8)` | 7, 5 |

- In-place reverse with recursion:
  - Swap `nums[start]` and `nums[end]`, then recurse inward. Stop when `start > end`.
  - An odd middle item stays put. `[]` returns `[]`.
  - Length 6 needs 3 swapping calls.
  - The function mutates the list and returns it. The recursive call sits inside the final `return helper_reverse(...)` line, so deleting that line stops the recursion after the first swap (and the function returns `None`). The stored key for 2026-jan/w06/q10 says otherwise; see Part 6.

### 1.14 Files

| Mode | Meaning |
|---|---|
| `'r'` | read; calling `write` → error |
| `'w'` | write; creates the file or **erases** it first; calling `read` → error |
| `'a'` | append at the end, keeping the old content |
| `'r+'` | read and write |

- `with open(name, mode) as f:` closes the file automatically.
- `read()` returns the whole text and `readlines()` a list of lines. Appending to that list does **not** change the file.
- Writing with `'w'` twice keeps only the second content. `'w'` then `'a'` gives both, joined: `hey there!!writing this file again`.
- A file holding `"0110"`: summing `int` of each character → 2.

### 1.15 Complexity facts

- Linear search: worst case O(n) comparisons (n). Average for a successful search = (n+1)/2 (5 for n = 9).
- Binary search: about log₂ n comparisons. The cards use 1000 → 10, 1024 → 10, 2048 → about 11, 256 → 9 (with `arr[mid]==target` checks), and 1,000,000 → about 20.
- Bubble sort: n−1 passes and n−1 comparisons per pass at most. It is worst when the input is in reverse order.
- Quick sort is the "fastest" answer (n log n average).
- Python loops over pixels are slow; NumPy vectorised operations are much faster.

---

## Part 2 — Libraries: what each part does

### 2.1 `random`

- **`randint(a, b)`** returns int from a to b, **both inclusive**. Trap: `randint(1,10)` can give 10; using `randint(0, len(L))` as an index can give an `IndexError`
- **`randrange(a, b[, step])`** works like `range`: **b excluded**. Trap: `randrange(1,10)` never gives 10; `randrange(50,100)` → 50–99; `randrange(1,100,10)` → 1, 11, …, 91
- **`random()`** returns float in [0, 1). Trap: no arguments
- **`uniform(a, b)`** returns float between a and b. Trap: not an index
- **`choice(seq)`** returns one random element. Trap: `choice(0, n)` has the wrong arguments
- **`choices(seq)`** returns list of k (default 1) random elements.
- **`sample(seq, k)`** returns list of k **distinct** elements. Trap: `"".join(random.sample(word, len(word)))` jumbles a word
- **`shuffle(list)`** reorders the list **in place** and returns `None`. Trap: can produce the original order

`random.choice` works directly on a string: `random.choice(string.ascii_uppercase)` is the same as using `list(...)` (a "Lot Box" of A–Z). `random.select`, `random.range`, `random.movie` and `random.node` do not exist. `random` is the module for random numbers. Runs give different results (simulations vary run to run).

### 2.2 Statistics

- `stats.trim_mean(data, proportion)` (scipy.stats): `trim_mean(L, 0.1)` cuts 10% from **each** end, and 2% is `0.02`.
- A **trimmed (truncated) mean**:
  1. Sort the values.
  2. Drop the top and bottom 10%.
  3. Average the rest.

  It reduces the effect of outliers. `estimates.sort()` sorts ascending, in place, and changes the original list.
- `statistics.mean` and `statistics.median` exist.

### 2.3 `matplotlib.pyplot` (as `plt`)

- The library for 2-D graphs. It draws line, bar, scatter, pie and histogram charts, not only line graphs. It is **not** for maps (use gmplot).
- `plt.plot(x, y, fmt)`, `plt.show()`, `plt.title`, `plt.xlabel`, `plt.ylabel`, `plt.legend`, `plt.figure`.
- A histogram shows how values are distributed.
- Format strings combine a colour letter, a marker and a line style:
  - Valid: `'g^'` = green triangles, `'ro'` = red circles, `'r--'` = red dashed line, `'bs'` = blue squares, `'b+'`, `'b*'`, `'b--'`.
  - **Invalid**: `'b++'`, `'r---'`.
- `plt.plot(x, y)` with x = y draws a straight 45° line. With `x` reversed, `plt.plot(y, x)` draws a line with negative slope.
- Choosing a fair graph:
  - Compare averages (not totals) when counts differ.
  - A cumulative total never goes down.
  - A pie chart's larger slice is the larger group.

### 2.4 `datetime`, `time`, `calendar`, `pytz`

`datetime`:

| Expression | Result |
|---|---|
| `datetime.datetime.now()` / `dt.now()` | current local date and time, `2026-10-12 23:34:33.760029` (year-month-day h:m:s.microseconds) |
| `datetime.date.today()` / `date.today()` | today's date, `2017-06-18` |
| `datetime.date(2018,12,12)` | prints `2018-12-12` |
| `datetime.datetime(2021,9,16)` | `2021-09-16 00:00:00` (midnight) |
| `datetime(y, m, d, h, mi, s, µs)` | argument order; the last is **microseconds**; `.month` etc. are attributes |
| `datetime.datetime.utcnow()` | UTC time (with `import datetime`, the class is `datetime.datetime`); deprecated since Python 3.12 in favour of `datetime.now(timezone.utc)` |
| `.weekday()` | Monday = **0** … Sunday = 6 |
| `.isoweekday()` | Monday = **1** … Sunday = 7 |
| `date + timedelta(days=i)` | moves the date; `date(2024,2,29) + timedelta(days=1)` → `2024-03-01`; adding `timedelta(days=99)` to the birth date gives the 100th day (MiSeDol) |
| `date2 - date1` | a `timedelta`; `.days` is the number of days between (5 Aug → 12 Oct 2025 = 68) |
| `date` object | has only year, month and day; `.hour` → `AttributeError` |
| `.astimezone()` on a naive datetime | assumes the local zone |
| `datetime.now().strftime('%x')` | locale date `mm/dd/yy` |

- `strftime` codes: `%A` full weekday name, `%B` full month name, `%d` day, `%Y` 4-digit year, `%W` week number of the year (6 June 2021 → 22), `%w` weekday number with Sunday = 0, `%x` locale date, `%Z` zone name (`IST`).
- `import datetime`, `from datetime import datetime` and `import datetime as dt` are all valid.
- `datetime.now()` and `date.today()` both give today's date. Login tracking needs `datetime.now()`, because it has the time too.
- `datetime.now()`, `date.today()` exist. `datetime.present()` and `date.now()` do **not**.

`time`:
- `time.time()` → seconds since the epoch (1 Jan 1970).
- `time.sleep(s)` → pause.
- `time.localtime()` → local time.

`calendar`:

| Function | Returns |
|---|---|
| `calendar.month(y, m)` | formatted string of one month (year first: `month(2021,10)`) |
| `calendar.prmonth(y, m)` | prints a month, returns nothing (there is no `printmonth`) |
| `calendar.calendar(y)` | whole-year calendar string |
| `calendar.prcal(y)` | prints the whole year |
| `calendar.isleap(y)` | Boolean |
| `calendar.leapdays(y1, y2)` | number of leap years in [y1, y2): `leapdays(2000, 2020)` → 5 |
| `calendar.weekday(y, m, d)` | 0 = Monday … 6 = Sunday (Friday = 4, Saturday = 5) |
| `calendar.day_name[i]` | name for a weekday number |
| `calendar.FRIDAY` etc. | weekday constants |
| `calendar.monthrange(y, m)` | (weekday of the 1st, number of days); `[1]` is the day count; `monthrange(2022,2)` → `(1, 28)` |
| `calendar.monthcalendar(y, m)` | 2-D list of weeks, each 7 day numbers Mon…Sun, **0** for days outside the month (`week[0]` = Monday, `week[4]` = Friday, `week[5]`/`week[6]` = Sat/Sun) |

- **Weekday-name trap**: `calendar.weekday()` counts from Monday = 0. Indexing a Sunday-first list (`['Sunday','Monday',…][i]`) therefore gives the wrong name (off by one). The 2020-sep card's accepted answer does exactly this. `calendar.day_of_week` and `datetime.weekday(y, m, d)` do not exist.

Calendar results that appear on cards:
- 9 Oct 2021 → 5 (Saturday).
- 1 Dec 2000 → 4 (Friday).
- January 2024 starts on a Monday and has 23 weekdays.
- Friday-the-13th counts in 1996 and 2024 are equal (2 each).
- 1990–2024 has 9 leap years.

`pytz`:
- The time-zone library.
- `pytz.all_timezones` lists every zone name (it can grow with newer versions).
- `pytz.timezone('Singapore')` / `('Asia/Kolkata')` gives a zone object.
- `dt.now(pytz.timezone(z))` gives the time in that zone.
- `tz.localize(naive)` attaches a zone without changing the clock time.
- Filtering: `[tz for tz in pytz.all_timezones if tz.startswith('Asia')]`.

### 2.5 `copy` and `operator`

- `copy.deepcopy(x)` makes a fully independent copy (see 1.8).
- `operator.itemgetter(1)` picks the second element (the value of an item pair) and is used as a `key=`.

### 2.6 NumPy (`import numpy as np`)

- Arrays are `ndarray`s, faster than lists (compact memory, one data type). The fast parts are written in C/C++. NumPy is used for matrices and for image pixels.
- `print(np.array([1,2,3]))` → `[1 2 3]` (no commas).
- `Numpy.array` → `NameError` (case).

| Expression | Result |
|---|---|
| `a.shape` | tuple of dimensions, an **attribute**; `np.array([[1,2,3],[4,5,6]]).shape` → `(2, 3)`; `a.shape()` → `TypeError` |
| `a.size` | total elements (`[[1,2,3],[0,1,4]]` → 6) |
| `a.T`, `a.transpose()`, `np.transpose(a)` | transpose; `a.T()` → error; `a.transpose` without `()` prints the method |
| `a.reshape(r, c)` | 12 items → `reshape(3,4)` / `reshape(4,3)` |
| `np.zeros((3,3))`, `np.ones((3,3))` | arrays of 0.0 / 1.0 (floats: `1.`) |
| `np.sum(a)` | total |
| `np.sum(a, axis=0)` | **column** sums (`[[1,2,3],[4,5,6]]` → `[5,7,9]`) |
| `np.sum(a, axis=1)` | **row** sums (`[[1,2],[3,4]]` → `[3 7]`) |
| `np.sum(p, axis=2)` on 2-D | `AxisError` |
| `a + b`, `a - b`, `a * b` | element-wise (`[1,2,3,5,8] + [0,3,4,2,1]` → `[1,5,7,7,9]`, then `* a` → `[1,10,21,35,72]`) |
| `a += 3` | adds in place to every element |
| shape `(3,)` × shape `(3,1)` | broadcasting → a 3×3 multiplication table |
| `arr[1, 2]` | row 1, column 2; `arr[1, -5]` counts from the end of row 1 |
| `a[1:4]` | `[2 3 4]` |
| `np.dot(A, B)` with (3,4)·(4,2) | shape (3, 2) |
| `np.random.randint(1, 5, (2,5))` | 2×5 array of ints 1–4 (upper limit excluded) |
| `np.random.rand(...)` | random floats in [0, 1) |
| `np.asarray` / `np.asanyarray(input)` | converts scalars, lists, tuples, lists of tuples and so on to an ndarray |
| `np.zeros([200,200,3], dtype=np.uint8)` | a black 200×200 RGB image array |
| `arr[:, :100] = [255,0,0]` / `arr[:, 100:] = [0,0,255]` | colours the **left** columns red / the **right** columns blue (`arr[:100]` would be the top rows) |
| `np.add(a1, a2)` | element-wise sum; left-red + right-blue gives a left-red/right-blue image |

### 2.7 PIL / Pillow (`from PIL import Image`)

- **PIL = Python Imaging Library**. Pillow is its maintained successor but is still imported as `PIL`. It opens many formats and can rotate and resize images. `from PIL import image` (lower case) → `ImportError`.

| Call | Does |
|---|---|
| `Image.open('f.jpg')` | load an image |
| `im.show()` | display |
| `im.save('new.png')` | write to a file (a copy with the same content) |
| `im.rotate(45)` | rotated copy |
| `im.transpose(Image.FLIP_LEFT_RIGHT)` / `FLIP_TOP_BOTTOM` | mirror / flip (there is no `flip` method) |
| `im.size` | `(width, height)` |
| `im.mode` | type, such as `'RGB'` or `'L'` |
| `Image.new(mode, size[, colour])` | new blank image; `Image.new(im.mode, im.size)` matches another image |
| `Image.fromarray(array)` | image from a NumPy array (a 200×200×3 array with the top 100 rows `[255,0,0]` and the rest `[0,0,255]` → red on top, blue below) |
| `im.getpixel((x, y))` | colour value of one pixel |
| `im.putpixel((x, y), colour)` | change one pixel (in memory until saved) |
| `pixels = im.load()` | pixel-access object; `pixels[x, y]` is an `(r,g,b)` **tuple** for RGB, a single int for grayscale |
| `im.thumbnail(size)` | shrink in place **keeping the aspect ratio** (`resize` forces the exact size) |
| `Image.open(f).convert('L')` | convert to grayscale (mode `'L'`, one value 0–255 per pixel) |
| `numpy.asarray(Image.open(f))` | image → NumPy array of pixel values |

- An image is a **matrix of pixels**. A colour has 3 values (RGB).
- Converting to black and white is **irreversible**: the colours cannot be recovered.
- Legacy: `scipy.misc` read images as NumPy arrays (the cards write `scipy.misc.read`).
- OpenCV (`cv2`): `clahe = cv2.createCLAHE()`, then `clahe.apply(gray)` enhances a grey image.

### 2.8 `turtle`

| Command | Does |
|---|---|
| `turtle.Turtle()`, `turtle.Pen()`, `turtle.Screen()` | create a turtle / the screen |
| `forward(d)` | move ahead |
| `backward(d)`, `back(d)`, `bk(d)` | three names for moving backward |
| `left(a)`, `right(a)` | turn; `right(-45)` = `left(45)` (anticlockwise) |
| `goto(x, y)`, `setpos(x, y)` | jump to a point (there is **no** `moveto`) |
| `penup()` / `pendown()` | stop / resume drawing; **the default state is pen down** |
| `dot()` | draw a dot |
| `speed(n)` | 1 slowest … 10 fast; **0 = fastest** (no animation) |
| `color()` | pen and fill colour |
| `pencolor()` | line colour |
| `fillcolor()` | fill colour (`changecolor` and `putcolor` do not exist) |
| `shape()` | turtle shape |
| `turtle.done()` | keep the window open |

- Turtle graphics come from **Logo**. The `turtle` module is "the" animation library on the cards.
- Polygons: n sides with a turn of **360/n**.
  - Triangle: 120° (equilateral).
  - Square: 90° (4 sides; `range(3)` draws only 3).
  - Hexagon: 60°.
  - Octagon: 45°.
  - Five-point **star**: 144°.
  - Forward or backward, left or right: any combination with equal sides and 90° turns gives a square.
- Pen-up on every other side of a hexagon draws 3 separate edges.
- A spiral of dots: `forward(2 + i/4)` with `left(30 - i/4)`.
- The turtle can draw any shape built from moves and turns.

### 2.9 `gmplot`, `csv`

- `gmplot` plots data on **Google Maps**.
  - `gmap = gmplot.GoogleMapPlotter(lat, lng, zoom)` creates a base map centred there.
  - `gmap.marker(lat, lng, title=name)` adds a marker.
  - `gmap.draw("file.html")` saves the map as HTML.
  - A marker needs a latitude and a longitude.
  - The GPS route program reads points from a CSV file (so it imports `csv` **and** `gmplot`).
  - Its purpose is to track the user's directions or route.
  - In one card the first row gets a red marker and the later rows yellow markers.
- **CSV = comma-separated values** (values separated by commas, tabular data).
  - `csv.reader(file)` reads rows.
  - `csv.writer(file)` writes rows with `writerow`.

### 2.10 NLTK, VADER, TextBlob, pandas

- **NLTK = Natural Language Toolkit**. It processes human (natural) language, not images.
  - `nltk.download()` fetches data packages (for example `'punkt'` for tokenisers).
  - `word_tokenize(text)` splits text into words and punctuation (`100%` → `'100'`, `'%'`).
  - `sent_tokenize(text)` splits text into sentences (`!!!` ends a sentence).
  - **Tokenisation** splits text into smaller units, which makes language easier to process.
  - `FreqDist(tokens)` / `nltk.FreqDist()` counts tokens (capital F and D). `len(freq)` = **unique** tokens and `len(tokens)` = all tokens. `freq[word]` is a count. `freq.plot(20, cumulative=False)` plots the top 20.
  - `stopwords.words('english')` gives common words such as `the` and `of`. Removing them shifts word-length distributions toward longer words.
  - `isalpha()` (a string method) keeps purely alphabetic tokens.
- **VADER = Valence Aware Dictionary and sEntiment Reasoner**.
  - A **lexicon and rule-based** sentiment tool. A lexicon is a dictionary of words with sentiment scores (positive or negative orientation).
  - It accounts for the **intensity** of emotion ("good" vs "very good!!!").
  - `SentimentIntensityAnalyzer()` → `.polarity_scores(text)` gives `neg`, `neu`, `pos` and **`compound`**. The compound score is normalised to **−1…+1**, so 1.5 is impossible.
  - In the cards' code, compound > 0 means Positive. VADER's own documented thresholds are compound ≥ 0.05 positive, ≤ −0.05 negative, and neutral in between.
  - It is often used with **pandas DataFrames**: `df['Sentiment'] = df['Review'].apply(get_sentiment)` adds a column of labels.
- **Sentiment analysis** decides whether text is positive, negative or neutral. A factual sentence ("SCCI labs … deals with research in Social Computing") is **neutral**.
- **TextBlob**: `TextBlob(text).sentiment.polarity` runs −1…+1, and 0.0 = neutral. Corpus-level sentiment smooths local noise.
- pandas: `import pandas as tiger` then `tiger.DataFrame(data)` builds a table from a dict of columns.

### 2.11 NetworkX (`import networkx as nx`)

- Used to **create, analyse and visualise** networks (it does not "break" them). It is written in Python, so it is **slow on large-scale** problems. Gephi (and Cytoscape) are graph visualisation tools. **Eclipse** is an IDE, not a graph tool.

| Call | Does |
|---|---|
| `nx.Graph()` / `nx.DiGraph()` | undirected / **directed** graph (capital D and G) |
| `G.add_node(1)`, `G.add_nodes_from(iterable)` | add nodes; list, set or dict keys all work |
| `G.add_edge(u, v[, weight=w])`, `G.add_edges_from([...])` | add edges; a repeated `(2,1)` after `(1,2)` is the same edge |
| `G.nodes()`, `G.edges()` | nodes / edges (empty graph → `[]` on the cards; current NetworkX prints `NodeView(())`); `len(G.nodes)` = number of nodes |
| `G.neighbors(n)` | directly connected nodes |
| `G.degree(n)` | degree of a node |
| `G.out_degree(n)`, `G.in_edges(n)`, `G.out_edges(n)` | directed versions; edges come back as tuples |
| `nx.path_graph(4)` | nodes `[0,1,2,3]` in a chain |
| `nx.complete_graph(10)` | every pair joined |
| `nx.cycle_graph(4)` | closed loop of 4 (undirected) |
| `nx.star_graph(6)` | a centre plus **6** leaves (7 nodes) |
| `nx.barbell_graph(m1, m2)` | two complete graphs of m1 nodes joined by a path of m2 nodes (`barbell_graph(8,3)`) |
| ladder graph, wheel graph | two rails with rungs; a centre joined to a ring (wheel of 5 = centre + 4-ring) |
| `nx.gnp_random_graph(n, p)` | **Erdős–Rényi** random graph: n nodes, each edge made with probability p; `p = 1` gives a complete graph (always connected); `p = 0.5` is **not** always connected |
| `nx.is_connected(G)` | True if a path exists between every pair |
| `nx.shortest_path(G, s, t)` | node list (counts edges if no weight) |
| `nx.shortest_path_length(G, source, target)` | 2nd argument = source, 3rd = target |
| `nx.average_shortest_path_length(G)` | = degree of separation |
| `nx.pagerank(G)` | returns a **dictionary** node → rank |
| `nx.read_edgelist("file.txt")` | graph from lines "u v" |
| `nx.write_gexf(g, 'Friendship.gexf')` | export to GEXF (for Gephi) |
| `nx.draw(G, with_labels=True)` + `plt.show()` | draw |
| `subgraph(G, nbunch)`, `union(G1,G2)`, `disjoint_union(G1,G2)`, `cartesian_product(G1,G2)` | operations; `disjoint_union` assumes all the nodes are **different** |

- A function that is defined but never called (graph loader): the next use of `graph` is the error line.
- Choosing a random node: `random.choice(list(G.nodes()))` (older versions: `random.choice(A.nodes())`).

### 2.12 Selenium (browser automation)

- `selenium` is **the** browser-automation library. It is open source and used for testing web apps, load/performance testing and web data extraction.
  - It runs on many browsers (Chrome, Firefox, Edge, Safari) and platforms (Linux, Mac OS X; the cards also list iOS, though mobile automation really needs Appium).
  - It automates the **web only**. Native mobile apps need Appium.
- The recommended import is `from selenium import webdriver`, then `driver = webdriver.Firefox()` or `webdriver.Chrome()`.
  - A WebDriver launches and controls a browser session.
  - The remote WebDriver is part of Selenium.
  - `webdriver.ActionChains` is valid; `webdriver.HtmlUnit` is **not** a valid class.
- `driver.get(url)` opens a page.
- The 2026 case code uses the Selenium 4 imports:
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as ec
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.common.by import By
  ```
  Then:
  - `webdriver.Chrome('path_to_chromedriver.exe')` (old style; Selenium 4.10+ needs `webdriver.Chrome(service=Service(path))` or no path at all).
  - `WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath)))` with `xpath = f"//span[contains(@title, '{name}')]"`.
  - `target.click()`.
  - `driver.find_element(By.CLASS_NAME, "_1Plpp")`.
  - A loop of `send_keys(text)`, `send_keys(Keys.RETURN)` and `time.sleep(1)`, then `driver.quit()`.
- Locating elements (Selenium 3 names as on the cards):
  - `find_element_by_id` is the best and fastest locator (ids are unique).
  - `find_element_by_name`, `find_element_by_class_name` (the first element with that class), `find_element_by_link_text`, `find_element_by_css_selector` (yes, by CSS) and `find_element_by_xpath` (XPath finds an element).
  - Selenium 4 writes these as `find_element(By.ID, ...)`.
- `element.send_keys("text" + Keys.ENTER)` types and presses Enter (`Keys.RETURN` also works). `send_keys` does **not** locate elements. `element.click()` clicks.
- Waiting:
  - `WebDriverWait(driver, 600).until(EC.presence_of_element_located(...))` waits only as long as needed, which gives buffer time for slow networks.
  - `time.sleep()` always waits the full time.
- `driver.quit()` ends the whole session and frees resources. Closing the window by hand can leave the driver running.
- WhatsApp Web automation:
  - Tasks it can do: send media, read messages, manage groups, update the profile.
  - The QR login is manual (it is tied to a real user's phone, for security).
  - Locating the contact by name in an XPath can match the wrong chat.
  - The script depends on WhatsApp's page structure (DOM, class names), so a page change breaks it.
  - Removing the delay between messages risks UI failures or account restrictions.
  - It is ethically sensitive (spam, harassment).

### 2.13 Speech recognition

- The library is `SpeechRecognition` (imported as `speech_recognition`); it converts speech to text, for example audio into lyrics.
- It reads **WAV, AIFF, FLAC**, not MP3. WAV (`.wav` / `.wave`) = Waveform Audio File Format, which holds audio recordings.
- `UnknownValueError` is raised when the audio cannot be understood.
- PyAudio supplies the microphone and the `wave` module reads WAV files. Neither does the recognition.

---

## Part 3 — Course topics and algorithms

### 3.0 Week 0 aptitude maths

- Numbers:
  - Primes have exactly **2 factors**. 1 is not prime (the odd one out in 1, 2, 3, 5). 6 is the odd one out of 2, 3, 5, 6.
  - The primes up to 30 are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 (10 of them).
  - 124 = 2²×31.
  - HCF(12,18) = 6.
  - LCM(4,8) = 8, LCM(12,8) = 24, LCM(5,15) = 15, LCM(18,57) = 342.
- Sums:
  - First n naturals = n(n+1)/2 (10 → 55).
  - First n odds = n² (10 → 100, 27 → 729).
- **Armstrong number** = sum of the cubes of its digits: 407 = 4³+0³+7³. A 2-digit variant uses the sum of squares.
- Sequences:
  - 4, 8, 16 → 32.
  - 9, 36, 144, 576 (×4) → the sum of 5 terms is 3069.
  - 1, 5, 13, 25 (differences 4, 8, 12) → 41.
- The golden ratio ≈ **1.618**.
- Circles:
  - Perimeter 2πr, area πr².
  - Doubling the radius quadruples the area.
  - A circle inscribed in a square of side s has diameter s (circumference sπ). In an 8×4 rectangle the diameter is the short side, 4 (12.57).
  - Circle area = the sum of circles with diameters 10 and 24 → diameter 26; diameters 6 and 8 → 10.
  - Equal perimeters, circle vs square: area ratio 14 : 11.
  - Circumference 31.4 → area 78.5.
- Squares and rectangles:
  - Perimeter 100 → area 625.
  - Tripled side gives perimeter 120 → original side 10.
  - Length 4× width with area 100 → width 5.
  - Scaling 2× and 3× multiplies the area by 6 (1800 → 300).
- Probability with two dice (36 outcomes):
  - Same number: 6/36 = 1/6.
  - Both even: 1/4.
- Inclusion–exclusion: neither = total − (A + B − both) (40 students → 16; 80 employees → 32).
- Speed, time and other puzzles:
  - 281 km in 281 minutes = 1 km/min.
  - A train passing a person moving the opposite way: add the speeds (55 m at 123 km/h ≈ 1.6 s).
  - A wheel of radius 3 m turning 14 times a minute covers 5.28 km in 20 min.
  - Discount: price = paid / (1 − rate) (74.8/0.85 = 88 → 44 each).
  - Cost = area × rate (90×74×11 = 73260).
  - Clock: the hour hand turns 30° per hour (5 → 11 pm = 180°).
- Pattern puzzles:
  - n – n = n² − 1 (11 → 120).
  - PARLE → QCUPJ is a +1, +2, +3, +4, +5 shift, so DABUR → ECEYW.
- Ratio: boys A:B = 2:1, girls A:B = 4:5 and equal totals → boys A : girls A = 1:2.
- Graph shapes:
  - Constant draining → a straight line falling.
  - Drive, stop, return → up, flat, down.
- Counting squares in a figure (27).

### 3.1 Week 1: Scratch

- Block categories:
  - **Motion**: `move (n) steps`, `turn ↻/↺ (n) degrees`, `glide`, `go to x: y:`, `set x to` / `set y to`, `change x by`, `point in direction`, `point towards`.
  - **Looks**: `say`, `think`, `show` / `hide`, `next costume` (changes the sprite's style or look), `change size by` (+ bigger, − smaller), `switch backdrop to`.
  - **Sound**: sounds come from the library, a microphone recording or an imported file.
  - **Control**: `wait (n) secs`, `repeat (n)`, `repeat until`, `forever`, `if`, `if-else`. There is **no** `forever until`.
  - **Sensing**: `touching (sprite)?`.
  - **Operators**: `join` (full name from first + last), `pick random a to b` (inclusive: 1 to 10 can never give 12), `mod`, `abs of`, `sqrt of`, `+ - * /`. There is **no power block**.
  - **Events**: `when ⚑ clicked` (the green flag starts the program), `broadcast` / `when I receive` (how sprites communicate).
  - **Variables**: they can be renamed, deleted and set.
  - There is no "Jump" category.
- Sprites come from the library, painting, uploading or the camera.
- The Scratch file extension is **`.sb`**.
- Semantics:
  - `move -10 steps` moves backwards.
  - `repeat t { turn 30 }` makes a full rotation when t = 12 (360/30).
  - Blocks run top to bottom, and the **last** `point in direction` before a move decides that move's direction (direction 90 = right; 60 = 30° up).
  - Swapping `turn` and `point in direction` changes the path.
  - Removing the reset block leaves the earlier heading in place.
  - `repeat until` checks **before** each pass, so if the condition is already true the body never runs.
  - `forever` never stops by itself.
  - Hide/show swaps poses (situps).
  - `set x / set y` at the start puts the sprite at a fixed starting point every time.
  - `glide to random position in 1 sec` inside `repeat 10` → 10 random positions, 1 second each.
- Trace results on the cards:
  - `change t by 3` ×10 from 3 → 33.
  - `change by -1` ×10 → −10.
  - From 100 with −2 ×10 → 80.
  - Start 0, +5 −1 per pass ×10 → 40.
  - Start 10, +10 ×10 then ÷5 → 22.
  - `((5+5)*5)/10` → 5.
  - Odd numbers: start 1, step 2.
  - Even filter with `x mod 2 = 0`.
  - A multiplication table via `i * j`.
  - Factorial with `repeat until counter > 5`.
  - The `j += x` while `i` counts down from `y` → x × y.
  - 7 random numbers added to x.
- Geometry:
  - Move 100, turn 90, move 100 → distance √(100²+100²) = 141.42.
  - Three moves with 120° turns → a triangle.
  - Small move plus small turn repeated → a circle or curve (a 340° total is an open curve).
  - CCW tilt = take-off/up, CW tilt = landing/down.
  - Nested `repeat 3 { repeat 4 { turn 90 } }` → 3 full rotations and 2 loops.
  - `repeat 1` is the same as no loop.
  - Squared distance = (x1−x2)² + (y1−y2)².
  - x from 0–20 with y = 20x − x² → a parabola ending 20 steps along x.

### 3.2 Week 3 projects

- **FizzBuzz**: multiples of 3 → Fizz, of 5 → Buzz, of both → FizzBuzz, so **test "both" first**.
  - 510 and 285 → FizzBuzz.
  - With user inputs a, b: fizz if divisible by a but not b, and so on.
- **Jumbled word**: a word of n distinct letters has n! arrangements, so **n! − 1** jumbled ways to pose it (CAT/SIT/HIT → 5; COMP → 24 arrangements; PUCROTEM → COMPUTER).
  - Code: `"".join(random.sample(word, len(word)))`; `", ".join(...)` gives a comma-separated version.
  - Collecting random jumbles until there are n! may give repeats.
- **Crowd computing / wisdom of crowds**: many independent estimates average out, so a crowd can be as good as an expert or better.
  - Use a **trimmed mean** (sort, drop 10% each end).
  - Examples: Wikipedia, Stack Exchange/StackOverflow, Quora, Facebook. ChatGPT and Twitch are not.
- **Genetic evolution / DNA**: a string of 0s, and flipping a random bit = mutation → evolution. Flipping each bit with probability 0.1 gives a random string with a few 1s.
- **Digit-sum puzzles**:
  - Peeling digits with `% 10` and `//= 10` gives the digit sum (10294343763482 → 56; 245326785456 → 57; trailing zeros add nothing).
  - A sort of the same digits never changes the sum.

### 3.3 Week 4 projects

- **Magic square** (n×n, numbers 1…n² each once):
  - Every row, column and both diagonals sum to the **magic constant n(n²+1)/2** = (n⁴+n²)/2n.
  - Values: 3 → **15**, 4 → 34, 5 → 65, 6 → 111, 7 → 175, 11 → 671. Ramanujan's magic square has constant **139** (differences 105 and 74).
  - The largest number in 5×5 is 25; 4×4 uses 1–16.
  - 3×3 solution: `8 1 6 / 3 5 7 / 4 9 2`. Filling `6 a 8 / b 5 c / 2 d 4` → a, b, c, d = 1, 7, 3, 9.
  - Order 1 is trivial and **order 2 is impossible**. The course algorithm (odd N) needs **N odd**.
  - The sum of two magic squares is magic. The transpose of a magic square is magic, with the same sums. Scaling every entry (×π) or subtracting a constant (−e) keeps it magic.
  - The lecture's algorithm (a rotated variant of the Siamese method, which classically starts in the top-middle cell):
    1. Put 1 at row n/2, column n−1.
    2. The next number goes to (i−1, j+1), wrapping around the edges. The statement "(i+1, j−1)" is **false**.
  - The prototype fills the matrix with zeros, so empty cells are easy to spot.
  - A checker verifies a square matrix plus row, column and diagonal sums.
- **Birthday paradox and pigeonhole principle**:
  - k categories → **k+1** people guarantee a shared one: 13 (months), 8 (weekdays), 366 (days in a non-leap year), 26 cards of 25 colours, 49 for 48 half-hour slots.
  - To guarantee **3** sharing: 2k+1 (97).
  - The chance of sharing your own birthday is 1/365.
  - The probability of some collision rises with group size: about 50% at 23 people, and "simulated with ≈40 people".
  - Collision probability is higher for a non-leap year (fewer days).
  - Simulation: `random.randint(1,365)` or `datetime` dates (a leap-year check for February).
    1. Convert each date to its day of the year (ignore the year).
    2. Sort, so duplicates sit next to each other.
    3. Counts differ each run.
- **Dobble (Spot It)**:
  - Any two cards share **exactly one** symbol; the deck has 55 cards with 8 symbols each.
  - Finding it takes at most k×k = **k²** comparisons (10 symbols → 100; 8 vs 10 → 80).
  - CHKIEF vs KYNOTQ → K.
  - In the generator, the common symbol and every used symbol are removed from the pool, which guarantees exactly one common symbol.
  - The pool `ascii_letters` gives at most 52 symbols. Positions are `randint(0,4)` for 5 slots (`0,5` → IndexError).
  - `pos1` and `pos2` may be equal. With `pos1 ≠ pos2` the filling loop runs 3 times.
  - Lowercase input for an uppercase symbol counts as wrong (an exact match is needed).
- **Guess the Movie**:
  - The title is shown as blanks or `*`.
  - A guessed letter opens **all** its copies at once, so a state with a letter open in one place and blank in another is impossible.
  - A missing letter gives a "not present" message and the game continues (no "nearest letter" is opened).
  - It ends when the masked title equals the title.
  - Input is converted with `.upper()`, and `isalpha()` decides what to mask.
  - 3-letter titles give 26³ = 17576 combinations.
  - Scoring variant: points = blanks remaining.
  - Pattern matches: `I_C_P_IO_` = INCEPTION, `A_E__E__` = AVENGERS.
  - Code: `random.choice(movies)` picks a title. Common-movie and unique-movie loops use a flag. A vowel counter counts both cases.
- **Leap year**: divisible by 4 and not by 100, **or** divisible by 400.
  - 1900 → not (February 28), 2000 → yes, 2100 → no, 2024 → yes.
  - Equivalent forms: `(y%100==0 and y%400==0) or (y%4==0 and y%100!=0)`.
  - A wrong version adds 100 and 1900 as leap years.
- **Number checks**:
  - Primes: test divisors 2…i−1 with a flag, or 2…√n. Note that `position <= 2: return False` wrongly rejects 2.
  - Perfect numbers: the sum of divisors below n equals n (6 = 1+2+3).
  - Factors of n excluding n (primes → `[1]`).
  - Common factors of two numbers.
  - Perfect squares via `j*j == i`.
  - Fibonacci via `a, b = b, a+b`.
- **Drunkard's walk**:
  - On a number line (+2 −4 from p, stepping one unit at a time to detect hitting 0).
  - On an XY plane (0.4 right, 0.4 up, 0.2 diagonal).
- **Masked-gun game** steps (generate a secret code → display → loop → …): an ordering question.

### 3.4 Week 5 projects

- **Monty Hall** (show "Let's Make a Deal"):
  - 3 doors: 1 car, 2 goats.
  - The host always opens a goat door: P(opens a goat | you picked the car) = 1, and P(not a goat) = 0.
  - **Switch wins 2/3, stay wins 1/3.**
  - P(first pick wrong) = 2/3. If the first pick was a goat, the car is surely behind the other closed door.
  - If you pick right first, switching loses.
  - The lesson: probability changes when new information is revealed.
  - Simulation:
    - `random.shuffle(doors)` places the car fairly.
    - The host chooses from `[i for i in range(3) if i != choice and doors[i]=='goat']`, so he never reveals the car. Letting the host open any door breaks the 2/3 result.
    - Switching sets `choice` to the remaining unopened door.
    - Thousands of trials approximate the probabilities (empirical).
  - In the simple game with no host reveal, more doors means a lower win chance.
- **Rock-Paper-Scissors**:
  - 3×3 = 9 combinations and 3 draws. No choice guarantees a win. Rock beats scissors, scissors beat paper, paper beats rock.
  - Secure version: each player types a long digit string with a **secret position**. The digit at that position mod 3 maps through that player's own table.
    - Without the positions the winner cannot be determined.
    - Example: 456 and 684 with positions 0 and 2 → 4 and 4 → Paper (P1) beats Rock (P2).
  - Rock-Paper-Scissors-Lizard-Spock: 5 choices and mod 5.
  - A `wins_against` dict maps a move to the move it beats.
  - Simulations: fraction of throws equal (`==`) or different (`!=`).
- **Searching**:
  - Linear search works on any list, sorted or not. It checks one by one and returns the index, or −1 / "not present".
  - **Binary search needs a sorted list** (ascending or descending, with the comparison adjusted).
    - Divide and conquer: `low=0`, `high=len−1`, `mid=(low+high)//2`.
    - If the target > `arr[mid]`, go right (`low=mid+1`); else go left (`high=mid−1`).
    - Stop when `low > high` → −1.
  - With duplicates, binary search may not find the first copy (a small modification can).
  - On an unsorted list it may miss an element that is present.
  - It is not *always* better: if the target is first, linear search wins.
  - Trace `[1,3,5,7,9]` for 7 → index 3. 8 elements: first mid = 3. 10 gates: first mid = index 4 (117), then search the right half.
- **Bubble sort**:
  - Each pass compares **adjacent** pairs and swaps if they are out of order. The largest moves to the end (`[2,9,5,4,8,1]` → `[2,5,4,8,1,9]`).
  - The inner loop fetches the consecutive pairs.
  - Swaps = number of inversions: [8,22,7,9,31,19,5,13] → 14; [8,22,7,9,31,5,13] → 10.
  - Pass 3 of [5,3,8,4,2] → [3,2,4,5,8]. Swaps in pass 3 of [4,3,2,1] = 1, of [5,4,3,2,1] = 2.
  - `if a[i] < a[j]: swap` over i<j sorts **descending**.
- **Random experiments**:
  - Bins and balls (10 bins, 100 balls). Finding the bin with the most balls (despite a variable named `min_`).
  - Printing bins in descending order by deleting the max.
  - Coin tosses until a head. Rolling until an even number. Rolling while the answer is 'y' or the sum is 12.
  - Two dice sum 2–12.
  - Proportional selection by age (running totals).

### 3.5 Week 6 projects

- **Ciphers**:
  - A **cipher** = an algorithm for encryption and decryption (the encrypted text is the ciphertext).
  - **Caesar**: shift every letter by the same amount. It is a **special case of the substitution cipher**. At most **26** tries break it.
    - −1 shift: AMIT → ZLHS, VIDHYA → UHCGXZ, SOUJANYA → RNTIZMXZ, GOLD → FNKC, PLATINUM → OKZSHMTL.
    - +4: PYTHON → TCXLSR, DIAMOND → HMEQSRH, COMPUTING → GSQTYXMRK.
    - Alternating ±3: PYTHON → SVWERK, COMPUTING → FLPMXQLKJ.
    - Lower +2 / upper +3: "The Joy OF Computing" → "Wjg Mqa RI Fqorwvkpi".
    - Subtracting 26 from a lowercase code → the capital 6 letters on.
  - **Substitution**: any fixed letter-to-letter map (SUDARSHAN/BHAWANA → SHUBH = YWLTW; COMPUTER/SCIENCE → SET = YQW).
    - Decrypt with the **reversed** key dict.
    - Digit coding: `string.digits[i-1]` maps each digit to the previous one (0 → 9).
  - **Frequency analysis**: substitution keeps letter frequencies, so the most common cipher letter ≈ `e` (a rare `z` mapped to `r` makes `r` rare).
    - It works on long texts.
    - It fails when the text is short or was encrypted with another method first.
- **Tic-Tac-Toe**:
  - A 3×3 matrix.
  - **8** winning lines (3 rows, 3 columns, 2 diagonals). The centre is on **4** lines, a corner on 3, an edge on 2, so starting in the centre gives more chances.
  - Strategy: **Min-Max (minimax)**: maximise your chance and minimise the opponent's, i.e. minimise the maximum possible loss.
  - A board with no three-in-a-row is a draw.
  - Game code:
    - Input like `2` without a comma → "Invalid input", asked again.
    - `turns += 1` only after a valid move.
    - It stops at a win. The `while … else` prints a draw.
    - A row checker `row[0]==row[1]==row[2] and row[0] != ' '` checks rows only and uses `break`.

### 3.6 Week 7 projects

- **Snakes and Ladders**:
  - You win by reaching the last cell (100). A game also ends if the player quits.
  - Track snakes and ladders with a dict (square → destination), `if/elif` tests (the instructor's way) or lists.
  - Landing on a snake head moves you at once, so you can never "stand" on 87 when `87: 18`.
  - At 19 a roll of 2 → 21 → ladder to 42. At 96 you need exactly 4 (P = 1/6), because 3 lands on the snake at 99.
  - The minimum throws for the given ladder set = 5. Without ladders ≈ 17, so the answer is "less than 30".
  - Variants:
    - Start only on 1 or 6.
    - Ignore moves beyond the target (`position + roll <= target`).
    - A snake re-drawn on every call (moving snake); a `flag` limits it to one bite.
    - An 8-sided die changes the roll step; a 200-tile board changes the setup and win check.
    - Ambiguity when `ladder_begin == snake_begin`.
    - A Chaupar/Pachisi step order of 2, 1, 3.
- **Spiral traversal** of a matrix:
  - Top row → right column down → bottom row backwards → left column up, then move inwards.
  - `k`, `l` = start row/column and `m`, `n` = end boundaries. After each side the matching boundary moves (`k += 1` after the top row).
  - In a 5×5, after (1,5) comes (2,5).
  - The problem is broken into a 2-D table.
  - Other orders appear: column down-then-up; reversed spiral from a stack; ring at layer i; snake pattern.
  - A drone visits every cell from the outside in.
- Recognising image-processing results such as compression and flip (see 2.7).

### 3.7 Week 8 projects

- **Gambling and lotteries**:
  - Expected value per play = P(win) × prize − cost. Pick 1 of 10, win 500, cost 100 → −50, so ten plays guarantee nothing; don't play.
  - Gambling is bad because over time you lose more than you win.
  - Lottery simulation over 30 days, losing 100 on a miss:
    - With no wins the balance is −3000.
    - P(win) per day = 1/10.
    - The graph shows long declines with rare jumps (+900 or +800 net).
    - More days give a more reliable result.
  - Other simulations:
    - Guessing a number daily for a year.
    - Average heads in 100 tosses over 100 plays.
    - A game with a 0.5 chance beats one with a 2/5 chance.
    - A plot that goes up on a mismatch and down on a match.
- **Anagrams**:
  - The same letters in a different order: listen/silent, night/thing, dusty/study, "A gentleman"/"Elegant man", Looted/Toledo. Not anagrams: cat/arc, "Monasteries"/"Aman stories".
  - Test with `sorted(s1) == sorted(s2)` (not `s1.sort()`), or compare lengths then per-character counts.
  - Equal ASCII sums are **necessary but not sufficient** ('ad' and 'bc' both sum to 197).
  - A puzzle generator: shuffle until the arrangement differs. A one-letter word loops forever.
- **Isomorphic strings** ("structural equivalence"):
  - `egg`/`add` → True and `ab`/`cc` → False.
  - Check the length first, then keep two dicts (s→t and t→s) for a one-to-one mapping.
- **Clap game**: claps when `ord(p1)+1 == ord(p2)` (the next letter).
- **Image enhancement**:
  - Enhancement (contrast) reveals hidden information.
  - **CLAHE = Contrast Limited Adaptive Histogram Equalisation**. It equalises small tiles, combines tiles by bilinear interpolation to **remove** artificial boundaries, and handles noise better than plain AHE.
  - Compression is what stores many images in little space (see 3.9).
- **Stylometry** basics: different people have distinct writing habits; "any two people may have the same vocabulary" is **not** a stylometry premise.

### 3.8 Week 9 projects

- **Stylometry** = the quantitative study of literary or linguistic style, mainly for authorship attribution. It rests on authors writing in unique ways.
  - Features: average word length, word-length distribution, sentence length, punctuation, word frequency, stopwords, Jaccard similarity, stylistic devices.
  - Methods: Kilgarriff's chi-squared, Burrows's Delta, word-length plots.
  - The cover or publisher does not identify an author.
  - **Project Gutenberg** = a repository of free ebooks.
  - Federalist Papers case (Hamilton, Madison, Jay, Disputed, Shared):
    - Preprocessing: tokenise, keep `isalpha()` words, drop stopwords (case is kept: "Liberty liberty Constitution").
    - Plots show word-length frequency.
    - Only stopwords → an empty plot. Without the stopword filter → a shift to shorter lengths.
    - Longer words → peaks at larger lengths. Multiple authors → a broader distribution.
  - Average-word-length code: `x = [len(w) for w in words]`; " Natural Language Processing Using Python " → 36 total, 7.2 average. Average sentence length must divide by the number of sentences, **not** `len(text)`.
  - A word-count code that removes empty strings and dashes counts 82 words.
- **Six degrees of separation**:
  - On average, any two people are about **6** steps apart (also called the "six handshakes" rule).
  - Proposed by **Frigyes Karinthy**, and tested by **Stanley Milgram**'s small-world letter experiment (≈6 intermediaries).
  - It is an *average*, not a minimum or maximum.
  - Degree of separation = **average shortest path length**.
    - Complete graph → 1.
    - Path of 6 nodes → 35/15 = 2.333.
    - Ring of 9 → 2.5.
    - The 10-node tree on the card → 2.82.
  - Friend-of-friend counts grow exponentially, so the paths are short.
  - Facebook dataset: `read_edgelist`, skip `u == v`, collect all pair lengths, compute the average. All-pairs shortest paths are expensive.
- **Graph basics**:
  - Node degree = the number of edges at the node. It identifies influential people.
  - The sum of degrees = 2 × edges, which is always even (a 4-cycle → total 8).
  - A complete graph has n(n−1)/2 edges (4 nodes → 6; 5 nodes → 10, the most edges a random loop on 5 nodes can add).
  - Connected = a path exists between every pair.
  - Friends of friends form a path through the middle person.
  - **Barabási–Albert** model → **scale-free** networks. Erdős–Rényi = `gnp_random_graph`.
  - Counting nodes, edges and neighbours from pictures. Edges `(1,2),(2,1),(2,3),(3,4),(4,1),(3,1)` → a square with a 1–3 diagonal.
- **Area estimation (Monte Carlo)**:
  - Throw random points over a known region. In principle, sub-area ≈ (points in the sub-region / all points) × total area. **The lecture code and the stored keys divide by the points in the rest of the country instead** (see 7.3 and Part 6); use that version on the exam.
  - It works for irregular shapes. More points mean less random variation and better accuracy (the law of large numbers), though it is not efficient everywhere.
  - Cards: 5400 km² with 23 state points → 1774.3 km² (the key divides by 70); India 10400 km² → Maharashtra 2657.77 km² (divides by 90).
  - Quarter circle: a point is inside if x² + y² ≤ r² (correct code → −1).
- **Images**:
  - RGB = 3 values. `getpixel` reads, `putpixel` writes.
  - `Image.new`, `save`, `fromarray`. A string of letters `list('joc python')`.

### 3.9 Week 10 projects

- **FLAMES** (Friends, Love, Affection, Marriage, Enemies, Siblings):
  1. Lower-case both names and remove spaces (for a fair comparison).
  2. Cancel common letters one at a time; `remove_matching_letter` returns right after one removal to avoid an `IndexError` with stale indexes.
  3. Count the remaining letters.
  4. Go round "FLAMES", removing the letter at `(count−1) % len(flames)` (the modulo keeps the index valid) and rotating, until **one letter** is left.
  - Card answers:
    - SAKSHI/AKASH → Friends.
    - ALIA/ANKIT → count 5.
    - RANVEER/DEEPIKA → Affection.
    - RAVIKIRAN/ANUSHKA → count 8.
    - RANBIR/ALIA → Marriage.
    - Alice/Bob → Affection.
  - The pattern is circular counting with iterative elimination, i.e. the **Josephus problem**.
    - Recurrence: J(1) = 1, J(n) = (J(n−1) + k − 1) % n + 1.
    - n = 25, k = 3 → 14.
- **Compression**:
  - Smaller files and lower quality (lossy). It can also change file type, resolution and bit depth.
  - **Lossless** (PNG) restores the original exactly; **lossy** (JPEG) throws detail away. They are not the same, and image compression is **not always** lossy.
- **Pixel processing**:
  - `img.load()` gives pixel access. `img.size` = (width, height).
  - A 200×100 image → 20,000 inner-loop passes.
  - `(r+g+b)//3` average: (90,150,180) → 140. With `average > 127` → bright; 127 counts as dark.
  - **Quantisation** to `floor(v/32)` → values 0–7, so the saved image looks **nearly black** (31 → 0, 223 → 6).
  - Without grayscale conversion the code fails (tuples). NumPy vectorisation speeds it up.
- String drills: replacing vowels at even first-occurrence positions; removing consonants; taking characters at even positions; reversing word order; writing a pattern file (`letters[i]` + `letters[-1-i]`).

### 3.10 Week 11 topics

- See 2.4 and 2.12.
- **PageRank** first appears here too: websites are nodes and hyperlinks are edges, and the "leader" is the node visited most (random walk). Details in 3.11.

### 3.11 Week 12 topics

- **PageRank**:
  - An algorithm to rank nodes in a network, originally the importance of web pages for search. The web graph has **pages = nodes, hyperlinks = edges** (directed).
  - The rank of a page depends on the rank of the pages referring to it (and, per one key, of the pages it refers to).
  - **Who** links matters more than how many: a link from an important page counts more. "The person liked by the most people is the most impressive" is **false**.
  - Inbound links from important pages raise rank. A node is important if important nodes point to it.
  - A page with many out-links gives a smaller share to each. Fewer out-links → a bigger share. The total a page gives = its current rank.
  - **Random walk (drunkard's walk)**: from a node, move to a random node it points to (one of its out-links).
    - At a **sink** (no outgoing edges) → jump to a random node from **all** nodes.
    - After many steps, the most-visited node is the leader. Points = visits.
  - **Point distribution**: every node starts with equal points (no bias). Each iteration a node divides its points **equally** among its out-links.
    - The total stays **constant**.
    - It is iterative and converges to the same distribution whatever the start; stopping too early gives misleading ranks.
    - Sinks trap points.
  - Code details:
    - A separate `new_rank` / `updated` dict keeps every contribution based on the original ranks.
    - Sorting the final values ranks the nodes, and converting to a dict keeps node–score pairs.
    - `nx.pagerank()` validates the manual result. A random graph tests scaling. Mathematical convergence makes it reliable.
  - A gold-coin game on a graph: the coins stay constant and can all end at a sink.
  - Google also uses content relevance and user experience.
- **Directed graphs**:
  - One edge goes only one way.
  - Directed examples: web links, citations, Twitter follows, supply chains, wikigraph, airline routes. **Facebook friendship is undirected.**
  - `out_degree` counts arrows leaving; a node with only incoming arrows has out-degree 0. `in_edges('D')` lists the edges ending at D.
  - Weighted edges can mean interaction time, relationship strength or shared interests.
  - A random walk explores the graph and reveals its properties.
- **Graph types**:
  - Barbell (two cliques plus a path) is connected.
  - Complete: every node has degree n−1.
  - Cycle: degree 2.
  - Star: leaves have degree 1.
  - Ladder, wheel.
  - A cycle 1-2-3-4-5-1 drawn as a star (pentagram layout).
  - A ring of 4 → (4 nodes, 4 edges).
  - The code that adds random edges until the graph is connected can never output a disconnected graph.
- **Collatz conjecture (3n+1 problem)**:
  - Even → n/2; odd → **3n+1** (not 3n). It stops at 1 (the 4, 2, 1 cycle).
  - It is an **open/unsolved problem**. Every number checked reaches 1 (none below 200 or 3000 fail).
  - Bigger numbers do **not** always take more steps.
  - Sequences:
    - 9 → 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
    - 10 → 5, 16, 8, 4, 2, 1.
    - 3 → 10, 5, 16, 8, 4, 2, 1.
  - Steps:
    - 75 → 14.
    - 7 → 16.
    - 8 → 3.
    - 5 → 5 steps (the key says 6, counting the numbers).
    - A power of 2 takes log₂ n steps.
  - The program prints 1 after the loop ends. `steps` goes up once per pass.
  - The variant 5n+1 from 7 → 7, 36, 18, 9, 46, 23, 116, 58, 29, 146.

---

## Part 4 — Edge cases and traps (all found on the cards)

These are code snippets where the intuitive answer is wrong:

1. `print( " "Hello" " )` → SyntaxError (the quote ends early).
2. `i + = 1` → SyntaxError, so nothing prints, not even the earlier lines.
3. `if(n>1) print(...)` → SyntaxError (no colon). An unindented `print` under `if` → IndentationError.
4. `if(number = 0):` → SyntaxError.
5. `c = b ** 3` with `b` undefined → NameError. `x = y` with `y` undefined → error.
6. `'5' * 3` → `'555'`; input `20` * 2 → `'2020'`; input `30` * 2 → `'3030'`.
7. `d = "a"; d + 1` → TypeError.
8. `3 == 3.0` → True.
9. `3*1**3` → 3 (`**` first).
10. `17 % -5` → −3.
11. `int(3.79) + int(2.1)` → 5. `int("123abc")` → ValueError.
12. `print('new' 'line')` → `newline`.
13. A lone `'''string'''` → no output.
14. `s.replace(...)` without assignment → `s` unchanged.
15. `word[2] = 'n'` → TypeError (strings are immutable).
16. `S.uppercase()` → AttributeError. Strings have no `append` or `insert`.
17. `'#'.join('JOC')` → `J#O#C` (no leading or trailing `#`). `'.'.join(['','h',…])` → leading `.`.
18. `sorted("HI! Amitabh")` → starts with `' '`, `'!'`, then capitals.
19. `L.sort()` → capitals first (`'Practice'` before `'makes'`).
20. `[1,2,3,4].append([5,6,7,8])` → length 5.
21. `a.insert(-3, 999)` → goes before the third-from-last item.
22. `b = a; b.append(40)` → `a` changes too.
23. `b = a.copy(); b[0][1] = 99` on nested lists → `a` changes. `b[1] = [0,0]` → `a` does not.
24. `copy.deepcopy` → nothing shared.
25. `x += [1,2]` inside a function changes the caller's list. `y += (3,4)` does not change the caller's tuple.
26. Rebinding a dict parameter (`d = {...}`) → the caller is unchanged.
27. `def log_error(msg, log=[])` → the default list is shared between calls.
28. A second `def func` → the first is replaced.
29. `message = "text"` after `def message()` → `message()` is a TypeError.
30. `print(identity)` → a function object, not a call.
31. `fun = len; fun(a)` → works.
32. `('purple')` is a string, so tuple + it → TypeError. `('Poonam',)` is a tuple.
33. `((1),(2))` → `(1,2)`. `t = 1, 2, 3` → a tuple.
34. `del t[2]` → TypeError, while `del t` → fine.
35. `tup[0].append(5)` → allowed (the inner list is mutable).
36. `{1: 'a', 1.0: 'b', True: 'c'}` → a single key `1` with value `'c'`.
37. `d[i] += 1` on a new key → KeyError.
38. `d.values()[0]` or `.count()` → error (it is a view).
39. Adding keys while looping over a dict → RuntimeError.
40. `{"ring", "ring"}` → one item. Sets are unordered and cannot be indexed.
41. `random.randint(1,10)` includes 10, `randrange(1,10)` excludes it, and `np.random.randint(1,5,…)` excludes 5.
42. `random.choice(0, len(movies))` → wrong. `randint(0, len(movies))` → can raise IndexError.
43. `random.shuffle` returns `None` and can return the same order.
44. `range(100)` starts at 0. A "1 to 100" claim fails for code that starts at 0.
45. `for lang in range(len(L)): print(lang)` → prints indexes.
46. `while True` with an unchanged condition variable → infinite. `while n >= 0` with `n //= 10` → infinite.
47. A recursion without a base case → RecursionError, described as an "infinite loop". `L[-1]` on an empty list → IndexError.
48. Opening `'w'` then `read()` → error. Opening `'r'` then `write()` → error. `'w'` erases the old content.
49. `readlines()` list changes → the file is unchanged.
50. `from PIL import image` → ImportError.
51. `data.shape()` → TypeError. `b.T()` → error. `b.transpose` without `()` → prints the method. `Numpy.array` → NameError.
52. `numpy.sum(p, axis=2)` on 2-D → AxisError.
53. `np.ones` gives floats (`1.`).
54. Broadcasting `(3,)` × `(3,1)` → 3×3.
55. The `plot` format strings `'b++'` and `'r---'` are invalid.
56. `nx.gnp_random_graph(n, 0.5)` → not always connected. `p = 1` → always connected.
57. `import network as nx`, `G.add node` with spaces, `nx.draw()` without a graph → error.
58. A repeated undirected edge `(2,1)` after `(1,2)` → one edge.
59. `calendar.weekday` / `datetime.weekday` → Monday = 0. `isoweekday` → Monday = 1. `strftime('%w')` → Sunday = 0.
60. `calendar.month(year, month)` takes the year **first**.
61. `datetime.date(...).hour` → AttributeError.
62. `leapdays(2000, 2020)` excludes 2020 → 5.
63. `monthrange(...)[1]` → the day count, not the first weekday.
64. A VADER compound score outside −1…1 is impossible.
65. A pixel average of exactly 127 with the test `> 127` → "dark".
66. Comparing `0 <= pixel <= 31` on an RGB pixel → TypeError (it is a tuple).
67. Lowercase vs uppercase in exact comparisons (Dobble input, dict values) → not equal.
68. In the Jack/Jill code, the combined `and` condition placed after a single condition is never reached.
69. `a,b = 1,0; a=a^b; b=a^b; a=a^b` → `a` = 0 (a swap).
70. `L = [[1,2,3],[0,4,5],[0,0,6]]` with `j` from 2 down to `i` → `3 2 1 5 4 6`.
71. `l = []*100` → still `[]`.
72. Bubble-style `a[i] < a[j]` swap over i<j → **descending** order.
73. `list1 = [1,3]; list2 = list1; list1[0] = 4` → `list2` = `[4,3]`.
74. `x = [10,20,30,40]` and `linear_search(arr, 25)` → −1.
75. `for w in range(len(weights)): sum += w` adds the **indexes** 0–4, not the weights. `for w in weights` is correct.
76. `if arr[i] == key: …break` followed by `if arr[i] % 2 == 0: continue` before a print → even numbers are skipped silently. `[3,8,1,7,9,2]` with key 7 prints `Checking 3`, `Checking 1`, `Found at index 3`.
77. Recursive binary search must go **left** (`low, mid-1`) when `arr[mid] > x`. The option that goes right in that case is wrong.
78. `a.Tran()` is not a NumPy method → error (use `a.T`).
79. In a Scratch "repeat 18" loop that sets the position before `change x by 1`, the last position is x = 17, not 18.
80. A negative number in `while n != 0: n //= 10` → infinite loop (it sticks at −1).
81. Weekday names from `calendar.weekday()` with a Sunday-first list → off by one.
82. Truthy conditions: `if 2:` runs, and so does any non-zero number or non-empty string.
83. In `print('_ '),` (Python 2 style) the trailing comma makes a tuple expression in Python 3; each call still prints on its own line.
84. Prime-printer variants:
    - `for j in range(2, 101)` or `range(2, i+1)` also tests `j == i`, so every number "has a divisor" and nothing prints.
    - `for i in range(101)` also prints 0 and 1.
    - Only `range(2, i)` with `i` from 2 is correct.
85. Perfect-number variants: `range(3, num)` misses divisors 1 and 2; swapped `True`/`False` or `!=` inverts the answer.
86. Turtle near-misses:
    - `range(3)` with `right(60)` / `forward(60)` draws half a hexagon.
    - `range(6)` with `right(30)` turns only 180°, so it is not closed.
    - A star with `range(3)` and 144° turns is unfinished; it needs 5 (or 6) sides.
87. Character arithmetic:
    - `chr((j+26) % 26)` gives control characters, not letters.
    - `(i + 26)` where `i` is a string → TypeError.
    - `((j+26-97) % 26) + 97` and `((j-97) % 26) + 97` both return the same letter.
88. Writing a file opened with `'r'` → error. Writing every line with `'\n'` adds a trailing newline. `range(len(letters))` instead of `// 2` writes 26 lines.
89. Star patterns: `if j >= 10-i and j <= 10+i: print('*')` with `i` going up then down → a diamond / triangle of stars.

---

## Part 5 — How to answer case/scenario questions

The 2025-jul, 2026-jan and 2026-jul sessions use a **case study**: a story plus a program (often with line numbers), followed by 5–20 questions on it. The other sessions also have "predict the output" / "what does this code do" cards. In the exam the code is given, so what you need is a method, plus the facts in Parts 1–3.

The case families on the cards, so nothing surprises you:
- Scratch: game scores, battery and loop counters.
- A nested-loop number pattern; a palindrome-number checker; a discount calculator.
- Kiosks for registration, cafeteria orders and bookstore checkout (input, conversion, update); an exercise counter (`while`).
- A grocery order list (append/insert/extend/sort/slice); student marks with comprehensions and tuples.
- A library catalogue (sort/reverse/count/insert/len); a workshop participant list; traffic-signal FizzBuzz; a wildlife survey (trimmed mean, histogram).
- A mini Dobble; list copy semantics; a birthday collision simulator; a Dobble generator; a magic-square prototype; the movie guessing game.
- Student records in nested dicts plus graphs; book-ID search (linear vs binary); a library borrow tracker (dict update/max); a Rock-Paper-Scissors championship (dict); airport gate search; reusable functions (methods vs attributes); a Monty Hall simulation.
- In-place array reversal (recursion); a terminal Tic-Tac-Toe; a secret notice encoder (substitution dict); a Tic-Tac-Toe winner checker; recursive folder search; recursive binary search over roll numbers.
- Tuples vs sets (archive); tuples/lists/dicts/files (learning centre); a drone spiral route; a mini snake-and-ladder; food-delivery gmplot markers.
- A lottery strategy simulation; isomorphic strings; student-record tuples; a lucky-draw game; an anagram puzzle generator; customer-feedback VADER with pandas.
- Federalist Papers stylometry plus TextBlob; Facebook shortest paths; product-review FreqDist; a book recommendation network; social six degrees; image quality inspection (`getpixel`/`putpixel`/`new`/`save`).
- FLAMES (two versions); grayscale quantisation; wildlife sunlight pixels; overexposure detection.
- WhatsApp Selenium automation; an academic schedule analyser (datetime/calendar); semester/meeting/shift/training planners (`monthcalendar`).
- Simplified PageRank code (one iteration); club PageRank; Collatz step counting.

"Predict / what does it do" families in the older sessions (2018–2025):
- **Factorial variants**: a loop multiplying 1…a−1 then adding 2 or 3 → `(a−1)! + 2` or `+ 3`. Outputs 722/723 fix `a` (factorial 720 = 6!). To print 8 you need (a−1)! = 6 → a = 4; for 123, a = 6.
- **Name/age filters**: print "You are lucky" when the age ≥ 18 and the name has more than one or two `a`s. Both prints sit inside `if flag == "True"`, so an underage person prints nothing.
- **Growing lists**: pass `i` builds a list of length `i`, so `a` = `[0 … n−1]` and the sum n(n−1)/2 = 21 → n = 7; 10 → n = 5. A value v is appended only when n > v.
- **Index-parity transforms**: even index → `x*2` (always even), odd index → `x+3` (either parity); odd index → `x*4`, even → `−x`. Changing the formula can make a stated property hold.
- **Digit sums**: `k` and `b` are both digit sums (sorting the digits changes nothing), so `b == k` always and one message never prints.
- **Factor lists**: `mystery1(n)` = factors below n; primes give `[1]`, so any two primes share exactly 1. A threshold of `len(list2) > 0` vs `> 1` decides whether "Completed" prints.
- **Infinite-loop fixes**: update the loop variable before the `if`. A `while` whose body has `i += 1` indented wrongly. Input-driven loops (`while c == 1`, entering 5 ends it).
- **Star / pattern printing**: a `j` range `10-i … 10+i` prints a triangle; the snake / spiral / ring orders of matrices.
- **Two-list comparisons**: common items by position vs by value; unique items of L1 (flag + break); first-letter matches are case-sensitive.
- **Counting / max loops**: a minimum finder (`if i < a: a = i`), a palindrome with two pointers (`telugu` False, `malayalam` True), "remove max then min until 2 remain" → average of the last two (4.5), a vowel counter, prime/perfect-square printers, and a GCF loop keeping the last common divisor.

The method:
1. **Read the whole program once and label each line's role** (input, conversion, initialisation, loop header, condition, update, output). Many questions are just "which line does X?".
2. **Trace with a value table.** Write each variable as a column and add a row per loop pass. Count passes exactly (`range(a, b)` runs b−a times; nested loops multiply).
3. **"After line N" questions**: stop the trace at exactly that point (for example `max_books` right after line 21 runs the first time = the first item's value).
4. **"What if line X is removed or changed?" questions** fall into these patterns:
   - A missing update → the loop repeats the same value, or never ends.
   - A missing `break` → extra iterations, but the same result if the item is unique.
   - A missing `return` → the side effect still happens but `None` is returned.
   - A `+=` moved inside a loop → added every pass.
   - A swapped order → a different result.
   - A missing base case → infinite recursion.
   - A missing type conversion → TypeError or a repeated string.
   - A changed bound (`randint(0,5)` on 5 slots) → IndexError.
5. **"Select all that apply"**: test every option separately against the code. Options that describe something the code does *not* do (for example "checks columns" when it checks rows only, "counts days" when it counts Mondays) are false.
6. **Boundary tests**: `>` vs `>=` (127 → dark; ₹2000 → the premium rule applies), `<=` in a loop condition, and an empty input (`[]`, an empty string, a one-letter word).
7. **Randomness**: any statement claiming a fixed output from `random` code is false. "Different result each run" and "could be equal or different" are the safe facts.
8. **Library calls in the story**: map each call to Part 2. For example:
   - `img.load()` → pixel access.
   - `monthcalendar` → weeks with 0s.
   - `polarity_scores(...)['compound']` → the score.
   - `G.neighbors` → direct links.
   - `FreqDist` length → unique tokens.

---

## Part 6 — Doubtful answer keys (don't learn these as facts)

Each of these cards has a stored key that is wrong, ambiguous or depends on an odd reading. The correct fact is given beside it.

- **2024-jan/w05/q01 Monty Hall, 4 doors, host opens 1 goat, switch**
  - Stored key: 3/4
  - Fact: Switching to one specific remaining door wins 3/8 (staying wins 1/4).
- **2021-jul/w08/q07 pandas**
  - Stored key: `tiger.DataFrames(data)`
  - Fact: The class is `DataFrame` (singular).
- **2021-jul/w03/q06 "mean of a list"**
  - Stored key: `statistics.median(a)`
  - Fact: The mean is `statistics.mean(a)`; median is a different measure.
- **2018-jul/w10/q06 `np.zeros(3,3)`**
  - Stored key: 3×3 zeros
  - Fact: Needs a tuple: `np.zeros((3,3))`; `zeros(3,3)` raises an error.
- **2018-jul/w10/q07 `a.shape()`**
  - Stored key: `(2,3)`
  - Fact: `shape` is an attribute: `a.shape` is `(2,3)`, and `a.shape()` is a TypeError (see 2025-jul/w05/q06).
- **2022-jul/w10/q04 `b = np.array([[1, 2]]), [3, 4]`**
  - Stored key: `[[4, 6]]`
  - Fact: The source line is garbled. For `np.array([[1,2],[3,4]])`, `np.sum(b)` = 10 and `axis=0` gives `[4 6]`.
- **2023-jul/w04/q04@gpt random letters grid**
  - Stored key: "A magic square of size n"
  - Fact: The code prints an n×n grid of random letters; it is not a magic square.
- **2023-jul/w06/q04@gpt `return num*(num-1)`**
  - Stored key: "product of first n terms"
  - Fact: It returns n×(n−1); there is no recursive call.
- **2023-jul/w06/q06@gpt `L[-1]*recursive(L[:-1])`**
  - Stored key: "infinite loop"
  - Fact: It reaches `[]` and `L[-1]` raises IndexError.
- **2020-sep/w06/q06, 2023-jan/w06/q09, 2024-jul/w06/q09 missing base case**
  - Stored key: "infinite loop" / "runs infinitely"
  - Fact: Conceptually yes; in Python it stops with RecursionError (2021-jan/w06/q09).
- **2023-jul/w06/q03@gpt**
  - Stored key: includes "recursive code is easier to debug"
  - Fact: A debatable statement that the key accepts.
- **2022-jul/w08/q04 storing a million images**
  - Stored key: Compression; Enhancement
  - Fact: Only compression reduces storage.
- **2023-jan/w04/q02 magic square N**
  - Stored key: "N should be odd"
  - Fact: True for the lecture's (Siamese-style) algorithm. Even-order magic squares exist (4×4), except order 2.
- **2019-jan/w11/q07, 2019-jul/w11/q04 "18 June 2017 (Thursday)"**
  - Stored key: weekday 3
  - Fact: 18 June 2017 was a Sunday (2020-jan/w11/q09 uses Sunday → 6). Answer from the card's stated weekday.
- **Binary search counts: 1000/1024 → 10, 256 → 9, 2048 → ≈11**
  - Stored key: mixed
  - Fact: With the usual code the worst case is ⌊log₂ n⌋ + 1 checks (1024 → 11); the cards round inconsistently. Follow each card's own convention.
- **2019-jul/w12/q07 vs 2021-jul/w12/q08 (random walk vs point distribution iterations)**
  - Stored key: "None of the above" vs "Statement b is correct"
  - Fact: The two sessions disagree.
- **2024-jan/w12/q10 Collatz of 5**
  - Stored key: 6
  - Fact: 5 → 16 → 8 → 4 → 2 → 1 is 5 steps. The lecture's `collatz()` starts `count=1`, so it counts the numbers including the start (6). Expect the lecture convention when a question says "the program".
- **2018-jul/w09/q01, 2019-jul/w09/q05 area estimation**
  - Stored key: divides by 70 / 90
  - Fact: This is the **lecture formula**: `AreaCalculate.py` counts country-coloured and state-coloured pixels separately and computes `(state points / rest-of-country points) × total area`. Use it on exams. A strict share-of-all-points reading would divide by 93.
- **2026-jul/w09/q05**
  - Stored key: includes "len(tokens) returns the number of unique words"
  - Fact: `len(tokens)` is all tokens; `len(freq)` is unique.
- **2026-jul/w09/q10**
  - Stored key: includes "Every node must be connected to every other node"
  - Fact: False for a general graph.
- **2026-jul/w09/q15**
  - Stored key: includes "Every pair of users must have a direct friendship for a path to exist"
  - Fact: False: paths can go through others (q12 on the same card set).
- **2026-jul/w09/q20**
  - Stored key: includes "getpixel() changes the color of a pixel"
  - Fact: `getpixel` reads; `putpixel` changes (q16–17).
- **2026-jul/w08/q20**
  - Stored key: includes "stores the sentiment score directly in the Review column"
  - Fact: The labels go into a new `Sentiment` column (q18). The NPTELWhisperer week-8 solution selects only "reviews in a DataFrame" and "labels via `get_sentiment()`".
- **2021-jul/w05/q09**
  - Stored key: "0"
  - Fact: The code prints "Element is not present in the given list" (108 is not in 1–100).
- **2018-jul/w09/q04, 2019-jan/w09/q04**
  - Stored key: `scipy.misc.read`
  - Fact: The legacy function was `scipy.misc.imread` (removed from modern SciPy).
- **Selenium `find_element_by_*` cards**
  - Stored key: as keyed
  - Fact: Selenium 3 names; Selenium 4 uses `find_element(By.…, …)`.
- **2020-sep/w11/q07 day of the week**
  - Stored key: Sunday-first list indexed by `calendar.weekday`
  - Fact: Off by one: `weekday` has Monday = 0.
- **2025-jan/w01/q10 Scratch parabola**
  - Stored key: stops 18 steps along x
  - Fact: The trace ends at x = 17.
- **2025-jan/w02/q08 infinite loop**
  - Stored key: "update `a` before the if"
  - Fact: The pictured code has no such `if`. The real risk is a negative `n` (`-1 // 10 == -1`).
- **2024-jan/w02/q07 multiplication table**
  - Stored key: prints the table
  - Fact: As printed, `i += 1` is indented deeper than `print`, which is an IndentationError.
- **2025-jan/w02/q03 decimal input**
  - Stored key: in(input()); int(input())
  - Fact: `a = int(a)` is not a decimal reader either.
- **2020-jan/w04/q05 dashes for a movie name**
  - Stored key: option A only
  - Fact: `for ch in range(len(ch))` also prints one dash per letter.
- **2020-sep/w04/q03 Lot Box**
  - Stored key: `choice(list(ascii_uppercase))` only
  - Fact: `choice(string.ascii_uppercase)` gives the same result.
- **2021-jan/w04/q09@portal guesses for a 5-letter title**
  - Stored key: 53,130
  - Fact: No clear basis: 53,130 = C(25,5); tracing gives at most 22 letter guesses.
- **2022-jan/w04/q02 leap-year program**
  - Stored key: option D
  - Fact: All four programs mishandle century years such as 1900.
- **2025-jan/w04/q04 valid magic squares**
  - Stored key: A, C
  - Fact: D (the first square × π) is also magic; the Jul-2024 version accepts it.
- **2024-jul/w05/q01 add a dict key**
  - Stored key: D
  - Fact: C (the same line ending in `;`) is also valid Python.
- **2022-jan/w06/q06 recursion without a base case on a list**
  - Stored key: infinite loop
  - Fact: `L[-1]` on `[]` raises IndexError.
- **2022-jul/w06/q05 binary search code**
  - Stored key: one option
  - Fact: Options C and D are identical code.
- **2026-jan/w06/q10 removing the final `return helper_reverse(...)`**
  - Stored key: still reversed, None returned
  - Fact: Without the recursive call only the first swap happens (D).
- **2026-jan/w06/q14 when the game stops**
  - Stored key: a win
  - Fact: Reaching nine turns also ends the loop.
- **2019-jul/w07/q06 spiral order in 5×5**
  - Stored key: …(1,4),(2,4)
  - Fact: A spiral goes on to (1,5) after (1,4).
- **2026-jul/w07/q20 heritage explorer**
  - Stored key: B, C
  - Fact: D (markers placed by latitude/longitude) is also true.
- **2026-jan/w08/q10 lottery losses**
  - Stored key: low win probability
  - Fact: 0.1 × 900 − 0.9 × 100 = 0, so the game is fair on average; the key is just the best option offered.
- **2024-jan/w10/q09 random matrix in [0,1)**
  - Stored key: `np.random.rand()` only
  - Fact: `np.random.random((r, c))` also works.
- **2022-jul/w11/q04, 2021-jul/w11/q05 current date and time**
  - Stored key: `now()`
  - Fact: `datetime.today()` also returns the current date and time.
- **2025-jan/w11/q05 modified linear search**
  - Stored key: "Found at index 3"
  - Fact: The loop prints `Checking 3`, `Checking 1`, then `Found at index 3`.
- **2024-jul/w11/q04 press Enter in Selenium**
  - Stored key: `Keys.RETURN`
  - Fact: `send_keys(Keys.ENTER)` also presses Enter.
- **2019-jul/w12/q06 Collatz of 9**
  - Stored key: A
  - Fact: Options A and D list the same sequence (NPTEL zero-weighted the question).
- **2019-jul/w12/q03 what a page's rank depends on**
  - Stored key: rank of pages it refers to + rank of pages referring to it
  - Fact: Only the pages **referring to it** matter (B, D).
- **2020-jan/w12/q04 vs 2022-jul/w12/q07 random node**
  - Stored key: "none of the above" vs `random.choice(A.nodes())`
  - Fact: Depends on the NetworkX version (`G.nodes()` is a view now); `random.choice(list(G.nodes()))` always works.
- **2022-jul/w12/q08 not true about Collatz**
  - Stored key: A, C
  - Fact: B ("steps are independent of the number") is also not true.

Cards with no stored answer, or whose answer is only a picture, are not listed one by one. Their concepts are covered in Parts 1–3: the spiral/turtle figure outputs (w07), plot shapes (w08) and the 2020-sep for-loop rewrite (w02).

---

## Part 7 — Lecture code, programming assignments and the final exam

Sources: `lecture-code/` (the course programs as written in the lectures), `programming-assignments/` (2021-jan, 2021-jul and 2022-jan solutions), `exams/` (the 2021 online programming tests, a recalled 34-question final exam paper and the exam-pattern notes).

### 7.1 Exam pattern

- **50 MCQs, 2 marks each = 100 marks, 180 minutes, no negative marking.**
  - Sections: 10 + 15 + 25 questions (the Oct-2023 note says 10 + 16 + 24; the split varies).
  - Some questions are multiple-select (more than one correct answer).
- Pass mark (per the older note): 40/100.
- Many questions come straight from the weekly quizzes, either word for word or with changed values or data. Others ask you to trace given code. A few come from the lectures.
- The exam-pattern notes name these topics: strings, lists, dictionaries, tuples, sets; loops and conditionals; `random` and NumPy; 2–3 Scratch/turtle questions; graphs (degree of separation, edge counts).

### 7.2 The recalled final exam (13 Dec, morning session, 34 questions)

Most were weekly-quiz questions already in this guide:
- FizzBuzz with a, b; `check_magic` printing all 2×2 matrices; the leap-year code that is *not* correct; the drunkard's walk.
- `get_gates` → two 'c' and one 'g'; `find(t, 99999)` → 0 to 99998; column down-then-up printing → `147741258852369963`.
- gmplot; the snakes-and-ladders start on 1 or 6; NLTK/VADER full forms; money proportional to age.
- `gnp_random_graph(100, 1)` connected → True; broadcasting `a*b` → a 3×3 table; `'ab'.isalpha()` → True; selenium.
- `Numpy.array` → NameError; GOLD→FNKC so PLATINUM→OKZSHMTL.

Questions that were new or changed:
- Edges of a complete graph on 10 nodes = 10×9/2 = **45**.
- A **tuple can be a dictionary key**: `d[(1,2,3)] = "apple"` works, because tuples are immutable and hashable. A list cannot be a key.
- `for i in range(5,-1,-1): print(i)` → 5 4 3 2 1 0.
- `while i <= 50` with an inner divisor loop that prints when `f == 1` → **composite** numbers (4, 6, 8, 9, …).
- 570 of every 1000 vote; for 20,000 → 570/1000 × 20000 = 11400.
- A letter-code puzzle in the style of COMPUTER → PLAMETUSOV, SCIENCE → WMAOLEPTY, then PYTHON → ? (the recall gives no answer).
- A `barbell_graph(m1, m2)` node count = **2·m1 + m2**.
- Pick the code for a left-aligned star triangle (`*`, `**`, `***`, …).
- `plt.plot(x, y, 'ro')` with y = x² → red dots on a rising parabola, not a line.
- Scratch `repeat n { turn 18° }`: a full rotation needs n = 360/18 = **20**.
- A lottery account-balance graph: "will you gamble?" → no.
- `def num(n): return -n if n > 0 else -n*-1` → always **−|n|** (the absolute negative value).
- `"".join(random.sample(word, random.randint(0, len(word))))` → a random subset of the letters of random length, which can be empty. It "may or may not" print the whole word.
- `List[-5:-1]` on `["hi","we","are","the","elements","in","the","list"]` → `['the','elements','in','the']`.
- `"hello".index('ells')` → **ValueError: substring not found**.

### 7.3 How the lectures wrote the course programs

Exam questions describe these programs, so know their exact logic:

- **Trimmed mean** (`Graphs.py`):
  ```python
  Estimates.sort()
  tv = int(0.1 * len(Estimates))
  Estimates = Estimates[tv:len(Estimates) - tv]
  mean(Estimates)  # from statistics import mean
  ```
  The same file draws `plt.plot([...], [...], 'r--')`.
- **Jumbled words** (`Hangman.py`, `Players.py`): a two-player game.
  - `choose()` = `random.choice(words)`; `jumble()` = `"".join(random.sample(word, len(word)))`.
  - Turns alternate with `turn % 2`, and the score is shown at exit.
- **Dobble** (`SameLetterCards.py`): `list(string.ascii_letters)` and two cards of 5. The shared symbol is placed at `pos1`/`pos2` and removed from the pool. Every other symbol is removed after use.
- **Magic square** (`MagicSquare.py`, odd n only):
  - The matrix starts as zeros. The first position is `i = n/2`, `j = n-1`.
  - Each next number goes to `(i-1, j+1)`.
  - Rule 3: if `i == -1 and j == n`, go to `(0, n-2)`.
  - Otherwise wrap: `j == n` → `0`, and `i < 0` → `n-1`.
  - If the cell is occupied, go to `(i+1, j-2)`.
  - It prints the magic sum `n*(n*n+1)/2` and formats cells with `'%2d '`.
- **Birthday / datetime** (`DateTime.py`):
  - `datetime.datetime.now()`.
  - `strftime`: `%Y` year, `%B` month name, `%d` day, `%W` week of the year, `%w` weekday number (Sunday = 0; the lecture comment wrongly calls it "week number of month"), **`%j` day of the year**, `%A` weekday name.
- **Dictionaries** (`Dictionary.py`): `conv_factor = {}`, `conv_factor["Dollar"] = 60`, then `keys()`, `values()`, `items()`.
- **Monty Hall** (`monteHall.py`): an interactive version. The car is placed at random; the host opens a random "Fake" door that is not the player's; the program counts swap wins vs non-swap wins.
- **Rock-Paper-Scissors** (`RockPaperScissors.py`):
  - A `tkinter` GUI.
  - A nested-dict `schema[user][computer]` → 2 = win, 1 = draw, 0 = loss.
  - The computer picks with `random.randint(0, 2)`. The scores are module variables changed with `global`, and the buttons use `lambda`.
- **Binary search** (`BinarySearch.py`): recursive.
  - Base `start == end` → `end` if found else −1.
  - `mid = int((start+end)/2)`.
  - Go left if `l[mid] > x`, right if `l[mid] < x`.
  - It prints position + 1.
- **Bubble sort** (`BubbleSort.py`):
  - It counts swaps over `input().split()`. The items stay **strings**, so they compare as text (`'10' < '9'`), which is why the comment says it "doesn't sort completely".
  - The assignment version converts with `int()` first.
- **Substitution cipher** (`substitutionCipher.py`):
  - `dict[string.ascii_letters[i]] = string.ascii_letters[i-2]` maps each letter to the one 2 places back across `a…zA…Z`, so `a`→`Y`, `b`→`Z`, `A`→`y`.
  - It reads a file one character at a time (`f.read(1)`; `if not c:` = end of file) and writes the result.
- **Tic-Tac-Toe** (`TicTacToe.py`): a `pygame` GUI on a NumPy `zeros((3,3))` board. `check_win` tests columns, rows and both diagonals, and players alternate with `player % 2 + 1`.
- **Files** (`FileOperations.py`): `open(..., "r+")`: `read()` first, then `write()` adds the text at the current position, i.e. the end.
- **Tuples** (`Tuple.py`):
  - A collection separated by commas; immutable.
  - "Faster to access than lists".
  - `+`, `len`, `count`, `index` (first occurrence), and repetition `('python',)*3`.
- **`sorted`** (`Sorted_KeyWord.py`):
  - `sorted(tuple)` returns a **list**.
  - `sorted(dict)` returns the sorted **keys**.
  - `sorted(L, key=len)` sorts by length.
- **Snakes and ladders** (`Snakes&Ladder.py`):
  - A 30-square board with two players.
  - `check_ladder()` and `check_snake()` are `if/elif` chains (ladders 3→22, 5→8, 11→26, 20→29; snakes 17→4, 19→7, 21→9, 27→1).
  - The position is capped at 30. Typing `n` ends the game and compares the scores.
- **GPS map** (`Gmplot.py`):
  ```python
  from gmplot import gmplot
  gmap = gmplot.GoogleMapPlotter(lat, long, 17)
  ```
  It reads `LatLong.csv` with `csv.reader`; the first point gets a green marker, the rest blue and the last red; `gmap.draw("Myhouse.html")`.
- **Gambling** (`Gambling.py`): 365 days. Each day `bet` and `luck` are `randint(1,10)`; a match gives `+900-100`, otherwise `-100`. The balance is plotted.
- **Anagrams** (`Anagrams.py`): `sorted(l) == sorted(word)` over a list of words.
- **Image flip** (`ImageTransposing.py`): `img.transpose(Image.FLIP_LEFT_RIGHT)` fixes a mirrored receipt; the result is saved.
- **CLAHE** (`ImgEnhancing.py`):
  ```python
  img = cv2.imread(f)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  clahe = cv2.createCLAHE()
  enh = clahe.apply(gray)
  cv2.imwrite('enhanced.jpg', enh)
  ```
- **Image as a matrix** (`Making-an-Img.py`): `np.zeros([100,200,3], dtype=np.uint8)` (uint8 = unsigned 8-bit, 0–255). `array[:, :100] = [200,128,61]` is the left half orange. Then `Image.fromarray(array).save(...)`.
- **Colour picker** (`Colorpicker.py`): `im.convert('RGB').getpixel((x, y))` → `r, g, b`.
- **Area estimation** (`AreaCalculate.py`):
  - Random pixels `(randint(0,789), randint(0,899))` on an India map.
  - A red value of 254 counts as India and 238 as the state.
  - `area_state = (count_state / count_india) * 3287263` (India's area in km²).
- **Stylometry / graphs** (`GraphsEdgeNode.py`):
  - `G.add_nodes_from(l)`, `add_edge`, `nx.complete_graph(10)`, `nx.gnp_random_graph(20, 0.1)`.
  - **`nx.barabasi_albert_graph(15, 2)`**: each new node attaches 2 edges, preferring high-degree nodes.
  - `nx.write_gexf(G, "x.gexf")`.
- **NumPy** (`Numpy.py`):
  - `type(a)`, `a.shape`, item assignment `a[1] = 6`, `np.zeros((2,2))`, `np.ones((2,2))`.
  - **`np.full((2,2), 5)`**, **`np.random.random((2,2))`**.
  - `dtype=np.int64` / an automatic float64 (`.dtype`).
  - `h.T`, `np.sum(h)`, `axis=0`/`1`.
  - **`np.multiply`**, `np.subtract`, `np.add`, **`np.sqrt`**, and broadcasting `h - g`.
- **Compression** (`ImageCompressing.py`): `ig.new(img.mode, img.size)`, then the 0–31→0 … 224–255→7 quantisation over `img.load()` pixels, then save, then `np.asanyarray(Image.open(...))`.
- **FLAMES** (`F.L.A.M.E.S.py`):
  - `remove_matching_letter` returns `[list1 + ["*"] + list2, True/False]`; the caller splits at `"*"` again.
  - `counter = len(l1) + len(l2)`.
  - Labels: Friend, Loves, Affection, Marriage, Enemy, Sister.
  - Loop: `split_index = counter % len(result) - 1`; if it is positive, `result = right + left`, else drop the last element.
- **Browser automation** (`BrowserAutoWatsapp.py`):
  - `webdriver.Chrome(path)` and `driver.get("https://web.whatsapp.com/")`.
  - `wait = WebDriverWait(driver, 600)`, then `wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(@title,"NAME")]')))` and `.click()`.
  - `driver.find_element_by_class_name(...)`.
  - A loop of `input_box.send_keys(string + Keys.ENTER)` with `time.sleep(1)`.
- **Time zones / calendar** (`Timezones.py`):
  - `pytz.timezone('Asia/Bangkok')` and `dt.now(tz)`.
  - `calendar.weekday(y, m, d)` indexes a **Monday-first** list `["MONDAY", …, "SUNDAY"]` (the correct pairing).
  - The call is wrapped in `try: … except Exception as e: print(e)`.
- **PageRank, point distribution** (`HowDoesGoogleWork.py`):
  - A `DiGraph` of 10 nodes, with each ordered pair linked when `random() < 0.5`.
  - Every node starts with **100** points.
  - Each round, a node splits its points equally over `G.out_edges(n)`; **a node with no out-edges keeps its own points**.
  - The rounds repeat until the user types `#`.
  - The ranking is `sorted(d.items(), key=lambda f: f[1])`, and the result is compared with `nx.pagerank(G)`.
- **PageRank, random walk** (`RandomWalkOnGraph.py`):
  - `nx.gnp_random_graph(10, 0.5, directed=True)`.
  - Start at a random node and walk 10,000 steps along `G.neighbors(x)`. With no neighbours (a sink), jump to a random node.
  - Visits are counted in a dict, sorted with `operator.itemgetter(1)` and compared with `nx.pagerank`.
  - `G.number_of_nodes()` gives the node count.
- **Reading a directed edge list** (`Pager.ipynb`): `nx.read_edgelist("page_rank.txt", create_using=nx.DiGraph, nodetype=str)`.
- **Collatz** (`CollatzConjecture.py`): `count = 1`, then `n = int(n/2)` or `3n+1` until 1, so it counts the numbers in the sequence, including the start.
- **Other lecture helpers**:
  - The k-th max plus k-th min (`KmaxKmin.py`).
  - A Fibonacci list builder (`FibonacciRecur.py`).

### 7.4 Programming-assignment patterns (code you may be asked to trace)

Reading input:
- `a, b = map(int, input().split())`.
- `[int(x) for x in input().split()]`.
- `input().split(',')` then `item.split(':')` for `key:value` pairs.
- Reading an n×n matrix row by row.
- `print(*lst)` prints the items separated by spaces.
- `' '.join(str(e) for e in lst)`.

List tasks:
- Remove numbers ending in 4 (`str.endswith("4")`).
- Remove duplicates keeping order (`if i not in res: res.append(i)`).
- Second largest + second smallest (watch for equal largest values).
- k-th largest `lst[-k]`, k-th smallest `lst[k-1]`, and distinct versions via dedupe.
- The first element occurring k times (counting dict, then a second pass in order).
- Running (prefix) sums.
- Odd-index elements `L[1:n:2]`.
- The three smallest `L[0:3]`, and the two largest reversed `L[-2:][::-1]`.
- Elements appearing exactly twice.
- The first prime in a list.
- Unique elements, sorted.
- Zeros moved to the end, keeping order.
- Rank of the k-th element `sorted(L).index(L[K-1]) + 1`.
- Fill a list so each value sits at its own index (`IL[v] = v`, zeros elsewhere).

Number tasks:
- GCD by trying 1…min(a, b).
- Factorial (`math.factorial`).
- Count multiples of 3 or 5.
- Pythagorean triple: sort and test `x² + y² == z²`, or `max` then `remove`.
- `((10**i - 1)//9)**2` → 1, 121, 12321, … (palindromic squares of repunits).
- Square pattern `count*count`. Number pyramid `str(i)*i`.
- Right-aligned star triangle (spaces when `j <= n-i`).
- Arrangements of 0s and 1s = n!/(zeros!·ones!).
- Sum 0…N = `sum(range(N+1))`.
- Reverse a number `int("".join(list(s)[::-1]))` (leading zeros vanish).
- Ways to write an even n as a sum of even numbers = 2^(n/2 − 1), using fast modular power with `y & 1` and `y >> 1`, mod `1e9+7`.
- Binary strings without consecutive 1s (the `a[i] = a[i-1] + b[i-1]`, `b[i] = a[i-1]` recurrence).
- Minimum moves to make all values equal: −1 if the sum is not divisible by n, else the sum of the shortfalls below the average.
- Minimum deletions from the ends to remove both the min and the max.

String tasks:
- Anagram check ignoring case and non-alphanumerics (`sorted(s.upper())` filtered by `isalnum`).
- Pangram check: every a–z present, via a `for … else` or a 26-flag list.
- Remove vowels (`anti_vowel` with `replace`).
- Remove punctuation (a punctuation string, or keep `isalnum()` plus spaces).
- Palindrome ignoring non-alphanumerics and case.
- Reverse Caesar decode with a shift of 3 (`(ord(c) - ord('A') - 3) % 26`), then reverse the string.
- Caesar +5 and an anagram check of the cipher (also the 2021 online test: `chr((ord(c)+5-ord('A')) % 26 + ord('A'))` and compare `sorted`).
- `swapcase()`.
- Replace consonants with `_` (vowel string includes the space).
- Replace runs of 3 vowels with `_`.
- Sort words by their reversed spelling.
- Split an email: `roll.split('@')[0]`, `.split('@')[1].split('.')[0]`.
- Sorted unique comma-separated words: `",".join(sorted(set(words)))`.
- Sort `#`-separated words in reverse.
- Does a large string use exactly the letters of the small strings (set equality plus equal length)?
- Longest palindrome that can be built from a string's letters (pairs plus one odd middle).
- Digit positions: each distinct digit followed by the indexes where it occurs.
- Run-length encoding, e.g. `aaabb` → `(3,a)(2,b)` with `"({},{})".format(len(n), n[0])` (2021-jul online test).
- Word-wrap text to width w with `textwrap.TextWrapper(width=w).wrap(text)` (2021-jul online test).

Matrix tasks:
- Is it a binary matrix (only 0/1; uses `sys.exit()` or a flag)?
- Is it symmetric (`l[i][j] == l[j][i]`, or `zip(*l)` transpose == l)?
- Print the lower-triangular part (0 where `i < j`).
- Fill an r×c matrix 1…r·c.
- An `R*row + col` table via a nested generator inside `'\n'.join`.
- Diagonal sums (main via `i == j`, anti via the reversed rows `L[::-1]`).
- Transpose via `numpy.array(M).transpose().tolist()`.
- Snake order (reverse every second row).
- A row or column with exactly two 1s (found by slicing a flat input into rows of size a).

Tuple / dict tasks:
- `squareT(t)` = t + a tuple of squares.
- `count_letters` dict.
- `mergeDic` that keeps d1's values.
- Count snakes vs ladders from `start:end` pairs (end > start = ladder).
- Play a snakes-and-ladders game from the dice list and report whether the total reaches ≥ 100.

Geometry and maths:
- Volume of a parallelepiped from 3 vectors = `abs(np.linalg.det(arr))`, formatted with `"{0:.1f}".format(v)`.
- An angle via `math.asin`, `math.degrees` and `round`.
- Closest school by Euclidean distance `((x-a)**2 + (y-b)**2)**0.5`.
- Count the questions where two exam answer keys disagree.

Syntax seen here:
- `print("Yes") if k == l else print("No")` (a conditional expression used as a statement).
- `[res.append(x) for x in new if x not in res]` (a comprehension used for its side effect).
- `from array import *`.
- `string.lower()` where `string` was never defined: a NameError bug in one online-test solution.


### 7.5 Current session (2026-jul) programming assignments

Source: the solution PDFs in `JyRaGa/NPTELWhisperer/solution pdfs/` (weeks 4–8 and 10–12; there are no files for weeks 1–3 or 9). Their MCQ answers match the 2026-jul cards covered in Parts 3–5.

- **Week 4: Max–min temperature difference.** `a = [int(x) for x in input().split()]`; `max(a) - min(a)`, or 0 for empty input; `print(..., end='')` (no trailing newline)
- **Week 4: Prime checker.** `a < 2` → False; otherwise test divisors `range(2, int(a ** 0.5) + 1)` and `break` at the first one
- **Week 4: Duplicate product IDs.** `len(items) != len(set(items))`: a set drops duplicates, so a shorter set means a repeat
- **Week 5: Smallest number with the highest frequency.** Count with `freq[num] = freq.get(num, 0) + 1`; `max(freq.values())`; candidates `[n for n, c in freq.items() if c == max_freq]`; `min(candidates)`
- **Week 5: First duplicate elements in order.** Two sets, `seen` and `added`: a number already in `seen` and not yet in `added` is appended once. Print `-1` if none, else `print(*result)`
- **Week 5: Elements appearing exactly twice.** The same frequency dict, keep `count == 2`, `sort()`, `-1` if none
- **Week 6: Count letters recursively.** `if not s: return 0`; `return (1 if s[0].isalpha() else 0) + count_alpha(s[1:])`
- **Week 6: List length recursively (no `len`).** `if not lst: return 0`; `return 1 + count_boxes(lst[1:])`
- **Week 6: Maximum recursively (no `max`).** Base `len(temps) == 1` → `temps[0]`; else compare `temps[0]` with `find_max(temps[1:])`
- **Week 7: Attraction ratings directory.** Each line splits into words: name = `" ".join(line[:-1])`, rating = `line[-1]`; answer with `attractions.get(target, -1)`
- **Week 7: Landmark linear search.** `landmarks.index(target)` inside `try`, and `except ValueError: print(-1)`
- **Week 7: Second highest value.** `arr.sort()`; `arr[-2]`
- **Week 8: Elevator floor tracker.** `sum(map(int, input().split()))`
- **Week 8: Online quiz scoring.** `score += 10 if int(x) == 1 else -2` (a conditional expression inside `+=`)
- **Week 8: Employee ID pattern match (isomorphic strings).** Equal lengths and `len(set(s1)) == len(set(s2)) == len(set(zip(s1, s2)))`: the number of distinct characters on each side equals the number of distinct pairs only for a one-to-one mapping
- **Week 10: Treasure-hunt elimination (Josephus).** `explorers = list(range(1, n+1))`; `idx = (idx + k - 1) % len(explorers)`; `explorers.pop(idx)` until one is left
- **Week 10: Temperature sensor grouping (quantisation).** Keep readings in 0–255; group = `value // 32` (0–7); print the sum of the groups
- **Week 10: Warehouse product-code matching (FLAMES count).** `a, b = [list(x) for x in input().split()]`; for each `ch` in a copy `a[:]`, if `ch in b`, remove it once from both; answer `len(a) + len(b)`. Looping over the copy `a[:]` is what makes removal during the loop safe
- **Week 11: Review word count.** `search, *reviews = input().split()` (star unpacking: the first word, then the rest as a list); `reviews.count(search)`
- **Week 11: Hotel stay duration.** `datetime.strptime(x, '%Y-%m-%d')` parses a date string; `abs((d2 - d1).days)`
- **Week 11: Sundays in a month.** `sum(1 for week in calendar.monthcalendar(y, m) if week[6] != 0)` (index 6 = Sunday, 0 = a padding day)
- **Week 12: PageRank transfer (A → B only).** A gives all its rank to B: prints `0, rank_a + rank_b`
- **Week 12: Mutual PageRank exchange (A ↔ B).** Each gives its rank to the other, so the ranks swap: `rank_b, rank_a`
- **Week 12: Three-page PageRank update.** A splits its rank between B and C, B passes all of its rank to C, and C keeps its own (no out-link): prints `0, rank_a // 2, rank_a // 2 + rank_b + rank_c`

New Python facts from these:
- `dict.get(key, default)` as a counter.
- `print(*list)` prints the items separated by spaces.
- Star unpacking `first, *rest = seq`.
- `datetime.strptime(text, format)` is the inverse of `strftime`: it parses a string into a datetime.
- `zip(s1, s2)` pairs characters position by position, and a `set` of those pairs counts the distinct mappings.
- `try/except ValueError` around `list.index`.
- Iterating over a copy `a[:]` while removing from `a`.

---

## Part 8 — Exam-day sheet: numbers, formulas and conventions

This collects in one place the values the exam reuses with changed data. Nothing here replaces the full sections; use the Contents links above to find the details for any line.

### Boundaries: included or excluded?

- `range(a, b)`, `randrange(a, b)`, slices `s[a:b]`, `np.random.randint(a, b)`: **b excluded**.
- `random.randint(a, b)`, Scratch `pick random a to b`: **both included**.
- `calendar.leapdays(y1, y2)`: y1 included, **y2 excluded**.
- Slice defaults: start 0, end len. `s[::-1]` reverses. `L[-1]` is the last item.
- A random float: `random.random()` and `np.random.rand()` give [0, 1).

### Index conventions

- `calendar.weekday()`, `date.weekday()`: **Monday = 0** … Sunday = 6.
- `date.isoweekday()`: Monday = 1 … Sunday = 7.
- `strftime('%w')`: **Sunday = 0**.
- `calendar.monthcalendar()` rows: index 0 = Monday … 4 = Friday, 5 = Saturday, 6 = Sunday; 0 = a day outside the month.
- `calendar.monthrange(y, m)` → (weekday of the 1st, number of days).
- `shortest_path_length(G, source, target)`: 2nd argument = source.
- `GoogleMapPlotter(lat, lng, zoom)`.
- `barbell_graph(m1, m2)`: m1 per clique, m2 in the path.
- `gnp_random_graph(n, p)`: n nodes, edge probability p.
- `np.sum(a, axis=0)`: column sums; `axis=1`: row sums.
- `im.size`: (width, height). `pixels[x, y]`: x = column, y = row.

### Formulas

| Topic | Formula / value |
|---|---|
| Sum 1…n | n(n+1)/2 (10 → 55) |
| Sum of the first n odd numbers | n² (10 → 100, 27 → 729) |
| Magic constant | n(n²+1)/2: 3 → 15, 4 → 34, 5 → 65, 6 → 111, 7 → 175, 8 → 260, 11 → 671; Ramanujan's square = 139 |
| Pigeonhole (guarantee 2 share) | k categories → k + 1 (months 13, weekdays 8, days 366, 48 half-hours → 49) |
| Pigeonhole (guarantee 3 share) | 2k + 1 (48 half-hours → 97) |
| Birthday paradox | ≈ 50% at 23 people; ≈ 90% near 40 |
| Jumbled word with n distinct letters | n! − 1 ways to pose it |
| Movie titles of length L | 26^L (3 → 17576) |
| Dobble comparisons | k × k (8 vs 10 symbols → 80) |
| Monty Hall (3 doors) | switch 2/3, stay 1/3 |
| Rock-Paper-Scissors | 9 combinations, 3 draws |
| Linear search | worst n, average successful (n+1)/2 |
| Binary search | about log₂ n; usual code worst case ⌊log₂ n⌋ + 1 (256 → 9, 1024 → 11); the cards also accept 1000/1024 → 10 |
| Bubble sort | n − 1 passes, n − 1 comparisons per pass, swaps = inversions |
| Tic-Tac-Toe | 8 winning lines; the centre is on 4, a corner on 3, an edge on 2 |
| Caesar cipher | at most 26 tries |
| Turtle polygon | turn 360/n: triangle 120°, square 90°, hexagon 60°, octagon 45°; star 144° |
| Scratch full rotation | repeats × turn = 360 (turn 30 → 12, turn 18 → 20) |
| Complete graph | n(n−1)/2 edges, each degree n − 1 |
| Degrees | sum of degrees = 2 × edges (always even) |
| Degree of separation | average shortest path length: complete graph → 1, path of 6 → 2.333, ring of 9 → 2.5 |
| Area estimation | (points in region ÷ reference points) × reference area (the lecture divides by the rest-of-country points) |
| Expected value of a bet | P(win) × prize − cost (1/10 × 500 − 100 = −50) |
| Josephus | J(1) = 1, J(n) = (J(n−1) + k − 1) % n + 1 (25, 3 → 14) |
| Collatz | even → n/2, odd → 3n+1; steps 5 → 5, 6 → 8, 7 → 16, 8 → 3, 9 → 19, 75 → 14 (the lecture counts the numbers, +1) |
| Leap year | divisible by 4 and not by 100, or by 400 (1900 no, 2000 yes, 2100 no) |
| Quantisation | value // 32 → 0–7 (31 → 0, 223 → 6) |
| Pixel average | (r + g + b) // 3; `> 127` = bright, so 127 is dark |
| VADER compound / TextBlob polarity | −1 … +1 |

### Character codes and modules

- `ord('A')` = 65, `ord('a')` = 97, the case gap = 32, `ord('f')` = 102. Sort order: space < `!` < digits < UPPER < lower.
- `string.ascii_letters` = 52 letters (a–z then A–Z); `ascii_lowercase`, `ascii_uppercase`, `digits`.
- Libraries by job:
  - Graphs: `matplotlib.pyplot`. Maps: `gmplot`. Images: `PIL` (Pillow); CLAHE: `cv2`.
  - Text: `nltk` (VADER inside it), `textblob`. Networks: `networkx`; visual tool: Gephi.
  - Browser: `selenium`. Dates: `datetime`, `calendar`; zones: `pytz`. Speech: `speech_recognition` (WAV/AIFF/FLAC).
  - Arrays: `numpy`. Trimmed mean: `scipy.stats.trim_mean`.
  - Animation / drawing: `turtle`. Copies: `copy.deepcopy`. Sorting key: `operator.itemgetter`.

### Full forms

- NLTK = Natural Language Toolkit.
- VADER = Valence Aware Dictionary and sEntiment Reasoner.
- PIL = Python Imaging Library.
- CSV = comma-separated values.
- CLAHE = Contrast Limited Adaptive Histogram Equalisation.
- FLAMES = Friends, Love, Affection, Marriage, Enemies, Siblings.
- WAV = Waveform Audio File Format.
- Scratch files: `.sb`. Python files: `.py`.

---

## Part 9 — Self-test drill

Cover the answer, predict it, then open it. Every answer below was produced by running the code (Python 3), so it is exact.

**1. (Week 2) What is printed?**

```python
print('new' 'line')
```

<details><summary>Answer</summary>

```text
newline
```

Adjacent string literals are joined before anything runs.

</details>

**2. (Week 2) The user types 5. What is printed?**

```python
c = '5'  # what input() returns
print(c * 3)
```

<details><summary>Answer</summary>

```text
555
```

input() gives a string; str * int repeats it.

</details>

**3. (Week 2) What is printed?**

```python
print(17 % -5, -17 % 5)
```

<details><summary>Answer</summary>

```text
-3 3
```

% takes the sign of the divisor.

</details>

**4. (Week 2) What is printed?**

```python
print(-7 // 2, 7 // -2)
```

<details><summary>Answer</summary>

```text
-4 -4
```

// rounds down (towards minus infinity), not towards zero.

</details>

**5. (Week 2) What is printed?**

```python
print(3 * 1 ** 3, 2 ** 3 ** 2)
```

<details><summary>Answer</summary>

```text
3 512
```

`**` binds tighter than `*`, and `**` groups right to left: `2 ** 3 ** 2` is `2 ** 9`.

</details>

**6. (Week 2) What is printed?**

```python
print(int(3.79) + int(-2.9))
```

<details><summary>Answer</summary>

```text
1
```

int() cuts the decimals off towards zero: 3 + (-2).

</details>

**7. (Week 2) What happens?**

```python
x = 'a'
print(x + 1)
```

<details><summary>Answer</summary>

```text
TypeError: can only concatenate str (not "int") to str
```

A string and an int cannot be added.

</details>

**8. (Week 2) What is printed?**

```python
print(bool('False'), bool(0), bool([]), bool(' '))
```

<details><summary>Answer</summary>

```text
True False False True
```

Any non-empty string is truthy, even 'False' and ' '.

</details>

**9. (Week 2) What is printed?**

```python
for i in range(5, -1, -2):
    print(i, end=' ')
```

<details><summary>Answer</summary>

```text
5 3 1 
```

range stops before -1, stepping by -2.

</details>

**10. (Week 2) What is printed?**

```python
print(list(range(10, 0, -3)))
```

<details><summary>Answer</summary>

```text
[10, 7, 4, 1]
```

The stop value 0 is never reached.

</details>

**11. (Week 2) What is printed?**

```python
for i in range(3):
    if i == 5:
        break
else:
    print('done')
```

<details><summary>Answer</summary>

```text
done
```

The loop's else runs because no break happened.

</details>

**12. (Week 3) What is printed?**

```python
L = [1, 2, 3, 4]
L.append([5, 6])
print(len(L), L[-1])
```

<details><summary>Answer</summary>

```text
5 [5, 6]
```

append adds the whole list as one item.

</details>

**13. (Week 3) What is printed?**

```python
L = [1, 2, 3, 4, 5]
L.insert(-2, 99)
print(L)
```

<details><summary>Answer</summary>

```text
[1, 2, 3, 99, 4, 5]
```

A negative index in insert puts the item before that position from the end.

</details>

**14. (Week 3) What is printed?**

```python
L = [3, 1, 2]
print(L.sort(), L)
```

<details><summary>Answer</summary>

```text
None [1, 2, 3]
```

sort() works in place and returns None.

</details>

**15. (Week 3) What is printed?**

```python
print(sorted('Hi! a'))
```

<details><summary>Answer</summary>

```text
[' ', '!', 'H', 'a', 'i']
```

Sorted by character code: space, !, capitals, then small letters.

</details>

**16. (Week 3) Which values can this return?**

```python
# the values random.randrange(1, 10, 3) can return:
print(list(range(1, 10, 3)))
```

<details><summary>Answer</summary>

```text
[1, 4, 7]
```

randrange follows range: the stop value is excluded.

</details>

**17. (Week 3) What is printed?**

```python
s = 'abcdef'
print(s[-2:], s[:-2], s[::-2])
```

<details><summary>Answer</summary>

```text
ef abcd fdb
```

Negative indexes count from the end; a step of -2 goes backwards.

</details>

**18. (Week 4) What is printed?**

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

<details><summary>Answer</summary>

```text
[1, 2, 3, 4]
```

b = a makes two names for one list.

</details>

**19. (Week 4) What is printed?**

```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][1] = 99
b[1] = [0, 0]
print(a)
```

<details><summary>Answer</summary>

```text
[[1, 99], [3, 4]]
```

A shallow copy shares the inner lists, but replacing b[1] does not touch a.

</details>

**20. (Week 4) What is the magic constant of an 8 x 8 magic square?**

```python
n = 8
print(n * (n * n + 1) // 2)
```

<details><summary>Answer</summary>

```text
260
```

n(n^2 + 1)/2.

</details>

**21. (Week 4) Minimum people to guarantee 3 share a weekday?**

```python
k = 7
print(2 * k + 1)
```

<details><summary>Answer</summary>

```text
15
```

Pigeonhole: 2 per weekday fits 14 people; the 15th makes 3.

</details>

**22. (Week 4) How many leap years are in [2000, 2024), and is 1900 a leap year?**

```python
import calendar
print(calendar.leapdays(2000, 2024))
print(calendar.isleap(1900))
```

<details><summary>Answer</summary>

```text
6
False
```

leapdays excludes the end year; 1900 is divisible by 100 but not 400.

</details>

**23. (Week 5) What is printed?**

```python
d = {1: 'a', 1.0: 'b', True: 'c'}
print(d)
```

<details><summary>Answer</summary>

```text
{1: 'c'}
```

1, 1.0 and True are the same key; the first key object stays, the last value wins.

</details>

**24. (Week 5) What is printed?**

```python
def f(x, L=[]):
    L.append(x)
    return L
f(1)
print(f(2))
```

<details><summary>Answer</summary>

```text
[1, 2]
```

The default list is created once and shared between calls.

</details>

**25. (Week 5) What is printed?**

```python
def f():
    pass
print(f())
```

<details><summary>Answer</summary>

```text
None
```

A function with no return gives None.

</details>

**26. (Week 5) Bubble sort: how many swaps to sort [4, 3, 1, 2]?**

```python
a = [4, 3, 1, 2]
pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
print(sum(1 for i, j in pairs if a[i] > a[j]))
```

<details><summary>Answer</summary>

```text
5
```

Swaps = number of out-of-order pairs (inversions).

</details>

**27. (Week 5) Worst-case comparisons of binary search on 100 sorted items?**

```python
import math
print(math.floor(math.log2(100)) + 1)
```

<details><summary>Answer</summary>

```text
7
```

floor(log2 n) + 1 checks with the usual code.

</details>

**28. (Week 6) What is printed?**

```python
def r(n):
    if n == 0:
        return 0
    return n % 10 + r(n // 10)
print(r(4096))
```

<details><summary>Answer</summary>

```text
19
```

It adds the digits recursively.

</details>

**29. (Week 6) Caesar shift +3: what is 'XYZ'?**

```python
print(''.join(chr((ord(c) - 65 + 3) % 26 + 65) for c in 'XYZ'))
```

<details><summary>Answer</summary>

```text
ABC
```

% 26 wraps past Z.

</details>

**30. (Week 7) What is printed?**

```python
print(len({1, 2, 2, 3}), type(('a')).__name__, type(('a',)).__name__)
```

<details><summary>Answer</summary>

```text
3 str tuple
```

A set drops duplicates; ('a') is just a string; ('a',) is a tuple.

</details>

**31. (Week 8) What happens?**

```python
t = ('a', 'b')
print(t + ('c'))
```

<details><summary>Answer</summary>

```text
TypeError: can only concatenate tuple (not "str") to tuple
```

('c') is a string, so a tuple cannot be joined with it.

</details>

**32. (Week 8) What is printed?**

```python
t = (1, 2, [3])
t[2].append(4)
print(t)
```

<details><summary>Answer</summary>

```text
(1, 2, [3, 4])
```

The tuple cannot change, but the list inside it can.

</details>

**33. (Week 8) What is printed?**

```python
print(sorted('listen') == sorted('silent'))
print(sum(map(ord, 'ad')) == sum(map(ord, 'bc')))
```

<details><summary>Answer</summary>

```text
True
True
```

Sorted letters decide anagrams; equal ASCII sums do not.

</details>

**34. (Week 9) Degree of separation of a path of 5 nodes?**

```python
n = 5
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
print(sum(j - i for i, j in pairs) / len(pairs))
```

<details><summary>Answer</summary>

```text
2.0
```

Average shortest path over all 10 pairs.

</details>

**35. (Week 9) Edges in a complete graph of 7 nodes, and nodes in star_graph(5)?**

```python
n = 7
print(n * (n - 1) // 2, 5 + 1)
```

<details><summary>Answer</summary>

```text
21 6
```

n(n-1)/2; star_graph(n) has a centre plus n leaves.

</details>

**36. (Week 10) What happens?**

```python
s = 'hello'
print(s.find('z'))
print(s.index('z'))
```

<details><summary>Answer</summary>

```text
-1
ValueError: substring not found
```

find returns -1; index raises an error.

</details>

**37. (Week 10) What is printed?**

```python
s = 'hello'
s.replace('l', 'L')
print(s)
```

<details><summary>Answer</summary>

```text
hello
```

Strings are immutable; the result was not assigned.

</details>

**38. (Week 10) What is printed?**

```python
print('#'.join('JOC'), '-'.join(['a', '', 'b']))
```

<details><summary>Answer</summary>

```text
J#O#C a--b
```

join puts the separator between items only.

</details>

**39. (Week 10) What is printed?**

```python
import numpy as np
a = np.array([[1, 2], [3, 4]])
print(np.sum(a, axis=0), np.sum(a, axis=1), a.shape)
```

<details><summary>Answer</summary>

```text
[4 6] [3 7] (2, 2)
```

axis=0 adds down the columns, axis=1 across the rows.

</details>

**40. (Week 10) What is the shape?**

```python
import numpy as np
print((np.array([1, 2, 3]) * np.array([[1], [2]])).shape)
```

<details><summary>Answer</summary>

```text
(2, 3)
```

Broadcasting (3,) with (2,1) gives (2,3).

</details>

**41. (Week 10) Josephus: 7 people, every 3rd eliminated. Who survives?**

```python
people = list(range(1, 8)); i = 0
while len(people) > 1:
    i = (i + 3 - 1) % len(people)
    people.pop(i)
print(people[0])
```

<details><summary>Answer</summary>

```text
4
```

The same counting-out loop as FLAMES.

</details>

**42. (Week 11) What is printed?**

```python
import calendar, datetime
print(calendar.weekday(2024, 1, 1))
print(datetime.date(2024, 1, 1).isoweekday())
```

<details><summary>Answer</summary>

```text
0
1
```

1 Jan 2024 was a Monday: weekday() counts from 0, isoweekday() from 1.

</details>

**43. (Week 11) What is printed?**

```python
import datetime
feb1 = datetime.date(2024, 2, 1)
print((datetime.date(2024, 3, 1) - feb1).days)
print(feb1.strftime('%j'))
```

<details><summary>Answer</summary>

```text
29
032
```

2024 is a leap year; %j is the day of the year.

</details>

**44. (Week 11) What is printed?**

```python
import calendar
print(calendar.monthrange(2023, 2))
```

<details><summary>Answer</summary>

```text
(calendar.WEDNESDAY, 28)
```

(weekday of the 1st, number of days); 1 Feb 2023 was a Wednesday. Python 3.12+ shows the weekday as calendar.WEDNESDAY, which equals 2; older versions print (2, 28).

</details>

**45. (Week 12) Collatz: how many steps does 6 take to reach 1?**

```python
n, steps = 6, 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps += 1
print(steps)
```

<details><summary>Answer</summary>

```text
8
```

6, 3, 10, 5, 16, 8, 4, 2, 1. The lecture version (count starts at 1) would say 9.

</details>

**46. (Week 12) One point-distribution round. A links to B and C, B links to C, C links to A. Each page starts with 1.0. New ranks?**

```python
links = {'A': ['B', 'C'], 'B': ['C'], 'C': ['A']}
rank = {p: 1.0 for p in links}
new = {p: 0.0 for p in links}
for p, outs in links.items():
    for q in outs:
        new[q] += rank[p] / len(outs)
print(new)
```

<details><summary>Answer</summary>

```text
{'A': 1.0, 'B': 0.5, 'C': 1.5}
```

Each page splits its rank equally over its out-links; the total stays 3.0.

</details>

---

## Part 10 — Examiner's oddities

Corner cases that examiners like because the intuitive answer is wrong. Every answer was produced by running the code (Python 3). Questions using `random` show what the outputs can be, not one fixed run.

**E1. (Floats) What is printed?**

```python
print(0.1 + 0.2 == 0.3)
print(sum([0.1] * 10) == 1.0)
```

<details><summary>Answer</summary>

```text
False
True
```

Decimal fractions are stored in binary, so 0.1 + 0.2 is 0.30000000000000004. Never compare floats with `==`.

</details>

**E2. (Rounding) What is printed?**

```python
print(round(2.5), round(3.5), round(-0.5))
```

<details><summary>Answer</summary>

```text
2 4 0
```

`round` uses banker's rounding: halves go to the nearest **even** number.

</details>

**E3. (Precedence) What is printed?**

```python
print(-2 ** 2)
print((-2) ** 2)
print(2 ** -1)
```

<details><summary>Answer</summary>

```text
-4
4
0.5
```

`**` binds tighter than unary minus, so `-2 ** 2` is `-(2 ** 2)`. A negative power gives a float.

</details>

**E4. (Precedence) What is printed?**

```python
print(7 // 2 * 2 + 7 % 2)
print(10 - 2 - 3, 2 ** 2 ** 3)
```

<details><summary>Answer</summary>

```text
7
5 256
```

`//`, `*` and `%` run left to right before `+`. `-` groups left to right, `**` right to left (2 ** 8).

</details>

**E5. (Booleans) What is printed?**

```python
print(True + True, True * 10, False - 1)
```

<details><summary>Answer</summary>

```text
2 10 -1
```

`True` is 1 and `False` is 0 in arithmetic.

</details>

**E6. (Booleans) What is printed?**

```python
print(3 or 0, 0 or [], [] and 7, not 0 and 5)
```

<details><summary>Answer</summary>

```text
3 [] [] 5
```

`or` returns the first truthy operand (or the last one); `and` returns the first falsy operand (or the last one). They return operands, not `True`/`False`.

</details>

**E7. (Booleans) What is printed?**

```python
print(bool('0'), bool(0.0), bool(' '), bool(None))
```

<details><summary>Answer</summary>

```text
True False True False
```

Only empty strings, zero numbers, empty containers and `None` are falsy. `'0'` and `' '` are non-empty strings.

</details>

**E8. (Comparisons) What is printed?**

```python
print(1 < 2 < 3, 3 > 2 > 1 == 1, 1 < 3 > 2)
```

<details><summary>Answer</summary>

```text
True True True
```

Comparisons chain: `a < b < c` means `a < b and b < c`.

</details>

**E9. (Comparisons) What is printed?**

```python
print(max('apple', 'Zebra'), min('10', '9'))
```

<details><summary>Answer</summary>

```text
apple 10
```

Strings compare character by character by code: lowercase `a` (97) beats `Z` (90), and `'1'` comes before `'9'`.

</details>

**E10. (Comparisons) What is printed?**

```python
print([] == [], [] is [], {1, 2} == {2, 1}, (1, 2) == (2, 1))
```

<details><summary>Answer</summary>

```text
True False True False
```

`==` compares values; `is` compares identity (two new lists are different objects). Sets ignore order; tuples do not.

</details>

**E11. (Division) What is printed?**

```python
print(10 / 5, type(10 / 5).__name__, divmod(17, 5))
```

<details><summary>Answer</summary>

```text
2.0 float (3, 2)
```

`/` always returns a float, even for exact division. `divmod(a, b)` gives `(a // b, a % b)`.

</details>

**E12. (Conversion) What is printed?**

```python
print(int('0010'), int('  7 '), int(-3.9), float('1e3'))
```

<details><summary>Answer</summary>

```text
10 7 -3 1000.0
```

`int` ignores leading zeros and surrounding spaces and truncates towards zero; `'1e3'` is 1000.0.

</details>

**E13. (Conversion) What happens?**

```python
print(int('3.5'))
```

<details><summary>Answer</summary>

```text
ValueError: invalid literal for int() with base 10: '3.5'
```

`int()` of a string must look like an integer; `int(float('3.5'))` would work.

</details>

**E14. (Strings) What is printed?**

```python
print('a' * 0 == '', len(''), 'abc'[10:] == '')
print('5' + '5', 5 + 5, '5' * 2)
```

<details><summary>Answer</summary>

```text
True 0 True
55 10 55
```

Repeating 0 times gives an empty string, and slicing past the end never errors (indexing would).

</details>

**E15. (Strings) What happens?**

```python
print('abc'[10])
```

<details><summary>Answer</summary>

```text
IndexError: string index out of range
```

Indexing past the end raises an error, unlike slicing.

</details>

**E16. (Strings) What is printed?**

```python
s = 'hello'
print(s.find('l'), s.rfind('l'), s.count('l'), s.find('z'))
```

<details><summary>Answer</summary>

```text
2 3 2 -1
```

`find` gives the first position, `rfind` the last, `count` the occurrences; a missing substring gives -1.

</details>

**E17. (Strings) What is printed?**

```python
print('Python'[-1:-4:-1], 'abc'[::-1][::-1])
print('a,b,,c'.split(','), len('hello  world'.split()))
```

<details><summary>Answer</summary>

```text
noh abc
['a', 'b', '', 'c'] 2
```

A negative step walks backwards. `split(',')` keeps empty pieces, but `split()` with no argument drops runs of spaces.

</details>

**E18. (Strings) What is printed?**

```python
print(chr(ord('a') + 25), ord('A') - ord('a'))
print(len(set('mississippi')))
```

<details><summary>Answer</summary>

```text
z -32
4
```

`z` is 25 letters after `a`; capitals are 32 below lowercase; mississippi has 4 distinct letters (m, i, s, p).

</details>

**E19. (Lists) What is printed?**

```python
x = [[0] * 2] * 2
x[0][0] = 1
print(x)
```

<details><summary>Answer</summary>

```text
[[1, 0], [1, 0]]
```

`* 2` on the outer list copies the **reference**, so both rows are the same list. Use `[[0] * 2 for _ in range(2)]`.

</details>

**E20. (Lists) What is printed?**

```python
a = b = []
a.append(1)
print(b)
c = [1, 2, 3]
c[1:1] = [9]
print(c)
```

<details><summary>Answer</summary>

```text
[1]
[1, 9, 2, 3]
```

`a = b = []` makes one list with two names. Assigning to an empty slice inserts without replacing.

</details>

**E21. (Lists) What is printed?**

```python
L = [1, 2, 3]
print(L * 2, [x * 2 for x in L])
print(list(range(5))[::-2])
```

<details><summary>Answer</summary>

```text
[1, 2, 3, 1, 2, 3] [2, 4, 6]
[4, 2, 0]
```

`*` on a list repeats it; use a comprehension (or NumPy) to multiply each element.

</details>

**E22. (Lists) What is printed?**

```python
L = [2, 4, 6, 8]
for x in L:
    if x % 2 == 0:
        L.remove(x)
print(L)
```

<details><summary>Answer</summary>

```text
[4, 8]
```

Removing shifts the later items left, so the item right after each removal is skipped (4 and 8 are never checked). Loop over a copy, `for x in L[:]`.

</details>

**E23. (Loops) What is printed?**

```python
for i in range(3):
    pass
print(i)
```

<details><summary>Answer</summary>

```text
2
```

The loop variable keeps its last value after the loop ends.

</details>

**E24. (Loops) What is printed?**

```python
i = 0
while i < 3:
    i += 1
else:
    print('else', i)
```

<details><summary>Answer</summary>

```text
else 3
```

A `while` loop's `else` runs when the condition becomes false (no `break`).

</details>

**E25. (Loops) What is printed?**

```python
for i in range(0):
    print('body')
else:
    print('else runs')
```

<details><summary>Answer</summary>

```text
else runs
```

A loop that runs zero times still runs its `else`.

</details>

**E26. (Functions) What is printed?**

```python
def f():
    return
def g():
    pass
print(f(), g())
```

<details><summary>Answer</summary>

```text
None None
```

A bare `return`, or no return at all, gives `None`.

</details>

**E27. (Functions) What is printed?**

```python
x = 5
def f():
    x = 10
f()
print(x)
```

<details><summary>Answer</summary>

```text
5
```

Assigning inside a function makes a new local `x`; the global is unchanged unless you write `global x`.

</details>

**E28. (Functions) What happens?**

```python
x = 5
def f():
    print(x)
    x = 10
f()
```

<details><summary>Answer</summary>

```text
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
```

Because `x` is assigned somewhere in `f`, Python treats it as local in the whole function, so reading it first fails.

</details>

**E29. (Dicts and sets) What happens?**

```python
d = {}
d[[1, 2]] = 'list key'
```

<details><summary>Answer</summary>

```text
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
```

A list is mutable, so it is unhashable and cannot be a dictionary key (a tuple can).

</details>

**E30. (Dicts and sets) What is printed?**

```python
print(type({}).__name__, type(set()).__name__, type({1}).__name__)
```

<details><summary>Answer</summary>

```text
dict set set
```

`{}` is an empty **dict**; an empty set must be written `set()`.

</details>

**E31. (Dicts and sets) What is printed?**

```python
d = {'a': 1, 'b': 2}
print(len(d), 'a' in d, 1 in d, list(d))
```

<details><summary>Answer</summary>

```text
2 True False ['a', 'b']
```

`len` and `in` work on the keys; `list(d)` gives the keys.

</details>

**E32. (Tuples) What is printed?**

```python
t = (1)
u = (1,)
v = ()
print(type(t).__name__, type(u).__name__, len(v))
```

<details><summary>Answer</summary>

```text
int tuple 0
```

The comma makes the tuple, not the brackets; `()` is the empty tuple.

</details>

**E33. (zip and unpacking) What is printed?**

```python
print(list(zip([1, 2, 3], 'ab')))
a, *b = [1, 2, 3]
print(a, b)
```

<details><summary>Answer</summary>

```text
[(1, 'a'), (2, 'b')]
1 [2, 3]
```

`zip` stops at the shorter input; star unpacking collects the rest into a list.

</details>

**E34. (NumPy) What is printed?**

```python
import numpy as np
print(np.array([1, 2, 3]) * 2)
print([1, 2, 3] * 2)
```

<details><summary>Answer</summary>

```text
[2 4 6]
[1, 2, 3, 1, 2, 3]
```

NumPy multiplies element-wise; a list repeats.

</details>

**E35. (NumPy) What is printed?**

```python
import numpy as np
a = np.array([1, 2, 3])
b = a
b[0] = 99
print(a, np.array([1, 2.5]).dtype)
```

<details><summary>Answer</summary>

```text
[99  2  3] float64
```

Assignment does not copy arrays either. One float makes the whole array float64.

</details>

**E36. (random) What is printed? (2000 draws, so every possible value shows up)**

```python
import random
vals = {random.randint(1, 3) for _ in range(2000)}
print(sorted(vals))
print(sorted({random.randrange(1, 3) for _ in range(2000)}))
```

<details><summary>Answer</summary>

```text
[1, 2, 3]
[1, 2]
```

`randint(1, 3)` includes 3; `randrange(1, 3)` never gives 3.

</details>

---

## Part 11 — ChatGPT-style questions

Plain concept MCQs in the style of the ChatGPT-converted 2023-jul cards (`@gpt`). Answers that can be checked by code were checked by running it.

**G1. Which of the following data types is mutable?**

- A. tuple
- B. str
- C. list
- D. frozenset

<details><summary>Answer</summary>

**C.** Lists can be changed in place; tuples, strings and frozensets cannot.

</details>

**G2. Which statement creates an empty set?**

- A. s = {}
- B. s = set()
- C. s = []
- D. s = ()

<details><summary>Answer</summary>

**B.** `{}` is an empty dictionary; only `set()` makes an empty set.

</details>

**G3. What is the data type of the value returned by `input()`?**

- A. int
- B. float
- C. str
- D. depends on what is typed

<details><summary>Answer</summary>

**C.** `input()` always returns a string; convert it with `int()` or `float()`.

</details>

**G4. Which method removes and returns the last element of a list?**

- A. remove()
- B. pop()
- C. del
- D. discard()

<details><summary>Answer</summary>

**B.** `pop()` with no index removes and returns the last item; `remove(x)` deletes by value and returns `None`.

</details>

**G5. What does `len()` return for a dictionary?**

- A. The number of values
- B. The number of keys
- C. The number of key-value characters
- D. An error

<details><summary>Answer</summary>

**B.** A dictionary's length is its number of keys (each key has one value).

</details>

**G6. Which keywords are used to handle exceptions in Python?**

- A. try / except
- B. catch / throw
- C. try / catch
- D. error / handle

<details><summary>Answer</summary>

**A.** Python uses `try` and `except` (plus optional `else` and `finally`).

</details>

**G7. What is the time complexity of binary search on a sorted list of n items?**

- A. O(1)
- B. O(log n)
- C. O(n)
- D. O(n²)

<details><summary>Answer</summary>

**B.** Each step halves the search range, so about log₂ n steps are needed.

</details>

**G8. What is the worst-case time complexity of bubble sort?**

- A. O(n)
- B. O(n log n)
- C. O(n²)
- D. O(log n)

<details><summary>Answer</summary>

**C.** In the worst case (reverse order) every pair is compared and swapped: about n²/2 operations.

</details>

**G9. Which sorting algorithm repeatedly compares and swaps adjacent elements?**

- A. Merge sort
- B. Quick sort
- C. Bubble sort
- D. Binary sort

<details><summary>Answer</summary>

**C.** Bubble sort compares neighbours and swaps them when they are out of order.

</details>

**G10. What does `random.random()` return?**

- A. An integer from 0 to 1
- B. A float in [0, 1)
- C. A float in [0, 1]
- D. A random element of a list

<details><summary>Answer</summary>

**B.** `random()` returns a float from 0 (inclusive) up to 1 (exclusive).

</details>

**G11. Which operator performs floor division?**

- A. /
- B. //
- C. %
- D. **

<details><summary>Answer</summary>

**B.** `//` divides and rounds down; `/` always gives a float.

</details>

**G12. What is the output of `print(type([]) == list)`?**

- A. True
- B. False
- C. list
- D. Error

<details><summary>Answer</summary>

**A.** `type([])` is the `list` class itself, so the comparison is `True`.

</details>

**G13. Which of these is NOT a valid variable name?**

- A. _count
- B. count2
- C. 2count
- D. Count

<details><summary>Answer</summary>

**C.** A name cannot start with a digit.

</details>

**G14. What is a base case in recursion?**

- A. The first call of the function
- B. A condition that stops further recursive calls
- C. The largest input
- D. A loop inside the function

<details><summary>Answer</summary>

**B.** The base case returns without calling the function again, which ends the recursion.

</details>

**G15. What does the `break` statement do?**

- A. Skips to the next iteration
- B. Exits the innermost loop
- C. Exits the program
- D. Pauses the loop

<details><summary>Answer</summary>

**B.** `break` leaves the innermost loop at once; `continue` skips to the next iteration.

</details>

**G16. What is the magic constant of a 3 × 3 magic square?**

- A. 12
- B. 15
- C. 18
- D. 45

<details><summary>Answer</summary>

**B.** n(n² + 1)/2 = 3 × 10 / 2 = 15.

</details>

**G17. In the Monty Hall problem, what is the probability of winning if you switch?**

- A. 1/3
- B. 1/2
- C. 2/3
- D. 1

<details><summary>Answer</summary>

**C.** Your first pick is wrong 2 times in 3, and switching then wins.

</details>

**G18. Which library is mainly used for natural language processing in this course?**

- A. NumPy
- B. NLTK
- C. Matplotlib
- D. Selenium

<details><summary>Answer</summary>

**B.** NLTK (Natural Language Toolkit) tokenises text, counts frequencies and includes VADER.

</details>

**G19. What does PIL stand for?**

- A. Python Image Loader
- B. Python Imaging Library
- C. Picture Import Library
- D. Pixel Image Language

<details><summary>Answer</summary>

**B.** PIL is the Python Imaging Library; Pillow is its maintained fork.

</details>

**G20. Which `datetime` call gives today's date only?**

- A. datetime.datetime.now()
- B. datetime.date.today()
- C. datetime.time()
- D. datetime.today.date

<details><summary>Answer</summary>

**B.** `date.today()` gives the date; `datetime.now()` includes the time.

</details>

**G21. What does `turtle.penup()` do?**

- A. Lifts the pen so the turtle moves without drawing
- B. Increases the pen width
- C. Moves the turtle up
- D. Changes the pen colour

<details><summary>Answer</summary>

**A.** After `penup()` the turtle moves without drawing until `pendown()`.

</details>

**G22. In a graph, what is the degree of a node?**

- A. The number of edges connected to it
- B. Its distance from the start
- C. Its PageRank
- D. Its label

<details><summary>Answer</summary>

**A.** The degree counts the edges at a node; the sum of all degrees is twice the number of edges.

</details>

**G23. What is the PageRank algorithm mainly used for?**

- A. Sorting numbers
- B. Ranking the importance of web pages
- C. Compressing images
- D. Encrypting messages

<details><summary>Answer</summary>

**B.** PageRank ranks pages by the importance of the pages that link to them.

</details>

**G24. What does Selenium automate?**

- A. Spreadsheets
- B. Web browsers
- C. Image editing
- D. Databases

<details><summary>Answer</summary>

**B.** Selenium WebDriver controls a browser from a program (testing, scraping, automation).

</details>

**G25. Which of the following is immutable?**

- A. list
- B. dict
- C. set
- D. tuple

<details><summary>Answer</summary>

**D.** A tuple cannot be changed after creation (its items cannot be reassigned).

</details>

**G26. What will `'Hello'[1:3]` return?**

- A. 'He'
- B. 'el'
- C. 'ell'
- D. 'llo'

<details><summary>Answer</summary>

**B.** The slice takes positions 1 and 2 (the end is excluded).

</details>

**G27. Which function converts a string `'42'` to an integer?**

- A. str()
- B. int()
- C. float()
- D. chr()

<details><summary>Answer</summary>

**B.** `int('42')` gives 42.

</details>

**G28. What does the `%` operator return?**

- A. The quotient
- B. The remainder
- C. A percentage
- D. The power

<details><summary>Answer</summary>

**B.** `a % b` is the remainder of `a` divided by `b`.

</details>

**G29. Which of these correctly opens a file for appending?**

- A. open('f.txt', 'r')
- B. open('f.txt', 'w')
- C. open('f.txt', 'a')
- D. open('f.txt', 'x')

<details><summary>Answer</summary>

**C.** `'a'` appends to the end and keeps old content; `'w'` erases the file first.

</details>

**G30. What is the output of `print(bool([]))`?**

- A. True
- B. False
- C. None
- D. Error

<details><summary>Answer</summary>

**B.** An empty list is falsy.

</details>
