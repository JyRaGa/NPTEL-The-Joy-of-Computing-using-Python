# Joy of Computing using Python: code from the picture cards

Companion to [Part 12 of the guidebook](GUIDEBOOK.md#part-12--what-only-the-website-shows). Every program and Scratch script that the site shows only as a picture is written out here, with its question, options and answer, so you do not need the website for them.

- Each transcription was checked against its image. Python that can run was run, and its output matches the card's stored answer.
- Scratch scripts are written block by block: `↻` turns clockwise (right), `↺` turns anticlockwise (left), blocks inside `repeat`, `forever` or `if` are indented, and `end` closes the block.
- Where the original picture is cut off or blurred, the code says so in a comment.
- Graph drawings, figures and plotted outputs (Part 12 groups B and C) are described in words where a card needs them.

## Contents

- [A. Scratch scripts](#a-scratch-scripts)
- [D. Program options](#d-program-options)
- [E1. Question code from screenshots](#e1-question-code-from-screenshots)
- [E2. 2026-jul case-study programs](#e2-2026-jul-case-study-programs)
- [E3. Code that was only in the page screenshots](#e3-code-that-was-only-in-the-page-screenshots)

---

## A. Scratch scripts

**`2018-jul/w01/q01@portal`** What should be the value of t so that the sprite shall complete one full rotation?

```text
repeat (t)
    turn ↻ (30) degrees
end
```

- **A.** 3
- **B.** 6
- **C.** 9
- **D.** 12

<details><summary>Answer</summary>

**D**. `repeat t` runs `turn 30 degrees` t times, so the total turn is 30 × t. A full rotation is 360°, so t = 360 ÷ 30 = `12`.

</details>

**`2020-jan/w01/q04`** When we double click the following instructions, the sprite (cat)

```text
set [t] to (10)
repeat (1)
    move (t) steps
    wait (1) secs
    move ((-1) * (t)) steps
end
```

- **A.** keeps moving forward
- **B.** moves forward in steps of 10
- **C.** moves backward 10 steps and then come back to its original position
- **D.** moves forward 10 steps and then come back to its original position

<details><summary>Answer</summary>

**D**. `t` is 10. The sprite moves 10 steps forward, waits a second, then moves −1 × 10 = −10 steps. Net movement is zero: it goes forward 10 and returns to where it started.

</details>

**`2020-jan/w01/q05`** Assuming our sprite to be an aeroplane now, the following instructions represent an aeroplane

```text
repeat (100)
    turn ↻ (15) degrees
    move (5) steps
end
```

- **A.** moving forward
- **B.** falling
- **C.** moving backward
- **D.** making circular motions

<details><summary>Answer</summary>

**D**. Each pass turns 15° and moves 5 steps, and it repeats 100 times. Moving a little and turning a little each time makes the sprite follow a circle, so the plane makes circular motions.

</details>

**`2020-jan/w01/q06`** Consider 2 blocks of instructions shown below for an aeroplane sprite. Choose the correct option from the following

```text
First block:                 Second block:
move (100) steps              move (100) steps
turn ↺ (15) degrees           turn ↻ (15) degrees
move (100) steps              move (100) steps
```

- **A.** First block represents landing while the second represents takeoff
- **B.** First block represents takeoff while the second represents landing
- **C.** Both the blocks represent takeoff
- **D.** Both the blocks represent landing

<details><summary>Answer</summary>

**B**. The plane faces right. Turning counter-clockwise 15° tilts its nose up before the second move, so the first block climbs (takeoff). Turning clockwise tilts it down, so the second block descends (landing).

</details>

**`2020-jan/w01/q08`** Imagine a ghost sprite. What does the following block of instructions represent

```text
point in direction (90)
turn ↺ (90) degrees
move (50) steps
wait (1) secs
turn ↻ (90) degrees
move (50) steps
wait (1) secs
turn ↻ (90) degrees
move (50) steps
```

- **A.** Ghost going vertically up and then down
- **B.** Ghost going backward and then forward
- **C.** Ghost going up, flying forward for some steps and then coming down
- **D.** None of the above

<details><summary>Answer</summary>

**C**. Direction 90 faces right. The ghost turns 90° counter-clockwise (faces up), moves 50 up, then turns 90° clockwise (faces right) and moves 50 forward, then turns clockwise again (faces down) and moves 50 down.

</details>

**`2020-sep/w01/q04`** Assume the sprite is a ball and predict the output of the following control structure. The ball glides to a random position in 1 second The ball glides to 10 random positions taking 1 second to reach each position The ball glides to a random position and waits there for 10 seconds The ball glides to 10 random positions within 1 second Accepted answer(s): The ball glides to 10 random positions taking 1 second to reach each position

```text
repeat (10)
    glide (1) secs to [random position]
end
```

- **A.** The ball glides to a random position in 1 second
- **B.** The ball glides to 10 random positions taking 1 second to reach each position
- **C.** The ball glides to a random position and waits there for 10 seconds
- **D.** The ball glides to 10 random positions within 1 second

<details><summary>Answer</summary>

**B**

</details>

**`2020-sep/w01/q06`** Predict the sequence of numbers that the sprite recites:

```text
set [num] to (1)
repeat (10)
    say (num) for (2) seconds
    change [num] by (2)
end
```

- **A.** 1, 2, 3, . . , 19
- **B.** 1, 3, 5, . . , 19
- **C.** 3, 5, 7, . . , 19
- **D.** 1, 2, 3, . . , 20

<details><summary>Answer</summary>

**B**. `num` starts at 1. Each pass says `num`, then adds 2, and the loop runs 10 times: 1, 3, 5, …, 19.

</details>

**`2020-sep/w01/q10`** Imagine a Magic wand sprite and predict the output for the following set of instructions.

```text
forever
    glide (1) secs to [random position]
    wait (0.25) seconds
end
```

- **A.** The Magic wand ﬂies to a random position takes 1 sec pause and then reaches another random position.
- **B.** The Magic wand ﬂies to a random position in 1 sec and after a 0.25 sec pause, it repeats the same until it is stopped.
- **C.** The Magic wand reaches all edges of the screen in a uniform pattern
- **D.** The Magic wand ﬂies between the top and bottom edges repeatedly.

<details><summary>Answer</summary>

**B**. `forever` repeats two blocks: glide for 1 second to a random position, then wait 0.25 seconds. So the wand flies to a random spot in 1 second, pauses 0.25 seconds, and repeats until stopped.

</details>

**`2021-jan/w01/q08@portal`** What one iteration of the  following block of instructions represent?

```text
repeat (10)
    move (-10) steps
    wait (1) secs
end
```

- **A.** Sprite going vertically up by 10 steps
- **B.** Sprite going backward by 10 steps
- **C.** Sprite going forward by 10
- **D.** Sprite remains in its place

<details><summary>Answer</summary>

**B**. Each pass moves −10 steps, which is 10 steps backwards, then waits 1 second. So one iteration sends the sprite backward by 10.

</details>

**`2021-jul/w01/q01`** What is the value of var after double clicking on the below block of code in scratch?

```text
set [var] to ((((5) + (5)) * (5)) / (10))
```

- **A.** 7.5
- **B.** 5
- **C.** 3
- **D.** 50

<details><summary>Answer</summary>

**B**. The blocks are `((5 + 5) * 5) / 10`. That is 10 × 5 = 50, then 50 ÷ 10 = `5`.

</details>

**`2021-jul/w01/q03`** How far will the sprite be from the initial position after executing this block of code?

```text
move (100) steps
wait (1) seconds
turn ↻ (90) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
```

- **A.** 141.42 steps
- **B.** 100 steps
- **C.** 10 steps
- **D.** 200 steps

<details><summary>Answer</summary>

**A**. The sprite moves 100 steps, turns 90°, then moves 100 steps again, so it ends at the far corner of a right angle. Its distance from the start is √(100² + 100²) = `141.42`.

</details>

**`2021-jul/w01/q07`** What will the sprite recite when the below block of code is executed?

```text
set [var] to (1)
repeat (100)
    say (var)
    wait (0.25) seconds
    change [var] by (2)
end
```

- **A.** All even numbers from 1 to 100
- **B.** All even numbers from 1 to 200
- **C.** All odd numbers from 1 to 100
- **D.** All odd numbers from 1 to 200

<details><summary>Answer</summary>

**D**. `var` starts at 1 and the loop runs 100 times, saying `var` and then adding 2. So it says 1, 3, 5, …, 199: all odd numbers from 1 to 200.

</details>

**`2021-jul/w01/q10`** When will the sprite stop moving when this block of code is executed ?

```text
forever
    move (100) steps
    wait (1) seconds
    turn ↻ (90) degrees
    wait (1) seconds
end
```

- **A.** Never
- **B.** It will stop after a while
- **C.** It will stop after 100 rounds
- **D.** None of the above

<details><summary>Answer</summary>

**A**. `forever` never ends by itself. It keeps repeating move 100, wait, turn 90, wait, so the sprite runs around a square until the user presses stop.

</details>

**`2022-jan/w01/q01`** Which of the following set of instructions will make the sprite(the cat) move in a triangle? ( Final and initial position, as well as the angle of the cat, should be the same)

- **A.**

  ```text
  turn ↺ (60) degrees
wait (1) seconds
move (200) steps
wait (1) seconds
turn ↻ (120) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↺ (-120) degrees
wait (1) seconds
move (200) steps
wait (1) seconds
turn ↻ (180) degrees
  ```

- **B.**

  ```text
  turn ↺ (60) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↻ (120) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↺ (-120) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↻ (90) degrees
  ```

- **C.**

  ```text
  turn ↺ (60) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↻ (120) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↺ (-120) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↻ (180) degrees
  ```

- **D.**

  ```text
  turn ↺ (60) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↻ (-60) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↺ (60) degrees
wait (1) seconds
move (100) steps
wait (1) seconds
turn ↻ (-60) degrees
  ```


<details><summary>Answer</summary>

**C**. Option C moves 100 steps three times, turning 120° each time (`turn -120` ccw is 120° clockwise), so the path closes into an equilateral triangle. The final `turn 180` brings the cat back to its original heading.

</details>

**`2022-jan/w01/q03`** What will be the value of my variable?

```text
set [my variable] to (10)
repeat (10)
    wait (1) seconds
    change [my variable] by (10)
end
set [my variable] to ((my variable) / (5))
```

- **A.** 20
- **B.** 10
- **C.** 22
- **D.** 25

<details><summary>Answer</summary>

**C**. The variable starts at 10 and the loop adds 10 each time for 10 passes, giving 110. Then it is divided by 5, so it ends at 110 ÷ 5 = `22`.

</details>

**`2022-jan/w01/q04`** What the sprite(the cat) will say?

```text
set [t] to (0)
repeat until <(t) > (5)>
    say (t)
    change [t] by (1)
    wait (1) seconds
end
```

- **A.** 0, 1, 2, 3, 4, 5
- **B.** 1, 2, 3, 4, 5
- **C.** 1, 2, 3, 4, 5, 6
- **D.** None of the above

<details><summary>Answer</summary>

**A**. `t` starts at 0 and the loop runs until `t > 5`. Each pass says `t` and then adds 1, so it says 0, 1, 2, 3, 4, 5 and stops once `t` reaches 6.

</details>

**`2022-jan/w01/q05`** What should be a set of instructions to make our sprite(cat) say a table of 5?

- **A.**

  ```text
  set [s] to (5)
set [t] to (1)
set [x] to (5)
repeat (10)
    say (x)
    set [x] to ((t) * (s))
    change [t] by (1)
    wait (1) seconds
end
  ```

- **B.**

  ```text
  set [s] to (5)
set [t] to (1)
set [x] to (5)
repeat (10)
    say (x)
    change [t] by (1)
    wait (1) seconds
    set [x] to ((t) * (s))
end
  ```

- **C.**

  ```text
  set [s] to (5)
set [t] to (1)
set [x] to (5)
repeat (11)
    say (x)
    change [t] by (1)
    wait (1) seconds
    set [x] to ((t) * (s))
end
  ```

- **D.**

  ```text
  set [s] to (5)
set [t] to (1)
set [x] to (5)
repeat (11)
    say (x)
    set [x] to ((t) * (s))
    change [t] by (1)
    wait (1) seconds
end
  ```


<details><summary>Answer</summary>

**B**. Option B says `x` first, then raises `t` and sets `x = t * s`, so it says 5, 10, 15, … over 10 passes: the table of 5 up to 50.

</details>

**`2022-jan/w01/q06`** Imagine a cricket ball as our sprite, the ball will move in

```text
repeat (17)
    turn ↺ (20) degrees
    move (30) steps
end
```

- **A.** a straight line.
- **B.** Circular motion.
- **C.** Curve path.
- **D.** Up and Down.

<details><summary>Answer</summary>

**C**. Each pass turns 20° and moves 30 steps, 17 times. The turns add up to 340°, short of a full circle, so the ball traces an open curve.

</details>

**`2022-jan/w01/q08`** Imagine a cricket player hitting a sixer on a delivery. Which code block represents the upward moment and downward movement of the ball.

```text
Left block:                   Right block:
turn ↺ (20) degrees            turn ↻ (60) degrees
move (100) steps               move (100) steps
wait (1) seconds               wait (1) seconds
turn ↺ (20) degrees            turn ↻ (40) degrees
move (100) steps               move (100) steps
wait (1) seconds               wait (1) seconds
```

- **A.** Left Block represents downward movement and the right block represents upward movement.
- **B.** Left Block represents upward movement and the right block represents downward movement.
- **C.** Both blocks represent upward movement.
- **D.** Both blocks represent downward movement.

<details><summary>Answer</summary>

**B**. The left block turns counter-clockwise 20° twice, so the ball heads upward; the right block turns clockwise 60° and then 40°, so it heads downward. Left is the upward movement, right the downward.

</details>

**`2022-jan/w01/q09`** Which of the following statements is true about the following block of code?

```text
set [x] to (1)
repeat (7)
    set [t] to (pick random (1) to (10))
    change [x] by (t)
    wait (1) seconds
end
show variable [x]
```

- **A.** This code block is adding 7 random numbers between 1 - 10 to x.
- **B.** This code block is adding 10 random numbers between 1 - 10 to x.
- **C.** This code block is adding 7 random numbers between 1 - 10 to t.
- **D.** This code block is adding 10 random numbers between 1 - 10 to t.

<details><summary>Answer</summary>

**A**. `x` starts at 1. The loop runs 7 times; each pass puts a random number from 1 to 10 in `t`, then adds `t` to `x`. So it adds 7 random numbers to `x`.

</details>

**`2022-jul/w01/q06`** What does the cat say after executing the following code? (Scratch blocks as shown: `set [x] to (2)` → `repeat (20)` { `if <((x) mod (2)) = (0)> then` { `say (x)` · `wait (1) seconds` } · `change [x] by (1)` })

```text
set [x] to (2)
repeat (20)
    if <((x) mod (2)) = (0)> then
        say (x)
        wait (1) seconds
    end
    change [x] by (1)
    ... (the recording cuts off here)
end
```

- **A.** All-natural numbers between 1-20. (Both inclusive)
- **B.** All even numbers between 1-20. (Both inclusive)
- **C.** All odd numbers between 1-20. (Both inclusive)
- **D.** All whole numbers between 0-20. (Both inclusive)

<details><summary>Answer</summary>

**B**. `x` starts at 2 and goes up by 1 on each of the 20 passes (2 to 21). The cat says `x` only when `x mod 2 = 0`, so it says the even numbers 2, 4, …, 20.

</details>

**`2023-jan/w01/q06`** Predict the output of the following:

```text
set [num] to (100)
repeat (10)
    change [num] by (-2)
end
```

- **A.** 0
- **B.** 100
- **C.** 20
- **D.** None of the above

<details><summary>Answer</summary>

**D**. `num` starts at 100 and `change num by -2` runs 10 times, so `num` = 100 − 20 = 80. That is not 0, 100 or 20, so the answer is none of the above.

</details>

**`2023-jul/w01/q05@gpt`** Imagine sprite to be a scooter. How many times scooter will move forward?

```text
set [z] to (2)
set [x] to (1)
repeat (10)
    if <((x) / (z)) = (1)> then
        move (10) steps
        change [z] by (2)
    end
    change [x] by (1)
    wait (1) seconds
end
```

- **A.** 7
- **B.** 4
- **C.** 6
- **D.** 5

<details><summary>Answer</summary>

**D**. `z` = 2 and `x` = 1. The `move` runs only when `x / z = 1`: that happens at x = 2, 4, 6, 8 and 10 (z grows by 2 each time), so the scooter moves forward 5 times.

</details>

**`2024-jan/w01/q05`** Knowing how to write a piece of code could help us get things done fast. Choose the areas where we can implement coding.?

```text
(Problem introduction: a picture of the Scratch cat playing volleyball with a ball,
 and the scripts below. Parts of the "define Boomerang" script are hidden behind a
 video overlay in the only recording.)

when I receive [Ball Kicked]
Boomerang
broadcast [Ball has hit cat's face]

when I receive [Ball has hit cat's face]
Rotate

define Boomerang            (the ball's script; see Q9)
repeat (2)
    move (10) steps
    turn ↻ (15) degrees
    wait (.1) seconds
    move (75) steps
    ...
end

define Rotate               (the cat's script; see Q7)
repeat (3)
    repeat (4)
        wait (.15) seconds
        turn ↺ (90) degrees
    end
end

(the cat's kick script; see Q6)
move (10) steps
wait (.1) seconds
turn ↻ (15) degrees
wait (.1) seconds
move (10) steps
wait (.1) seconds
turn ↺ (15) degrees
broadcast [Ball Kicked]
```

- **A.** Physics
- **B.** Mathematics
- **C.** Economics
- **D.** Small Scale Business

<details><summary>Answer</summary>

**A, B, C, D**. Code can model physics, do maths, analyse economics and automate small-business tasks. All four areas are valid, so all four options are correct.

</details>

**`2024-jan/w01/q06`** The block of code displayed here is meant for the cat, what is the functionality of this code? (Scratch blocks: `move (10) steps` · `wait (1) seconds` · `turn ↻ (15) degrees` · `wait (1) seconds` · `move (10) steps` · `wait (1) seconds` · `turn ↺ (15) degrees` — wait values read as "1"; may be ".1", see image)

```text
move (10) steps
wait (.1) seconds
turn ↻ (15) degrees
wait (.1) seconds
move (10) steps
wait (.1) seconds
turn ↺ (15) degrees
```

- **A.** It brings the ball closer to the cat.
- **B.** It makes the cat appear like kicking the ball.
- **C.** It makes the cat tumble and rotate
- **D.** The code throws an error.

<details><summary>Answer</summary>

**B**. The cat moves 10 steps, tilts 15° clockwise, moves 10 more, then tilts 15° back. A small step forward with a lean and recovery looks like a kick.

</details>

**`2024-jan/w01/q09`** The block of code displayed here is meant for the ball, how many loops are there in total? (Scratch blocks: `repeat (2)` { `move (10) steps` · `turn ↻ (15) degrees` · `wait (.1) seconds` · `move (75) steps` · `wait (.1) seconds` · `turn ↺ (15) degrees` · `wait (.1) seconds` · `move (65) steps` · `wait (.1) seconds` · `turn ↺ (90) degrees` · `wait (.1) seconds` · `move (50) steps` · `wait (.1) seconds` · `turn ↺ (90) degrees` } — "65" could be "55"/"85", blurry; see image)

```text
repeat (2)
    move (10) steps
    turn ↻ (15) degrees
    wait (.1) seconds
    move (75) steps
    wait (.1) seconds
    turn ↺ (15) degrees
    wait (.1) seconds
    move (65) steps          (blurry: could be 55 or 85)
    wait (.1) seconds
    turn ↺ (90) degrees
    wait (.1) seconds
    move (50) steps
    wait (.1) seconds
    turn ↺ (90) degrees
end
```

- **A.** One
- **B.** Two
- **C.** Three
- **D.** Four

<details><summary>Answer</summary>

**B**. The picture has a single `repeat 2` block, so "how many loops" can mean one loop block or two runs of it. This card counts the runs: the body executes twice, which gives Two.

</details>

**`2024-jul/w01/q10`** What task does the block below accomplish ?

```text
set [x] to (0)
set [y] to (0)
repeat (21)
    wait (1) seconds
    go to x: (x) y: (y)
    set [x] to ((x) + (1))
    set [y] to (((20) * (x)) + (((0) - (x)) * (x)))
end
```

- **A.** Moves the ball in a parabolic path and stops 21 away steps from center(0, 0) in x direction.
- **B.** Moves the ball in a circular path and 21 times.
- **C.** Moves the ball in a triangular path and end at the center (0, 0).
- **D.** Moves the ball in a parabolic path and stops 20 away steps from center(0, 0) in x direction.

<details><summary>Answer</summary>

**D**. x runs 0 to 20 over the 21 passes and y = 20x − x², a parabola. The last pass puts the ball at x = 20, y = 0: 20 steps from the centre along x.

</details>

**`2025-jan/w01/q10`** What task does the block below accomplish ?

```text
set [x] to (0)
set [y] to (0)
repeat (18)
    wait (1) seconds
    set x to (x)
    set y to (y)
    change [x] by (1)
    set [y] to ((((0) - (x)) * (x)) + ((17) * (x)))
end
```

- **A.** Moves the ball in a parabolic path and stops 18 away steps from center(0, 0) in x direction.
- **B.** Moves the ball in a circular path and 18 times.
- **C.** Moves the ball in a parabolic path and stops 18 away steps from center(0, 0) in y direction.
- **D.** Moves the ball in a parabolic path and stops 17 away steps from center(0, 0) in x direction.

<details><summary>Answer</summary>

**A**

</details>

**`2026-jul/w01/q10`** Which statement best summarizes the role of loops in programming?

```text
move (5) steps
turn ↻ (15) degrees
move (5) steps
point in direction (90)
move (10) steps
```

- **A.** Loops are useful only for mathematical calculations.
- **B.** Loops replace the need for variables.
- **C.** Loops help automate repetitive tasks and make programs easier to modify and maintain.
- **D.** Loops should be avoided because they make programs difficult to understand.

<details><summary>Answer</summary>

**C**. Loops automate repeated work, so you write the steps once. That also makes programs shorter and easier to change and maintain.

</details>

**`2026-jul/w01/q11`** Which Scratch block determines the direction of the sprite before its final movement of 10 steps?

(Same program as the previous card.)

- **A.** move 5 steps (first block)
- **B.** turn 15 degrees
- **C.** move 5 steps (third block)
- **D.** point in direction 90°

<details><summary>Answer</summary>

**D**. Blocks run top to bottom. `point in direction 90` is the last block that sets direction before the final `move 10 steps`, so it decides which way that move goes.

</details>

**`2026-jul/w01/q12`** What is the purpose of the turn 15 degrees block in this program?

(Same program as the previous card.)

- **A.** It changes the sprite's direction before the second movement.
- **B.** It changes the sprite's position by 15 steps.
- **C.** It changes the direction for the entire program, including after the point in direction block.
- **D.** It makes the sprite move automatically.

<details><summary>Answer</summary>

**A**. `turn 15 degrees` rotates the sprite, so the next `move 5 steps` goes along the new heading.

</details>

**`2026-jul/w01/q13`** Suppose the point in direction 90° block is removed while keeping all other blocks unchanged. Which statement is most likely to be true?

(Same program as the previous card.)

- **A.** The final movement will continue in the direction established by the earlier turn.
- **B.** The sprite will not execute the last move.
- **C.** The sprite will return to its starting position.
- **D.** The program will stop with an error.

<details><summary>Answer</summary>

**A**. Without `point in direction 90`, nothing resets the heading, so the final `move 10 steps` follows the direction left by the 15° turn.

</details>

**`2026-jul/w01/q14`** Which Scratch blocks in the program only change the sprite's position and never its direction?

(Same program as the previous card.)

- **A.** the two move 5 blocks
- **B.** all three move blocks
- **C.** turn and point
- **D.** move 10 and point

<details><summary>Answer</summary>

**B**. All three `move` blocks only change the sprite's position along its current heading. `turn` and `point in direction` are the blocks that change direction.

</details>

**`2026-jul/w01/q15`** A student accidentally swaps the positions of the turn 15 degrees block and the point in direction 90° block. What is the most likely effect?

(Same program as the previous card.)

- **A.** The sprite will follow exactly the same path.
- **B.** The final movement will occur after turning 15° from 90°, producing a different path.
- **C.** The sprite will not execute the second movement.
- **D.** The program will become an infinite loop.

<details><summary>Answer</summary>

**B**. Blocks run in order. After swapping, `turn 15` comes before `point in direction 90`, so the final move heads along 90 + 15 and the path is different.

</details>

**`2026-jul/w01/q16`** Why does the program use the expression counter mod 2 = 0?

```text
set [score] to (12)
set [counter] to (0)
set [bonus] to (0)
repeat (6)
    change [score] by (5)
    change [counter] by (1)
    if <((counter) mod (2)) = (0)> then
        change [bonus] by (3)
    else
        change [bonus] by (1)
    end
end
change [score] by (bonus)
if <<(score) > (50)> or <(score) = (50)>> then
    say [Excellent!] for (2) seconds
else
    if <<(score) > (40)> or <(score) = (40)>> then
        say [Level Cleared!] for (2) seconds
    else
        say [Try Again!] for (2) seconds
    end
end
```

- **A.** To check whether the current round number is even.
- **B.** To stop the repeat loop after two iterations.
- **C.** To calculate the total score.
- **D.** To reset the bonus variable.

<details><summary>Answer</summary>

**A**. `counter mod 2` is the remainder after dividing by 2. A remainder of 0 means the counter is even, so the test checks for an even round.

</details>

**`2026-jul/w01/q17`** Which variable is updated in every iteration of the repeat loop, regardless of the outcome of the if-else condition?

(Same program as the previous card.)

- **A.** bonus
- **B.** counter
- **C.** score
- **D.** Both score and counter

<details><summary>Answer</summary>

**D**. Every pass runs `change score by 5` and `change counter by 1`, whatever the `if` result. `bonus` changes only inside the if/else, by 3 or 1.

</details>

**`2026-jul/w01/q18`** What is the purpose of the statement change score by bonus placed after the repeat loop?

(Same program as the previous card.)

- **A.** It resets the score before displaying the final message.
- **B.** It adds the total bonus accumulated during all iterations to the final score.
- **C.** It increases the bonus by the current score.
- **D.** It determines how many times the loop executes.

<details><summary>Answer</summary>

**B**. `bonus` collects points during the loop. `change score by bonus` adds that total to `score` once, after the loop ends.

</details>

**`2026-jul/w01/q19`** Suppose the statement change score by bonus is moved inside the repeat loop, immediately before the if condition. What would be the most likely effect?

(Same program as the previous card.)

- **A.** The final score would become much larger because the bonus would be added repeatedly.
- **B.** The final score would remain unchanged.
- **C.** The bonus variable would always become zero.
- **D.** The repeat loop would execute fewer times.

<details><summary>Answer</summary>

**A**. Inside the loop, the bonus would be added to `score` on every pass, so `score` would grow far past the original value.

</details>

---

## D. Program options

**`2022-jan/w03/q02`** What should be the code to print all Even numbers between 1-10 (both inclusive)?

- **A.**

  ```python
  for i in range(10):
    if(i%2 == 0):
        print(i)
  ```

- **B.**

  ```python
  for i in range(11):
    if(i%2 == 0):
        print(i)
  ```

- **C.**

  ```python
  for i in range(1,11):
    if(i%2 == 0):
        print(i)
  ```

- **D.**

  ```python
  for i in range(1,11):
    if(i%2 == 1):
        print(i)
  ```


<details><summary>Answer</summary>

**C**. `range(1, 11)` gives 1 to 10, and `i%2 == 0` keeps the even ones, so it prints 2, 4, 6, 8, 10.

</details>

**`2022-jan/w03/q06`** What is the correct code for a function to return the sum of elements of list L?

- **A.**

  ```python
  def sum_of_list(L):

    Total = 0

    for i in range(len(L)):
        Total = Total + L[i]

    return Total

L = [1,2,3,4,5,6,7,8,9,10]

total_sum = sum_of_list(L)

print(total_sum)
  ```

- **B.**

  ```python
  def sum_of_list(L):

    Total = 0

    for i in range(len(L)):
        Total = Total + L[i]


L = [1,2,3,4,5,6,7,8,9,10]

total_sum = sum_of_list(L)

print(total_sum)
  ```

- **C.**

  ```python
  def sum_of_list():

    Total = 0

    for i in range(len(L)):
        Total = Total + L[i]

    return Total

L = [1,2,3,4,5,6,7,8,9,10]

total_sum = sum_of_list(L)

print(total_sum)
  ```

- **D.**

  ```python
  def sum_of_list(L):

    Total = 0

    for i in range(len(L)):
        Total = Total + L[i]

    return Total

L = [1,2,3,4,5,6,7,8,9,10]

total_sum = sum_of_list()

print(total_sum)
  ```


<details><summary>Answer</summary>

**A**. Option A defines `sum_of_list(L)` with a parameter, adds each element to `Total`, returns it, and calls it with `L`.

</details>

**`2021-jan/w04/q07`** Which of the following will print all prime numbers in an interval?

- **A.**

  ```python
  lower = int(input())
upper = int(input())
for num in range(lower, upper + 1):
    if num>1:
        for i in range (2,num):
            if(num % i) == 0:
                break
        else:
            print(num)
  ```

- **B.**

  ```python
  for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) != 0:
                print(num)
  ```

- **C.**

  ```python
  for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                continue
            else:
                print(num)
  ```

- **D.**

  ```python
  for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) != 0:
                break
            else:
                print(num)
  ```


<details><summary>Answer</summary>

**A**. Option A has a `for … else`: the `else` runs only if no `i` from 2 to num−1 divides `num` (no `break` happened), and then it prints `num`. That prints the primes.

</details>

**`2021-jul/w04/q07`** Which program will choose an element from the below list and display it in jumbled order?

- **A.**

  ```python
  import random
l=["abc","cde","efg","hij"]
a=random.choice(l)
print("".join(random.sample(a,len(a))))
  ```

- **B.**

  ```python
  l=["abc","cde","efg","hij"]
a=random.choice(l)
print("".join(random.sample(a,len(a))))
  ```

- **C.**

  ```python
  import random
l=["abc","cde","efg","hij"]
a=random.Random(l)
print(a)
print("".join(random.sample(a,len(a))))
  ```

- **D.**

  ```python
  import random
l=["abc","cde","efg","hij"]
a=random.sample(l)
print(a)
print("".join(random.choice(a,len(a))))
  ```


<details><summary>Answer</summary>

**A**. Option A imports `random`, picks one string with `random.choice`, and jumbles its letters with `random.sample(a, len(a))` joined into a string.

</details>

**`2022-jan/w04/q02`** What is the correct code to display whether the entered year is a leap year or not?

- **A.**

  ```python
  def leap_year(year):

    if(year%400 == 0):
        print("Its a leap year")
        return
    else:
        print("not a leap year")
        return

year = int(input("Enter Year: ")) #will convert in input into integer
leap_year(year)
  ```

- **B.**

  ```python
  def leap_year(year):

    if(year%400 == 0 or year%4 == 0):
        print("Its a leap year")

    if(year%100 == 0):
        print("not a leap year")
        return

year = int(input("Enter Year: ")) #will convert in input into integer
leap_year(year)
  ```

- **C.**

  ```python
  def leap_year(year):

    if(year%400 == 0 or year%4 == 0):
        print("Its a leap year")

    print("not a leap year")
    return

year = int(input("Enter Year: ")) #will convert in input into integer
leap_year(year)
  ```

- **D.**

  ```python
  def leap_year(year):

    if(year%400 == 0 or year%4 == 0):
        print("Its a leap year")
        return
    else:
        print("not a leap year")
        return

year = int(input("Enter Year: ")) #will convert in input into integer
leap_year(year)
  ```


<details><summary>Answer</summary>

**D**

</details>

**`2022-jan/w04/q06`** What is the code to generate all prime numbers between 0-100?

- **A.**

  ```python
  for i in range(2,101):
    flag=0
    for j in range(2, 101):
        if(i%j == 0):
            flag=1
            break
    if(flag == 0):
        print(i)
  ```

- **B.**

  ```python
  for i in range(2,101):
    flag=0
    for j in range(2, i):
        if(i%j == 0):
            flag=1
            break
    if(flag == 0):
        print(i)
  ```

- **C.**

  ```python
  for i in range(2,101):
    flag=0
    for j in range(2, i+1):
        if(i%j == 0):
            flag=1
            break
    if(flag == 0):
        print(i)
  ```

- **D.**

  ```python
  for i in range(101):
    flag=0
    for j in range(2, i):
        if(i%j == 0):
            flag=1
            break
    if(flag == 0):
        print(i)
  ```


<details><summary>Answer</summary>

**B**. For each `i` from 2 to 100, option B tries every `j` from 2 up to `i-1`. If any `j` divides `i`, `flag` becomes 1; otherwise `i` is prime and is printed.

</details>

**`2022-jan/w04/q07`** What is code to replace all the letters of a movie name except special(‘-’, ‘White spaces’, etc) characters with * in a single line.

- **A.**

  ```python
  import string
import random

L = ['spider-man', 'matrix', 'harry potter', 'terminator',
        'alien isolation', 'resident evil']

sc = string.ascii_letters+'0123456789'

movie = random.choice(L)

for ch in movie:
    if(ch not in sc):
        print('*', end='')
    else:
        print(ch, end='')
  ```

- **B.**

  ```python
  import string
import random

L = ['spider-man', 'matrix', 'harry potter', 'terminator',
        'alien isolation', 'resident evil']

sc = string.ascii_letters+'0123456789'

movie = random.choice(L)

for ch in movie:
    if(ch in sc):
        print('*')
    else:
        print(ch)
  ```

- **C.**

  ```python
  import string
import random

L = ['spider-man', 'matrix', 'harry potter', 'terminator',
        'alien isolation', 'resident evil']

sc = string.ascii_letters+'0123456789'

movie = random.choice(L)

for ch in movie:
    if(ch not in sc):
        print('*')
    else:
        print(ch)
  ```

- **D.**

  ```python
  import string
import random

L = ['spider-man', 'matrix', 'harry potter', 'terminator',
        'alien isolation', 'resident evil']

sc = string.ascii_letters+'0123456789'

movie = random.choice(L)

for ch in movie:
    if(ch in sc):
        print('*', end='')
    else:
        print(ch, end='')
  ```


<details><summary>Answer</summary>

**D**. Option D prints `*` for every character that is a letter or a digit (in `sc`), and prints the other characters as they are. `end=''` keeps the output on one line.

</details>

**`2022-jan/w04/q09`** What's the correct code to calculate the sum of series 1 + (1+2) + (1+2+3) + (1+2+3+4) + …. + n terms.

- **A.**

  ```python
  num = int(input())
total = 0

for i in range(1,num+1):
    for j in range(1,i):
        total = total+j

print(total)
  ```

- **B.**

  ```python
  num = int(input())
total = 0

for i in range(1,num):
    for j in range(1,i+1):
        total = total+j

print(total)
  ```

- **C.**

  ```python
  num = int(input())
total = 0

for i in range(1,num+1):
    for j in range(1,i+1):
        total = total+j

print(total)
  ```

- **D.**

  ```python
  num = int(input())
total = 0

for i in range(1,num+1):
    for j in range(1,i+1):

    total = total+j

print(total)
  ```


<details><summary>Answer</summary>

**C**. Each `i` needs the inner sum 1 + 2 + … + i, so the inner loop must run to `i` (`range(1, i+1)`), and `total = total + j` must sit inside it. The outer loop must run to `num` (`range(1, num+1)`).

</details>

**`2022-jan/w04/q10`** A perfect number is a number in which the sum of divisors is equal to that number. For example, 6 is a perfect number as a sum of its divisors 1,2,3 is equal to 6. Which function returns True if the number is a perfect number?

- **A.**

  ```python
  def perfect_number(num):
    ans=0
    for i in range(1,num):
        if(num%i==0):
            ans = ans + i
    if(ans==num):
        return True
    else:
        return False
  ```

- **B.**

  ```python
  def perfect_number(num):
    ans=0
    for i in range(1,num):
        if(num%i==0):
            ans+=i
    if(ans==num):
        return False
    else:
        return True
  ```

- **C.**

  ```python
  def perfect_number(num):
    ans=0
    for i in range(3,num):
        if(num%i==0):
            ans = ans + i
    if(ans==num):
        return True
    else:
        return False
  ```

- **D.**

  ```python
  def perfect_number(num):
    ans=0
    for i in range(1,num):
        if(num%i==0):
            ans = ans + i
    if(ans!=num):
        return True
    else:
        return False
  ```


<details><summary>Answer</summary>

**A**. Option A adds up every divisor of `num` below `num` and returns `True` only if the sum equals `num`. For 6 that is 1 + 2 + 3 = 6.

</details>

**`2022-jan/w05/q08`** What is the correct code to choose rock, paper, or scissors correctly?

- **A.**

  ```python
  d = {1 : 'Rock', 2 : 'Paper', 3 : 'scissors'}

choice = int(input())


game_choice = d[choice%3]
  ```

- **B.**

  ```python
  d = {0 : 'Rock', 1 : 'Paper', 2 : 'scissors'}

choice = int(input())


game_choice = d[choice%2]
  ```

- **C.**

  ```python
  d = {0 : 'Rock', 1 : 'Paper', 2 : 'scissors'}

choice = input()


game_choice = d[choice%3]
  ```

- **D.**

  ```python
  d = {0 : 'Rock', 1 : 'Paper', 2 : 'scissors'}

choice = int(input())


game_choice = d[choice%3]
  ```


<details><summary>Answer</summary>

**D**. Option D keeps the keys 0, 1, 2 in the dictionary and uses `int(input())` with `choice % 3`, so any number maps to a valid key.

</details>

**`2021-jul/w06/q08`** Which of the following programs will calculate the factorial of a given number?

- **A.**

  ```python
  def fact(n):
    if(n==0):
        return 1
    else:
        return(n*fact(n+1))

n=int(input("Enter the number whose factorial has to be calculated\n"))
if(n<0):
    print("Enter a valid number")
print("The factorial of",n,"is",fact(n))
  ```

- **B.**

  ```python
  def fact(n,t):
    if(t==n):
        return n
    else:
        return t*fact(n,t+1)

n=int(input("Enter the number whose factorial has to be calculated\n"))
if(n<0):
    print("Enter a valid number")
print("The factorial of",n,"is",fact(n,0))
  ```

- **C.**

  ```python
  def fact(n,t):
    if(t==n):
        return n
    else:
        return t*fact(n,t+1)

n=int(input("Enter the number whose factorial has to be calculated\n"))
if(n<0):
    print("Enter a valid number")
print("The factorial of",n,"is",fact(n,1))
  ```

- **D.** None of the following

<details><summary>Answer</summary>

**C**. Option C calls `fact(n, 1)`: it multiplies `t` from 1 up to `n` and returns `n` at the end, giving n!. Option A calls `fact(n+1)` forever, and option B starts at 0, so the product is 0.

</details>

**`2021-jan/w08/q08`** Which of the following code will convert the uppercase letters of the given string into lower case and prints the converted string?

- **A.**

  ```python
  strng = input()
out = ''
for i in strng:
    if i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        out = out + i
    else:
        j = ord(i)
        k = j + 32
        out = out + chr(k)
print(out)
  ```

- **B.**

  ```python
  strng = input ()
out = ''
for i in strng:
    if ord (i) >= 65 and ord(i) <= 90:
        j = ord(i) + 32
        k = chr (j)
        out = out + k
print(out)
  ```

- **C.** both A and B
- **D.** none

<details><summary>Answer</summary>

**A**. Option A keeps every character that is not in the uppercase string, and for an uppercase letter adds 32 to its code, which gives the lowercase letter. The result is the whole string with only uppercase letters changed.

</details>

**`2022-jan/w10/q04`** Which code snippet represent replacing all vowels with ‘_’ in a string?(suppose string name is s)

- **A.**

  ```python
  s='The joy of Computing'

s.replace('a', '_')
s.replace('e', '_')
s.replace('i', '_')
s.replace('i', '_')
s.replace('o', '_')
s.replace('u', '_')

print(s)
  ```

- **B.**

  ```python
  s='The joy of Computing'

s.replace('_', 'a')
s.replace('_', 'e')
s.replace('_', 'i')
s.replace('_', 'o')
s.replace('_', 'u')

print(s)
  ```

- **C.**

  ```python
  s='The joy of Computing'

s = s.replace('_', 'a')
s = s.replace('_', 'e')
s = s.replace('_', 'i')
s = s.replace('_', 'o')
s = s.replace('_', 'u')

print(s)
  ```

- **D.**

  ```python
  s='The joy of Computing'

s = s.replace('a', '_')
s = s.replace('e', '_')
s = s.replace('i', '_')
s = s.replace('o', '_')
s = s.replace('u', '_')

print(s)
  ```


<details><summary>Answer</summary>

**D**. Option D assigns the result of `replace` back to `s` five times, once for each vowel, so every vowel is changed to `_`. A and B only call `replace` and throw the result away, since strings cannot be changed in place. C replaces `_` with vowels, the other way round.

</details>

**`2021-jan/w11/q10`** Which of the following is the correct code to find whether a given year is a leap year or not?

- **A.**

  ```python
  year = int(input())
if (year % 100) or (year % 400) == 0:
    print("leap year")
else:
    print("not a leap year")
  ```

- **B.**

  ```python
  year = int(input())
if (year % 100) == 0:
    if (year % 400) == 0:
            print("leap year")
    else:
            print("not a leap year")
else:
        print("leap year")
  ```

- **C.**

  ```python
  year = int(input())
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")
  ```

- **D.**

  ```python
  year = int(input())
if (year % 100) or (year % 400) == 0:
    print("leap year")
else:
    print("not a leap year")
# (option D's picture shows the same program as option A)
  ```


<details><summary>Answer</summary>

**C**. In option C, a year divisible by 4 is a leap year, unless it is divisible by 100, in which case it must also be divisible by 400. Years that are not divisible by 4 are not leap years. That is the correct rule.

</details>

---

## E1. Question code from screenshots

**`2021-jul/w02/q01`** What will be the output for the following program if the user gives an input value of 3 to it?

```python
c= input("Enter a number")
print(c*5)
```

- **A.** 15
- **B.** 33333
- **C.** Error message
- **D.** 555

<details><summary>Answer</summary>

**B**. `input()` returns the string `'3'`, and a string times 5 repeats it five times, so `c*5` prints `33333`.

</details>

**`2021-jul/w02/q03`** What will be the output of the following code when  executed?

```python
for i in range(3,30,3):
    print (i)
```

- **A.** It will print numbers from 3 to 30
- **B.** It will print multiples of 3 till 30
- **C.** It will print multiples of 3 till 27
- **D.** It will print 3 thirty times

<details><summary>Answer</summary>

**C**. `range(3, 30, 3)` starts at 3 and steps by 3 but stops before 30: 3, 6, …, 27. So it prints the multiples of 3 up to 27.

</details>

**`2021-jul/w02/q04`** What will the output of the following code be when executed?

```python
c=30
a=4
print(c/a)
print(c//a)
```

- **A.**

  ```python
  7.5
7
  ```

- **B.**

  ```python
  7.5
7.5
  ```

- **C.**

  ```python
  7
7
  ```

- **D.**

  ```python
  7.5
2
  ```


<details><summary>Answer</summary>

**A**. `c/a` is true division, so 30/4 gives `7.5`. `c//a` is floor division, so 30//4 gives `7`.

</details>

**`2021-jul/w02/q07`** What will the output of the following program be?

```python
c=input()
print(type(c))
```

- **A.** < class 'str' >
- **B.** < class 'int' >
- **C.** < class 'number' >
- **D.** < class 'variable ' >

<details><summary>Answer</summary>

**A**. `input()` always returns a string, so `type(c)` is `<class 'str'>`, even if the user types digits.

</details>

**`2022-jan/w02/q02`** What is the output of the following code?

```python
a = "round."
b = "lot of"
c= "dust."

print('Earth is')
print(a)
print("Moon has", b, c)
```

- **A.**

  ```python
  Earth is round.
Moon has lot of dust.
  ```

- **B.**

  ```python
  Earth is
round.
Moon has
lot of dust.
  ```

- **C.**

  ```python
  Earth is
round.
Moon has lot of dust.
  ```

- **D.** Earth is round.Moon has lot of dust.

<details><summary>Answer</summary>

**C**. The first `print` outputs `Earth is` and a newline. The second prints `round.` and a newline. The third joins `Moon has`, `lot of` and `dust.` with spaces on one line.

</details>

**`2022-jan/w02/q06`** What will be the output? suppose the input is 20

```python
number = input("Enter Number")

new_number = number * 2

print(new_number)
```

- **A.** 40
- **B.** Error
- **C.** 2020
- **D.** None of the above

<details><summary>Answer</summary>

**C**. `input()` returns the string `'20'`, and `* 2` repeats a string twice. So `new_number` is `'2020'` and that is printed.

</details>

**`2022-jan/w02/q07`** What will be the output of the following code be?

```python
number = 20/10 * 0

if(number < 0):
    print('numbrt is less than 0')

if(number > 0):
    print('number is greater than zero')

if(number = 0):
    print('number is zero')
```

- **A.** number is less than 0
- **B.** number is greater than 0
- **C.** number is zero
- **D.** Error

<details><summary>Answer</summary>

**D**. The last test is `if(number = 0):`. A single `=` assigns, so Python raises a `SyntaxError` and runs nothing.

</details>

**`2022-jan/w02/q08`** What will be the output of the following code?

```python
a = 10

for i in range(10):
    a = i

print(a)
```

- **A.** 9
- **B.** 10
- **C.** 0
- **D.** None of the above

<details><summary>Answer</summary>

**A**. `a` starts at 10. The loop sets `a = i` on each pass, so after the last pass `a` holds the final `i`, which is `9`.

</details>

**`2022-jan/w02/q09`** What will be the output of the following code?

```python
a = 1
for i in range(10):

    a = a + (i+1)

print(a)
```

- **A.** 56
- **B.** 45
- **C.** 0
- **D.** Error

<details><summary>Answer</summary>

**A**. `a` starts at 1 and `a = a + (i+1)` adds 1, 2, …, 10 for i = 0 to 9. That is 1 + 55 = `56`.

</details>

**`2022-jan/w02/q10`** What will be the output of the following code?

```python
a = 0
while(a < 10):
    a = a+2
    print(a)
```

- **A.** 1,2,3,4,5,6,7,8,9,10
- **B.** 2,4,6,8,10
- **C.** 0,1,2,3,4,5,6,7,8,9,10
- **D.** Error

<details><summary>Answer</summary>

**B**. `a` starts at 0 and each pass adds 2 before printing. It prints 2, 4, 6, 8, 10 and stops when `a` reaches 10.

</details>

**`2021-jul/w03/q02`** What will the output of the following program be?

```python
a=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(a),2):
    print(a[i])
```

- **A.** All numbers from 1 to 10
- **B.** All even numbers from 1 to 10
- **C.** All odd numbers from 1 to 10
- **D.** It will give an error

<details><summary>Answer</summary>

**C**. `range(0, len(a), 2)` gives indexes 0, 2, 4, 6, 8, so it prints `a[0]`, `a[2]`, … = 1, 3, 5, 7, 9, the odd numbers.

</details>

**`2021-jul/w03/q03`** What will the output of the following program be?

```python
a=[1,2,3,4,5,6,7,8,9,10]
a.insert(-3, 999)
print(a)
```

- **A.** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- **B.** [1, 2, 3, 4, 5, 6, 7, 999, 8, 9, 10]
- **C.** It will give an error
- **D.** [999, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

<details><summary>Answer</summary>

**B**. `a.insert(-3, 999)` inserts before the third item from the end, which is position 7. So `999` lands between 7 and 8.

</details>

**`2021-jul/w03/q08`** What is the output of the following program?

```python
a="Hello"
print("+".join(a))
```

- **A.** H+e+l+l+o
- **B.** +Hello+
- **C.** +H+e+l+l+o
- **D.** +Hello

<details><summary>Answer</summary>

**A**. `"+".join(a)` puts `+` between the characters of the string: `H+e+l+l+o`.

</details>

**`2022-jan/w03/q01`** What will be the output of the following code?

```python
L = ["Practice", "makes", "the", "man", "perfect."]
L.sort()

for element in L:
    print(element)
```

- **A.** Practice,Practice,Practice,Practice,Practice
- **B.** Practice makes the man perfect.
- **C.** Practice makes man perfect. the
- **D.** Makes man perfect. Practice the

<details><summary>Answer</summary>

**C**. `L.sort()` sorts the strings by their character codes, and capital letters come before small ones. The order is `Practice`, `makes`, `man`, `perfect.`, `the`.

</details>

**`2022-jan/w03/q04`** What will be the output of the following code?

```python
L = ["we", "were", "here", "together"]

for i in range(3):
    print(L[i])
```

- **A.** we were here together
- **B.** we were here
- **C.** we were
- **D.** we

<details><summary>Answer</summary>

**B**. `range(3)` gives i = 0, 1, 2, so it prints `L[0]`, `L[1]`, `L[2]`: `we were here`.

</details>

**`2022-jan/w03/q05`** What will be the value of list L?

```python
L = []

for i in range(5):
    if (i%2 == 0):
        L.append("Even")
    else:
        L.append("Odd")

print(L)
```

- **A.** ['Even', 'Odd', 'Even', 'Odd']
- **B.** ['Even', 'Odd', 'Even', 'Odd', 'Even', ‘Odd’]
- **C.** ['Even', 'Odd', 'Even', ‘Even', 'Even']
- **D.** ['Even', 'Odd', 'Even', 'Odd', 'Even']

<details><summary>Answer</summary>

**D**. For i = 0 to 4, even `i` appends `Even` and odd `i` appends `Odd`: Even, Odd, Even, Odd, Even.

</details>

**`2022-jan/w03/q07`** What does the following code represent?

```python
a = int(input("Enter number 1"))
b = int(input("Enter number 2"))

while(1):

    if(a%b == 0):
        print("Wow...")
        break

    else:
        print("If you want to continue press 1 else 0")
        choice = int(input())

        if(choice == 1):
            b = int(input("Enter second number again"))

        if(choice == 0):
            break
```

- **A.** Checks if a is divisible by b.
- **B.** Checks if b is divisible by a.
- **C.** Checks if a and b are multiples of 5.
- **D.** None of the above.

<details><summary>Answer</summary>

**A**. `a%b == 0` means `a` divides evenly by `b`, so the code checks whether `a` is divisible by `b`.

</details>

**`2022-jan/w03/q08`** Suppose there exists a file named file.txt. What the following code will do?

```python
with open('file.txt','r') as file:
    print(file.read())
    file.write('hey there!!')
file.close()
```

- **A.** Print whatever is there in the file and add hey there.
- **B.** Throws an error in the end as the file is not opened in writable mode.
- **C.** Throws an error in the end as the file is not opened in readable mode.
- **D.** No error will be thrown and the code will work fine.

<details><summary>Answer</summary>

**B**. The file is opened in `'r'` mode. Reading and printing works, but `file.write(...)` then fails because a read-only file cannot be written.

</details>

**`2022-jan/w03/q09`** Suppose there is an empty file named file.txt. What will be the output of the following code?

```python
with open('file.txt','w') as file:
    file.write('hey there!!')
file.close()

with open('file.txt', 'a') as file:
    file.write('writing this file again')

with open('file.txt', 'r') as file:
    print(file.read())
```

- **A.** writing this file again
- **B.** hey there!!
- **C.** hey there!!writing this file again
- **D.** Throws an error

<details><summary>Answer</summary>

**C**. `'w'` writes `hey there!!`, then `'a'` adds `writing this file again` at the end. Reading prints both together: `hey there!!writing this file again`.

</details>

**`2022-jan/w03/q10`** What will be the output of the following code?

```python
with open('file.txt','w') as file:
    file.write('1000111011')

file.close()

with open('file.txt','r') as file:
    L = list(file.read())

file.close()

for i in range(len(L)):
    if(i%2 == 0  and L[i]=='0'):
        L[i]='1'
    if(i%2 != 0 and L[i]=='1'):
        L[i]='0'

print(L)
```

- **A.** Alternative 1’s and 0’s respectively
- **B.** Alternative 0’s and 1’s respectively.
- **C.** All Zeroes towards left and ones towards the right.
- **D.** All ones towards the left and zeroes towards the right.

<details><summary>Answer</summary>

**A**. The file holds `1000111011`, split into characters. Even positions holding `0` become `1`, and odd positions holding `1` become `0`. The result alternates 1, 0, 1, 0, …

</details>

**`2021-jul/w04/q04`** What will the output of the following program be?

```python
l=[31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a=1900
if(a%4==0 and a%100!=0 or a%400==0):
    l.insert(1,29)
else:
    l.insert(1,28)

print("In the year 1900, february has",l[1],"days")
```

- **A.** In the year 1900, february has 28 days
- **B.** In the year 1900, february has 29 days
- **C.** In the year 1900, february has 0 days
- **D.** It will throw an error

<details><summary>Answer</summary>

**A**. `1900 % 4 == 0` is true, but `1900 % 100 != 0` is false, and `1900 % 400` is not 0. So the condition fails and the code inserts 28 at index 1, giving 28 days.

</details>

**`2021-jul/w04/q05`** Consider today's date to be 06-06-2021 and the day after tomorrow is tuesday.. What will be the output of the following program?

```python
import datetime
x=datetime.datetime.now()
print(x.strftime("%W"))
print(x.strftime("%w"))
```

- **A.**

  ```python
  22
0
  ```

- **B.**

  ```python
  0
22
  ```

- **C.**

  ```python
  Monday
29
  ```

- **D.**

  ```python
  29
Tuesday
  ```


<details><summary>Answer</summary>

**A**. `%W` is the week number of the year, which is 22 for 6 June 2021. `%w` is the weekday as a number from 0 (Sunday), and 6 June 2021 is a Sunday, so it prints 22 then 0.

</details>

**`2021-jul/w04/q06`** What will the following program do?

```python
a=input("Enter any positive number\n")
p=int(a)
sum=0
while(p!=0):
    sum=sum+p%10
    p//=10

print(sum)
```

- **A.** Print the sum of digits of a given number
- **B.** Print the number by dividing it by 10
- **C.** Print the reverse of the number
- **D.** None of the above

<details><summary>Answer</summary>

**A**. The loop takes the last digit with `p%10`, adds it to `sum`, and drops it with `p//=10`, until `p` is 0. So it prints the sum of the digits.

</details>

**`2021-jul/w04/q09`** What does the following code snippet in python compute?

```python
a=0
b=1
print(a,end=" ")
for i in range(0,15,1):
    print(b,end=" ")
    a,b=b,a+b
```

- **A.** Factorial of numbers from 0 to 15
- **B.** Fibonacci series
- **C.** None
- **D.** Sequence of numbers from 0 to 15

<details><summary>Answer</summary>

**B**. `a, b = b, a + b` makes each new number the sum of the previous two, starting 0, 1. It prints 0 1 1 2 3 5 8 …, the Fibonacci series.

</details>

**`2022-jan/w04/q03`** What the following code will do?

```python
L1 = ['harry potter', 'matrix', 'spiderman', 'avengers', 'john wick']
L2= ['drishyam', 'spiderman', 'bahubali', 'dhoom', 'race', 'matrix']

L = []


for i in range(len(L1)):

    flag = 0

    for j in range(len(L2)):

        if(L1[i] == L2[j]):
            flag = 1
            break
        else:
            flag = 0

    if(flag == 0):
        L.append(L1[i])

print(L)
```

- **A.** Print unique movies of list L1
- **B.** Print unique movies of list L2
- **C.** Print common movies of lists L1 and L2
- **D.** Shows an error

<details><summary>Answer</summary>

**A**. For each movie in `L1` the inner loop looks for it in `L2`. If it is found, `flag` becomes 1 and it is skipped; otherwise it is appended to `L`. So `L` holds the movies that are in `L1` only.

</details>

**`2022-jan/w04/q04`** What will be the output of the following code?

```python
import random

L = ['harry potter', 'matrix', 'spiderman', 'terminator', 'karate ki...
# (the screenshot cuts this line off after 'karate ki')

movie = random.choice(L)

count = 0

for character in movie:

    if(character == 'a' or character == 'A'):
        count = count+1

    elif(character == 'e' or character == 'E'):
        count = count+1

    elif(character == 'i' or character == 'I'):
        count = count+1

    elif(character == 'o' or character == 'O'):
        count = count+1

    elif(character == 'U' or character == 'u'):
        count = count+1

print(count, movie)
```

- **A.** Displays the number of consonants and the name of the movie.
- **B.** Displays the number of letters and the name of the movie.
- **C.** Displays the number of vowels and the name of the movie.
- **D.** Displays the number of special characters and the name of the movie.

<details><summary>Answer</summary>

**C**. The loop adds 1 to `count` for each `a`, `e`, `i`, `o` or `u` (any case) in the movie name. It then prints that count with the name, so it shows the number of vowels.

</details>

**`2022-jan/w04/q08`** What's the output of the following code?

```python
print([i**2 for i in range(10) if i%2 == 0])
```

- **A.** List of squares of even numbers.
- **B.** List of squares of numbers between 0-10.
- **C.** List of squares of numbers between 0-9.
- **D.** List of squares of odd numbers.

<details><summary>Answer</summary>

**A**. The comprehension squares every `i` from 0 to 9 for which `i%2 == 0`, so it squares the even numbers: `[0, 4, 16, 36, 64]`.

</details>

**`2021-jul/w05/q01`** What will the output of the following program be?

```python
dict1={
    "ID":"0121",
    "Name":"zzz"
}
dict2={
    "Name":"ZZZ"
}

dict2.update({"ID":"0121"})
if(dict1==dict2):
    print("They are equal")
else:
    print("They are not equal")
```

- **A.** They are equal
- **B.** They are not equal
- **C.** It will throw an error

<details><summary>Answer</summary>

**B**. The first dictionary has `"Name": "zzz"`, the second `"Name": "ZZZ"`. Strings differ by case, so the dictionaries are not equal and the `else` branch prints `They are not equal`.

</details>

**`2021-jul/w05/q02`** What will the output of the following program be?

```python
dictA={
    "name":"Joy of computing",
    "Length":"12 Weeks",
    "Professor_name":"Dr Sudarshan Iyengar",
    "Language":"Python"
}
dictB={
}
dictB.update(dictA)
for x,y in dictB.items():
    print(x,y)
```

- **A.**

  ```python
  name Joy of computing
Length 12 Weeks
Professor_name Dr Sudarshan Iyengar
Language Python
  ```

- **B.** {'name': 'Joy of computing', 'Length': Sudarshan Iyengar', 'Language': 'Python'}
- **C.** It will throw an error
- **D.** dictB will be empty

<details><summary>Answer</summary>

**A**. `dictB.update(dictA)` copies all four items of `dictA` into the empty `dictB`. The loop then prints each key and value separated by a space.

</details>

**`2021-jul/w05/q07`** Which of these following statements are true with respect to the program below?

```python
import random
a=[1,2,3,4,5,6]
sum=0
for i in range (0,2):
    sum=sum+random.choice(a)
print(sum)
```

- **A.** The value of sum will always be between 1 and 11
- **B.** The value of sum will be from 2 to 12
- **C.** The value of sum will be within 12
- **D.** The maximum value of sum cannot exceed 6

<details><summary>Answer</summary>

**B**. The loop runs twice and adds `random.choice(a)`, a number from 1 to 6, each time. So `sum` is the total of two dice, from 2 to 12.

</details>

**`2021-jul/w05/q10`** Will the following program give an error?

```python
a=["1", "2", "3", "4", "5"]
fun=len
print(fun(a))
```

- **A.** Yes
- **B.** No

<details><summary>Answer</summary>

**B**. `fun = len` gives the function `len` a second name. `fun(a)` then calls `len(a)` and prints 5. There is no error.

</details>

**`2022-jan/w05/q04`** What will be the output of the following code?

```python
d = {'a': 20, 'b':'30'}

print(d.values())
```

- **A.** 20 ‘30’
- **B.** ‘20’ ‘30’
- **C.** 20 30
- **D.** a b

<details><summary>Answer</summary>

**A**. `d.values()` returns the values `20` and `'30'`. The first is an integer and the second a string, so Python shows them as `20, '30'`.

</details>

**`2022-jan/w05/q06`** What will be the output of the following code?

```python
import string


bags = {}
name = string.ascii_letters

for i in range(20):
    bags[name[i]] = 0

print(bags)
```

- **A.** Creates a dictionary with keys in range 0-19 and values 0
- **B.** Creates a dictionary with keys in range a-t and values 0.
- **C.** Creates a dictionary with keys in range a-z and values in range 0-19.
- **D.** Creates a dictionary with keys in range a-t and values in range 0-19.

<details><summary>Answer</summary>

**B**. The loop takes the first 20 letters of `string.ascii_letters` (a to t) as keys and sets each value to 0. So it makes a dictionary with keys a–t and value 0.

</details>

**`2022-jan/w05/q07`** What does the following code mimics?

```python
import string
import random

bags = {}
name = string.ascii_letters

for i in range(20):
    bags[name[i]] = 0

for i in range(1000):
    key = random.choice(list(bags.keys()))
    bags[key] = bags[key] + 1
```

- **A.** Distribute 1000 marbles evenly in every bag.
- **B.** Distribute 500 marbles randomly in every bag.
- **C.** Distribute 1000 marbles randomly in every bag.
- **D.** Throws an error.

<details><summary>Answer</summary>

**C**. It makes 20 bags that start at 0, then runs 1000 times: pick a random bag and add 1. So it spreads 1000 marbles randomly among the bags.

</details>

**`2022-jan/w05/q10`** What will be the output of the following code?

```python
def test(L):

    for i in range(len(L)-1):

        for j in range(len(L)-1):

            if(L[j] < L[j+1]):

                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp

    print(L[0])
```

- **A.** The first element of the initial list.
- **B.** The largest element of the list.
- **C.** The smallest element of the list.
- **D.** Throws an error.

<details><summary>Answer</summary>

**B**. The nested loop swaps `L[j]` and `L[j+1]` when `L[j] < L[j+1]`. That pushes smaller items to the end, so the list ends sorted in descending order and `L[0]` is the largest element.

</details>

**`2021-jan/w06/q07`** Which of the following is the optimal code among the given codes using recursive binary search?

- **A.**

  ```python
  def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1
  ```

- **B.**

  ```python
  def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
  ```

- **C.**

  ```python
  def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
  ```

- **D.**

  ```python
  def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            return binary_search(arr, low, mid, x)
        else:
            return binary_search(arr, mid, high, x)
    else:
        return -1
  ```


<details><summary>Answer</summary>

**B**

</details>

**`2021-jul/w06/q02`** What operation will the following program do?

```python
import string
s="hello"
n=""
for i in range(len(s)):
    c=int(ord(s[i])-26)
    n=n+chr(c)
print(n)
```

- **A.** Shift the letter by 6 to the right and then print the capital of that letter.
- **B.** Shift the letter by 6 to the left and then print the capital of that letter.
- **C.** Shift the letter by 6 to the right and then print the small letter.
- **D.** Shift the letter by 6 to the left and then print the small letter.

<details><summary>Answer</summary>

**A**. The code subtracts 26 from each lowercase letter's code. Lowercase letters are 32 codes above their capitals, so this lands on the capital letter six places later: `h` gives `N`. The letter is shifted 6 to the right and printed as a capital.

</details>

**`2021-jul/w06/q03`** What is the output of the following program?

```python
import string
s="hello, and welcome to joy of computing course"
if(s.capitalize()==s[0:1].upper()+s[1:len(s)]):
    print("True")
else:
    print("False")
```

- **A.** False
- **B.** True

<details><summary>Answer</summary>

**B**. `s.capitalize()` makes the first letter capital and the rest lowercase. `s[0:1].upper() + s[1:len(s)]` also capitalises the first letter. `s` is already lowercase after the first letter, so the two are equal and it prints `True`.

</details>

**`2021-jul/w06/q04`** What will be the output of the following program?

```python
import string
s="hello, and welcome to joy of computing course"
print(s[::2].replace("e","l"))
```

- **A.** ll,adwlolt o fcmuigcus
- **B.** hlo n lcm ojyo optn orl
- **C.** hello, and welcome to jy of computing course
- **D.** It will show an error

<details><summary>Answer</summary>

**B**. `s[::2]` keeps every second character: `hlo n lcm ojyo optn orl`. That text has no `e`, so `.replace("e", "l")` changes nothing.

</details>

**`2021-jul/w06/q06`** What is the output of the following program? ( Assuming that k and n are any 2 positive numbers)

```python
def fun(k,n):
    if(n==0):
        return 1
    else:
        return(k*fun(k,n-1))

print(fun(k,n))
```

- **A.** It will find the value of k raised to the power of k
- **B.** It will find the value of n raised to the power of k
- **C.** It will find the value of k raised to the power of n
- **D.** It will find the value of n raised to the power of n

<details><summary>Answer</summary>

**C**. `fun(k, n)` returns 1 when `n == 0`, and `k * fun(k, n-1)` otherwise. So it multiplies `k` by itself `n` times: k to the power n.

</details>

**`2021-jul/w06/q07`** The output of the following program is as follows [[ 1 4 13] [ 2 2 9] [ 3 3 6]] What should be written in the empty blank in the following program to get the above desired output?

```python
import numpy
arr=numpy.array([[1,2,3],[4,2,3,],[13,9,6]])
print(____________)
```

- **A.** numpy.transpose(arr)
- **B.** arr.transpose( )
- **C.** Either a or b options can be used
- **D.** arr.reverse( )

<details><summary>Answer</summary>

**C**. The array printed is the original with rows turned into columns, which is the transpose. Both `numpy.transpose(arr)` and `arr.transpose()` give it.

</details>

**`2022-jan/w06/q02`** What will be the output of the following code if the input is ‘The Joy OF Computing’ ?

```python
import string

def test(word):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    new_word = ''

    for ch in word:
        if(ch in lower):
            index = lower.index(ch)
            new_word = new_word + lower[(index+2) % 26]

        elif(ch in upper):
            index = upper.index(ch)
            new_word = new_word + upper[(index+3) % 26]

        else:
            new_word = new_word + ch

    return new_word

print(test('The Joy OF Computing'))
```

- **A.** Wjg Mqa Rh Fqorwvkpi
- **B.** vjg lqa eh eqorwvkpi
- **C.** Wjg Mqa RI Fqorwvkpi
- **D.** vjg Mqa RI Fqorwvkpi

<details><summary>Answer</summary>

**C**. Lowercase letters move 2 places on, capitals move 3: `The Joy OF Computing` becomes `Wjg Mqa RI Fqorwvkpi`.

</details>

**`2022-jan/w06/q05`** What will be the output of the following program?

```python
def recursive(L):

    if(len(L) == 1):
        return L[0]

    return L[0] + recursive(L[1:])

print(recursive([1,2,3,4,5,6,7,8,9,10]))
```

- **A.** 55
- **B.** 45
- **C.** Infinite loop
- **D.** 50

<details><summary>Answer</summary>

**A**. `recursive(L)` returns the first item plus `recursive` of the rest, and the last item when one is left. So it adds 1 + 2 + … + 10 = `55`.

</details>

**`2022-jan/w06/q08`** What the following code will do?

```python
def recursive(L):

    if(len(L) <= 6):
        return L[-1]

    return L[-1] * recursive(L[:-1])
```

- **A.** Returns product of elements from 5th index onwards.
- **B.** Returns product of elements from 1st to 5th index.
- **C.** Returns product of elements from 6th index onwards.
- **D.** Returns product of elements from 4th index onwards.

<details><summary>Answer</summary>

**A**. The function stops when 6 or fewer items remain and returns the last one. Otherwise it multiplies the last item by the result for the list without it. So it multiplies from index 5 (the 6th item) to the end.

</details>

**`2022-jul/w06/q05`** What's the correct code for Binary search?

```python
# The only source is a screen recording; each option is partly cut off.
# Option 1 (visible part)
def Binary(L,find, start, end):

    mid = int((start+end)/2)

    if(start < end):
        if(L[end] == find):
            return end
        else:
            return -100


    if(L[mid] == find):
        return mid

    elif(find > L[mid]):
        return Binary(L, find, mid + 1, end)
    # (rest not visible)

# Option 2
def Binary(L,find, start, end):

    mid = int((start+end)/2)

    if(start == end):
        if(L[end] == find):
            return end
        else:
            return -100


    if(L[mid] == find):
        return mid

    elif(find > L[mid]):
        return Binary(L, find, start, mid - 1)

    else:
        return Binary(L, find, mid + 1, end)

# Option 3 (the one selected in the recording)
def Binary(L,find, start, end):

    mid = int((start+end)/2)

    if(start == end):
        if(L[end] == find):
            return end
        else:
            return -100


    if(L[mid] == find):
        return mid

    elif(find > L[mid]):
        return Binary(L, find, mid + 1, end)

    else:
        return Binary(L, find, start, mid-1)
```

- **A.** Option 1
- **B.** Option 2
- **C.** Option 3
- **D.** Option 4

<details><summary>Answer</summary>

**C**

</details>

**`2021-jul/w07/q01`** What will the following program do?

```python
from PIL import Image
im=Image.open('snakesandladders.png')
im.show()
im.save('snakeimage.png')
```

- **A.** Rename the snakesandladders.png file as snakeimage.png
- **B.** Creates a new file called snakeimage.png
- **C.** Creates a new file called snakeimage.png with the same content as in the snakesandladders.png
- **D.** Invalid operation

<details><summary>Answer</summary>

**C**. `Image.open` loads the picture, `im.show()` displays it, and `im.save('snakeimage.png')` writes a new file with the same content.

</details>

**`2021-jul/w07/q04`** What will be the output of the following program?

```python
R = 4
C = 5

def Traversal(m, n, a):
    k = 0
    l = 0
    stk = []

    while (k <= m and l <= n):
        for i in range(l, n + 1):
            stk.append(a[k][i])
        k += 1
        for i in range(k, m + 1):
            stk.append(a[i][n])
        n -= 1
        if ( k <= m):
            for i in range(n, l - 1, -1):
                stk.append(a[m][i])
            m -= 1
        if (l <= n):
            for i in range(m, k - 1, -1):
                stk.append(a[i][l])
            l += 1

    while len(stk) != 0:
        print(str(stk[-1]), end = " ")
        stk.pop()
mat = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]

Traversal(R - 1, C - 1, mat)
```

- **A.** 12 13 14 9 8 7 6 11 16 17 18 19 20 15 10 5 4 3 2 1
- **B.** 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
- **C.** 1 6 11 16 17 18 19 20 15 10 5 4 3 2 7 12 13 14 9 8
- **D.** 13 12 7 8 9 14 19 18 17 16 11 6 1 2 3 4 5 10 15 20

<details><summary>Answer</summary>

**A**. `Traversal` collects the spiral order of the 4 × 5 matrix on a stack: 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12. It then prints from the top of the stack, so the output is that order reversed.

</details>

**`2021-jul/w07/q06`** What is the output of the following program?

```python
import turtle
tr=turtle.Turtle()

for i in range (9):
    tr.forward(90)
    tr.left(45)
```

- **A.** Octagon
- **B.** Pentagon
- **C.** Nonagon
- **D.** Hexagon

<details><summary>Answer</summary>

**A**. The turtle moves forward 90 and turns left 45°. Eight turns of 45° make a full 360°, so the path is an octagon (the ninth step repeats the first side).

</details>

**`2022-jul/w07/q09`** Which of the following code will draw a star?

```python
# The only source is a screen recording; option 2 is partly hidden.
# Option 1
import turtle
mypen = turtle.Turtle()

for i in range(3):
    mypen.forward(50)
    mypen.right(144)

turtle.done()

# Option 2 (lines 3-4 hidden; line 5 reads mypen.forward(100))
import turtle
mypen = turtle.Turtle()
...
    mypen.forward(100)
    mypen.right(144)

turtle.done()

# Option 3 (the one selected in the recording)
import turtle
mypen = turtle.Turtle()

for i in range(6):
    mypen.forward(50)
    mypen.right(144)

turtle.done()

# Option 4
import turtle
mypen = turtle.Turtle()

for i in range(6):
    mypen.forward(100)
    mypen.right(60)

turtle.done()
```

- **A.** Option 1
- **B.** Option 2
- **C.** Option 3
- **D.** Option 4

<details><summary>Answer</summary>

**C**. Option 3 loops 6 times, moving 50 and turning 144°. A 144° turn traces a five-pointed star, and six moves are enough to close it.

</details>

**`2021-jul/w08/q03`** What is the output of the following program?

```python
t=(1 , 2 , 3)
(a, b, c)=t
print(a,b,c)
```

- **A.** 1 2 3
- **B.** Error
- **C.** a b c
- **D.** t t t

<details><summary>Answer</summary>

**A**. `(a, b, c) = t` unpacks the tuple, so `a = 1`, `b = 2`, `c = 3`. `print(a, b, c)` prints `1 2 3`.

</details>

**`2021-jul/w08/q04`** What will be the output of the following program?

```python
import random
i=random. randint(1,100)
if(i%3==0):
    print(i)
```

- **A.** It generates a random number and prints it
- **B.** It generates a random number and doesn't do anything
- **C.** It will generate a random number and prints it
- **D.** It will generate a random number and prints it only if its a multiple of 3

<details><summary>Answer</summary>

**D**. The program picks a random number `i` from 1 to 100 and prints it only when `i % 3 == 0`, that is, only when it is a multiple of 3.

</details>

**`2021-jul/w08/q06`** What is the output of the following program?

```python
import matplotlib.pyplot as plt
x=[]
y=[]
for i in range (1,11):
    x.append(i)
    y.append(i)

x.reverse()
print(x)
print (y)
plt.plot(y,x)
plt.show()
```

- **A.** Linear graph with positive slope
- **B.** Linear graph with negative slope
- **C.** Non linear graph with positive slope
- **D.** Non linear graph with negative slope

<details><summary>Answer</summary>

**B**. `x` becomes `[10, 9, ..., 1]` after `reverse()` and `y` stays `[1, ..., 10]`. `plt.plot(y, x)` draws `x` against `y`: as `y` goes up, `x` goes down by 1, a straight line with negative slope.

</details>

**`2021-jul/w08/q09`** What will the output of the following program be?

```python
a=input()
if(a==a[::-1]):
    print(a)
```

- **A.** Prints the reverse of string a
- **B.** Prints the string only if its an anagram
- **C.** Prints the string only if its a palindrome
- **D.** Error message

<details><summary>Answer</summary>

**C**. `a[::-1]` is `a` reversed, so `a == a[::-1]` is true exactly when `a` is a palindrome. Only then does `print(a)` run.

</details>

**`2021-jul/w09/q03`** What is the output of the following program?

```python
import networkx as nx
g=nx.Graph()
g.add_edge('a','b', weight=.1)
g.add_edge('b','c',weight=1.5)
g.add_edge('a','c',weight=1.0)
g.add_edge('c','d',weight=2.2)
print (nx.shortest_path(g,'b','d'))
```

- **A.** ['b', 'c', 'd']
- **B.** ['b', 'a', 'c', 'd']
- **C.** It will give an error
- **D.** ['d', 'a', 'c', 'b']

<details><summary>Answer</summary>

**A**. Without a `weight=` argument `shortest_path` counts edges, so from `b` to `d` the shortest path is `b → c → d`: `['b', 'c', 'd']`.

</details>

**`2021-jul/w09/q10`** What is the output of the following program?

```python
var="hello PYTHON"
print(var.casefold())
```

- **A.** Hello python
- **B.** HELLO PYTHON
- **C.** HELLO python
- **D.** hello python

<details><summary>Answer</summary>

**D**. `casefold()` makes the whole string lowercase, so `"hello PYTHON"` becomes `hello python`.

</details>

**`2021-jan/w10/q08`** Which of the following code snippet will print transpose of the matrix a?

- **A.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(a.Tran())
  ```

- **B.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(a.Transpose())
  ```

- **C.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(a.Trans)
  ```

- **D.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(a.T)
  ```


<details><summary>Answer</summary>

**D**

</details>

**`2021-jan/w10/q09`** Which of the following will print column sum of the matrix a?

- **A.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(np.sum(a,axis=0))
  ```

- **B.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(np.sum(a,axis=1))
  ```

- **C.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(np.sum(a.col))
  ```

- **D.**

  ```python
  import numpy as np
a = np.array([[1,2],[3,4]])
print(np.colsum(a))
  ```


<details><summary>Answer</summary>

**A**

</details>

**`2021-jul/w10/q04`** What is the output of the following program ?

```python
import numpy as np
arr=np.array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
print(arr[1,-5])
```

- **A.** 5
- **B.** 2
- **C.** 2
- **D.** Error message

<details><summary>Answer</summary>

**A**. `arr[1, -5]` is row 1, which is `[6, 5, 4, 3, 2, 1]`, at position -5, the fifth from the end, so the value 5.

</details>

**`2021-jul/w10/q05`** What is the output of the following program?

```python
a = ['a','e','i','o','u','A','E','I','O','U',' ']
b = 'Hello have a good day'
for i in b:
    if i not in a:
        b = b[:b.index(i)] + b[b.index(i)+1:]
print(b)
```

- **A.** eo ae a oo a
- **B.** oe ae a oo a
- **C.** ae ae a oo a
- **D.** None of the above

<details><summary>Answer</summary>

**A**. The loop goes over the letters of the original `b`. Each time the letter is not in the list `a` (so it is a consonant), the first occurrence of that letter is removed from the changing `b`. This removes all the consonants of `Hello have a good day` and leaves `eo ae a oo a`.

</details>

**`2021-jul/w10/q06`** What is the output of the following program?

```python
def ring(str):
    result = ""
    for i in range(len(str)):
        if i%2==0:
            result = result + str[i]
    return result

print(ring("Welcome to Joy of Computing Course"))
```

- **A.** Wloet o fCmuigCus
- **B.** ecm t Jyo CmuigCus
- **C.** Welcome to Joy of Computing Course
- **D.** None of the above

<details><summary>Answer</summary>

**A**. The function adds the character at every even position (0, 2, 4, ...) of the string to `result`. For `Welcome to Joy of Computing Course` that gives `Wloet o fCmuigCus`.

</details>

**`2021-jul/w10/q07`** What will the following function in the program do?

```python
def ring(text):
    for line in text.split("\n"):
        return " ".join(line.split()[::-1])
```

- **A.** Reverse all the strings in the sentence
- **B.** Reverse the sentence
- **C.** Reverse the first word of the sentence.
- **D.** None of the above

<details><summary>Answer</summary>

**B**. `text.split('\n')` gives the lines, and the function returns on the first line: it splits the line into words, reverses the list of words with `[::-1]` and joins them back with spaces. So it reverses the order of the words in the sentence.

</details>

**`2021-jul/w10/q09`** What will the following program print?

```python
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
```

- **A.** We cannot reshape the array.
- **B.**

  ```python
  [[ 1 2 3]  ✅
[ 4 5 6]
[ 7 8 9]
[10 11 12]]
  ```

- **C.** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

<details><summary>Answer</summary>

**B**. `reshape(4, 3)` rearranges the 12 numbers into 4 rows of 3, so the print shows `[[1 2 3] [4 5 6] [7 8 9] [10 11 12]]`.

</details>

**`2021-jul/w10/q10`** What is the output of the following program?

```python
import numpy as np
a = np.array([1,2,3,5,8])
b = np.array([0,3,4,2,1])
c = a + b
c = c*a
print (c[2])
```

- **A.** 7
- **B.** 12
- **C.** 10
- **D.** 21

<details><summary>Answer</summary>

**D**. `a + b` is `[1, 5, 7, 7, 9]`, and `c * a` multiplies item by item to give `[1, 10, 21, 35, 72]`. `c[2]` is 21.

</details>

---

## E2. 2026-jul case-study programs

Each case below gives the story, the program exactly as printed (line numbers included, since the questions refer to them) and every question on it.

### `2026-jul/w02/q06`–`q10`: Ordering Food at a School Cafeteria

Ordering Food at a School Cafeteria A school cafeteria has introduced a self-service ordering kiosk. Students enter their name and the food item they would like to order. The kiosk stores this information and displays a confirmation message. Before the order is finalized, one student changes their order from Sandwich to Pasta. The kiosk updates the stored value and prints the final order receipt. The Python program running on the kiosk is shown below.

```python
1. print("Welcome to the School Cafeteria!")
2. customer = input("Enter your name: ")
3. order = input("Enter your food item: ")
4. print("Hello", customer)
5. print("You ordered", order)
6. order = "Pasta"
7. print("Updated Order:", order)
8. print("Thank you for your order,", customer)
```

**`2026-jul/w02/q06`** Which line collects the name of the customer?

- **A.** Line 1
- **B.** Line 2
- **C.** Line 3
- **D.** Line 8

<details><summary>Answer</summary>

**B**. Line 2 is `customer = input("Enter your name: ")`; `input()` reads the name the user types.

</details>

**`2026-jul/w02/q07`** A student initially enters Sandwich as the food item. What will be displayed in Line 7?

- **A.** Sandwich
- **B.** Sandwich Pasta
- **C.** Pasta
- **D.** No food item will be displayed.

<details><summary>Answer</summary>

**C**. Line 6 sets `order` to `"Pasta"`, replacing `Sandwich`. Line 7 then prints `Updated Order: Pasta`.

</details>

**`2026-jul/w02/q08`** Which variable stores the name of the customer throughout the program?

- **A.** order
- **B.** customer
- **C.** input
- **D.** print

<details><summary>Answer</summary>

**B**. Line 2 stores the typed name in the variable `customer`, and lines 4 and 8 use it.

</details>

**`2026-jul/w02/q09`** If the customer enters Neha as the name, what will be displayed in Line 8?

- **A.** Thank you for your order, customer
- **B.** Thank you for your order, Neha
- **C.** Thank you for your order, Pasta
- **D.** Thank you for your order

<details><summary>Answer</summary>

**B**. `customer` holds `Neha`, so line 8 prints `Thank you for your order, Neha`.

</details>

**`2026-jul/w02/q10`** Why is the variable order updated in Line 6 instead of creating another variable?

- **A.** A variable can only store one value at a time, and the latest value replaces the previous one.
- **B.** Python does not allow more than one variable in a program.
- **C.** The original value cannot be changed.
- **D.** Updating a variable permanently changes all future programs.

<details><summary>Answer</summary>

**A**. A variable holds one value at a time, and assigning a new value replaces the old one. So line 6 reuses `order` and the program uses the latest value.

</details>

### `2026-jul/w02/q16`–`q20`: Morning Exercise Counter

Morning Exercise Counter A school has installed a digital exercise board in the playground. Every morning, the board displays the number of jumping jacks students should perform. It starts from 1 and continues until the teacher decides to stop the session. The board repeatedly displays the next exercise number as long as the teacher chooses to continue. The following Python program is used for the exercise board.

```python
1. print("Morning Exercise Begins")
2. count = 1
3. continue_session = 1
4.
5. while continue_session == 1:
6.     print("Do Exercise", count)
7.     count = count + 1
8.     continue_session = int(input("Continue? (1 = Yes, 0 = No): "))
9.
10. print("Exercise Session Over")
```

**`2026-jul/w02/q16`** What is displayed first when the program starts?

- **A.** Do Exercise 1
- **B.** Continue? (1 = Yes, 0 = No)
- **C.** Morning Exercise Begins
- **D.** Exercise Session Over

<details><summary>Answer</summary>

**C**. Line 1 runs before the loop, so the first thing displayed is `Morning Exercise Begins`.

</details>

**`2026-jul/w02/q17`** The teacher enters 1 three times and then enters 0. Which exercise numbers will be displayed?

- **A.** 1, 2, 3
- **B.** 1, 2, 3, 4
- **C.** 0, 1, 2, 3
- **D.** 2, 3, 4

<details><summary>Answer</summary>

**B**. It prints `Do Exercise 1`, then each `1` entered makes it print the next number. Three 1s give exercises 2, 3 and 4, and the `0` stops the loop. So the numbers are 1, 2, 3, 4.

</details>

**`2026-jul/w02/q18`** Which statements about the program are correct? (Select all that apply.)

- **A.** The value of count increases by 1 during each repetition.
- **B.** The while loop repeats only while continue_session is equal to 1.
- **C.** The message "Exercise Session Over" is displayed after the loop ends.
- **D.** The value of count decreases during each repetition.

<details><summary>Answer</summary>

**A, B, C**. `count = count + 1` raises `count` by 1 on every pass. The `while` test is `continue_session == 1`. Line 10 runs after the loop ends. `count` never goes down.

</details>

**`2026-jul/w02/q19`** Why is a while loop used in this program?

- **A.** Because the number of repetitions depends on the teacher's choice.
- **B.** Because the program always repeats exactly 10 times.
- **C.** Because Python cannot print numbers without a while loop.
- **D.** Because variables cannot be used inside a for loop.

<details><summary>Answer</summary>

**A**. The teacher decides when to stop, so the number of repetitions is not known in advance. A `while` loop keeps going while its condition holds.

</details>

**`2026-jul/w02/q20`** Which of the following statements correctly compare for loops and while loops? (Select all that apply.)

- **A.** A for loop is useful when the number of repetitions is known in advance.
- **B.** A while loop continues until its condition becomes false.
- **C.** A while loop always executes exactly 10 times.
- **D.** Both for and while loops are used to repeat tasks.

<details><summary>Answer</summary>

**A, B, D**. A `for` loop suits a known number of repetitions. A `while` loop runs until its condition becomes false. Both repeat tasks. A `while` loop may run any number of times.

</details>

### `2026-jul/w03/q06`–`q10`: Managing Participants for a Workshop

Managing Participants for a Workshop A training institute maintains a list of participant names for a Python workshop. As registrations are received, new participants are added to the list. A late VIP registration is inserted at a specific position. Before printing attendance sheets, the participant names are arranged alphabetically. Finally, only a selected group of participants is displayed for one workshop batch. Study the following program and answer the questions.

```python
1. participants = ["Riya", "Aman", "Kiran", "Neha", "Aman"]
2. participants.append("Sana")
3. participants.insert(1, "Bhavna")
4. participants.sort()
5. batch = participants[1:5]
6. print(participants)
7. print(batch)
```

**`2026-jul/w03/q06`** What will be the output of line 6?

- **A.** ['Aman', 'Aman', 'Bhavna', 'Kiran', 'Neha', 'Riya', 'Sana']
- **B.** ['Riya', 'Bhavna', 'Aman', 'Kiran', 'Neha', 'Aman', 'Sana']
- **C.** ['Aman', 'Bhavna', 'Kiran', 'Neha', 'Riya', 'Sana']
- **D.** ['Bhavna', 'Aman', 'Aman', 'Kiran', 'Neha', 'Riya', 'Sana']

<details><summary>Answer</summary>

**A**. The list starts with 5 names, then `append` adds Sana and `insert(1, ...)` adds Bhavna. `sort()` orders all 7 names alphabetically, with Aman twice, and line 6 prints that list.

</details>

**`2026-jul/w03/q07`** What is stored in the variable batch after line 5?

- **A.** ['Aman', 'Bhavna', 'Kiran', 'Neha']
- **B.** ['Bhavna', 'Kiran', 'Neha', 'Riya']
- **C.** ['Aman', 'Aman', 'Bhavna', 'Kiran']
- **D.** ['Kiran', 'Neha', 'Riya', 'Sana']

<details><summary>Answer</summary>

**A**. After sorting, the list is Aman, Aman, Bhavna, Kiran, Neha, Riya, Sana. `participants[1:5]` takes indexes 1 to 4: Aman, Bhavna, Kiran, Neha.

</details>

**`2026-jul/w03/q08`** Which of the following statements are true after line 4?

- **A.** The participant Sana has been added to the list.
- **B.** The name Aman appears twice.
- **C.** The list contains 6 participants.
- **D.** The names are arranged alphabetically.

<details><summary>Answer</summary>

**A, B, D**. After line 4 the list has 7 names: `append` added Sana, `Aman` is in it twice, and `sort()` arranged the names alphabetically. There are 7 participants, not 6.

</details>

**`2026-jul/w03/q09`** Which line inserts the participant Bhavna at a specific position in the list?

- **A.** Line 1
- **B.** Line 2
- **C.** Line 3
- **D.** Line 5

<details><summary>Answer</summary>

**C**. Line 3, `participants.insert(1, "Bhavna")`, puts Bhavna at index 1, a specific position.

</details>

**`2026-jul/w03/q10`** Which operation is demonstrated by line 5?

- **A.** Appending a new participant
- **B.** Sorting the participant list
- **C.** Counting duplicate names
- **D.** Extracting a portion of the participant list

<details><summary>Answer</summary>

**D**. `participants[1:5]` is slicing: it takes a part of the list and stores it in `batch`.

</details>

### `2026-jul/w04/q11`–`q15`: Building the First Prototype of a Magic Square Generator

Building the First Prototype of a Magic Square Generator A software development team is creating a Python program to generate odd-sized Magic Squares. Rather than implementing the complete algorithm immediately, they decide to build and test the program incrementally. In the first prototype, the program accepts the size of the square (n), creates an n × n matrix initialized with zeros, determines the starting position for the first number using the Magic Square algorithm, places the number 1 at that position, and then displays the matrix for verification. Once this initial step works correctly, the team plans to extend the program to place the remaining numbers by following the movement rules of the algorithm.

```python
n = 3

magic_square = [[0 for j in range(n)] for i in range(n)]

row = n // 2
col = n - 1

magic_square[row][col] = 1

for r in magic_square:
    print(r)
```

**`2026-jul/w04/q11`** Which programming construct is primarily responsible for creating the two-dimensional matrix in the prototype?

- **A.** Nested list comprehension
- **B.** Nested if-else statements
- **C.** Nested while loops
- **D.** Function recursion

<details><summary>Answer</summary>

**A**. `[[0 for j in range(n)] for i in range(n)]` is a nested list comprehension: the inner part builds one row of n zeros and the outer part makes n such rows.

</details>

**`2026-jul/w04/q12`** If the value of n is changed from 3 to 5, which statement remains true without modifying the rest of the program?

- **A.** The number 1 will always be placed in the center of the matrix.
- **B.** The number 1 will always be placed in the middle row of the last column.
- **C.** The matrix will automatically become a valid Magic Square.
- **D.** The program will generate numbers from 1 to 25 automatically.

<details><summary>Answer</summary>

**B**. The code sets `row = n // 2` and `col = n - 1`, so for any odd n the 1 goes in the middle row of the last column. For n = 5 that is row 2, column 4.

</details>

**`2026-jul/w04/q13`** Why is the matrix initialized with zeros instead of leaving it empty?

- **A.** To allow the program to identify cells that have not yet been assigned a value.
- **B.** To ensure that every row initially has the same sum.
- **C.** To improve the speed of printing the matrix.
- **D.** To prevent duplicate numbers from being generated.

<details><summary>Answer</summary>

**A**. Filling the matrix with 0 first lets the program tell empty cells (0) from cells that already hold a number, since the magic square uses 1 and above.

</details>

**`2026-jul/w04/q14`** What is the primary limitation of this prototype compared to the complete Magic Square algorithm?

- **A.** It cannot create matrices larger than 3 × 3.
- **B.** It places only the first number and does not determine positions for the remaining numbers.
- **C.** It cannot display the matrix.
- **D.** It requires recursion to execute.

<details><summary>Answer</summary>

**B**. The prototype creates the matrix and places only the number 1. It has no code yet for the movement rules that position 2, 3, … so it is not yet a magic square.

</details>

**`2026-jul/w04/q15`** Which of the following statements correctly describe the prototype program? (Select all that apply.)

- **A.** It allocates memory for an n × n matrix before placing any numbers.
- **B.** It determines the initial position of the first number using the Magic Square algorithm.
- **C.** It uses nested iteration while creating the matrix.
- **D.** It verifies that every row, column, and diagonal has the same sum.

<details><summary>Answer</summary>

**A, B, C**. The program builds an n × n matrix (nested list comprehension, so nested iteration) and puts the first number at the position given by the algorithm (`row = n // 2`, `col = n - 1`). It never checks sums.

</details>

### `2026-jul/w04/q16`–`q20`: Movie Guessing Game

Movie Guessing Game A movie streaming platform is developing a Movie Guessing Game to improve user engagement. The game randomly selects a movie title from a predefined list and displays a masked version of it, where every alphabetic character is replaced with * while spaces remain visible. The player repeatedly guesses one letter at a time. If the guessed letter is present in the movie title, all its occurrences are revealed. Otherwise, the player is informed that the letter is not present. The game continues until the player successfully reveals the complete movie title.

```python
import random

movies = [
    "THE LION KING",
    "3 IDIOTS",
    "DANGAL",
    "LAGAAN",
    "INTERSTELLAR"
]


def create_question(movie):
    question = ""

    for ch in movie:
        if ch == " ":
            question += " "
        elif ch.isalpha():
            question += "*"
        else:
            question += ch

    return question


def is_present(letter, movie):
    return movie.count(letter) > 0


def unlock(question, movie, letter):
    result = ""

    for i in range(len(movie)):
        if movie[i] == letter:
            result += letter
        else:
            result += question[i]

    return result


movie = random.choice(movies)

question = create_question(movie)

print("Guess the movie:")
print(question)

while question != movie:

    letter = input("Enter a letter: ").upper()

    if is_present(letter, movie):
        question = unlock(question, movie, letter)
        print("Correct!")
    else:
        print("Letter not found.")

    print(question)

print("Congratulations! You guessed the movie.")
```

**`2026-jul/w04/q16`** Which function is responsible for creating the initial masked movie title displayed to the player?

- **A.** unlock()
- **B.** is_present()
- **C.** create_question()
- **D.** random.choice()

<details><summary>Answer</summary>

**C**. `create_question(movie)` loops over the title and appends `*` for each letter, keeping spaces and other characters. That gives the masked title.

</details>

**`2026-jul/w04/q17`** The player enters a letter that is not present in the selected movie title. What happens next?

- **A.** The movie title is selected again.
- **B.** The current masked title remains unchanged, and a message is displayed.
- **C.** The game terminates immediately.
- **D.** All hidden letters are revealed.

<details><summary>Answer</summary>

**B**. When `is_present` is false, the program prints `Letter not found.` and then prints the unchanged masked title. The loop carries on.

</details>

**`2026-jul/w04/q18`** Why does the unlock() function receive both the original movie title and the current masked title as parameters?

- **A.** To compare their lengths before displaying the result.
- **B.** To generate a new random movie title.
- **C.** To reveal only the newly guessed letters while preserving previously revealed letters.
- **D.** To convert the movie title into uppercase.

<details><summary>Answer</summary>

**C**. `unlock` builds a new string: where `movie[i]` equals the guessed letter it writes the letter, otherwise it copies `question[i]`. So it needs both: the title to find matches and the mask to keep earlier reveals.

</details>

**`2026-jul/w04/q19`** Which condition causes the game loop to terminate?

- **A.** The player enters an incorrect letter.
- **B.** All letters in the movie title have been revealed.
- **C.** The player guesses five incorrect letters.
- **D.** The movie list becomes empty.

<details><summary>Answer</summary>

**B**. The loop is `while question != movie`. It ends when the masked title becomes identical to the original, that is, when every letter has been revealed.

</details>

**`2026-jul/w04/q20`** Which of the following statements about the program are correct? (Select all that apply.)

- **A.** random.choice() is used to select one movie title from the list.
- **B.** isalpha() ensures that spaces and non-alphabetic characters are replaced with *.
- **C.** The unlock() function may reveal multiple occurrences of the guessed letter in a single attempt.
- **D.** The player's input is converted to uppercase before it is checked against the movie title.

<details><summary>Answer</summary>

**A, C, D**. `random.choice(movies)` picks one title, the input is made uppercase with `.upper()`, and `unlock` copies the letter into every matching position, so it can reveal several at once. `isalpha()` makes letters `*` and keeps spaces and digits.

</details>

### `2026-jul/w05/q01`–`q05`: Community Library Book Tracker

Community Library Book Tracker A community library keeps track of the number of books borrowed from different categories. At the end of the day, the librarian wants to update the records based on newly borrowed books and determine which category had the highest number of borrowings. Study the following Python program carefully and answer the questions that follow.

```python
1. borrow_count = {
2.     "Fiction": 12,
3.     "Science": 8,
4.     "History": 5,
5.     "Technology": 10
6. }

7. updates = {
8.     "Science": 4,
9.     "History": 2,
10.     "Art": 6
11. }

12. for category, count in updates.items():
13.     if category in borrow_count:
14.         borrow_count[category] += count
15.     else:
16.         borrow_count[category] = count

17. highest = ""
18. max_books = -1

19. for category, count in borrow_count.items():
20.     if count > max_books:
21.         max_books = count
22.         highest = category

23. print(borrow_count)
24. print(highest, max_books)
```

**`2026-jul/w05/q01`** How many key-value pairs are present in borrow_count immediately after the completion of Line 16?

- **A.** 4
- **B.** 5
- **C.** 6
- **D.** 7

<details><summary>Answer</summary>

**B**. `borrow_count` starts with 4 keys. In the loop, Science and History already exist and are added to, and Art is new, so Art is added. That makes 5 keys after line 16.

</details>

**`2026-jul/w05/q02`** Which statement correctly describes the execution of the else block (Lines 15–16)?

- **A.** It executes for every category in updates.
- **B.** It executes only when a category already exists in borrow_count.
- **C.** It executes only when a category is not present in borrow_count.
- **D.** It never executes because all categories already exist.

<details><summary>Answer</summary>

**C**. The `else` belongs to `if category in borrow_count`. It runs only when the category is not yet a key. Here only `Art` is missing, so it runs once.

</details>

**`2026-jul/w05/q03`** Immediately after executing Line 21 for the first time, what is the value of max_books?

- **A.** -1
- **B.** 10
- **C.** 12
- **D.** 7

<details><summary>Answer</summary>

**C**. `max_books` starts at -1. The first item of `borrow_count` is Fiction with 12, and 12 > -1, so line 21 sets `max_books` to `12` at its first execution.

</details>

**`2026-jul/w05/q04`** Which variable stores the largest borrowing count after the program completes execution?

- **A.** highest
- **B.** category
- **C.** count
- **D.** max_books

<details><summary>Answer</summary>

**D**. `max_books` holds the largest count found. `highest` holds the name of that category, and `category` and `count` are the loop variables for the current pair.

</details>

**`2026-jul/w05/q05`** Which of the following statements are correct?

- **A.** The values of "Science" and "History" are increased.
- **B.** The value of "Technology" remains unchanged.
- **C.** Exactly one new key is added to the dictionary.
- **D.** The final dictionary contains fewer keys than the initial dictionary.

<details><summary>Answer</summary>

**A, B, C**. Science goes from 8 to 12 and History from 5 to 7. Technology is not in `updates`, so it stays 10. `Art` is the only new key. The dictionary grows from 4 to 5 keys.

</details>

### `2026-jul/w05/q06`–`q10`: Rock–Paper–Scissors Championship

Rock–Paper–Scissors Championship A coding club is organizing a Rock–Paper–Scissors championship. The choices made by both players are stored in two lists. A dictionary is used to define which move defeats another. The program compares the choices in each round, updates the scores, and declares the overall winner. Study the following program and answer the questions.

```python
1. wins_against = {
2.     "Rock": "Scissors",
3.     "Paper": "Rock",
4.     "Scissors": "Paper"
5. }
6.
7. playerA = ["Rock", "Paper", "Scissors", "Rock", "Paper"]
8. playerB = ["Scissors", "Rock", "Paper", "Rock", "Scissors"]
9.
10. score = {
11.     "Player A": 0,
12.     "Player B": 0
13. }
14.
15. for i in range(len(playerA)):
16.     if playerA[i] == playerB[i]:
17.         continue
18.     elif wins_against[playerA[i]] == playerB[i]:
19.         score["Player A"] += 1
20.     else:
21.         score["Player B"] += 1
22.
23. print(score)
24.
25. if score["Player A"] > score["Player B"]:
26.     print("Player A Wins")
27. elif score["Player B"] > score["Player A"]:
28.     print("Player B Wins")
29. else:
30.     print("Match Draw")
```

**`2026-jul/w05/q06`** What is the purpose of the dictionary wins_against?

- **A.** It stores the scores of both players.
- **B.** It stores the choices made by each player.
- **C.** It stores which move defeats another move.
- **D.** It stores the winner of each round.

<details><summary>Answer</summary>

**C**. `wins_against` maps each move to the move it defeats: Rock to Scissors, Paper to Rock, Scissors to Paper.

</details>

**`2026-jul/w05/q07`** What is the value of the score dictionary after the loop finishes?

- **A.** {"Player A": 2, "Player B": 2}
- **B.** {"Player A": 3, "Player B": 1}
- **C.** {"Player A": 4, "Player B": 0}
- **D.** {"Player A": 1, "Player B": 3}

<details><summary>Answer</summary>

**B**. Rounds: Rock beats Scissors (A), Paper beats Rock (A), Scissors beats Paper (A), Rock and Rock draw, and Paper vs Scissors goes to B. The score is A 3, B 1.

</details>

**`2026-jul/w05/q08`** What does the expression wins_against[playerA[i]] return?

- **A.** The current score of Player A.
- **B.** The move that defeats Player A's current move.
- **C.** The move defeated by Player A's current move.
- **D.** The current round number.

<details><summary>Answer</summary>

**C**. `wins_against[playerA[i]]` looks up Player A's move in the dictionary and returns the move that it defeats. For `"Paper"` it returns `"Rock"`.

</details>

**`2026-jul/w05/q09`** Which statement is printed at the end of the program?

- **A.** Player A Wins
- **B.** Player B Wins
- **C.** Match Draw
- **D.** No output is printed.

<details><summary>Answer</summary>

**A**. The final score is A 3, B 1. `score["Player A"] > score["Player B"]` is true, so it prints `Player A Wins`.

</details>

**`2026-jul/w05/q10`** Which of the following statements are correct?

- **A.** The dictionary score is updated during program execution.
- **B.** The dictionary wins_against is modified during the program.
- **C.** The program records one drawn round.
- **D.** The statement score["Player A"] += 1 updates the value associated with the key "Player A".

<details><summary>Answer</summary>

**A, C, D**. `score` changes whenever a round has a winner, and `score["Player A"] += 1` adds 1 to Player A's value. Round 4 (Rock vs Rock) is a draw. `wins_against` is only read, never changed.

</details>

### `2026-jul/w05/q11`–`q15`: Library Book Search System

Library Book Search System. A digital library stores book IDs in a sorted list. When a student searches for a book, the librarian first performs a Linear Search to locate the book. Later, the system uses a Binary Search to improve search efficiency on the same sorted list. Study the following program and answer the questions.

```python
1. book_ids = [105, 112, 118, 126, 134, 142, 150, 163]
2. target = 134
3.
4. # Linear Search
5. linear_index = -1
6. for i in range(len(book_ids)):
7.     if book_ids[i] == target:
8.         linear_index = i
9.         break
10.
11. # Binary Search
12. low = 0
13. high = len(book_ids) - 1
14. binary_index = -1
15.
16. while low <= high:
17.     mid = (low + high) // 2
18.
19.     if book_ids[mid] == target:
20.         binary_index = mid
21.         break
22.     elif target < book_ids[mid]:
23.         high = mid - 1
24.     else:
25.         low = mid + 1
26.
27. print("Linear Search:", linear_index)
28. print("Binary Search:", binary_index)
```

**`2026-jul/w05/q11`** Why is the list book_ids arranged in ascending order?

- **A.** To reduce memory usage.
- **B.** Because Binary Search requires the data to be sorted.
- **C.** Because Linear Search requires the data to be sorted.
- **D.** To avoid duplicate values.

<details><summary>Answer</summary>

**B**. Binary search compares with the middle item and drops half the list, which only works when the list is in order, so `book_ids` is sorted.

</details>

**`2026-jul/w05/q12`** What is the output of the program?

- **A.** Linear Search: 3 and Binary Search: 3
- **B.** Linear Search: 4 and Binary Search: 4
- **C.** Linear Search: 5 and Binary Search: 5
- **D.** Linear Search: -1 and Binary Search: -1

<details><summary>Answer</summary>

**B**. `target` 134 is at index 4 of `book_ids`. Linear search sets `linear_index = 4`, and binary search sets `binary_index = 4`. It prints `Linear Search: 4` and `Binary Search: 4`.

</details>

**`2026-jul/w05/q13`** During the first iteration of the Binary Search loop, what is the value of mid?

- **A.** 2
- **B.** 3
- **C.** 4
- **D.** 5

<details><summary>Answer</summary>

**B**. `low = 0` and `high = len(book_ids) - 1 = 7`, so `mid = (0 + 7) // 2 = 3`.

</details>

**`2026-jul/w05/q14`** Suppose the statement break on Line 9 is removed. Which statement is correct?

- **A.** The program produces an error.
- **B.** The Linear Search continues checking the remaining elements even after finding the target.
- **C.** The Binary Search stops working.
- **D.** The value of linear_index becomes -1.

<details><summary>Answer</summary>

**B**. Without `break`, the linear loop keeps checking the remaining items after finding 134. Since 134 appears only once, `linear_index` keeps the value 4, but extra checks are done.

</details>

**`2026-jul/w05/q15`** Which of the following statements are correct?

- **A.** Linear Search checks elements one by one from the beginning of the list.
- **B.** Binary Search repeatedly divides the search space into two halves.
- **C.** Both Linear Search and Binary Search return index 4 for the given input.
- **D.** Binary Search can be applied correctly even if book_ids is not sorted.

<details><summary>Answer</summary>

**A, B, C**. Linear search checks one by one from the start, and binary search halves the range each time. Here both return index 4. Binary search needs a sorted list; `book_ids` happens to be sorted.

</details>

### `2026-jul/w06/q01`–`q05`: Secret Notice Encoder

Secret Notice Encoder A college club regularly shares announcements with its members. Since these messages are posted on a public notice board, the club wants to make them difficult for outsiders to read. To achieve this, the club uses a Substitution Cipher. Every alphabetic character is replaced by the previous letter in string.ascii_letters. Non-alphabetic characters such as spaces, digits, and punctuation marks remain unchanged. The following Python program performs this encryption.

```python
1. import string
2.
3. cipher = {}
4.
5. letters = string.ascii_letters
6.
7. for i in range(len(letters)):
8.     cipher[letters[i]] = letters[i - 1]

10. text = input("Enter a message: ")
11.
12. encrypted = ""
13.
14. for ch in text:
15.     if ch in cipher:
16.         encrypted += cipher[ch]
17.     else:
18.         encrypted += ch
19.
20. print("Original :", text)
21. print("Encrypted:", encrypted)
```

**`2026-jul/w06/q01`** Which line creates the substitution rule that maps each letter to its replacement?

- **A.** Line 5
- **B.** Line 7
- **C.** Line 8
- **D.** Line 16

<details><summary>Answer</summary>

**C**. Line 8 is `cipher[letters[i]] = letters[i - 1]`, which stores each letter as a key and the previous letter as its value. That is the substitution rule.

</details>

**`2026-jul/w06/q02`** Suppose the user enters the input: ABC123 Which statement ensures that the digits 1, 2, and 3 remain unchanged?

- **A.** Line 10
- **B.** Lines 17–18
- **C.** Line 20
- **D.** Line 21

<details><summary>Answer</summary>

**B**. The digits are not keys in `cipher`, so `ch in cipher` is false and the `else` branch on lines 17–18 copies the character unchanged.

</details>

**`2026-jul/w06/q03`** What is the purpose of Line 12?

- **A.** It stores the substitution dictionary.
- **B.** It stores the original input.
- **C.** It initializes an empty string to build the encrypted message.
- **D.** It prints the encrypted output.

<details><summary>Answer</summary>

**C**. Line 12 sets `encrypted = ""`, an empty string. Each encrypted character is added to it later.

</details>

**`2026-jul/w06/q04`** If Line 16 encrypted += cipher[ch] is replaced with encrypted += ch what will be the result?

- **A.** Only uppercase letters will be encrypted.
- **B.** The program will generate an error.
- **C.** Only digits will be encrypted.
- **D.** The output will be identical to the input.

<details><summary>Answer</summary>

**D**. With `encrypted += ch`, every character is copied unchanged and `cipher` is never used. So the output is identical to the input.

</details>

**`2026-jul/w06/q05`** Which of the following statements about the program are correct? (Select all that apply.)

- **A.** Line 5 stores all lowercase and uppercase English letters.
- **B.** Line 8 creates a substitution mapping using a dictionary.
- **C.** Line 15 checks whether the current character is a digit.
- **D.** Lines 20 and 21 display both the original and encrypted messages.

<details><summary>Answer</summary>

**A, B, D**. `string.ascii_letters` holds both lowercase and uppercase letters (line 5). Line 8 builds the letter-to-letter dictionary. Lines 20 and 21 print the original and the encrypted text. Line 15 tests `ch in cipher`, not whether `ch` is a digit.

</details>

### `2026-jul/w06/q06`–`q10`: Tic-Tac-Toe Winner Checker

Tic-Tac-Toe Winner Checker A programming club is developing a simple Tic-Tac-Toe game. The game board is represented using a nested list, where each inner list represents a row of the board. - 'X' represents Player X. - 'O' represents Player O. - ' ' (space) represents an empty cell. The program checks only the rows of the board to determine whether either player has won. If a row contains three identical non-space symbols, that player is declared the winner. Otherwise, the program reports that there is no row winner.

```python
1. board = [
2.     ['X', 'X', 'X'],
3.     ['O', ' ', 'O'],
4.     [' ', 'O', ' ']
5. ]
6.
7. winner = "None"
8.
9. for row in board:
10.     if row[0] == row[1] == row[2] and row[0] != ' ':
11.         winner = row[0]
12.         break
13.
14. if winner != "None":
15.     print("Winner:", winner)
16. else:
17.     print("No row winner")
```

**`2026-jul/w06/q06`** Which line checks whether all three cells in a row contain the same non-empty symbol?

- **A.** Line 7
- **B.** Line 9
- **C.** Line 10
- **D.** Line 15

<details><summary>Answer</summary>

**C**. Line 10 tests `row[0] == row[1] == row[2] and row[0] != ' '`: all three cells equal and not blank.

</details>

**`2026-jul/w06/q07`** What is the purpose of the break statement in Line 12?

- **A.** It skips the current row.
- **B.** It exits the loop after finding a winner.
- **C.** It resets the board.
- **D.** It starts checking the rows again.

<details><summary>Answer</summary>

**B**. Once a winning row is found, `break` leaves the `for` loop, since the remaining rows do not need checking.

</details>

**`2026-jul/w06/q08`** Which variable stores the winning player's symbol?

- **A.** board
- **B.** row
- **C.** winner
- **D.** print

<details><summary>Answer</summary>

**C**. `winner` starts as `"None"` and is set to `row[0]` (`'X'` or `'O'`) when a winning row is found.

</details>

**`2026-jul/w06/q09`** If Line 11 winner = row[0] is replaced with winner = "Player" what will the program display when a winning row is found?

- **A.** The winning symbol (X or O)
- **B.** "Player"
- **C.** "None"
- **D.** The entire row

<details><summary>Answer</summary>

**B**. With `winner = "Player"`, the winner is the string `"Player"`. It is not `"None"`, so line 15 prints `Winner: Player`.

</details>

**`2026-jul/w06/q10`** Which of the following statements about the program are correct? (Select all that apply.)

- **A.** The board is represented using a nested list.
- **B.** The program checks only row-wise winning conditions.
- **C.** The loop stops immediately after a winner is found.
- **D.** The program checks both row-wise and diagonal winning conditions.

<details><summary>Answer</summary>

**A, B, C**. The board is a list of lists, only rows are checked (not columns or diagonals), and `break` stops the loop at the first winning row.

</details>

### `2026-jul/w06/q16`–`q20`: Recursive Binary Search for Student Roll Numbers

Recursive Binary Search for Student Roll Numbers A university stores student roll numbers in ascending order. When an administrator wants to verify whether a particular roll number exists, the system performs a recursive binary search. The search begins by checking the middle roll number in the current range. - If the middle roll number matches the required roll number, the search is successful. - If the required roll number is smaller, the same search process is repeated on the left half. - If the required roll number is larger, the search continues recursively on the right half. - If the search range becomes invalid (the left index becomes greater than the right index), the roll number is reported as not found. The following program implements this recursive binary search.

```python
1. def binary_search(arr, low, high, target):
2.     if low > high:
3.         return -1
4.
5.     mid = (low + high) // 2
6.
7.     if arr[mid] == target:
8.         return mid
9.
10.     elif target < arr[mid]:
11.         return binary_search(arr, low, mid - 1, target)
12.
13.     else:
14.         return binary_search(arr, mid + 1, high, target)
15.
16. numbers = [105, 112, 118, 124, 131, 145, 152, 168]
17. key = 131
18.
19. result = binary_search(numbers, 0, len(numbers)-1, key)
20.
21. if result != -1:
22.     print("Roll number found at index", result)
23. else:
24.     print("Roll number not found")
```

**`2026-jul/w06/q16`** Which line represents the base case where the search terminates because the search range has become invalid?

- **A.** Line 5
- **B.** Line 2
- **C.** Line 7
- **D.** Line 14

<details><summary>Answer</summary>

**B**. Line 2 checks `if low > high`, and line 3 returns -1. That is the base case for an invalid search range.

</details>

**`2026-jul/w06/q17`** Which line performs the recursive search on the left half of the list?

- **A.** Line 5
- **B.** Line 8
- **C.** Line 11
- **D.** Line 19

<details><summary>Answer</summary>

**C**. Line 11 is `return binary_search(arr, low, mid - 1, target)`, the call that searches the left half when the target is smaller than `arr[mid]`.

</details>

**`2026-jul/w06/q18`** What is the purpose of Line 5?

- **A.** It checks whether the element is found.
- **B.** It calculates the middle index of the current search range.
- **C.** It sorts the list.
- **D.** It prints the search result.

<details><summary>Answer</summary>

**B**. Line 5 is `mid = (low + high) // 2`, which finds the middle index of the current range.

</details>

**`2026-jul/w06/q19`** If Line 14 return binary_search(arr, mid + 1, high, target) is replaced with return binary_search(arr, low, high, target) what is the most likely outcome when the target is greater than the middle element?

- **A.** The program always finds the target immediately.
- **B.** The search correctly moves to the right half.
- **C.** The search continues without reducing the search range, leading to infinite recursion.
- **D.** The program searches only the left half.

<details><summary>Answer</summary>

**C**. If the call keeps `low` and `high` the same, the range never shrinks. The same call repeats forever, so the recursion never ends.

</details>

**`2026-jul/w06/q20`** Which of the following statements about the program are correct? (Select all that apply.)

- **A.** The recursive calls in Lines 11 and 14 reduce the search space in every recursive step.
- **B.** The program can correctly perform binary search even if numbers is not sorted.
- **C.** Line 5 compares the target with every element in the list.
- **D.** The recursion stops either when the target is found (Line 8) or when the search range becomes invalid (Line 3).

<details><summary>Answer</summary>

**A, D**. Each recursive call searches only one half, so the range shrinks every step. The recursion stops when `arr[mid] == target` or when `low > high`. Binary search needs a sorted list, and line 5 only computes `mid`.

</details>

### `2026-jul/w07/q01`–`q05`: Drone Surveillance Route

Drone Surveillance Route A disaster management team uses a drone to capture images of a disaster-affected area. The images are stored in a matrix. During analysis, the system processes the images in a spiral order, beginning from the outer boundary and gradually moving toward the center so that all regions are examined systematically. The following Python program performs the spiral traversal of the matrix.

```python
1. def spiral(m, n, a):
2.     k = 0
3.     l = 0
4.
5.     while k < m and l < n:
6.
7.         for i in range(l, n):
8.             print(a[k][i], end=" ")
9.         k += 1
10.
11.         for i in range(k, m):
12.             print(a[i][n-1], end=" ")
13.         n -= 1
14.
15.         if k < m:
16.             for i in range(n-1, l-1, -1):
17.                 print(a[m-1][i], end=" ")
18.             m -= 1
19.
20.         if l < n:
21.             for i in range(m-1, k-1, -1):
22.                 print(a[i][l], end=" ")
23.             l += 1
24.
25. matrix = [
26.     [1, 2, 3, 4],
27.     [5, 6, 7, 8],
28.     [9, 10, 11, 12],
29.     [13, 14, 15, 16]
30. ]
31.
32. spiral(4, 4, matrix)
```

**`2026-jul/w07/q01`** Which variables store the starting row and starting column of the current spiral layer?

- **A.** k and l
- **B.** m and n
- **C.** i and k
- **D.** a and i

<details><summary>Answer</summary>

**A**. `k` is the starting row and `l` is the starting column of the current layer. `m` and `n` are the end boundaries.

</details>

**`2026-jul/w07/q02`** What is the purpose of the statement at line 9?

- **A.** It moves to the next column.
- **B.** It moves to the next row after printing the top row.
- **C.** It moves to the previous row.
- **D.** It resets the row index.

<details><summary>Answer</summary>

**B**. Line 9 is `k += 1`. After the top row has been printed, the starting row moves down by one.

</details>

**`2026-jul/w07/q03`** Which statement best describes the loop at lines 11–12?

- **A.** It prints the first column from top to bottom.
- **B.** It prints the last row from left to right.
- **C.** It prints the last column from top to bottom.
- **D.** It prints the top row from right to left.

<details><summary>Answer</summary>

**C**. The loop on lines 11–12 prints `a[i][n-1]` for `i` from `k` to `m-1`. The column stays fixed at the last one, and the row goes down: the last column, top to bottom.

</details>

**`2026-jul/w07/q04`** What is the first sequence of numbers printed by the program?

- **A.** 1 2 3 4
- **B.** 4 8 12 16
- **C.** 13 14 15 16
- **D.** 1 5 9 13

<details><summary>Answer</summary>

**A**. The first loop prints the top row from left to right: 1 2 3 4.

</details>

**`2026-jul/w07/q05`** Which of the following statements are true about the program?

- **A.** The variables k, l, m, and n define the current boundaries of the unvisited portion of the matrix.
- **B.** After each side of the spiral is printed, the corresponding boundary is updated.
- **C.** The program prints only square matrices correctly.
- **D.** The program traverses the matrix column by column throughout.

<details><summary>Answer</summary>

**A, B**. `k`, `l`, `m` and `n` mark the first and last row and column not yet visited. After each side is printed, the matching boundary moves inward. The code also handles rectangles, and it does not go column by column throughout.

</details>

### `2026-jul/w07/q06`–`q10`: Mini Snake and Ladder Tournament

Mini Snake and Ladder Tournament A board game club is testing a simplified Snake and Ladder game. The board has 25 positions. A player starts at position 1 and moves according to a sequence of dice rolls. If the player lands on the bottom of a ladder, the player climbs immediately. If the player lands on the head of a snake, the player slides down immediately. If the player's position becomes greater than 25, the move is ignored. The game has the following snakes and ladders: - Ladder: 4 → 12 - Ladder: 9 → 18 - Snake: 16 → 7 - Snake: 22 → 14 The following Python program simulates the player's journey.

```python
1. def play_game():
2.     position = 1
3.     target = 25
4.     rolls = [3, 5, 7, 6, 4, 2]
5.
6.     for roll in rolls:
7.         if position + roll <= target:
8.             position += roll
9.
10.         if position == 4:
11.             position = 12
12.         elif position == 9:
13.             position = 18
14.         elif position == 16:
15.             position = 7
16.         elif position == 22:
17.             position = 14
18.
19.         print(position, end=" ")
20.
21.         if position == target:
22.             break
23.
24. play_game()
```

**`2026-jul/w07/q06`** Which statement ensures that the player does not move beyond the last position on the board?

- **A.** if position == target:
- **B.** if position + roll <= target:
- **C.** position += roll
- **D.** break

<details><summary>Answer</summary>

**B**. Line 7 checks `position + roll <= target`, so a move that would pass 25 is skipped.

</details>

**`2026-jul/w07/q07`** If the player reaches position 16, what happens next?

- **A.** The player moves to position 22.
- **B.** The player stays at position 16.
- **C.** The player moves to position 18.
- **D.** The player moves to position 7.

<details><summary>Answer</summary>

**D**. Position 16 is a snake head: `elif position == 16: position = 7`. The player slides down to 7.

</details>

**`2026-jul/w07/q08`** What is the purpose of the statement at line 21?

- **A.** It checks whether all dice rolls are completed.
- **B.** It checks whether the player has reached the target position.
- **C.** It resets the player's position.
- **D.** It moves the player to the next turn.

<details><summary>Answer</summary>

**B**. Line 21 is `if position == target`, which checks whether the player has reached square 25.

</details>

**`2026-jul/w07/q09`** Which statement immediately ends the loop once the player reaches the target?

- **A.** break
- **B.** position += roll
- **C.** print(position, end=" ")
- **D.** for roll in rolls:

<details><summary>Answer</summary>

**A**. `break` exits the `for` loop at once, so no more rolls are used once the player reaches the target.

</details>

**`2026-jul/w07/q10`** Which of the following statements are true about the program?

- **A.** The player always moves after every dice roll.
- **B.** The game stops only after all dice rolls are processed.
- **C.** A move is ignored if it takes the player beyond position 25.
- **D.** Landing on a snake or ladder changes the player's position immediately.

<details><summary>Answer</summary>

**C, D**. A move is skipped if it would go beyond 25 (line 7). When the player lands on a ladder or snake square, the position is changed at once (lines 10–17).

</details>

### `2026-jul/w07/q11`–`q15`: Food Delivery Pickup Locations

Food Delivery Pickup Locations A food delivery company uses a map to display the locations of restaurants where delivery agents need to collect orders. Each restaurant is represented by a marker on the map. When a marker is clicked, the restaurant's name is displayed. The following Python program creates a map and places markers for three restaurants.

```python
1. import gmplot
2.
3. gmap = gmplot.GoogleMapPlotter(15.3647, 75.1240, 13)
4.
5. restaurants = [
6.     ("Pizza Hub", 15.3655, 75.1258),
7.     ("Green Bowl", 15.3628, 75.1219),
8.     ("Spice Corner", 15.3672, 75.1285)
9. ]
10.
11. for name, lat, lon in restaurants:
12.     gmap.marker(lat, lon, title=name)
13.
14. gmap.draw("restaurants.html")
```

**`2026-jul/w07/q11`** What is the purpose of the statement at line 3?

- **A.** It creates a marker on the map.
- **B.** It stores restaurant names.
- **C.** It creates a Google map centered at the given location.
- **D.** It saves the map as an HTML file.

<details><summary>Answer</summary>

**C**. Line 3 is `gmplot.GoogleMapPlotter(15.3647, 75.1240, 13)`, which creates a Google map centred on those coordinates at zoom 13.

</details>

**`2026-jul/w07/q12`** Which statement adds a marker for each restaurant?

- **A.** gmap.draw("restaurants.html")
- **B.** gmap.marker(lat, lon, title=name)
- **C.** restaurants = [...]
- **D.** for name, lat, lon in restaurants:

<details><summary>Answer</summary>

**B**. Line 12 is `gmap.marker(lat, lon, title=name)`, which puts a marker with that name at the coordinates.

</details>

**`2026-jul/w07/q13`** What is displayed as the title of each marker?

- **A.** The latitude value
- **B.** The longitude value
- **C.** The map's zoom level
- **D.** The restaurant name

<details><summary>Answer</summary>

**D**. `title=name` passes the restaurant's name to the marker, so the name is shown as its title.

</details>

**`2026-jul/w07/q14`** What is the purpose of the statement at line 14?

- **A.** It creates another marker.
- **B.** It removes all markers from the map.
- **C.** It changes the map center.
- **D.** It saves the map as an HTML file.

<details><summary>Answer</summary>

**D**. Line 14 is `gmap.draw("restaurants.html")`, which writes the map with its markers to an HTML file.

</details>

**`2026-jul/w07/q15`** Which of the following statements are true about the program?

- **A.** The program creates a separate map for each restaurant.
- **B.** The markers are added using the latitude and longitude values.
- **C.** The program iterates through all restaurants using a for loop.
- **D.** The HTML file is created before the markers are added.

<details><summary>Answer</summary>

**B, C**. The `for` loop goes through every restaurant, and `marker(lat, lon, ...)` places a marker at each one's latitude and longitude. It uses one map, and the HTML file is written after the markers are added.

</details>

### `2026-jul/w07/q16`–`q20`: Smart Heritage City Explorer

Smart Heritage City Explorer. The tourism department of a heritage city has developed a Smart Heritage City Explorer to help visitors explore popular attractions.
The city is represented as a matrix, where each cell corresponds to a location. Every morning, an inspection drone scans the city in a spiral order, starting from the outer boundary and moving towards the center to ensure that every location is inspected exactly once.
Information about each attraction is stored in a dictionary containing the attraction's name, category, visitor rating, latitude, and longitude. When a visitor searches for an attraction, the application uses linear search if the attractions are stored in random order. If the attractions are sorted alphabetically, the application uses binary search to locate the attraction more efficiently.
After an attraction is found, its latitude and longitude are used to place a marker on a Google Map so that visitors can easily navigate to the destination.
The application also includes a Treasure Trail game. Visitors move across 25 checkpoints using dice rolls. Some checkpoints contain ladders that move visitors ahead, while others contain snakes that move them backward. If a dice roll takes a visitor beyond the final checkpoint, that move is ignored.
The developers use appropriate data structures and algorithms so that the application remains efficient and easy to maintain.

(This case is a story only; it has no program.)

**`2026-jul/w07/q16`** The attractions are stored in random order. Which searching technique is most appropriate for finding a particular attraction?

- **A.** Binary Search
- **B.** Spiral Search
- **C.** Linear Search
- **D.** Depth First Search

<details><summary>Answer</summary>

**C**. Binary search needs sorted data. For attractions in random order, linear search (check one by one) is the right choice.

</details>

**`2026-jul/w07/q17`** Why does the inspection drone use a spiral traversal of the city matrix?

- **A.** To visit only the corner locations.
- **B.** To inspect every location by moving from the outer boundary towards the center.
- **C.** To sort the locations alphabetically.
- **D.** To search for a specific attraction.

<details><summary>Answer</summary>

**B**. A spiral traversal goes around the matrix from the outside edge toward the centre and visits every cell once, so the drone can inspect all locations.

</details>

**`2026-jul/w07/q18`** Which information is essential for placing an attraction on the Google Map?

- **A.** Name and Category
- **B.** Rating and Category
- **C.** Latitude and Longitude
- **D.** Name and Rating

<details><summary>Answer</summary>

**C**. A map marker needs its position, which is the latitude and longitude.

</details>

**`2026-jul/w07/q19`** In the Treasure Trail game, what should happen if a dice roll moves the visitor beyond checkpoint 25?

- **A.** The visitor returns to checkpoint 1.
- **B.** The visitor wins immediately.
- **C.** The visitor moves to checkpoint 25.
- **D.** The move is ignored.

<details><summary>Answer</summary>

**D**. The game rule is that a move which would pass the last checkpoint (25) is ignored, so the visitor stays where they are.

</details>

**`2026-jul/w07/q20`** Which of the following statements are true about the Smart Heritage City Explorer?

- **A.** Binary search can be used efficiently even if the attractions are stored in random order.
- **B.** A dictionary is suitable for storing multiple details about each attraction.
- **C.** Spiral traversal is a suitable approach for visiting every location in a matrix.
- **D.** Google Map markers are placed using the latitude and longitude of an attraction.

<details><summary>Answer</summary>

**B, C**

</details>

### `2026-jul/w08/q06`–`q10`: Lucky Draw Betting Game

Lucky Draw Betting Game A gaming café has introduced a simple Lucky Draw Challenge. A player starts with ₹0 in their game account. The game is played 7 times. In every round: - The player's bet number is randomly chosen between 1 and 10. - The lucky draw number is also randomly chosen between 1 and 10. - If both numbers are the same, the player wins ₹900, but ₹100 is deducted as the participation fee. Hence, the account increases by ₹800. - If the numbers are different, the player only loses the ₹100 participation fee. - After every round, the current account balance is displayed. The following Python program implements this game.

```python
1. import random
2.
3. account = 0
4.
5. for i in range(7):
6.     bet = random.randint(1, 10)
7.     lucky_draw = random.randint(1, 10)
8.     print("Bet:", bet)
9.     print("Lucky draw:", lucky_draw)
10.
11.     if bet == lucky_draw:
12.         account = account + 900 - 100
13.     else:
14.         account = account - 100
15.
16.     print("Amount in your game account:", account)
```

**`2026-jul/w08/q06`** According to Line 5, how many rounds will the game be played?

- **A.** 7
- **B.** 8
- **C.** 10
- **D.** Depends on the random numbers

<details><summary>Answer</summary>

**A**. Line 5 is `for i in range(7)`, so the loop body runs 7 times, once for each round.

</details>

**`2026-jul/w08/q07`** Which lines generate the random numbers for the player's bet and the lucky draw?

- **A.** Lines 3 and 5
- **B.** Lines 8 and 9
- **C.** Lines 11 and 12
- **D.** Lines 6 and 7

<details><summary>Answer</summary>

**D**. Line 6 sets `bet = random.randint(1, 10)` and line 7 sets `lucky_draw = random.randint(1, 10)`.

</details>

**`2026-jul/w08/q08`** If the bet number and lucky draw number are equal, what is the net change in the account balance according to Line 12?

- **A.** +₹100
- **B.** +₹900
- **C.** +₹700
- **D.** +₹800

<details><summary>Answer</summary>

**D**. Line 12 is `account = account + 900 - 100`, so the net change is +800.

</details>

**`2026-jul/w08/q09`** According to Lines 13–14, what happens when the bet number and lucky draw number are different?

- **A.** ₹100 is deducted from the account.
- **B.** ₹900 is added to the account.
- **C.** The account balance remains unchanged.
- **D.** A new account is created.

<details><summary>Answer</summary>

**A**. Lines 13–14 are the `else` branch, `account = account - 100`, so 100 is deducted.

</details>

**`2026-jul/w08/q10`** Which of the following statements about the program are correct? (Choose all that apply.)

- **A.** The player's account balance is printed after every round.
- **B.** The player's bet is entered by the user using input().
- **C.** The lucky draw number is always different from the bet number.
- **D.** The player's account balance can become negative.

<details><summary>Answer</summary>

**A, D**. Line 16 prints the balance after each round, so A is correct. The balance starts at 0 and loses 100 per losing round, so it can become negative, so D is correct. The numbers are random, not typed with `input()`, and they can be equal.

</details>

### `2026-jul/w08/q11`–`q15`: Secure Access Puzzle Generator

Secure Access Puzzle Generator A cybersecurity training platform uses anagrams to create authentication puzzles. Before granting access to a practice lab, the system displays a shuffled version of a secret keyword. To ensure the puzzle is meaningful, the displayed word must not be identical to the original keyword. The system keeps generating new arrangements until a valid anagram is produced. The following Python program implements this logic.

```python
1. import random
2.
3. keyword = input("Enter the secret keyword: ")
4. letters = list(keyword)
5.
6. while True:
7.     random.shuffle(letters)
8.     candidate = "".join(letters)
9.
10.     if candidate != keyword:
11.         break
12.
13. print("Authentication Puzzle:", candidate)
```

**`2026-jul/w08/q11`** Suppose the user enters the word LEVEL. Which of the following statements is always true?

- **A.** The displayed puzzle will never contain repeated letters.
- **B.** The displayed puzzle will always have exactly five letters.
- **C.** The displayed puzzle will always be alphabetically sorted.
- **D.** The displayed puzzle cannot be generated because the word contains repeated letters.

<details><summary>Answer</summary>

**B**. `random.shuffle` only changes the order of the letters, so the candidate always has the same 5 letters as `LEVEL`.

</details>

**`2026-jul/w08/q12`** Consider the execution of Lines 6–11. Which situation can cause the loop to execute more than once?

- **A.** The entered keyword has fewer than five letters.
- **B.** random.shuffle() arranges the letters in the same order as the original keyword.
- **C.** The keyword contains only uppercase letters.
- **D.** The keyword contains duplicate characters.

<details><summary>Answer</summary>

**B**. The loop repeats when `candidate != keyword` is false, which happens when the shuffle returns the same order as the original word.

</details>

**`2026-jul/w08/q13`** Which of the following inputs may cause the program to never terminate?

- **A.** PYTHON
- **B.** RANDOM
- **C.** A
- **D.** SECURE

<details><summary>Answer</summary>

**C**. A one-letter word such as `A` has only one arrangement, so `candidate` always equals `keyword`. The test on line 10 is never true, so the `while True` loop never breaks.

</details>

**`2026-jul/w08/q14`** Which statement best describes the purpose of Lines 10–11?

- **A.** They ensure that every possible anagram is generated exactly once.
- **B.** They ensure that duplicate letters are removed.
- **C.** They stop the loop only after a shuffled word different from the original has been generated.
- **D.** They guarantee that the generated anagram is alphabetically smallest.

<details><summary>Answer</summary>

**C**. Line 10 breaks out of the loop only if `candidate != keyword`. So the loop goes on shuffling until it gets an arrangement that differs from the original.

</details>

**`2026-jul/w08/q15`** Which of the following statements about the program are correct? (Choose all that apply.)

- **A.** If the input contains only one character, the program may run indefinitely.
- **B.** Every execution of the program produces a different anagram.
- **C.** The program guarantees that all possible anagrams will eventually be generated.
- **D.** The generated puzzle always contains exactly the same characters as the original keyword.

<details><summary>Answer</summary>

**A, D**. A one-letter keyword can never give a different candidate, so the loop can run forever. `random.shuffle` only reorders the existing letters, so the puzzle always has the same characters as the keyword.

</details>

### `2026-jul/w08/q16`–`q20`: Customer Feedback Analysis

Customer Feedback Analysis An online shopping company collects customer reviews after every purchase. The data is stored in a Pandas DataFrame. To understand customer satisfaction, the company uses NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer. Each review is assigned a compound sentiment score. Reviews with a positive compound score are labeled Positive; otherwise, they are labeled Negative. The following Python program performs this analysis.

```python
1. import pandas as pd
2. from nltk.sentiment.vader import SentimentIntensityAnalyzer
3.
4. reviews = pd.DataFrame({
5.     "Customer": ["Asha", "Rahul", "Neha", "Arjun"],
6.     "Review": [
7.         "Excellent product and fast delivery",
8.         "The quality is average",
9.         "Very disappointed with the service",
10.         "Worth every penny"
11.     ]
12. })
13.
14. analyzer = SentimentIntensityAnalyzer()
15.
16. def get_sentiment(review):
17.     score = analyzer.polarity_scores(review)["compound"]
18.     if score > 0:
19.         return "Positive"
20.     else:
21.         return "Negative"
22.
23. reviews["Sentiment"] = reviews["Review"].apply(get_sentiment)
24.
25. print(reviews)
```

**`2026-jul/w08/q16`** What is the primary purpose of Line 14?

- **A.** To create a Pandas DataFrame.
- **B.** To create an object that can analyze the sentiment of text.
- **C.** To read customer reviews from a file.
- **D.** To display the final DataFrame.

<details><summary>Answer</summary>

**B**. Line 14 is `analyzer = SentimentIntensityAnalyzer()`, which creates the VADER object used to score text.

</details>

**`2026-jul/w08/q17`** According to Line 17, which value is used to determine whether a review is positive or negative?

- **A.** neg
- **B.** compound
- **C.** neu
- **D.** pos

<details><summary>Answer</summary>

**B**. Line 17 takes `["compound"]` from the dictionary that `polarity_scores` returns, and lines 18–21 call the review Positive when that score is above 0.

</details>

**`2026-jul/w08/q18`** What is the purpose of Line 23?

- **A.** It removes reviews with negative sentiment.
- **B.** It creates a new column containing the sentiment label for each review.
- **C.** It sorts the reviews based on sentiment.
- **D.** It replaces the original review text with sentiment scores.

<details><summary>Answer</summary>

**B**. Line 23 calls `get_sentiment` on every review with `apply` and stores the labels in a new column `Sentiment`.

</details>

**`2026-jul/w08/q19`** Which statement best describes the role of the function get_sentiment()?

- **A.** It converts reviews into uppercase.
- **B.** It counts the number of words in each review.
- **C.** It calculates the average sentiment score of all reviews.
- **D.** It assigns a sentiment label to a single review based on its compound score.

<details><summary>Answer</summary>

**D**. `get_sentiment` gets one review, computes its compound score and returns `"Positive"` if the score is above 0, otherwise `"Negative"`.

</details>

**`2026-jul/w08/q20`** Which of the following statements are correct? (Choose all that apply.)

- **A.** The program stores the sentiment score directly in the Review column.
- **B.** The reviews are stored in a Pandas DataFrame.
- **C.** The sentiment label for each review is generated using the get_sentiment() function.
- **D.** The program classifies reviews based on the length of the review text.

<details><summary>Answer</summary>

**A, B, C, D**

</details>

### `2026-jul/w09/q01`–`q05`: Product Review Analysis

Product Review Analysis An online marketplace wants to analyze the words used in customer reviews. The program tokenizes the review text, creates a frequency distribution using FreqDist, and displays only the words that occur more than once. It also reports the total number of unique words.

```python
1. from nltk.tokenize import word_tokenize
2. from nltk import FreqDist
3.
4. reviews = """
5. Fast delivery and good packaging.
6. Good quality and fast service.
7. Delivery was fast and packaging was good.
8. """
9.
10. tokens = word_tokenize(reviews.lower())
11. freq = FreqDist(tokens)
12.
13. print(len(tokens))
14. print(len(freq))
15.
16. for word in sorted(freq):
17.     if freq[word] > 1:
18.         print(word, freq[word])
```

**`2026-jul/w09/q01`** Which statement converts the review text into a list of tokens?

- **A.** Line 10
- **B.** Line 11
- **C.** Line 13
- **D.** Line 16

<details><summary>Answer</summary>

**A**. Line 10 is `tokens = word_tokenize(reviews.lower())`, which splits the text into tokens.

</details>

**`2026-jul/w09/q02`** What does the expression len(freq) in Line 14 return?

- **A.** Total number of characters in the review
- **B.** Number of unique tokens in the review
- **C.** Total number of repeated words
- **D.** Number of lines in the review

<details><summary>Answer</summary>

**B**. A `FreqDist` keeps one entry per different token, so `len(freq)` is the number of unique tokens. Here that is 9.

</details>

**`2026-jul/w09/q03`** Which line creates the frequency distribution of the tokens?

- **A.** Line 10
- **B.** Line 16
- **C.** Line 11
- **D.** Line 13

<details><summary>Answer</summary>

**C**. Line 11 is `freq = FreqDist(tokens)`, which counts how often each token occurs.

</details>

**`2026-jul/w09/q04`** Which part of the program prints only the words that occur more than once?

- **A.** Line 10
- **B.** Line 13
- **C.** Line 14
- **D.** Lines 16–18

<details><summary>Answer</summary>

**D**. Lines 16–18 loop over the sorted words and print a word only when `freq[word] > 1`. So they show only the words that occur more than once.

</details>

**`2026-jul/w09/q05`** Which of the following statements are correct?

- **A.** len(tokens) returns the number of unique words in the review.
- **B.** word_tokenize() automatically counts the frequency of each token.
- **C.** FreqDist stores each token as a key and its frequency as the corresponding value.
- **D.** len(freq) gives the number of distinct tokens present in the text.

<details><summary>Answer</summary>

**A, C, D**

</details>

### `2026-jul/w09/q06`–`q10`: Library Book Recommendation Network

Library Book Recommendation Network A digital library recommends books based on their similarity. Each book is represented as a node, and an edge between two books indicates that they are frequently borrowed together. The librarian uses NetworkX to model and examine this recommendation network.

```python
1. import networkx as nx
2.
3. G = nx.Graph()
4.
5. G.add_nodes_from(["Python", "AI", "ML", "Data", "Cloud"])
6.
7. G.add_edges_from([
8.     ("Python", "AI"),
9.     ("Python", "Data"),
10.     ("AI", "ML"),
11.     ("ML", "Data"),
12.     ("Cloud", "Data")
13. ])
14.
15. print(len(G.nodes))
16. print(len(G.edges))
17.
18. for book in G.nodes:
19.     print(book, list(G.neighbors(book)))
```

**`2026-jul/w09/q06`** In this graph, what does a node represent?

- **A.** A book
- **B.** A recommendation between two books
- **C.** The total number of books
- **D.** A borrowing record

<details><summary>Answer</summary>

**A**. `G.add_nodes_from` on line 5 adds the five book names as nodes, so each node is one book.

</details>

**`2026-jul/w09/q07`** What does an edge between two books indicate?

- **A.** The books have the same author.
- **B.** The books belong to different categories.
- **C.** The books are borrowed together and are recommended to each other.
- **D.** The books have the same publication year.

<details><summary>Answer</summary>

**C**. An edge joins two books that are borrowed together, which is the recommendation link between them (for example `Python`–`AI`).

</details>

**`2026-jul/w09/q08`** What does len(G.nodes) represent?

- **A.** Number of recommendations
- **B.** Number of books in the network
- **C.** Number of neighboring books
- **D.** Number of connected components

<details><summary>Answer</summary>

**B**. `G.nodes` holds all the books in the graph, so `len(G.nodes)` is the number of books, here 5.

</details>

**`2026-jul/w09/q09`** Why is G.neighbors(book) used in the program?

- **A.** To remove duplicate books
- **B.** To sort the books alphabetically
- **C.** To calculate the shortest path
- **D.** To find books directly connected to a given book

<details><summary>Answer</summary>

**D**. `G.neighbors(book)` returns the nodes that share an edge with `book`, the books directly connected to it. Line 19 prints them as a list.

</details>

**`2026-jul/w09/q10`** Which of the following statements are correct?

- **A.** Every node must be connected to every other node.
- **B.** An edge can exist without any nodes.
- **C.** len(G.edges) returns the total number of recommendation links in the graph.
- **D.** A graph can be used to model relationships between connected objects.

<details><summary>Answer</summary>

**A, C, D**

</details>

### `2026-jul/w09/q16`–`q20`: Quality Inspection of Product Images

Quality Inspection of Product Images An online retail company inspects product images before publishing them on its website. The system opens an image, checks the color of a specific pixel, marks that pixel with a new color for verification, creates a small thumbnail image, and saves the modified image.

```python
1. from PIL import Image
2.
3. img = Image.open("product.jpg")
4.
5. print(img.size)
6. print(img.getpixel((20, 20)))
7.
8. img.putpixel((20, 20), (255, 0, 0))
9.
10. thumb = Image.new("RGB", (100, 100), "white")
11. thumb.save("thumbnail.jpg")
12.
13. img.save("verified_product.jpg")
```

**`2026-jul/w09/q16`** Why is getpixel() used in this program?

- **A.** To resize the image
- **B.** To change the image dimensions
- **C.** To retrieve the color value of a specific pixel
- **D.** To save the image

<details><summary>Answer</summary>

**C**. Line 6 calls `img.getpixel((20, 20))`, which returns the colour value of the pixel at that position.

</details>

**`2026-jul/w09/q17`** What is the purpose of putpixel()?

- **A.** To create a new image
- **B.** To modify the color of a specific pixel
- **C.** To compress the image
- **D.** To display the image

<details><summary>Answer</summary>

**B**. `putpixel((x, y), colour)` sets the colour of one pixel. Line 8 uses it to mark the checked pixel red.

</details>

**`2026-jul/w09/q18`** What is the purpose of Image.new()?

- **A.** To open an existing image
- **B.** To copy an existing image
- **C.** To convert an image into grayscale
- **D.** To create a new blank image

<details><summary>Answer</summary>

**D**. `Image.new(mode, size, colour)` creates a new image. Line 10 creates a 100 × 100 white `RGB` image.

</details>

**`2026-jul/w09/q19`** Why is the save() method used?

- **A.** To store the processed image as a file
- **B.** To display the image on the screen
- **C.** To remove unwanted pixels
- **D.** To count the number of pixels

<details><summary>Answer</summary>

**A**. `save()` writes the image to a file, as lines 11 and 13 do.

</details>

**`2026-jul/w09/q20`** Which of the following statements are correct?

- **A.** getpixel() changes the color of a pixel.
- **B.** Image.new() creates a new image with the specified mode and dimensions.
- **C.** putpixel() automatically saves the modified image to disk.
- **D.** Changes made using putpixel() are stored in memory until the image is saved.

<details><summary>Answer</summary>

**A, B, D**

</details>

### `2026-jul/w10/q01`–`q05`: FLAMES

- FLAMES A school is conducting a fun activity where students enter two names to predict their relationship using the classic FLAMES game. The program removes all common letters from the two names, counts the remaining letters, and repeatedly eliminates letters from the word FLAMES until only one letter remains. Based on the final letter, the corresponding relationship is displayed. Study the program below and answer the questions.

```python
1. name1 = input("Enter first name: ").lower().replace(" ", "")
2. name2 = input("Enter second name: ").lower().replace(" ", "")

3. list1 = list(name1)
4. list2 = list(name2)

5. for ch in name1:
6.     if ch in list2:
7.         list1.remove(ch)
8.         list2.remove(ch)

9. count = len(list1) + len(list2)

10. flames = ["F", "L", "A", "M", "E", "S"]

11. while len(flames) > 1:
12.     index = (count - 1) % len(flames)
13.     flames.pop(index)
14.     flames = flames[index:] + flames[:index]

15. result = {
16.     "F": "Friends",
17.     "L": "Love",
18.     "A": "Affection",
19.     "M": "Marriage",
20.     "E": "Enemies",
21.     "S": "Siblings"
22. }

23. print(result[flames[0]])
```

**`2026-jul/w10/q01`** What is the purpose of the statements in Lines 1 and 2?

- **A.** Convert both names to uppercase.
- **B.** Convert names to lowercase and remove spaces.
- **C.** Reverse both names.
- **D.** Remove duplicate letters from the names.

<details><summary>Answer</summary>

**B**. `lower()` makes the name lowercase and `replace(" ", "")` deletes the spaces, so letters compare equally.

</details>

**`2026-jul/w10/q02`** What is stored in the variable count at Line 9?

- **A.** Total number of letters in the original names.
- **B.** Number of common letters.
- **C.** Total number of remaining letters after removing common letters.
- **D.** Number of letters in the word FLAMES.

<details><summary>Answer</summary>

**C**. Line 9 adds the lengths of `list1` and `list2` after the loop has removed the common letters. So `count` is the number of letters left.

</details>

**`2026-jul/w10/q03`** Which statement actually removes a letter from the FLAMES list during each iteration?

- **A.** Line 11
- **B.** Line 12
- **C.** Line 13
- **D.** Line 14

<details><summary>Answer</summary>

**C**. Line 13, `flames.pop(index)`, removes the letter at that position from the list.

</details>

**`2026-jul/w10/q04`** Why is the modulo operator (%) used in Line 12?

- **A.** To convert the index into a floating-point value.
- **B.** To ensure the index always stays within the current size of the list.
- **C.** To sort the FLAMES list.
- **D.** To count the number of common letters.

<details><summary>Answer</summary>

**B**. `(count - 1) % len(flames)` wraps the count around the current length of the list, so the index is always valid, however large `count` is.

</details>

**`2026-jul/w10/q05`** Which of the following statements are correct about the program?

- **A.** The loop in Lines 11–14 continues until only one letter remains in the flames list.
- **B.** The dictionary result maps each FLAMES letter to a relationship.
- **C.** The program removes all vowels before calculating the result.
- **D.** list(name1) in Line 3 converts the first name into a list of characters.

<details><summary>Answer</summary>

**A, B, D**. The loop on lines 11–14 repeats until one letter is left, the dictionary `result` maps each `FLAMES` letter to a relationship, and `list(name1)` makes a list of the characters. The program removes common letters, not vowels.

</details>

### `2026-jul/w10/q06`–`q10`: FLAMES 2

– FLAMES 2 A software company has developed a Team Compatibility Analyzer to compare the names of two employees working on a project. The program removes the common letters from both names, counts the remaining letters, and repeatedly eliminates options from a predefined list until only one category remains. The final category is then displayed as the team's compatibility result. Study the program carefully and answer the following questions.

```python
1. name1 = input("Enter first name: ").lower().replace(" ", "")
2. name2 = input("Enter second name: ").lower().replace(" ", "")

3. list1 = list(name1)
4. list2 = list(name2)

5. for ch in name1:
6.     if ch in list2:
7.         list1.remove(ch)
8.         list2.remove(ch)

9. count = len(list1) + len(list2)

10. flames = ["F", "L", "A", "M", "E", "S"]

11. while len(flames) > 1:
12.     index = (count - 1) % len(flames)
13.     flames.pop(index)
14.     flames = flames[index:] + flames[:index]

15. result = {
16.     "F": "Friendly",
17.     "L": "Leader-Follower",
18.     "A": "Adaptive",
19.     "M": "Mentor-Mentee",
20.     "E": "Efficient",
21.     "S": "Supportive"
22. }

23. print(result[flames[0]])
```

**`2026-jul/w10/q06`** Why are the methods lower() and replace(" ", "") used in Lines 1 and 2 before comparing the names?

- **A.** To sort the letters in each name.
- **B.** To make the comparison independent of letter case and spaces.
- **C.** To remove duplicate characters.
- **D.** To reverse the names before processing.

<details><summary>Answer</summary>

**B**. `lower()` removes the difference between `A` and `a`, and `replace(" ", "")` removes spaces, so the comparison is independent of case and spaces.

</details>

**`2026-jul/w10/q07`** Which statement correctly describes the value stored in count at Line 9?

- **A.** The total number of characters entered by the user.
- **B.** The number of matching characters between the two names.
- **C.** The total number of characters remaining after common letters are removed.
- **D.** The number of elements in the flames list.

<details><summary>Answer</summary>

**C**. Line 9 adds the lengths of the two lists after the loop has removed the common letters, so `count` is the number of characters left.

</details>

**`2026-jul/w10/q08`** Which line changes the size of the flames list during each iteration of the loop?

- **A.** Line 11
- **B.** Line 12
- **C.** Line 13
- **D.** Line 14

<details><summary>Answer</summary>

**C**. Line 13, `flames.pop(index)`, removes one element each time round the loop, which reduces the size of the list by one.

</details>

**`2026-jul/w10/q09`** Suppose count is greater than the current length of the flames list. Why does the program still work correctly?

- **A.** Python automatically increases the size of the list.
- **B.** The modulo operator (%) converts the value into a valid list index.
- **C.** The list is sorted before accessing an element.
- **D.** The while loop ignores values larger than the list size.

<details><summary>Answer</summary>

**B**. The index is `(count - 1) % len(flames)`. The modulo wraps a large count around the list, so the index is always valid.

</details>

**`2026-jul/w10/q10`** Which of the following statements about the program are correct?

- **A.** The while loop continues until only one element remains in the flames list.
- **B.** Removing Line 14 would change the sequence in which elements are eliminated.
- **C.** The dictionary result is used to remove elements from the flames list.
- **D.** The value of count is computed only after common letters have been removed from both names.

<details><summary>Answer</summary>

**A, B, D**. The `while` loop runs while more than one element is left, line 14 rotates the list and so decides which element is counted next, and `count` is computed after the common letters are removed. The dictionary is used only to print the final result.

</details>

### `2026-jul/w10/q11`–`q15`: Wild Life

Wild Life A wildlife research team is studying drone images of a forest to estimate the amount of sunlight reaching the ground. They use a Python program that examines every pixel in an image. For each pixel, the program calculates the average intensity of its Red (R), Green (G), and Blue (B) values. If the average intensity is greater than 127, the pixel is classified as Bright; otherwise, it is classified as Dark. Finally, the program displays the total number of bright and dark pixels in the image. Study the following program and answer the questions.

```python
1. from PIL import Image

2. img = Image.open("sample.jpg")

3. pixels = img.load()

4. width, height = img.size

5. bright = 0
6. dark = 0

7. for x in range(width):
8.     for y in range(height):
9.         r, g, b = pixels[x, y]

10.         average = (r + g + b) // 3

11.         if average > 127:
12.             bright += 1
13.         else:
14.             dark += 1

15. print("Bright Pixels:", bright)
16. print("Dark Pixels:", dark)
```

**`2026-jul/w10/q11`** What is the purpose of Line 3 (pixels = img.load())?

- **A.** It opens the image file.
- **B.** It creates a pixel access object to read individual pixel values.
- **C.** It converts the image into grayscale.
- **D.** It returns the width and height of the image.

<details><summary>Answer</summary>

**B**. `img.load()` returns a pixel access object, so `pixels[x, y]` can read the value of each pixel.

</details>

**`2026-jul/w10/q12`** What is stored in the variables width and height at Line 4?

- **A.** The total number of pixels in the image.
- **B.** The RGB values of the first pixel.
- **C.** The dimensions of the image in pixels.
- **D.** The brightness and darkness counts.

<details><summary>Answer</summary>

**C**. `img.size` is a `(width, height)` pair, so line 4 stores the width and height of the image in pixels.

</details>

**`2026-jul/w10/q13`** What is the value of r, g, and b after executing Line 9?

- **A.** The row, column, and pixel number.
- **B.** The Red, Green, and Blue intensity values of the current pixel.
- **C.** The width, height, and brightness of the image.
- **D.** Three randomly generated numbers.

<details><summary>Answer</summary>

**B**. `pixels[x, y]` returns an `(R, G, B)` tuple for the pixel at that position, and the line unpacks it into `r`, `g` and `b`.

</details>

**`2026-jul/w10/q14`** Why is integer division (//) used in Line 10?

- **A.** To compute the average RGB intensity as a whole number.
- **B.** To increase the brightness of every pixel.
- **C.** To convert the image into grayscale.
- **D.** To avoid using nested loops.

<details><summary>Answer</summary>

**A**. `(r + g + b) // 3` divides and throws away the decimal part, so the average is a whole number that can be compared with 127.

</details>

**`2026-jul/w10/q15`** Suppose an image has 200 × 100 pixels. How many times will the statement in Line 9 execute?

- **A.** 200
- **B.** 100
- **C.** 300
- **D.** 20,000

<details><summary>Answer</summary>

**D**. The outer loop runs 200 times, once for each `x`, and the inner loop runs 100 times for each of those. Line 9 runs `200 × 100 = 20,000` times.

</details>

### `2026-jul/w10/q16`–`q20`: PixelMap Image Quality Inspector

PixelMap Image Quality Inspector A photography studio has developed a PixelMap Image Quality Inspector to identify overexposed regions in digital photographs. The program scans every pixel in an image using the PixelMap, calculates the average intensity of its Red (R), Green (G), and Blue (B) values, and classifies each pixel as Bright or Dark based on a threshold value. At the end, it reports the total number of bright and dark pixels. Study the following program and answer the questions.

```python
1. from PIL import Image

2. img = Image.open("sample.jpg")

3. pixels = img.load()

4. width, height = img.size

5. bright = 0
6. dark = 0

7. for x in range(width):
8.     for y in range(height):
9.         r, g, b = pixels[x, y]

10.         average = (r + g + b) // 3

11.         if average > 127:
12.             bright += 1
13.         else:
14.             dark += 1

15. print("Bright Pixels:", bright)
16. print("Dark Pixels:", dark)
```

**`2026-jul/w10/q16`** Which statement ensures that every pixel in the image is processed exactly once?

- **A.** Line 3
- **B.** Lines 7–8
- **C.** Line 10
- **D.** Line 15

<details><summary>Answer</summary>

**B**. Lines 7–8 are two nested loops over every `x` and `y`, so each pixel position is visited exactly once.

</details>

**`2026-jul/w10/q17`** What is the data type of the value returned by pixels[x, y] for a color image?

- **A.** Integer
- **B.** String
- **C.** Tuple
- **D.** List

<details><summary>Answer</summary>

**C**. For a colour (RGB) image `pixels[x, y]` returns a tuple `(r, g, b)`.

</details>

**`2026-jul/w10/q18`** If the current pixel has RGB values (90, 150, 180), what will be the value of average?

- **A.** 120
- **B.** 140
- **C.** 150
- **D.** 420

<details><summary>Answer</summary>

**B**. `(90 + 150 + 180) // 3 = 420 // 3 = 140`.

</details>

**`2026-jul/w10/q19`** If a pixel has an average intensity of 127, how will it be classified?

- **A.** Bright
- **B.** Dark
- **C.** Both Bright and Dark
- **D.** The program generates an error.

<details><summary>Answer</summary>

**B**. The test is `average > 127`. 127 is not greater than 127, so the `else` branch runs and the pixel counts as dark.

</details>

**`2026-jul/w10/q20`** Which of the following statements are correct?

- **A.** img.load() allows the program to access individual pixel values.
- **B.** The variables bright and dark are used as counters.
- **C.** The nested loops execute once for each row only.
- **D.** The program processes pixels using their (x, y) coordinates.

<details><summary>Answer</summary>

**A, B, D**. `img.load()` gives access to the pixel values, `bright` and `dark` are counters, and each pixel is read with its `(x, y)` position. The nested loops visit every pixel, not only each row.

</details>

---

## E3. Code that was only in the page screenshots

**`2018-jul/w01/q03@portal`** Which of the following can never be an output of the above statement?

```text
pick random (1) to (10)
```

- **A.** 3
- **B.** 6
- **C.** 9
- **D.** 12

<details><summary>Answer</summary>

**D**. `pick random 1 to 10` returns a whole number from 1 to 10 inclusive. 12 is above the top of that range, so it can never come out.

</details>

**`2020-jan/w01/q02`** What is the output of the following

```text
set [t] to (3)
repeat (10)
    change [t] by (3)
end
```

- **A.** 3
- **B.** 33
- **C.** 30
- **D.** None of the above

<details><summary>Answer</summary>

**B**. `t` is set to 3, then `change t by 3` runs 10 times, adding 30. So `t` = 3 + 30 = `33`.

</details>

**`2020-jan/w01/q03`** What is the output of the following

```text
set [t] to (0)
repeat (10)
    change [t] by (-1)
end
```

- **A.** 0
- **B.** 10
- **C.** -10
- **D.** None of the above

<details><summary>Answer</summary>

**C**. `t` starts at 0 and `change t by -1` runs 10 times, so `t` ends at 0 − 10 = `-10`.

</details>

**`2020-jan/w01/q10`** What does the following code compute

```text
set [j] to (0)
set [x] to (2)
set [y] to (9)
set [i] to (y)
repeat until <(i) = (0)>
    set [j] to ((j) + (x))
    set [i] to ((i) - (1))
end
show variable [j]
```

- **A.** multiplication of x and y
- **B.** x to the power y
- **C.** factorial of x
- **D.** None of the above

<details><summary>Answer</summary>

**A**. `j` starts at 0, `x` = 2, and `i` starts at `y` = 9. Each pass adds `x` to `j` and lowers `i` by 1 until `i` = 0, so `j` becomes 9 × 2 = 18: the product of x and y.

</details>

**`2021-jan/w01/q06@portal`** What is the output of the following

```text
set [num] to (100)
repeat (10)
    change [num] by (-2)
end
```

- **A.** 0
- **B.** 100
- **C.** 80
- **D.** 20

<details><summary>Answer</summary>

**C**. `num` starts at 100 and `change num by -2` runs 10 times, so `num` = 100 − 20 = `80`.

</details>

**`2021-jan/w01/q10@portal`** What is the output of the following code?

```text
set [i] to (2)
set [j] to (1)
repeat (10)
    set [x] to ((i) * (j))
    change [j] by (1)
    show variable [x]
    wait (1) secs
end
```

- **A.** Multiplication table of 2
- **B.** Power of 2
- **C.** Factorial of x
- **D.** None of the above

<details><summary>Answer</summary>

**A**. `i` is 2 and `j` starts at 1. Each pass sets `x` to `i * j`, then adds 1 to `j`, so `x` shows 2, 4, 6, …, 20: the multiplication table of 2.

</details>

**`2020-jan/w02/q02`** What is the output of the following code snippet?

```python
a = "Hi"
b = "Arjuna"
c = "Bhimaa"
print("Hi", a, b, c)
```

- **A.** Hi Arjuna Bhimaa
- **B.** Hi Arjuna Hi Bhimaa
- **C.** Hi Hi Arjuna Bhimaa
- **D.** Hi Arjuna Bhimaa Hi

<details><summary>Answer</summary>

**C**. `print` joins its arguments with spaces: the text `Hi`, then the values of `a`, `b` and `c`. The output is `Hi Hi Arjuna Bhimaa`.

</details>

**`2020-jan/w02/q05`** What is the output of the following code?

```python
d=-20
if (d>0)
        print(d)
if (d<0):
        print(-1*d)
```

- **A.** -20
- **B.** Syntax error
- **C.** 20
- **D.** Displays nothing

<details><summary>Answer</summary>

**B**. The line `if (d>0)` has no colon, so Python raises a `SyntaxError` before running anything.

</details>

**`2020-jan/w02/q06`** What does the following code do?

```python
for i in range(5):
        print(i)
```

- **A.** displays numbers from 0 to 4
- **B.** displays numbers from 1 to 5
- **C.** displays numbers from 0 to 5
- **D.** none of the above

<details><summary>Answer</summary>

**A**. `range(5)` gives 0, 1, 2, 3, 4, so the loop prints the numbers from 0 to 4.

</details>

**`2020-jan/w02/q07`** What does the following code do?

```python
for i in range(10):
        print("2 *",(i),"=",2*(i+1))
```

- **A.** displays table of 2
- **B.** syntax error
- **C.** displays table of 10
- **D.** none of the above

<details><summary>Answer</summary>

**D**. The loop prints `2 * 0 = 2`, `2 * 1 = 4`, … because `i` starts at 0 but the result is `2*(i+1)`. The lines do not form a correct table of 2 or of 10.

</details>

**`2020-jan/w02/q08`** What does the following code do?

```python
a=1
for i in range(5):
        a=a*(i+1)
print(a)
```

- **A.** 24
- **B.** 0
- **C.** 120
- **D.** none of the above

<details><summary>Answer</summary>

**C**. `a` starts at 1 and is multiplied by `i+1` for i = 0 to 4, so by 1, 2, 3, 4, 5. The result is 5! = `120`.

</details>

**`2020-jan/w02/q09`** What is the output of the following code?

```python
d=5
while (d>1):
        d=d-1
        print(d),
```

- **A.** 4 3 2 1
- **B.** 5 4 3 2 1
- **C.** 4 3 2 1 0
- **D.** 5 4 3 2 1 0

<details><summary>Answer</summary>

**A**. `d` starts at 5. Each pass subtracts 1 and then prints, so it prints 4, 3, 2, 1. When `d` becomes 1, `d>1` is false and the loop stops.

</details>

**`2020-jan/w02/q10`** What is the output of the following code?

```python
d="a"
for i in range(2):
        d=d+1
        print(d),
```

- **A.** a b c
- **B.** a b
- **C.** b c
- **D.** Error

<details><summary>Answer</summary>

**D**. `d` is the string `"a"`, and `d+1` tries to add an int to a string. Python raises a `TypeError`, so nothing is printed.

</details>

**`2020-sep/w02/q02`** Predict the output for the following code that checks the eligibility to vote.

```python
age=19
if age>=18
        print('Hey! You are eligible to vote')
else:
        print('OOPS! You are not eligible to vote')
```

- **A.** Hey! You are eligible to vote
- **B.** OOPS! You are not eligible to vote
- **C.** Syntax Error: invalid syntax
- **D.** Invalid age

<details><summary>Answer</summary>

**C**. The line `if age>=18` has no colon at the end, so Python raises a `SyntaxError` before running anything.

</details>

**`2020-sep/w02/q05`** For the given code, what is the value of ‘total’ variable at the end of execution?

```python
m1 = '98'
m2 = '79'
m3 = '87'
total = m1 + m2 + m3
print(total)
```

- **A.** syntax error
- **B.** 264
- **C.** 988779
- **D.** 987987

<details><summary>Answer</summary>

**D**. `m1`, `m2` and `m3` are strings, so `+` joins them end to end: `'98' + '79' + '87'` is `'987987'`.

</details>

**`2020-sep/w02/q07`** Which of the following is the output for the given code?

```python
n=5;print(n+5);print(n+5);print(n+5);print(n+5);
```

- **A.** 10 10 10 10
- **B.** 5 10 15 20
- **C.**

  ```python
  10
10
10
10
  ```

- **D.**

  ```python
  5
10
15
20
  ```


<details><summary>Answer</summary>

**C**

</details>

**`2020-sep/w02/q09`** What happens if we key in number 5 for the variable c in the below code?

```python
c=1
while(c==1):
        print('hello')
        c=int(input('Enter choice:0/1:'))
```

- **A.** Loop terminates
- **B.** Continues execution
- **C.** Program restarts execution
- **D.** None of the above

<details><summary>Answer</summary>

**A**. The loop runs while `c==1`. Entering 5 sets `c` to 5, the test becomes false, and the loop ends.

</details>

**`2020-sep/w02/q10`** What is the output of the following code?

```python
d=-20
while(d>0):
        print(d)
if(d<0):
        print(-1*d)
```

- **A.** Infinite loop
- **B.** -20 20
- **C.** 20
- **D.** -20

<details><summary>Answer</summary>

**C**. `d` is -20, so `while(d>0)` is false at once and its body is skipped. `if(d<0)` is true, so it prints `-1*d`, which is `20`.

</details>

**`2021-jan/w02/q04@portal`** What is the output of this code snippet ?

```python
a=3
b=3.0
if(a==b):
  print("numbers are equal")
else:
  print("numbers are not equal")
```

- **A.** numbers are equal
- **B.** numbers are not equal

<details><summary>Answer</summary>

**A**. `a==b` compares values, and 3 equals 3.0, so the condition is true and it prints `numbers are equal`.

</details>

**`2021-jan/w02/q05@portal`** What does the following code snippet print?

```python
for i in range(0,20,2):
  print(i)
```

- **A.** All numbers from 0 to 19
- **B.** Pair of numbers from 0 to 19 whose difference is 2
- **C.** All even numbers from 0 to 19
- **D.** All odd numbers from 0 to 19

<details><summary>Answer</summary>

**C**. `range(0, 20, 2)` starts at 0 and steps by 2, giving 0, 2, 4, …, 18: the even numbers from 0 to 19.

</details>

**`2021-jan/w02/q06@portal`** What is the output of the code snippet given?

```python
a=10
b=100%90
print(a,b)
```

- **A.** 10 100
- **B.** 10 90
- **C.** An error will be generated
- **D.** 10 10

<details><summary>Answer</summary>

**D**. `b = 100 % 90` is the remainder of 100 ÷ 90, which is 10. So `print(a, b)` shows `10 10`.

</details>

**`2021-jan/w02/q07@portal`** Given this code snippet, determine its output?

```python
a=1
for i in range(1,7):
  a=a*(i+1)
print(a)
```

- **A.** 5040
- **B.** 4050
- **C.** 504
- **D.** 405

<details><summary>Answer</summary>

**A**. `i` runs 1 to 6 and `a` is multiplied by `i+1`, so by 2, 3, 4, 5, 6, 7. The result is 7! = `5040`.

</details>

**`2021-jan/w02/q08@portal`** Consider the code snippet given, describe its output?

```python
a=int(input("enter the number"))
for i in range(1,7):
  print(a+i)
```

- **A.** Some 7 numbers
- **B.** First 6 natural numbers
- **C.** Next 6 Numbers after the input number a
- **D.** Next 7 Numbers after the input number a

<details><summary>Answer</summary>

**C**. `i` runs 1 to 6 and the loop prints `a+i`, so it prints the 6 numbers after the input `a` (a+1 … a+6).

</details>

**`2021-jan/w02/q09@portal`** Consider the code snippet given, What might be the output of this?

```python
a=8
while(a>1):
  a=a-1
  print(a)
```

- **A.** Decreasing order of natural numbers from 7
- **B.** Decreasing order of natural numbers from 8
- **C.** Increasing order of natural numbers till 7
- **D.** Increasing order of natural numbers till 8

<details><summary>Answer</summary>

**A**. `a` starts at 8. Each pass subtracts 1 and prints, so it prints 7, 6, 5, 4, 3, 2, 1: natural numbers in decreasing order from 7.

</details>

**`2024-jul/w02/q04`** The following program outputs 722 - For what value of a does the code output 8 ?

```python
a = 7
result = 1
for i in range(a):
    if(i > 0):
        result = result * i
print(result+2)
```

- **A.** 2
- **B.** 1
- **C.** 4
- **D.** 6

<details><summary>Answer</summary>

**C**. The loop multiplies `result` by every `i` from 1 to a−1, giving (a−1)!, then prints it plus 2. For 8 we need (a−1)! = 6 = 3!, so a−1 = 3 and `a` = `4`.

</details>

**`2024-jul/w02/q09`** For which of the following values of name and age variables does the following code print ”You are lucky”?

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
flag = "False"
if(age >= 18):
    flag = "True"
else:
    flag = "False"
counter = 0
for i in name:
    if(i == "a"):
        counter += 1
if(flag == "True"):
    if(counter > 2):
        print("You are lucky")
    else:
        print("You are not lucky")
```

- **A.** aryan, 20
- **B.** arjun, 19
- **C.** aakash, 17
- **D.** aatreya, 18

<details><summary>Answer</summary>

**D**. It prints `You are lucky` only if the age is at least 18 and the name has more than 2 letters `a`. `aatreya` is 18 and has three a's.

</details>

**`2025-jan/w02/q04`** The following program outputs 723 -

```python
def mystery(container):
  result = []
  for i in range(len(container)):
    if i % 2 != 0:
      result.append(container[i] * 4)
    else:
      result.append(container[i] * (-1))
  return result
```

- **A.** 1
- **B.** 2
- **C.** 6
- **D.** 5

<details><summary>Answer</summary>

**C**. The program prints (a−1)! + 3. We need 123, so (a−1)! = 120 = 5!, which means a−1 = 5 and `a` = `6`.

</details>

**`2025-jan/w02/q08`** The following program might/might not have an infinite loop. Does the program have infinite loop ?

```python
n = ?
k = 0
a = []
b = 0
while (n != 0):
    k = k + (n % 10)
    a.append(n % 10)
    n = n // 10
a.sort()
for i in a:
    b = b + i
if(b != k):
    print("PYTHON IS FUN")
else:
    print("PYTHON IS BORING")
```

- **A.** No, the program doesn’t have infinite loop.
- **B.** Yes, it can be prevented by updating the value of a before the if block at line 3.
- **C.** Yes, it can be prevented by removing both the if blocks inside the while loop.
- **D.** Yes, but it cannot be prevented.

<details><summary>Answer</summary>

**B**

</details>

**`2020-jan/w03/q02`** The below code displays

```python
for i in range(100):
    if(i%10==0):
        print(i)
```

- **A.** all numbers from 1 to 100 which are divisible by 10
- **B.** all numbers from 1 to 99 which are divisible by 10
- **C.** all numbers from 1 to 110 which are divisible by 10
- **D.** none of the above

<details><summary>Answer</summary>

**D**. `range(100)` starts at 0, so the code prints 0, 10, 20, …, 90. That includes 0 and stops at 90, so none of the listed ranges matches.

</details>

**`2020-jan/w03/q03`** What is the output of the following code?

```python
list1=["hi","we","are","the","elements","in","a","list"]
for i in list1:
    print(list1[i]),
```

- **A.** hi hi hi hi hi hi hi hi
- **B.** hi we are the elements in a list
- **C.** hi
- **D.** error

<details><summary>Answer</summary>

**D**. `for i in list1` makes `i` a word, such as `"hi"`, and `list1[i]` indexes a list with a string. Python raises a `TypeError`.

</details>

**`2020-jan/w03/q04`** What is the output of the following code?

```python
list1=["hi","we","are","the","elements","in","a","list"]
for i in range(4):
    print(list1[i]),
```

- **A.** hi we are the elements in a list
- **B.** hi we are the elements
- **C.** hi we are the
- **D.** hi we are

<details><summary>Answer</summary>

**C**. `range(4)` gives i = 0, 1, 2, 3, so it prints `list1[0]` to `list1[3]`: `hi we are the`.

</details>

**`2020-jan/w03/q07`** Given a variable word which is a string where no letter is repeated, what does the following code snippet do?

```python
import random
word=input("Enter a word in which no letter is repeated")
l=[]
total=1
for i in range(1,len(word)+1):
    total=total*i
while(len(l)<total):
    j="".join(random.sample(word,len(word)))
    l.append(j)
for each in l:
    print each
```

- **A.** keeps printing the jumbled form of the word in an infinite loop
- **B.** shows all the jumbled forms of the word where some forms might be repeated
- **C.** shows some jumbled forms of the word where some forms might be repeated as well
- **D.** shows all unique jumbled forms of the word including the original word as well

<details><summary>Answer</summary>

**C**. The loop keeps adding random arrangements of the word until the list has n! items (n = length of the word). Random picks can repeat, so some jumbled forms may appear twice while others never appear.

</details>

**`2020-jan/w03/q08`** Assuming, there is no file named "file.txt" on my computer, what does the following code do?

```python
with open("file.txt","w") as f:
    print(f.read())
    f.write("Hey! I am writing");
f.close()
```

- **A.** Creates a file named file.txt and adds “Hey! I am writing” to it
- **B.** Shows an error because file does not exist
- **C.** Shows an error because file in not opened in the reading mode
- **D.** None of the above

<details><summary>Answer</summary>

**D**. The lines inside `with` are indented unevenly (`print` deeper than `f.write`), so Python raises an `IndentationError` before anything runs. That is none of the listed outcomes.

</details>

**`2020-jan/w03/q09`** Assuming, there is no file named "file.txt" on my computer, what does the following code do?

```python
with open("fi.txt","w") as f:
    f.write("Hey! I am writing.");
f.close()
with open("fi.txt","w") as f:
    f.write("Hey I am writing the second line.");
f.close()
with open("fi.txt","r") as f:
    print(f.read())
f.close()
```

- **A.** Shows error
- **B.** Displays: Hey I am writing the second line
- **C.** Displays: Hey! I am writing.Hey I am writing the second line.
- **D.** Displays: Hey! I am writing.

<details><summary>Answer</summary>

**B**. The first block writes `Hey! I am writing.` to `fi.txt`. The second `"w"` open erases the file and writes the second line. The final read prints only `Hey I am writing the second line.`

</details>

**`2020-jan/w03/q10`** What is the output of the following code?

```python
with open("f.txt","w") as myfile:
    myfile.write("0110");
myfile.close()

with open("f.txt","r") as myfile:
    l=list(myfile.read());
    sum1=0
    for each in l:
        sum1=sum1+int(each)
    print(sum1)
myfile.close()
```

- **A.** Displays 1
- **B.** Displays 2
- **C.** Displays 0
- **D.** Shows error

<details><summary>Answer</summary>

**B**. The file gets `"0110"`. `list(...)` splits it into `['0','1','1','0']`, and the loop adds `int` of each: 0 + 1 + 1 + 0 = `2`.

</details>

**`2020-sep/w03/q04`** Pick the relevant output for the given code.

```python
n=[1,4,2,8,21,17]
n.reverse()
print(n)
```

- **A.** [1, 2, 4, 8, 17, 21]
- **B.** [21, 17, 8, 4, 2, 1]
- **C.** [17, 21, 8, 2, 4, 1]
- **D.** [1, 4, 2, 8, 21, 17]

<details><summary>Answer</summary>

**C**. `n.reverse()` reverses the list in place, so `n` becomes `[17, 21, 8, 2, 4, 1]`.

</details>

**`2024-jul/w03/q02`** In the below code - For what value of n does the program print 21 ? 7

```python
n= ?
a = []
for i in range(n):
    l1 = []
    p = 0
    for j in range(i):
        l1.append(j)
    for k in l1:
        p+=1
    a.append(p)
k=0
for l in a:
    k+=1
print(k)
```

<details><summary>Answer</summary>

**7**. Pass `i` builds `l1` of length `i`, so `p = i` and `a` becomes `[0, 1, …, n-1]`. `k` then adds up the items of `a`: n(n-1)/2. For 21 we need n(n-1) = 42, so n = 7.

</details>

**`2024-jul/w03/q08`** What does the following code print forn = 3?

```python
n = ?
k = 0
a = []
b = 0
while (n != 0):
    k = k + (n % 10)
    a.append(n % 10)
    n = n//10
a.sort()
for i in a:
    b = b + i
if(b == k):
    print("WE KNOW THE WISDOM OF SERIES")
else:
    print("WE ARE YET TO KNOW MANY THINGS")
```

- **A.** WE KNOW THE WISDOM OF SERIES
- **B.** WE ARE YET TO KNOW MANY THINGS

<details><summary>Answer</summary>

**A**. For n = 3: `k` is 3, `a` is `[3]`, and `b` is the sum of `a`, also 3. `b == k`, so it prints `WE KNOW THE WISDOM OF SERIES`.

</details>

**`2025-jan/w03/q02`** In the below code - 45

```python
n= ?
a = []
for i in range(n):
    l1 = []
    p = 0
    for j in range(i):
        l1.append(j)
    for k in l1:
        p+=1
    a.append(p)
k=0
for l in a:
    k+=1
print(k)
```

<details><summary>Answer</summary>

**5**. Pass `i` builds `l1` of length `i`, so `p = i` and `a` becomes `[0, 1, …, n-1]`. `k` adds up `a`: n(n-1)/2. For 10 we need n(n-1) = 20, so n = 5.

</details>

**`2025-jan/w03/q08`** What does the following code print for n = 256?

```python
n = ?
k = 0
a = []
b = 0
while (n != 0):
    k = k + (n % 10)
    a.append(n % 10)
    n = n // 10
a.sort()
for i in a:
    b = b + i
if(b != k):
    print("PYTHON IS FUN")
else:
    print("PYTHON IS BORING")
```

- **A.** PYTHON IS BORING
- **B.** PYTHON IS FUN

<details><summary>Answer</summary>

**A**. `k` is the sum of the digits of `n`, and `b` is the sum of the same digits (sorted). They are always equal, so `b != k` is false and it prints `PYTHON IS BORING`.

</details>

**`2020-jan/w04/q01`** What does the check_magic() function in the following code do

```python
def check_magic():
    num=[1,2,3,4,5,6,7,8,9]
    a00=0
    a01=0
    a10=0
    a11=0
    for i in range(0,9):
        for j in range(0,9):
            for k in range(0,9):
                for l in range(0,9):
                    a00=num[i]
                    a01=num[j]
                    a10=num[k]
                    a11=num[l]
                    l=[a00,a01,a10,a11]

                    print a00,'\t',a01,'\n',a10,'\t',a11
                    print '\n' 
```

- **A.** displays all 2 × 2 matrices where elements are from 1 to 9.
- **B.** displays all 2 × 2 matrices where elements are from 1 to 9 but no element is repeated
- **C.** displays magic squares of size 2
- **D.** none of the above

<details><summary>Answer</summary>

**A**. Four nested loops each run over all of `num` (1 to 9), and print every 2 × 2 grid `a00 a01 / a10 a11`. Repeats are allowed, so it prints all 2 × 2 matrices with elements from 1 to 9.

</details>

**`2020-jan/w04/q02`** What does the following code do?

```python
l1 = ["apple", "banana" , "kiwi" , "orange"]
l2 = ["watermelon", "melon", "kiwi", "banana"]
cmn=[]
for i in range(4):
    if(l1[i]==l2[i]):
        cmn.append(l1[i])
print(cmn)
```

- **A.** displays common fruits in both the lists l1 and l2
- **B.** displays fruits which are in l1 but not in l2
- **C.** displays fruits which are in l2 but not in l1
- **D.** none of the above

<details><summary>Answer</summary>

**D**. The loop compares `l1[i]` with `l2[i]`, the fruits at the same position. Only `kiwi` sits at index 2 in both lists, so it prints `['kiwi']`. That is not the same as the fruits common to both lists.

</details>

**`2020-jan/w04/q04`** What does the following function do

```python
def leap(year):
    if(year%400==0 or (year%100!=0 and year%4==0)):
        return 1
    else:
        return 0
```

- **A.** returns true for century year and false for non century year
- **B.** returns true for leap year and false for non leap year
- **C.** returns false for century year and true for non century year
- **D.** none of the above

<details><summary>Answer</summary>

**B**. The condition is true for years divisible by 400, or divisible by 4 but not by 100. That is the leap-year rule, so the function returns 1 for leap years and 0 otherwise.

</details>

**`2020-jan/w04/q07`** What does the following code do?

```python
s1=input("Enter a string")
s2=input("Enter another string")
for each in list(s2):
    for each2 in list(s1):
        if(each==each2):
            print("yes")
            break
```

- **A.** prints yes if both strings are same
- **B.** prints yes if both strings have atleast one common character
- **C.** prints yes if first string is contained in the second
- **D.** none of the above

<details><summary>Answer</summary>

**B**. The code takes each character of `s2` and looks for it in `s1`. When a match is found it prints `yes` and breaks out of the inner loop. So it reports `yes` whenever the strings share a character.

</details>

**`2020-jan/w04/q08`** Which numbers from 1 to 100 does the following code print?

```python
for i in range(1001):
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        print(i)
```

- **A.** prime numbers
- **B.** perfect squares
- **C.** numbers which are factorial of some other number
- **D.** perfect cubes

<details><summary>Answer</summary>

**A**. For each `i`, the inner loop looks for a divisor `j` from 2 to i−1. If none divides `i`, `f` stays 0 and `i` is printed. So it prints the numbers with no such divisor: the primes (and 0 and 1).

</details>

**`2020-jan/w04/q09`** Which numbers from 1 to 100 does the following code print?

```python
for i in range(1001):
    f=0
    for j in range(2,i):
        if(j*j==i):
            f=1
            break
    if(f==1):
        print(i)
```

- **A.** prime numbers
- **B.** perfect squares
- **C.** numbers which are factorial of some other number
- **D.** perfect cubes

<details><summary>Answer</summary>

**B**. The loop sets `f = 1` when some `j` from 2 up satisfies `j*j == i`. Numbers with `f == 1` are printed, so it prints perfect squares such as 4, 9, 16.

</details>

**`2021-jan/w04/q03@portal`** Assuming that num is always a 2-digit number, what is the output of the following code?

```python
num = int(input())
temp = num
x = len(str(num))
z = 0
while temp > 0:
    y = temp % 10
    z += y ** x
    temp //= 10
if num == z:
    print(num)
```

- **A.** Prints the number if the sum of squares of its digits is the number itself
- **B.** Prints the number if the sum its digits is the number itself
- **C.** Prints the number if the product of its digits is the number itself
- **D.** Prints nothing

<details><summary>Answer</summary>

**A**. `x` is the number of digits (2) and `z` adds up each digit raised to the power `x`. So it prints `num` when the sum of the squares of its digits equals `num`.

</details>

**`2024-jul/w04/q07`** What task does function1() perform ?

```python
def function1(number):
    list1 = []
    for i in range(1, number):
        if number % i == 0:
            list1.append(i)
    return list1


def function2(n1, n2):
    flag = False
    list2 = []
    for i in function1(n1):
        for j in function1(n2):
            if i == j:
                flag = True
                list2.append(i)
    if len(list2) > 0:
        print("Completed")
```

- **A.** Calculate factorial of number n.
- **B.** Calculate factors of number n.
- **C.** Calculate prime factors of number n.
- **D.** Calculate factors of number n excluding n.

<details><summary>Answer</summary>

**D**. `function1(number)` collects every `i` from 1 to number−1 that divides `number`. That is the list of its factors, leaving out the number itself.

</details>

**`2024-jul/w04/q08`** For what n1,n2 flag will the variable flag inside function2() be not equal to true ?

```python
# Uses the program shown with 2024-jul/w04/q07:
def function1(number):
    list1 = []
    for i in range(1, number):
        if number % i == 0:
            list1.append(i)
    return list1


def function2(n1, n2):
    flag = False
    list2 = []
    for i in function1(n1):
        for j in function1(n2):
            if i == j:
                flag = True
                list2.append(i)
    if len(list2) > 0:
        print("Completed")
```

- **A.** 2,3
- **B.** 0,0
- **C.** 1,1
- **D.** 1,0

<details><summary>Answer</summary>

**B, C, D**. `flag` becomes `True` only if the two factor lists share a value. `function1(0)` and `function1(1)` are empty (`range(1, 0)` and `range(1, 1)`), so for (0,0), (1,1) and (1,0) there is no match. For (2,3) both lists are `[1]`, so `flag` is `True`.

</details>

**`2024-jul/w04/q10`** If numbers of pairs of primes which result in function2 to print ”Completed” are greater than 0, Can we edit the code in function2() so that ”Completed” is never printed for any pair of primes ?

(Same program as the previous card.)

- **A.** Yes, we can change the logic for setting flag variable to True.
- **B.** Yes, we can change/increase the threshold for length oflist2 in the last if block.
- **C.** No, it is logically not possible.
- **D.** Yes, we can change the initial value of flag to True, instead of False.

<details><summary>Answer</summary>

**B**. The print depends only on `len(list2)`. For prime pairs `list2` has length 1, so raising the threshold to `> 1` stops it from ever printing. Changing `flag` has no effect on the print.

</details>

**`2025-jan/w04/q08`** For what n1, n2 will the variable flag inside mystery2() be equal to True?

```python
# Uses the program shown with 2025-jan/w04/q07:
def mystery1(number):
    list1 = []
    for i in range(1, number):
        if number % i == 0:
            list1.append(i)
    return list1

def mystery2(n1,n2):
    flag = False
    list2 = []
    for i in mystery1(n1):
        for j in mystery1(n2):
            if i == j:
                flag = True
                list2.append(i)
    if len(list2) > 1:
        print("Completed")
```

- **A.** 1,2
- **B.** 2,3
- **C.** 3,4
- **D.** 0,0

<details><summary>Answer</summary>

**B, C**. `flag` becomes `True` only if the two factor lists share a value. For (2,3) both lists are `[1]`, and for (3,4) the lists are `[1]` and `[1, 2]`, so they share 1. For (1,2) and (0,0) one list is empty.

</details>

**`2025-jan/w04/q10`** If numbers of pairs of primes which result in mystery2 to print ”Completed” are

(Same program as the previous card.)

- **A.** Yes, we can change the logic for setting flag variable to False.
- **B.** No, it is logically not possible.
- **C.** Yes, we can change/decrease the threshold for length of list2 in the last if block.
- **D.** Yes, we can change the initial value of flag to False, instead of True.

<details><summary>Answer</summary>

**C**. The print depends only on `len(list2)`. For prime pairs it is 1, so lowering the threshold from `> 1` to `> 0` makes it print. Changing `flag` has no effect on the print.

</details>

**`2020-jan/w05/q01`** What does the following code do?

```python
import random
def get_gates():
    r=random.randint(0,2)
    r1=random.randint(0,2)
    while(r==r1):
        r=random.randint(0,2)
    l=['x','x','x']
    l[r]='c'
    l[r1]='c'
    ind =[0,1,2]
    for each in ind:
        if(each!=r1 and each!=r):
            l[each]='g'
    print(l)

get_gates()
```

- **A.** creates a list where two random elements are ‘c’ and the other element is ‘g’
- **B.** creates a list where two random elements are ‘g’ and the other element is ‘c’
- **C.** creates a list where one random elements is ‘c’ and the other element is ‘g’
- **D.** none of the above

<details><summary>Answer</summary>

**A**. `r` and `r1` are different random positions in a three-slot list `l` of `'x'`. Both positions get `'c'`, and the remaining slot gets `'g'`. So the list has two random `'c'` and one `'g'`.

</details>

**`2020-jan/w05/q04`** For the code below, which of the statement in the options is false?

```python
t=[]
for i in range(10):
    a=int(input("Enter the number you want to insert in the list"))
    if(len(t)==0):
        t.append(a)
    else:
        if(a>t[len(t)-1]):
            t.append(a)
print(t)
```

- **A.** The loop runs exactly 10 times
- **B.** All the integers taken as input from the user need not be in the list l
- **C.** The list l consists of exactly 10 elements at the end of the program
- **D.** The list l printed in the last line is a sorted list

<details><summary>Answer</summary>

**C**. The code adds a number only when it is larger than the last item. Numbers that are not larger are skipped, so the list can end with fewer than 10 elements. It is sorted in increasing order, and the loop runs 10 times.

</details>

**`2020-jan/w05/q06`** Assuming that “bins” represents a dictionary where key is the number of a bin and value represents the number of balls present in the corresponding bin, what is the output of the following code?

```python
min_=0
min_i=-1
for each in bins:
    if(bins[each]>min_):
        min_i=each
        min_=bins[each]
print(min_i)
```

- **A.** Displays the maximum number of balls present in any bin
- **B.** Displays the number of the bin containing maximum balls
- **C.** Displays the number of the bin containing minimum balls
- **D.** None of the above

<details><summary>Answer</summary>

**B**. The loop keeps the largest value seen in `min_` and the key where it occurred in `min_i`, because it tests `bins[each] > min_`. Despite its name, it prints the bin number that holds the most balls.

</details>

**`2020-jan/w05/q07`** Assuming that “bins” represents a dictionary where key is the number of a bin and value represents the number of balls present in the corresponding bin, what is the output of the following code?

```python
def mbin():
    max_=0
    max_i=-1
    for each in bins:
        if(bins[each]>max_):
            max_i=each
            max_=bins[each]
    print(max_i)
    return max_i

while(len(bins)>0):
    b=mbin()
    del(bins[b])
```

- **A.** Displays the maximum number of balls present in any bin
- **B.** Displays bins in the ascending order of the number of balls they have
- **C.** Displays bins in the descending order of the number of balls they have
- **D.** None of the above

<details><summary>Answer</summary>

**C**. `mbin()` finds the bin with the most balls, prints its number, and `del` removes it. The loop repeats until the dictionary is empty, so the bins print from the most balls to the fewest.

</details>

**`2020-jan/w05/q08`** The above code generates numbers from

```python
def find(list1,num):
    for each in list1:
        if(each!=num):
            print(each)
        else:
            break

t=[]
for i in range(100000):
    t.append(i)

find(t,99999)
```

- **A.** 0 to 99999
- **B.** 0 to 100000
- **C.** 0 to 99998
- **D.** 1 to 99998

<details><summary>Answer</summary>

**C**. `find` prints every item not equal to `num` and stops at the first match. `t` holds 0 to 99999 and `num` is 99999, so it prints 0 up to 99998.

</details>

**`2020-jan/w05/q10`** Assuming that “bins” represents a dictionary where key is the number of a bin and value represents the number of balls present in the corresponding bin, what plot does the following code generate?

```python
import matplotlib.pyplot as plt
val=bins.values()
x=[]
y=[]
print(val)
for each in list(set(val)):
    x.append(each)
    y.append(val.count(each))
    print(each,val.count(each))
plt.plot(x,y)
plt.show()
```

- **A.** X axis: Number of balls, Y axis: Number of bins having as many balls as specified by X axis
- **B.** X axis: Bin number, Y axis: Number of balls in the bin whose number is specified by X axis
- **C.** X axis: Ball number, Y axis: The bin number which contained the ball whose number is specified by the X axis
- **D.** None of the above

<details><summary>Answer</summary>

**D**. `val` is `bins.values()`. In Python 3 that is a view with no `.count()`, so `val.count(each)` raises an `AttributeError` and no plot appears. (With a list, x would be the ball counts and y the number of bins with that count.)

</details>

**`2020-sep/w05/q08`** The following code takes a list as input and prints the sorted list as an output. The outer for loop is to count the number of iterations. What is the purpose of the inner for loop?

```python
def bubble(mylist):
    n=len(mylist)
    for i in range(n):
        for j in range(0,n-i-1):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    print(mylist)
```

- **A.** To fetch the pair of consecutive elements to be compared
- **B.** Index of the element for which the right position is to be found
- **C.** To identify the max element
- **D.** To check if the list is sorted

<details><summary>Answer</summary>

**A**. The inner loop runs `j` from 0 to n−i−2 and compares `mylist[j]` with `mylist[j+1]`. So it fetches each pair of consecutive elements to compare, and swaps them if needed.

</details>

**`2021-jan/w05/q09@portal`** Which are the given statements precisely explains the action of the given code?

```python
import random
roll_the_dice = "y"
while roll_the_dice== "y" or x+y==12:
    print ("Rolling the dices...")
    print ("The values are....")
    x = random.randint(1, 6)
    print (x)
    y = random.randint(1, 6)
    print (y)
    roll_the_dice = input("Do you want to roll the dices?")
```

- **A.** rolls the dices as long as the input is ’y’
- **B.** rolls the dices until the sum of their face values is 12
- **C.** rolls the dices as long as the input is ’y’ or the sum of their face values is 12
- **D.** rolls the dices inﬁnitely

<details><summary>Answer</summary>

**C**. The loop condition is `roll_the_dice == "y" or x+y == 12`. It keeps rolling while the player answers `y`, or while the last two dice add up to 12.

</details>

**`2021-jan/w05/q10@portal`** What will be the output of the following code?

```python
some_list = {'abc':10, 'xyz':3, 'pqr':2}
s = ''
for i in some_list:
    s = s + str(some_list[i]) + ' '
    s1 = s[:-1]
print(s1[::-1])
```

- **A.** 3 2
- **B.** 2 3
- **C.** 2 3 01
- **D.** 01 3 2

<details><summary>Answer</summary>

**C**. The loop goes over the keys. Each pass adds `str(value) + ' '` to `s`, giving `'10 3 2 '`. `s[:-1]` drops the last space, and `s1[::-1]` reverses it: `2 3 01`.

</details>

**`2024-jul/w05/q06`** What does this program print in the end ?

```python
import random
n=10
counter = 0
for i in range(n):
    choices = ["rock", "paper", "scissors"]
    choice1 = random.choice(choices)
    choice2 = random.choice(choices)
    if choice1 == choice2:
        counter += 1
print(counter/n)
```

- **A.** Fraction of throws where both players showed different symbol(rock/paper/scissors)
- **B.** Fraction of throws where both players showed rock.
- **C.** Fraction of throws where both players showed same symbol(rock/paper/scissors)
- **D.** Fraction of throws where both players showed paper.

<details><summary>Answer</summary>

**C**. Each of the 10 rounds picks two random choices and adds 1 to `counter` when they are equal. It prints `counter/n`: the fraction of throws where both players showed the same symbol.

</details>

**`2025-jan/w05/q06`** What does this program print in the end ?

```python
import random
n = 10
counter = 0
for i in range(n):
  choices = ["rock", "paper", "scissors"]
  choice1 = random.choice(choices)
  choice2 = random.choice(choices)
  if choice1 != choice2:
    counter += 1
print(counter/n)
```

- **A.** Fraction of throws where both players showed different symbol(rock/paper/scissors)
- **B.** Fraction of throws where both players showed rock.
- **C.** Fraction of throws where both players showed same symbol(rock/paper/scissors)
- **D.** Fraction of throws where both players showed paper.

<details><summary>Answer</summary>

**A**. Each of the 10 rounds picks two random choices and adds 1 to `counter` when they differ (`!=`). It prints `counter/n`: the fraction of throws where the two players showed different symbols.

</details>

**`2020-jan/w06/q01`** Give that the statement chr(ord(alpha) + i) returns the character(alphabet or a special character) at the location i ahead than the alphabet alpha, eg, chr(ord(’a’)+1) returns ‘b’; what is the output of the following code?

```python
def encrypt(ltr,key):
    l=[]
    for each in list(ltr):
        l.append(chr(ord(each) + 1))
    return ("".join(l))

letter_body="ABCDEFGH"
d=encrypt(letter_body,4)
print(d)
```

- **A.** ABCDEFGH
- **B.** BCDEFGHI
- **C.** EFGHIJKL
- **D.** none of the above

<details><summary>Answer</summary>

**B**. `encrypt` adds 1 to each letter's code (the `key` of 4 is never used). So ABCDEFGH becomes BCDEFGHI.

</details>

**`2020-jan/w06/q02`** What does the following code do?

```python
def guess(num):
    a=input("Guess a number")
    if(a==num):
        print("SUCCESS")
    else:
        guess(num)

guess(10)
```

- **A.** Keeps asking the user to guess a number until the user guesses 10
- **B.** The computer generates a random number r and keeps it. The user is repeatedly prompted to enter a number. If the user enters r, the code says success and ends, else the prompting is continued.
- **C.** Enters an infinite loop
- **D.** The computer generates a random number r and keeps it. The user is repeatedly prompted to enter a number. If the user enters r, the code says success and ends, else the computer generates a new random number r and thereafter the prompting is continued.

<details><summary>Answer</summary>

**C**. `input` returns a string, and `a == num` compares it with the number 10. They are never equal, so the function calls itself again and again. It never ends.

</details>

**`2020-jan/w06/q06`** The following code represents

```python
import random
def search(l,loc,item):
    if(loc<0):
        loc=0
    if(l[loc]==item):
        print("Found",item,"at index",loc)
        return
    if(loc==len(l)-1):
        print("Element not present")
        return(0)
    else:
        return(search(l,loc+1,item))

l=[1,2,3,4,5,6,7,8,9]
search(l,-11,3)
```

- **A.** recursive algorithm for linear search an element in a list
- **B.** recursive algorithm for binary search an element in a list
- **C.** non-recursive algorithm for linear search an element in a list
- **D.** none of the above

<details><summary>Answer</summary>

**A**. The function checks the item at `loc`, and if it is not there, calls itself with `loc+1`. That is a recursive linear search.

</details>

**`2020-jan/w06/q08`** The following code to its best, represents a scenario

```python
def func(i):
    print(i)
    if(i==0):
        print("OVER")
    else:
        func(i/2)
```

- **A.** A cake getting eaten by half of its current amount every time
- **B.** A student attempting alternate questions, starting from a given question
- **C.** Viruses doubling inside a body and killing the person once their population becomes 128 or more.
- **D.** Metro train serving 128 stations to and fro

<details><summary>Answer</summary>

**A**. The function prints `i` and calls itself with `i/2`, so the value halves each time, like a cake that is halved again and again.

</details>

**`2020-jan/w06/q09`** The following code to its best, represents a scenario

```python
def func(i):
    print(i)
    if(i>128):
        print("OVER")
    else:
        func(2*i)
```

- **A.** A cake getting eaten by half of its current amount every time
- **B.** A student attempting alternate questions, starting from a given question
- **C.** Viruses doubling inside a body and killing the person once their population becomes 128 or more.
- **D.** Metro train serving 128 stations to and fro

<details><summary>Answer</summary>

**C**. The function prints `i`, doubles it, and stops when `i > 128`. That is a population that doubles until it reaches 128 or more.

</details>

**`2020-jan/w06/q10`** The following code to its best, represents a scenario

```python
def func(i,f):
    print(i)
    if(i==0):
        f=1
        func(i+1,f)
    if(i==128):
        f=-1
        func(i-1,f)
    if(f==1):
        func(i+1,f)
    if(f==-1):
        func(i-1,f)
```

- **A.** A cake getting eaten by half of its current amount every time
- **B.** A student attempting alternate questions, starting from a given question
- **C.** Viruses doubling inside a body and killing the person once their population becomes 128 or more.
- **D.** Metro train serving 128 stations to and fro

<details><summary>Answer</summary>

**D**. The function counts up from 0 to 128 with `f = 1`, then at 128 sets `f = -1` and counts back down. That is a train that runs 128 stations and then back again.

</details>

**`2020-sep/w06/q04`** What is the output for the given code?

```python
import numpy
mat=numpy.array([[1,2,3],[4,5,6],[7,8,9]])

def add(mat):
        sum=0
        for i in range(2):
                for j in range(2):
                        if i==j:
                                sum=sum+mat[i][j]
        return(sum)

print(add(mat))
```

- **A.** 15
- **B.** 9
- **C.** 6
- **D.** 24

<details><summary>Answer</summary>

**C**. `add` loops `i` and `j` over 0 and 1 and adds `mat[i][j]` only when `i == j`. That is `mat[0][0] + mat[1][1]` = 1 + 5 = `6`.

</details>

**`2021-jan/w06/q02@portal`** What is the result of the following code if the input is COMPUTING?

```python
result = ""
text = input()
shift = 4
for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
        result += chr((ord(char) + shift-65) % 26 + 65)

    else:
        result += chr((ord(char) + shift - 97) % 26 + 97)
```

- **A.** FRPSXWLQJ
- **B.** HTRUZYNSL
- **C.** GSQTYXMRK
- **D.** none of the above

<details><summary>Answer</summary>

**C**. The code adds a shift of 4 to every letter and wraps around the alphabet: C→G, O→S, M→Q, P→T, U→Y, T→X, I→M, N→R, G→K. That gives `GSQTYXMRK`.

</details>

**`2021-jan/w06/q04@portal`** What is the output of the following code?

```python
num1 = int(input())
num2 = int(input())
i = 1
while(i <= num1 and i <= num2):
    if(num1 % i == 0 and num2 % i == 0):
        output = i
    i = i + 1
```

- **A.** Greatest common factor of num1 and num2
- **B.** Least common factor of num1 and num2
- **C.** Least common multiple of num1 and num2
- **D.** Greatest common multiple of num1 and num2

<details><summary>Answer</summary>

**A**. The loop tries every `i` from 1 up to the smaller number. It keeps the last `i` that divides both numbers, so `output` ends as their greatest common factor.

</details>

**`2021-jan/w06/q05@portal`** What does the following python code compute?

```python
def xyz(a, b):
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a
    if a == 1:
        return b
    return a + xyz(a, b - 1)
```

- **A.** power of a raised to b
- **B.** sum of a and b
- **C.** product of a and b
- **D.** none of the above

<details><summary>Answer</summary>

**C**. `xyz(a, b)` adds `a` to `xyz(a, b-1)`, so it adds `a` a total of `b` times: it computes the product a × b.

</details>

**`2021-jan/w06/q09@portal`** What is the output of the following python code?

```python
def abc(num):
    return num * abc(num-1)

print(abc(4))
```

- **A.** 24
- **B.** Runs inﬁnitely
- **C.** Recursion error
- **D.** 1

<details><summary>Answer</summary>

**C**. `abc(num)` calls `abc(num-1)` forever, because there is no base case. Python stops it with a `RecursionError`.

</details>

**`2024-jul/w06/q03`** What is the output of following code ?

```python
def func(x):
    return x * 2

def func(x, y=3):
    return x + y

print(func(5))
```

- **A.** 10
- **B.** 8
- **C.** 5
- **D.** Error

<details><summary>Answer</summary>

**B**. The second `def func` replaces the first, so `func(5)` uses `x + y` with `y = 3`: `8`.

</details>

**`2025-jan/w06/q03`** What is the output of following code ?

```python
def func(x):
  return x ** 2

def func(x, y=1):
  return x**2 + y

print(func(5))
```

- **A.** Error
- **B.** 25
- **C.** 26
- **D.** 5

<details><summary>Answer</summary>

**C**. The second `def func` replaces the first, so `func(5)` is `5**2 + 1` = `26`.

</details>

**`2020-jan/w07/q06`** Imagine a single player snakes and ladders game. The code below represents

```python
import random

def play(psn):
    snake_begin=-1
    snake_end=-1
    while(snake_begin <= snake_end):
        snake_begin=random.randint(1,99)
        snake_end=random.randint(1,99)
    print("Snake from",snake_begin,"to",snake_end)
    r = random.randint(1,6)
    print("Dice rolled:",r)
    if(psn==0):
        if(r==1 or r==6):
            psn=1
    else:
        psn=psn+r
    print("Position=",psn)
    input()
    if(psn==snake_begin):
        print("Bitten by snake")
        psn=snake_end
    if(psn>=100):
        print("You won")
        return
    play(psn)

position=0
print("Position=",position)
play(position)
```

- **A.** A snakes and ladders game with one snake whose position remains constant while the player is playing. The position also remains the same during any subsequent plays (i.e. the game board does not change while you sleep and play again the next day).
- **B.** A snakes and ladders game with one snake whose position remains constant while the player is playing.However, the position can change during any subsequent plays (i.e. the game board might change while you sleep and play again the next day).
- **C.** A snakes and ladders game with one snake where the snake can change its position during the game and also during any subsequent plays (a board game where the snakes keep moving). Further, the snake can bite you any number of times.
- **D.** A snakes and ladders game with one snake where the snake can change its position during the game and also during any subsequent plays (a board game where the snake keeps moving). Further, the snake can bite you only ones when you play.

<details><summary>Answer</summary>

**C**. A new snake position is drawn at the start of every call, so the snake moves during the game and in later games. There is no flag, so every time the player lands on the snake's head, it bites.

</details>

**`2020-jan/w07/q08`** Assuming that the play1() function implements the recursive play of snakes and ladders with the prespecified position of the snake and the ladder as shown in the code below, which of the ambiguities in the options can result in the code? Kindly assume a typical snakes and ladders game.

```python
import random
def play(psn):
    snake_begin=-1
    snake_end=-1
    while(snake_begin <= snake_end):
        snake_begin=random.randint(1,99)
        snake_end=random.randint(1,99)
    ladder_begin=-1
    ladder_end=-1
    while(ladder_end <= ladder_begin):
        ladder_begin=random.randint(1,99)
        ladder_end=random.randint(1,99)
    play1(psn,snake_begin,snake_end,ladder_begin,ladder_end)
```

- **A.** snake_begin=snake_end
- **B.** ladder_begin=ladder_end
- **C.** ladder_begin=snake_begin
- **D.** ladder_end=snake_end

<details><summary>Answer</summary>

**C**. The code picks the ladder and the snake independently. If they get the same start square, that square would have both a snake and a ladder, which is ambiguous. The loops already stop snake_begin = snake_end and ladder_begin = ladder_end.

</details>

**`2020-jan/w07/q09`** What is the output of the following code?

```python
import random
def play(psn):
    snake_begin=-1
    snake_end=-1
    while(snake_begin <= snake_end):
        snake_begin=random.randint(1,99)
        snake_end=random.randint(1,99)
    ladder_begin=-1
    ladder_end=-1
    while(ladder_end <= ladder_begin):
        ladder_begin=random.randint(1,99)
        ladder_end=random.randint(1,99)
    play1(psn,snake_begin,snake_end,ladder_begin,ladder_end)

# (In the original page this question repeats the code of the previous question,
#  but its options are pictures of star patterns: the code of Q10 belongs here.)
```

<details><summary>Answer</summary>

**[]**

</details>

**`2020-jan/w07/q10`** What is the output of the following code?

```python
def func():
    print()
    c=10
    i=3
    while(i<=6):
        j=0
        while(j<=20):
            if(j>=10-i and j<=10+i):
                print('*',end=" ")
            else:
                print(' ',end=" ")
            j=j+1
        print('\n')
        i=i+1
    i=6
    while(i>=3):
        j=0
        while(j<=20):
            if(j>=10-i and j<=10+i):
                print('*',end=" ")
            else:
                print(' ',end=" ")
            j=j+1
        print('\n')
        i=i-1
func()

# The options are pictures of star patterns. The accepted answer is a
# diamond-like block: rows of 7, 9, 11, 13, 13, 11, 9 and 7 stars, centred.
```

<details><summary>Answer</summary>

**[]**

</details>

**`2020-sep/w07/q09`** Comment on the following code:

```python
import csv
from gmplot import gmplot

gmap=gmplot.GoogleMapPlotter(9.920227,78.158252,12)

gmap.coloricon = 'http://www.googlemapsmarkers.com/v1/%s'

with open('path1.csv','r') as d:
    reader = csv.reader(d)
    k=0

    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        if(k==0):
            gmap.marker(lat,long,'red')
            k = 1
        else:
            gmap.marker(lat,long,'yellow')

gmap.draw('mymap.html')
```

- **A.** Red marker is used for initial and final positions
- **B.** Yellow marker is used for the final position only
- **C.** Yellow marker is placed for all positions except first position which has a red marker.
- **D.** Red marker is placed for all positions except first position which has a yellow marker

<details><summary>Answer</summary>

**C**. The first row of the file gets a red marker (when `k == 0`), and `k` becomes 1. Every later row gets a yellow marker.

</details>

**`2021-jan/w07/q04@portal`** What is the output of the following spiralprint python function?

```python
def spiralprint(m, n, spiralmatrix):
    k = 0
    l = 0
    while (k < m and l < n):
        for i in range(l, n):
            print(spiralmatrix[k][i], end=" ")
        k += 1
        for i in range(k, m):
            print(spiralmatrix[i][n - 1], end=" ")
        n -= 1
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(spiralmatrix[m - 1][i], end=" ")
            m -= 2
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(spiralmatrix[i][l], end=" ")
            l += 2
spiralmatrix = [[1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18]]

rows = 3
cols = 6
spiralprint(rows, cols, spiralmatrix)
```

- **A.** 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
- **B.** 1 2 3 4 5 6 12 18 17 16 15 14 13
- **C.** 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
- **D.** 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1

<details><summary>Answer</summary>

**B**. With `m -= 2` and `l += 2` the loop ends early: it prints the top row (1–6), the right column (12, 18), and the bottom row backwards (17–13). Then `m` becomes 1 and `k < m` is false, so the left column 7–11 is not printed.

</details>

**`2025-jan/w07/q01`** What will be the output of the following code?

```python
my_dict = {1: 2, 2: 3, 3: 4}
x = my_dict[my_dict[1]]
print(x)
```

- **A.** 2
- **B.** 3
- **C.** 4
- **D.** Error

<details><summary>Answer</summary>

**B**. `my_dict[1]` is 2, so `my_dict[my_dict[1]]` is `my_dict[2]`, which is `3`.

</details>

**`2025-jan/w07/q03`** What type of triangle is drawn by the given code?

```python
import turtle

pen = turtle.Turtle()

for i in range(3):

    pen.forward(60)
    pen.right(120)

turtle.done()
```

- **A.** Scalar triangle
- **B.** Right angle triangle
- **C.** Equilateral triangle
- **D.** Isosceles triangle

<details><summary>Answer</summary>

**C**. The code moves forward 60 and turns right 120° three times. Equal sides and equal turns close up into an equilateral triangle.

</details>

**`2025-jan/w07/q05`** What will be the output of the following code?

```python
my_dict = {}
my_dict[1] = "one"
my_dict[1.0] = "float one"
my_dict[True] = "boolean one"

print(my_dict)
```

- **A.** {1: ”one”, 1.0: ”float one”, True: ”boolean one”}
- **B.** {1: ”boolean one”}
- **C.** {1: ”one”, 1.0: ”float one”}
- **D.** {1.0: ”float one”, True: ”boolean one”}

<details><summary>Answer</summary>

**B**. In Python `1`, `1.0` and `True` are equal and have the same hash, so they are the same key. Each assignment overwrites the previous one, and the first key `1` stays. The result is `{1: "boolean one"}`.

</details>

**`2020-jan/w08/q06`** Which of the plots in the options is most likely to be generated from the following code?

```python
import random
import matplotlib.pyplot as plt

def play():
    amt=0
    for i in range(0,100):
        r=random.randint(1,6)
        amt=amt+r
    return amt

l=[]
for j in range(0,100):
    s=0
    for i in range(0,100):
        s=s+play()
    l.append(s)
x=[]
y=[]
for each in list(set(l)):
    x.append(each)
    y.append(l.count(each))
plt.plot(x,y,'ro')
plt.show()

# The options are four scatter plots. The accepted one has almost every point
# along the bottom (count 1), a few points at count 2 and one at count 3.
```

<details><summary>Answer</summary>

**[]**

</details>

**`2020-jan/w08/q07`** What is the output of the following code?

```python
dict_age={}
dict_age["Arun"]=20
dict_age["Bhima"]=10
dict_age["Chirag"]=40
dict_age["Deepak"]=30

dict1=dict_age
l=dict_age.values()
l[0]=90
print(l)
```

- **A.** [20,10,40,30]
- **B.** [90,10,40,30]
- **C.** [10,20,30,40]
- **D.** Error

<details><summary>Answer</summary>

**D**. In Python 3, `dict_age.values()` is a view. It cannot be assigned to by index, so `l[0] = 90` raises a `TypeError`.

</details>

**`2020-jan/w08/q08`** Which of the scenarios in the options does the following code represent?

```python
import random
dict_age={}
dict_age["Arun"]=20
dict_age["Bhima"]=10
dict_age["Chirag"]=40
dict_age["Deepak"]=30

l=list(dict_age.values())

dict1={}
l_name=dict_age.keys()
i=0
prev=0
for each in dict_age:
    dict1[each]=prev+l[i]
    prev=dict1[each]
    i=i+1
print(dict1)

r=random.randint(0,sum(dict_age.values()))
print(r)
for each in dict1:
    if(r<dict1[each]):
        print("Give all money to",each)
        break
```

- **A.** All money is given to the oldest person
- **B.** All money is given to the youngest person
- **C.** Money is given to a person with a probability proportional to his/her age
- **D.** Money is given to a person with a probability inversely proportional to his/er age

<details><summary>Answer</summary>

**C**. `dict1` stores running totals of the ages. A random number from 0 to the sum is compared with each total, and the first total above it wins. A person with a larger age covers a larger share, so the chance is proportional to age.

</details>

**`2020-jan/w08/q09`** Which of the scenarios in the options does the following code represent?

```python
import random
import operator


dict_age={}
dict_age["Arun"]=20
dict_age["Bhima"]=10
dict_age["Chirag"]=40
dict_age["Deepak"]=30

print("Give all money to", max(dict_age.items(), key=operator.itemgetter(1))[0])
l=list(dict_age.values())
```

- **A.** All money is given to the oldest person
- **B.** All money is given to the youngest person
- **C.** Money is given to a person with a probability proportional to his/her age
- **D.** Money is given to a person with a probability inversely proportional to his/er age

<details><summary>Answer</summary>

**A**. `max(dict_age.items(), key=operator.itemgetter(1))[0]` picks the name with the largest age, so all the money goes to the oldest person.

</details>

**`2020-sep/w08/q01`** What is the output of the following snippet?

```python
t1=('Amit','Simran','Neeru','Ravi','Shubhadha')
t2=t1+t1
print(len(t2))
```

- **A.** 5
- **B.** 10
- **C.** Error, because there is no len() function for Tuple
- **D.** Error, because Tuples are immutable

<details><summary>Answer</summary>

**B**. `t2 = t1 + t1` joins two 5-item tuples into one 10-item tuple. `len(t2)` is 10.

</details>

**`2020-sep/w08/q02`** Which of the following instruction produces a tuple, Team with ‘Poonam’ as the sixth member? Given:

```python
Team=('Amit','Simran','Neeru','Ravi','Shubhadha')
```

- **A.** Team=Team.append(‘Poonam’)
- **B.** Team=Team+tuple(‘Poonam’)
- **C.** Team=Team+(‘Poonam’)
- **D.** Team=Team+(‘Poonam’,)

<details><summary>Answer</summary>

**D**. A tuple with one item needs a trailing comma: `('Poonam',)`. Adding it to `Team` gives a new tuple with 6 items.

</details>

**`2020-sep/w08/q07`** Identify the best instruction to debug the following code that checks if the given strings are Anagrams:

```python
s1=input('Enter first string:')

s2=input('Enter Second string:')
if s1.sort()!=s2.sort():
        print('These are Anagrams')
else:
        print('Not Anagrams')
```

- **A.** if s1.sort()==s2.sort():
- **B.** if s1.sorted()==s2.sorted():
- **C.** if sorted(s1)==sorted(s2):
- **D.** if sorted(s1)!=sorted(s2):

<details><summary>Answer</summary>

**C**. Strings have no `sort` method, so `s1.sort()` fails. `sorted(s1)` returns a list of the letters in order, and two strings are anagrams exactly when these lists are equal. The test must use `==`, not `!=`.

</details>

**`2021-jan/w08/q04@portal`** What is the output of the following code?

```python
import random
random_number = random.randint(1,10)
tries = 0
x = int(input())
while x != random_number:
        tries += 1
        x = int(input())
        if x == random_number:
            print("stop")
```

- **A.** the program stops when the number entered matches with the random number generated
- **B.** the program stops after certain number of trials
- **C.** the program never stops
- **D.** error

<details><summary>Answer</summary>

**A**. The loop runs while `x != random_number`. Each pass reads a new `x`. When the input equals the random number the loop ends and `stop` is printed, so the program stops when the input matches.

</details>

**`2021-jan/w08/q05@portal`** What does the following program plot?

```python
import random
import matplotlib.pyplot as plt
rn=random.randint(0,9)
print(rn)
l=[0 for i in range(10)]
y=[]
for i in range(10):
  x=int(input())
  y.append(i)
  if x==rn:
    l[x]+=1
plt.plot(y,l)
plt.show()
```

- **A.** Plots the random number generated in each iteration
- **B.** Plots the number of times the given input matches with the random number generated
- **C.** Plots the input entered for each iteration
- **D.** none of the above

<details><summary>Answer</summary>

**B**. `l` has ten zeros, and `l[x] += 1` runs only when the input `x` equals the random number `rn`. So `l` counts how many times the input matched `rn`, and that is what is plotted.

</details>

**`2021-jan/w08/q07@portal`** What does the following code snippet in python compute?

```python
text1 = input()
len1 = len(text1)
text2 = input()
len2 = len(text2)
for i in range(0,len1-len2+1):
    j = 0
    while ((j < len2) and (text1[i + j] == text2[j])):
        j = j + 1
    if (j==len2):
        print(text2)
```

- **A.** checks whether the two given texts are same
- **B.** searches for text2 in text1
- **C.** ﬁnds all the occurrences of text2 in text1
- **D.** none of the above

<details><summary>Answer</summary>

**C**. For each start `i`, the `while` loop compares `text2` with `text1` from position `i`. If all `len2` characters match (`j == len2`) it prints `text2`. There is no `break`, so every occurrence is found.

</details>

**`2023-jul/w08/q05@gpt`** When the following program will clap?

```python
print('Enter a letter between a-z')

player1 = str(input())
player2 = str(input())

while(True):

    if(ord(player1.lower())+1 == ord(player2.lower())):
        print('clap')
        break
    else:
        player1 = str(input())
        player2 = str(input())
```

- **A.** When both players will enter the same letters.
- **B.** When player 2 will enter the next letter with respect to player 1.
- **C.** When player 1 will enter the next letter with respect to player 2.
- **D.** It will never clap.

<details><summary>Answer</summary>

**B**. The program claps when `ord(player1) + 1 == ord(player2)`, which means player 2's letter is the next letter after player 1's.

</details>

**`2025-jan/w08/q01`** What will be the output of the following Python code?

```python
tup = ([1, 2], [3, 4])
tup[0].append(5)
print(tup)
```

- **A.** ([1, 2, 5], [3, 4])
- **B.** ([1, 2], [3, 4])
- **C.** ([1, 2], [3, 4, 5])
- **D.** TypeError: Tuple object does not support item assignment

<details><summary>Answer</summary>

**A**. `tup` is a tuple whose first item is a list. A list can be changed in place, so `tup[0].append(5)` adds 5 to that list and the tuple still holds the same list objects. The output is `([1, 2, 5], [3, 4])`.

</details>

**`2025-jan/w08/q03`** What will be the output of the following Python code?

```python
t = (1,2,3,4,5)

for i in range(-1,-len(t), -1):
    print(t[i])
```

- **A.** 1,2,3,4,5
- **B.** 5,4,3,2,1
- **C.** 5,4,3,2
- **D.** 1,2,3,4

<details><summary>Answer</summary>

**C**. `range(-1, -len(t), -1)` gives -1, -2, -3, -4, so it prints `t[-1]` to `t[-4]`: 5, 4, 3, 2.

</details>

**`2025-jan/w08/q04`** What will be the output of the following Python code?

```python
word = 'facebook'
new = ''

for w in word:
    i = ord(w)

    j = ((( i+26 ) - 97 ) % 26 ) + 97

    new = new + chr(j)

print(new)
```

- **A.** facebook
- **B.** gbdfcppl
- **C.** ezbdannj
- **D.** ytvxuhhd

<details><summary>Answer</summary>

**A**. For each letter, `((ord(w) + 26 - 97) % 26) + 97` shifts it by 26 places and wraps around, which brings it back to the same letter. So `facebook` is unchanged.

</details>

**`2025-jan/w08/q06`** What will be the effect of the following Python code on the graph?

```python
import random
import matplotlib.pyplot as plt

l = []
count = 0

for i in range(10):
    guess = random.randint(1, 10)
    pick = random.randint(1, 10)

    if(guess!=pick):
        count+=1
        l.append(count)
    else:
        count-=1
        l.append(count)

plt.plot(l)
plt.show()

# (The page also shows one sample plot: a line that dips from 1 to 0, then rises
#  steadily to 8.)
```

- **A.** The graph will go up when guess and pick are the same.
- **B.** The graph will go down when guess and pick are the same.
- **C.** The graph will go up when guess and pick are not the same.
- **D.** Both (b) and (c).

<details><summary>Answer</summary>

**D**. When `guess != pick`, `count` goes up by 1 and is appended. When they are equal, `count` goes down by 1 and is appended. So the line goes down at a match (b) and goes up at a mismatch (c).

</details>

**`2025-jan/w08/q08`** What will be the output of the following Python code?

```python
string = 'hey!there'

a = sorted(string)
a.reverse()

print(a)
```

- **A.** [’!’, ’e’, ’e’, ’e’, ’h’, ’h’, ’r’, ’t’, ’y’]
- **B.** [’h’, ’e’, ’y’, ’!’, ’t’, ’h’, ’e’, ’r’, ’e’]
- **C.** [’y’, ’t’, ’r’, ’h’, ’h’, ’e’, ’e’, ’e’, ’!’]
- **D.** None of the above

<details><summary>Answer</summary>

**C**. `sorted('hey!there')` gives the letters in ascending order: `['!', 'e', 'e', 'e', 'h', 'h', 'r', 't', 'y']`. `a.reverse()` flips the list in place, so it prints `['y', 't', 'r', 'h', 'h', 'e', 'e', 'e', '!']`.

</details>

**`2020-sep/w09/q02`** Identify the option that best describes the graph output of the following code.

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for i in range(1,11):
        G.add_node(i)
e = [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)]
G.add_edges_from(e)

nx.draw(G)
plt.show()
```

- **A.** A complete graph with 10 nodes
- **B.** A complete graph with 9 nodes
- **C.** A connected graph with 10 nodes
- **D.** A connected graph with 9 nodes

<details><summary>Answer</summary>

**C**. The code adds nodes 1 to 10 and the edges (1,2), (2,3), ..., (9,10). That is a chain of 10 nodes, which is connected but not complete.

</details>

**`2020-sep/w09/q04`** What does p and q represent in the following instruction to find the shortest path length?

```python
networkx.shortest_path_length(H,p,q)
```

- **A.** p and q represent to two lists of nodes
- **B.** p represents the source node and q represents the target node
- **C.** p represents the target node and q represents source the node
- **D.** p and q represent two paths

<details><summary>Answer</summary>

**B**. In `shortest_path_length(H, p, q)` the second argument is the source node and the third is the target node.

</details>

**`2020-sep/w09/q09`** What is the output of the following snippet?

```python
arr=np.zeros([200,200,3],dtype=np.uint8)
arr[:100,:]=[255,0,0]
arr[100:,:]=[0,0,255]
img=Image.fromarray(arr)
img.save('test.png')
```

- **A.** Image of size 200 x 200 with Red on left and Blue on right
- **B.** Image of size 200 x 3 with Red on top and Blue at the bottom
- **C.** Image of size 200 x 200 with Red on top and Green at the bottom
- **D.** Image of size 200 x 200 with Red on top and Blue at the bottom

<details><summary>Answer</summary>

**D**. `arr` is 200 × 200 with 3 colour values. The first 100 rows (`arr[:100]`) are set to `[255, 0, 0]`, which is red, and the rest (`arr[100:]`) to `[0, 0, 255]`, blue. Rows are the top-to-bottom direction, so the image has red on top and blue at the bottom.

</details>

**`2025-jan/w09/q04`** What is the output of the following code?

```python
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 1), (2, 3), (3,4), (4,1), (3,1)])

nx.draw(G,with_labels=True)
plt.show()

# The options are drawings: A) a path of 4 nodes, B) a path of 3 nodes plus a
# lone node, C) 4 nodes joined in a crossed "bow-tie" (4 edges), D) 4 nodes in a
# quadrilateral with one diagonal (5 edges). The accepted answer is D.
```

<details><summary>Answer</summary>

**[]**

</details>

**`2025-jan/w09/q10`** What will be the output of the following code?

```python
s = "hello"
s[0] = "H"
```

- **A.** It will print ”Hello”
- **B.** It will raise a TypeError
- **C.** The string will be updated to ”Hello”
- **D.** It will change the first character to uppercase and print ”Hello”

<details><summary>Answer</summary>

**B**. A string is immutable, so `s[0] = 'H'` raises `TypeError: 'str' object does not support item assignment`. Nothing is printed.

</details>

**`2020-jan/w10/q08`** What is the output of the following code ?

```python
example = "snow world"
example[3] = 's'
print(example)
```

- **A.** snow
- **B.** snow world C
- **C.** Error
- **D.** snos world

<details><summary>Answer</summary>

**C**. Strings cannot be changed in place, so `example[3] = 's'` raises `TypeError: 'str' object does not support item assignment`.

</details>

**`2020-jan/w10/q09`** What is the output of the following code ?

```python
print('ab'.isalpha())
```

- **A.** True
- **B.** False
- **C.** None
- **D.** Error

<details><summary>Answer</summary>

**A**. `'ab'.isalpha()` is `True`, since every character is a letter.

</details>

**`2020-sep/w10/q08`** Choose the relevant image for test3.png created by the given code.

```python
import numpy as np
from PIL import Image

array1=np.zeros([200,200,3],dtype=np.uint8)
array2=np.zeros([200,200,3],dtype=np.uint8)

array1[:,:100]=[255,0,0]
array2[:,100:]=[0,0,255]
array3=np.add(array1,array2)

img1=Image.fromarray(array1)
img2=Image.fromarray(array2)
img3=Image.fromarray(array3)

img3.save('test3.png')

# Options are pictures: black, blue, blue, red-over-blue, and a square that is
# red on the left half and blue on the right half.
```

<details><summary>Answer</summary>

**[]**

</details>

**`2021-jan/w10/q02@portal`** Predict the output of the following code

```python
import string
S = "Hello"
S = S.uppercase()
print(S)
```

- **A.** HELLO
- **B.** Hello
- **C.** hello
- **D.** error

<details><summary>Answer</summary>

**D**. Strings have no `uppercase()` method, so `S.uppercase()` raises `AttributeError`. The right method is `upper()`.

</details>

**`2025-jan/w10/q02`** What will be the output of the following code?

```python
s = "PythonProgramming"
print(s[2:15:3] + s[::-4])
```

- **A.** toPmiagmnrh
- **B.** toPmiagmnrPg
- **C.** tnoaigmooP
- **D.** toPmiagmnr

<details><summary>Answer</summary>

**C**. `s[2:15:3]` takes positions 2, 5, 8, 11, 14: `t`, `n`, `o`, `a`, `i`, which is `tnoai`. `s[::-4]` starts at the last letter and moves back by 4: `g`, `m`, `o`, `o`, `P`, which is `gmooP`. Together they print `tnoaigmooP`.

</details>

**`2025-jan/w10/q03`** What does the following code print?

```python
s = "Python Programming"
print(s.index('o', 5, 10))
```

- **A.** 6
- **B.** 7
- **C.** 9
- **D.** Value Error

<details><summary>Answer</summary>

**C**. `s.index('o', 5, 10)` looks for `o` only between positions 5 and 9. The first `o` of `Python` is at 4, outside the range. The next one is the `o` of `Programming` at position 9.

</details>

**`2025-jan/w10/q05`** What will be the output of the following Python code?

```python
print(17 % -5)
```

- **A.** 3
- **B.** 2
- **C.** 0
- **D.** -3

<details><summary>Answer</summary>

**D**. Python's `%` takes the sign of the divisor. `17 = (-4) × (-5) + (-3)`, so `17 % -5` is -3.

</details>

**`2025-jan/w10/q08`** What will be the output of the following code?

```python
import numpy as np
arr = np.array([[1, [2, 3]], [4, [5, 6]], [7, [8, 9]]], dtype=object)
print(arr[1][1][0])
```

- **A.** 2
- **B.** 5
- **C.** [5, 6]
- **D.** 4

<details><summary>Answer</summary>

**B**. `arr[1]` is the row `[4, [5, 6]]`, `arr[1][1]` is its list `[5, 6]` and `[0]` of that is 5.

</details>

**`2025-jan/w10/q09`** For which value of axis the output is [5, 7, 9] in the below code?

```python
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(a, axis= ? ))   # the value of axis is hidden in the picture
```

- **A.** 0
- **B.** 1
- **C.** 2
- **D.** axis argument is not required.

<details><summary>Answer</summary>

**A**. Summing along axis 0 adds the columns: `[1 + 4, 2 + 5, 3 + 6] = [5, 7, 9]`.

</details>

**`2020-jan/w11/q09`** What will be the output of the following Python code if the system date is 18th June, 2017 (Sunday)?

```python
tday=datetime.date.today()
print(tday.weekday())
```

- **A.** 6
- **B.** 1
- **C.** 0
- **D.** 7

<details><summary>Answer</summary>

**A**. `weekday()` numbers the days from Monday = 0, so Sunday is 6.

</details>

**`2021-jan/w11/q05@portal`** Which of the following code snippet will print today’s date?

```python
# Option A
from datetime import date
today = date.today()

# Option B
from datetime import datetime
today = datetime.now()
```

- **A.** Both A and B
- **B.** none

<details><summary>Answer</summary>

**A**. `date.today()` returns today's date, and `datetime.now()` returns today's date with the time. Both snippets get today's date.

</details>

**`2021-jan/w11/q07@portal`** What does the following code print?

```python
import calendar
print (calendar.leapdays(2000, 2020))
```

- **A.** Number of leapdays between the speciﬁed years
- **B.** Lists all leapdays between the speciﬁed years
- **C.** Lists the leapdays and its count between the speciﬁed years
- **D.** None

<details><summary>Answer</summary>

**A**. `calendar.leapdays(2000, 2020)` returns how many leap years lie between the two years (2000, 2004, 2008, 2012 and 2016), so it prints the number 5.

</details>

**`2024-jul/w11/q09`** What does the following Python code output?

```python
import calendar
print(calendar.isleap(2024))
```

- **A.** True
- **B.** False
- **C.** 2024.0
- **D.** None

<details><summary>Answer</summary>

**A**. 2024 is divisible by 4 and not by 100, so it is a leap year. `calendar.isleap(2024)` returns `True`.

</details>

**`2025-jan/w11/q04`** What is the output of the following Python code?

```python
for i in range(5):
    for j in range(5):
        if j == 2:
            break
        if i == 3:
            continue
        print(f"({i}, {j})", end=" ")
```

- **A.** (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1) (4, 0) (4, 1)
- **B.** (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1) (3, 0) (3, 1) (4, 0) (4, 1)
- **C.** (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1) (3, 0) (3, 1) (3, 2) (4, 0) (4, 1)
- **D.** (0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1) (3, 0) (4, 0) (4, 1) (4, 2)

<details><summary>Answer</summary>

**A**. For each `i`, the inner loop prints `(i, 0)` and `(i, 1)` and then breaks at `j == 2`. When `i` is 3, the `continue` skips every print before `j` reaches 2, so nothing is printed for 3. The output is `(0, 0) (0, 1) (1, 0) (1, 1) (2, 0) (2, 1) (4, 0) (4, 1)`.

</details>

**`2025-jan/w11/q05`** What will be the output of the following Python code, which performs a modified

```python
arr = [3, 8, 1, 7, 9, 2]
key = 7

for i in range(len(arr)):
    if arr[i] == key:
        print(f"Found at index {i}")
        break
    if arr[i] % 2 == 0:
        continue
    print(f"Checking {arr[i]}")
```

- **A.** Checking 3 Checking 8 Checking 1 Found at index 3
- **B.** Checking 3 Checking 1 Found at index 3
- **C.** Checking 3 Checking 8 Checking 1 Checking 7 Found at index 3
- **D.** Found at index 3

<details><summary>Answer</summary>

**D**

</details>

**`2025-jan/w11/q10`** What is the output of the following Python code?

```python
from datetime import datetime
import pytz

dt_naive = datetime(2024, 2, 29, 12, 0, 0)
tz_ist = pytz.timezone('Asia/Kolkata')

dt_aware = tz_ist.localize(dt_naive)
print(dt_aware.strftime("%Y-%m-%d %H:%M:%S %Z"))
```

- **A.** 2024-02-29 12:00:00 IST
- **B.** 2024-02-29 06:30:00 UTC
- **C.** 2024-02-29 12:00:00 UTC
- **D.** Error

<details><summary>Answer</summary>

**A**. `localize` attaches the `Asia/Kolkata` zone to the 12:00 time without changing it. `%Z` prints the zone abbreviation, `IST`, so it prints `2024-02-29 12:00:00 IST`.

</details>

**`2025-jan/w12/q06`** What will be the output of the following code?

```python
import networkx as nx

G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
print(len(G.nodes()), len(G.edges()))
```

- **A.** (4, 4)
- **B.** (4, 8)
- **C.** (4, 2)
- **D.** (8, 4)

<details><summary>Answer</summary>

**A**. The edges (1,2), (2,3), (3,4) and (4,1) make a ring with 4 nodes and 4 edges. The code prints `4 4`, so the answer is `(4, 4)`.

</details>

**`2025-jan/w12/q07`** What is the output of this code?

```python
def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps

print(collatz_steps(7))
```

- **A.** 7
- **B.** 16
- **C.** 5
- **D.** 10

<details><summary>Answer</summary>

**B**. Starting at 7 the sequence is 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. That takes 16 steps, which the function returns.

</details>
