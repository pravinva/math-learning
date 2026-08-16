#!/usr/bin/env python3
"""Generate DPEN022 Trig short-lesson practice sets from Weeks 1A–2A notes."""
from pathlib import Path
import html as H
import math
from _dpen22_lesson_kit import escape_math_brackets

OUT = Path(__file__).resolve().parent / 'siddharth' / 'dpen22' / 'class-notes' / 'trig' / 'lessons'
OUT.mkdir(parents=True, exist_ok=True)

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
.exam-note{background:#fff7ed;border:2px solid #f0b429;border-radius:8px;padding:12px 14px;margin:14px 0;color:#92400e;font-size:15px;}
.exam-note strong{color:#78350f;}
.tri-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0;}
@media(max-width:700px){.tri-grid{grid-template-columns:1fr;}}
.tri-card{background:#f8fafc;border:1px solid var(--line);border-radius:8px;padding:10px 10px 12px;text-align:center;}
.tri-card h4{font-size:14px;color:var(--navy);margin:0 0 8px;}
.tri-card svg{max-width:100%;height:auto;}
.ratio-table{width:100%;border-collapse:collapse;margin:10px 0 4px;font-size:14px;}
.ratio-table th,.ratio-table td{border:1px solid #c9dff7;padding:7px 8px;text-align:center;}
.ratio-table th{background:#eef6ff;color:var(--navy);}
.problems ol{margin-left:22px;}
.problems li{margin:10px 0;}
.ans{background:#f0fdf4;border-left:4px solid var(--green);padding:8px 12px;margin:8px 0;border-radius:0 6px 6px 0;overflow-x:auto;}
.ans .katex-display{overflow-x:auto;margin:6px 0;}
@media(max-width:640px){.ans .katex{font-size:0.95em;}}
details{margin-top:10px;}
summary{cursor:pointer;font-weight:600;color:var(--navy);}
.tag{display:inline-block;background:var(--orange);color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;margin-bottom:8px;}
.chiprow{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 18px;}
.chip{display:inline-block;padding:7px 11px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:600;border:1px solid #c9dff7;background:#eef6ff;color:var(--blue);}
.chip.on{background:var(--navy);border-color:var(--navy);color:#fff;}
'''

def _rt_triangle_svg(base_units, height_units, base_lab, height_lab, hyp_lab,
                     ang_bottom, ang_top, W=330, H=250):
    """Right triangle with the right angle at bottom-left, drawn to scale.

    Angle arc sweep follows the sign of the cross product because SVG's y-axis
    points down, so a positive cross product is clockwise on screen.
    """
    x0, y0 = 66.0, 196.0
    scale = 176.0 / max(base_units, height_units)
    bx, hy = base_units * scale, height_units * scale
    R, B, T = (x0, y0), (x0 + bx, y0), (x0, y0 - hy)
    NAVY, INK, MUT = '#1B3A5C', '#2c2a28', '#6b6762'

    def arc(centre, v1, v2, r):
        n1 = math.hypot(*v1) or 1.0
        n2 = math.hypot(*v2) or 1.0
        p1 = (centre[0] + r * v1[0] / n1, centre[1] + r * v1[1] / n1)
        p2 = (centre[0] + r * v2[0] / n2, centre[1] + r * v2[1] / n2)
        sweep = 1 if v1[0] * v2[1] - v1[1] * v2[0] > 0 else 0
        return (f'<path d="M{p1[0]:.1f},{p1[1]:.1f} A{r},{r} 0 0,{sweep} '
                f'{p2[0]:.1f},{p2[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="1.6"/>')

    def bisector_label(centre, v1, v2, dist, text):
        n1 = math.hypot(*v1) or 1.0
        n2 = math.hypot(*v2) or 1.0
        ux = v1[0] / n1 + v2[0] / n2
        uy = v1[1] / n1 + v2[1] / n2
        n = math.hypot(ux, uy) or 1.0
        x, y = centre[0] + dist * ux / n, centre[1] + dist * uy / n
        return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="middle" '
                f'dominant-baseline="middle" font-size="13.5" font-family="Georgia,serif" '
                f'fill="{NAVY}" font-weight="bold">{text}</text>')

    vB1, vB2 = (R[0] - B[0], R[1] - B[1]), (T[0] - B[0], T[1] - B[1])
    vT1, vT2 = (R[0] - T[0], R[1] - T[1]), (B[0] - T[0], B[1] - T[1])
    mid = (x0 + bx / 2, y0 - hy / 2)
    dxo, dyo = mid[0] - R[0], mid[1] - R[1]
    no = math.hypot(dxo, dyo) or 1.0

    vy = y0 - hy - 30  # crop dead space above a short apex
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 {vy:.1f} {W} {H - vy:.1f}" width="{W}" height="{H - vy:.0f}" role="img">
<polygon points="{R[0]:.1f},{R[1]:.1f} {B[0]:.1f},{B[1]:.1f} {T[0]:.1f},{T[1]:.1f}"
 fill="#eef6ff" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/>
<path d="M{x0 + 15},{y0} L{x0 + 15},{y0 - 15} L{x0},{y0 - 15}" fill="none" stroke="{NAVY}" stroke-width="1.6"/>
{arc(B, vB1, vB2, 34)}
{arc(T, vT1, vT2, 34)}
{bisector_label(B, vB1, vB2, 56, ang_bottom)}
{bisector_label(T, vT1, vT2, 56, ang_top)}
<text x="{x0 + bx / 2:.1f}" y="{y0 + 26:.1f}" text-anchor="middle" font-size="15" font-family="Georgia,serif" fill="{INK}">{base_lab}</text>
<text x="{x0 - 14:.1f}" y="{y0 - hy / 2:.1f}" text-anchor="end" dominant-baseline="middle" font-size="15" font-family="Georgia,serif" fill="{INK}">{height_lab}</text>
<text x="{mid[0] + 22 * dxo / no:.1f}" y="{mid[1] + 22 * dyo / no:.1f}" text-anchor="middle" dominant-baseline="middle" font-size="15" font-family="Georgia,serif" fill="{INK}">{hyp_lab}</text>
<text x="{x0 + 15:.1f}" y="{y0 - 22:.1f}" font-size="11" font-family="Georgia,serif" fill="{MUT}">90°</text>
</svg>'''


TRI_45 = _rt_triangle_svg(1, 1, '1', '1', '&#8730;2', '45°', '45°')
TRI_30 = _rt_triangle_svg(math.sqrt(3), 1, '&#8730;3', '1', '2', '30°', '60°')

CANONICAL_TRIANGLES = r'''
<div class="exam-note"><strong>Exam note.</strong> The exam expects you to know the exact ratios for
\(30^\circ,45^\circ,60^\circ\) (that is \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\))
straight from these two canonical right triangles — calculators are not accepted for exact-value questions.
Learn to redraw both triangles from memory and read the ratios off them.</div>
<div class="tri-grid">
  <div class="tri-card">
    <h4>Isosceles right triangle &mdash; \(45^\circ\!-\!45^\circ\!-\!90^\circ\) \(\left(\tfrac{\pi}{4},\tfrac{\pi}{4},\tfrac{\pi}{2}\right)\)</h4>
    ''' + TRI_45 + r'''
    <p style="font-size:13px;color:#6b6762;margin-top:6px;">Sides \(1:1:\sqrt2\) &mdash; start from a unit square and cut along the diagonal.</p>
  </div>
  <div class="tri-card">
    <h4>Half-equilateral triangle &mdash; \(30^\circ\!-\!60^\circ\!-\!90^\circ\) \(\left(\tfrac{\pi}{6},\tfrac{\pi}{3},\tfrac{\pi}{2}\right)\)</h4>
    ''' + TRI_30 + r'''
    <p style="font-size:13px;color:#6b6762;margin-top:6px;">Sides \(1:\sqrt3:2\) &mdash; start from an equilateral triangle of side \(2\) and cut it in half.</p>
  </div>
</div>
<table class="ratio-table">
<thead><tr><th>Angle (deg)</th><th>Angle (rad)</th><th>\(\sin\)</th><th>\(\cos\)</th><th>\(\tan\)</th></tr></thead>
<tbody>
<tr><td>\(30^\circ\)</td><td>\(\dfrac{\pi}{6}\)</td><td>\(\dfrac12\)</td><td>\(\dfrac{\sqrt3}{2}\)</td><td>\(\dfrac{1}{\sqrt3}=\dfrac{\sqrt3}{3}\)</td></tr>
<tr><td>\(45^\circ\)</td><td>\(\dfrac{\pi}{4}\)</td><td>\(\dfrac{\sqrt2}{2}\)</td><td>\(\dfrac{\sqrt2}{2}\)</td><td>\(1\)</td></tr>
<tr><td>\(60^\circ\)</td><td>\(\dfrac{\pi}{3}\)</td><td>\(\dfrac{\sqrt3}{2}\)</td><td>\(\dfrac12\)</td><td>\(\sqrt3\)</td></tr>
</tbody>
</table>
<table class="ratio-table">
<thead><tr><th>Angle</th><th>\(\csc\)</th><th>\(\sec\)</th><th>\(\cot\)</th></tr></thead>
<tbody>
<tr><td>\(30^\circ=\dfrac{\pi}{6}\)</td><td>\(2\)</td><td>\(\dfrac{2}{\sqrt3}=\dfrac{2\sqrt3}{3}\)</td><td>\(\sqrt3\)</td></tr>
<tr><td>\(45^\circ=\dfrac{\pi}{4}\)</td><td>\(\sqrt2\)</td><td>\(\sqrt2\)</td><td>\(1\)</td></tr>
<tr><td>\(60^\circ=\dfrac{\pi}{3}\)</td><td>\(\dfrac{2}{\sqrt3}=\dfrac{2\sqrt3}{3}\)</td><td>\(2\)</td><td>\(\dfrac{1}{\sqrt3}=\dfrac{\sqrt3}{3}\)</td></tr>
</tbody>
</table>
'''


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


def set_page(meta, siblings):
    chips = ''.join(
        f'<a class="chip{" on" if s["slug"]==meta["slug"] else ""}" href="{s["slug"]}.html">{s["short"]}</a>'
        for s in siblings
    )
    lesson_html = ''.join(
        p if str(p).lstrip().startswith('<') else f'<p>{p}</p>'
        for p in meta['lesson']
    )
    if meta.get('example'):
        lesson_html += f'<div class="ex"><strong>Worked example.</strong> {meta["example"]}</div>'
    points = ''.join(f'<li>{x}</li>' for x in meta['points'])
    formulas = ''.join(f'<li>{x}</li>' for x in meta['formulas'])
    probs = ''.join(f'<li>{q}</li>' for q in meta['problems'])
    body = f'''
<div class="eyebrow">DPEN022 Trigonometry · {meta["source"]}</div>
<span class="tag">{meta["group"]}</span>
<h1>{H.escape(meta["title"])}</h1>
<p class="sub">{meta["blurb"]}</p>
<div class="nav">
  <a href="index.html">← Lesson sets hub</a>
  <a href="{meta["slug"]}-answers.html">Open Separate Answers</a>
  <a href="../../index.html">Class notes</a>
  <a href="../../../index.html">DPEN22 home</a>
</div>
<div class="chiprow">{chips}</div>

<h2>1. Short lesson</h2>
<div class="lesson">{lesson_html}</div>

<h2>2. Key points summary</h2>
<div class="summary"><ul>{points}</ul></div>

<h2>3. Formulas &amp; identities</h2>
<div class="formulas"><ul>{formulas}</ul></div>

<h2>4. Practice problems (15)</h2>
<div class="problems"><ol>{probs}</ol></div>

<div class="chiprow" style="margin-top:22px;">
  <a class="chip on" href="{meta["slug"]}-answers.html">✅ Answers for this set</a>
</div>
'''
    (OUT / f'{meta["slug"]}.html').write_text(page(meta['title'], body))
    answers_page(meta, siblings)


def answers_page(meta, siblings):
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
<div class="eyebrow">DPEN022 Trigonometry · {meta["source"]}</div>
<span class="tag">{meta["group"]} · ANSWERS</span>
<h1>{H.escape(title)}</h1>
<p class="sub">Answers to the 15 practice problems in this set.</p>
<div class="nav">
  <a href="{meta["slug"]}.html">← Back to lesson &amp; problems</a>
  <a href="index.html">Lesson sets hub</a>
  <a href="../../index.html">Class notes</a>
</div>
<div class="chiprow">{chips}</div>

<h2>Answers (15)</h2>
<div class="answers">{rows}</div>
'''
    (OUT / f'{meta["slug"]}-answers.html').write_text(page(title, body))


# ===================== CONTENT =====================
# Group A: Weeks 1A + 1B → 3 sets
# Group B: Week 1C → 3 sets
# Group C: Week 1D → 3 sets
# Group D: Week 2A → 3 sets

GROUPS = {}

GROUPS['1a1b'] = {
  'label': 'Weeks 1A + 1B',
  'sets': [
  {
    'slug': 'w1ab-set1', 'short': '1A+1B Set 1', 'group': 'WEEKS 1A + 1B · SET 1 OF 5',
    'source': 'Student Notes Week 1A (filled-in)',
    'title': 'Right triangles & trigonometric ratios',
    'blurb': 'From Week 1A: naming sides, SOH-CAH-TOA, reciprocal ratios, and complementary angles.',
    'lesson': [
      r'Trigonometry studies the relationship between sides and angles in triangles. In a right-angled triangle the <strong>hypotenuse</strong> is opposite the \(90^\circ\) angle and is the longest side. Relative to a chosen acute angle \(\theta\), the other sides are the <strong>opposite</strong> and <strong>adjacent</strong>.',
      r'In similar right triangles the side ratios are constant for a fixed \(\theta\). Those constant ratios are \(\sin\theta\), \(\cos\theta\) and \(\tan\theta\). Their reciprocals are \(\csc\theta\), \(\sec\theta\) and \(\cot\theta\).',
      r'Complementary angles add to \(90^\circ\). This gives the co-function identities \(\sin\theta=\cos(90^\circ-\theta)\) and \(\cos\theta=\sin(90^\circ-\theta)\).',
    ],
    'example': r'In a \(3\)-\(4\)-\(5\) triangle, if the opposite to \(\theta\) is \(3\) and the hypotenuse is \(5\), then \(\sin\theta=\dfrac35\), \(\cos\theta=\dfrac45\), \(\tan\theta=\dfrac34\), \(\csc\theta=\dfrac53\), \(\sec\theta=\dfrac54\), \(\cot\theta=\dfrac43\).',
    'points': [
      'Hypotenuse is always opposite the right angle.',
      'Opposite/adjacent depend on which acute angle you choose.',
      'Remember <strong>SOH-CAH-TOA</strong>.',
      r'\(\sin\theta\) and \(\cos\theta\) are never greater than \(1\) in a right triangle.',
      r'Reciprocals: \(\csc\theta=\dfrac{1}{\sin\theta}\), \(\sec\theta=\dfrac{1}{\cos\theta}\), \(\cot\theta=\dfrac{1}{\tan\theta}\).',
      r'Complementary: \(\sin\theta=\cos(90^\circ-\theta)\).',
    ],
    'formulas': [
      r'\(\sin\theta=\dfrac{\text{opp}}{\text{hyp}},\quad \cos\theta=\dfrac{\text{adj}}{\text{hyp}},\quad \tan\theta=\dfrac{\text{opp}}{\text{adj}}\)',
      r'\(\csc\theta=\dfrac{\text{hyp}}{\text{opp}},\quad \sec\theta=\dfrac{\text{hyp}}{\text{adj}},\quad \cot\theta=\dfrac{\text{adj}}{\text{opp}}\)',
      r'\(\csc\theta=\dfrac{1}{\sin\theta},\ \sec\theta=\dfrac{1}{\cos\theta},\ \cot\theta=\dfrac{1}{\tan\theta}=\dfrac{\cos\theta}{\sin\theta}\)',
      r'\(\sin\theta=\cos(90^\circ-\theta),\quad \cos\theta=\sin(90^\circ-\theta),\quad \tan\theta=\cot(90^\circ-\theta)\)',
    ],
    'problems': [
      r'In a right triangle, label opp/adj/hyp relative to an acute angle \(\theta\) when the sides touching \(\theta\) are \(5\) and \(12\), and the hypotenuse is \(13\).',
      r'Using those sides, find \(\sin\theta\), \(\cos\theta\) and \(\tan\theta\).',
      r'Find \(\sec\theta\) and \(\cot\theta\) for the same triangle.',
      r'If \(\sin\alpha=\dfrac{5}{13}\) and \(\alpha\) is acute, find \(\cos\alpha\) and \(\tan\alpha\).',
      r'If \(\cos\beta=\dfrac{8}{17}\) (acute), find \(\sin\beta\) and \(\sec\beta\).',
      r'Write \(\cos 25^\circ\) as a sine of a complementary angle.',
      r'Write \(\sin 72^\circ\) as a cosine of a complementary angle.',
      r'In \(\triangle ABC\) right-angled at \(C\), \(AC=6\), \(BC=8\). Find \(\sin A\) and \(\cos A\).',
      r'Find \(\tan A\) and \(\csc A\) for the triangle in Q8.',
      r'If \(\tan\theta=\dfrac{7}{24}\) (acute), find \(\sin\theta\) and \(\cos\theta\).',
      r'Simplify \(\dfrac{\sin\theta}{\cos\theta}\).',
      r'Simplify \(\sin\theta\cdot\csc\theta\).',
      r'Explain why \(\sin\theta\) cannot equal \(1.2\) for a real acute angle in a right triangle.',
      r'If \(\sec\theta=\dfrac{5}{3}\) (acute), find \(\cos\theta\) and \(\sin\theta\).',
      r'Find \(\cot(90^\circ-\theta)\) in terms of \(\tan\theta\).',
    ],
    'answers': [
      r'opp \(5\), adj \(12\), hyp \(13\) (or swapped if \(\theta\) is at the other acute corner — state your choice).',
      r'\(\sin=\dfrac{5}{13},\ \cos=\dfrac{12}{13},\ \tan=\dfrac{5}{12}\).',
      r'\(\sec=\dfrac{13}{12},\ \cot=\dfrac{12}{5}\).',
      r'adj \(12\); \(\cos=\dfrac{12}{13},\ \tan=\dfrac{5}{12}\).',
      r'opp \(15\); \(\sin=\dfrac{15}{17},\ \sec=\dfrac{17}{8}\).',
      r'\(\cos25^\circ=\sin65^\circ\).',
      r'\(\sin72^\circ=\cos18^\circ\).',
      r'\(\sin A=\dfrac{8}{10}=\dfrac45,\ \cos A=\dfrac{6}{10}=\dfrac35\).',
      r'\(\tan A=\dfrac43,\ \csc A=\dfrac54\).',
      r'hyp \(25\); \(\sin=\dfrac{7}{25},\ \cos=\dfrac{24}{25}\).',
      r'\(\tan\theta\).',
      r'\(1\).',
      r'Opposite cannot exceed hypotenuse, so \(\sin\theta\le 1\).',
      r'\(\cos=\dfrac35\); opp \(4\); \(\sin=\dfrac45\).',
      r'\(\cot(90^\circ-\theta)=\tan\theta\).',
    ],
  },
  {
    'slug': 'w1ab-set2', 'short': '1A+1B Set 2', 'group': 'WEEKS 1A + 1B · SET 2 OF 5',
    'source': 'Student Notes Week 1A (filled-in)',
    'title': 'Exact ratios & right-triangle applications',
    'blurb': r'From Week 1A: exact values for \(30^\circ,45^\circ,60^\circ\), calculator use, and standard right-triangle problems (including elevation).',
    'lesson': [
      r'Exact trig values come from two special triangles: the isosceles right triangle (\(45^\circ\)-\(45^\circ\)-\(90^\circ\)) with sides \(1:1:\sqrt2\), and the half-equilateral triangle (\(30^\circ\)-\(60^\circ\)-\(90^\circ\)) with sides \(1:\sqrt3:2\).',
      CANONICAL_TRIANGLES,
      r'Read every ratio straight off the triangles with SOH-CAH-TOA. For example \(\sin 30^\circ\) is the side opposite \(30^\circ\) over the hypotenuse, \(\dfrac12\); and \(\tan 60^\circ\) is opposite over adjacent, \(\dfrac{\sqrt3}{1}=\sqrt3\).',
      r'The same two triangles serve radian questions unchanged — \(30^\circ,45^\circ,60^\circ\) are just \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\), so \(\sin\dfrac{\pi}{6}=\dfrac12\) and \(\cos\dfrac{\pi}{4}=\dfrac{\sqrt2}{2}\).',
      r'These give exact \(\sin,\cos,\tan\) of \(30^\circ,45^\circ,60^\circ\) without a calculator. For other acute angles, use a calculator in <strong>degree</strong> mode (or <strong>radian</strong> mode when the question is in radians) and round as required.',
      'Right-triangle applications: choose the ratio that links the known side/angle to the unknown. Elevation/depression problems are just right triangles standing upright.',
    ],
    'example': r'\(\sin 30^\circ=\dfrac12\), \(\cos 30^\circ=\dfrac{\sqrt3}{2}\), \(\tan 30^\circ=\dfrac{1}{\sqrt3}\); \(\sin 45^\circ=\cos 45^\circ=\dfrac{\sqrt2}{2}\), \(\tan 45^\circ=1\); \(\sin 60^\circ=\dfrac{\sqrt3}{2}\), \(\cos 60^\circ=\dfrac12\), \(\tan 60^\circ=\sqrt3\).',
    'points': [
      r'<strong>Exam requirement:</strong> know the exact ratios for \(30^\circ,45^\circ,60^\circ\) (\(\tfrac{\pi}{6},\tfrac{\pi}{4},\tfrac{\pi}{3}\)) from the two canonical triangles, in degrees and radians.',
      r'\(45^\circ\)-\(45^\circ\)-\(90^\circ\) (\(\tfrac{\pi}{4},\tfrac{\pi}{4},\tfrac{\pi}{2}\)) sides: \(1:1:\sqrt2\) — half a unit square.',
      r'\(30^\circ\)-\(60^\circ\)-\(90^\circ\) (\(\tfrac{\pi}{6},\tfrac{\pi}{3},\tfrac{\pi}{2}\)) sides: \(1:\sqrt3:2\) (short leg opposite \(30^\circ\)) — half an equilateral triangle of side \(2\).',
      'If you can redraw the two triangles, you can rebuild every exact ratio without memorising the table.',
      'Check the calculator mode matches the question: degrees for degree problems, radians for radian problems.',
      'Elevation: angle up from horizontal; depression: angle down from horizontal.',
    ],
    'formulas': [
      r'\(\sin30^\circ=\sin\dfrac{\pi}{6}=\dfrac12,\ \cos30^\circ=\dfrac{\sqrt3}{2},\ \tan30^\circ=\dfrac{1}{\sqrt3}\)',
      r'\(\sin45^\circ=\sin\dfrac{\pi}{4}=\dfrac{\sqrt2}{2},\ \cos45^\circ=\dfrac{\sqrt2}{2},\ \tan45^\circ=1\)',
      r'\(\sin60^\circ=\sin\dfrac{\pi}{3}=\dfrac{\sqrt3}{2},\ \cos60^\circ=\dfrac12,\ \tan60^\circ=\sqrt3\)',
      r'Reciprocals: \(\csc30^\circ=2,\ \sec45^\circ=\sqrt2,\ \cot60^\circ=\dfrac{1}{\sqrt3}\)',
      r'Degrees to radians: multiply by \(\dfrac{\pi}{180}\); radians to degrees: multiply by \(\dfrac{180}{\pi}\).',
      r'Unknown side: rearrange SOH-CAH-TOA, e.g. \(\text{opp}=\text{hyp}\sin\theta\).',
    ],
    'problems': [
      r'Find the exact value of \(\sin 60^\circ+\cos 30^\circ\).',
      r'Find the exact value of \(\tan 45^\circ\cdot\sin 30^\circ\).',
      r'Find the exact value of \(\dfrac{\sin 60^\circ}{\cos 60^\circ}\).',
      r'Simplify \(\sin^2 45^\circ+\cos^2 45^\circ\).',
      r'A right triangle has an acute angle \(30^\circ\) and hypotenuse \(10\). Find the exact opposite and adjacent sides.',
      r'A right triangle has an acute angle \(45^\circ\) and adjacent side \(6\). Find the exact hypotenuse and opposite.',
      r'Find \(x\) to 2 d.p. if \(\sin 38^\circ=\dfrac{x}{12}\).',
      r'Find \(\theta\) to the nearest degree if \(\cos\theta=\dfrac{7}{15}\) and \(\theta\) is acute.',
      r'Find \(\theta\) to the nearest minute if \(\tan\theta=\dfrac{9}{20}\) and \(\theta\) is acute.',
      r'From a point \(40\) m from a tower base, the angle of elevation to the top is \(28^\circ\). Find the tower height to 1 d.p.',
      r'A \(15\) m ladder leans against a wall at \(65^\circ\) to the ground. How far is the base from the wall (2 d.p.)?',
      r'Exact value of \(\sec 30^\circ\).',
      r'Exact value of \(\csc 45^\circ\).',
      r'Exact value of \(\cot 60^\circ\).',
      r'A ship is \(1.8\) km from a lighthouse. Angle of elevation to the top is \(14^\circ\). Find the lighthouse height to 2 d.p. (in km).',
    ],
    'answers': [
      r'\(\dfrac{\sqrt3}{2}+\dfrac{\sqrt3}{2}=\sqrt3\).',
      r'\(1\cdot\dfrac12=\dfrac12\).',
      r'\(\sqrt3\).',
      r'\(1\).',
      r'opp \(5\), adj \(5\sqrt3\).',
      r'hyp \(6\sqrt2\), opp \(6\).',
      r'\(x=12\sin38^\circ\approx7.39\).',
      r'\(\theta=\cos^{-1}(7/15)\approx62^\circ\).',
      r'\(\theta=\tan^{-1}(9/20)\approx24^\circ14\'\).',
      r'\(40\tan28^\circ\approx21.3\) m.',
      r'\(15\cos65^\circ\approx6.34\) m.',
      r'\(\dfrac{2}{\sqrt3}=\dfrac{2\sqrt3}{3}\).',
      r'\(\sqrt2\).',
      r'\(\dfrac{1}{\sqrt3}=\dfrac{\sqrt3}{3}\).',
      r'\(1.8\tan14^\circ\approx0.45\) km.',
    ],
  },
  {
    'slug': 'w1ab-set3', 'short': '1A+1B Set 3', 'group': 'WEEKS 1A + 1B · SET 3 OF 5',
    'source': 'Student Notes Week 1B (filled-in)',
    'title': 'Angles of any magnitude (degrees)',
    'blurb': r'From Week 1B: unit circle, CAST signs, reference angles, exact values beyond \(90^\circ\), and solving trig equations in degrees.',
    'lesson': [
      r'On the unit circle, a point \(P\) at angle \(\theta\) (from the positive \(x\)-axis, anticlockwise positive) has coordinates \((\cos\theta,\sin\theta)\). This extends trig ratios to any magnitude, including negatives.',
      'Signs by quadrant (CAST / ASTC): All positive in Q1; Sin positive in Q2; Tan positive in Q3; Cos positive in Q4.',
      r'A <strong>reference angle</strong> is the acute angle between the terminal ray and the \(x\)-axis. Exact values for non-acute angles = (sign from quadrant) × (exact acute value).',
      r'To solve equations like \(\sin\theta=k\) on \(0^\circ\le\theta\le360^\circ\): find the reference angle, then list all solutions in the correct quadrants.',
    ],
    'example': r'\(\sin 150^\circ=\sin 30^\circ=\dfrac12\) (Q2, sin +). \(\cos 210^\circ=-\cos 30^\circ=-\dfrac{\sqrt3}{2}\) (Q3, cos −).',
    'points': [
      r'\(P(\cos\theta,\sin\theta)\) on the unit circle.',
      'Positive angles anticlockwise; negative clockwise.',
      'Remember CAST for signs.',
      'Reference angle is always acute.',
      r'Axis angles: \(0^\circ,90^\circ,180^\circ,270^\circ,360^\circ\) have simple coordinates.',
      'Equation solving: reference angle → correct quadrants → list all in the interval.',
    ],
    'formulas': [
      r'\(\sin\theta=y,\ \cos\theta=x,\ \tan\theta=\dfrac{y}{x}\) on the unit circle.',
      r'Reference angles: Q2: \(180^\circ-\theta\); Q3: \(\theta-180^\circ\); Q4: \(360^\circ-\theta\).',
      r'\(\sin(180^\circ-\theta)=\sin\theta,\ \cos(180^\circ-\theta)=-\cos\theta\).',
      r'\(\sin(-\theta)=-\sin\theta,\ \cos(-\theta)=\cos\theta,\ \tan(-\theta)=-\tan\theta\).',
    ],
    'problems': [
      r'State the sign of \(\sin\theta\), \(\cos\theta\), \(\tan\theta\) in Quadrant 2.',
      r'Find the reference angle for \(150^\circ\).',
      r'Find the reference angle for \(240^\circ\).',
      r'Find the reference angle for \(-135^\circ\).',
      r'Exact value of \(\sin 150^\circ\).',
      r'Exact value of \(\cos 210^\circ\).',
      r'Exact value of \(\tan 315^\circ\).',
      r'Exact value of \(\sin(-90^\circ)\).',
      r'Which quadrant contains \(\theta\) if \(\sin\theta<0\) and \(\cos\theta>0\)?',
      r'Which quadrant if \(\sec\theta<0\) and \(\cot\theta>0\)?',
      r'Solve \(\sin\theta=\dfrac12\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\cos\theta=-\dfrac{\sqrt3}{2}\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\tan\theta=1\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(2\sin\theta=-1\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(2\cos\theta=\sqrt{2}\) for \(0^\circ\le\theta\le360^\circ\).',
    ],
    'answers': [
      r'sin +, cos −, tan −.',
      r'\(30^\circ\).',
      r'\(60^\circ\).',
      r'\(45^\circ\) (coterminal \(225^\circ\)).',
      r'\(\dfrac12\).',
      r'\(-\dfrac{\sqrt3}{2}\).',
      r'\(-1\).',
      r'\(-1\).',
      r'Quadrant 4.',
      r'Quadrant 3.',
      r'\(30^\circ,150^\circ\).',
      r'\(150^\circ,210^\circ\).',
      r'\(45^\circ,225^\circ\).',
      r'\(210^\circ,330^\circ\).',
      r'\(45^\circ,315^\circ\).',
    ],
  },
  {
      'slug': 'w1ab-set4', 'short': '1A+1B Set 4', 'group': 'WEEKS 1A + 1B · SET 4 OF 5',
      'source': 'Student Notes Week 1A (filled-in)',
      'title': 'Mixed right-triangle applications & exact values',
      'blurb': r'From Weeks 1A–1B: multi-step right-triangle problems, exact \(30^\circ/45^\circ/60^\circ\) values, co-functions, and elevation/bearing-style applications.',
      'lesson': [
        r'Application problems often need more than one right triangle, or a mix of exact special angles and calculator work. Sketch first, mark known sides and angles, then choose SOH-CAH-TOA for each unknown.',
        r'When two observers (or two positions) look at the same object, draw both triangles sharing a height or a common side. Solve one triangle, then feed that length into the second.',
        r'Exact and approximate answers can appear in the same question: leave special-angle work in surds, and use a calculator (degree mode) only where the angle is not \(30^\circ\), \(45^\circ\) or \(60^\circ\).',
        r'Co-function identities \(\sin\theta=\cos(90^\circ-\theta)\) remain useful for rewriting and for checking complementary angles in a right triangle.',
      ],
      'example': r'From a point \(A\), the angle of elevation to the top of a tower is \(30^\circ\). From a point \(B\) a further \(20\) m toward the tower, the elevation is \(45^\circ\). Height \(h\) satisfies \(\dfrac{h}{d+20}=\tan30^\circ\) and \(\dfrac{h}{d}=\tan45^\circ\), so \(h=d\) and \(d+20=h\sqrt3\), giving \(h=20(\sqrt3+1)\).',
      'points': [
        'Sketch and label every triangle before writing ratios.',
        'Shared heights or shared bases link multi-triangle problems.',
        r'Exact values for \(30^\circ,45^\circ,60^\circ\); calculator for other acute angles.',
        r'Co-functions: \(\sin\theta=\cos(90^\circ-\theta)\).',
        'State units and round only at the end when a decimal is required.',
        'Bearings: measure clockwise from north unless the question says otherwise.',
      ],
      'formulas': [
        r'\(\sin\theta=\dfrac{\text{opp}}{\text{hyp}},\ \cos\theta=\dfrac{\text{adj}}{\text{hyp}},\ \tan\theta=\dfrac{\text{opp}}{\text{adj}}\)',
        r'\(\sin30^\circ=\dfrac12,\ \sin45^\circ=\dfrac{\sqrt2}{2},\ \sin60^\circ=\dfrac{\sqrt3}{2}\) (and matching cos/tan)',
        r'\(\sin\theta=\cos(90^\circ-\theta),\ \cos\theta=\sin(90^\circ-\theta)\)',
        r'Two-triangle elevation: eliminate the unknown base distance between stations.',
        r'Bearing: direction measured clockwise from north.',
      ],
      'problems': [
        r'From point \(A\) on level ground, the angle of elevation to the top of a tower is \(30^\circ\). From point \(B\), \(40\) m closer to the tower on the same straight line, the elevation is \(45^\circ\). Find the exact height of the tower.',
        r'A surveyor at \(P\) measures the angle of elevation to the top of a cliff as \(28^\circ\). Walking \(50\) m toward the cliff to \(Q\), the elevation becomes \(41^\circ\). Find the cliff height to 1 d.p.',
        r'Exact value of \(\sin 60^\circ\cos 30^\circ+\cos 60^\circ\sin 30^\circ\).',
        r'Exact value of \(\dfrac{\tan 60^\circ-\tan 45^\circ}{1+\tan 60^\circ\tan 45^\circ}\).',
        r'Write \(\cos 18^\circ\) as a sine, and \(\sin 72^\circ\) as a cosine, using co-functions.',
        r'In right \(\triangle ABC\) with right angle at \(C\), \(AC=5\sqrt3\) and \(\angle A=30^\circ\). Find exact \(BC\) and \(AB\).',
        r'A \(12\) m ladder leans against a wall so that the angle with the ground is \(60^\circ\). Find the exact height reached on the wall and the exact distance of the foot from the wall.',
        r'A ship sails from harbour \(H\) on a bearing of \(035^\circ\) for \(4.5\) km to \(A\). Find, to 2 d.p., how far east and how far north of \(H\) the ship is at \(A\).',
        r'If \(\tan\theta=\dfrac{5}{12}\) (acute) and \(\phi=90^\circ-\theta\), find exact \(\sin\phi\) and \(\cos\phi\).',
        r'A kite string is \(85\) m long and makes a \(52^\circ\) angle with the ground. Find the kite height to the nearest metre, and the horizontal distance from flyer to a point directly below the kite (1 d.p.).',
        r'Exact value of \(\sec 45^\circ+\csc 30^\circ-\cot 60^\circ\).',
        r'An observer on a cliff \(60\) m above sea level sees a boat at an angle of depression of \(18^\circ\). Find the boat distance from the cliff base to 1 d.p.',
        r'In a right triangle, one acute angle is \(x\) and the opposite side is \(7\). The adjacent side is \(7\sqrt3\). Find \(x\) exactly and the hypotenuse.',
        r'Simplify \(\dfrac{\sin(90^\circ-\theta)}{\cos(90^\circ-\theta)}\) in terms of \(\tan\theta\).',
        r'From \(A\), elevation to a tower top is \(35^\circ\); from \(B\), \(25\) m farther from the tower along the line of sight on level ground, elevation is \(22^\circ\). Find the tower height to 1 d.p.',
      ],
      'answers': [
        r'''Let the distance from \(B\) to the tower base be \(d\) m and the height be \(h\) m.
  Then \(\tan45^\circ=\dfrac{h}{d}\) and \(\tan30^\circ=\dfrac{h}{d+40}\).
  \[
  \begin{aligned}
  h&=d\cdot 1=d,\\
  \frac{h}{d+40}&=\frac{1}{\sqrt3}\implies h\sqrt3=d+40=h+40,\\
  h(\sqrt3-1)&=40,\\
  h&=\frac{40}{\sqrt3-1}=\frac{40(\sqrt3+1)}{2}=20(\sqrt3+1).
  \end{aligned}
  \]
  \[\boxed{h=20(\sqrt3+1)\text{ m}}\]''',
        r'''Let \(d\) be the distance from \(Q\) to the cliff base and \(h\) the height.
  \[
  \begin{aligned}
  \tan41^\circ&=\frac{h}{d},\quad \tan28^\circ=\frac{h}{d+50}\\
  h&=d\tan41^\circ=(d+50)\tan28^\circ\\
  d\tan41^\circ-d\tan28^\circ&=50\tan28^\circ\\
  d&=\frac{50\tan28^\circ}{\tan41^\circ-\tan28^\circ}\approx 87.09\\
  h&=d\tan41^\circ\approx 75.7.
  \end{aligned}
  \]
  \[\boxed{h\approx 75.7\text{ m}}\]''',
        r'''Use exact values \(\sin60^\circ=\dfrac{\sqrt3}{2}\), \(\cos30^\circ=\dfrac{\sqrt3}{2}\), \(\cos60^\circ=\dfrac12\), \(\sin30^\circ=\dfrac12\).
  \[
  \begin{aligned}
  \sin60^\circ\cos30^\circ+\cos60^\circ\sin30^\circ
  &=\frac{\sqrt3}{2}\cdot\frac{\sqrt3}{2}+\frac12\cdot\frac12
  =\frac{3}{4}+\frac{1}{4}=1.
  \end{aligned}
  \]
  (This is also \(\sin(60^\circ+30^\circ)=\sin90^\circ=1\).)
  \[\boxed{1}\]''',
        r'''Exact values: \(\tan60^\circ=\sqrt3\), \(\tan45^\circ=1\).
  \[
  \begin{aligned}
  \frac{\tan60^\circ-\tan45^\circ}{1+\tan60^\circ\tan45^\circ}
  &=\frac{\sqrt3-1}{1+\sqrt3\cdot 1}
  =\frac{\sqrt3-1}{\sqrt3+1}
  =\frac{(\sqrt3-1)^2}{3-1}
  =\frac{3-2\sqrt3+1}{2}
  =\frac{4-2\sqrt3}{2}=2-\sqrt3.
  \end{aligned}
  \]
  (This equals \(\tan(60^\circ-45^\circ)=\tan15^\circ\).)
  \[\boxed{2-\sqrt3}\]''',
        r'''Co-function identities: \(\cos\theta=\sin(90^\circ-\theta)\) and \(\sin\theta=\cos(90^\circ-\theta)\).
  \[
  \begin{aligned}
  \cos18^\circ&=\sin(90^\circ-18^\circ)=\sin72^\circ,\\
  \sin72^\circ&=\cos(90^\circ-72^\circ)=\cos18^\circ.
  \end{aligned}
  \]
  \[\boxed{\cos18^\circ=\sin72^\circ;\ \sin72^\circ=\cos18^\circ}\]''',
        r'''Relative to \(\angle A=30^\circ\), adjacent \(AC=5\sqrt3\), opposite \(BC\), hypotenuse \(AB\).
  \[
  \begin{aligned}
  \cos30^\circ&=\frac{AC}{AB}=\frac{\sqrt3}{2}\implies AB=\frac{5\sqrt3}{\sqrt3/2}=10,\\
  \tan30^\circ&=\frac{BC}{AC}=\frac{1}{\sqrt3}\implies BC=\frac{5\sqrt3}{\sqrt3}=5.
  \end{aligned}
  \]
  \[\boxed{BC=5,\ AB=10}\]''',
        r'''Hypotenuse \(12\), angle with ground \(60^\circ\).
  \[
  \begin{aligned}
  \text{height}&=12\sin60^\circ=12\cdot\frac{\sqrt3}{2}=6\sqrt3,\\
  \text{base}&=12\cos60^\circ=12\cdot\frac12=6.
  \end{aligned}
  \]
  \[\boxed{\text{height }6\sqrt3\text{ m},\ \text{base }6\text{ m}}\]''',
        r'''Bearing \(035^\circ\) from north means the path makes \(35^\circ\) with the north direction.
  East component (opposite \(35^\circ\)): \(4.5\sin35^\circ\approx 4.5(0.5736)=2.581\approx 2.58\) km.
  North component (adjacent \(35^\circ\)): \(4.5\cos35^\circ\approx 4.5(0.8192)=3.686\approx 3.69\) km.
  \[\boxed{\text{east }2.58\text{ km},\ \text{north }3.69\text{ km}}\]''',
        r'''If \(\tan\theta=\dfrac{5}{12}\) (acute), then opp \(5\), adj \(12\), hyp \(13\), so \(\sin\theta=\dfrac{5}{13}\), \(\cos\theta=\dfrac{12}{13}\).
  Since \(\phi=90^\circ-\theta\),
  \[
  \begin{aligned}
  \sin\phi&=\sin(90^\circ-\theta)=\cos\theta=\frac{12}{13},\\
  \cos\phi&=\cos(90^\circ-\theta)=\sin\theta=\frac{5}{13}.
  \end{aligned}
  \]
  \[\boxed{\sin\phi=\dfrac{12}{13},\ \cos\phi=\dfrac{5}{13}}\]''',
        r'''String is hypotenuse \(85\) m at \(52^\circ\) to the ground.
  \[
  \begin{aligned}
  h&=85\sin52^\circ\approx 85(0.7880)=66.98\approx 67\text{ m},\\
  x&=85\cos52^\circ\approx 85(0.6157)=52.33\approx 52.3\text{ m}.
  \end{aligned}
  \]
  \[\boxed{h\approx 67\text{ m},\ x\approx 52.3\text{ m}}\]''',
        r'''Exact reciprocals: \(\sec45^\circ=\sqrt2\), \(\csc30^\circ=2\), \(\cot60^\circ=\dfrac{1}{\sqrt3}=\dfrac{\sqrt3}{3}\).
  \[
  \sec45^\circ+\csc30^\circ-\cot60^\circ=\sqrt2+2-\frac{\sqrt3}{3}.
  \]
  \[\boxed{\sqrt2+2-\dfrac{\sqrt3}{3}}\]''',
        r'''Angle of depression \(18^\circ\) equals the angle of elevation from the boat. Height \(60\) m is opposite; distance \(d\) from the cliff base is adjacent.
  \[
  \begin{aligned}
  \tan18^\circ&=\frac{60}{d}\\
  d&=\frac{60}{\tan18^\circ}\approx\frac{60}{0.3249}\approx 184.7.
  \end{aligned}
  \]
  \[\boxed{d\approx 184.7\text{ m}}\]''',
        r'''\(\tan x=\dfrac{\text{opp}}{\text{adj}}=\dfrac{7}{7\sqrt3}=\dfrac{1}{\sqrt3}\), so \(x=30^\circ\).
  Hypotenuse:
  \[
  \text{hyp}=\sqrt{7^2+(7\sqrt3)^2}=\sqrt{49+147}=\sqrt{196}=14.
  \]
  \[\boxed{x=30^\circ,\ \text{hyp}=14}\]''',
        r'''Use co-functions: \(\sin(90^\circ-\theta)=\cos\theta\) and \(\cos(90^\circ-\theta)=\sin\theta\).
  \[
  \frac{\sin(90^\circ-\theta)}{\cos(90^\circ-\theta)}=\frac{\cos\theta}{\sin\theta}=\cot\theta=\frac{1}{\tan\theta}.
  \]
  \[\boxed{\dfrac{1}{\tan\theta}}\]''',
        r'''Let \(d\) be the distance from \(A\) to the tower base and \(h\) the height.
  \[
  \begin{aligned}
  \tan35^\circ&=\frac{h}{d},\quad \tan22^\circ=\frac{h}{d+25}\\
  h&=d\tan35^\circ=(d+25)\tan22^\circ\\
  d&=\frac{25\tan22^\circ}{\tan35^\circ-\tan22^\circ}\approx 61.44\\
  h&=d\tan35^\circ\approx 43.0.
  \end{aligned}
  \]
  \[\boxed{h\approx 43.0\text{ m}}\]''',
      ],
  },
  {
      'slug': 'w1ab-set5', 'short': '1A+1B Set 5', 'group': 'WEEKS 1A + 1B · SET 5 OF 5',
      'source': 'Student Notes Week 1B (filled-in)',
      'title': 'CAST, reference angles & multi-solution equations',
      'blurb': r'From Week 1B: exact values beyond \(90^\circ\), CAST signs, reference angles, and solving trig equations on \(0^\circ\le\theta\le360^\circ\) with several solutions.',
      'lesson': [
        r'For any angle, reduce to a reference angle (acute angle to the \(x\)-axis), read the special-triangle value, then attach the CAST sign for the quadrant.',
        r'Equations such as \(\sin\theta=k\) or \(\cos\theta=k\) generally give two solutions per full turn (when \(|k|\lt 1\)). Equations involving \(\tan\theta=k\) also give two solutions in \([0^\circ,360^\circ)\) because the period of tan is \(180^\circ\).',
        r'Forms like \(\sin 2\theta=k\) or \(2\cos\theta=\sqrt2\) are handled by first isolating a single trig expression. For \(\sin 2\theta=k\), solve for \(2\theta\) on a doubled interval, then divide by \(2\) and keep solutions in the original domain.',
        r'Negative angles and angles greater than \(360^\circ\) are first rewritten with a coterminal angle in \([0^\circ,360^\circ)\) before applying CAST.',
      ],
      'example': r'Solve \(2\sin\theta=-\sqrt3\) on \(0^\circ\le\theta\le360^\circ\): \(\sin\theta=-\dfrac{\sqrt3}{2}\), reference \(60^\circ\), sin negative in Q3/Q4 → \(\theta=240^\circ,300^\circ\).',
      'points': [
        r'Reference angle is always acute (or \(0^\circ/90^\circ\) on axes).',
        'CAST gives the sign; the magnitude comes from the reference angle.',
        r'List every solution in the stated interval.',
        r'For \(\sin 2\theta\), work with the interval for \(2\theta\) first.',
        r'Axis angles \(0^\circ,90^\circ,180^\circ,270^\circ,360^\circ\) need special care (one coordinate is \(0\)).',
        r'Tangent repeats every \(180^\circ\).',
      ],
      'formulas': [
        r'Q2 ref: \(180^\circ-\theta\); Q3: \(\theta-180^\circ\); Q4: \(360^\circ-\theta\).',
        r'\(\sin(180^\circ-\theta)=\sin\theta\),\ \(\cos(180^\circ-\theta)=-\cos\theta\).',
        r'\(\sin(-\theta)=-\sin\theta\),\ \(\cos(-\theta)=\cos\theta\).',
        r'If \(\sin\theta=k\): Q1/Q2 when \(k\gt 0\); Q3/Q4 when \(k\lt 0\).',
        r'If \(\cos\theta=k\): Q1/Q4 when \(k\gt 0\); Q2/Q3 when \(k\lt 0\).',
      ],
      'problems': [
        r'Exact value of \(\sin 225^\circ\).',
        r'Exact value of \(\cos 300^\circ\).',
        r'Exact value of \(\tan 210^\circ\).',
        r'Exact value of \(\sin(-150^\circ)\).',
        r'Exact value of \(\cos 495^\circ\) (reduce first).',
        r'Find the reference angle for \(318^\circ\) and state the signs of \(\sin,\cos,\tan\).',
        r'If \(\sin\theta=-\dfrac{\sqrt2}{2}\) and \(\cos\theta\gt 0\), find \(\theta\) in \([0^\circ,360^\circ]\).',
        r'Solve \(\cos\theta=\dfrac12\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(2\sin\theta=\sqrt3\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(\tan\theta=-\sqrt3\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(2\cos\theta+\sqrt2=0\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(\sin 2\theta=\dfrac{\sqrt3}{2}\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(2\sin\theta\cos\theta=\dfrac12\) for \(0^\circ\le\theta\le180^\circ\) (use \(\sin 2\theta=2\sin\theta\cos\theta\)).',
        r'Solve \(\sqrt3\csc\theta=2\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(\sin\theta=\cos\theta\) for \(0^\circ\le\theta\le360^\circ\).',
      ],
      'answers': [
        r'''\(225^\circ\) is in Q3; reference angle \(225^\circ-180^\circ=45^\circ\). Sin is negative in Q3.
  \[
  \sin225^\circ=-\sin45^\circ=-\frac{\sqrt2}{2}.
  \]
  \[\boxed{-\dfrac{\sqrt2}{2}}\]''',
        r'''\(300^\circ\) is in Q4; reference \(360^\circ-300^\circ=60^\circ\). Cos is positive in Q4.
  \[
  \cos300^\circ=\cos60^\circ=\frac12.
  \]
  \[\boxed{\dfrac12}\]''',
        r'''\(210^\circ\) is in Q3; reference \(210^\circ-180^\circ=30^\circ\). Tan is positive in Q3.
  \[
  \tan210^\circ=\tan30^\circ=\frac{1}{\sqrt3}=\frac{\sqrt3}{3}.
  \]
  \[\boxed{\dfrac{\sqrt3}{3}}\]''',
        r'''\(\sin\) is odd: \(\sin(-150^\circ)=-\sin150^\circ\). Also \(150^\circ\) is Q2 with reference \(30^\circ\), so \(\sin150^\circ=\dfrac12\).
  \[
  \sin(-150^\circ)=-\frac12.
  \]
  \[\boxed{-\dfrac12}\]''',
        r'''Reduce by \(360^\circ\): \(495^\circ-360^\circ=135^\circ\). Then \(135^\circ\) is Q2 with reference \(45^\circ\); cos is negative in Q2.
  \[
  \cos495^\circ=\cos135^\circ=-\cos45^\circ=-\frac{\sqrt2}{2}.
  \]
  \[\boxed{-\dfrac{\sqrt2}{2}}\]''',
        r'''\(318^\circ\) is in Q4. Reference angle:
  \[
  360^\circ-318^\circ=42^\circ.
  \]
  In Q4: \(\sin\lt 0\), \(\cos\gt 0\), \(\tan\lt 0\).
  \[\boxed{\text{ref }42^\circ;\ \sin-,\ \cos+,\ \tan-}\]''',
        r'''\(\sin\theta=-\dfrac{\sqrt2}{2}\) with \(\cos\theta\gt 0\) places \(\theta\) in Q4. Reference \(45^\circ\).
  \[
  \theta=360^\circ-45^\circ=315^\circ.
  \]
  \[\boxed{315^\circ}\]''',
        r'''\(\cos\theta=\dfrac12\) has reference \(60^\circ\). Cos positive in Q1 and Q4.
  \[
  \theta=60^\circ,\quad 360^\circ-60^\circ=300^\circ.
  \]
  \[\boxed{60^\circ,\ 300^\circ}\]''',
        r'''Isolate: \(\sin\theta=\dfrac{\sqrt3}{2}\). Reference \(60^\circ\); sin positive in Q1 and Q2.
  \[
  \theta=60^\circ,\quad 180^\circ-60^\circ=120^\circ.
  \]
  \[\boxed{60^\circ,\ 120^\circ}\]''',
        r'''\(\tan\theta=-\sqrt3\). Reference \(60^\circ\); tan negative in Q2 and Q4.
  \[
  \theta=180^\circ-60^\circ=120^\circ,\quad 360^\circ-60^\circ=300^\circ.
  \]
  \[\boxed{120^\circ,\ 300^\circ}\]''',
        r'''\(2\cos\theta=-\sqrt2\Rightarrow\cos\theta=-\dfrac{\sqrt2}{2}\). Reference \(45^\circ\); cos negative in Q2 and Q3.
  \[
  \theta=180^\circ-45^\circ=135^\circ,\quad 180^\circ+45^\circ=225^\circ.
  \]
  \[\boxed{135^\circ,\ 225^\circ}\]''',
        r'''Let \(\alpha=2\theta\). Then \(\sin\alpha=\dfrac{\sqrt3}{2}\) with \(0^\circ\le\alpha\le720^\circ\).
  Solutions for \(\alpha\): \(60^\circ,120^\circ\) and add \(360^\circ\): \(420^\circ,480^\circ\).
  \[
  \begin{aligned}
  2\theta&=60^\circ,120^\circ,420^\circ,480^\circ\\
  \theta&=30^\circ,60^\circ,210^\circ,240^\circ.
  \end{aligned}
  \]
  \[\boxed{30^\circ,\ 60^\circ,\ 210^\circ,\ 240^\circ}\]''',
        r'''Use \(\sin 2\theta=2\sin\theta\cos\theta\), so \(\sin 2\theta=\dfrac12\) with \(0^\circ\le\theta\le180^\circ\) hence \(0^\circ\le 2\theta\le360^\circ\).
  \[
  \begin{aligned}
  2\theta&=30^\circ,150^\circ\\
  \theta&=15^\circ,75^\circ.
  \end{aligned}
  \]
  (Within \(0^\circ\le 2\theta\le360^\circ\) the only solutions of \(\sin=\tfrac12\) are \(30^\circ\) and \(150^\circ\).)
  \[\boxed{15^\circ,\ 75^\circ}\]''',
        r'''\(\sqrt3\csc\theta=2\Rightarrow\csc\theta=\dfrac{2}{\sqrt3}\Rightarrow\sin\theta=\dfrac{\sqrt3}{2}\).
  Same as Q9:
  \[
  \theta=60^\circ,\ 120^\circ.
  \]
  \[\boxed{60^\circ,\ 120^\circ}\]''',
        r'''Divide by \(\cos\theta\) (where \(\cos\theta\neq 0\)): \(\tan\theta=1\). Also check \(\cos\theta=0\) is impossible for \(\sin=\cos\).
  \[
  \theta=45^\circ,\ 225^\circ.
  \]
  \[\boxed{45^\circ,\ 225^\circ}\]''',
      ],
  },
]}

GROUPS['1c'] = {
  'label': 'Week 1C',
  'sets': [
  {
    'slug': 'w1c-set1', 'short': '1C Set 1', 'group': 'WEEK 1C · SET 1 OF 5',
    'source': 'Student Notes Week 1C (filled-in)',
    'title': 'Radian measure & conversion',
    'blurb': 'From Week 1C: what a radian is, and converting between degrees and radians (exact and approximate).',
    'lesson': [
      r'One radian is the central angle subtended by an arc of length equal to the radius. On a unit circle, a full turn is circumference \(2\pi\), so \(2\pi\) radians \(=360^\circ\) and \(\pi\) radians \(=180^\circ\).',
      r'When no unit is written, angles are assumed to be in radians in higher mathematics. Degree problems must be marked with \(^\circ\).',
      r'Convert degrees → radians by multiplying by \(\dfrac{\pi}{180}\). Convert radians → degrees by multiplying by \(\dfrac{180}{\pi}\).',
    ],
    'example': r'\(90^\circ=\dfrac{\pi}{2}\) rad. \(\dfrac{\pi}{4}\) rad \(=45^\circ\). \(156^\circ\approx 2.72\) rad (2 d.p.).',
    'points': [
      r'\(\pi\) rad \(=180^\circ\) is the master conversion.',
      r'Full turn: \(2\pi\) rad \(=360^\circ\).',
      'Anticlockwise positive; clockwise negative (same as degrees).',
      r'Leave exact answers in terms of \(\pi\) unless asked for decimals.',
    ],
    'formulas': [
      r'\(\pi\ \text{rad}=180^\circ\)',
      r'degrees → radians: multiply by \(\dfrac{\pi}{180}\)',
      r'radians → degrees: multiply by \(\dfrac{180}{\pi}\)',
      r'\(1\) rad \(\approx 57.3^\circ\);\ \(1^\circ\approx 0.0175\) rad',
    ],
    'problems': [
      r'Express \(30^\circ\) in radians (exact).',
      r'Express \(135^\circ\) in radians (exact).',
      r'Express \(240^\circ\) in radians (exact).',
      r'Express \(156^\circ\) in radians to 2 d.p.',
      r'Express \(\dfrac{\pi}{2}\) in degrees.',
      r'Express \(\dfrac{2\pi}{3}\) in degrees.',
      r'Express \(\dfrac{5\pi}{6}\) in degrees.',
      r'Express \(\dfrac{7\pi}{4}\) in degrees.',
      r'Express \(1.2\) rad in degrees to 1 d.p.',
      r'How many radians in three full turns (exact)?',
      r'Convert \(-90^\circ\) to radians (exact).',
      r'Convert \(-\dfrac{\pi}{3}\) to degrees.',
      r'Which is larger: \(2\) rad or \(100^\circ\)? Justify.',
      r'An arc of a unit circle has length \(\dfrac{\pi}{3}\). What central angle (rad and deg)?',
      r'Write \(270^\circ\) in radians and state its unit-circle coordinates.',
    ],
    'answers': [
      r'\(\dfrac{\pi}{6}\).',
      r'\(\dfrac{3\pi}{4}\).',
      r'\(\dfrac{4\pi}{3}\).',
      r'\(\approx 2.72\).',
      r'\(90^\circ\).',
      r'\(120^\circ\).',
      r'\(150^\circ\).',
      r'\(315^\circ\).',
      r'\(\approx 68.8^\circ\).',
      r'\(6\pi\).',
      r'\(-\dfrac{\pi}{2}\).',
      r'\(-60^\circ\).',
      r'\(2\) rad \(\approx 114.6^\circ\gt 100^\circ\).',
      r'\(\dfrac{\pi}{3}\) rad \(=60^\circ\).',
      r'\(\dfrac{3\pi}{2}\); point \((0,-1)\).',
    ],
  },
  {
    'slug': 'w1c-set2', 'short': '1C Set 2', 'group': 'WEEK 1C · SET 2 OF 5',
    'source': 'Student Notes Week 1C (filled-in)',
    'title': 'Exact ratios & quadrants in radians',
    'blurb': r'From Week 1C: exact trig values using radian arguments, and identifying quadrants for angles in terms of \(\pi\).',
    'lesson': [
      r'The same special-triangle values apply with radian arguments: replace \(30^\circ,45^\circ,60^\circ\) by \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\).',
      r'Quadrants for \(0\lt \theta\lt 2\pi\): Q1 \(0\lt \theta\lt \dfrac{\pi}{2}\); Q2 \(\dfrac{\pi}{2}\lt \theta\lt \pi\); Q3 \(\pi\lt \theta\lt \dfrac{3\pi}{2}\); Q4 \(\dfrac{3\pi}{2}\lt \theta\lt 2\pi\).',
      r'Angles differing by \(2\pi k\) land on the same unit-circle point. Reduce first, then find the quadrant and reference angle.',
    ],
    'example': r'\(\sin\dfrac{5\pi}{6}=\sin\dfrac{\pi}{6}=\dfrac12\) (Q2). \(\cos\dfrac{4\pi}{3}=-\dfrac12\) (Q3).',
    'points': [
      r'Memorise \(\sin,\cos,\tan\) of \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\) and axis angles.',
      r'Reduce by \(\pm 2\pi\) to get into \([0,2\pi)\).',
      r'Reference angle in radians is still the acute angle to the \(x\)-axis.',
      'CAST signs unchanged.',
    ],
    'formulas': [
      r'\(\sin\dfrac{\pi}{6}=\dfrac12,\ \sin\dfrac{\pi}{4}=\dfrac{\sqrt2}{2},\ \sin\dfrac{\pi}{3}=\dfrac{\sqrt3}{2}\)',
      r'\(\cos\dfrac{\pi}{6}=\dfrac{\sqrt3}{2},\ \cos\dfrac{\pi}{4}=\dfrac{\sqrt2}{2},\ \cos\dfrac{\pi}{3}=\dfrac12\)',
      r'\(\tan\dfrac{\pi}{6}=\dfrac{1}{\sqrt3},\ \tan\dfrac{\pi}{4}=1,\ \tan\dfrac{\pi}{3}=\sqrt3\)',
      r'Q2 ref: \(\pi-\theta\); Q3: \(\theta-\pi\); Q4: \(2\pi-\theta\).',
    ],
    'problems': [
      r'Exact \(\sin\dfrac{\pi}{3}\).',
      r'Exact \(\cos\dfrac{\pi}{4}\).',
      r'Exact \(\tan\dfrac{\pi}{6}\).',
      r'Exact \(\sin\dfrac{2\pi}{3}\).',
      r'Exact \(\cos\dfrac{5\pi}{6}\).',
      r'Exact \(\tan\dfrac{7\pi}{4}\).',
      r'Exact \(\sin\dfrac{3\pi}{2}\).',
      r'Which quadrant is \(\dfrac{7\pi}{4}\) in?',
      r'Which quadrant is \(\dfrac{7\pi}{6}\) in?',
      r'Which quadrant is \(-\dfrac{3\pi}{4}\) in (principal position)?',
      r'Reference angle for \(\dfrac{5\pi}{6}\).',
      r'Reference angle for \(\dfrac{5\pi}{3}\).',
      r'Exact \(\sec\dfrac{\pi}{3}\).',
      r'Exact \(\csc\dfrac{3\pi}{4}\).',
      r'Reduce \(\dfrac{17\pi}{6}\) into \([0,2\pi)\) and find \(\sin\) of it.',
    ],
    'answers': [
      r'\(\dfrac{\sqrt3}{2}\).',
      r'\(\dfrac{\sqrt2}{2}\).',
      r'\(\dfrac{1}{\sqrt3}\).',
      r'\(\dfrac{\sqrt3}{2}\).',
      r'\(-\dfrac{\sqrt3}{2}\).',
      r'\(-1\).',
      r'\(-1\).',
      r'Q4.',
      r'Q3.',
      r'Q3 (coterminal \(\dfrac{5\pi}{4}\)).',
      r'\(\dfrac{\pi}{6}\).',
      r'\(\dfrac{\pi}{3}\).',
      r'\(2\).',
      r'\(\sqrt2\).',
      r'\(\dfrac{5\pi}{6}\); \(\sin=\dfrac12\).',
    ],
  },
  {
    'slug': 'w1c-set3', 'short': '1C Set 3', 'group': 'WEEK 1C · SET 3 OF 5',
    'source': 'Student Notes Week 1C (filled-in)',
    'title': 'Solving trig equations in radians',
    'blurb': 'From Week 1C: solve sine/cosine/tangent equations on a given radian interval with exact answers.',
    'lesson': [
      r'Working in radians is the same process as degrees: find a reference angle, place solutions in the correct quadrants, and list every solution inside the required interval (often \(0\le\theta\le 2\pi\)).',
      r'Write answers as exact multiples of \(\pi\) whenever possible. Check calculator mode only for decimal approximations.',
      r'For equations like \(2\sin\theta=-1\), first isolate the trig function: \(\sin\theta=-\dfrac12\), then solve.',
    ],
    'example': r'Solve \(\sin\theta=\dfrac12\) for \(0\le\theta\le 2\pi\): \(\theta=\dfrac{\pi}{6},\dfrac{5\pi}{6}\).',
    'points': [
      'Isolate the trig ratio first.',
      'Reference angle from the acute inverse (exact where possible).',
      'Use CAST to choose quadrants.',
      'Include all solutions in the interval.',
      r'Answers usually in terms of \(\pi\).',
    ],
    'formulas': [
      r'If \(\sin\theta=k\): solutions in Q1/Q2 (or Q3/Q4 if \(k\lt 0\)).',
      r'If \(\cos\theta=k\): solutions in Q1/Q4 (or Q2/Q3 if \(k\lt 0\)).',
      r'If \(\tan\theta=k\): solutions in Q1/Q3 (or Q2/Q4 if \(k\lt 0\)), period \(\pi\).',
    ],
    'problems': [
      r'Solve \(\sin\theta=\dfrac{\sqrt3}{2}\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\cos\theta=-\dfrac12\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\tan\theta=\sqrt3\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(2\sin\theta=1\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(2\cos\theta=-\sqrt{2}\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\tan\theta=-1\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\sin\theta=0\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\cos\theta=1\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\sin 2\theta=\dfrac12\) for \(0\le\theta\le\pi\) (careful: interval for \(2\theta\)).',
      r'Solve \(2\cos\theta+\sqrt{3}=0\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\sqrt{2}\sin\theta=1\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\cot\theta=1\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\sin\theta=-\dfrac{\sqrt2}{2}\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\cos\theta=0\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(2\sin\theta=-\sqrt{3}\) for \(0\le\theta\le 2\pi\).',
    ],
    'answers': [
      r'\(\dfrac{\pi}{3},\dfrac{2\pi}{3}\).',
      r'\(\dfrac{2\pi}{3},\dfrac{4\pi}{3}\).',
      r'\(\dfrac{\pi}{3},\dfrac{4\pi}{3}\).',
      r'\(\dfrac{\pi}{6},\dfrac{5\pi}{6}\).',
      r'\(\dfrac{3\pi}{4},\dfrac{5\pi}{4}\).',
      r'\(\dfrac{3\pi}{4},\dfrac{7\pi}{4}\).',
      r'\(0,\pi,2\pi\).',
      r'\(0,2\pi\).',
      r'\(2\theta=\dfrac{\pi}{6},\dfrac{5\pi}{6},\dfrac{13\pi}{6},\dfrac{17\pi}{6}\) (within \(0\le 2\theta\le 2\pi\)); \(\theta=\dfrac{\pi}{12},\dfrac{5\pi}{12},\dfrac{13\pi}{12},\dfrac{17\pi}{12}\) — keep those with \(\theta\le\pi\): \(\dfrac{\pi}{12},\dfrac{5\pi}{12}\).',
      r'\(\theta=\dfrac{5\pi}{6},\dfrac{7\pi}{6}\).',
      r'\(\dfrac{\pi}{4},\dfrac{3\pi}{4}\).',
      r'\(\dfrac{\pi}{4},\dfrac{5\pi}{4}\).',
      r'\(\dfrac{5\pi}{4},\dfrac{7\pi}{4}\).',
      r'\(\dfrac{\pi}{2},\dfrac{3\pi}{2}\).',
      r'\(\dfrac{4\pi}{3},\dfrac{5\pi}{3}\).',
    ],
  },
  {
      'slug': 'w1c-set4', 'short': '1C Set 4', 'group': 'WEEK 1C · SET 4 OF 5',
      'source': 'Student Notes Week 1C (filled-in)',
      'title': 'Radian conversion, arcs & exact values',
      'blurb': r'From Week 1C: mixed degree–radian conversion, arc length and sector area, and exact trig values with radian arguments.',
      'lesson': [
        r'Arc length on a circle of radius \(r\) with central angle \(\theta\) in radians is \(s=r\theta\). Sector area is \(A=\dfrac12 r^2\theta\) (again with \(\theta\) in radians).',
        r'Mixed conversion questions may ask for both exact \(\pi\)-form and a decimal. Keep exact form until the last step when a decimal is required.',
        r'Exact trig values in radians use the same special triangles: \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\) and their coterminal / reference-angle cousins in other quadrants.',
        r'When an arc length or sector is given in degrees, convert the angle to radians before using \(s=r\theta\) or \(A=\dfrac12 r^2\theta\).',
      ],
      'example': r'A sector of radius \(6\) and angle \(\dfrac{\pi}{3}\) has arc \(s=6\cdot\dfrac{\pi}{3}=2\pi\) and area \(A=\dfrac12\cdot 36\cdot\dfrac{\pi}{3}=6\pi\).',
      'points': [
        r'\(\pi\) rad \(=180^\circ\) is the conversion key.',
        r'Arc \(s=r\theta\) and sector \(A=\dfrac12 r^2\theta\) need \(\theta\) in radians.',
        r'Reduce angles into \([0,2\pi)\) before reading quadrants.',
        r'Leave exact answers in terms of \(\pi\) unless a decimal is asked.',
        r'Special values: \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\) and axis angles.',
      ],
      'formulas': [
        r'deg \(\to\) rad: \(\times\dfrac{\pi}{180}\); rad \(\to\) deg: \(\times\dfrac{180}{\pi}\)',
        r'\(s=r\theta,\quad A=\dfrac12 r^2\theta\) (\(\theta\) in radians)',
        r'\(\sin\dfrac{\pi}{6}=\dfrac12,\ \sin\dfrac{\pi}{4}=\dfrac{\sqrt2}{2},\ \sin\dfrac{\pi}{3}=\dfrac{\sqrt3}{2}\)',
        r'Full circle: \(\theta=2\pi\), circumference \(2\pi r\), area \(\pi r^2\).',
        r'Q2 ref: \(\pi-\theta\); Q3: \(\theta-\pi\); Q4: \(2\pi-\theta\).',
      ],
      'problems': [
        r'Convert \(210^\circ\) to radians (exact) and \(3.8\) rad to degrees (1 d.p.).',
        r'Convert \(\dfrac{11\pi}{6}\) to degrees and \(75^\circ\) to radians (exact).',
        r'A circle has radius \(5\) cm. Find the exact arc length subtended by a central angle of \(120^\circ\).',
        r'For the same circle (radius \(5\) cm) and \(120^\circ\) central angle, find the exact sector area.',
        r'An arc of length \(10\) cm on a circle of radius \(4\) cm subtends central angle \(\theta\). Find \(\theta\) in radians and in degrees (1 d.p.).',
        r'A sector has area \(18\pi\) and radius \(6\). Find the exact central angle in radians and the exact arc length.',
        r'Exact value of \(\sin\dfrac{5\pi}{3}+\cos\dfrac{5\pi}{3}\).',
        r'Exact value of \(\tan\dfrac{7\pi}{6}\cdot\cos\dfrac{\pi}{6}\).',
        r'Exact value of \(\sec\dfrac{3\pi}{4}+\csc\dfrac{\pi}{6}\).',
        r'Reduce \(\dfrac{19\pi}{4}\) into \([0,2\pi)\) and find exact \(\sin\) and \(\cos\) of the reduced angle.',
        r'A wheel of radius \(0.35\) m rotates through \(250^\circ\). Find the distance a point on the rim travels, to 2 d.p.',
        r'Which is larger: \(\dfrac{5\pi}{6}\) rad or \(140^\circ\)? Justify with a conversion.',
        r'Exact \(\sin\!\left(-\dfrac{2\pi}{3}\right)\) and \(\cos\!\left(-\dfrac{2\pi}{3}\right)\).',
        r'A sector of a circle of radius \(10\) has arc length \(4\pi\). Find the sector area exactly.',
        r'Express \(1\) rad in degrees to the nearest minute.',
      ],
      'answers': [
        r'''Degrees to radians: multiply by \(\dfrac{\pi}{180}\).
  \[
  210^\circ=210\cdot\frac{\pi}{180}=\frac{7\pi}{6}.
  \]
  Radians to degrees: \(3.8\cdot\dfrac{180}{\pi}\approx 217.7^\circ\).
  \[\boxed{\dfrac{7\pi}{6};\ 217.7^\circ}\]''',
        r'''\[
  \frac{11\pi}{6}\cdot\frac{180}{\pi}=330^\circ,\qquad
  75^\circ=75\cdot\frac{\pi}{180}=\frac{5\pi}{12}.
  \]
  \[\boxed{330^\circ;\ \dfrac{5\pi}{12}}\]''',
        r'''Convert \(120^\circ\) to radians: \(\dfrac{2\pi}{3}\). Then \(s=r\theta\).
  \[
  s=5\cdot\frac{2\pi}{3}=\frac{10\pi}{3}\text{ cm}.
  \]
  \[\boxed{\dfrac{10\pi}{3}\text{ cm}}\]''',
        r'''With \(\theta=\dfrac{2\pi}{3}\) and \(r=5\),
  \[
  A=\frac12 r^2\theta=\frac12\cdot 25\cdot\frac{2\pi}{3}=\frac{25\pi}{3}\text{ cm}^2.
  \]
  \[\boxed{\dfrac{25\pi}{3}\text{ cm}^2}\]''',
        r'''\[
  \theta=\frac{s}{r}=\frac{10}{4}=2.5\text{ rad}.
  \]
  In degrees: \(2.5\cdot\dfrac{180}{\pi}\approx 143.2^\circ\).
  \[\boxed{2.5\text{ rad};\ 143.2^\circ}\]''',
        r'''\(A=\dfrac12 r^2\theta\Rightarrow 18\pi=\dfrac12\cdot 36\cdot\theta=18\theta\Rightarrow\theta=\pi\).
  Arc \(s=r\theta=6\pi\).
  \[\boxed{\theta=\pi,\ s=6\pi}\]''',
        r'''\(\dfrac{5\pi}{3}\) is Q4; reference \(\dfrac{\pi}{3}\). Sin −, cos +.
  \[
  \sin\frac{5\pi}{3}=-\frac{\sqrt3}{2},\quad\cos\frac{5\pi}{3}=\frac12,
  \]
  so the sum is \(-\dfrac{\sqrt3}{2}+\dfrac12=\dfrac{1-\sqrt3}{2}\).
  \[\boxed{\dfrac{1-\sqrt3}{2}}\]''',
        r'''\(\dfrac{7\pi}{6}\) is Q3; reference \(\dfrac{\pi}{6}\); tan positive: \(\tan\dfrac{7\pi}{6}=\dfrac{1}{\sqrt3}\).
  Also \(\cos\dfrac{\pi}{6}=\dfrac{\sqrt3}{2}\).
  \[
  \tan\frac{7\pi}{6}\cdot\cos\frac{\pi}{6}=\frac{1}{\sqrt3}\cdot\frac{\sqrt3}{2}=\frac12.
  \]
  \[\boxed{\dfrac12}\]''',
        r'''\(\sec\dfrac{3\pi}{4}=\dfrac{1}{\cos(3\pi/4)}=\dfrac{1}{-\sqrt2/2}=-\sqrt2\), and \(\csc\dfrac{\pi}{6}=2\).
  \[
  \sec\frac{3\pi}{4}+\csc\frac{\pi}{6}=-\sqrt2+2.
  \]
  \[\boxed{2-\sqrt2}\]''',
        r'''\(\dfrac{19\pi}{4}-2\cdot 2\pi=\dfrac{19\pi}{4}-\dfrac{16\pi}{4}=\dfrac{3\pi}{4}\) (in \([0,2\pi)\)).
  \[
  \sin\frac{3\pi}{4}=\frac{\sqrt2}{2},\quad\cos\frac{3\pi}{4}=-\frac{\sqrt2}{2}.
  \]
  \[\boxed{\dfrac{3\pi}{4};\ \sin=\dfrac{\sqrt2}{2},\ \cos=-\dfrac{\sqrt2}{2}}\]''',
        r'''Convert \(250^\circ\) to radians: \(\theta=250\cdot\dfrac{\pi}{180}=\dfrac{25\pi}{18}\).
  \[
  s=r\theta=0.35\cdot\frac{25\pi}{18}\approx 1.53\text{ m}.
  \]
  \[\boxed{s\approx 1.53\text{ m}}\]''',
        r'''Convert \(\dfrac{5\pi}{6}\) to degrees: \(\dfrac{5\pi}{6}\cdot\dfrac{180}{\pi}=150^\circ\gt 140^\circ\).
  Alternatively convert \(140^\circ\) to radians: \(140\cdot\dfrac{\pi}{180}=\dfrac{7\pi}{9}\approx 2.443\), while \(\dfrac{5\pi}{6}\approx 2.618\).
  \[\boxed{\dfrac{5\pi}{6}\text{ is larger}}\]''',
        r'''Odd/even: \(\sin(-\theta)=-\sin\theta\), \(\cos(-\theta)=\cos\theta\).
  \(\dfrac{2\pi}{3}\) is Q2 with reference \(\dfrac{\pi}{3}\), so \(\sin\dfrac{2\pi}{3}=\dfrac{\sqrt3}{2}\), \(\cos\dfrac{2\pi}{3}=-\dfrac12\).
  \[
  \sin\!\left(-\frac{2\pi}{3}\right)=-\frac{\sqrt3}{2},\quad
  \cos\!\left(-\frac{2\pi}{3}\right)=-\frac12.
  \]
  \[\boxed{\sin=-\dfrac{\sqrt3}{2},\ \cos=-\dfrac12}\]''',
        r'''From \(s=r\theta\): \(4\pi=10\theta\Rightarrow\theta=\dfrac{2\pi}{5}\).
  \[
  A=\frac12 r^2\theta=\frac12\cdot 100\cdot\frac{2\pi}{5}=20\pi.
  \]
  \[\boxed{A=20\pi}\]''',
        r'''\[
  1\text{ rad}=\frac{180}{\pi}^\circ\approx 57.2958^\circ.
  \]
  Decimal part \(0.2958^\circ\times 60\approx 17.75'\), which rounds to \(18'\).
  \[\boxed{57^\circ 18'}\]''',
      ],
  },
  {
      'slug': 'w1c-set5', 'short': '1C Set 5', 'group': 'WEEK 1C · SET 5 OF 5',
      'source': 'Student Notes Week 1C (filled-in)',
      'title': r'Radian equations on \([0,2\pi]\)',
      'blurb': 'From Week 1C: solve sine, cosine and tangent equations in radians on a full turn, including rearranging and double-angle forms.',
      'lesson': [
        r'Isolate the trig function first, then find the reference angle in radians and place solutions using CAST. Answers should be exact multiples of \(\pi\) whenever possible.',
        r'When the equation involves \(2\theta\) or \(3\theta\), solve for the multiple angle on the expanded interval, then divide. Keep only solutions that land in the required interval for \(\theta\).',
        r'Rearrangements such as \(2\cos\theta+\sqrt3=0\) or \(\sqrt2\sin\theta-1=0\) are routine once the trig ratio is isolated. Reciprocal equations (\(\sec,\csc,\cot\)) convert to \(\sin,\cos,\tan\) first.',
        r'Always check the endpoints \(0\) and \(2\pi\) when they satisfy the equation, and discard solutions outside the stated interval.',
      ],
      'example': r'Solve \(2\cos\theta=-\sqrt3\) on \(0\le\theta\le 2\pi\): \(\cos\theta=-\dfrac{\sqrt3}{2}\), ref \(\dfrac{\pi}{6}\), Q2/Q3 → \(\theta=\dfrac{5\pi}{6},\dfrac{7\pi}{6}\).',
      'points': [
        'Isolate, reference angle, CAST, list all in the interval.',
        r'For \(k\theta\), expand the interval for \(k\theta\) first.',
        r'Write answers in terms of \(\pi\).',
        'Convert sec/csc/cot to sin/cos/tan before solving.',
        r'Tan has period \(\pi\), so two solutions per \(2\pi\) interval when defined.',
      ],
      'formulas': [
        r'If \(\sin\theta=k\): Q1/Q2 (\(k\gt 0\)) or Q3/Q4 (\(k\lt 0\)).',
        r'If \(\cos\theta=k\): Q1/Q4 (\(k\gt 0\)) or Q2/Q3 (\(k\lt 0\)).',
        r'If \(\tan\theta=k\): period \(\pi\).',
        r'\(\sin 2\theta=2\sin\theta\cos\theta\) (useful when a product appears).',
        r'Reciprocals: \(\csc\theta=\dfrac{1}{\sin\theta}\), etc.',
      ],
      'problems': [
        r'Solve \(\sin\theta=-\dfrac12\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\cos\theta=\dfrac{\sqrt2}{2}\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\tan\theta=\dfrac{1}{\sqrt3}\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(2\sin\theta+\sqrt3=0\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\sqrt2\cos\theta-1=0\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(3\tan\theta+\sqrt3=0\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\sin 2\theta=-\dfrac{\sqrt2}{2}\) for \(0\le\theta\le\pi\).',
        r'Solve \(2\cos 2\theta=1\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\csc\theta=-2\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\sec\theta=\dfrac{2}{\sqrt3}\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\sin\theta=\cos\theta\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(2\sin\theta\cos\theta=\dfrac{\sqrt3}{2}\) for \(0\le\theta\le\pi\).',
        r'Solve \(\cos\theta(\cos\theta-1)=0\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(2\sin^2\theta-1=0\) for \(0\le\theta\le 2\pi\) (use a double-angle idea or factor).',
        r'Solve \(\tan\theta\sin\theta=\sin\theta\) for \(0\le\theta\le 2\pi\) (factor carefully).',
      ],
      'answers': [
        r'''Reference \(\dfrac{\pi}{6}\); sin negative in Q3 and Q4.
  \[
  \theta=\pi+\frac{\pi}{6}=\frac{7\pi}{6},\quad
  2\pi-\frac{\pi}{6}=\frac{11\pi}{6}.
  \]
  \[\boxed{\dfrac{7\pi}{6},\ \dfrac{11\pi}{6}}\]''',
        r'''Reference \(\dfrac{\pi}{4}\); cos positive in Q1 and Q4.
  \[
  \theta=\frac{\pi}{4},\quad 2\pi-\frac{\pi}{4}=\frac{7\pi}{4}.
  \]
  \[\boxed{\dfrac{\pi}{4},\ \dfrac{7\pi}{4}}\]''',
        r'''\(\tan\theta=\dfrac{1}{\sqrt3}\) has reference \(\dfrac{\pi}{6}\); tan positive in Q1 and Q3.
  \[
  \theta=\frac{\pi}{6},\quad \pi+\frac{\pi}{6}=\frac{7\pi}{6}.
  \]
  \[\boxed{\dfrac{\pi}{6},\ \dfrac{7\pi}{6}}\]''',
        r'''\(2\sin\theta=-\sqrt3\Rightarrow\sin\theta=-\dfrac{\sqrt3}{2}\). Reference \(\dfrac{\pi}{3}\); Q3/Q4.
  \[
  \theta=\pi+\frac{\pi}{3}=\frac{4\pi}{3},\quad
  2\pi-\frac{\pi}{3}=\frac{5\pi}{3}.
  \]
  \[\boxed{\dfrac{4\pi}{3},\ \dfrac{5\pi}{3}}\]''',
        r'''\(\sqrt2\cos\theta=1\Rightarrow\cos\theta=\dfrac{1}{\sqrt2}=\dfrac{\sqrt2}{2}\).
  Same as Q2:
  \[
  \theta=\frac{\pi}{4},\ \frac{7\pi}{4}.
  \]
  \[\boxed{\dfrac{\pi}{4},\ \dfrac{7\pi}{4}}\]''',
        r'''\(3\tan\theta=-\sqrt3\Rightarrow\tan\theta=-\dfrac{1}{\sqrt3}\). Reference \(\dfrac{\pi}{6}\); tan negative in Q2/Q4.
  \[
  \theta=\pi-\frac{\pi}{6}=\frac{5\pi}{6},\quad
  2\pi-\frac{\pi}{6}=\frac{11\pi}{6}.
  \]
  \[\boxed{\dfrac{5\pi}{6},\ \dfrac{11\pi}{6}}\]''',
        r'''Let \(\alpha=2\theta\). Then \(\sin\alpha=-\dfrac{\sqrt2}{2}\) with \(0\le\alpha\le 2\pi\).
  \[
  \alpha=\frac{5\pi}{4},\ \frac{7\pi}{4}
  \implies\theta=\frac{5\pi}{8},\ \frac{7\pi}{8}.
  \]
  \[\boxed{\dfrac{5\pi}{8},\ \dfrac{7\pi}{8}}\]''',
        r'''\(\cos 2\theta=\dfrac12\). Let \(\alpha=2\theta\) with \(0\le\alpha\le 4\pi\).
  \[
  \begin{aligned}
  \alpha&=\frac{\pi}{3},\ \frac{5\pi}{3},\ \frac{7\pi}{3},\ \frac{11\pi}{3}\\
  \theta&=\frac{\pi}{6},\ \frac{5\pi}{6},\ \frac{7\pi}{6},\ \frac{11\pi}{6}.
  \end{aligned}
  \]
  \[\boxed{\dfrac{\pi}{6},\ \dfrac{5\pi}{6},\ \dfrac{7\pi}{6},\ \dfrac{11\pi}{6}}\]''',
        r'''\(\csc\theta=-2\Rightarrow\sin\theta=-\dfrac12\), same as Q1.
  \[\boxed{\dfrac{7\pi}{6},\ \dfrac{11\pi}{6}}\]''',
        r'''\(\sec\theta=\dfrac{2}{\sqrt3}\Rightarrow\cos\theta=\dfrac{\sqrt3}{2}\). Reference \(\dfrac{\pi}{6}\); Q1/Q4.
  \[
  \theta=\frac{\pi}{6},\quad 2\pi-\frac{\pi}{6}=\frac{11\pi}{6}.
  \]
  \[\boxed{\dfrac{\pi}{6},\ \dfrac{11\pi}{6}}\]''',
        r'''\(\sin\theta=\cos\theta\Rightarrow\tan\theta=1\) (where \(\cos\theta\neq 0\)).
  \[
  \theta=\frac{\pi}{4},\ \frac{5\pi}{4}.
  \]
  \[\boxed{\dfrac{\pi}{4},\ \dfrac{5\pi}{4}}\]''',
        r'''\(2\sin\theta\cos\theta=\sin 2\theta=\dfrac{\sqrt3}{2}\) with \(0\le\theta\le\pi\) so \(0\le 2\theta\le 2\pi\).
  \[
  2\theta=\frac{\pi}{3},\ \frac{2\pi}{3}
  \implies\theta=\frac{\pi}{6},\ \frac{\pi}{3}.
  \]
  \[\boxed{\dfrac{\pi}{6},\ \dfrac{\pi}{3}}\]''',
        r'''\(\cos\theta=0\) or \(\cos\theta=1\).
  \[
  \cos\theta=0\Rightarrow\theta=\frac{\pi}{2},\ \frac{3\pi}{2};
  \quad\cos\theta=1\Rightarrow\theta=0,\ 2\pi.
  \]
  \[\boxed{0,\ \dfrac{\pi}{2},\ \dfrac{3\pi}{2},\ 2\pi}\]''',
        r'''\(2\sin^2\theta-1=0\Rightarrow\sin^2\theta=\dfrac12\Rightarrow\sin\theta=\pm\dfrac{\sqrt2}{2}\).
  \[
  \theta=\frac{\pi}{4},\ \frac{3\pi}{4},\ \frac{5\pi}{4},\ \frac{7\pi}{4}.
  \]
  (Equivalently \(\cos 2\theta=0\).)
  \[\boxed{\dfrac{\pi}{4},\ \dfrac{3\pi}{4},\ \dfrac{5\pi}{4},\ \dfrac{7\pi}{4}}\]''',
        r'''Factor: \(\sin\theta(\tan\theta-1)=0\).
  So \(\sin\theta=0\) or \(\tan\theta=1\), excluding points where \(\tan\) is undefined.
  \[
  \sin\theta=0\Rightarrow\theta=0,\pi,2\pi;
  \quad\tan\theta=1\Rightarrow\theta=\frac{\pi}{4},\frac{5\pi}{4}.
  \]
  At \(\theta=\dfrac{\pi}{2},\dfrac{3\pi}{2}\), \(\tan\) is undefined, so those are not solutions of the original form as written.
  \[\boxed{0,\ \dfrac{\pi}{4},\ \pi,\ \dfrac{5\pi}{4},\ 2\pi}\]''',
      ],
  },
]}

GROUPS['1d'] = {
  'label': 'Week 1D',
  'sets': [
  {
    'slug': 'w1d-set1', 'short': '1D Set 1', 'group': 'WEEK 1D · SET 1 OF 5',
    'source': 'Student Notes Week 1D (filled-in)',
    'title': 'Graphs of sin, cos and tan',
    'blurb': r'From Week 1D: basic graphs in radians, period, amplitude, and key features of \(y=\sin x\), \(y=\cos x\), \(y=\tan x\).',
    'lesson': [
      r'Plotting unit-circle \(y\)-coordinates as \(x\) varies produces \(y=\sin x\). Plotting \(x\)-coordinates produces \(y=\cos x\). Both are continuous, amplitude \(1\), period \(2\pi\).',
      r'The cosine graph is a horizontal shift of the sine graph (by \(\dfrac{\pi}{2}\)).',
      r'\(y=\tan x\) has period \(\pi\), vertical asymptotes at \(x=\dfrac{\pi}{2}+k\pi\), and no amplitude (range all real \(y\)).',
    ],
    'example': r'For \(y=\sin x\): at \(x=0,\dfrac{\pi}{2},\pi,\dfrac{3\pi}{2},2\pi\) the values are \(0,1,0,-1,0\).',
    'points': [
      r'\(\sin\) and \(\cos\): period \(2\pi\), amplitude \(1\), range \([-1,1]\).',
      r'\(\tan\): period \(\pi\), range \(\mathbb{R}\), asymptotes odd multiples of \(\dfrac{\pi}{2}\).',
      r'\(\sin(x+2k\pi)=\sin x\); \(\tan(x+k\pi)=\tan x\).',
      r'Cosine is sine shifted left by \(\dfrac{\pi}{2}\): \(\cos x=\sin\!\left(x+\dfrac{\pi}{2}\right)\).',
    ],
    'formulas': [
      r'Amplitude of \(a\sin x\) or \(a\cos x\): \(|a|\)',
      r'Period of \(\sin x\) / \(\cos x\): \(2\pi\); of \(\tan x\): \(\pi\)',
      r'Asymptotes of \(\tan x\): \(x=\dfrac{\pi}{2}+k\pi\)',
    ],
    'problems': [
      r'State amplitude and period of \(y=\sin x\).',
      r'State amplitude and period of \(y=\cos x\).',
      r'State period of \(y=\tan x\). Does it have an amplitude?',
      r'Fill: \(\sin 0=\ldots,\ \sin\dfrac{\pi}{2}=\ldots,\ \sin\pi=\ldots\).',
      r'Fill: \(\cos 0=\ldots,\ \cos\dfrac{\pi}{2}=\ldots,\ \cos\pi=\ldots\).',
      r'Where are the first positive asymptotes of \(y=\tan x\)?',
      r'Sketch one cycle of \(y=\sin x\) for \(0\le x\le 2\pi\) (describe key points).',
      r'Sketch one cycle of \(y=\cos x\) for \(0\le x\le 2\pi\) (describe key points).',
      r'What is the range of \(y=\sin x\)?',
      r'What is the range of \(y=\tan x\)?',
      r'True/false: \(\cos x=\sin\!\left(x-\dfrac{\pi}{2}\right)\).',
      r'Find \(x\in[0,2\pi]\) where \(\sin x=0\).',
      r'Find \(x\in[0,2\pi]\) where \(\cos x=-1\).',
      r'Explain why \(y=\tan x\) repeats every \(\pi\), not \(2\pi\).',
      r'Compare \(y=\sin x\) and \(y=\cos x\): what horizontal shift maps one to the other?',
    ],
    'answers': [
      r'amp \(1\), period \(2\pi\).',
      r'amp \(1\), period \(2\pi\).',
      r'period \(\pi\); no amplitude.',
      r'\(0,1,0\).',
      r'\(1,0,-1\).',
      r'\(x=\dfrac{\pi}{2}\) (then \(\dfrac{3\pi}{2}\), …).',
      r'Key points \((0,0),(\pi/2,1),(\pi,0),(3\pi/2,-1),(2\pi,0)\).',
      r'Key points \((0,1),(\pi/2,0),(\pi,-1),(3\pi/2,0),(2\pi,1)\).',
      r'\([-1,1]\).',
      r'all real numbers.',
      r'False (that would be \(-\!\cos x\) related); correct is \(\cos x=\sin(x+\pi/2)\).',
      r'\(0,\pi,2\pi\).',
      r'\(\pi\).',
      r'Tan uses slope \(y/x\); signs and values repeat after half-turn \(\pi\).',
      r'Shift cosine left by \(\pi/2\), or sine right by \(\pi/2\).',
    ],
  },
  {
    'slug': 'w1d-set2', 'short': '1D Set 2', 'group': 'WEEK 1D · SET 2 OF 5',
    'source': 'Student Notes Week 1D (filled-in)',
    'title': 'Amplitude, period & the general sine/cosine model',
    'blurb': r'From Week 1D: transformations \(y=a\sin(bx)+d\) and \(y=a\cos(bx)+d\) — reading amplitude, period and midline.',
    'lesson': [
      r'For \(y=a\sin(bx)\) or \(y=a\cos(bx)\): amplitude is \(|a|\); period is \(\dfrac{2\pi}{|b|}\). The graph is stretched vertically by \(|a|\) and horizontally by \(\dfrac{1}{|b|}\).',
      r'A vertical shift \(+d\) moves the midline to \(y=d\). Range becomes \([d-|a|, d+|a|]\).',
      'Always state amplitude, period, midline/range when describing a transformed wave.',
    ],
    'example': r'\(y=3\sin(2x)\): amp \(3\), period \(\pi\). \(y=2\cos\!\left(\dfrac{x}{2}\right)-1\): amp \(2\), period \(4\pi\), midline \(y=-1\), range \([-3,1]\).',
    'points': [
      r'Amplitude \(=|a|\).',
      r'Period \(=\dfrac{2\pi}{|b|}\) for sine/cosine.',
      r'Midline \(y=d\); range \([d-|a|,d+|a|]\).',
      r'Larger \(|b|\) → shorter period (more cycles).',
    ],
    'formulas': [
      r'\(y=a\sin(bx)+d\) or \(y=a\cos(bx)+d\)',
      r'Amplitude \(|a|\); period \(\dfrac{2\pi}{|b|}\); midline \(y=d\)',
      r'For tangent: \(y=a\tan(bx)\) has period \(\dfrac{\pi}{|b|}\)',
    ],
    'problems': [
      r'State amp and period of \(y=4\sin x\).',
      r'State amp and period of \(y=\sin(3x)\).',
      r'State amp and period of \(y=2\cos(2x)\).',
      r'State amp and period of \(y=-5\sin\!\left(\dfrac{x}{2}\right)\).',
      r'State amp, period and midline of \(y=3\sin x+2\).',
      r'State range of \(y=3\sin x+2\).',
      r'State amp, period, midline of \(y=\cos(4x)-1\).',
      r'Find \(b\) if \(y=\sin(bx)\) has period \(\dfrac{\pi}{2}\).',
      r'Find \(a\) if \(y=a\cos x\) has amplitude \(7\).',
      r'Write an equation with amp \(2\), period \(\pi\), midline \(0\), sine type.',
      r'Write an equation with amp \(3\), period \(4\pi\), midline \(1\), cosine type.',
      r'Period of \(y=\tan(2x)\)?',
      r'How many cycles of \(y=\sin(2x)\) occur on \([0,2\pi]\)?',
      r'Describe the transformation from \(y=\sin x\) to \(y=2\sin x-3\).',
      r'Describe the transformation from \(y=\cos x\) to \(y=\cos(3x)\).',
    ],
    'answers': [
      r'amp \(4\), period \(2\pi\).',
      r'amp \(1\), period \(\dfrac{2\pi}{3}\).',
      r'amp \(2\), period \(\pi\).',
      r'amp \(5\), period \(4\pi\).',
      r'amp \(3\), period \(2\pi\), midline \(y=2\).',
      r'\([-1,5]\).',
      r'amp \(1\), period \(\dfrac{\pi}{2}\), midline \(y=-1\).',
      r'\(b=4\).',
      r'\(a=\pm 7\) (usually \(a=7\) if unmarked).',
      r'e.g. \(y=2\sin(2x)\).',
      r'e.g. \(y=3\cos\!\left(\dfrac{x}{2}\right)+1\).',
      r'\(\dfrac{\pi}{2}\).',
      r'\(2\) cycles.',
      r'Vertical stretch ×2, shift down \(3\).',
      r'Horizontal compress by factor \(3\) (period \(\dfrac{2\pi}{3}\)).',
    ],
  },
  {
    'slug': 'w1d-set3', 'short': '1D Set 3', 'group': 'WEEK 1D · SET 3 OF 5',
    'source': 'Student Notes Week 1D (filled-in)',
    'title': 'Phase shift & full transformations',
    'blurb': r'From Week 1D: horizontal shifts / phase, and reading/writing full models \(y=a\sin(b(x-c))+d\).',
    'lesson': [
      r'A phase shift appears when the angle is \(b(x-c)\) or \(bx-c\). In the form \(a\sin(b(x-c))+d\), the graph shifts right by \(c\) if \(c\gt 0\).',
      r'If written as \(a\sin(bx-c)+d\), the phase shift is \(\dfrac{c}{b}\) (to the right if \(\dfrac{c}{b}\gt 0\)).',
      'When sketching: mark midline, amplitude envelope, period length, then place one key point using the phase shift.',
    ],
    'example': r'\(y=2\sin\!\left(3x-\dfrac{\pi}{2}\right)+1\): amp \(2\), period \(\dfrac{2\pi}{3}\), phase shift \(\dfrac{\pi}{6}\) right, midline \(y=1\).',
    'points': [
      r'Factor \(b\) out of the angle to read phase cleanly.',
      r'Right shift for \((x-c)\); left for \((x+c)\).',
      'List amp, period, phase, midline, range.',
      'Check one easy point to verify the sketch.',
    ],
    'formulas': [
      r'\(y=a\sin(b(x-c))+d\): amp \(|a|\), period \(\dfrac{2\pi}{|b|}\), phase shift \(c\), midline \(d\)',
      r'\(y=a\sin(bx-c)+d\): phase shift \(\dfrac{c}{b}\)',
      r'Range: \([d-|a|, d+|a|]\)',
    ],
    'problems': [
      r'State phase shift of \(y=\sin\!\left(x-\dfrac{\pi}{3}\right)\).',
      r'State phase shift of \(y=\cos\!\left(x+\dfrac{\pi}{4}\right)\).',
      r'For \(y=3\sin\!\left(2x-\dfrac{\pi}{2}\right)\), find amp, period, phase shift.',
      r'For \(y=2\cos\!\left(3\!\left(x-\dfrac{\pi}{6}\right)\right)\), find amp, period, phase shift.',
      r'State midline and range of \(y=4\sin(x-\pi)-1\).',
      r'Write a sine equation with amp \(5\), period \(2\pi\), shift right \(\dfrac{\pi}{2}\), midline \(0\).',
      r'Write a cosine equation with amp \(1\), period \(\pi\), shift left \(\dfrac{\pi}{4}\), midline \(2\).',
      r'Sketch description: key starting point for \(y=\sin\!\left(x-\dfrac{\pi}{2}\right)\).',
      r'Find period and phase of \(y=-\sin\!\left(4x+\pi\right)\).',
      r'Does a vertical shift change the period? Explain.',
      r'Does a phase shift change the amplitude? Explain.',
      r'Match: \(y=\cos x\) equals which phase-shifted sine?',
      r'On \([0,2\pi]\), how many peaks does \(y=\sin(3x)\) have?',
      r'Find an \(x\)-intercept of \(y=\sin\!\left(x-\dfrac{\pi}{6}\right)\) in \((0,2\pi)\).',
      r'State amp, period, phase, midline for \(y=-2\cos\!\left(2x+\dfrac{\pi}{3}\right)+5\).',
    ],
    'answers': [
      r'\(\dfrac{\pi}{3}\) right.',
      r'\(\dfrac{\pi}{4}\) left.',
      r'amp \(3\), period \(\pi\), phase \(\dfrac{\pi}{4}\) right.',
      r'amp \(2\), period \(\dfrac{2\pi}{3}\), phase \(\dfrac{\pi}{6}\) right.',
      r'midline \(y=-1\); range \([-5,3]\).',
      r'\(y=5\sin\!\left(x-\dfrac{\pi}{2}\right)\).',
      r'\(y=\cos\!\left(2\!\left(x+\dfrac{\pi}{4}\right)\right)+2\).',
      r'Like \(-\!\cos x\): at \(x=0\), \(y=-1\).',
      r'period \(\dfrac{\pi}{2}\); phase \(\dfrac{\pi}{4}\) left (from \(4\!\left(x+\dfrac{\pi}{4}\right)\)).',
      r'No — period depends on \(b\) only.',
      r'No — amplitude depends on \(|a|\) only.',
      r'\(y=\sin\!\left(x+\dfrac{\pi}{2}\right)\).',
      r'\(3\) peaks.',
      r'e.g. \(x=\dfrac{\pi}{6}\) (where argument \(0\)).',
      r'amp \(2\), period \(\pi\), phase \(\dfrac{\pi}{6}\) left, midline \(5\).',
    ],
  },
  {
      'slug': 'w1d-set4', 'short': '1D Set 4', 'group': 'WEEK 1D · SET 4 OF 5',
      'source': 'Student Notes Week 1D (filled-in)',
      'title': 'Reading features of transformed models',
      'blurb': r'From Week 1D: amplitude, period, phase and midline for multi-parameter sine and cosine models; locate max/min points.',
      'lesson': [
        r'For \(y=a\sin(b(x-c))+d\) or \(y=a\cos(bx-c)+d\), list amplitude \(|a|\), period \(\dfrac{2\pi}{|b|}\), phase shift, and midline \(y=d\) before sketching.',
        r'A maximum value is \(d+|a|\) and a minimum is \(d-|a|\). For a sine model with \(a\gt 0\), a maximum occurs when the argument equals \(\dfrac{\pi}{2}+2k\pi\); for cosine with \(a\gt 0\), when the argument is \(2k\pi\).',
        r'If the form is \(a\sin(bx-c)+d\), rewrite as \(a\sin\!\big(b\big(x-\dfrac{c}{b}\big)\big)+d\) to read the phase shift \(\dfrac{c}{b}\).',
        r'Negative \(a\) reflects the graph in the midline: maxima and minima swap roles relative to the unreflected wave.',
      ],
      'example': r'\(y=-3\cos\!\left(2x-\dfrac{\pi}{3}\right)+1\): amp \(3\), period \(\pi\), phase \(\dfrac{\pi}{6}\) right, midline \(y=1\), range \([-2,4]\). A maximum \(4\) occurs when \(\cos(\ldots)=-1\).',
      'points': [
        r'Amplitude \(|a|\); period \(\dfrac{2\pi}{|b|}\); midline \(y=d\).',
        r'Phase: factor \(b\) out of the angle.',
        r'Max \(d+|a|\); min \(d-|a|\).',
        r'Negative \(a\) reflects through the midline.',
        'State one max point and one min point when asked.',
      ],
      'formulas': [
        r'\(y=a\sin(b(x-c))+d\): amp \(|a|\), period \(\dfrac{2\pi}{|b|}\), phase \(c\), midline \(d\)',
        r'\(y=a\sin(bx-c)+d\): phase shift \(\dfrac{c}{b}\)',
        r'Range \([d-|a|,d+|a|]\)',
        r'For \(a\gt 0\): \(\sin\) max when argument \(\dfrac{\pi}{2}\); \(\cos\) max when argument \(0\)',
        r'Tangent: period \(\dfrac{\pi}{|b|}\) for \(y=a\tan(bx-c)\)',
      ],
      'problems': [
        r'For \(y=5\sin\!\left(3x-\dfrac{\pi}{2}\right)-2\), state amplitude, period, phase shift and midline.',
        r'For the model in Q1, state the range and the maximum and minimum values.',
        r'Find one \(x\)-coordinate in \([0,2\pi]\) where \(y=5\sin\!\left(3x-\dfrac{\pi}{2}\right)-2\) attains its maximum.',
        r'For \(y=-4\cos\!\left(2\!\left(x+\dfrac{\pi}{6}\right)\right)+1\), state amp, period, phase shift, midline.',
        r'Find the first positive \(x\) where the model in Q4 attains its minimum value.',
        r'For \(y=2\sin\!\left(\dfrac{x}{2}+\dfrac{\pi}{4}\right)\), rewrite in the form \(a\sin\!\big(b(x-c)\big)\) and state phase shift.',
        r'State amp, period and midline of \(y=7\cos(4x)+3\), and find max/min \(y\)-values.',
        r'For \(y=-2\sin(\pi x)+5\) (period in terms of the variable \(x\)), state amp, period, midline.',
        r'How many complete cycles of \(y=3\cos(4x)\) occur on \(0\le x\le 2\pi\)?',
        r'For \(y=\tan\!\left(2x-\dfrac{\pi}{3}\right)\), state the period and the first positive asymptote.',
        r'Compare \(y=4\sin(2x)\) and \(y=4\sin\!\left(2x-\dfrac{\pi}{2}\right)\): what is the horizontal shift from the first to the second?',
        r'For \(y=-6\cos\!\left(x-\dfrac{\pi}{3}\right)+2\), find the coordinates of a maximum point.',
        r'State amp, period, phase, midline for \(y=1.5\sin\!\left(6x+\dfrac{\pi}{2}\right)-0.5\).',
        r'Find the midline and amplitude of \(y=8-3\cos(5x)\), and explain which way the cosine is reflected.',
        r'For \(y=2\cos\!\left(3x+\dfrac{\pi}{2}\right)\), find one \(x\in[0,2\pi]\) where \(y=0\).',
      ],
      'answers': [
        r'''Rewrite \(3x-\dfrac{\pi}{2}=3\!\left(x-\dfrac{\pi}{6}\right)\).
  \[
  |a|=5,\quad\text{period }=\frac{2\pi}{3},\quad\text{phase }=\frac{\pi}{6}\text{ right},\quad\text{midline }y=-2.
  \]
  \[\boxed{\text{amp }5,\ \text{period }\dfrac{2\pi}{3},\ \text{phase }\dfrac{\pi}{6}\text{ right},\ \text{midline }y=-2}\]''',
        r'''Range is \([d-|a|,d+|a|]=[-2-5,-2+5]=[-7,3]\).
  Max \(3\), min \(-7\).
  \[\boxed{\text{range }[-7,3];\ \max 3,\ \min -7}\]''',
        r'''Maximum when \(\sin\!\left(3x-\dfrac{\pi}{2}\right)=1\), so \(3x-\dfrac{\pi}{2}=\dfrac{\pi}{2}+2k\pi\).
  For \(k=0\): \(3x=\pi\Rightarrow x=\dfrac{\pi}{3}\) (in \([0,2\pi]\)).
  \[\boxed{x=\dfrac{\pi}{3}}\]''',
        r'''Amp \(4\), period \(\dfrac{2\pi}{2}=\pi\), phase \(\dfrac{\pi}{6}\) left (from \(x+\dfrac{\pi}{6}\)), midline \(y=1\).
  \[\boxed{\text{amp }4,\ \text{period }\pi,\ \text{phase }\dfrac{\pi}{6}\text{ left},\ \text{midline }y=1}\]''',
        r'''Because of the leading minus, the cosine is reflected: the minimum of \(y\) is \(1-4=-3\), which occurs when \(\cos\!\big(2(x+\pi/6)\big)=1\).
  \[
  2\!\left(x+\frac{\pi}{6}\right)=0\Rightarrow x=-\frac{\pi}{6}.
  \]
  First positive: use \(2\!\left(x+\dfrac{\pi}{6}\right)=2\pi\Rightarrow x+\dfrac{\pi}{6}=\pi\Rightarrow x=\pi-\dfrac{\pi}{6}=\dfrac{5\pi}{6}\).
  \[\boxed{x=\dfrac{5\pi}{6}}\]''',
        r'''\[
  \frac{x}{2}+\frac{\pi}{4}=\frac12\left(x+\frac{\pi}{2}\right),
  \]
  so \(y=2\sin\!\Big(\dfrac12\big(x-(-\pi/2)\big)\Big)\): phase \(\dfrac{\pi}{2}\) left.
  \[\boxed{y=2\sin\!\big(\tfrac12(x+\pi/2)\big);\ \text{phase }\dfrac{\pi}{2}\text{ left}}\]''',
        r'''Amp \(7\), period \(\dfrac{2\pi}{4}=\dfrac{\pi}{2}\), midline \(y=3\).
  Max \(3+7=10\), min \(3-7=-4\).
  \[\boxed{\text{amp }7,\ \text{period }\dfrac{\pi}{2},\ \text{midline }3;\ \max 10,\ \min -4}\]''',
        r'''Here \(b=\pi\), so period \(\dfrac{2\pi}{\pi}=2\). Amp \(2\), midline \(y=5\).
  \[\boxed{\text{amp }2,\ \text{period }2,\ \text{midline }y=5}\]''',
        r'''Period \(\dfrac{2\pi}{4}=\dfrac{\pi}{2}\). On an interval of length \(2\pi\),
  \[
  \frac{2\pi}{\pi/2}=4
  \]
  complete cycles.
  \[\boxed{4}\]''',
        r'''Period of \(a\tan(bx-c)\) is \(\dfrac{\pi}{|b|}=\dfrac{\pi}{2}\).
  Asymptotes when \(2x-\dfrac{\pi}{3}=\dfrac{\pi}{2}+k\pi\). For the first positive:
  \[
  2x-\frac{\pi}{3}=\frac{\pi}{2}\Rightarrow 2x=\frac{\pi}{2}+\frac{\pi}{3}=\frac{5\pi}{6}\Rightarrow x=\frac{5\pi}{12}.
  \]
  \[\boxed{\text{period }\dfrac{\pi}{2};\ \text{asymptote }x=\dfrac{5\pi}{12}}\]''',
        r'''Second model: \(2x-\dfrac{\pi}{2}=2\!\left(x-\dfrac{\pi}{4}\right)\), so phase \(\dfrac{\pi}{4}\) right relative to \(y=4\sin(2x)\).
  \[\boxed{\dfrac{\pi}{4}\text{ right}}\]''',
        r'''Max value \(2+6=8\) when \(\cos\!\left(x-\dfrac{\pi}{3}\right)=-1\) (because of the leading minus).
  \[
  x-\frac{\pi}{3}=\pi\Rightarrow x=\frac{4\pi}{3}.
  \]
  Point \(\left(\dfrac{4\pi}{3},\,8\right)\).
  \[\boxed{\left(\dfrac{4\pi}{3},\,8\right)}\]''',
        r'''\(6x+\dfrac{\pi}{2}=6\!\left(x+\dfrac{\pi}{12}\right)\): amp \(1.5\), period \(\dfrac{2\pi}{6}=\dfrac{\pi}{3}\), phase \(\dfrac{\pi}{12}\) left, midline \(y=-0.5\).
  \[\boxed{\text{amp }1.5,\ \text{period }\dfrac{\pi}{3},\ \text{phase }\dfrac{\pi}{12}\text{ left},\ \text{midline }-0.5}\]''',
        r'''Write \(y=-3\cos(5x)+8\): amp \(3\), midline \(y=8\). The factor \(-3\) reflects the cosine through the midline (peaks become troughs relative to \(+3\cos(5x)+8\)).
  \[\boxed{\text{midline }8,\ \text{amp }3;\ \text{reflected cosine}}\]''',
        r'''\(2\cos\!\left(3x+\dfrac{\pi}{2}\right)=0\Rightarrow\cos\!\left(3x+\dfrac{\pi}{2}\right)=0\).
  So \(3x+\dfrac{\pi}{2}=\dfrac{\pi}{2}+k\pi\).
  For \(k=0\): \(3x=0\Rightarrow x=0\). For \(k=1\): \(3x=\pi\Rightarrow x=\dfrac{\pi}{3}\).
  \[\boxed{x=0\text{ (one valid solution; also }\dfrac{\pi}{3},\ldots\text{)}}\]''',
      ],
  },
  {
      'slug': 'w1d-set5', 'short': '1D Set 5', 'group': 'WEEK 1D · SET 5 OF 5',
      'source': 'Student Notes Week 1D (filled-in)',
      'title': 'Writing models, sketches & solving on graphs',
      'blurb': r'From Week 1D: construct sine/cosine equations from descriptions, give sketch instructions, and solve when a model equals a stated value.',
      'lesson': [
        r'To write a model from a description: read amplitude, period (hence \(b=\dfrac{2\pi}{\text{period}}\)), midline \(d\), and phase from a stated starting behaviour (e.g. sine through the midline going up, or cosine at a maximum).',
        r'Sketch instructions should name: midline, amplitude envelope, period length, phase placement of one key point, and whether the graph is sine- or cosine-shaped (or reflected).',
        r'To solve \(a\sin(bx-c)+d=k\), isolate the trig function, then solve the resulting equation on the required interval using reference angles and CAST (in radians).',
        r'More than one equation can fit the same data (e.g. a phase-shifted sine versus a cosine). Prefer the form requested by the question.',
      ],
      'example': r'Amp \(2\), period \(\pi\), midline \(1\), passes through a maximum at \(x=0\): \(y=2\cos(2x)+1\). Solve \(2\cos(2x)+1=0\) on \([0,\pi]\): \(\cos(2x)=-\dfrac12\Rightarrow 2x=\dfrac{2\pi}{3},\dfrac{4\pi}{3}\Rightarrow x=\dfrac{\pi}{3},\dfrac{2\pi}{3}\).',
      'points': [
        r'\(b=\dfrac{2\pi}{\text{period}}\) for sine/cosine.',
        'Choose sine or cosine to match a stated key point.',
        'Sketch: midline → envelope → one key point → period.',
        r'To solve \(y=k\): isolate trig, then CAST on the interval.',
        'State all solutions in the given domain.',
      ],
      'formulas': [
        r'\(y=a\sin(b(x-c))+d\) or \(y=a\cos(b(x-c))+d\)',
        r'Period \(=\dfrac{2\pi}{|b|}\Rightarrow |b|=\dfrac{2\pi}{\text{period}}\)',
        r'Solve \(a\sin(\ldots)+d=k\Rightarrow\sin(\ldots)=\dfrac{k-d}{a}\)',
        r'Range check: if \(\left|\dfrac{k-d}{a}\right|\gt 1\), no solution.',
      ],
      'problems': [
        r'Write a sine equation with amplitude \(4\), period \(\dfrac{2\pi}{3}\), phase shift \(\dfrac{\pi}{6}\) right, midline \(y=-1\).',
        r'Write a cosine equation with amplitude \(2\), period \(4\pi\), no phase shift, midline \(y=5\), reflected in the midline.',
        r'A tide height is modelled by \(h(t)=3\cos\!\left(\dfrac{\pi}{6}t\right)+7\) (metres, \(t\) in hours). State amp, period, midline, and max/min heights.',
        r'Using the model in Q3, find the first two times \(t\ge 0\) when \(h(t)=8.5\).',
        r'Write a model \(y=a\sin(bx)+d\) with range \([1,7]\) and period \(\pi\).',
        r'Describe how to sketch one full cycle of \(y=3\sin\!\left(2x-\dfrac{\pi}{2}\right)+1\) for \(x\) starting at the phase-shifted origin.',
        r'Solve \(2\sin x+1=0\) for \(0\le x\le 2\pi\).',
        r'Solve \(4\cos(2x)=2\) for \(0\le x\le\pi\).',
        r'Solve \(3\sin\!\left(x-\dfrac{\pi}{4}\right)=-\dfrac{3\sqrt2}{2}\) for \(0\le x\le 2\pi\).',
        r'Solve \(-2\cos x+3=4\) for \(0\le x\le 2\pi\).',
        r'A temperature model \(T(t)=10\sin\!\left(\dfrac{\pi}{12}t\right)+18\) (\(t\) hours after midnight). Find all \(t\in[0,24]\) with \(T(t)=23\).',
        r'Write two different equations (one sine, one cosine) for a wave with amp \(1\), period \(2\pi\), midline \(0\), maximum at \(x=\dfrac{\pi}{2}\).',
        r'Solve \(\sin(3x)=\dfrac12\) for \(0\le x\le\pi\).',
        r'Explain why \(y=2\sin x+5=1\) has no real solution, and find all solutions of \(2\sin x+5=5\) on \([0,2\pi]\).',
        r'For \(y=5\cos\!\left(x+\dfrac{\pi}{3}\right)-1\), find all \(x\in[0,2\pi]\) where \(y=1.5\).',
      ],
      'answers': [
        r'''Period \(\dfrac{2\pi}{3}\) gives \(b=3\). Phase \(\dfrac{\pi}{6}\) right:
  \[
  y=4\sin\!\left(3\!\left(x-\frac{\pi}{6}\right)\right)-1.
  \]
  \[\boxed{y=4\sin\!\big(3(x-\pi/6)\big)-1}\]''',
        r'''Period \(4\pi\) gives \(b=\dfrac12\). Reflection: negative cosine.
  \[
  y=-2\cos\!\left(\frac{x}{2}\right)+5.
  \]
  \[\boxed{y=-2\cos(x/2)+5}\]''',
        r'''Amp \(3\), period \(\dfrac{2\pi}{\pi/6}=12\) hours, midline \(y=7\).
  Max \(7+3=10\) m, min \(7-3=4\) m.
  \[\boxed{\text{amp }3,\ \text{period }12\text{ h},\ \text{midline }7;\ \max 10,\ \min 4}\]''',
        r'''\[
  3\cos\!\left(\frac{\pi}{6}t\right)+7=8.5\Rightarrow\cos\!\left(\frac{\pi}{6}t\right)=\frac12.
  \]
  Let \(\alpha=\dfrac{\pi}{6}t\). Then \(\alpha=\dfrac{\pi}{3},\dfrac{5\pi}{3},\ldots\)
  \[
  \frac{\pi}{6}t=\frac{\pi}{3}\Rightarrow t=2;\qquad
  \frac{\pi}{6}t=\frac{5\pi}{3}\Rightarrow t=10.
  \]
  \[\boxed{t=2,\ 10}\]''',
        r'''Range \([1,7]\) means midline \(\dfrac{1+7}{2}=4\) and amp \(3\). Period \(\pi\) gives \(b=2\).
  \[
  y=3\sin(2x)+4
  \]
  (or \(y=-3\sin(2x)+4\), etc.).
  \[\boxed{y=3\sin(2x)+4}\]''',
        r'''Midline \(y=1\), amplitude envelope \(1\pm 3\) i.e. \(y=-2\) and \(y=4\). Period \(\pi\).
  Rewrite \(2x-\dfrac{\pi}{2}=2\!\left(x-\dfrac{\pi}{4}\right)\): start the sine cycle at \(x=\dfrac{\pi}{4}\) where \(y=1\) and the graph is about to rise (standard sine shape after that shift). Mark key points one quarter-period apart.
  \[\boxed{\text{midline }1;\ \text{env. }[-2,4];\ \text{period }\pi;\ \text{sine start at }x=\pi/4}\]''',
        r'''\(2\sin x=-1\Rightarrow\sin x=-\dfrac12\). Q3/Q4, ref \(\dfrac{\pi}{6}\).
  \[
  x=\frac{7\pi}{6},\ \frac{11\pi}{6}.
  \]
  \[\boxed{\dfrac{7\pi}{6},\ \dfrac{11\pi}{6}}\]''',
        r'''\(\cos(2x)=\dfrac12\) with \(0\le x\le\pi\) so \(0\le 2x\le 2\pi\).
  \[
  2x=\frac{\pi}{3},\ \frac{5\pi}{3}\Rightarrow x=\frac{\pi}{6},\ \frac{5\pi}{6}.
  \]
  \[\boxed{\dfrac{\pi}{6},\ \dfrac{5\pi}{6}}\]''',
        r'''\(\sin\!\left(x-\dfrac{\pi}{4}\right)=-\dfrac{\sqrt2}{2}\). Let \(\alpha=x-\dfrac{\pi}{4}\).
  \[
  \alpha=\frac{5\pi}{4},\ \frac{7\pi}{4}
  \]
  (and check \(+\ 2\pi\) shifts stay in range for \(x\)).
  \[
  x=\frac{5\pi}{4}+\frac{\pi}{4}=\frac{6\pi}{4}=\frac{3\pi}{2};\quad
  x=\frac{7\pi}{4}+\frac{\pi}{4}=2\pi.
  \]
  Also \(\alpha=\dfrac{5\pi}{4}-2\pi=-\dfrac{3\pi}{4}\Rightarrow x=-\dfrac{3\pi}{4}+\dfrac{\pi}{4}=-\dfrac{\pi}{2}\) (outside). And \(\alpha=\dfrac{7\pi}{4}-2\pi=-\dfrac{\pi}{4}\Rightarrow x=0\).
  So \(x=0,\dfrac{3\pi}{2},2\pi\).
  \[\boxed{0,\ \dfrac{3\pi}{2},\ 2\pi}\]''',
        r'''\(-2\cos x+3=4\Rightarrow -2\cos x=1\Rightarrow\cos x=-\dfrac12\).
  \[
  x=\frac{2\pi}{3},\ \frac{4\pi}{3}.
  \]
  \[\boxed{\dfrac{2\pi}{3},\ \dfrac{4\pi}{3}}\]''',
        r'''\[
  10\sin\!\left(\frac{\pi}{12}t\right)+18=23\Rightarrow\sin\!\left(\frac{\pi}{12}t\right)=\frac12.
  \]
  Let \(\alpha=\dfrac{\pi}{12}t\) with \(0\le t\le 24\Rightarrow 0\le\alpha\le 2\pi\).
  \[
  \alpha=\frac{\pi}{6},\ \frac{5\pi}{6}\Rightarrow t=2,\ 10.
  \]
  \[\boxed{t=2,\ 10}\]''',
        r'''Maximum at \(x=\dfrac{\pi}{2}\) with amp \(1\): sine is max when argument \(\dfrac{\pi}{2}\), so \(y=\sin x\). Cosine max at argument \(0\), so shift: \(y=\cos\!\left(x-\dfrac{\pi}{2}\right)\).
  \[\boxed{y=\sin x;\ y=\cos(x-\pi/2)}\]''',
        r'''\(0\le 3x\le 3\pi\). \(\sin(3x)=\dfrac12\Rightarrow 3x=\dfrac{\pi}{6},\dfrac{5\pi}{6},\dfrac{13\pi}{6},\dfrac{17\pi}{6}\) (those \(\le 3\pi\)).
  \[
  x=\frac{\pi}{18},\ \frac{5\pi}{18},\ \frac{13\pi}{18},\ \frac{17\pi}{18}.
  \]
  \[\boxed{\dfrac{\pi}{18},\ \dfrac{5\pi}{18},\ \dfrac{13\pi}{18},\ \dfrac{17\pi}{18}}\]''',
        r'''\(2\sin x+5=1\Rightarrow\sin x=-2\), impossible since \(|\sin|\le 1\).
  \(2\sin x+5=5\Rightarrow\sin x=0\Rightarrow x=0,\pi,2\pi\) on \([0,2\pi]\).
  \[\boxed{\text{no solution for }=1;\ x=0,\pi,2\pi\text{ for }=5}\]''',
        r'''\[
  5\cos\!\left(x+\frac{\pi}{3}\right)-1=1.5\Rightarrow\cos\!\left(x+\frac{\pi}{3}\right)=\frac{2.5}{5}=\frac12.
  \]
  Let \(\alpha=x+\dfrac{\pi}{3}\). Then \(\alpha=\dfrac{\pi}{3},\dfrac{5\pi}{3}\) (and \(+\ 2\pi\)).
  \[
  x=0;\quad x=\frac{5\pi}{3}-\frac{\pi}{3}=\frac{4\pi}{3};
  \]
  also \(\alpha=\dfrac{\pi}{3}+2\pi=\dfrac{7\pi}{3}\Rightarrow x=2\pi\), and \(\alpha=\dfrac{5\pi}{3}-2\pi=-\dfrac{\pi}{3}\Rightarrow x=-\dfrac{2\pi}{3}\) (out).
  So \(x=0,\dfrac{4\pi}{3},2\pi\).
  \[\boxed{0,\ \dfrac{4\pi}{3},\ 2\pi}\]''',
      ],
  },
]}

GROUPS['2a'] = {
  'label': 'Week 2A',
  'sets': [
  {
    'slug': 'w2a-set1', 'short': '2A Set 1', 'group': 'WEEK 2A · SET 1 OF 5',
    'source': 'Student Notes Week 2A (filled-in)',
    'title': 'Pythagorean trigonometric identities',
    'blurb': r'From Week 2A: deriving and using \(\sin^2\theta+\cos^2\theta=1\) and the companion identities.',
    'lesson': [
      r'On the unit circle, \(x=\cos\theta\), \(y=\sin\theta\) and \(x^2+y^2=1\). Substituting gives the fundamental identity \(\sin^2\theta+\cos^2\theta=1\).',
      r'Divide by \(\cos^2\theta\) (where defined) to get \(1+\tan^2\theta=\sec^2\theta\). Divide by \(\sin^2\theta\) to get \(1+\cot^2\theta=\csc^2\theta\).',
      r'These identities are true for all \(\theta\) where the functions exist. Use them to rewrite expressions and find exact ratios.',
    ],
    'example': r'If \(\sin\theta=\dfrac{2}{\sqrt{29}}\) and \(\theta\) obtuse, then \(\cos\theta=-\sqrt{1-\sin^2\theta}=-\dfrac{5}{\sqrt{29}}\) (negative in Q2).',
    'points': [
      r'Primary: \(\sin^2+\cos^2=1\).',
      r'Then: \(1+\tan^2=\sec^2\) and \(1+\cot^2=\csc^2\).',
      'Choose the sign of the square root using the quadrant.',
      r'Identities hold for all valid \(\theta\), not just acute angles.',
    ],
    'formulas': [
      r'\(\sin^2\theta+\cos^2\theta=1\)',
      r'\(1+\tan^2\theta=\sec^2\theta\)',
      r'\(1+\cot^2\theta=\csc^2\theta\)',
      r'\(\cos^2\theta=1-\sin^2\theta,\quad \sin^2\theta=1-\cos^2\theta\)',
    ],
    'problems': [
      r'Show that \(\theta=30^\circ\) satisfies \(\sin^2\theta+\cos^2\theta=1\).',
      r'If \(\sin\theta=\dfrac35\) (acute), find \(\cos\theta\) and \(\tan\theta\).',
      r'If \(\cos\theta=-\dfrac{8}{17}\) and \(\theta\) is in Q2, find \(\sin\theta\).',
      r'If \(\tan\theta=\dfrac43\) (acute), find \(\sec\theta\) using an identity.',
      r'If \(\sec\theta=-\dfrac{17}{8}\) and \(\dfrac{\pi}{2}\lt \theta\lt \pi\), find \(\tan\theta\).',
      r'Simplify \(\sin^2\theta+\cos^2\theta+\tan^2\theta\) in terms of \(\sec\theta\) where possible.',
      r'Express \(\cos^2\theta\) in terms of \(\sin\theta\) only.',
      r'Express \(\sin^2\theta\) in terms of \(\cos\theta\) only.',
      r'Use \(1+\tan^2\theta=\sec^2\theta\) to find \(\sec\theta\) if \(\tan\theta=\sqrt3\) (Q1).',
      r'If \(\cot\theta=2\) (acute), find \(\csc\theta\).',
      r'True/false: \(\sin^2\theta+\cos^2\theta=1\) for \(\theta=200^\circ\).',
      r'Find \(\cos\theta\) if \(\sin\theta=-\dfrac{5}{13}\) and \(\theta\) in Q3.',
      r'Find \(\sin\theta\) if \(\cos\theta=\dfrac{12}{13}\) and \(\theta\) in Q4.',
      r'Simplify \(1-\sin^2\theta\).',
      r'Simplify \(\sec^2\theta-\tan^2\theta\).',
    ],
    'answers': [
      r'\(\left(\dfrac12\right)^2+\left(\dfrac{\sqrt3}{2}\right)^2=\dfrac14+\dfrac34=1\).',
      r'\(\cos=\dfrac45,\ \tan=\dfrac34\).',
      r'\(\sin=\dfrac{15}{17}\) (+ in Q2).',
      r'\(\sec=\dfrac53\).',
      r'\(\tan=-\dfrac{15}{8}\) (Q2: tan −).',
      r'\(1+\tan^2=\sec^2\).',
      r'\(1-\sin^2\theta\).',
      r'\(1-\cos^2\theta\).',
      r'\(\sec=2\).',
      r'\(\csc=\sqrt5\).',
      r'True.',
      r'\(\cos=-\dfrac{12}{13}\).',
      r'\(\sin=-\dfrac{5}{13}\).',
      r'\(\cos^2\theta\).',
      r'\(1\).',
    ],
  },
  {
    'slug': 'w2a-set2', 'short': '2A Set 2', 'group': 'WEEK 2A · SET 2 OF 5',
    'source': 'Student Notes Week 2A (filled-in)',
    'title': 'Simplifying & proving identities',
    'blurb': 'From Week 2A: rewrite trig expressions and prove identities by moving from one side to the other.',
    'lesson': [
      r'To simplify: expand products, factor, rewrite everything in \(\sin\) and \(\cos\), then apply Pythagorean identities.',
      'To prove an identity: start from the more complicated side and transform it into the other side. Do not move terms across the equals sign as if solving an equation.',
      r'Common moves: \(1-\sin^2=\cos^2\), factor \(\sin^2\) or \(\cos^2\), and rewrite tan/sec in sin/cos.',
    ],
    'example': r'Simplify \(\sin^4\theta+\sin^2\theta\cos^2\theta=\sin^2\theta(\sin^2\theta+\cos^2\theta)=\sin^2\theta\).',
    'points': [
      'Complicated side → simpler side.',
      r'Prefer \(\sin/\cos\) form for algebra.',
      'Factor common terms early.',
      'Quote the identity you use.',
    ],
    'formulas': [
      r'\(\tan\theta=\dfrac{\sin\theta}{\cos\theta},\ \sec\theta=\dfrac{1}{\cos\theta}\)',
      r'\((\csc\theta-1)(\csc\theta+1)=\cot^2\theta\)',
      r'Difference of squares and Pythagorean swaps are the main tools.',
    ],
    'problems': [
      r'Simplify \((\csc\theta-1)(\csc\theta+1)\).',
      r'Simplify \(\dfrac{\tan\theta}{\sec\theta}\).',
      r'Simplify \(\cos\theta\tan\theta\).',
      r'Simplify \(\sin\theta\cot\theta\).',
      r'Simplify \(\dfrac{1-\cos^2\theta}{\sin\theta}\).',
      r'Simplify \(\sec^2\theta(1-\sin^2\theta)\).',
      r'Prove \(\dfrac{1-\cos^2\theta}{\cos^2\theta}=\tan^2\theta\).',
      r'Prove \((\sec\theta-\tan\theta)(\sec\theta+\tan\theta)=1\).',
      r'Prove \(\dfrac{\sin\theta}{\csc\theta}+\dfrac{\cos\theta}{\sec\theta}=1\).',
      r'Simplify \(\dfrac{\sec^2\theta-1}{\sec^2\theta}\).',
      r'Simplify \(\sin^2\theta(\cot^2\theta+1)\).',
      r'Prove \(1+\cot^2\theta=\csc^2\theta\) starting from \(\sin^2+\cos^2=1\).',
      r'Simplify \(\dfrac{\cos\theta}{\sin\theta}+\dfrac{\sin\theta}{\cos\theta}\).',
      r'Prove \(\dfrac{\sin\theta}{1+\cos\theta}+\dfrac{1+\cos\theta}{\sin\theta}=2\csc\theta\) (optional challenge outline).',
      r'Simplify \(\tan\theta\cos\theta\csc\theta\).',
    ],
    'answers': [
      r'\(\cot^2\theta\).',
      r'\(\sin\theta\).',
      r'\(\sin\theta\).',
      r'\(\cos\theta\).',
      r'\(\sin\theta\).',
      r'\(1\).',
      r'\(\dfrac{\sin^2}{\cos^2}=\tan^2\).',
      r'\(\sec^2-\tan^2=1\).',
      r'\(\sin^2+\cos^2=1\).',
      r'\(\sin^2\theta\) (since \(\dfrac{\tan^2}{\sec^2}=\sin^2\)).',
      r'\(1\).',
      r'Divide \(\sin^2+\cos^2=1\) by \(\sin^2\).',
      r'\(\dfrac{1}{\sin\cos}=2\csc 2\theta\) or leave as \(\dfrac{\cos^2+\sin^2}{\sin\cos}=\dfrac{1}{\sin\cos}\).',
      r'Common denominator \(\sin(1+\cos)\); numerator becomes \(2(1+\cos)\) after expansion — then simplify to \(2/\sin\).',
      r'\(1\).',
    ],
  },
  {
    'slug': 'w2a-set3', 'short': '2A Set 3', 'group': 'WEEK 2A · SET 3 OF 5',
    'source': 'Student Notes Week 2A (filled-in)',
    'title': 'Equations that need identities',
    'blurb': 'From Week 2A: solve trig equations by rewriting with Pythagorean identities, then solving on a stated interval.',
    'lesson': [
      r'Some equations are not solvable until rewritten. Classic pattern: replace \(\cos^2\theta\) by \(1-\sin^2\theta\) (or vice versa) to get a quadratic in one trig function.',
      r'After rewriting, solve the quadratic for \(\sin\theta\) or \(\cos\theta\), discard impossible roots (\(|k|\gt 1\)), then find angles in the interval.',
      'Always check solutions in the original equation if you squared or used reciprocal steps.',
    ],
    'example': r'Solve \(2\sin^2\theta-\sin\theta-1=0\) on \(0^\circ\le\theta\le360^\circ\): \((2\sin\theta+1)(\sin\theta-1)=0\) → \(\sin\theta=-\dfrac12\) or \(1\) → \(\theta=90^\circ,210^\circ,330^\circ\).',
    'points': [
      'Rewrite to one trig function when possible.',
      r'Quadratic in \(\sin\) or \(\cos\) is common.',
      r'Reject roots with absolute value \(\gt 1\).',
      'Finish with the usual quadrant method.',
    ],
    'formulas': [
      r'Replace \(\cos^2=1-\sin^2\), \(\sin^2=1-\cos^2\).',
      r'Replace \(\sec^2=1+\tan^2\) when the equation is in tan/sec.',
      r'Standard quadratic formula / factoring after substitution \(u=\sin\theta\).',
    ],
    'problems': [
      r'Solve \(2\sin^2\theta-\sin\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(2\cos^2\theta+\cos\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\sin^2\theta=\dfrac34\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(2\cos^2\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\tan^2\theta=3\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\sec^2\theta=4\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(2\sin^2\theta+\sin\theta=0\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\cos^2\theta-\sin^2\theta=0\) for \(0\le\theta\le 2\pi\) (hint: \(\cos 2\theta\)).',
      r'Solve \(1+\tan^2\theta=4\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(2\sin\theta\cos\theta=\sin\theta\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\sin^2\theta-\cos\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\) (rewrite \(\sin^2\)).',
      r'Solve \(2\cos^2\theta= \cos\theta\) for \(0\le\theta\le 2\pi\).',
      r'Solve \(\cot^2\theta=1\) for \(0^\circ\le\theta\le360^\circ\), \(\theta\ne k\cdot 180^\circ\).',
      r'Solve \(3\sin^2\theta-2\sin\theta=0\) for \(0^\circ\le\theta\le360^\circ\).',
      r'Solve \(\cos 2\theta=\sin\theta\) is beyond basic Pythagorean — instead solve \(\cos^2\theta=\dfrac12\) for \(0^\circ\le\theta\le360^\circ\).',
    ],
    'answers': [
      r'\(90^\circ,210^\circ,330^\circ\).',
      r'\(60^\circ,180^\circ,300^\circ\).',
      r'\(60^\circ,120^\circ,240^\circ,300^\circ\).',
      r'\(45^\circ,135^\circ,225^\circ,315^\circ\).',
      r'\(60^\circ,120^\circ,240^\circ,300^\circ\).',
      r'\(\dfrac{\pi}{3},\dfrac{2\pi}{3},\dfrac{4\pi}{3},\dfrac{5\pi}{3}\).',
      r'\(0^\circ,180^\circ,360^\circ,210^\circ,330^\circ\).',
      r'\(\cos2\theta=0\Rightarrow\theta=\dfrac{\pi}{4},\dfrac{3\pi}{4},\dfrac{5\pi}{4},\dfrac{7\pi}{4}\).',
      r'\(\sec^2=4\Rightarrow\cos=\pm\dfrac12\Rightarrow\) same as Q6.',
      r'\(\sin\theta(2\cos\theta-1)=0\Rightarrow\sin=0\) or \(\cos=\tfrac12\Rightarrow 0^\circ,180^\circ,360^\circ,60^\circ,300^\circ\).',
      r'\(1-\cos^2-\cos-1=0\Rightarrow\cos^2+\cos=0\Rightarrow\cos(\cos+1)=0\Rightarrow\cos=0\) or \(-1\Rightarrow 90^\circ,270^\circ,180^\circ\).',
      r'\(\cos\theta(2\cos\theta-1)=0\Rightarrow \theta=\dfrac{\pi}{2},\dfrac{3\pi}{2},\dfrac{\pi}{3},\dfrac{5\pi}{3}\).',
      r'\(\tan=\pm1\Rightarrow 45^\circ,135^\circ,225^\circ,315^\circ\).',
      r'\(\sin\theta(3\sin\theta-2)=0\Rightarrow 0^\circ,180^\circ,360^\circ\) and \(\sin=\tfrac23\Rightarrow\) two more acute/obtuse solutions (~\(41.8^\circ,138.2^\circ\)).',
      r'\(\cos\theta=\pm\dfrac{\sqrt2}{2}\Rightarrow 45^\circ,135^\circ,225^\circ,315^\circ\).',
    ],
  },
  {
      'slug': 'w2a-set4', 'short': '2A Set 4', 'group': 'WEEK 2A · SET 4 OF 5',
      'source': 'Student Notes Week 2A (filled-in)',
      'title': 'Multi-step simplifying & proving',
      'blurb': 'From Week 2A: longer simplifications and proofs using Pythagorean identities, factoring, and sin/cos rewriting.',
      'lesson': [
        r'Longer proofs still move from the more complicated side to the simpler side. Rewrite tan/sec/cot/csc in \(\sin\) and \(\cos\), then apply \(\sin^2+\cos^2=1\) or the companion identities.',
        r'Factoring early often reveals a Pythagorean swap: e.g. \(\sin^2\theta(1+\cot^2\theta)=\sin^2\theta\csc^2\theta=1\).',
        r'Difference of squares is frequent: \((\sec\theta-\tan\theta)(\sec\theta+\tan\theta)=\sec^2\theta-\tan^2\theta=1\).',
        r'When both sides look messy, convert everything to \(\sin\) and \(\cos\) over a common denominator, expand the numerator, and cancel.',
      ],
      'example': r'Prove \(\dfrac{\sin\theta}{1+\cos\theta}+\dfrac{1+\cos\theta}{\sin\theta}=2\csc\theta\): common denominator \(\sin\theta(1+\cos\theta)\) gives numerator \(\sin^2\theta+(1+\cos\theta)^2=2+2\cos\theta=2(1+\cos\theta)\), which cancels to \(\dfrac{2}{\sin\theta}\).',
      'points': [
        'Complicated side → simpler side.',
        r'Rewrite in \(\sin/\cos\) when stuck.',
        'Factor and use difference of squares.',
        'Quote each Pythagorean identity you use.',
        'Check excluded values where you divide by zero.',
      ],
      'formulas': [
        r'\(\sin^2\theta+\cos^2\theta=1,\ 1+\tan^2\theta=\sec^2\theta,\ 1+\cot^2\theta=\csc^2\theta\)',
        r'\(\tan\theta=\dfrac{\sin\theta}{\cos\theta},\ \sec\theta=\dfrac{1}{\cos\theta},\ \cot\theta=\dfrac{\cos\theta}{\sin\theta},\ \csc\theta=\dfrac{1}{\sin\theta}\)',
        r'\(\sec^2\theta-\tan^2\theta=1,\ \csc^2\theta-\cot^2\theta=1\)',
        r'Common patterns: factor \(\sin^2\) or \(\cos^2\); combine fractions.',
      ],
      'problems': [
        r'Simplify \(\dfrac{1-\cos^2\theta}{1-\sin^2\theta}\).',
        r'Simplify \(\dfrac{\sec\theta}{\tan\theta}-\dfrac{\tan\theta}{\sec\theta}\).',
        r'Simplify \(\sin\theta\cos\theta\tan\theta+\sin\theta\cos\theta\cot\theta\).',
        r'Prove \(\dfrac{\cos\theta}{1-\sin\theta}-\dfrac{\cos\theta}{1+\sin\theta}=2\tan\theta\) (where defined).',
        r'Prove \((\sin\theta+\cos\theta)^2+(\sin\theta-\cos\theta)^2=2\).',
        r'Simplify \(\dfrac{\csc^2\theta-1}{\csc^2\theta}\).',
        r'Prove \(\dfrac{1+\tan^2\theta}{1+\cot^2\theta}=\tan^2\theta\).',
        r'Simplify \(\dfrac{\sin^4\theta-\cos^4\theta}{\sin^2\theta-\cos^2\theta}\).',
        r'Prove \(\sec\theta-\cos\theta=\sin\theta\tan\theta\).',
        r'Simplify \(\dfrac{1}{\sec\theta-1}+\dfrac{1}{\sec\theta+1}\) in terms of \(\cot\theta\) or \(\cos\theta\).',
        r'Prove \(\dfrac{\sin\theta}{\csc\theta}-\dfrac{\cos\theta}{\sec\theta}=\sin^2\theta-\cos^2\theta\).',
        r'Simplify \(\tan\theta+\cot\theta\) into a single fraction, then show it equals \(\dfrac{1}{\sin\theta\cos\theta}\).',
        r'Prove \(\dfrac{\cos\theta}{\sin\theta}+\dfrac{\sin\theta}{\cos\theta}=\sec\theta\csc\theta\).',
        r'Simplify \(\dfrac{\tan^2\theta}{\sec\theta+1}+\sec\theta-1\).',
        r'Prove \(\dfrac{1-\sin\theta}{\cos\theta}=\dfrac{\cos\theta}{1+\sin\theta}\) (where defined).',
      ],
      'answers': [
        r'''Numerator \(1-\cos^2\theta=\sin^2\theta\), denominator \(1-\sin^2\theta=\cos^2\theta\).
  \[
  \frac{\sin^2\theta}{\cos^2\theta}=\tan^2\theta.
  \]
  \[\boxed{\tan^2\theta}\]''',
        r'''Combine over a common denominator:
  \[
  \begin{aligned}
  \frac{\sec\theta}{\tan\theta}-\frac{\tan\theta}{\sec\theta}
  &=\frac{\sec^2\theta-\tan^2\theta}{\sec\theta\tan\theta}
  =\frac{1}{\sec\theta\tan\theta}
  =\frac{\cos^2\theta}{\sin\theta}
  =\cos\theta\cot\theta.
  \end{aligned}
  \]
  \[\boxed{\cos\theta\cot\theta}\]''',
        r'''Factor \(\sin\theta\cos\theta(\tan\theta+\cot\theta)\).
  \[
  \tan\theta+\cot\theta=\frac{\sin}{\cos}+\frac{\cos}{\sin}=\frac{\sin^2+\cos^2}{\sin\cos}=\frac{1}{\sin\cos},
  \]
  so the product is \(\sin\cos\cdot\dfrac{1}{\sin\cos}=1\).
  \[\boxed{1}\]''',
        r'''Common denominator \((1-\sin\theta)(1+\sin\theta)=1-\sin^2\theta=\cos^2\theta\).
  \[
  \begin{aligned}
  \frac{\cos}{1-\sin}-\frac{\cos}{1+\sin}
  &=\cos\cdot\frac{(1+\sin)-(1-\sin)}{\cos^2}
  =\frac{\cos\cdot 2\sin}{\cos^2}
  =\frac{2\sin}{\cos}=2\tan\theta.
  \end{aligned}
  \]
  \[\boxed{2\tan\theta\text{ (proved)}}\]''',
        r'''Expand:
  \[
  (\sin+\cos)^2+(\sin-\cos)^2=\sin^2+2\sin\cos+\cos^2+\sin^2-2\sin\cos+\cos^2=2\sin^2+2\cos^2=2.
  \]
  \[\boxed{2\text{ (proved)}}\]''',
        r'''\(\csc^2-1=\cot^2\), so
  \[
  \frac{\cot^2\theta}{\csc^2\theta}=\frac{\cos^2/\sin^2}{1/\sin^2}=\cos^2\theta.
  \]
  \[\boxed{\cos^2\theta}\]''',
        r'''Left side: \(\dfrac{\sec^2\theta}{\csc^2\theta}\) because \(1+\tan^2=\sec^2\) and \(1+\cot^2=\csc^2\).
  \[
  \frac{\sec^2}{\csc^2}=\frac{1/\cos^2}{1/\sin^2}=\frac{\sin^2}{\cos^2}=\tan^2\theta.
  \]
  \[\boxed{\tan^2\theta\text{ (proved)}}\]''',
        r'''Difference of squares: \(\sin^4-\cos^4=(\sin^2-\cos^2)(\sin^2+\cos^2)=\sin^2-\cos^2\).
  \[
  \frac{\sin^4-\cos^4}{\sin^2-\cos^2}=1
  \]
  (where \(\sin^2\neq\cos^2\)).
  \[\boxed{1}\]''',
        r'''Right side target from left:
  \[
  \sec-\cos=\frac{1}{\cos}-\cos=\frac{1-\cos^2}{\cos}=\frac{\sin^2}{\cos}=\sin\cdot\frac{\sin}{\cos}=\sin\tan.
  \]
  \[\boxed{\text{proved}}\]''',
        r'''Common denominator \(\sec^2-1=\tan^2\):
  \[
  \frac{1}{\sec-1}+\frac{1}{\sec+1}=\frac{(\sec+1)+(\sec-1)}{\sec^2-1}=\frac{2\sec}{\tan^2}.
  \]
  Also \(=\dfrac{2/\cos}{\sin^2/\cos^2}=\dfrac{2\cos}{\sin^2}=2\cot\theta\csc\theta\).
  In terms of cos: \(\dfrac{2\cos\theta}{\sin^2\theta}\).
  \[\boxed{\dfrac{2\cos\theta}{\sin^2\theta}\ \text{or}\ 2\cot\theta\csc\theta}\]''',
        r'''\(\dfrac{\sin}{\csc}=\sin^2\) and \(\dfrac{\cos}{\sec}=\cos^2\), so left side \(\sin^2-\cos^2\).
  \[\boxed{\text{proved}}\]''',
        r'''\[
  \tan+\cot=\frac{\sin}{\cos}+\frac{\cos}{\sin}=\frac{\sin^2+\cos^2}{\sin\cos}=\frac{1}{\sin\cos}.
  \]
  \[\boxed{\dfrac{1}{\sin\theta\cos\theta}}\]''',
        r'''Same calculation as Q12: \(\dfrac{\sin^2+\cos^2}{\sin\cos}=\dfrac{1}{\sin\cos}=\csc\theta\sec\theta\).
  \[\boxed{\csc\theta\sec\theta\text{ (proved)}}\]''',
        r'''Since \(\tan^2\theta=\sec^2\theta-1=(\sec\theta-1)(\sec\theta+1)\),
  \[
  \frac{\tan^2\theta}{\sec\theta+1}=\sec\theta-1,
  \]
  and therefore
  \[
  \frac{\tan^2\theta}{\sec\theta+1}+\sec\theta-1=(\sec\theta-1)+(\sec\theta-1)=2(\sec\theta-1).
  \]
  \[\boxed{2(\sec\theta-1)}\]''',
        r'''Cross-multiply check / start from left:
  \[
  \frac{1-\sin}{\cos}\cdot\frac{1+\sin}{1+\sin}=\frac{1-\sin^2}{\cos(1+\sin)}=\frac{\cos^2}{\cos(1+\sin)}=\frac{\cos}{1+\sin}.
  \]
  \[\boxed{\text{proved}}\]''',
      ],
  },
  {
      'slug': 'w2a-set5', 'short': '2A Set 5', 'group': 'WEEK 2A · SET 5 OF 5',
      'source': 'Student Notes Week 2A (filled-in)',
      'title': 'Equations needing identities',
      'blurb': 'From Week 2A: solve trig equations by rewriting with Pythagorean and double-angle-ready identities, then listing all solutions on a stated interval.',
      'lesson': [
        r'Replace \(\cos^2\theta\) by \(1-\sin^2\theta\) (or vice versa) to obtain a quadratic in one trig function. Factor or use the quadratic formula, discard impossible roots with absolute value greater than \(1\), then solve on the interval.',
        r'Equations such as \(\sin 2\theta=\cos\theta\) can be rewritten with \(\sin 2\theta=2\sin\theta\cos\theta\), then factored. Always consider the cases carefully so you do not lose solutions.',
        r'Forms in \(\tan\) and \(\sec\) often use \(1+\tan^2=\sec^2\). Forms with a product \(\sin\theta\cos\theta\) suggest \(\sin 2\theta\).',
        r'Finish every question by listing all solutions in the given degree or radian interval, using CAST and reference angles.',
      ],
      'example': r'Solve \(2\cos^2\theta+\cos\theta-1=0\) on \(0^\circ\le\theta\le360^\circ\): \((2\cos\theta-1)(\cos\theta+1)=0\Rightarrow\cos\theta=\dfrac12\) or \(-1\Rightarrow\theta=60^\circ,300^\circ,180^\circ\).',
      'points': [
        'Rewrite to one trig function when possible.',
        r'Reject \(|u|\gt 1\) after substituting \(u=\sin\theta\) or \(\cos\theta\).',
        'Factor products; do not cancel trig factors without checking zeros.',
        r'Use \(\sin 2\theta=2\sin\theta\cos\theta\) when a double angle helps.',
        'State every solution in the interval.',
      ],
      'formulas': [
        r'\(\cos^2\theta=1-\sin^2\theta,\ \sin^2\theta=1-\cos^2\theta\)',
        r'\(1+\tan^2\theta=\sec^2\theta\)',
        r'\(\sin 2\theta=2\sin\theta\cos\theta,\ \cos 2\theta=\cos^2\theta-\sin^2\theta=2\cos^2\theta-1=1-2\sin^2\theta\)',
        r'Quadratic in \(u=\sin\theta\) or \(\cos\theta\), then CAST.',
      ],
      'problems': [
        r'Solve \(2\sin^2\theta+\sin\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(2\cos^2\theta-3\cos\theta+1=0\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(\sin^2\theta+\sin\theta=0\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(4\cos^2\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(\tan^2\theta-\tan\theta=0\) for \(0^\circ\le\theta\le360^\circ\), \(\theta\neq 90^\circ,270^\circ\).',
        r'Solve \(1+\tan^2\theta=2\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(2\sin\theta\cos\theta=\cos\theta\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(\sin 2\theta=\sin\theta\) for \(0\le\theta\le 2\pi\).',
        r'Solve \(\cos 2\theta=\cos\theta\) for \(0^\circ\le\theta\le360^\circ\) (use a double-angle expansion).',
        r'Solve \(2\cos^2\theta+\sin\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\) (rewrite \(\cos^2\)).',
        r'Solve \(\tan^2\theta+\tan\theta-2=0\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(2\sin^2\theta=\sin 2\theta\) for \(0\le\theta\le\pi\).',
        r'Solve \(\cos^2\theta=\dfrac34\) for \(0^\circ\le\theta\le360^\circ\).',
        r'Solve \(\sin 2\theta=-\dfrac{\sqrt3}{2}\) for \(0^\circ\le\theta\le180^\circ\).',
        r'Solve \(\cos 2\theta+3\sin\theta-2=0\) for \(0^\circ\le\theta\le360^\circ\) (expand \(\cos 2\theta\) in terms of \(\sin\theta\)).',
      ],
      'answers': [
        r'''Factor: \((2\sin\theta-1)(\sin\theta+1)=0\).
  \[
  \sin\theta=\frac12\quad\text{or}\quad\sin\theta=-1.
  \]
  \[
  \sin=\tfrac12\Rightarrow\theta=30^\circ,150^\circ;\quad\sin=-1\Rightarrow\theta=270^\circ.
  \]
  \[\boxed{30^\circ,\ 150^\circ,\ 270^\circ}\]''',
        r'''\((2\cos\theta-1)(\cos\theta-1)=0\).
  \[
  \cos\theta=\frac12\Rightarrow\theta=60^\circ,300^\circ;\quad\cos\theta=1\Rightarrow\theta=0^\circ,360^\circ.
  \]
  \[\boxed{0^\circ,\ 60^\circ,\ 300^\circ,\ 360^\circ}\]''',
        r'''\(\sin\theta(\sin\theta+1)=0\).
  \[
  \sin\theta=0\Rightarrow\theta=0,\pi,2\pi;\quad\sin\theta=-1\Rightarrow\theta=\frac{3\pi}{2}.
  \]
  \[\boxed{0,\ \pi,\ \dfrac{3\pi}{2},\ 2\pi}\]''',
        r'''\(\cos^2\theta=\dfrac14\Rightarrow\cos\theta=\pm\dfrac12\).
  \[
  \cos=\tfrac12\Rightarrow 60^\circ,300^\circ;\quad\cos=-\tfrac12\Rightarrow 120^\circ,240^\circ.
  \]
  \[\boxed{60^\circ,\ 120^\circ,\ 240^\circ,\ 300^\circ}\]''',
        r'''\(\tan\theta(\tan\theta-1)=0\).
  \[
  \tan\theta=0\Rightarrow\theta=0^\circ,180^\circ,360^\circ;\quad\tan\theta=1\Rightarrow\theta=45^\circ,225^\circ.
  \]
  \[\boxed{0^\circ,\ 45^\circ,\ 180^\circ,\ 225^\circ,\ 360^\circ}\]''',
        r'''\(\sec^2\theta=2\Rightarrow\cos\theta=\pm\dfrac{1}{\sqrt2}=\pm\dfrac{\sqrt2}{2}\).
  \[
  \theta=\frac{\pi}{4},\ \frac{3\pi}{4},\ \frac{5\pi}{4},\ \frac{7\pi}{4}.
  \]
  \[\boxed{\dfrac{\pi}{4},\ \dfrac{3\pi}{4},\ \dfrac{5\pi}{4},\ \dfrac{7\pi}{4}}\]''',
        r'''\(\cos\theta(2\sin\theta-1)=0\).
  \[
  \cos\theta=0\Rightarrow\theta=90^\circ,270^\circ;\quad\sin\theta=\tfrac12\Rightarrow\theta=30^\circ,150^\circ.
  \]
  \[\boxed{30^\circ,\ 90^\circ,\ 150^\circ,\ 270^\circ}\]''',
        r'''\(2\sin\theta\cos\theta-\sin\theta=0\Rightarrow\sin\theta(2\cos\theta-1)=0\).
  \[
  \sin\theta=0\Rightarrow\theta=0,\pi,2\pi;\quad\cos\theta=\tfrac12\Rightarrow\theta=\frac{\pi}{3},\frac{5\pi}{3}.
  \]
  \[\boxed{0,\ \dfrac{\pi}{3},\ \pi,\ \dfrac{5\pi}{3},\ 2\pi}\]''',
        r'''Use \(\cos 2\theta=2\cos^2\theta-1\): \(2\cos^2\theta-1=\cos\theta\Rightarrow 2\cos^2\theta-\cos\theta-1=0\).
  \[
  (2\cos\theta+1)(\cos\theta-1)=0\Rightarrow\cos\theta=-\tfrac12\text{ or }1.
  \]
  \[
  \cos=1\Rightarrow 0^\circ,360^\circ;\quad\cos=-\tfrac12\Rightarrow 120^\circ,240^\circ.
  \]
  \[\boxed{0^\circ,\ 120^\circ,\ 240^\circ,\ 360^\circ}\]''',
        r'''\(2(1-\sin^2\theta)+\sin\theta-1=0\Rightarrow -2\sin^2\theta+\sin\theta+1=0\Rightarrow 2\sin^2\theta-\sin\theta-1=0\).
  \[
  (2\sin\theta+1)(\sin\theta-1)=0\Rightarrow\sin\theta=-\tfrac12\text{ or }1.
  \]
  \[
  \sin=1\Rightarrow 90^\circ;\quad\sin=-\tfrac12\Rightarrow 210^\circ,330^\circ.
  \]
  \[\boxed{90^\circ,\ 210^\circ,\ 330^\circ}\]''',
        r'''Let \(u=\tan\theta\). Then \(u^2+u-2=0\Rightarrow(u+2)(u-1)=0\).
  \[
  \tan\theta=1\quad\text{or}\quad\tan\theta=-2.
  \]
  \[
  \tan\theta=1\Rightarrow\theta=45^\circ,225^\circ.
  \]
  For \(\tan\theta=-2\), reference \(\alpha=\tan^{-1}2\) (acute). Tan is negative in Q2 and Q4:
  \[
  \theta=180^\circ-\alpha,\quad 360^\circ-\alpha
  \]
  with \(\alpha=\tan^{-1}2\approx 63.43^\circ\), so \(\theta\approx 116.57^\circ,\ 296.57^\circ\).
  \[\boxed{45^\circ,\ 225^\circ,\ 180^\circ-\tan^{-1}2,\ 360^\circ-\tan^{-1}2}\]''',
        r'''\(2\sin^2\theta=2\sin\theta\cos\theta\Rightarrow 2\sin\theta(\sin\theta-\cos\theta)=0\).
  \[
  \sin\theta=0\Rightarrow\theta=0,\pi;\quad\sin\theta=\cos\theta\Rightarrow\tan\theta=1\Rightarrow\theta=\frac{\pi}{4}.
  \]
  (Within \(0\le\theta\le\pi\); \(\theta=\dfrac{5\pi}{4}\) is outside.)
  \[\boxed{0,\ \dfrac{\pi}{4},\ \pi}\]''',
        r'''\(\cos\theta=\pm\dfrac{\sqrt3}{2}\).
  \[
  \cos=\tfrac{\sqrt3}{2}\Rightarrow 30^\circ,330^\circ;\quad\cos=-\tfrac{\sqrt3}{2}\Rightarrow 150^\circ,210^\circ.
  \]
  \[\boxed{30^\circ,\ 150^\circ,\ 210^\circ,\ 330^\circ}\]''',
        r'''\(\sin 2\theta=-\dfrac{\sqrt3}{2}\) with \(0^\circ\le\theta\le180^\circ\Rightarrow 0^\circ\le 2\theta\le360^\circ\).
  \[
  2\theta=240^\circ,300^\circ\Rightarrow\theta=120^\circ,150^\circ.
  \]
  \[\boxed{120^\circ,\ 150^\circ}\]''',
        r'''Use \(\cos 2\theta=1-2\sin^2\theta\):
  \[
  1-2\sin^2\theta+3\sin\theta-2=0\Rightarrow -2\sin^2\theta+3\sin\theta-1=0\Rightarrow 2\sin^2\theta-3\sin\theta+1=0.
  \]
  \[
  (2\sin\theta-1)(\sin\theta-1)=0\Rightarrow\sin\theta=\tfrac12\text{ or }1.
  \]
  \[
  \sin=\tfrac12\Rightarrow 30^\circ,150^\circ;\quad\sin=1\Rightarrow 90^\circ.
  \]
  \[\boxed{30^\circ,\ 90^\circ,\ 150^\circ}\]''',
      ],
  },
]}


def write_hub():
    cards = []
    for key, g in GROUPS.items():
        links = ''.join(
            f'<a class="chip" href="{s["slug"]}.html">{s["short"]}: {H.escape(s["title"])}</a>'
            f'<a class="chip on" href="{s["slug"]}-answers.html">{s["short"]} answers</a>'
            for s in g['sets']
        )
        cards.append(f'''<div class="summary" style="margin-bottom:16px;">
<h3 style="margin-top:0;">{H.escape(g["label"])} — 5 sets</h3>
<p class="sub" style="margin:0 0 10px;">Each set: short lesson · key points · formulas/identities · 15 problems, with answers on a separate page</p>
<div class="chiprow">{links}</div>
</div>''')
    body = f'''
<div class="eyebrow">DPEN022 Trigonometry</div>
<span class="tag">LESSON SETS</span>
<h1>Trig lesson packs from Weeks 1A–2A</h1>
<p class="sub">Built from the filled-in student notes: Weeks <strong>1A + 1B</strong> (5 sets), then <strong>1C</strong>, <strong>1D</strong> and <strong>2A</strong> (5 sets each).</p>
<div class="nav">
  <a href="../../index.html">← Class notes hub</a>
  <a href="../../../index.html">DPEN22 home</a>
  <a href="../../tests/trig-questions.html">Trig practice tests</a>
</div>
{''.join(cards)}
'''
    (OUT / 'index.html').write_text(page('DPEN022 Trig Lesson Sets', body))


def main():
    for g in GROUPS.values():
        for s in g['sets']:
            set_page(s, g['sets'])
            print('wrote', s['slug'])
    write_hub()
    print('hub written to', OUT)


if __name__ == '__main__':
    main()
