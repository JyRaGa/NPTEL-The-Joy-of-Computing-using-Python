# Visual check of the quiz site (read-only)

Checked at http://localhost:8765/site/, Weeks 0–12, default view (all sessions, "Most repeated first"), so card numbers match the audit.

**How this was done.** A script ran in the page for every week, followed by looking at screenshots of sample cards.
- I did not look at every card by eye (about 1,950 cards).
- The script force-loaded every image and checked that it loaded.
- It also scanned the rendered text for leftover markdown, garbled glyphs, portal feedback, empty or duplicate options, and stems that mention code or a figure the card does not show.
- Cards where the only code is in the collapsed "Original portal page" were counted but not listed (about 7–20 per week in Weeks 7–12).
- Nothing was fixed or committed.

**Images.** Every `<img>` on every week page loaded; there were no broken image links. Nothing was found for the other things I did not scan for (layout on a wide screen, dark/light theme, the Weeks 5, 6 and 7 collapsed crops).

## Week 0
- Q36: options A and B ("15.6") are identical.

## Week 1
- Q16, Q74, Q103, Q104, Q106: the stem has a raw transcriber description in backticks, for example "(Scratch blocks: `when ⚑ clicked` · `forever` …)". Q74, Q103 and Q106 do show an image as well, so the description is a duplicate.
- Q105, Q107: the stem says "(same blocks as Q7 …)" and "(same ball script as Q9 …)" with no image on the card.
- Q153, Q156: options like "move 5 steps (first block)" refer to blocks that are not shown.
- Q154: asks about "the turn 15 degrees block in this program", but no program or image is on the card.
- Q32, Q33: the portal text leaked into the stem. Q32's stem lists its own options, and Q33's stem repeats the answers.
- Q59: stem ends in a stray `?**\`, and all four options are blank (picture options).
- Q119: options C and D are identical ("move 40 steps; turn left 40 degrees").

## Week 2
- Q2, Q96, Q106, Q132–Q135: literal backticks show around variable names (`c`, `_`, `i += 1`).
- Q105–Q107: options show literal `**n**`, `**1**` markdown.
- Q106: the stem has an editorial note, "(as displayed on the portal, `i += 1` is indented deeper than `print`)".
- Q38: the stem ends with "> Score: 0", the options are blank, and the card is reveal-only.
- Q119: the stem ends with "> Partially Correct. Score: 0.67".
- Q62: "What will the output of the following program be?" shows no code.
- Q81: the stem shows only the first line of the code, and option C carries an editorial note, "(author first clicked "1 to a", then changed …)".
- Q74: options A and D are identical ("Hello Mr. Bond 34").

## Week 3
- Q92, Q98, Q99, Q100: "What is the output of the following code?" with no code or image on the card.
- Q102: option D shows literal `**This_is_not_List = [ ]**`.
- Q120, Q130: Q130 is badly garbled (private-use glyphs and one-digit lines in the stem), and Q120 refers to "question 8" which is not on the card.
- Q75: options A and D are identical.

## Week 4
- Q63: the stem shows literal `<img src= "img/noc21_cs75/cs75W4Q3.png" alt="">` and the matrix image is missing.
- Q31: the stem has an escaped `\*`, and the options show backslashes ("IN\_ER\_\_ELL\_R") and a cut-off "[…]".
- Q46: option A is letter-spaced text ("r e s u l t = a ( b+( c * * 2 ) )").
- Q106: the stem is about arranging steps, but all options are blank.
- Q108: very long code (60 lines), with `**Dataset:**` markdown in the stem.
- Q109: the stem has an editorial note, "right edge cut off in the recording", and raw `**…**`.
- Q89: the stem is clean but the options are `^`, `*`, `**`, `***`; rendered markdown may swallow `**`.
- Q122: PDF-garbled stem, with private-use glyphs, one character per line and "Accepted answer(s): 2; (; +; 1; )…" in the text.
- Q125: PDF-garbled stem with matrix glyphs (⎡⎤⎢⎥) and the same "Accepted answer(s)" junk.
- Q13, Q97: reveal-only (no known answer).

## Week 5
- Q85: options start with a literal "Option 1 is correct, …".
- Q102: bullet list in the stem is shown as plain "- Rock wins against Scissors." lines.
- Q107: stem and options show literal `\`low\``, `\`high\`` and `**…**`.
- Q112, Q132: literal `**…**`.
- Q148: the stem has an editorial note, "(author first clicked "1", then changed to "-1")".
- Q160–Q169: each repeats the same 63-line scenario code before the question. This is by design but very long.

## Week 6
- Q80: options 1–4 are four full code panels, each prefixed "Option N", and option 4 shows "*(appears identical to Option 3 in every captured frame — any differen…" in the text.
- Q81: also "Option N" labels.
- Q93: output options show raw star blocks; D shows blank lines between rows.
- Q95, Q97, Q100, Q102, Q103: literal backticks in the stem or options (`upper()`).
- Q133: the last option has stray "- o An "X" / - o An "O" / - o Or remain empty" lines glued on.
- Q134–Q138: each repeats the same 56-line scenario code.
- Q90: reveal-only.

## Week 7
- Q85: raw "(Image: 3×4 matrix with arrows — row 0 `15 23 8 7` →, …)" description (the image is also attached).
- Q88, Q89: literal `\`csv\`` backticks in the stem and options.
- Q80: options are "Output A / B / C / D" with no picture (the picture options are missing).
- Q107: options C and D are identical ("Both A and B.").
- Q13: very long code (54 lines).
- Q26, Q27, Q29, Q32, Q33, Q37, Q38, Q106: reveal-only.

## Week 8
- Q76: the stem has "q43 the correct representation of tuples?** *(sic — "q43" as printed on the portal)*".
- Q66: stem ends in a stray `?**\`.
- Q78: the option cards show "Option 1" followed by the line-number gutter and the code, which looks odd.
- Q89, Q93: literal `**…**` in the options; Q93 also has a `""hello"` typo in an option.
- Q94: literal `*(…` fragment in an option.
- Q37: stem is just "What is VADER?" (short, but looks right).
- Q43, Q44: reveal-only.

## Week 9
- Q81, Q83, Q85: the stem shows a raw "(graph image — see first panel of the linked image …)" note, and the graph images are now attached.
- Q96, Q106: stem has a raw "(Image: nodes 2 and 1 at the top …)" description (no image).
- Q133: the last option has a stray "- o The dataset is read and converted into a graph str…" glued on.
- Q97: 49 lines of code; Q126–Q133 repeat the same 50-line scenario code.
- Q113: stem is just "Gephi is:"; Q52 and Q120 are reveal-only.

## Week 10
- Q16: option A is "Powered by" (stray page text) and the real options start at B.
- Q104: stray page text in the card.
- Q30: stem has a "[…]** (the rest of the line is cut off at the frame edge)" note and raw `**`.
- Q61: option A shows a literal ✅ in the text, and the stem has "PNG\\" with a trailing backslash.
- Q69: option B shows a literal ✅.
- Q64: options B and C are identical ("2").
- Q73: all four options are blank (the same option picture is used four times, or none).
- Q88: options are just "(Option A)", "(Option B)" and so on, with no content, and the stem says "(checkboxes: more than one can be selected)".
- Q92, Q94–Q99: literal `**lower()**` or backticks.
- Q136–Q140: stray "- " bullet characters.
- Q121–Q130: each repeats the same 48-line scenario code.
- Q27: editorial note "*(not visible in this recording; taken from the Jul-2019 official revi…".
- Q43, Q48, Q58, Q59: reveal-only.

## Week 11
- Q76: options B and D are identical ("datetime.utc()").
- Q93: the stem is a long story and the options are blank (an answer is also typed into the stem).
- Q22: "In the question above, …" refers to a card that is not adjacent.
- Q44: reveal-only.

## Week 12
- Q7: options 1 and 4 are identical (the 19-number sequence).
- Q56: two options are identical ("Statement b is correct").
- Q69: stem is "NLTK ________." (short but correct).
- Q76, Q77: the stem has a raw "(Image: …)" description, and the real image is now also attached.
- Q72: raw "(image: labelled nodes 1–2–3 and 4 …)".
- Q89: stem shows "Answer entered: `6`" and the card is reveal-only, so the answer is visible.
- Q91: portal text in the stem ("It is divided by 2 / It remains unchanged … Accepted answer(s): n × 3 + 1; It is replaced by").
- Q15: asks "Which of the following python function will return random floating point number …", correct, no problems.
- Q37, Q39, Q99: reveal-only.

## Things that cut across weeks
- Backticks and `**bold**` markdown appear as literal characters in the stem and options (the page does not render them). Weeks 1, 2, 4–10 and 12 are affected.
- Several picture-only option cards show four blank option rows (Week 1 Q59, Week 4 Q106, Week 10 Q73, Week 11 Q93).
- The "Scenario" code for the 2026 sets is repeated in full on every card of the set (Weeks 5, 6, 9, 10).
