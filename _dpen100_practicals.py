#!/usr/bin/env python3
"""Generate DPEN100 / ENGG100 Practicals-to-do HTML from worksheet + Hahn & Valentine refs."""
from pathlib import Path
import html as H
import shutil

OUT = Path(__file__).resolve().parent / 'siddharth' / 'dpen100' / 'practicals'
STUDY = Path('/Users/pravin.varma/Documents/Study/DPEN100')
BOOK = 'Hahn &amp; Valentine, <em>Essential MATLAB for Engineers and Scientists</em> (7th ed., 2019)'

CSS = r'''
:root{--navy:#1B3A5C;--orange:#FF3621;--blue:#185FA5;--bg:#fafaf8;--text:#2c2a28;--muted:#6b6762;--line:#e8e6e0;--green:#15803d;--amber:#b45309;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Georgia,"Times New Roman",serif;background:var(--bg);color:var(--text);line-height:1.65;padding:28px 18px 80px}
.wrap{max-width:920px;margin:0 auto;background:#fff;border:1px solid var(--line);padding:28px 30px 42px;border-radius:10px}
.eyebrow{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
h1{font-size:clamp(24px,3.2vw,34px);color:var(--navy);margin-bottom:8px}
h2{font-size:20px;color:var(--navy);margin:28px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--navy)}
h3{font-size:16px;color:var(--blue);margin:0 0 8px}
.sub{color:var(--muted);margin-bottom:14px}
.nav a{color:var(--blue);font-weight:600;text-decoration:none;margin-right:14px}
.tag{display:inline-block;background:var(--orange);color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;margin-bottom:8px}
.ref{display:inline-block;background:#eef6ff;border:1px solid #c9dff7;color:var(--blue);font-size:12px;font-weight:600;padding:2px 8px;border-radius:4px;margin:0 6px 8px 0}
.star{display:inline-block;background:#fff7ed;border:1px solid #f0b429;color:#92400e;font-size:11px;font-weight:700;padding:2px 7px;border-radius:4px;margin-left:6px}
.q{background:#f8fafc;border:1px solid var(--line);border-radius:8px;padding:14px 16px;margin:12px 0}
.q ol{margin:8px 0 0 22px}.q li{margin:4px 0}
.hint{background:#fff7f5;border-left:4px solid var(--orange);padding:8px 12px;margin-top:10px;border-radius:0 6px 6px 0;font-size:14px}
.do{background:#f0fdf4;border-left:4px solid var(--green);padding:8px 12px;margin-top:10px;border-radius:0 6px 6px 0;font-size:14px}
.plan{background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px 14px;margin:10px 0;font-family:ui-monospace,Menlo,monospace;font-size:13px;white-space:pre-wrap}
code,pre{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px}
pre{background:#1e293b;color:#e2e8f0;padding:12px 14px;border-radius:8px;overflow-x:auto;margin:10px 0}
.fig{display:block;max-width:100%;height:auto;margin:12px auto;border:1px solid var(--line);border-radius:6px;background:#fff}
.chiprow{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}
.chip{display:inline-block;padding:8px 12px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:600;border:1px solid #c9dff7;background:#eef6ff;color:var(--blue)}
.chip.on{background:var(--navy);border-color:var(--navy);color:#fff}
.chip.pdf{background:#fff7ed;border-color:#f0b429;color:var(--amber)}
.card{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:0 0 14px}
.card h3{margin-top:0}
.meta{font-size:13px;color:var(--muted);margin:4px 0 10px}
.todo-box{background:#fff7ed;border:2px solid #f0b429;border-radius:10px;padding:16px 18px;margin:18px 0}
.todo-box h2{margin-top:0;border:0;padding:0;font-size:18px;color:#92400e}
.prep{background:#eef6ff;border:1px solid #c9dff7;border-radius:10px;padding:16px 18px;margin:16px 0 22px}
.prep h2{margin:0 0 10px;border:0;padding:0;font-size:18px;color:var(--navy)}
.prep h3{margin:14px 0 6px;font-size:14px;color:var(--blue);text-transform:uppercase;letter-spacing:.04em}
.prep ul{margin:0 0 0 18px}.prep li{margin:4px 0}
.prep .ml{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.prep .ml code{background:#fff;border:1px solid #c9dff7;padding:3px 8px;border-radius:4px;font-size:12.5px;color:var(--navy)}
.ans{background:#f0fdf4;border-left:4px solid var(--green);padding:10px 12px;margin:8px 0;border-radius:0 6px 6px 0;overflow-x:auto}
.flow-wrap{overflow-x:auto;margin:12px 0;padding:8px;background:#fff;border:1px solid var(--line);border-radius:8px}
.flow-wrap svg{display:block;margin:0 auto;max-width:100%;height:auto}
.flow-cap{font-size:13px;color:var(--muted);text-align:center;margin:4px 0 0}
details{margin-top:8px} summary{cursor:pointer;font-weight:600;color:var(--navy)}
@media(max-width:640px){.wrap{padding:18px 14px 32px}}
'''


def page(title, body):
    return f'''<!DOCTYPE html>
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


def nav(current=''):
    items = [
        ('index.html', 'Practicals hub'),
        ('p03.html', 'P3'),
        ('p04.html', 'P4'),
        ('p05.html', 'P5'),
        ('lab06.html', 'Lab 6'),
        ('p08.html', 'P8'),
        ('../index.html', 'DPEN100 home'),
    ]
    chips = ''.join(
        f'<a class="chip{" on" if href==current else ""}" href="{href}">{lab}</a>'
        for href, lab in items
    )
    return f'<div class="chiprow">{chips}</div>'


def q(n, title, body, book_ref=None, star=False, hint=None, do=None, answer=None):
    refs = ''
    if book_ref:
        refs += f'<span class="ref">{book_ref}</span>'
    if star:
        refs += '<span class="star">★ Workshop priority</span>'
    tip = f'<div class="hint"><strong>Hint.</strong> {hint}</div>' if hint else ''
    action = f'<div class="do"><strong>Do.</strong> {do}</div>' if do else ''
    ans = ''
    if answer:
        ans = f'''<details class="ans-box" open style="margin-top:12px;">
<summary>✅ Model answer / flowchart</summary>
<div class="ans">{answer}</div>
</details>'''
    return f'''<div class="q" id="q{n}">
{refs}
<h3>Q{n}. {title}</h3>
{body}
{tip}{action}
{ans}
</div>'''


def prep_box(ideas, matlab, also=None):
    """Summary block at the top of each practical."""
    idea_li = ''.join(f'<li>{x}</li>' for x in ideas)
    ml = ''.join(f'<code>{x}</code>' for x in matlab)
    also_html = ''
    if also:
        also_html = '<h3>Also useful</h3><ul>' + ''.join(f'<li>{x}</li>' for x in also) + '</ul>'
    return f'''<div class="prep">
<h2>Before you start — key ideas &amp; MATLAB</h2>
<h3>Concepts &amp; ideas</h3>
<ul>{idea_li}</ul>
<h3>MATLAB functionality you will use</h3>
<div class="ml">{ml}</div>
{also_html}
</div>'''


# ───────────────────── SVG flowchart helpers ─────────────────────

NAVY, BLUE, ORANGE, GREEN, INK, MUT = '#1B3A5C', '#185FA5', '#FF3621', '#15803d', '#2c2a28', '#6b6762'


def _arrow(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="1.8"/>'
            f'<polygon points="{x2-5},{y2-8} {x2+5},{y2-8} {x2},{y2}" fill="{NAVY}"/>'
            if abs(x2 - x1) < 1 else
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="1.8" marker-end="url(#arr)"/>')


def _esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            if isinstance(s, str) else s)


def _terminal(cx, cy, w, h, text):
    text = _esc(text)
    return (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="{h/2}" '
            f'fill="#eef6ff" stroke="{NAVY}" stroke-width="2"/>'
            f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="13" font-family="Georgia,serif" '
            f'fill="{NAVY}" font-weight="700">{text}</text>')


def _process(cx, cy, w, h, text, lines=None):
    fill = '#f8fafc'
    box = (f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="6" '
           f'fill="{fill}" stroke="{BLUE}" stroke-width="2"/>')
    if lines:
        texts = ''.join(
            f'<text x="{cx}" y="{cy - 8*(len(lines)-1)/2 + 14*i}" text-anchor="middle" '
            f'font-size="12" font-family="Georgia,serif" fill="{INK}">{_esc(ln)}</text>'
            for i, ln in enumerate(lines)
        )
    else:
        texts = (f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12.5" '
                 f'font-family="Georgia,serif" fill="{INK}">{_esc(text)}</text>')
    return box + texts


def _decision(cx, cy, w, h, text, lines=None):
    # diamond via polygon
    pts = f'{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}'
    box = f'<polygon points="{pts}" fill="#fff7ed" stroke="{ORANGE}" stroke-width="2"/>'
    if lines:
        texts = ''.join(
            f'<text x="{cx}" y="{cy - 7*(len(lines)-1) + 13*i}" text-anchor="middle" '
            f'font-size="11.5" font-family="Georgia,serif" fill="{INK}" font-weight="600">{_esc(ln)}</text>'
            for i, ln in enumerate(lines)
        )
    else:
        texts = (f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12" '
                 f'font-family="Georgia,serif" fill="{INK}" font-weight="600">{_esc(text)}</text>')
    return box + texts


def _io(cx, cy, w, h, text):
    # parallelogram
    skew = 14
    pts = f'{cx-w/2+skew},{cy-h/2} {cx+w/2+skew},{cy-h/2} {cx+w/2-skew},{cy+h/2} {cx-w/2-skew},{cy+h/2}'
    return (f'<polygon points="{pts}" fill="#f0fdf4" stroke="{GREEN}" stroke-width="2"/>'
            f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12.5" '
            f'font-family="Georgia,serif" fill="{INK}">{_esc(text)}</text>')


def _vlink(x, y1, y2, label=None, label_side='right'):
    mid = (y1 + y2) / 2
    s = (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-6}" stroke="{NAVY}" stroke-width="1.8"/>'
         f'<polygon points="{x-5},{y2-8} {x+5},{y2-8} {x},{y2}" fill="{NAVY}"/>')
    if label:
        lx = x + 8 if label_side == 'right' else x - 8
        anchor = 'start' if label_side == 'right' else 'end'
        s += (f'<text x="{lx}" y="{mid+4}" text-anchor="{anchor}" font-size="11" '
              f'font-family="Georgia,serif" fill="{MUT}" font-weight="700">{label}</text>')
    return s


def _hlink(x1, y, x2, y2=None, label=None):
    y2 = y if y2 is None else y2
    # horizontal then optional vertical into target
    s = f'<path d="M{x1},{y} L{x2},{y}" fill="none" stroke="{NAVY}" stroke-width="1.8"/>'
    if label:
        s += (f'<text x="{(x1+x2)/2}" y="{y-6}" text-anchor="middle" font-size="11" '
              f'font-family="Georgia,serif" fill="{MUT}" font-weight="700">{label}</text>')
    return s


def flow_wrap(svg, caption):
    return f'<div class="flow-wrap">{svg}</div><p class="flow-cap">{caption}</p>'


def flowchart_fahrenheit():
    W, cx = 320, 160
    parts = [
        _terminal(cx, 28, 100, 32, 'Start'),
        _vlink(cx, 44, 68),
        _io(cx, 90, 200, 36, 'Input F (Fahrenheit)'),
        _vlink(cx, 108, 132),
        _process(cx, 158, 220, 40, '', lines=['C = (F − 32) × 5/9']),
        _vlink(cx, 178, 202),
        _io(cx, 224, 180, 36, 'Display C'),
        _vlink(cx, 242, 266),
        _terminal(cx, 284, 100, 32, 'Stop'),
    ]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 310" width="{W}" height="310" role="img" aria-label="Fahrenheit to Celsius flowchart">
{''.join(parts)}
</svg>'''
    return flow_wrap(svg, 'Flowchart — Fahrenheit → Celsius (Input / Operations / Output)')


def flowchart_vertical_motion():
    W, cx = 360, 180
    parts = [
        _terminal(cx, 28, 100, 32, 'Start'),
        _vlink(cx, 44, 68),
        _io(cx, 92, 260, 44, '',),
        # custom multi-line IO
    ]
    # rebuild with multi-line IO manually
    parts = [
        _terminal(cx, 28, 100, 32, 'Start'),
        _vlink(cx, 44, 70),
        _process(cx, 100, 280, 52, '', lines=['INPUT: g = 9.81, u = 60', 't = 0 : 0.01 : 12.3']),
        _vlink(cx, 126, 152),
        _process(cx, 182, 280, 48, '', lines=['OPERATIONS:', 's = u·t − ½ g t²  (array)']),
        _vlink(cx, 206, 232),
        _process(cx, 262, 280, 48, '', lines=['OUTPUT: plot(t, s)', 'title, labels, grid']),
        _vlink(cx, 286, 312),
        _terminal(cx, 330, 100, 32, 'Stop'),
    ]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 360" width="{W}" height="360" role="img" aria-label="Vertical motion flowchart">
{''.join(parts)}
</svg>'''
    return flow_wrap(svg, 'Flowchart — §2.4 Vertical motion under gravity (throw.m)')


def flowchart_quadratic():
    """Decision-heavy quadratic solver flowchart."""
    W, H = 720, 780
    cx = 360
    # Layout columns: left branch (a=0), centre main, right results
    parts = []
    parts.append(_terminal(cx, 28, 100, 32, 'Start'))
    parts.append(_vlink(cx, 44, 68))
    parts.append(_io(cx, 90, 200, 36, 'Input a, b, c'))
    parts.append(_vlink(cx, 108, 140))
    parts.append(_decision(cx, 180, 160, 70, '', lines=['a = 0?']))

    # YES left → nested a=0 branch
    # NO down → discriminant

    # Left arrow Yes
    parts.append(_hlink(cx - 80, 180, 140, label='Yes'))
    parts.append(f'<line x1="140" y1="180" x2="140" y2="214" stroke="{NAVY}" stroke-width="1.8"/>')
    parts.append(f'<polygon points="135,214 145,214 140,222" fill="{NAVY}"/>')
    parts.append(_decision(140, 260, 130, 64, '', lines=['b = 0?']))

    # b=0 Yes → further left
    parts.append(_hlink(140 - 65, 260, 40, label='Yes'))
    parts.append(f'<line x1="40" y1="260" x2="40" y2="300" stroke="{NAVY}" stroke-width="1.8"/>')
    parts.append(f'<polygon points="35,300 45,300 40,308" fill="{NAVY}"/>')
    parts.append(_decision(40, 340, 120, 60, '', lines=['c = 0?']))
    parts.append(_vlink(40, 370, 400, 'Yes', 'right'))
    parts.append(_process(40, 430, 130, 40, '', lines=['Indeterminate']))
    parts.append(_hlink(40 + 65, 340, 40 + 65))  # noop
    # c=0 No
    parts.append(_hlink(40 + 60, 340, 120, label='No'))
    parts.append(f'<line x1="120" y1="340" x2="120" y2="400" stroke="{NAVY}" stroke-width="1.8"/>')
    parts.append(f'<polygon points="115,400 125,400 120,408" fill="{NAVY}"/>')
    parts.append(_process(120, 430, 120, 40, '', lines=['No solution']))

    # b=0 No → linear
    parts.append(_vlink(140, 292, 400, 'No', 'right'))
    parts.append(_process(140, 440, 150, 44, '', lines=['x = −c/b', '(linear)']))

    # Merge left branch down to stop later via lines

    # a=0 No → discriminant path (centre-right)
    parts.append(_vlink(cx, 215, 270, 'No', 'right'))
    parts.append(_decision(cx, 310, 170, 72, '', lines=['b² < 4ac?']))

    # Yes → complex
    parts.append(_hlink(cx + 85, 310, 560, label='Yes'))
    parts.append(f'<line x1="560" y1="310" x2="560" y2="350" stroke="{NAVY}" stroke-width="1.8"/>')
    parts.append(f'<polygon points="555,350 565,350 560,358" fill="{NAVY}"/>')
    parts.append(_process(560, 390, 150, 44, '', lines=['Complex roots', '(or use complex √)']))

    # No → equal?
    parts.append(_vlink(cx, 346, 400, 'No', 'right'))
    parts.append(_decision(cx, 440, 170, 72, '', lines=['b² = 4ac?']))

    # Yes equal
    parts.append(_hlink(cx + 85, 440, 560, label='Yes'))
    parts.append(f'<line x1="560" y1="440" x2="560" y2="480" stroke="{NAVY}" stroke-width="1.8"/>')
    parts.append(f'<polygon points="555,480 565,480 560,488" fill="{NAVY}"/>')
    parts.append(_process(560, 520, 160, 44, '', lines=['Equal root', 'x = −b/(2a)']))

    # No → two real
    parts.append(_vlink(cx, 476, 530, 'No', 'right'))
    parts.append(_process(cx, 570, 240, 52, '', lines=['x₁, x₂ via quadratic formula', '√(b² − 4ac)']))

    # All converge conceptually to Stop
    parts.append(_vlink(cx, 596, 650))
    parts.append(_vlink(560, 542, 650))
    parts.append(_vlink(560, 412, 650))
    parts.append(f'<line x1="40" y1="450" x2="40" y2="650" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    parts.append(f'<line x1="140" y1="462" x2="140" y2="650" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    parts.append(f'<line x1="120" y1="450" x2="120" y2="650" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    parts.append(f'<line x1="40" y1="650" x2="560" y2="650" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>')
    parts.append(_vlink(cx, 650, 700))
    parts.append(_terminal(cx, 722, 100, 32, 'Stop'))

    # legend
    parts.append(f'<text x="20" y="765" font-size="11" font-family="Georgia,serif" fill="{MUT}">Diamonds = decisions (every branch the structure plan needs). Dashed lines merge to Stop.</text>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Quadratic equation flowchart">
{''.join(parts)}
</svg>'''
    return flow_wrap(svg, 'Flowchart — quadratic ax²+bx+c=0 with all decision boxes (Book pp. 94–96)')


def flowchart_euclidean():
    W, cx = 400, 200
    parts = [
        _terminal(cx, 28, 100, 32, 'Start'),
        _vlink(cx, 44, 68),
        _process(cx, 92, 200, 36, '', lines=['Set M, N']),
        _vlink(cx, 110, 140),
        _decision(cx, 180, 150, 68, '', lines=['M = N?']),
    ]
    # Yes → display
    parts.append(_hlink(cx + 75, 180, 340, label='Yes'))
    parts.append(f'<line x1="340" y1="180" x2="340" y2="520" stroke="{NAVY}" stroke-width="1.8"/>')
    parts.append(f'<polygon points="335,520 345,520 340,528" fill="{NAVY}"/>')
    parts.append(_io(340, 560, 140, 36, 'Display M'))
    parts.append(_vlink(340, 578, 620))
    parts.append(_terminal(340, 640, 100, 32, 'Stop'))

    # No → M>N?
    parts.append(_vlink(cx, 214, 260, 'No', 'left'))
    parts.append(_decision(cx, 300, 150, 68, '', lines=['M > N?']))
    parts.append(_hlink(cx - 75, 300, 70, label='Yes'))
    parts.append(f'<line x1="70" y1="300" x2="70" y2="360" stroke="{NAVY}" stroke-width="1.8"/>')
    parts.append(f'<polygon points="65,360 75,360 70,368" fill="{NAVY}"/>')
    parts.append(_process(70, 400, 120, 40, '', lines=['M ← M − N']))
    # loop back
    parts.append(f'<path d="M70,420 V450 H{cx} V214" fill="none" stroke="{NAVY}" stroke-width="1.8" stroke-dasharray="5 3"/>')
    parts.append(f'<text x="110" y="445" font-size="11" font-family="Georgia,serif" fill="{MUT}" font-weight="700">loop</text>')

    parts.append(_vlink(cx, 334, 390, 'No', 'right'))
    parts.append(_process(cx, 430, 140, 40, '', lines=['N ← N − M']))
    parts.append(f'<path d="M{cx+70},430 H{cx+110} V214 H{cx+75}" fill="none" stroke="{NAVY}" stroke-width="1.8" stroke-dasharray="5 3"/>')

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 680" width="{W}" height="680" role="img" aria-label="Euclidean algorithm flowchart">
{''.join(parts)}
</svg>'''
    return flow_wrap(svg, 'Flowchart — Exercise 3.2 Euclidean algorithm (GCD by subtraction)')


def flowchart_larger_of_two():
    W, cx = 420, 210
    parts = [
        _terminal(cx, 28, 100, 32, 'Start'),
        _vlink(cx, 44, 68),
        _io(cx, 90, 180, 36, 'Input A, B'),
        _vlink(cx, 108, 140),
        _decision(cx, 180, 140, 64, '', lines=['A = B?']),
        _hlink(cx + 70, 180, 350, label='Yes'),
        f'<line x1="350" y1="180" x2="350" y2="240" stroke="{NAVY}" stroke-width="1.8"/>',
        f'<polygon points="345,240 355,240 350,248" fill="{NAVY}"/>',
        _process(350, 280, 140, 40, '', lines=['“A equals B”']),
        _vlink(cx, 212, 260, 'No', 'left'),
        _decision(cx, 300, 140, 64, '', lines=['A > B?']),
        _hlink(cx - 70, 300, 70, label='Yes'),
        f'<line x1="70" y1="300" x2="70" y2="360" stroke="{NAVY}" stroke-width="1.8"/>',
        f'<polygon points="65,360 75,360 70,368" fill="{NAVY}"/>',
        _process(70, 400, 120, 40, '', lines=['Display A']),
        _vlink(cx, 332, 390, 'No', 'right'),
        _process(cx, 430, 140, 40, '', lines=['Display B']),
        # merge
        f'<line x1="70" y1="420" x2="70" y2="500" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        f'<line x1="{cx}" y1="450" x2="{cx}" y2="500" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        f'<line x1="350" y1="300" x2="350" y2="500" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        f'<line x1="70" y1="500" x2="350" y2="500" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        _vlink(cx, 500, 540),
        _terminal(cx, 560, 100, 32, 'Stop'),
    ]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 600" width="{W}" height="600" role="img">
{''.join(str(p) for p in parts)}
</svg>'''
    return flow_wrap(svg, 'Flowchart — Exercise 3.4 larger of two numbers')


def flowchart_simultaneous():
    W, cx = 520, 260
    parts = [
        _terminal(cx, 28, 100, 32, 'Start'),
        _vlink(cx, 44, 70),
        _io(cx, 95, 280, 40, 'Input a,b,c,d,e,f'),
        _vlink(cx, 115, 145),
        _process(cx, 175, 260, 40, '', lines=['Δ = ae − bd']),
        _vlink(cx, 195, 230),
        _decision(cx, 270, 150, 68, '', lines=['Δ = 0?']),
        _hlink(cx + 75, 270, 430, label='No'),
        f'<line x1="430" y1="270" x2="430" y2="330" stroke="{NAVY}" stroke-width="1.8"/>',
        f'<polygon points="425,330 435,330 430,338" fill="{NAVY}"/>',
        _process(430, 380, 170, 56, '', lines=['Unique intersection', 'x=(ce−bf)/Δ', 'y=(af−cd)/Δ']),
        _vlink(430, 408, 560),
        _vlink(cx, 304, 360, 'Yes', 'left'),
        _decision(cx, 410, 180, 80, '', lines=['Same line?', 'ratios match']),
        _hlink(cx - 90, 410, 90, label='Yes'),
        f'<line x1="90" y1="410" x2="90" y2="480" stroke="{NAVY}" stroke-width="1.8"/>',
        f'<polygon points="85,480 95,480 90,488" fill="{NAVY}"/>',
        _process(90, 520, 150, 44, '', lines=['Infinite solutions', '(coincident)']),
        _vlink(cx, 450, 500, 'No', 'right'),
        _process(cx, 540, 160, 44, '', lines=['No solution', '(parallel)']),
        f'<line x1="90" y1="542" x2="90" y2="600" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        f'<line x1="{cx}" y1="562" x2="{cx}" y2="600" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        f'<line x1="430" y1="560" x2="430" y2="600" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        f'<line x1="90" y1="600" x2="430" y2="600" stroke="{NAVY}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        _vlink(cx, 600, 640),
        _terminal(cx, 660, 100, 32, 'Stop'),
    ]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 700" width="{W}" height="700" role="img">
{''.join(parts)}
</svg>'''
    return flow_wrap(svg, 'Flowchart — Exercise 3.6 two simultaneous linear equations')



# ───────────────────── Practical pages ─────────────────────

def build_p03():
    qs = []
    qs.append(q(1, 'Using the Editor and running a script',
        r'''<p>Open MATLAB and create a <strong>New Script</strong>. Type a short script that (i) builds a small matrix,
(ii) computes its inverse, and (iii) checks \(A A^{-1}\approx I\) within machine epsilon (as in the textbook walkthrough).</p>
<pre>% ExA1_1 style check
A = [1 2 3; 0 1 4; 5 6 0];
AI = inv(A);
IPredicted = A*AI;
IM = eye(3);
difference = IPredicted - IM;</pre>''',
        book_ref='Book §1.2.1 · pp. 14–16',
        do='Save as an <code>.m</code> file, Run from the Editor, and confirm variables appear in the Workspace.'))

    qs.append(q(2, 'Structure plan — Fahrenheit to Celsius',
        r'''<p>Read the structure-plan idea in the book, then write a <strong>multi-level structure plan</strong> for converting Fahrenheit to Celsius,
labelling the stages <strong>Input / Operations / Output</strong>.</p>
<div class="plan">Level 1
1. Initialize Fahrenheit temperature
2. Calculate and display Celsius temperature
3. Stop

Level 2
1. Initialize Fahrenheit temperature F
2. C = (F − 32) × 5/9
3. Display C
4. Stop</div>''',
        book_ref='Book §2.3.8 Structure plan',
        do=r'Translate your plan into a commented MATLAB script and run it for \(F=32\) and \(F=212\).',
        answer=flowchart_fahrenheit() + r'''<p>Check: \(F=32\Rightarrow C=0\); \(F=212\Rightarrow C=100\).</p>'''))

    qs.append(q(3, 'Vertical motion under gravity',
        r'''<p>A stone is thrown vertically upward. Follow the book’s structure plan and produce a script that plots
displacement \(s\) against time \(t\).</p>
<p>Use \(g=9.81\,\mathrm{m/s^2}\), \(u=60\,\mathrm{m/s}\), and \(t=0:0.01:12.3\), with
\[s = ut - \tfrac12 g t^2.\]</p>
<pre>g = 9.81; u = 60;
t = 0:0.01:12.3;
s = u*t - g/2*t.^2;
plot(t,s,'k','LineWidth',3), grid
title('Vertical motion under gravity')
xlabel('time'), ylabel('vertical displacement')</pre>''',
        book_ref='Book §2.4 Vertical motion under gravity',
        do=r'Draw the flowchart for the structure plan, then generate the program from it with plenty of comments. Save as <code>throw.m</code>.',
        answer=flowchart_vertical_motion()))

    qs.append(q(4, 'Program design process &amp; the projectile problem',
        r'''<p>Read the <strong>7 steps</strong> of the program design process. Work through the projectile example to the end of Steps 6 &amp; 7.</p>
<ol>
<li>Problem statement</li><li>Analysis</li><li>Design (structure plan)</li>
<li>Implementation</li><li>Testing / evaluation</li><li>Documentation</li><li>Maintenance</li>
</ol>
<p>Write 3–5 sentences: how would you <em>test</em> (Step 6) that a projectile script is correct?</p>''',
        book_ref='Book §3.1 · §3.1.1 Projectile problem',
        do=r'List at least three concrete test cases (e.g. \(v_0=0\), \(45^\circ\) max-range check, landing when \(y=0\)).',
        answer=r'''<ul>
<li>\(v_0=0\): trajectory stays at the launch point (range \(=0\)).</li>
<li>\(\theta=45^\circ\) on flat ground: range should be \(v_0^2/g\) (maximum).</li>
<li>\(\theta=90^\circ\): range \(=0\); time of flight \(=2v_0/g\).</li>
<li>Landing: solve \(y(t)=0\) for \(t&gt;0\) and compare with the plotted landing time.</li>
</ul>'''))

    qs.append(q(5, 'Quadratic equation — structure plan &amp; flowchart',
        r'''<p>Study the quadratic structure plan (Book pp. 94–95). Draw a flowchart that shows every <strong>decision box</strong>
needed to handle all cases of \(ax^2+bx+c=0\).</p>
<div class="plan">QUADRATIC EQUATION STRUCTURE PLAN
1. Start
2. Input a, b, c
3. If a = 0 then
      If b = 0 then
         If c = 0 → "Solution indeterminate"
         else → "There is no solution"
      else → x = −c/b  (linear)
   else if b² &lt; 4ac → "Complex roots"
   else if b² = 4ac → equal root x = −b/(2a)
   else → two real roots via quadratic formula
4. Stop</div>''',
        book_ref='Book §3.1 / §3.2.2 · pp. 94–96',
        do='Keep this flowchart for Practical 4 (you will implement it with <code>if</code>/<code>elseif</code>). Discuss other math problems that need conditionals or loops.',
        answer=flowchart_quadratic()))

    prep = prep_box(
        ideas=[
            r'<strong>Script vs Command Window:</strong> a script (<code>.m</code>) stores a reusable sequence of commands; the Editor lets you edit, comment, and re-run.',
            r'<strong>Structure plan / flowchart:</strong> top-down design in pseudo-code before coding — label Input, Operations, Output.',
            r'<strong>Array arithmetic:</strong> vectors of time values let you evaluate \(s(t)\) for every \(t\) at once (element-wise <code>.^</code>).',
            r'<strong>Program design process:</strong> seven steps from problem statement through testing and documentation.',
            r'<strong>Decision structure:</strong> the quadratic solver needs nested decisions for linear / complex / equal / two-real cases.',
        ],
        matlab=['Editor / New Script', 'Run', '% comments', 'colon operator :', '.^', 'plot', 'title', 'xlabel', 'ylabel', 'grid', 'inv', 'eye'],
        also=[
            'Workspace and Current Folder panes to see variables and saved files',
            'Flowchart symbols: oval = start/stop, parallelogram = I/O, rectangle = process, diamond = decision',
        ],
    )
    body = f'''
<div class="eyebrow">DPEN100 · ENGG100 · Week 3</div>
<span class="tag">PRACTICAL 3</span>
<h1>Using MATLAB for engineering analysis</h1>
<p class="sub">Work through parts of Chapters 1–3 of {BOOK}. Each card is a concrete task pulled from the practical worksheet and the cited book section. Where a flowchart is required, open <strong>Model answer / flowchart</strong>.</p>
{nav('p03.html')}
<p><a class="chip pdf" href="pdfs/engg100-practical-3-using-matlab-for-engineering-analysis.pdf" target="_blank" rel="noopener">Original Practical 3 PDF</a></p>
{prep}
{''.join(qs)}
'''
    (OUT / 'p03.html').write_text(page('DPEN100 Practical 3', body))


def build_p04():
    qs = []
    qs.append(q(1, 'One-line <code>if</code> and relational operators',
        r'''<p>At the Command Window, repeatedly try:</p>
<pre>r = rand
if r &gt; 0.5, disp('greater indeed'), end</pre>
<p>Also evaluate the logical expressions <code>2 &gt; 0</code> and <code>-1 &gt; 0</code>. Recall MATLAB uses \(1\) for true and \(0\) for false.</p>
<p>Relational operators: <code>&lt; &lt;= == ~= &gt; &gt;=</code>.</p>''',
        book_ref='Book §2.8 · §2.8.1',
        do='Note any discrepancy between what you expected and what MATLAB printed.'))

    qs.append(q(2, 'Nested decisions — implement the quadratic flowchart',
        r'''<p>Using your Practical 3 flowchart, implement the quadratic solver with <code>if</code> / <code>elseif</code> / <code>else</code>.
Compare with the book listing on pp. 95–96.</p>
<pre>function x = quadratic(a,b,c)
% a*x^2 + b*x + c = 0
if a==0 &amp;&amp; b==0 &amp;&amp; c==0
    disp('Solution indeterminate')
elseif a==0 &amp;&amp; b==0
    disp('There is no solution')
elseif a==0
    x = -c/b;   % linear
elseif b^2 &lt; 4*a*c
    disp('Complex roots')
    x = [(-b+sqrt(b^2-4*a*c))/(2*a), (-b-sqrt(b^2-4*a*c))/(2*a)];
elseif b^2 == 4*a*c
    x = -b/(2*a);
else
    x = [(-b+sqrt(b^2-4*a*c))/(2*a), (-b-sqrt(b^2-4*a*c))/(2*a)];
end
end</pre>
<p>Test: <code>quadratic(4,2,-2)</code> should give roots \(0.5\) and \(-1\).</p>''',
        book_ref='Book §2.8.2–2.8.7 · pp. 95–96',
        do='Save as <code>quadratic.m</code> and test indeterminate / linear / complex / equal / two-real cases.',
        answer='<p>Same decision structure as Practical 3 Q5 — use this flowchart while coding:</p>' + flowchart_quadratic()))

    qs.append(q(3, 'Rewrite with <code>switch</code>',
        r'''<p>Read §2.8.9. Sketch how you could classify the quadratic outcome with a <code>switch</code> on a status code
(e.g. flag \(0,1,2,99\) as in Exercise 7.7 later).</p>
<pre>d = floor(3*rand)+1;
switch d
  case 1, disp("That's a 1!")
  case 2, disp("That's a 2!")
  otherwise, disp('Must be 3!')
end</pre>''',
        book_ref='Book §2.8.9 The switch statement',
        do='Optional stretch: re-write your quadratic classifier using <code>switch</code> outside class time.'))

    qs.append(q(4, 'Repeating with <code>for</code> — pick one algorithm',
        r'''<p>Read §§2.7–2.7.5. Choose <strong>one</strong> of: Newton’s method for square roots, factorial, or limit of a sequence,
and implement it with a <code>for</code> loop.</p>
<p>Then pick <strong>one</strong> series from the end of §2.7 (book p. 63) and compute it with a loop <em>and</em> by vectorisation:</p>
<ul>
<li>\(\sum_{k=1}^{1000} k^2\) &nbsp;(answer \(333\,833\,500\))</li>
<li>\(1-\frac13+\frac15-\frac17+\cdots-\frac1{1003}\) &nbsp;(≈ \(0.7849\to\pi/4\))</li>
<li>\(\displaystyle\sum \frac{1}{(2k-1)^2(2k+1)^2}=\frac{\pi^2-8}{16}\) &nbsp;(≈ \(0.1169\) with 500 terms)</li>
</ul>''',
        book_ref='Book §2.7 · series on p. 63',
        do='Time both the loop and vectorised versions with <code>tic</code>/<code>toc</code>.'))

    qs.append(q(5, 'Exercise 2.19 — Basel sum script',
        r'''<p>Work out <strong>by hand</strong> the output of this script for \(n=4\). Then run it for larger \(n\).</p>
<pre>n = input('Number of terms? ');
s = 0;
for k = 1:n
  s = s + 1/(k^2);
end
disp(sqrt(6*s))</pre>
<p>As \(n\to\infty\), \(\sqrt{6\sum 1/k^2}\to\pi\). Rewrite using vectors / array operations.</p>''',
        book_ref='Book Exercise 2.19 · p. 78',
        do=r'Hand-trace for \(n=4\), then vectorise: <code>s=sum(1./(1:n).^2); disp(sqrt(6*s))</code>.'))

    qs.append(q(6, 'Exercise 2.20 — nested loop hand-trace',
        r'''<p>Work through by hand. Draw a table of \(i\), \(j\), and \(m\) as the script runs. Check by executing it.</p>
<pre>v = [3 1 5];
i = 1;
for j = v
  i = i + 1;
  if i == 3
    i = i + 2;
    m = i + j;
  end
end</pre>''',
        book_ref='Book Exercise 2.20 · p. 78',
        do=r'Submit your hand-trace table and the final values of \(i\), \(j\), \(m\).'))

    prep = prep_box(
        ideas=[
            r'<strong>Relational &amp; logical operators:</strong> compare values (<code>== ~= &lt; &gt;</code>) and combine conditions (<code>&amp;&amp; || ~</code>). True → \(1\), false → \(0\).',
            r'<strong>Branching:</strong> <code>if</code> / <code>elseif</code> / <code>else</code> / <code>end</code> implements decision diamonds; <code>switch</code>/<code>case</code> for discrete labels.',
            r'<strong>Repetition:</strong> a <code>for</code> loop runs a known number of times; useful for sums, Newton iterations, and series.',
            r'<strong>Vectorisation:</strong> replace many loops with array ops (<code>sum</code>, <code>1./(1:n)</code>) — usually faster.',
            r'<strong>Hand-tracing:</strong> before trusting code, step through variable values on paper (Exercises 2.19–2.20).',
        ],
        matlab=['if', 'elseif', 'else', 'end', 'switch', 'case', 'otherwise', 'for', 'rand', 'floor', 'disp', 'input', 'sqrt', 'sum', 'tic', 'toc', './', '.^'],
        also=[
            'Function M-file layout for <code>quadratic.m</code> (inputs in header, locals not cluttering Workspace)',
            'Nesting: an <code>else</code> belongs to the nearest unmatched <code>if</code> — place <code>end</code> carefully',
        ],
    )
    body = f'''
<div class="eyebrow">DPEN100 · ENGG100 · Week 4</div>
<span class="tag">PRACTICAL 4</span>
<h1>MATLAB programming with decision structures</h1>
<p class="sub">Finish Chapter 2 decisions &amp; loops from {BOOK}, then implement last week’s quadratic flowchart.</p>
{nav('p04.html')}
<p><a class="chip pdf" href="pdfs/engg100-practical-4-matlab-programming-with-decision-structures.pdf" target="_blank" rel="noopener">Original Practical 4 PDF</a></p>
{prep}
{''.join(qs)}
'''
    (OUT / 'p04.html').write_text(page('DPEN100 Practical 4', body))


def build_p05():
    qs = []
    qs.append(q(1, 'Inline objects &amp; <code>y = f(x)</code>',
        r'''<p>Work §§3.2.1–3.2.2. Create a simple function M-file:</p>
<pre>function y = f(x)
y = x.^3 - 0.95*x;
end</pre>
<p>Check <code>f(2)</code> → \(6.1\). Revisit last week’s quadratic function and test several inputs.</p>''',
        book_ref='Book §3.2.1 · §3.2.2',
        do='Show your tutor the Command Window output for several test inputs.'))

    qs.append(q(2, 'Exercise 3.2 — Euclidean algorithm structure plan',
        r'''<p>Consider the structure plan ( \(M,N\) MATLAB variables ):</p>
<div class="plan">1. Set M = 44 and N = 28
2. While M ≠ N repeat:
      While M &gt; N: replace M by M − N
      While N &gt; M: replace N by N − M
3. Display M
4. Stop</div>
<ol type="a">
<li>Work through, tabulating \(M\) and \(N\). Give the output.</li>
<li>Repeat for \(M=14\), \(N=24\).</li>
<li>What general arithmetic procedure is this?</li>
</ol>''',
        book_ref='Book Exercise 3.2 · p. 97',
        do='Then implement as a MATLAB function and verify against your hand-trace.',
        answer=flowchart_euclidean() + r'''
<p><strong>(a)</strong> \(M=44,N=28\to 16,28\to 16,12\to 4,12\to 4,8\to 4,4\). Output \(M=4\).</p>
<p><strong>(b)</strong> \(M=14,N=24\to 14,10\to 4,10\to 4,6\to 4,2\to 2,2\). Output \(M=2\).</p>
<p><strong>(c)</strong> Greatest common divisor (Euclidean algorithm by repeated subtraction).</p>'''))

    qs.append(q(3, 'Exercise 3.4 — larger of two numbers',
        r'''<p>Write a script that inputs any two numbers (which may be equal) and displays the larger one with a suitable message,
or reports that they are equal.</p>''',
        book_ref='Book Exercise 3.4 · p. 97',
        do='Structure-plan first, then code. Test equal and unequal cases.',
        answer=flowchart_larger_of_two()))

    qs.append(q(4, 'Exercise 3.6 — two simultaneous linear equations',
        r'''<p>Develop a structure plan for
\[ax+by=c,\qquad dx+ey=f\]
that handles intersecting, parallel, and coincident lines. Implement and test on
\[x+y=3,\qquad 2x-y=3\]
(solution \(x=2\), \(y=1\)).</p>''',
        book_ref='Book Exercise 3.6 · pp. 97–98',
        do=r'Input all six coefficients; branch on the determinant \(ae-bd\).',
        answer=flowchart_simultaneous() + r'''
<p>Test: \(a=1,b=1,c=3,d=2,e=-1,f=3\Rightarrow\Delta=-3\neq0\Rightarrow x=2,\,y=1\).</p>'''))

    qs.append(q(5, 'Chapter 7 — function M-files &amp; <code>stats.m</code>',
        r'''<p>Read Ch. 7 intro and §7.1 (no need to code Newton’s method yet). Create <code>stats.m</code> from §7.2 and run the book’s tests.
Read §§7.3–7.5 (handles, command/function duality, name resolution). Skip §§7.2.1–7.2.4.</p>''',
        book_ref='Book Ch. 7 · §§7.1–7.5',
        do='Confirm multiple M-files can call each other from the Current Folder.'))

    qs.append(q(6, 'Exercise 7.3 — <code>double(x)</code>',
        r'''<p>Write and test a function <code>double(x)</code> that doubles its input argument, so
<code>x = double(x)</code> doubles the value in <code>x</code>.</p>
<p><em>Note:</em> MATLAB already has a built-in <code>double</code> type-cast — use a different file name such as
<code>mydouble.m</code> if the built-in shadows yours, or clear the path carefully as the book intends.</p>''',
        book_ref='Book Exercise 7.3 · p. 179',
        do='Structure plan → function M-file → test with scalars and arrays.'))

    qs.append(q(7, 'Exercise 7.4 — <code>swop(x,y)</code>',
        r'''<p>Write and test a function that exchanges the values of its two input arguments.
(In modern MATLAB you typically return both outputs: <code>[a,b] = swop(a,b)</code>.)</p>''',
        book_ref='Book Exercise 7.4 · p. 179',
        do='Discuss with peers whether pass-by-value requires returning both outputs.'))

    qs.append(q(8, 'Exercise 7.7 — robust quadratic function',
        r'''<p>Write
<code>function [x1,x2,flag] = quad(a,b,c)</code>
using the structure plan in Fig. 3.3 / §3.2.2. The flag must return:</p>
<ul>
<li>\(0\): no solution (\(a=b=0\), \(c\neq0\))</li>
<li>\(1\): one real root (\(a=0\), \(b\neq0\) → \(x=-c/b\))</li>
<li>\(2\): two real or complex roots</li>
<li>\(99\): any \(x\) is a solution (\(a=b=c=0\))</li>
</ul>
<p>Test on Exercise 3.5 data: \((1,1,1)\), \((2,4,2)\), \((2,2,-12)\).</p>''',
        book_ref='Book Exercise 7.7 · pp. 179–180',
        do='Show your tutor flag outputs for each test case.',
        answer='<p>Implement using the same decision tree as Practical 3:</p>' + flowchart_quadratic()))

    prep = prep_box(
        ideas=[
            r'<strong>Functions vs scripts:</strong> a function M-file has a header <code>function [outs] = name(ins)</code>; variables inside stay local to the Workspace.',
            r'<strong>Reusable algorithms:</strong> GCD by subtraction, max-of-two, simultaneous lines, and robust quadratics all start from a structure plan / flowchart.',
            r'<strong>Multiple outputs &amp; flags:</strong> return status codes (e.g. Exercise 7.7) so the caller knows which case occurred.',
            r'<strong>Function handles &amp; name resolution:</strong> Chapter 7 ideas — how MATLAB finds <code>f.m</code>, and how handles pass functions as data.',
            r'<strong>Testing:</strong> exercise every branch (equal numbers, parallel lines, \(a=b=c=0\), complex roots).',
        ],
        matlab=['function', 'end', 'inline (legacy)', 'function handles', 'feval', 'while', 'if / elseif', 'disp', 'NaN', 'sqrt'],
        also=[
            'Save each function as <code>name.m</code> matching the function name; keep them on the path / Current Folder',
            'Avoid shadowing built-ins (e.g. name your doubler <code>mydouble.m</code> if needed)',
        ],
    )
    body = f'''
<div class="eyebrow">DPEN100 · ENGG100 · Week 5</div>
<span class="tag">PRACTICAL 5</span>
<h1>MATLAB functions &amp; chapter exercises</h1>
<p class="sub">Chapters 3 and 7 of {BOOK}: inline/function M-files, then Exercises 3.2, 3.4, 3.6 and 7.3, 7.4, 7.7. Flowcharts are in the model answers where a structure plan / flowchart is required.</p>
{nav('p05.html')}
<p><a class="chip pdf" href="pdfs/engg100-practical-5-matlab-functions-and-chapter-exercises-guide.pdf" target="_blank" rel="noopener">Original Practical 5 PDF</a></p>
{prep}
{''.join(qs)}
'''
    (OUT / 'p05.html').write_text(page('DPEN100 Practical 5', body))


def build_lab06():
    qs = []
    qs.append(q(1, 'While-loop kinematics arrays',
        r'''<p>A car starts at rest and follows:</p>
<ul>
<li>Constant acceleration \(2\,\mathrm{m/s^2}\) until \(v=40\,\mathrm{m/s}\)</li>
<li>Then constant velocity until \(s=800\,\mathrm{m}\)</li>
<li>Then constant deceleration \(-4\,\mathrm{m/s^2}\) until rest</li>
</ul>
<img class="fig" src="figs/lab6-v-t.png" alt="Piecewise velocity schedule" style="max-width:520px">
<p>Use <code>while</code> loops with \(\Delta t=0.1\,\mathrm{s}\) to build arrays of displacement, velocity, acceleration and time.
Then <code>plot</code> \(s(t)\), \(v(t)\) and \(a(t)\).</p>''',
        do='Use subplot or three separate figures. Label axes and add a legend.'))

    qs.append(q(2, 'Function <code>trapArea</code>',
        r'''<p>Write <code>trapArea(x1,y1,x2,y2)</code> returning the trapezium area between \((x_1,y_1)\) and \((x_2,y_2)\):</p>
\[\mathrm{area}=\tfrac12(y_1+y_2)(x_2-x_1).\]
<img class="fig" src="figs/lab6-trap.png" alt="Trapezium under a chord" style="max-width:280px">''',
        do='Four inputs, one output. Test on a known rectangle and a right triangle.'))

    qs.append(q(3, 'Function <code>areaUnderCurve</code>',
        r'''<p>Write <code>areaUnderCurve(x,y)</code> that calls <code>trapArea</code> in a loop over consecutive points of 1-D arrays \(x\) and \(y\).</p>
<img class="fig" src="figs/lab6-area.png" alt="Composite trapezoidal rule" style="max-width:320px">
<p>Verify on:</p>
<ul>
<li>\(\displaystyle\int_0^3 x^2\,\mathrm{d}x = 9\)</li>
<li>\(\displaystyle\int_{-\pi/2}^{\pi/2}\cos x\,\mathrm{d}x = 2\)</li>
</ul>
<p>Sample the integrands with a fine spacing (e.g. \(0.01\)) so the trapezoidal sum is close to the exact value.</p>''',
        do='Print both numerical estimates and the absolute error vs the exact answers.'))

    prep = prep_box(
        ideas=[
            r'<strong>Piecewise kinematics:</strong> different \(a\) (or \(v\)) rules in successive phases — switch when a threshold is hit (\(v=40\), \(s=800\), \(v=0\)).',
            r'<strong>Discrete time stepping:</strong> with \(\Delta t=0.1\,\mathrm{s}\), update \(v\leftarrow v+a\Delta t\), \(s\leftarrow s+v\Delta t\) (or a consistent integrator) inside <code>while</code> loops.',
            r'<strong>Growing arrays:</strong> append samples each step (or preallocate if you know a bound) so you can plot afterwards.',
            r'<strong>Trapezoidal rule:</strong> area of one strip \(\tfrac12(y_1+y_2)(x_2-x_1)\); sum strips for \(\int y\,\mathrm{d}x\).',
            r'<strong>Function composition:</strong> <code>areaUnderCurve</code> should call <code>trapArea</code> in a loop — modular code.',
        ],
        matlab=['while', 'end', 'function', 'plot', 'subplot', 'xlabel', 'ylabel', 'legend', 'title', 'grid', 'length', 'for', 'linspace', 'pi', 'cos'],
        also=[
            'Test <code>trapArea</code> on a rectangle and a triangle before wiring the composite rule',
            r'Verify \(\int_0^3 x^2\,\mathrm{d}x=9\) and \(\int_{-\pi/2}^{\pi/2}\cos x\,\mathrm{d}x=2\) with a fine sample spacing',
        ],
    )
    body = f'''
<div class="eyebrow">DPEN100 · ENGG100 · Week 7</div>
<span class="tag">COMPUTER LAB 6</span>
<h1>Arrays, while loops &amp; numerical area</h1>
<p class="sub">Lab worksheet (not a Hahn chapter drill): build kinematic arrays with <code>while</code>, then trapezoidal integration via functions.</p>
{nav('lab06.html')}
<p><a class="chip pdf" href="pdfs/engg100-lab-6-arrays-functions-in-engineering-computing.pdf" target="_blank" rel="noopener">Original Lab 6 PDF</a></p>
{prep}
{''.join(qs)}
'''
    (OUT / 'lab06.html').write_text(page('DPEN100 Lab 6', body))


def build_p08():
    qs = []
    qs.append(q(1, 'Position polynomial — position &amp; path length',
        r'''<p>A particle travels along a straight line with
\[s=1.2t^3-16.2t^2+50.4t\quad(\mathrm{m}),\quad t\text{ in seconds.}\]
Determine</p>
<ol type="a"><li>the position when \(t=10\,\mathrm{s}\)</li>
<li>the total distance travelled during the \(10\,\mathrm{s}\) interval</li></ol>''',
        star=True,
        hint=r'Draw the path: find times when \(v=0\) to split the journey into segments.',
        do=r'Differentiate for \(v(t)\); integrate absolute velocity or sum \(|\Delta s|\) on each segment.'))

    qs.append(q(2, r'Cubic motion — zero velocity &amp; state at \(t=5\)',
        r'''<p>Motion defined by \(x=t^3-6t^2+9t+5\) (m, s). Determine</p>
<ol type="a"><li>when the velocity is zero</li>
<li>position, acceleration and total distance travelled when \(t=5\,\mathrm{s}\)</li></ol>'''))

    qs.append(q(3, 'Speedboat — velocity, acceleration, maximum speed',
        r'''<p>For \(2\le t\le 10\), \(s=4t+1.6t^2-0.08t^3\) m. Determine</p>
<ol type="a"><li>velocity and acceleration at \(t=4\,\mathrm{s}\)</li>
<li>maximum velocity in the interval and when it occurs</li></ol>''',
        star=True))

    qs.append(q(4, r'Car — shortest time for \(1200\,\mathrm{m}\) with \(v_{\max}=60\)',
        r'''<p>A car can accelerate / decelerate at \(5\,\mathrm{m/s^2}\), starts from rest, max speed \(60\,\mathrm{m/s}\),
and must stop after travelling \(1200\,\mathrm{m}\). Find the shortest time.</p>''',
        hint=r'Draw a \(v\)–\(t\) graph (accelerate → cruise → brake).'))

    qs.append(q(5, r'Cyclist — constant acceleration to \(30\,\mathrm{km/h}\)',
        r'''<p>From rest, after \(20\,\mathrm{m}\) the speed is \(30\,\mathrm{km/h}\). Find</p>
<ol type="a"><li>acceleration (assume constant)</li>
<li>time to reach \(30\,\mathrm{km/h}\)</li></ol>'''))

    qs.append(q(6, r'Ball thrown upward from a \(10\,\mathrm{m}\) tower',
        r'''<p>Released \(10\,\mathrm{m}\) above ground; falls past the thrower \(0.8\,\mathrm{s}\) later. Determine</p>
<ol type="a"><li>throw speed</li>
<li>time of flight</li>
<li>impact speed on the ground</li></ol>''',
        star=True,
        hint=r'Take upward positive; when it passes the thrower again, \(s=0\) relative to release.'))

    qs.append(q(7, r'Erratic motion from a \(v\)–\(t\) graph',
        r'''<p>Particle starts from rest at \(x=-3\,\mathrm{m}\) with the velocity history below.</p>
<img class="fig" src="figs/p8-v-t.png" alt="Velocity-time history" style="max-width:480px">
<ol type="a">
<li>Plot \(a\)–\(t\) for \(0\le t\le 4\,\mathrm{s}\)</li>
<li>Plot \(x\)–\(t\) for \(0\le t\le 4\,\mathrm{s}\)</li>
<li>Find time \(t\) when the particle crosses the origin</li>
</ol>''',
        star=True))

    qs.append(q(8, 'Subway train — braking interval &amp; station spacing',
        r'''<p>Acceleration schedule:</p>
<img class="fig" src="figs/p8-a-t.png" alt="Acceleration schedule" style="max-width:480px">
<ol type="a">
<li>Find \(\Delta t\) while braking at \(-2\,\mathrm{m/s^2}\) to a stop</li>
<li>Find the distance between stations</li>
</ol>'''))

    # worked answers (numeric) for key star questions — concise but complete
    answers = r'''
<h2>Worked answers (selected)</h2>
<details open><summary>Show / hide numeric solutions</summary>
<div class="ans"><strong>Q1.</strong> \(v=\dot s=3.6t^2-32.4t+50.4\). At rest when \(t=2\,\mathrm{s}\) and \(t=7\,\mathrm{s}\).
\[s(10)=1.2(1000)-16.2(100)+50.4(10)=84\,\mathrm{m}.\]
Positions: \(s(0)=0\), \(s(2)=45.6\), \(s(7)=-29.4\), \(s(10)=84\).
Total distance \(=45.6+75.0+113.4=234\,\mathrm{m}\).
\[\boxed{s(10)=84\,\mathrm{m};\ \text{distance}=234\,\mathrm{m}}\]</div>

<div class="ans"><strong>Q2.</strong> \(v=3t^2-12t+9=3(t-1)(t-3)\). Zero at \(t=1,3\,\mathrm{s}\).
At \(t=5\): \(x=25\,\mathrm{m}\), \(a=6t-12=18\,\mathrm{m/s^2}\). Path: \(x(0)=5\to x(1)=9\to x(3)=5\to x(5)=25\).
Distance \(=4+4+20=28\,\mathrm{m}\).
\[\boxed{t=1,3\,\mathrm{s};\ x=25\,\mathrm{m},\ a=18\,\mathrm{m/s^2},\ \text{distance}=28\,\mathrm{m}}\]</div>

<div class="ans"><strong>Q3.</strong> \(v=4+3.2t-0.24t^2\), \(a=3.2-0.48t\).
At \(t=4\): \(v=12.96\,\mathrm{m/s}\), \(a=1.28\,\mathrm{m/s^2}\).
Max \(v\) when \(a=0\Rightarrow t=\frac{20}{3}\approx6.67\,\mathrm{s}\) (in range);
\(v_{\max}=\frac{44}{3}\approx14.67\,\mathrm{m/s}\).
\[\boxed{v(4)=12.96\,\mathrm{m/s},\ a(4)=1.28\,\mathrm{m/s^2};\ v_{\max}\approx14.67\,\mathrm{m/s}\ \text{at}\ t\approx6.67\,\mathrm{s}}\]</div>

<div class="ans"><strong>Q4.</strong> Accel distance to \(60\,\mathrm{m/s}\): \(s_a=\frac{v^2}{2a}=360\,\mathrm{m}\) (same for brake).
Cruise \(s_c=1200-720=480\,\mathrm{m}\). Times: \(t_a=t_b=\frac{60}{5}=12\,\mathrm{s}\), \(t_c=\frac{480}{60}=8\,\mathrm{s}\).
\[\boxed{t=32\,\mathrm{s}}\]</div>

<div class="ans"><strong>Q5.</strong> \(30\,\mathrm{km/h}=8.333\,\mathrm{m/s}\). \(v^2=2as\Rightarrow a=\frac{v^2}{2s}=\frac{69.44}{40}=1.736\,\mathrm{m/s^2}\).
\(t=v/a=4.80\,\mathrm{s}\).
\[\boxed{a\approx1.74\,\mathrm{m/s^2},\ t\approx4.80\,\mathrm{s}}\]</div>

<div class="ans"><strong>Q6.</strong> Up positive, release at \(s=0\). Passes thrower at \(t=0.8\,\mathrm{s}\): \(0=u(0.8)-\tfrac12 g(0.8)^2\Rightarrow u=3.924\,\mathrm{m/s}\).
Flight to ground \(s=-10\): \(-10=ut-\tfrac12 gt^2\Rightarrow t\approx1.88\,\mathrm{s}\) (positive root).
Impact \(v=u-gt\approx-14.5\,\mathrm{m/s}\) (speed \(14.5\,\mathrm{m/s}\) down).
\[\boxed{u\approx3.92\,\mathrm{m/s};\ t_{\mathrm{flight}}\approx1.88\,\mathrm{s};\ |v_{\mathrm{impact}}|\approx14.5\,\mathrm{m/s}}\]</div>

<div class="ans"><strong>Q7.</strong> From the graph: \(a=4\) on \([0,1]\), \(a=0\) on \([1,2]\), \(a=-\frac83\) on \([2,4]\).
Displacement from areas under \(v\)–\(t\) starting at \(x(0)=-3\). Origin crossing: solve cumulative area \(=3\).
(Construct \(a\)–\(t\) and \(x\)–\(t\) carefully from the piecewise slopes/areas.)</div>

<div class="ans"><strong>Q8.</strong> Build \(v\) from integrating \(a\): after \(10\,\mathrm{s}\) at \(1\,\mathrm{m/s^2}\), \(v=10\); after next \(6\,\mathrm{s}\) at \(2\,\mathrm{m/s^2}\), \(v=22\);
\(12\,\mathrm{s}\) coast keeps \(v=22\). Brake at \(-2\,\mathrm{m/s^2}\): \(\Delta t=\frac{22}{2}=11\,\mathrm{s}\).
Distance = area under \(v\)–\(t\) (or integrate piecewise).
\[\boxed{\Delta t=11\,\mathrm{s};\ \text{station spacing}=531\,\mathrm{m}}\]
(Breakdown: \(s=50+96+264+121\).)</div>
</details>
'''

    prep = prep_box(
        ideas=[
            r'<strong>Rectilinear kinematics:</strong> \(v=\dot s\), \(a=\dot v=\ddot s\). Position polynomials → differentiate for \(v,a\).',
            r'<strong>Displacement vs distance:</strong> displacement is net change in \(s\); total distance sums \(|\Delta s|\) on each segment between turning points (\(v=0\)).',
            r'<strong>Constant acceleration (SUVAT):</strong> \(v=u+at\), \(s=ut+\tfrac12 at^2\), \(v^2=u^2+2as\) — use with a clear sign convention.',
            r'<strong>Graphical kinematics:</strong> slope of \(v\)–\(t\) is \(a\); area under \(v\)–\(t\) is \(\Delta s\); area under \(a\)–\(t\) is \(\Delta v\).',
            r'<strong>Piecewise / erratic motion:</strong> split the timeline at kinks; integrate each constant-\(a\) (or linear-\(v\)) piece separately.',
        ],
        matlab=['(optional) diff / gradient', 'roots / solve for v=0', 'plot for checking s(t), v(t)', 'syms (symbolic check)'],
        also=[
            'Starred questions are Workshop 8 priority — do those first',
            'Always sketch the path or a \(v\)–\(t\) graph before computing totals',
            'Convert units carefully (e.g. km/h → m/s)',
        ],
    )
    body = f'''
<div class="eyebrow">DPEN100 · ENGG100 · Week 8</div>
<span class="tag">PRACTICAL 8</span>
<h1>Kinematics — rectilinear motion</h1>
<p class="sub">Mechanics worksheet (not from the MATLAB textbook). Starred items are Workshop 8 priority.</p>
{nav('p08.html')}
<p><a class="chip pdf" href="pdfs/engg100-practical-8-kinematics-in-rectilinear-motion-exercises.pdf" target="_blank" rel="noopener">Original Practical 8 PDF</a></p>
{prep}
{''.join(qs)}
{answers}
'''
    (OUT / 'p08.html').write_text(page('DPEN100 Practical 8', body))


def build_hub():
    cards = [
        ('p03.html', 'Practical 3 · Week 3', 'Editor, structure plans, vertical motion, program design, quadratic flowchart',
         'Book Ch. 1–3', 'pdfs/engg100-practical-3-using-matlab-for-engineering-analysis.pdf'),
        ('p04.html', 'Practical 4 · Week 4', 'if / switch decisions, for-loops, series, Exercises 2.19 & 2.20, quadratic code',
         'Book Ch. 2', 'pdfs/engg100-practical-4-matlab-programming-with-decision-structures.pdf'),
        ('p05.html', 'Practical 5 · Week 5', 'Functions, Exercises 3.2 / 3.4 / 3.6 and 7.3 / 7.4 / 7.7',
         'Book Ch. 3 & 7', 'pdfs/engg100-practical-5-matlab-functions-and-chapter-exercises-guide.pdf'),
        ('lab06.html', 'Lab 6 · Week 7', 'while-loop kinematics arrays, trapArea, areaUnderCurve integrals',
         'Lab worksheet', 'pdfs/engg100-lab-6-arrays-functions-in-engineering-computing.pdf'),
        ('p08.html', 'Practical 8 · Week 8', '8 rectilinear kinematics problems (★ workshop set) with worked answers',
         'Mechanics', 'pdfs/engg100-practical-8-kinematics-in-rectilinear-motion-exercises.pdf'),
    ]
    rows = []
    for href, title, desc, tag, pdf in cards:
        rows.append(f'''<div class="card">
<h3><a href="{href}" style="color:var(--navy);text-decoration:none">{title}</a></h3>
<p class="meta">{tag} · tasks converted to HTML questions</p>
<p>{desc}</p>
<div class="chiprow">
  <a class="chip on" href="{href}">Open tasks</a>
  <a class="chip pdf" href="{pdf}" target="_blank" rel="noopener">Original PDF</a>
</div>
</div>''')

    body = f'''
<div class="eyebrow">DPEN100 · ENGG100</div>
<span class="tag">PRACTICALS TO DO</span>
<h1>Practicals &amp; computer labs</h1>
<p class="sub">Tasks extracted from the ENGG100 practical worksheets. MATLAB items cite sections and end-of-chapter exercises from {BOOK}; kinematics / lab items come from the class PDFs. Work these in order after the matching theory guide.</p>
{nav('index.html')}

<div class="todo-box">
<h2>How to use this section</h2>
<ol style="margin-left:20px">
<li>Open the practical card for the week you are on.</li>
<li>Each <strong>Q</strong> is a concrete task — book section references are blue chips.</li>
<li>Keep the original PDF open for any figure the worksheet expects you to hand-draw.</li>
<li>For Practical 8, starred questions are the Workshop 8 minimum; worked numerics are at the bottom.</li>
</ol>
</div>

{''.join(rows)}

<p class="sub" style="margin-top:20px">Textbook access: use your library portal for the official PDF of Hahn &amp; Valentine (7e). This site restates only the assigned exercises / section tasks from the practicals.</p>
'''
    (OUT / 'index.html').write_text(page('DPEN100 Practicals to do', body))


def ensure_pdfs():
    pdf_dir = OUT / 'pdfs'
    pdf_dir.mkdir(parents=True, exist_ok=True)
    names = [
        'engg100-practical-3-using-matlab-for-engineering-analysis.pdf',
        'engg100-practical-4-matlab-programming-with-decision-structures.pdf',
        'engg100-practical-5-matlab-functions-and-chapter-exercises-guide.pdf',
        'engg100-practical-8-kinematics-in-rectilinear-motion-exercises.pdf',
        'engg100-lab-6-arrays-functions-in-engineering-computing.pdf',
    ]
    for n in names:
        src = STUDY / n
        if src.exists():
            shutil.copy2(src, pdf_dir / n)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'figs').mkdir(exist_ok=True)
    ensure_pdfs()
    build_p03()
    build_p04()
    build_p05()
    build_lab06()
    build_p08()
    build_hub()
    print('wrote practicals to', OUT)


if __name__ == '__main__':
    main()
