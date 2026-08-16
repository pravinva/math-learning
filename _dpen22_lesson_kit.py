#!/usr/bin/env python3
"""Shared HTML kit for DPEN022 short-lesson practice sets."""
from pathlib import Path
import html as H
import re

CSS = r'''
:root{--navy:#1B3A5C;--orange:#FF3621;--blue:#185FA5;--bg:#fafaf8;--text:#2c2a28;--muted:#6b6762;--line:#e8e6e0;--green:#15803d;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:Georgia,"Times New Roman",serif;background:var(--bg);color:var(--text);line-height:1.65;padding:28px 18px 70px;}
.wrap{max-width:900px;margin:0 auto;background:#fff;border:1px solid var(--line);padding:28px 30px 40px;border-radius:10px;}
.eyebrow{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:6px;}
h1{font-size:clamp(24px,3vw,34px);color:var(--navy);margin-bottom:8px;}
h2{font-size:20px;color:var(--navy);margin:26px 0 10px;padding-bottom:6px;border-bottom:2px solid var(--navy);}
h3{font-size:16px;color:var(--blue);margin:16px 0 8px;}
.sub{color:var(--muted);margin-bottom:14px;}
.nav a{color:var(--blue);font-weight:600;text-decoration:none;margin-right:14px;}
.lesson,.summary,.formulas,.problems,.answers{margin:14px 0 18px;}
.lesson p,.summary li,.formulas li{margin:8px 0;}
.summary,.formulas{background:#f8fafc;border:1px solid var(--line);border-radius:8px;padding:14px 16px;}
.formulas{background:#eef6ff;border-color:#c9dff7;}
.formulas ul,.summary ul{margin-left:20px;}
.ex{background:#fff7f5;border-left:4px solid var(--orange);padding:10px 12px;margin:12px 0;border-radius:0 6px 6px 0;}
.problems ol{margin-left:22px;}
.problems li{margin:10px 0;}
.ans{background:#f0fdf4;border-left:4px solid var(--green);padding:8px 12px;margin:8px 0;border-radius:0 6px 6px 0;overflow-x:auto;}
.ans .katex-display{overflow-x:auto;margin:6px 0;}
@media(max-width:640px){.ans .katex{font-size:0.95em;}}
.tag{display:inline-block;background:var(--orange);color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;margin-bottom:8px;}
.chiprow{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 18px;}
.chip{display:inline-block;padding:7px 11px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:600;border:1px solid #c9dff7;background:#eef6ff;color:var(--blue);}
.chip.on{background:var(--navy);border-color:var(--navy);color:#fff;}
'''


_MATH_SPAN = re.compile(
    r'(?<!\\)\\\(.*?(?<!\\)\\\)|(?<!\\)\\\[.*?(?<!\\)\\\]|\$\$.*?\$\$',
    re.S,
)
_PROTECTED = re.compile(r'<svg[\s\S]*?</svg>|<style[\s\S]*?</style>|<script[\s\S]*?</script>', re.I)


def escape_math_brackets(html: str) -> str:
    """Escape < and > inside math spans.

    The browser parses the HTML before KaTeX ever runs, so a raw `<` in
    something like \\(-\\pi/2<x<\\pi/2\\) opens a bogus tag and swallows the
    rest of the line. Entities survive parsing and reach KaTeX as plain text.
    """
    def fix_span(m):
        return m.group(0).replace('<', '&lt;').replace('>', '&gt;')

    out, pos = [], 0
    for prot in _PROTECTED.finditer(html):
        out.append(_MATH_SPAN.sub(fix_span, html[pos:prot.start()]))
        out.append(prot.group(0))
        pos = prot.end()
    out.append(_MATH_SPAN.sub(fix_span, html[pos:]))
    return ''.join(out)


def page(title, body):
    html = f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'\\\\[',right:'\\\\]',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}]}});"></script>
<style>{CSS}</style>
</head><body><div class="wrap">
{body}
</div></body></html>
'''
    return escape_math_brackets(html.replace("\\'", "'"))


def set_page(out: Path, subject: str, meta: dict, siblings: list, hub_up='../../index.html', home_up='../../../index.html'):
    n = len(meta['problems'])
    assert n == len(meta['answers']), f"{meta['slug']}: {n} problems vs {len(meta['answers'])} answers"
    chips = ''.join(
        f'<a class="chip{" on" if s["slug"]==meta["slug"] else ""}" href="{s["slug"]}.html">{s["short"]}</a>'
        for s in siblings
    )
    lesson_html = ''.join(f'<p>{p}</p>' for p in meta['lesson'])
    if meta.get('example'):
        lesson_html += f'<div class="ex"><strong>Worked example.</strong> {meta["example"]}</div>'
    points = ''.join(f'<li>{x}</li>' for x in meta['points'])
    formulas = ''.join(f'<li>{x}</li>' for x in meta['formulas'])
    probs = ''.join(f'<li>{q}</li>' for q in meta['problems'])
    formulas_title = meta.get('formulas_title', 'Formulas &amp; identities')
    body = f'''
<div class="eyebrow">DPEN022 {H.escape(subject)} · {meta["source"]}</div>
<span class="tag">{meta["group"]}</span>
<h1>{H.escape(meta["title"])}</h1>
<p class="sub">{meta["blurb"]}</p>
<div class="nav">
  <a href="index.html">← Lesson sets hub</a>
  <a href="{meta["slug"]}-answers.html">Open Separate Answers</a>
  <a href="{hub_up}">Class notes</a>
  <a href="{home_up}">DPEN22 home</a>
</div>
<div class="chiprow">{chips}</div>

<h2>1. Short lesson</h2>
<div class="lesson">{lesson_html}</div>

<h2>2. Key points summary</h2>
<div class="summary"><ul>{points}</ul></div>

<h2>3. {formulas_title}</h2>
<div class="formulas"><ul>{formulas}</ul></div>

<h2>4. Practice problems ({n})</h2>
<div class="problems"><ol>{probs}</ol></div>

<div class="chiprow" style="margin-top:22px;">
  <a class="chip on" href="{meta["slug"]}-answers.html">✅ Answers for this set</a>
</div>
'''
    out.mkdir(parents=True, exist_ok=True)
    (out / f'{meta["slug"]}.html').write_text(page(meta['title'], body))
    answers_page(out, subject, meta, siblings, n)


def answers_page(out: Path, subject: str, meta: dict, siblings: list, n: int):
    chips = ''.join(
        f'<a class="chip{" on" if s["slug"]==meta["slug"] else ""}" href="{s["slug"]}-answers.html">{s["short"]}</a>'
        for s in siblings
    )
    rows = ''.join(
        f'<div class="ans"><strong>Q{i}.</strong> {a}</div>'
        for i, a in enumerate(meta['answers'], 1)
    )
    title = f'{meta["title"]} — Answers'
    body = f'''
<div class="eyebrow">DPEN022 {H.escape(subject)} · {meta["source"]}</div>
<span class="tag">{meta["group"]} · ANSWERS</span>
<h1>{H.escape(title)}</h1>
<p class="sub">Answers to the {n} practice problems in this set.</p>
<div class="nav">
  <a href="{meta["slug"]}.html">← Back to lesson &amp; problems</a>
  <a href="index.html">Lesson sets hub</a>
  <a href="../../index.html">Class notes</a>
</div>
<div class="chiprow">{chips}</div>

<h2>Answers ({n})</h2>
<div class="answers">{rows}</div>
'''
    (out / f'{meta["slug"]}-answers.html').write_text(page(title, body))


def write_hub(out: Path, subject: str, title: str, blurb: str, groups: dict, extra_nav=''):
    cards = []
    for g in groups.values():
        links = ''.join(
            f'<a class="chip" href="{s["slug"]}.html">{s["short"]}: {H.escape(s["title"])}</a>'
            f'<a class="chip on" href="{s["slug"]}-answers.html">{s["short"]} answers</a>'
            for s in g['sets']
        )
        nprob = len(g['sets'][0]['problems']) if g['sets'] else 15
        cards.append(f'''<div class="summary" style="margin-bottom:16px;">
<h3 style="margin-top:0;">{H.escape(g["label"])} — {len(g["sets"])} sets</h3>
<p class="sub" style="margin:0 0 10px;">Each set: short lesson · key points · formulas · {nprob} problems, with answers on a separate page</p>
<div class="chiprow">{links}</div>
</div>''')
    body = f'''
<div class="eyebrow">DPEN022 {H.escape(subject)}</div>
<span class="tag">LESSON SETS</span>
<h1>{H.escape(title)}</h1>
<p class="sub">{blurb}</p>
<div class="nav">
  <a href="../../index.html">← Class notes hub</a>
  <a href="../../../index.html">DPEN22 home</a>
  {extra_nav}
</div>
{''.join(cards)}
'''
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(page(title, body))


def generate(out: Path, subject: str, groups: dict, hub_title: str, hub_blurb: str, extra_nav=''):
    for g in groups.values():
        for s in g['sets']:
            set_page(out, subject, s, g['sets'])
            print('wrote', s['slug'])
    write_hub(out, subject, hub_title, hub_blurb, groups, extra_nav=extra_nav)
    print('hub written to', out)
