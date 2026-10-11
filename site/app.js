"use strict";
const WEEKS = [
  // W1–W12: official course titles; W0 is the pre-course warm-up quiz
  "Warm-up: aptitude and maths", "Introduction to Programming", "Variables, Expressions and the Python Console",
  "Lists, Slicing and Comprehensions", "Probability and Combinatorial Thinking", "Speech Recognition, Sorting and Searching",
  "Cryptography, Game Logic and Recursion", "Matrix Traversal and Route Finding", "Data Structures and Applied Analysis",
  "Natural Language Processing and Graphs", "Pattern Matching and Data Compression", "Automation with Python", "Web Search Algorithms and Number Theory",
];
// official week descriptions from the NPTEL course outline
const DESC = [
  "Pre-course warm-up questions on aptitude and maths.",
  "Introduction to programming, Scratch and its features, loops and sequencing.",
  "Variables and expressions, printing and assigning values, executing instructions in the console, design your own calculator.",
  "Slicing, removing items, list comprehensions, FizzBuzz, crowd computing, permutations of jumbled words.",
  "Magic Square, Dobble game, Birthday Paradox, Guess the Movie.",
  "Speech recognition, Monty Hall problem, Rock, Paper, Scissors, sorting and searching.",
  "Substitution cipher, Tic Tac Toe, recursion.",
  "Snakes and Ladders, spiral traversal, GPS route tracking.",
  "Tuples, lottery simulation, image processing, anagrams, sentiment analysis.",
  "Natural Language Processing, NetworkX, Six Degrees of Separation, area calculation.",
  "FLAMES, data compression.",
  "Browser automation, working with the calendar.",
  "Page Rank, Collatz conjecture.",
];
const BADGE = { official: "Official answer", pdf: "Course PDF answer", run: "Verified by running", reviewed: "Reviewed answer", uploader: "Unverified" };
const ICON = {
  ok: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>',
  bad: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
  save: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4h10v16l-5-3.5L7 20z"/></svg>',
};
const $ = (s, el = document) => el.querySelector(s);
const esc = (s) => String(s ?? "").replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const termLabel = (t) => { const [y, s] = t.split("-"); return s[0].toUpperCase() + s.slice(1) + " " + y; };
const termKey = (t) => +t.slice(0, 4) * 100 + ({ jan: 1, jul: 7, sep: 9 }[t.slice(5)] || 0);
const imgSrc = (p) => (/^https?:/.test(p) ? p : "../" + p);
const LETTERS = "ABCDEFGH";
// sources carry a few inline tags (<br>, <sup>); allow only those, everything else stays escaped
const rich = (s) => esc(s).replace(/&lt;(\/?)(br|sup|sub|b|i|em|strong|code)\s*\/?&gt;/gi, (m, c, t) => (t.toLowerCase() === "br" ? "\n" : `<${c}${t}>`));

/* ---------- progress store (browser only) ---------- */
let store = { a: {}, s: {} };
try { store = Object.assign(store, JSON.parse(localStorage.getItem("joc:v1") || "{}")); } catch (e) { /* private mode */ }
const persist = () => { try { localStorage.setItem("joc:v1", JSON.stringify(store)); } catch (e) { /* ignore */ } };

/* ---------- data ---------- */
const cache = {};
let meta = { weeks: {} };
const loadWeek = (w) => (cache[w] ??= fetch(`data/week-${String(w).padStart(2, "0")}.json`).then((r) => r.json()));

/* ---------- view state <-> URL ---------- */
const state = { w: 0, years: new Set(), f: "all", s: "rep", q: "", g: "" };
function readHash() {
  const [path, qs] = location.hash.slice(1).split("?");
  const p = new URLSearchParams(qs || "");
  state.w = Math.min(12, Math.max(0, parseInt((path || "w0").slice(1), 10) || 0));
  state.years = new Set((p.get("y") || "").split(",").filter(Boolean));
  state.f = p.get("f") || "all";
  state.s = p.get("s") || "rep";
  state.g = p.get("g") || "";
}
function writeHash(replace) {
  const p = new URLSearchParams();
  if (state.years.size) p.set("y", [...state.years].join(","));
  if (state.f !== "all") p.set("f", state.f);
  if (state.s !== "rep") p.set("s", state.s);
  const h = `#w${state.w}` + (p.toString() ? "?" + p.toString().replace(/%2C/g, ",") : "");
  if (h !== location.hash) history[replace ? "replaceState" : "pushState"](null, "", h);
}

/* ---------- rendering helpers ---------- */
function codePanel(code, html) {
  const n = code.split("\n").length;
  const gut = Array.from({ length: n }, (_, i) => i + 1).join("\n");
  return `<div class="code"><pre class="gut" aria-hidden="true">${gut}</pre><pre data-code>${html || esc(code)}</pre>` +
    `<button class="copy" type="button" data-copy>Copy</button></div>`;
}
const looksLikeOutput = (t) => t.length < 160 && /[\[\]{}()=_'"*]|^\s*-?\d/.test(t) && !/\s(the|is|of|and|to|will|it|by)\s/i.test(t);
const img = (p, alt) => `<img class="zoomable" src="${esc(imgSrc(p))}" alt="${esc(alt)}" loading="lazy" decoding="async">`;

function renderQ(g, idx) {
  const rec = store.a[g.gid];
  const sess = g.terms.map(termLabel).join(" · ");
  const rep = g.terms.length > 1 ? `<span class="rep">Asked ${g.terms.length}×</span>` : "";
  const wk = state.q ? `<span class="wk-tag">Week ${g.week}</span>` : "";
  let h = `<article class="q" id="g-${g.gid}" data-gid="${g.gid}" tabindex="-1" aria-labelledby="t-${g.gid}">
    <div class="q-head"><a class="q-id" href="#w${g.week}?g=${g.gid}">Q${idx}<span class="pil">¶</span></a>${wk}
    <span class="sess">${sess}</span>${rep}
    <button class="icon-btn save" type="button" aria-pressed="${!!store.s[g.gid]}" aria-label="Save question" data-save>${ICON.save}</button></div>`;
  if (g.context && (g.context.text || g.context.code || g.context.images)) {
    h += `<details class="ctx"${idx === 1 || !g.context.text || g.context.images ? " open" : ""}><summary>${g.context.text ? "Scenario" : "Code for this question"}</summary><div class="ctx-body">${rich(g.context.text)}` +
      (g.context.images ? `<div class="q-imgs">${g.context.images.map((p) => img(p, "Scenario program")).join("")}</div>` : "") +
      (g.context.code ? codePanel(g.context.code, g.context.code_html) : "") + `</div></details>`;
  }
  h += `<p class="q-text" id="t-${g.gid}">${rich(g.text)}</p>`;
  if (g.images.length) h += `<div class="q-imgs">${g.images.map((p) => img(p, "Question figure")).join("")}</div>`;
  if (g.code) h += codePanel(g.code, g.code_html);
  if (g.type === "multi") h += `<p class="multi-hint">Select all that apply, then submit.</p>`;
  if (g.options.length && g.type !== "numeric") {
    const outQ = /output|print/i.test(g.text) && (g.code || g.images.length || g.context?.code);
    h += `<ol class="opts">` + g.options.map((o, i) => {
      const body = (o.text ? `<span class="otext${looksLikeOutput(o.text) || (outQ && o.text.length < 80) ? " mono" : ""}">${rich(o.text)}</span>` : "") +
        (o.img ? img(o.img, `Option ${LETTERS[i]}`) : "") + (o.code ? codePanel(o.code, o.code_html) : "");
      return `<li><button class="opt" type="button" data-i="${i}" aria-pressed="false"><span class="letter">${LETTERS[i]}</span><span>${body}</span><span class="mk"></span></button></li>`;
    }).join("") + `</ol>`;
  }
  h += `<div class="actions">`;
  if (g.type === "multi") h += `<button class="btn" type="button" data-submit disabled>Submit</button>`;
  if (g.type === "numeric") h += `<input class="num-in" inputmode="decimal" aria-label="Your answer" data-num><button class="btn" type="button" data-check>Check</button>`;
  if (g.type === "reveal") h += `<button class="btn" type="button" data-reveal>Show answer</button>`;
  h += `</div><div class="result" aria-live="polite"></div>`;
  if (g.crops.length) h += `<details class="src"><summary>Original portal page</summary><div class="crops">${g.crops.map((p) => img(p, "Portal page")).join("")}</div></details>`;
  h += `</article>`;
  return h;
}

/* ---------- grading ---------- */
const known = (g) => (g.type === "numeric" ? !!g.answer : g.answer.length > 0);
function numEq(a, b) {
  const accepted = String(b).split(/\s*(?:,|;|\bor\b)\s*/);
  return accepted.some((x) => x.trim().toLowerCase() === a.trim().toLowerCase() || (x !== "" && !isNaN(x) && !isNaN(a) && a.trim() !== "" && Math.abs(+x - +a) < 1e-9));
}
function grade(g, pick) {
  let ok = null;
  if (known(g)) ok = g.type === "numeric" ? numEq(pick, g.answer) : pick.length === g.answer.length && pick.every((i) => g.answer.includes(i));
  const prev = store.a[g.gid];
  store.a[g.gid] = { p: pick, ok, n: (prev?.n || 0) + 1, w: g.week };
  persist();
}
function paint(el, g) {
  const rec = store.a[g.gid];
  const res = $(".result", el);
  if (!rec) { res.innerHTML = ""; return; }
  const opts = [...el.querySelectorAll(".opt")];
  const ans = Array.isArray(g.answer) ? g.answer : [];
  opts.forEach((b) => {
    const i = +b.dataset.i, picked = Array.isArray(rec.p) && rec.p.includes(i), right = ans.includes(i);
    b.disabled = true;
    b.classList.toggle("is-ok", picked && right);
    b.classList.toggle("is-bad", picked && !right && known(g));
    b.classList.toggle("is-missed", !picked && right);
    b.setAttribute("aria-pressed", String(picked));
    $(".mk", b).innerHTML = right ? ICON.ok : picked && known(g) ? ICON.bad : "";
  });
  el.querySelectorAll("[data-submit],[data-check],[data-reveal],[data-num]").forEach((x) => (x.hidden = true));
  const call = g.type === "numeric" ? `answer(${JSON.stringify(rec.p)})` : g.type === "reveal" ? "show_answer()" : `answer(${rec.p.map((i) => `"${LETTERS[i]}"`).join(", ")})`;
  const correct = g.type === "numeric" ? g.answer : ans.map((i) => LETTERS[i]).join(", ");
  let verdict;
  if (g.type === "reveal") verdict = known(g) ? `<span class="verdict na">Answer: ${esc(correct)}</span>` : `<span class="verdict na">No checked answer yet; see the original page below.</span>`;
  else if (rec.ok === true) verdict = `<span class="verdict ok">${ICON.ok} Correct</span>`;
  else if (rec.ok === false) verdict = `<span class="verdict bad">${ICON.bad} Not quite. Answer: ${esc(correct)}</span>`;
  else verdict = `<span class="verdict na">No checked answer for this one yet.</span>`;
  const badge = known(g) ? `<span class="badge ${g.answer_source}">${BADGE[g.answer_source] || ""}</span>` : "";
  let h = `<div><span class="prompt">&gt;&gt;&gt;</span> ${esc(call)}</div><div class="verdict-row">${verdict}${badge}<button class="link-btn again" type="button" data-again>Try again</button></div>`;
  if (g.note) h += `<div class="adm warn"><p class="adm-t">About the official answer</p><p>${esc(g.note)}</p></div>`;
  if (g.explanation) h += `<div class="adm"><p class="adm-t">Explanation</p><p>${esc(g.explanation)}</p></div>`;
  res.innerHTML = h;
  if (g.type === "reveal") { const s = $(".src", el); if (s) s.open = true; }
}

/* ---------- page ---------- */
let current = [];
async function render() {
  const list = $("#list");
  let groups;
  if (state.q) {
    const all = (await Promise.all(Object.keys(meta.weeks).map((w) => loadWeek(+w)))).flat();
    const q = state.q.toLowerCase();
    groups = all.filter((g) => (g.text + "\n" + (g.code || "") + "\n" + g.options.map((o) => o.text).join("\n")).toLowerCase().includes(q));
    $("#title").innerHTML = `Search: <span class="num">${esc(state.q)}</span>`;
    $("#week-desc").textContent = "";
  } else {
    groups = await loadWeek(state.w);
    $("#title").innerHTML = `<span class="num">Week ${state.w}</span> · ${esc(WEEKS[state.w])}`;
    $("#week-desc").textContent = DESC[state.w];
  }
  const base = groups;
  // year chips
  const tc = {};
  base.forEach((g) => g.terms.forEach((t) => (tc[t] = (tc[t] || 0) + 1)));
  const terms = Object.keys(tc).sort((a, b) => termKey(b) - termKey(a));
  $("#years").innerHTML = `<button class="chip clear" type="button" aria-pressed="${state.years.size === 0}" data-year="">All sessions</button>` +
    terms.map((t) => `<button class="chip" type="button" aria-pressed="${state.years.has(t)}" data-year="${t}">${termLabel(t)} <span aria-hidden="true">·</span> ${tc[t]}</button>`).join("");
  // filter + sort
  if (state.years.size) groups = groups.filter((g) => g.terms.some((t) => state.years.has(t)));
  if (state.f === "todo") groups = groups.filter((g) => !store.a[g.gid]);
  if (state.f === "wrong") groups = groups.filter((g) => store.a[g.gid]?.ok === false);
  if (state.f === "saved") groups = groups.filter((g) => store.s[g.gid]);
  const newest = (g) => Math.max(...g.terms.map(termKey)), oldest = (g) => Math.min(...g.terms.map(termKey));
  if (state.s === "new") groups = [...groups].sort((a, b) => newest(b) - newest(a));
  if (state.s === "old") groups = [...groups].sort((a, b) => oldest(a) - oldest(b));
  current = groups;
  list.innerHTML = groups.map((g, i) => renderQ(g, i + 1)).join("");
  groups.forEach((g) => paint($(`#g-${g.gid}`), g));
  markScrollers(list);
  const empty = $("#empty");
  empty.hidden = groups.length > 0;
  empty.textContent = state.f === "wrong" ? "Nothing answered wrong here. Nice." : state.f === "saved" ? "No saved questions in this view yet." : state.f === "todo" ? "Every question in this view is answered." : "No questions match.";
  // segmented control + sort
  document.querySelectorAll("#status button").forEach((b) => b.setAttribute("aria-checked", String(b.dataset.f === state.f)));
  $("#sort").value = state.s;
  summary(base);
  renderToc();
  if (state.g) { const el = $(`#g-${state.g}`); if (el) { el.scrollIntoView({ block: "start" }); focusQ(el); } state.g = ""; }
}
function summary(base) {
  const answered = base.filter((g) => store.a[g.gid]);
  const ok = answered.filter((g) => store.a[g.gid].ok === true).length;
  const bad = answered.filter((g) => store.a[g.gid].ok === false).length;
  const repeats = base.filter((g) => g.terms.length > 1).length;
  $("#summary").textContent = `${base.length} questions · ${repeats} asked in more than one session · ${answered.length} answered, ${ok} correct`;
  $("#bar-ok").style.width = (base.length ? (ok / base.length) * 100 : 0) + "%";
  $("#bar-bad").style.width = (base.length ? (bad / base.length) * 100 : 0) + "%";
}
function renderToc() {
  const done = {};
  Object.values(store.a).forEach((r) => (done[r.w] = (done[r.w] || 0) + 1));
  $("#weeks").innerHTML = WEEKS.map((t, w) => `<li><a href="#w${w}"${!state.q && w === state.w ? ' aria-current="page"' : ""}>` +
    `<span class="wk">W${String(w).padStart(2, "0")}</span><span class="tp">${esc(t)}</span><span class="ct">${done[w] || 0} / ${meta.weeks[w] || 0} answered</span></a></li>`).join("");
}
function markScrollers(root) {
  requestAnimationFrame(() => root.querySelectorAll("pre[data-code]").forEach((p) => p.classList.toggle("scrolls", p.scrollWidth > p.clientWidth + 1)));
}

/* ---------- interaction ---------- */
const groupOf = (el) => current.find((g) => g.gid === el.dataset.gid);
document.addEventListener("click", (e) => {
  const t = e.target;
  const art = t.closest(".q");
  if (t.closest("[data-copy]")) {
    const b = t.closest("[data-copy]"), code = $("pre[data-code]", b.parentElement).textContent;
    navigator.clipboard?.writeText(code).then(() => { b.textContent = "Copied"; setTimeout(() => (b.textContent = "Copy"), 1200); });
    return;
  }
  if (t.closest(".zoomable")) {
    const im = t.closest(".zoomable");
    $("#zoom-body").innerHTML = `<img src="${esc(im.getAttribute("src"))}" alt="${esc(im.alt)}">`;
    $("#zoom").showModal();
    return;
  }
  if (t.closest("[data-year]")) {
    const y = t.closest("[data-year]").dataset.year;
    if (!y) state.years.clear(); else state.years.has(y) ? state.years.delete(y) : state.years.add(y);
    writeHash(); render(); return;
  }
  if (t.closest("#status button")) { state.f = t.closest("button").dataset.f; writeHash(); render(); return; }
  if (!art) return;
  const g = groupOf(art);
  if (!g) return;
  focusQ(art, false);
  const opt = t.closest(".opt");
  if (opt && !opt.disabled) pickOpt(art, g, +opt.dataset.i);
  else if (t.closest("[data-submit]")) submitMulti(art, g);
  else if (t.closest("[data-check]")) checkNum(art, g);
  else if (t.closest("[data-reveal]")) { grade(g, []); paint(art, g); after(); }
  else if (t.closest("[data-again]")) { delete store.a[g.gid]; persist(); art.outerHTML = renderQ(g, +$(".q-id", art).textContent.slice(1).replace("¶", "")); const n = $(`#g-${g.gid}`); paint(n, g); markScrollers(n); focusQ(n); after(); }
  else if (t.closest("[data-save]")) { const b = t.closest("[data-save]"); store.s[g.gid] ? delete store.s[g.gid] : (store.s[g.gid] = 1); persist(); b.setAttribute("aria-pressed", String(!!store.s[g.gid])); }
});
function pickOpt(art, g, i) {
  if (g.type === "multi") {
    const b = $(`.opt[data-i="${i}"]`, art);
    b.setAttribute("aria-pressed", String(b.getAttribute("aria-pressed") !== "true"));
    $("[data-submit]", art).disabled = !art.querySelector('.opt[aria-pressed="true"]');
  } else { grade(g, [i]); paint(art, g); after(); }
}
function submitMulti(art, g) {
  const pick = [...art.querySelectorAll('.opt[aria-pressed="true"]')].map((b) => +b.dataset.i);
  if (!pick.length) return;
  grade(g, pick); paint(art, g); after();
}
function checkNum(art, g) {
  const v = $("[data-num]", art).value;
  if (!v.trim()) return;
  grade(g, v); paint(art, g); after();
}
async function after() { summary(state.q ? current : await loadWeek(state.w)); renderToc(); }

/* keyboard: J/K move, digits pick, Enter submit */
let focused = null;
function focusQ(el, scroll = true) {
  focused?.classList.remove("focus");
  focused = el; el.classList.add("focus");
  if (scroll) { el.focus({ preventScroll: true }); el.scrollIntoView({ block: "start", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" }); }
}
document.addEventListener("keydown", (e) => {
  if (e.target.matches("input, select, textarea") || e.metaKey || e.ctrlKey || e.altKey) {
    if (e.key === "Enter" && e.target.matches("[data-num]")) { const a = e.target.closest(".q"); checkNum(a, groupOf(a)); }
    return;
  }
  const arts = [...document.querySelectorAll(".q")];
  if (!arts.length) return;
  const at = focused && document.contains(focused) ? arts.indexOf(focused) : -1;
  if (e.key === "j" || e.key === "k") {
    const n = e.key === "j" ? Math.min(arts.length - 1, at + 1) : Math.max(0, at - 1);
    focusQ(arts[n]); e.preventDefault(); return;
  }
  if (at < 0) return;
  const g = groupOf(focused);
  if (/^[1-8]$/.test(e.key) && g.options[+e.key - 1]) { const b = $(`.opt[data-i="${+e.key - 1}"]`, focused); if (b && !b.disabled) pickOpt(focused, g, +e.key - 1); }
  else if (e.key === "Enter" && g.type === "multi") submitMulti(focused, g);
});

/* toolbar */
$("#sort").addEventListener("change", (e) => { state.s = e.target.value; writeHash(); render(); });
let sTimer;
$("#q").addEventListener("input", (e) => { clearTimeout(sTimer); sTimer = setTimeout(() => { state.q = e.target.value.trim(); render(); }, 220); });
$("#theme").addEventListener("click", () => {
  const dark = document.documentElement.dataset.theme ? document.documentElement.dataset.theme === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
  document.documentElement.dataset.theme = dark ? "light" : "dark";
  try { localStorage.setItem("joc:theme", document.documentElement.dataset.theme); } catch (e) { /* ignore */ }
});
const size = (d) => {
  const cur = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--fs")) || 16;
  const n = Math.min(21, Math.max(14, cur + d));
  document.documentElement.style.setProperty("--fs", n + "px");
  try { localStorage.setItem("joc:size", n); } catch (e) { /* ignore */ }
  markScrollers(document);
};
$("#smaller").addEventListener("click", () => size(-1));
$("#larger").addEventListener("click", () => size(1));
$("#menu").addEventListener("click", () => { const o = $("#toc").classList.toggle("open"); $("#menu").setAttribute("aria-expanded", String(o)); });
$("#toc").addEventListener("click", (e) => { if (e.target.closest("a")) { $("#toc").classList.remove("open"); $("#menu").setAttribute("aria-expanded", "false"); $("#q").value = ""; state.q = ""; } });
$("#export").addEventListener("click", () => {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([JSON.stringify(store)], { type: "application/json" }));
  a.download = `joc-progress-${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
});
$("#import").addEventListener("change", async (e) => {
  try {
    const d = JSON.parse(await e.target.files[0].text());
    if (!d || typeof d.a !== "object") throw new Error("not a progress file");
    Object.assign(store.a, d.a); Object.assign(store.s, d.s || {}); persist(); render();
  } catch (err) { alert("That file is not a JOC progress export."); }
  e.target.value = "";
});
window.addEventListener("hashchange", () => {
  const prevW = state.w;
  readHash();
  const jump = state.g;
  render().then(() => { if (!jump && state.w !== prevW) window.scrollTo(0, 0); });
});

(async function init() {
  readHash();
  try { meta = await fetch("data/meta.json").then((r) => r.json()); } catch (e) { /* counts only */ }
  if (!location.hash) writeHash(true);
  await render();
})();
