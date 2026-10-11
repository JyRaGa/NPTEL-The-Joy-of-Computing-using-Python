# Answer-review brief (for reviewer agents)

You are checking answers for past NPTEL "Joy of Computing using Python" weekly-quiz questions. Work in `JRG JOC/` (path has a space; quote it). Do NOT edit any file except through the commands below.

## Loop, per assigned week N
1. `python tools/review_dump.py N` lists every question still needing review: `## <gid> <type> ans=<current pick>`, question text, `CODE:` / `CTXCODE:`, `IMG:` paths (question figures), options `A) ...` (an option may be `IMG:path` or carry `CODE:`), `CROPS:` (portal page scans).
   The current pick (`ans=`) is a YouTuber's tick: often right, sometimes wrong. Decide the correct answer yourself.
2. Decide each question:
   - Short pure-Python code: run it (`python -c` or a temp file in your scratch dir) instead of guessing.
   - If the code or options exist only as images (`IMG:`), open the image with the Read tool (paths are relative to `JRG JOC/`). To save tokens, combine several images into one sheet first:
     `"C:/Users/rajes/AppData/Local/Temp/jocenv/Scripts/python.exe" "C:/Users/rajes/AppData/Local/Temp/claude/C--Users-rajes-OneDrive-Documents-GitHub-NPTEL-The-Joy-of-Computing-using-Python/577d7b9a-ea36-4908-94b0-6ebf9268266a/scratchpad/strip.py" OUT.png img1 img2 ...` (labels them A, B, C... in red), then Read OUT.png. Write OUT.png into your own scratch dir.
   - Scratch-block questions: trace the blocks exactly.
   - Concept questions: use the course's framing (e.g. the course's "jumbled question" count for a 3-letter word is 3! - 1 = 5).
3. Record decisions in batches (one call per ~20):
   `python tools/review_add.py --week=N <gid>=B <gid>=A,C <gid>=n:42 <gid>=type:multi:A,B`
   - letters = correct option(s); several letters for multi-select.
   - `n:VALUE` for a typed numeric answer (questions with no options but a known value); `type:numeric:n:VALUE` if the type must change.
   - `type:multi:A,B` when a question marked single actually has several correct options (e.g. says [MSQ] / select all).
4. SKIP (record nothing) when: the question is genuinely ambiguous (two options defensible), the needed code/image is missing or unreadable, or it depends on a live website/random output you cannot pin down. Skipped questions stay labelled "Unverified" on the site; that is fine.

## Rules
- Never rewrite question text. You only choose answers.
- Never mention the YouTuber or their tick anywhere.
- Be token-efficient: no long explanations; batch image reads; don't re-dump.

## Final report (keep under 120 words)
Per week: number decided, number skipped, and a list of gids where your answer differs from the `ans=` pick, each with the correct letter and a 6-word reason.
