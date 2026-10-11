# Gap-fixing brief (for agents)

Work in `C:\Users\rajes\OneDrive\Documents\GitHub\NPTEL-The-Joy-of-Computing-using-Python\JRG JOC` (quote paths). Some quiz questions have missing code, missing/garbled options, or no answer. Recover them from screenshots/videos, verbatim. Never edit any existing `quizzes/**/*.md` file.

1. `python tools/gaps.py <TERM>` lists the open questions: `## <gid> week=.. type ans=.. src=<id> file=<md>`, text, CODE, IMG (figures and portal page crops), options.
2. Find the original screen for each (sources named in your task). Save the cropped question screenshot as a PNG under `quizzes/<TERM>/img/recovered/<gid>.png` (crop with PIL: `C:/Users/rajes/AppData/Local/Temp/jocenv/Scripts/python.exe`, it has Pillow). These crops are kept as evidence and shown on the site.
3. Read the screenshot and transcribe exactly: code with original indentation, options in on-screen order. Determine the answer: an NPTEL "Accepted Answer" visible on screen = official; otherwise run the code / reason it out (= reviewed). If unreadable or ambiguous, skip.
4. Append one JSON object per line to `index/fixes/<your-file>.jsonl` (your task names the file). Keys (include only what you recovered):
   `{"gid": "...", "code": "...", "options": ["...", "..."], "crops": ["quizzes/<TERM>/img/recovered/<gid>.png"], "answer": [1], "badge": "official"|"reviewed"}`
   - `answer` = 0-based option indices (A=0) in YOUR `options` order (or the existing order if you don't send `options`); for a typed answer use `"type": "numeric", "answer": "42"`.
   - Validate each line with `python -c "import json;[json.loads(l) for l in open(r'index/fixes/<file>.jsonl',encoding='utf-8')]"`.
5. Final report under 120 words: counts fixed / official / skipped, and any gid whose answer differs from the old `ans=`.
Be token-efficient: batch several screenshots into one image before reading when possible.
