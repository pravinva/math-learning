#!/usr/bin/env python3
"""Generate MATH142 revision packs (18) with separate answer pages."""
from pathlib import Path
from _math142_rev_data_a import PACKS as PACKS_A
from _math142_rev_data_b import PACKS as PACKS_B

OUT = Path(__file__).resolve().parent / "siddharth" / "math142" / "revision"
ORDER = [
    "t01-integration",
    "t02-partial-improper",
    "t03-numerical",
    "t04-polar",
    "t05-parametric",
    "t06-areas-volumes",
    "t07-arc-surfaces",
    "t08-first-order-de",
    "t09-second-order-shm",
    "t10-limits-series-taylor",
    "q1-weeks1-3",
    "q2-weeks4-6",
    "q3-weeks7-9",
    "q4-weeks10-12",
    "m1-exam1-style",
    "m2-exam2-style",
    "f1-full-a",
    "f2-full-b",
]

KIND_LABEL = {
    "topic": "Topic revision",
    "quarter": "Quarter revision",
    "mid": "Mid revision",
    "full": "Full revision",
}

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap');
:root{
  --navy:#1B2431;--red:#FF3621;--paper:#ffffff;--grid:#e3e8ef;--line:#c8d2de;
  --text:#1B2431;--muted:#5b6779;--blue-box:#eef3fb;--green:#2f8f5b;--amber:#b45309;
}
*{box-sizing:border-box}
body{
  margin:0;font-family:'Barlow',sans-serif;color:var(--text);
  background:
    linear-gradient(var(--grid) 1px, transparent 1px) 0 0/28px 28px,
    linear-gradient(90deg, var(--grid) 1px, transparent 1px) 0 0/28px 28px,
    var(--paper);
  padding:0 0 80px;
}
header{background:var(--navy);color:#fff;padding:32px 24px 28px;border-bottom:6px solid var(--red)}
header .eyebrow{font-family:'Roboto Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#9fb0c9;margin-bottom:6px}
header h1{margin:0;font-size:clamp(22px,3vw,28px);font-weight:700}
header p{margin:8px 0 0;color:#c3ccdb;font-size:15px;max-width:720px;line-height:1.55}
.wrap{max-width:860px;margin:0 auto;padding:0 24px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 8px}
.chip{display:inline-block;padding:7px 11px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:600;
  border:1px solid var(--line);background:#fff;color:var(--navy)}
.chip:hover{border-color:var(--red);color:var(--red)}
.chip.on{background:var(--navy);border-color:var(--navy);color:#fff}
.chip.ans{background:#f0fdf4;border-color:#86efac;color:var(--green)}
.chip.hub{background:var(--blue-box);border-color:#b8c9e0;color:#185FA5}
.meta{font-size:13px;color:var(--muted);margin:4px 0 14px}
.note{background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px 14px;margin:12px 0;font-size:14px;line-height:1.55}
.q{background:#fff;border:1px solid var(--line);border-radius:8px;padding:14px 16px;margin:14px 0}
.q .num{font-family:'Roboto Mono',monospace;font-size:12px;letter-spacing:.08em;color:var(--red);font-weight:700;margin-bottom:6px}
.q .body{font-size:15px;line-height:1.65}
.ans{background:#f3faf6;border-left:4px solid var(--green);padding:12px 14px;margin:10px 0;border-radius:0 8px 8px 0;font-size:15px;line-height:1.65}
.ans h3{margin:0 0 8px;font-size:15px;color:var(--green)}
.card{background:#fff;border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:0 0 14px}
.card h3{margin:0 0 6px;font-size:17px;color:var(--navy)}
.tag{display:inline-block;font-family:'Roboto Mono',monospace;font-size:11px;letter-spacing:.06em;
  padding:3px 7px;border-radius:4px;background:var(--blue-box);color:#185FA5;margin-bottom:8px}
.tag.quarter{background:#fff7ed;color:var(--amber)}
.tag.mid{background:#fef2f2;color:#b91c1c}
.tag.full{background:#1B2431;color:#fff}
.footer{margin:28px 0 10px;font-size:13px;color:var(--muted)}
.footer a{color:#185FA5;text-decoration:none}
"""


def page(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script>
window.MathJax = {{
  tex: {{ inlineMath: [['$','$'],['\\\\(','\\\\)']], displayMath: [['$$','$$'],['\\\\[','\\\\]']] }}
}};
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<style>{CSS}</style>
</head><body>
{body}
</body></html>
"""


def nav_chips(active: str, ans: bool = False) -> str:
    bits = [
        '<a class="chip hub" href="index.html">Revision hub</a>',
        '<a class="chip" href="../index.html">MATH142 home</a>',
    ]
    if active:
        qhref = f"{active}.html"
        ahref = f"{active}-answers.html"
        bits.append(f'<a class="chip {"on" if not ans else ""}" href="{qhref}">Questions</a>')
        bits.append(f'<a class="chip ans {"on" if ans else ""}" href="{ahref}">Answers</a>')
    return '<div class="wrap"><div class="chips">' + "".join(bits) + "</div></div>"


def render_questions(pack: dict, slug: str) -> str:
    parts = []
    for i, item in enumerate(pack["questions"], 1):
        parts.append(
            f'<div class="q" id="q{i}"><div class="num">QUESTION {i}</div>'
            f'<div class="body">{item["q"]}</div></div>'
        )
    kind = pack["kind"]
    body = f"""
<header>
  <div class="wrap">
    <div class="eyebrow">MATH142 · {KIND_LABEL[kind].upper()} · {pack["id"]}</div>
    <h1>{pack["title"]}</h1>
    <p>{pack["blurb"]} Coverage: {pack["weeks"]}.</p>
  </div>
</header>
{nav_chips(slug, False)}
<div class="wrap">
  <p class="meta">{len(pack["questions"])} questions · answers on a separate page · show full working</p>
  <div class="note"><strong>How to use.</strong> Attempt every question before opening the answers page.
  Aim for exam-style written solutions (method + justification + boxed result).</div>
  {"".join(parts)}
  <p class="footer"><a href="{slug}-answers.html">→ Full worked answers</a> · <a href="index.html">Revision hub</a></p>
</div>
"""
    return page(f"MATH142 {pack['id']} — Questions", body)


def render_answers(pack: dict, slug: str) -> str:
    parts = []
    for i, item in enumerate(pack["questions"], 1):
        parts.append(
            f'<div class="ans" id="a{i}"><h3>Q{i} — worked solution</h3>{item["a"]}</div>'
        )
    kind = pack["kind"]
    body = f"""
<header>
  <div class="wrap">
    <div class="eyebrow">MATH142 · ANSWERS · {pack["id"]}</div>
    <h1>{pack["title"]} — Answers</h1>
    <p>Fully worked solutions for the {KIND_LABEL[kind].lower()} pack ({pack["weeks"]}).</p>
  </div>
</header>
{nav_chips(slug, True)}
<div class="wrap">
  <p class="meta">{len(pack["questions"])} worked solutions</p>
  {"".join(parts)}
  <p class="footer"><a href="{slug}.html">← Back to questions</a> · <a href="index.html">Revision hub</a></p>
</div>
"""
    return page(f"MATH142 {pack['id']} — Answers", body)


def render_hub(packs: dict) -> str:
    sections = [
        ("topic", "Topic revision sets", "Related-topic drills aligned to weekly clusters."),
        ("quarter", "Quarter revisions", "Three-week blocks — integration → applications → DEs → series."),
        ("mid", "Mid revisions", "Exam 1 style (W1–6) and Exam 2 style (W7–12)."),
        ("full", "Full revisions", "Whole-subject mixed papers with separate answers."),
    ]
    blocks = []
    for kind, heading, sub in sections:
        cards = []
        for slug in ORDER:
            p = packs[slug]
            if p["kind"] != kind:
                continue
            cards.append(
                f"""<div class="card">
  <span class="tag {kind}">{p["id"]} · {KIND_LABEL[kind]}</span>
  <h3>{p["title"]}</h3>
  <p class="meta">{p["weeks"]} · {len(p["questions"])} questions</p>
  <p style="font-size:14px;line-height:1.55;margin:0 0 10px">{p["blurb"]}</p>
  <div class="chips" style="margin:0">
    <a class="chip on" href="{slug}.html">Questions</a>
    <a class="chip ans" href="{slug}-answers.html">Answers</a>
  </div>
</div>"""
            )
        blocks.append(
            f'<h2 style="margin:28px 0 10px;font-size:22px;color:var(--navy)">{heading}</h2>'
            f'<p class="meta">{sub}</p>' + "".join(cards)
        )

    body = f"""
<header>
  <div class="wrap">
    <div class="eyebrow">MATH142 · ENGINEERING MATHEMATICS 2</div>
    <h1>Revision packs</h1>
    <p>18 practice packs with separate full worked answers: 10 topic · 4 quarter · 2 mid · 2 full.</p>
  </div>
</header>
<div class="wrap">
  <div class="chips">
    <a class="chip on" href="index.html">Revision hub</a>
    <a class="chip" href="../index.html">MATH142 home</a>
    <a class="chip" href="../MATH142_Exam1_Review.html">Exam 1 review</a>
    <a class="chip" href="../MATH142_Exam2_Review.html">Exam 2 review</a>
  </div>
  <div class="note"><strong>Suggested path.</strong> Topic packs while learning → Quarter checks every three weeks →
  Mid A before Exam 1 → Mid B before Exam 2 → Full A/B in the final fortnight.</div>
  {"".join(blocks)}
  <p class="footer"><a href="../index.html">← MATH142 home</a></p>
</div>
"""
    return page("MATH142 Revision Packs", body)


def main():
    packs = {**PACKS_A, **PACKS_B}
    missing = [s for s in ORDER if s not in packs]
    if missing:
        raise SystemExit(f"Missing packs: {missing}")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(render_hub(packs), encoding="utf-8")
    for slug in ORDER:
        p = packs[slug]
        (OUT / f"{slug}.html").write_text(render_questions(p, slug), encoding="utf-8")
        (OUT / f"{slug}-answers.html").write_text(render_answers(p, slug), encoding="utf-8")
    nq = sum(len(packs[s]["questions"]) for s in ORDER)
    print(f"wrote {OUT} — {len(ORDER)} packs, {nq} questions, {2*len(ORDER)+1} HTML files")


if __name__ == "__main__":
    main()
