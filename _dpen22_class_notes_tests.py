#!/usr/bin/env python3
"""Generate DPEN022 Class Notes hub + practice tests per strand (with answers)."""
from pathlib import Path
import html as H
import math
from _dpen22_lesson_kit import escape_math_brackets
from _figkit_exam import (
    limit_removable, limit_jump, limit_one_sided, area_under, area_between,
)
from _figkit_trig import pi_label, plot as trig_plot

BASE = Path(__file__).resolve().parent / 'siddharth' / 'dpen22' / 'class-notes'
TESTS = BASE / 'tests'
TESTS.mkdir(parents=True, exist_ok=True)

CSS = """
body{font-family:Georgia,"Times New Roman",serif;background:#f8fafc;color:#1f2937;margin:0;}
.wrap{max-width:980px;margin:24px auto;background:#fff;border:1px solid #d1d5db;padding:24px 28px 40px;}
h1,h2,h3{color:#1B3A5C;margin:0 0 10px;}
.sub{color:#4b5563;line-height:1.6;margin:8px 0 14px;}
.meta{background:#eef6ff;border-left:4px solid #185FA5;padding:10px 12px;margin:10px 0 16px;font-size:14px;}
.test{border:1px solid #d1d5db;border-radius:8px;padding:14px 16px;margin:16px 0;}
.mc{margin:6px 0 6px 18px;color:#374151;}
ol>li{margin:10px 0;line-height:1.65;}
.top-links a{margin-right:12px;text-decoration:none;color:#185FA5;font-weight:600;}
.ans{background:#f0fdf4;border-left:4px solid #15803d;padding:10px 12px;margin:8px 0 14px;overflow-x:auto;}
.katex-display{overflow-x:auto;overflow-y:hidden;padding-bottom:2px;}
@media(max-width:520px){.ans .katex{font-size:.92em;}}
.mark{color:#6b7280;font-size:13px;}
.paper-rules{background:#f8fafc;border:1px solid #cbd5e1;border-radius:6px;padding:10px 14px;margin:10px 0 16px;font-size:14px;}
.paper-rules ul{margin:6px 0 0 20px;padding:0;}
.paper-rules li{margin:3px 0;}
.part-title{margin:16px 0 6px;color:#1B3A5C;font-size:16px;border-bottom:1px solid #d1d5db;padding-bottom:5px;}
.question-mark{display:block;text-align:right;color:#4b5563;font-size:13px;font-weight:600;margin-top:4px;}
.fig{margin:8px 0 4px;}
"""

def page(title, body, katex=True):
    kx = ''
    if katex:
        kx = '''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\\\[',right:'\\\\]',display:true},{left:'\\\\(',right:'\\\\)',display:false}]});"></script>'''
    rendered = f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(title)}</title>
{kx}
<style>{CSS}</style>
</head><body><div class="wrap">
{body}
</div></body></html>
'''
    # Python source uses \' inside single-quoted raw strings; KaTeX needs a plain
    # apostrophe for derivatives and arcminutes.
    return escape_math_brackets(rendered.replace("\\'", "'"))


def write_pair(slug, subject, timing, sample_href, tests_q, tests_a, fmt):
    """fmt keys: total, mc, long_marks, mc_label, long_label, rules"""
    total = fmt['total']
    n_mc = fmt['mc']
    long_marks = fmt['long_marks']
    diagram_copy = (
        'Required given diagrams and graph-sketching axes are provided.'
        if slug == 'trig'
        else 'Diagrams are provided where the sample uses graphs.'
    )
    extra_question_links = {
        'trig': (
            '  <a href="trig-identity-sheet.html">Identity Sheet</a>\n'
            '  <a href="trig-identity-proofs-questions.html">Identity Proof Tests (11 × 10)</a>\n'
        ),
        'limits-diff': (
            '  <a href="differentiation-focused-questions.html">Focused Differentiation Questions</a>\n'
            '  <a href="differentiation-focused-answers.html">Focused Worked Answers</a>\n'
        ),
        'integration': (
            '  <a href="integration-focused-questions.html">Focused Integration Questions</a>\n'
            '  <a href="integration-focused-answers.html">Focused Worked Answers</a>\n'
        ),
    }.get(slug, '')
    extra_answer_links = {
        'trig': (
            '  <a href="trig-identity-sheet.html">Identity Sheet</a>\n'
            '  <a href="trig-identity-proofs-answers.html">Identity Proofs — Worked Answers</a>\n'
        ),
        'limits-diff': extra_question_links,
        'integration': extra_question_links,
    }.get(slug, '')
    assert n_mc + len(long_marks) == total
    q_blocks = []
    for i, qs in enumerate(tests_q, 1):
        assert len(qs) == total, f'{slug} test {i}: expected {total} questions, got {len(qs)}'
        assert all(isinstance(q, tuple) for q in qs[:n_mc])
        assert all(isinstance(q, str) for q in qs[n_mc:])
        mc_items = []
        for stem, choices in qs[:n_mc]:
            ch = ''.join(f'<div class="mc">{c}</div>' for c in choices)
            mc_items.append(f'<li>{stem}{ch}</li>')
        long_items = [
            f'<li>{q}<span class="question-mark">[{mark} mark{"s" if mark != 1 else ""}]</span></li>'
            for q, mark in zip(qs[n_mc:], long_marks)
        ]
        long_start = n_mc + 1
        q_blocks.append(
            f'<div class="test"><h3>Test {i}</h3>{fmt["rules"]}'
            f'<h4 class="part-title">{fmt["mc_label"]}</h4><ol>\n'
            + '\n'.join(mc_items)
            + f'\n</ol><h4 class="part-title">{fmt["long_label"]}</h4><ol start="{long_start}">\n'
            + '\n'.join(long_items) + '\n</ol></div>'
        )

    q_body = f'''
<h1>DPEN022 {H.escape(subject)} — Practice Tests (Questions)</h1>
<p class="sub">{len(tests_q)} practice papers modelled on the official DPEN022 {H.escape(subject)} Exam Sample.
Timing guide: {timing}. Show full working on long-answer items. {diagram_copy}</p>
<div class="meta"><strong>Official sample:</strong> <a href="{sample_href}">open PDF</a> · use it as the style/difficulty reference for these papers.</div>
<div class="top-links">
  <a href="{slug}-answers.html">Open Separate Answers</a>
{extra_question_links.rstrip()}
  <a href="../index.html">Class Notes Hub</a>
  <a href="../../index.html">DPEN22 Index</a>
</div>
{''.join(q_blocks)}
'''
    (TESTS / f'{slug}-questions.html').write_text(page(f'DPEN022 {subject} Practice Tests — Questions', q_body))

    a_blocks = []
    for i, ans in enumerate(tests_a, 1):
        assert len(ans) == total, f'{slug} answers test {i}: expected {total}, got {len(ans)}'
        items = []
        for j, a in enumerate(ans, 1):
            items.append(f'<div class="ans"><strong>Q{j}.</strong> {a}</div>')
        a_blocks.append(f'<div class="test"><h3>Test {i} — Answers</h3>\n' + '\n'.join(items) + '\n</div>')

    a_body = f'''
<h1>DPEN022 {H.escape(subject)} — Practice Tests (Answers)</h1>
<p class="sub">Separate worked answers for the {len(tests_a)} {H.escape(subject)} practice papers.</p>
<div class="top-links">
  <a href="{slug}-questions.html">Back to Questions</a>
{extra_answer_links.rstrip()}
  <a href="../index.html">Class Notes Hub</a>
  <a href="../../index.html">DPEN22 Index</a>
</div>
{''.join(a_blocks)}
'''
    answer_path = TESTS / f'{slug}-answers.html'
    # The limits/differentiation page has hand-expanded worked solutions for
    # Tests 1–6. Keep those and regenerate only the extension papers.
    if slug == 'limits-diff' and answer_path.exists():
        existing = answer_path.read_text()
        if "<span class='rule'>" in existing:
            first_extension = existing.find('<div class="test"><h3>Test 7')
            close = existing.rfind('</div></body></html>')
            cut = first_extension if first_extension >= 0 else close
            preserved = existing[:cut]
            preserved = preserved.replace(
                'all 6 practice papers (108 questions)',
                f'all {len(tests_a)} practice papers ({len(tests_a) * total} questions)',
            )
            extension = ''.join(a_blocks[6:]).replace(' — Answers</h3>', ' — Worked Solutions</h3>')
            answer_path.write_text(preserved + extension + '\n</div></body></html>\n')
        else:
            answer_path.write_text(page(f'DPEN022 {subject} Practice Tests — Answers', a_body))
    else:
        answer_path.write_text(page(f'DPEN022 {subject} Practice Tests — Answers', a_body))


TRIG_FMT = {
    'total': 15,
    'mc': 6,
    'long_marks': [2, 3, 2, 2, 3, 3, 3, 3, 3],
    'mc_label': 'Questions 1–6: Multiple choice',
    'long_label': 'Questions 7–15: Long answer',
    'rules': '''<div class="paper-rules"><strong>Total number of questions: 15</strong>
<ul><li>Questions 1–6 are multiple choice. Each question is worth 1 mark; marks are awarded for the answer only.</li>
<li>Questions 7–15 are long-answer questions. The value of each question is indicated; show all working.</li></ul></div>''',
}

DIFF_FMT = {
    'total': 18,
    'mc': 6,
    'long_marks': [1, 4, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    'mc_label': 'Questions 1–6: Multiple choice',
    'long_label': 'Questions 7–18: Long answer',
    'rules': '''<div class="paper-rules"><strong>Total number of questions: 18</strong>
<ul><li>Questions 1–6 are multiple choice. Each question is worth 1 mark; marks are awarded for the answer only.</li>
<li>Questions 7–18 are long-answer questions. The value of each question is indicated; show all working.</li></ul></div>''',
}

INT_FMT = {
    'total': 16,
    'mc': 6,
    'long_marks': [2, 2, 2, 3, 4, 3, 2, 4, 4, 3],
    'mc_label': 'Questions 1–6: Multiple choice',
    'long_label': 'Questions 7–16: Long answer',
    'rules': '''<div class="paper-rules"><strong>Total number of questions: 16</strong>
<ul><li>Questions 1–6 are multiple choice. Each question is worth 1 mark; marks are awarded for the answer only.</li>
<li>Questions 7–16 are long-answer questions. The value of each question is indicated; show all working.</li></ul></div>''',
}

# ---------- TRIG (6 tests x 15) ----------
# Sample distribution:
# MC1 right-triangle side, MC2 reference angle, MC3 quadrant, MC4 rad<->deg,
# MC5 transformations, MC6 simplify identity
# L7(2) angle nearest minute, L8(3) exact sec/tan from ratio+diagram,
# L9(2) co-function solve for x, L10(2) exact special value,
# L11(3) solve degrees, L12(3) solve radians, L13(3) sketch amp/period,
# L14(3) prove identity, L15(3) solve trig equation

def _svg_text(x, y, text, *, anchor='middle', size=15, weight='normal', fill='#1f2937'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Georgia,serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}">{H.escape(text)}</text>')


def right_triangle_svg(horizontal, vertical, hypotenuse, angle, *,
                       caption='Right-triangle diagram', context='', vertices=None,
                       answer_prompt=''):
    """Labelled right triangle used by the given Q1 diagrams and acute Q8 answers."""
    labels = [
        _svg_text(210, 235, horizontal) if horizontal else '',
        _svg_text(372, 136, vertical, anchor='start') if vertical else '',
        _svg_text(195, 120, hypotenuse, anchor='end') if hypotenuse else '',
        _svg_text(108, 198, angle, size=14, fill='#185FA5') if angle else '',
        _svg_text(22, 25, caption, anchor='start', size=15, weight='bold', fill='#1B3A5C'),
    ]
    if context:
        labels.append(_svg_text(22, 252, context, anchor='start', size=12, fill='#6b7280'))
    if answer_prompt:
        labels.append(_svg_text(225, 52, answer_prompt, size=14, weight='bold', fill='#15803d'))
    if vertices:
        a, b, c = vertices
        labels.extend([
            _svg_text(58, 226, a, anchor='end', weight='bold'),
            _svg_text(362, 48, b, anchor='start', weight='bold'),
            _svg_text(362, 226, c, anchor='start', weight='bold'),
        ])
    return f'''<div class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 270"
 role="img" aria-label="{H.escape(caption)}" style="width:100%;max-width:520px;height:auto;background:#fff;border:1px solid #d8dee7;border-radius:8px">
<line x1="70" y1="210" x2="350" y2="210" stroke="#1B3A5C" stroke-width="3"/>
<line x1="350" y1="210" x2="350" y2="55" stroke="#1B3A5C" stroke-width="3"/>
<line x1="70" y1="210" x2="350" y2="55" stroke="#185FA5" stroke-width="3"/>
<path d="M 330 210 L 330 190 L 350 190" fill="none" stroke="#1B3A5C" stroke-width="2"/>
<path d="M 111 210 A 41 41 0 0 0 106 190" fill="none" stroke="#185FA5" stroke-width="2"/>
{''.join(labels)}</svg></div>'''


def q2_reference_triangle_svg():
    """Accurate quadrant-II reference triangle; theta is a standard-position angle."""
    return f'''<div class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300"
 role="img" aria-label="Quadrant two reference triangle for sine twelve thirteenths"
 style="width:100%;max-width:560px;height:auto;background:#fff;border:1px solid #d8dee7;border-radius:8px">
{_svg_text(22, 25, 'QII reference triangle', anchor='start', size=15, weight='bold', fill='#1B3A5C')}
<line x1="35" y1="235" x2="450" y2="235" stroke="#1f2937" stroke-width="2"/>
<line x1="270" y1="275" x2="270" y2="42" stroke="#1f2937" stroke-width="2"/>
{_svg_text(454, 230, 'x', anchor='start')}{_svg_text(280, 48, 'y', anchor='start')}
<line x1="270" y1="235" x2="155" y2="75" stroke="#185FA5" stroke-width="3"/>
<line x1="155" y1="75" x2="155" y2="235" stroke="#1B3A5C" stroke-width="3"/>
<line x1="155" y1="235" x2="270" y2="235" stroke="#1B3A5C" stroke-width="3"/>
<path d="M 175 235 L 175 215 L 155 215" fill="none" stroke="#1B3A5C" stroke-width="2"/>
<path d="M 323 235 A 53 53 0 0 0 239 192" fill="none" stroke="#c2410c" stroke-width="2.5"/>
{_svg_text(316, 190, 'θ (obtuse)', anchor='start', fill='#c2410c', weight='bold')}
{_svg_text(205, 143, 'r = 13', anchor='end', fill='#185FA5')}
{_svg_text(145, 158, 'y = 12', anchor='end')}
{_svg_text(212, 257, 'x = −5')}
{_svg_text(150, 62, '(−5, 12)', anchor='end', size=13, fill='#15803d')}
</svg></div>'''


def blank_trig_grid(xmin, xmax, xticks, *, caption):
    """Blank labelled axes for a student's Q13 graph sketch."""
    width, height = 640, 300
    left, right, top, bottom = 58, 28, 38, 52
    pw, ph = width - left - right, height - top - bottom
    sx = lambda x: left + (x - xmin) / (xmax - xmin) * pw
    axis_y = top + ph / 2
    parts = [f'''<div class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}"
 role="img" aria-label="{H.escape(caption)} blank graphing axes"
 style="width:100%;max-width:660px;height:auto;background:#fff;border:1px solid #d8dee7;border-radius:8px">
{_svg_text(left, 24, caption, anchor='start', size=15, weight='bold', fill='#1B3A5C')}''']
    for i in range(9):
        y = top + i * ph / 8
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left+pw}" y2="{y:.1f}" stroke="#e5e7eb"/>')
    for x in xticks:
        px = sx(x)
        parts.append(f'<line x1="{px:.1f}" y1="{top}" x2="{px:.1f}" y2="{top+ph}" stroke="#e5e7eb"/>')
        parts.append(f'<line x1="{px:.1f}" y1="{axis_y-4}" x2="{px:.1f}" y2="{axis_y+4}" stroke="#1f2937"/>')
        parts.append(_svg_text(round(px, 1), height - 22, pi_label(x), size=12))
    parts.extend([
        f'<line x1="{left}" y1="{axis_y}" x2="{left+pw}" y2="{axis_y}" stroke="#1f2937" stroke-width="1.7"/>',
        f'<line x1="{sx(0):.1f}" y1="{top}" x2="{sx(0):.1f}" y2="{top+ph}" stroke="#1f2937" stroke-width="1.7"/>',
        _svg_text(left + pw + 5, axis_y - 7, 'x', anchor='start'),
        _svg_text(sx(0) + 9, top + 12, 'y', anchor='start'),
        '</svg></div>',
    ])
    return ''.join(parts)


trig_q = [
[
 (r'In a right triangle, adjacent side \(5\) m and angle \(13^\circ45\'\). Find the hypotenuse correct to 2 d.p.',
  ['(A) \(1.19\) m','(B) \(5.15\) m','(C) \(21.04\) m','(D) \(4.86\) m','(E) \(20.43\) m']),
 (r'What is the reference angle for \(\theta=-135^\circ\)?',
  ['(A) \(135^\circ\)','(B) \(225^\circ\)','(C) \(315^\circ\)','(D) \(45^\circ\)','(E) \(90^\circ\)']),
 (r'If \(\sec\theta<0\) and \(\cot\theta>0\), which quadrant contains \(\theta\)?',
  ['(A) 1','(B) 2','(C) 3','(D) 4','(E) none']),
 (r'Convert \(\dfrac{11\pi}{12}\) to degrees.',
  ['(A) \(165^\circ\)','(B) \(195^\circ\)','(C) \(150^\circ\)','(D) \(135^\circ\)','(E) \(15^\circ\)']),
 (r'Starting from \(y=\cos x\): amplitude \(3\), period \(4\pi\), shift down \(2\). The equation is',
  [r'(A) \(3\cos(4\pi x)-2\)',r'(B) \(3\cos\!\left(\dfrac{x}{2}\right)-2\)',r'(C) \(3\cos(2x)-2\)',r'(D) \(2\cos(4\pi x)-3\)',r'(E) \(2\cos(3x)-2\)']),
 (r'Simplify \((1-\sin^2 x)\sec^2 x\).',
  [r'(A) \(\cos^2 x\)',r'(B) \(0\)',r'(C) \(1\)',r'(D) \(\tan^2 x\)',r'(E) \(\sec^2 x\)']),
 r'Hypotenuse \(15\) m, adjacent \(7\) m. Find the included angle to the nearest minute.',
 r'If \(\sin\theta=\dfrac{3}{5}\) and \(\theta\) is acute: (i) draw a diagram; (ii) find the exact value of \(\sec\theta\).',
 r'Find \(x\) if \(\sin 80^\circ=\cos(90^\circ-2x)\).',
 r'Find the exact value of \(\tan\dfrac{2\pi}{3}\).',
 r'Solve \(\cos\theta=\dfrac{1}{2}\) for \(0^\circ\le\theta\le360^\circ\). Give exact answers in degrees.',
 r'Solve \(\cot\theta=\sqrt{3}\) for \(0\le\theta\le2\pi\). Give exact answers in radians.',
 r'Sketch \(y=\dfrac12\sin 2x\) for \(-\pi\le x\le\pi\) and state its amplitude and period.',
 r'Prove \(\sin 2\theta=2\sin\theta\cos\theta\).',
 r'Solve \(2\sin^2 x-\cos 2x=2\) for \(0^\circ\le x\le360^\circ\). Give exact answers in degrees.',
],
[
 (r'Adjacent \(8\) m, angle \(22^\circ\). Find the opposite side to 2 d.p.',
  ['(A) \(3.23\) m','(B) \(7.42\) m','(C) \(21.20\) m','(D) \(8.64\) m','(E) \(19.80\) m']),
 (r'Reference angle for \(\theta=210^\circ\)?',
  ['(A) \(30^\circ\)','(B) \(60^\circ\)','(C) \(150^\circ\)','(D) \(210^\circ\)','(E) \(45^\circ\)']),
 (r'If \(\sin\theta>0\) and \(\tan\theta<0\), \(\theta\) lies in quadrant',
  ['(A) 1','(B) 2','(C) 3','(D) 4','(E) none']),
 (r'Convert \(240^\circ\) to radians (exact).',
  [r'(A) \(\dfrac{2\pi}{3}\)',r'(B) \(\dfrac{4\pi}{3}\)',r'(C) \(\dfrac{5\pi}{6}\)',r'(D) \(\dfrac{3\pi}{4}\)',r'(E) \(\pi\)']),
 (r'\(y=\sin x\) stretched to amplitude \(2\), period \(\pi\), up \(1\):',
  [r'(A) \(2\sin(2x)+1\)',r'(B) \(2\sin\!\left(\dfrac{x}{2}\right)+1\)',r'(C) \(\sin(2x)+2\)',r'(D) \(2\sin(\pi x)+1\)',r'(E) \(2\sin x-1\)']),
 (r'Simplify \(\dfrac{\sin\theta}{\cos\theta}\cdot\cos\theta\sec\theta\).',
  [r'(A) \(\sin\theta\)',r'(B) \(\cos\theta\)',r'(C) \(1\)',r'(D) \(\sec\theta\)',r'(E) \(\tan\theta\)']),
 r'Opposite \(9\) m, hypotenuse \(15\) m. Find the angle opposite the \(9\) m side to the nearest degree.',
 r'If \(\cos\theta=\dfrac{5}{13}\) and \(\theta\) is acute: (i) draw a diagram; (ii) find exact \(\tan\theta\).',
 r'Find \(x\) if \(\cos 35^\circ=\sin(2x)\).',
 r'Find the exact value of \(\sin\dfrac{5\pi}{6}\).',
 r'Solve \(2\sin\theta=-1\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
 r'Solve \(\tan\theta=1\) for \(0\le\theta\le2\pi\). Exact answers in radians.',
 r'Sketch \(y=2\cos 3x\) on \([0,2\pi]\) and state amplitude and period.',
 r'Prove \((\sec\theta-\tan\theta)(\sec\theta+\tan\theta)=1\).',
 r'Solve \(2\cos^2\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
],
[
 (r'Angle of elevation \(18^\circ\) from a point \(40\) m from a tower base. Tower height to 1 d.p.?',
  ['(A) \(12.4\) m','(B) \(13.0\) m','(C) \(38.0\) m','(D) \(123.1\) m','(E) \(41.2\) m']),
 (r'Reference angle for \(\theta=-\dfrac{5\pi}{6}\)?',
  [r'(A) \(\dfrac{\pi}{6}\)',r'(B) \(\dfrac{5\pi}{6}\)',r'(C) \(\dfrac{\pi}{3}\)',r'(D) \(\dfrac{2\pi}{3}\)',r'(E) \(\dfrac{\pi}{2}\)']),
 (r'\(\csc\theta<0\) and \(\cos\theta>0\): quadrant?',
  ['(A) 1','(B) 2','(C) 3','(D) 4','(E) none']),
 (r'Convert \(\dfrac{7\pi}{4}\) to degrees.',
  ['(A) \(135^\circ\)','(B) \(225^\circ\)','(C) \(315^\circ\)','(D) \(405^\circ\)','(E) \(45^\circ\)']),
 (r'\(y=\cos x\): amplitude \(4\), period \(2\pi\), left shift \(\dfrac{\pi}{2}\), up \(1\):',
  [r'(A) \(4\cos\!\left(x-\dfrac{\pi}{2}\right)+1\)',r'(B) \(4\cos(2x)+1\)',r'(C) \(4\cos\!\left(x+\dfrac{\pi}{2}\right)-1\)',r'(D) \(\cos\!\left(4x-\dfrac{\pi}{2}\right)+1\)',r'(E) \(4\cos x+\dfrac{\pi}{2}\)']),
 (r'Simplify \(1+\tan^2\theta\).',
  [r'(A) \(\sin^2\theta\)',r'(B) \(\cos^2\theta\)',r'(C) \(\sec^2\theta\)',r'(D) \(\csc^2\theta\)',r'(E) \(1\)']),
 r'A ship is \(2.5\) km from a lighthouse. Angle of elevation to the top is \(12^\circ\). Find the lighthouse height to the nearest minute-level accuracy (2 d.p. in km).',
 r'If \(\tan\theta=\dfrac{8}{15}\) and \(\theta\) is acute: (i) draw a diagram; (ii) find exact \(\sin\theta\).',
 r'Find \(x\) if \(\sin 70^\circ=\cos(3x)\).',
 r'Find the exact value of \(\cos\dfrac{3\pi}{4}\).',
 r'Solve \(2\cos\theta=\sqrt{3}\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
 r'Solve \(2\sin\theta=\sqrt{2}\) for \(0\le\theta\le2\pi\). Exact answers in radians.',
 r'Sketch \(y=3\sin\!\left(\dfrac{x}{2}\right)\) for \(0\le x\le4\pi\) and state amplitude and period.',
 r'Prove \(\dfrac{1-\cos 2\theta}{\sin 2\theta}=\tan\theta\).',
 r'Solve \(\sin 2\theta=\dfrac12\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
],
[
 (r'In \(\triangle ABC\), right-angled at \(C\), \(AC=6\), \(BC=8\). Find \(\sin A\).',
  [r'(A) \(\dfrac{3}{4}\)',r'(B) \(\dfrac{4}{5}\)',r'(C) \(\dfrac{3}{5}\)',r'(D) \(\dfrac{5}{4}\)',r'(E) \(\dfrac{6}{8}\)']),
 (r'Reference angle for \(300^\circ\)?',
  ['(A) \(30^\circ\)','(B) \(60^\circ\)','(C) \(120^\circ\)','(D) \(300^\circ\)','(E) \(45^\circ\)']),
 (r'\(\sin\theta<0\) and \(\sec\theta<0\): quadrant?',
  ['(A) 1','(B) 2','(C) 3','(D) 4','(E) none']),
 (r'Convert \(75^\circ\) to radians (exact).',
  [r'(A) \(\dfrac{5\pi}{12}\)',r'(B) \(\dfrac{\pi}{3}\)',r'(C) \(\dfrac{3\pi}{8}\)',r'(D) \(\dfrac{2\pi}{5}\)',r'(E) \(\dfrac{\pi}{4}\)']),
 (r'\(y=\sin x\): amplitude \(5\), period \(6\pi\), down \(3\):',
  [r'(A) \(5\sin\!\left(\dfrac{x}{3}\right)-3\)',r'(B) \(5\sin(3x)-3\)',r'(C) \(5\sin(6\pi x)-3\)',r'(D) \(\sin\!\left(\dfrac{x}{3}\right)-5\)',r'(E) \(5\sin x-3\)']),
 (r'Simplify \(\cos^2\theta(\sec^2\theta-1)\).',
  [r'(A) \(\tan^2\theta\)',r'(B) \(\sin^2\theta\)',r'(C) \(1\)',r'(D) \(\cos^2\theta\)',r'(E) \(\sec^2\theta\)']),
 r'A wire from the top of a \(12\) m pole makes \(35^\circ\) with the ground. Find the wire length to 2 d.p.',
 r'If \(\sin\theta=\dfrac{12}{13}\) and \(\theta\) is obtuse: (i) draw a diagram; (ii) find exact \(\cos\theta\).',
 r'Find \(x\) if \(\cos 20^\circ=\sin(90^\circ-x)\).',
 r'Exact value of \(\tan\!\left(-\dfrac{\pi}{4}\right)\).',
 r'Solve \(\sin 2\theta=0\) for \(0^\circ\le\theta\le180^\circ\). Exact answers in degrees.',
 r'Solve \(2\cos\theta+1=0\) for \(0\le\theta\le2\pi\). Exact answers in radians.',
 r'Sketch \(y=2\sin\!\left(x-\dfrac{\pi}{2}\right)\) for \(0\le x\le2\pi\) and state amplitude and period.',
 r'Prove \(\dfrac{1-\cos 2\theta}{1+\cos 2\theta}=\tan^2\theta\).',
 r'Solve \(\sin^2\theta=\dfrac34\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
],
[
 (r'Opposite \(7\) m, angle \(28^\circ\). Find the adjacent side to 2 d.p.',
  ['(A) \(3.29\) m','(B) \(13.16\) m','(C) \(7.92\) m','(D) \(6.18\) m','(E) \(14.89\) m']),
 (r'Reference angle for \(\theta=150^\circ\)?',
  ['(A) \(30^\circ\)','(B) \(60^\circ\)','(C) \(150^\circ\)','(D) \(15^\circ\)','(E) \(120^\circ\)']),
 (r'If \(\cos\theta<0\) and \(\tan\theta>0\), \(\theta\) lies in quadrant',
  ['(A) 1','(B) 2','(C) 3','(D) 4','(E) none']),
 (r'Convert \(\dfrac{5\pi}{6}\) to degrees.',
  ['(A) \(120^\circ\)','(B) \(150^\circ\)','(C) \(30^\circ\)','(D) \(60^\circ\)','(E) \(210^\circ\)']),
 (r'\(y=\cos x\): amplitude \(2\), period \(\pi\), down \(1\):',
  [r'(A) \(2\cos(2x)-1\)',r'(B) \(2\cos\!\left(\dfrac{x}{2}\right)-1\)',r'(C) \(\cos(2x)-2\)',r'(D) \(2\cos(\pi x)-1\)',r'(E) \(2\cos x+1\)']),
 (r'Simplify \(\dfrac{1-\cos^2\theta}{\sin\theta}\).',
  [r'(A) \(\sin\theta\)',r'(B) \(\cos\theta\)',r'(C) \(\tan\theta\)',r'(D) \(\sec\theta\)',r'(E) \(1\)']),
 r'Hypotenuse \(20\) m, opposite \(9\) m. Find the angle opposite the \(9\) m side to the nearest minute.',
 r'If \(\cos\theta=\dfrac{8}{17}\) and \(\theta\) is acute: (i) draw a diagram; (ii) find exact \(\csc\theta\).',
 r'Find \(x\) if \(\sin 55^\circ=\cos(90^\circ-3x)\).',
 r'Find the exact value of \(\cos\dfrac{2\pi}{3}\).',
 r'Solve \(2\sin\theta=\sqrt{3}\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
 r'Solve \(\cot\theta=-1\) for \(0\le\theta\le2\pi\). Exact answers in radians.',
 r'Sketch \(y=4\cos 2x\) for \(0\le x\le\pi\) and state amplitude and period.',
 r'Prove \(1+\cot^2\theta=\csc^2\theta\).',
 r'Solve \(\cos 2\theta=-\dfrac12\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
],
[
 (r'A ladder leans against a wall at \(62^\circ\) to the ground. Base is \(3.5\) m from the wall. Ladder length to 2 d.p.?',
  ['(A) \(1.64\) m','(B) \(6.58\) m','(C) \(7.45\) m','(D) \(3.96\) m','(E) \(4.12\) m']),
 (r'Reference angle for \(\theta=-\dfrac{3\pi}{4}\)?',
  [r'(A) \(\dfrac{\pi}{4}\)',r'(B) \(\dfrac{3\pi}{4}\)',r'(C) \(\dfrac{\pi}{2}\)',r'(D) \(\dfrac{\pi}{3}\)',r'(E) \(\dfrac{\pi}{6}\)']),
 (r'\(\tan\theta>0\) and \(\sin\theta<0\): quadrant?',
  ['(A) 1','(B) 2','(C) 3','(D) 4','(E) none']),
 (r'Convert \(210^\circ\) to radians (exact).',
  [r'(A) \(\dfrac{7\pi}{6}\)',r'(B) \(\dfrac{5\pi}{6}\)',r'(C) \(\dfrac{2\pi}{3}\)',r'(D) \(\dfrac{3\pi}{4}\)',r'(E) \(\dfrac{5\pi}{4}\)']),
 (r'\(y=\sin x\): amplitude \(3\), period \(4\pi\), up \(2\):',
  [r'(A) \(3\sin\!\left(\dfrac{x}{2}\right)+2\)',r'(B) \(3\sin(2x)+2\)',r'(C) \(3\sin(4\pi x)+2\)',r'(D) \(\sin\!\left(\dfrac{x}{2}\right)+3\)',r'(E) \(2\sin(x/2)+3\)']),
 (r'Simplify \(\sin\theta\cot\theta\).',
  [r'(A) \(\cos\theta\)',r'(B) \(\sin\theta\)',r'(C) \(\tan\theta\)',r'(D) \(1\)',r'(E) \(\sec\theta\)']),
 r'Adjacent \(11\) m, opposite \(5\) m. Find the included acute angle to the nearest minute.',
 r'If \(\sin\theta=\dfrac{7}{25}\) and \(\theta\) is acute: (i) draw a diagram; (ii) find exact \(\cot\theta\).',
 r'Find \(x\) if \(\cos 40^\circ=\sin(50^\circ-x)\).',
 r'Find the exact value of \(\sin\dfrac{3\pi}{2}\).',
 r'Solve \(\tan\theta=-\sqrt{3}\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
 r'Solve \(2\cos\theta=-\sqrt{2}\) for \(0\le\theta\le2\pi\). Exact answers in radians.',
 r'Sketch \(y=-\sin 2x\) for \(0\le x\le2\pi\) and state amplitude and period.',
 r'Prove \(\dfrac{\sin 2\theta}{1+\cos 2\theta}=\tan\theta\).',
 r'Solve \(2\cos^2\theta+\cos\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
],
]

trig_a = [
[
 r'(B) \(5.15\) m.',
 r'(D) \(45^\circ\).',
 r'(C) Quadrant 3.',
 r'(A) \(165^\circ\).',
 r'(B) \(3\cos(x/2)-2\).',
 r'(C) \(1\).',
 r'\(\cos^{-1}(7/15)\approx62^\circ11\'\).',
 r'Diagram with opp \(3\), hyp \(5\), adj \(4\); \(\sec\theta=5/4\).',
 r'\(x=40^\circ\) (from \(80^\circ=90^\circ-2x\)).',
 r'\(-\sqrt{3}\).',
 r'\(\theta=60^\circ,300^\circ\).',
 r'\(\theta=\pi/6,7\pi/6\).',
 r'Amplitude \(1/2\), period \(\pi\).',
 r'Use double-angle formula / expansion from \(\sin(A+B)\).',
 r'Use \(\cos2x=1-2\sin^2 x\); solutions \(x=90^\circ,270^\circ\) (check domain carefully with identities).',
],
[
 r'(A) \(3.23\) m.',
 r'(A) \(30^\circ\).',
 r'(B) Quadrant 2.',
 r'(B) \(4\pi/3\).',
 r'(A) \(2\sin(2x)+1\).',
 r'(D) \(\sec\theta\).',
 r'\(\sin^{-1}(9/15)\approx37^\circ\).',
 r'Diagram; \(\tan\theta=12/5\).',
 r'\(x=27.5^\circ\) (from \(2x=55^\circ\)).',
 r'\(1/2\).',
 r'\(\theta=210^\circ,330^\circ\).',
 r'\(\theta=\pi/4,5\pi/4\).',
 r'Amplitude \(2\), period \(2\pi/3\).',
 r'\(\sec^2\theta-\tan^2\theta=1\).',
 r'\(\theta=45^\circ,135^\circ,225^\circ,315^\circ\).',
],
[
 r'(B) \(13.0\) m.',
 r'(A) \(\pi/6\).',
 r'(D) Quadrant 4.',
 r'(C) \(315^\circ\).',
 r'(A) \(4\cos(x-\pi/2)+1\).',
 r'(C) \(\sec^2\theta\).',
 r'\(2.5\tan12^\circ\approx0.53\) km.',
 r'Diagram; hyp \(17\); \(\sin\theta=8/17\).',
 r'\(x=\tfrac{20^\circ}{3}\) from \(3x=20^\circ\).',
 r'\(-\dfrac{\sqrt2}{2}\).',
 r'\(\theta=30^\circ,330^\circ\).',
 r'\(\theta=\pi/4,3\pi/4\).',
 r'Amplitude \(3\), period \(4\pi\).',
 r'\(\dfrac{2\sin^2\theta}{2\sin\theta\cos\theta}=\tan\theta\).',
 r'\(2\theta=30^\circ,150^\circ,\ldots\) so \(\theta=15^\circ,75^\circ,195^\circ,255^\circ\).',
],
[
 r'(B) \(4/5\).',
 r'(B) \(60^\circ\).',
 r'(C) Quadrant 3.',
 r'(A) \(5\pi/12\).',
 r'(A) \(5\sin(x/3)-3\).',
 r'(B) \(\sin^2\theta\).',
 r'\(12/\sin35^\circ\approx20.92\) m.',
 r'Diagram in Q2; \(\cos\theta=-5/13\).',
 r'\(x=20^\circ\).',
 r'\(-1\).',
 r'\(\theta=0^\circ,90^\circ,180^\circ\).',
 r'\(\theta=2\pi/3,4\pi/3\).',
 r'Amplitude \(2\), period \(2\pi\).',
 r'\(\dfrac{2\sin^2\theta}{2\cos^2\theta}=\tan^2\theta\).',
 r'\(\theta=60^\circ,120^\circ,240^\circ,300^\circ\).',
],
[
 r'(B) \(13.16\) m (\(7/\tan28^\circ\)).',
 r'(A) \(30^\circ\).',
 r'(C) Quadrant 3.',
 r'(B) \(150^\circ\).',
 r'(A) \(2\cos(2x)-1\).',
 r'(A) \(\sin\theta\).',
 r'\(\sin^{-1}(9/20)\approx26^\circ44\'\).',
 r'Diagram; opp \(15\); \(\csc\theta=17/15\).',
 r'\(x=\tfrac{55^\circ}{3}\) from \(3x=55^\circ\).',
 r'\(-1/2\).',
 r'\(\theta=60^\circ,120^\circ\).',
 r'\(\theta=3\pi/4,7\pi/4\).',
 r'Amplitude \(4\), period \(\pi\).',
 r'Divide by \(\sin^2\theta\): \(1+\cot^2=\csc^2\).',
 r'\(2\theta=120^\circ,240^\circ,\ldots\) so \(\theta=60^\circ,120^\circ,240^\circ,300^\circ\).',
],
[
 r'(C) \(7.45\) m (\(3.5/\cos62^\circ\)).',
 r'(A) \(\pi/4\).',
 r'(C) Quadrant 3.',
 r'(A) \(7\pi/6\).',
 r'(A) \(3\sin(x/2)+2\).',
 r'(A) \(\cos\theta\).',
 r'\(\tan^{-1}(5/11)\approx24^\circ26\'\).',
 r'Diagram; adj \(24\); \(\cot\theta=24/7\).',
 r'\(x=10^\circ\) from \(50^\circ-x=40^\circ\).',
 r'\(-1\).',
 r'\(\theta=120^\circ,300^\circ\).',
 r'\(\theta=3\pi/4,5\pi/4\).',
 r'Amplitude \(1\), period \(\pi\).',
 r'\(\dfrac{2\sin\theta\cos\theta}{2\cos^2\theta}=\tan\theta\).',
 r'\((2\cos\theta-1)(\cos\theta+1)=0\Rightarrow\theta=60^\circ,180^\circ,300^\circ\).',
],
]

# Diagram and worked-answer upgrades.  These are kept data-driven so every
# paper uses the same reusable SVG helpers while retaining its question slots.
q1_diagrams = [
    right_triangle_svg('5 m', '', 'x m', "13°45′",
                       caption='Given right triangle: find the hypotenuse',
                       context='adjacent = 5 m; hypotenuse = x'),
    right_triangle_svg('8 m', 'x m', '', '22°',
                       caption='Given right triangle: find the opposite side',
                       context='adjacent = 8 m; opposite = x'),
    right_triangle_svg('40 m', 'h m', 'line of sight', '18°',
                       caption='Tower and angle of elevation',
                       context='observer                         tower base; tower height = h'),
    right_triangle_svg('AC = 6', 'BC = 8', '', 'A',
                       caption='Triangle ABC, right-angled at C',
                       vertices=('A', 'B', 'C'), answer_prompt='sin A = ?'),
    right_triangle_svg('a m', '7 m', '', '28°',
                       caption='Given right triangle: find the adjacent side',
                       context='opposite = 7 m; adjacent = a'),
    right_triangle_svg('3.5 m', 'wall', 'L m (ladder)', '62°',
                       caption='Ladder leaning against a vertical wall',
                       context='ground                         wall; ladder length = L'),
]
for test, diagram in zip(trig_q, q1_diagrams):
    stem, choices = test[0]
    test[0] = (stem + diagram, choices)

# Correct pre-existing answer/choice issues found during the six-paper audit.
trig_a[1][5] = r'(E) \(\tan\theta\).'
transform_stem, transform_choices = trig_q[2][4]
transform_choices[0] = r'(A) \(4\cos\!\left(x+\dfrac{\pi}{2}\right)+1\)'
trig_q[2][4] = (transform_stem, transform_choices)
trig_a[2][4] = r'(A) \(4\cos\!\left(x+\dfrac{\pi}{2}\right)+1\).'
trig_a[4][6] = r'\(\sin^{-1}(9/20)\approx26^\circ45\'\).'
trig_a[5][6] = r'\(\tan^{-1}(5/11)\approx24^\circ27\'\).'
trig_a[5][8] = (
    r'\(x=0^\circ\), since \(\cos40^\circ=\sin50^\circ\), '
    r'so \(50^\circ-x=50^\circ\).'
)

# Coherent 2-mark application question (height rounded to two decimal places).
trig_q[2][6] = (r'A ship is \(2.5\) km horizontally from a lighthouse. The angle of elevation '
                r'to the top is \(12^\circ\). Find the lighthouse height to 2 d.p. in kilometres.')

acute_q8 = [
    right_triangle_svg('4', '3', '5', 'θ', caption='Reference triangle for sin θ = 3/5'),
    right_triangle_svg('5', '12', '13', 'θ', caption='Reference triangle for cos θ = 5/13'),
    right_triangle_svg('15', '8', '17', 'θ', caption='Reference triangle for tan θ = 8/15'),
    q2_reference_triangle_svg(),
    right_triangle_svg('8', '15', '17', 'θ', caption='Reference triangle for cos θ = 8/17'),
    right_triangle_svg('24', '7', '25', 'θ', caption='Reference triangle for sin θ = 7/25'),
]
q8_working = [
    r'''Since \(\sin\theta=\frac{\mathrm{opp}}{\mathrm{hyp}}=\frac35\), take opposite \(3\)
and hypotenuse \(5\). By Pythagoras, the adjacent side is
\(\sqrt{5^2-3^2}=4\). Hence \(\displaystyle\sec\theta=\frac{\mathrm{hyp}}{\mathrm{adj}}=\frac54\).''',
    r'''Since \(\cos\theta=\frac{\mathrm{adj}}{\mathrm{hyp}}=\frac5{13}\), take adjacent \(5\)
and hypotenuse \(13\). The opposite side is
\(\sqrt{13^2-5^2}=12\). Hence \(\displaystyle\tan\theta=\frac{\mathrm{opp}}{\mathrm{adj}}=\frac{12}{5}\).''',
    r'''Since \(\tan\theta=\frac{\mathrm{opp}}{\mathrm{adj}}=\frac8{15}\), take opposite \(8\)
and adjacent \(15\). The hypotenuse is \(\sqrt{8^2+15^2}=17\), so
\(\displaystyle\sin\theta=\frac{\mathrm{opp}}{\mathrm{hyp}}=\frac8{17}\).''',
    r'''\(\theta\) lies in quadrant II, so \(y>0\) and \(x<0\). With
\(\sin\theta=\frac{y}{r}=\frac{12}{13}\), Pythagoras gives
\(|x|=\sqrt{13^2-12^2}=5\), hence \(x=-5\). Therefore
\(\displaystyle\cos\theta=\frac{x}{r}=-\frac5{13}\). The diagram shows
\(\theta\) in standard position; it is not the acute reference angle.''',
    r'''Since \(\cos\theta=\frac{\mathrm{adj}}{\mathrm{hyp}}=\frac8{17}\), the opposite side is
\(\sqrt{17^2-8^2}=15\). Thus
\(\displaystyle\csc\theta=\frac{\mathrm{hyp}}{\mathrm{opp}}=\frac{17}{15}\).''',
    r'''Since \(\sin\theta=\frac{\mathrm{opp}}{\mathrm{hyp}}=\frac7{25}\), the adjacent side is
\(\sqrt{25^2-7^2}=24\). Thus
\(\displaystyle\cot\theta=\frac{\mathrm{adj}}{\mathrm{opp}}=\frac{24}{7}\).''',
]
for i in range(6):
    trig_a[i][7] = q8_working[i] + acute_q8[i]

graph_specs = [
    {
        'fn': lambda x: 0.5 * math.sin(2*x), 'xmin': -math.pi, 'xmax': math.pi,
        'amp': 0.5, 'period': math.pi, 'step': math.pi/4,
        'period_tex': r'\pi',
        'caption': 'y = ½ sin(2x),  −π ≤ x ≤ π',
        'notes': ('midline y = 0',),
    },
    {
        'fn': lambda x: 2 * math.cos(3*x), 'xmin': 0, 'xmax': 2*math.pi,
        'amp': 2, 'period': 2*math.pi/3, 'step': math.pi/6,
        'period_tex': r'\dfrac{2\pi}{3}',
        'caption': 'y = 2 cos(3x),  0 ≤ x ≤ 2π',
        'notes': ('midline y = 0',),
    },
    {
        'fn': lambda x: 3 * math.sin(x/2), 'xmin': 0, 'xmax': 4*math.pi,
        'amp': 3, 'period': 4*math.pi, 'step': math.pi,
        'period_tex': r'4\pi',
        'caption': 'y = 3 sin(x/2),  0 ≤ x ≤ 4π',
        'notes': ('midline y = 0',),
    },
    {
        'fn': lambda x: 2 * math.sin(x-math.pi/2), 'xmin': 0, 'xmax': 2*math.pi,
        'amp': 2, 'period': 2*math.pi, 'step': math.pi/2,
        'period_tex': r'2\pi',
        'caption': 'y = 2 sin(x − π/2),  0 ≤ x ≤ 2π',
        'notes': ('midline y = 0', 'phase shift = π/2 to the right'),
    },
    {
        'fn': lambda x: 4 * math.cos(2*x), 'xmin': 0, 'xmax': math.pi,
        'amp': 4, 'period': math.pi, 'step': math.pi/4,
        'period_tex': r'\pi',
        'caption': 'y = 4 cos(2x),  0 ≤ x ≤ π',
        'notes': ('midline y = 0',),
    },
    {
        'fn': lambda x: -math.sin(2*x), 'xmin': 0, 'xmax': 2*math.pi,
        'amp': 1, 'period': math.pi, 'step': math.pi/4,
        'period_tex': r'\pi',
        'caption': 'y = −sin(2x),  0 ≤ x ≤ 2π',
        'notes': ('midline y = 0', 'reflection of y = sin(2x) in the x-axis'),
    },
]

for i, spec in enumerate(graph_specs):
    count = round((spec['xmax'] - spec['xmin']) / spec['step'])
    xs = [spec['xmin'] + j * spec['step'] for j in range(count + 1)]
    points = [(x, 0.0 if abs(spec['fn'](x)) < 1e-10 else spec['fn'](x)) for x in xs]
    # Coordinate text is reserved for extrema and endpoints; every intercept
    # and quarter-period point is still marked and has its own labelled x tick.
    labelled = [(x, y) for j, (x, y) in enumerate(points)
                if abs(abs(y) - spec['amp']) < 1e-9 or j in (0, len(points)-1)]
    trig_q[i][12] += blank_trig_grid(
        spec['xmin'], spec['xmax'], xs, caption=f"Sketching grid: {spec['caption']}")
    graph = trig_plot(
        spec['fn'], spec['xmin'], spec['xmax'],
        -spec['amp'] - 0.6, spec['amp'] + 0.6, points,
        midline=0, amplitude=spec['amp'], period=spec['period'],
        caption=spec['caption'], extra_notes=spec['notes'],
        yticks=[-spec['amp'], 0, spec['amp']], xticks=xs,
        label_points=labelled,
    )
    amp_answer = r'\frac12' if math.isclose(spec['amp'], 0.5) else f'{spec["amp"]:g}'
    trig_a[i][12] = (
        f'''Amplitude \(={amp_answer}\); period \(={spec["period_tex"]}\).
The marked points occur at every quarter-period, so all intercepts and extrema
are shown across the full stated domain.''' + graph
    )

# Proper LHS-to-RHS identity proofs, with each algebraic substitution shown.
trig_a[0][13] = r'''\[
\begin{aligned}
\text{LHS}&=\sin(2\theta)\\
&=\sin(\theta+\theta)\\
&=\sin\theta\cos\theta+\cos\theta\sin\theta\\
&=2\sin\theta\cos\theta=\text{RHS}.
\end{aligned}
\]'''
trig_a[1][13] = r'''\[
\begin{aligned}
\text{LHS}&=(\sec\theta-\tan\theta)(\sec\theta+\tan\theta)\\
&=\sec^2\theta-\tan^2\theta\\
&=(1+\tan^2\theta)-\tan^2\theta\\
&=1=\text{RHS}.
\end{aligned}
\]'''
trig_a[2][13] = r'''\[
\begin{aligned}
\text{LHS}&=\frac{1-\cos2\theta}{\sin2\theta}\\
&=\frac{2\sin^2\theta}{2\sin\theta\cos\theta}\\
&=\frac{\sin\theta}{\cos\theta}\\
&=\tan\theta=\text{RHS}.
\end{aligned}
\]'''
trig_a[3][13] = r'''\[
\begin{aligned}
\text{LHS}&=\frac{1-\cos2\theta}{1+\cos2\theta}\\
&=\frac{2\sin^2\theta}{2\cos^2\theta}\\
&=\left(\frac{\sin\theta}{\cos\theta}\right)^2\\
&=\tan^2\theta=\text{RHS}.
\end{aligned}
\]'''
trig_a[4][13] = r'''\[
\begin{aligned}
\text{LHS}&=1+\cot^2\theta\\
&=1+\frac{\cos^2\theta}{\sin^2\theta}\\
&=\frac{\sin^2\theta+\cos^2\theta}{\sin^2\theta}\\
&=\frac1{\sin^2\theta}=\csc^2\theta=\text{RHS}.
\end{aligned}
\]'''
trig_a[5][13] = r'''\[
\begin{aligned}
\text{LHS}&=\frac{\sin2\theta}{1+\cos2\theta}\\
&=\frac{2\sin\theta\cos\theta}{2\cos^2\theta}\\
&=\frac{\sin\theta}{\cos\theta}\\
&=\tan\theta=\text{RHS}.
\end{aligned}
\]'''

# ---------------------------------------------------------------------------
# Fully worked long-answer solutions for the six trig papers.
# Each override shows the method/setup, every algebraic/trig step, quadrant and
# reference-angle reasoning where relevant, and ends with a boxed final answer.
# Q7 (idx6) nearest-minute / applied ratios; Q9 (idx8) co-function solve;
# Q10 (idx9) exact special values; Q11 (idx10) solve in degrees;
# Q12 (idx11) solve in radians; Q15 (idx14) solve trig equation.
# ---------------------------------------------------------------------------

# Q7 (index 6): inverse-trig / applied right-triangle, answer to nearest minute
# or 2 d.p. as the question demands.
q7_working = [
    r'''Draw the right triangle with hypotenuse \(15\) m and adjacent side \(7\) m; the
included angle \(\theta\) satisfies \(\cos\theta=\dfrac{\text{adjacent}}{\text{hypotenuse}}\).
\[
\begin{aligned}
\cos\theta&=\frac{7}{15}\\
\theta&=\cos^{-1}\!\left(\frac{7}{15}\right)=62.1819\ldots^\circ.
\end{aligned}
\]
Convert the decimal part to minutes: \(0.1819^\circ\times 60=10.9'\), which rounds to \(11'\).
\[\boxed{\theta\approx 62^\circ 11'}\]''',
    r'''The \(9\) m side is opposite \(\theta\) with hypotenuse \(15\) m, so
\(\sin\theta=\dfrac{\text{opposite}}{\text{hypotenuse}}\).
\[
\begin{aligned}
\sin\theta&=\frac{9}{15}=\frac{3}{5}\\
\theta&=\sin^{-1}(0.6)=36.87^\circ.
\end{aligned}
\]
To the nearest degree,
\[\boxed{\theta\approx 37^\circ}\]''',
    r'''The horizontal distance \(2.5\) km is adjacent to the \(12^\circ\) angle of elevation
and the height \(h\) is opposite, so \(\tan 12^\circ=\dfrac{h}{2.5}\).
\[
\begin{aligned}
h&=2.5\tan 12^\circ\\
&=2.5(0.21256\ldots)\\
&=0.5314\ldots
\end{aligned}
\]
\[\boxed{h\approx 0.53\text{ km}}\]''',
    r'''The \(12\) m pole is opposite the \(35^\circ\) angle and the wire \(L\) is the hypotenuse,
so \(\sin 35^\circ=\dfrac{12}{L}\).
\[
\begin{aligned}
L&=\frac{12}{\sin 35^\circ}\\
&=\frac{12}{0.57358\ldots}\\
&=20.9214\ldots
\end{aligned}
\]
\[\boxed{L\approx 20.92\text{ m}}\]''',
    r'''The \(9\) m side is opposite \(\theta\) with hypotenuse \(20\) m, so
\(\sin\theta=\dfrac{\text{opposite}}{\text{hypotenuse}}\).
\[
\begin{aligned}
\sin\theta&=\frac{9}{20}=0.45\\
\theta&=\sin^{-1}(0.45)=26.7437\ldots^\circ.
\end{aligned}
\]
Convert to minutes: \(0.7437^\circ\times 60=44.6'\), which rounds to \(45'\).
\[\boxed{\theta\approx 26^\circ 45'}\]''',
    r'''With opposite side \(5\) m and adjacent side \(11\) m,
\(\tan\theta=\dfrac{\text{opposite}}{\text{adjacent}}\).
\[
\begin{aligned}
\tan\theta&=\frac{5}{11}\\
\theta&=\tan^{-1}\!\left(\frac{5}{11}\right)=24.4440\ldots^\circ.
\end{aligned}
\]
Convert to minutes: \(0.4440^\circ\times 60=26.6'\), which rounds to \(27'\).
\[\boxed{\theta\approx 24^\circ 27'}\]''',
]

# Q9 (index 8): co-function identity solve for x.
q9_working = [
    r'''Apply the co-function identity \(\cos(90^\circ-\alpha)=\sin\alpha\) to the right side.
\[
\begin{aligned}
\cos(90^\circ-2x)&=\sin 2x\\
\sin 80^\circ&=\sin 2x\\
2x&=80^\circ\\
x&=40^\circ.
\end{aligned}
\]
\[\boxed{x=40^\circ}\]''',
    r'''Rewrite the cosine as a sine using \(\cos\alpha=\sin(90^\circ-\alpha)\).
\[
\begin{aligned}
\cos 35^\circ&=\sin(90^\circ-35^\circ)=\sin 55^\circ\\
\sin 2x&=\sin 55^\circ\\
2x&=55^\circ\\
x&=27.5^\circ.
\end{aligned}
\]
\[\boxed{x=27.5^\circ}\]''',
    r'''Convert the sine to a cosine with \(\sin\alpha=\cos(90^\circ-\alpha)\).
\[
\begin{aligned}
\sin 70^\circ&=\cos(90^\circ-70^\circ)=\cos 20^\circ\\
\cos 3x&=\cos 20^\circ\\
3x&=20^\circ\\
x&=\frac{20^\circ}{3}=6^\circ 40'.
\end{aligned}
\]
\[\boxed{x=\tfrac{20^\circ}{3}\approx 6^\circ 40'}\]''',
    r'''Apply the co-function identity \(\sin(90^\circ-x)=\cos x\).
\[
\begin{aligned}
\sin(90^\circ-x)&=\cos x\\
\cos 20^\circ&=\cos x\\
x&=20^\circ.
\end{aligned}
\]
\[\boxed{x=20^\circ}\]''',
    r'''Use \(\cos(90^\circ-\alpha)=\sin\alpha\) to convert the right-hand side.
\[
\begin{aligned}
\cos(90^\circ-3x)&=\sin 3x\\
\sin 55^\circ&=\sin 3x\\
3x&=55^\circ\\
x&=\frac{55^\circ}{3}.
\end{aligned}
\]
\[\boxed{x=\tfrac{55^\circ}{3}\approx 18^\circ 20'}\]''',
    r'''First convert the cosine to a sine: \(\cos 40^\circ=\sin(90^\circ-40^\circ)=\sin 50^\circ\).
\[
\begin{aligned}
\sin(50^\circ-x)&=\sin 50^\circ\\
50^\circ-x&=50^\circ\\
x&=0^\circ.
\end{aligned}
\]
\[\boxed{x=0^\circ}\]''',
]

# Q10 (index 9): exact value via quadrant + reference angle + special triangle.
q10_working = [
    r'''\(\dfrac{2\pi}{3}=120^\circ\) lies in Quadrant II, where the tangent is negative, with
reference angle \(180^\circ-120^\circ=60^\circ=\dfrac{\pi}{3}\). Using the special-triangle
value \(\tan\dfrac{\pi}{3}=\sqrt3\),
\[
\tan\frac{2\pi}{3}=-\tan\frac{\pi}{3}=-\sqrt3.
\]
\[\boxed{\tan\tfrac{2\pi}{3}=-\sqrt3}\]''',
    r'''\(\dfrac{5\pi}{6}=150^\circ\) lies in Quadrant II, where the sine is positive, with
reference angle \(180^\circ-150^\circ=30^\circ=\dfrac{\pi}{6}\). Using \(\sin\dfrac{\pi}{6}=\dfrac12\),
\[
\sin\frac{5\pi}{6}=+\sin\frac{\pi}{6}=\frac12.
\]
\[\boxed{\sin\tfrac{5\pi}{6}=\tfrac12}\]''',
    r'''\(\dfrac{3\pi}{4}=135^\circ\) lies in Quadrant II, where the cosine is negative, with
reference angle \(180^\circ-135^\circ=45^\circ=\dfrac{\pi}{4}\). Using \(\cos\dfrac{\pi}{4}=\dfrac{\sqrt2}{2}\),
\[
\cos\frac{3\pi}{4}=-\cos\frac{\pi}{4}=-\frac{\sqrt2}{2}.
\]
\[\boxed{\cos\tfrac{3\pi}{4}=-\tfrac{\sqrt2}{2}}\]''',
    r'''\(-\dfrac{\pi}{4}=-45^\circ\) is a Quadrant IV angle (measured clockwise), where the
tangent is negative, with reference angle \(\dfrac{\pi}{4}\). Since tangent is odd and
\(\tan\dfrac{\pi}{4}=1\),
\[
\tan\!\left(-\frac{\pi}{4}\right)=-\tan\frac{\pi}{4}=-1.
\]
\[\boxed{\tan\!\left(-\tfrac{\pi}{4}\right)=-1}\]''',
    r'''\(\dfrac{2\pi}{3}=120^\circ\) lies in Quadrant II, where the cosine is negative, with
reference angle \(180^\circ-120^\circ=60^\circ=\dfrac{\pi}{3}\). Using \(\cos\dfrac{\pi}{3}=\dfrac12\),
\[
\cos\frac{2\pi}{3}=-\cos\frac{\pi}{3}=-\frac12.
\]
\[\boxed{\cos\tfrac{2\pi}{3}=-\tfrac12}\]''',
    r'''\(\dfrac{3\pi}{2}=270^\circ\) is a quadrantal angle whose terminal side is the negative
\(y\)-axis, meeting the unit circle at \((0,-1)\). Since \(\sin\theta\) is the
\(y\)-coordinate,
\[
\sin\frac{3\pi}{2}=-1.
\]
\[\boxed{\sin\tfrac{3\pi}{2}=-1}\]''',
]

# Q11 (index 10): solve in degrees over 0 to 360 (or as stated).
q11_working = [
    r'''Since \(\cos\theta=\dfrac12\) is positive, \(\theta\) is in Quadrants I and IV. The
reference angle is \(\cos^{-1}\dfrac12=60^\circ\).
\[
\theta=60^\circ\quad\text{(QI)}\qquad\text{or}\qquad\theta=360^\circ-60^\circ=300^\circ\quad\text{(QIV)}.
\]
\[\boxed{\theta=60^\circ,\ 300^\circ}\]''',
    r'''\[2\sin\theta=-1\ \Rightarrow\ \sin\theta=-\tfrac12.\]
Sine is negative in Quadrants III and IV; the reference angle is \(\sin^{-1}\dfrac12=30^\circ\).
\[
\theta=180^\circ+30^\circ=210^\circ\qquad\text{or}\qquad\theta=360^\circ-30^\circ=330^\circ.
\]
\[\boxed{\theta=210^\circ,\ 330^\circ}\]''',
    r'''\[2\cos\theta=\sqrt3\ \Rightarrow\ \cos\theta=\tfrac{\sqrt3}{2}.\]
Cosine is positive in Quadrants I and IV; the reference angle is \(30^\circ\).
\[
\theta=30^\circ\qquad\text{or}\qquad\theta=360^\circ-30^\circ=330^\circ.
\]
\[\boxed{\theta=30^\circ,\ 330^\circ}\]''',
    r'''Let \(\phi=2\theta\). As \(0^\circ\le\theta\le180^\circ\) we have \(0^\circ\le\phi\le360^\circ\).
Sine is zero at integer multiples of \(180^\circ\):
\[
2\theta=0^\circ,\ 180^\circ,\ 360^\circ\ \Rightarrow\ \theta=0^\circ,\ 90^\circ,\ 180^\circ.
\]
\[\boxed{\theta=0^\circ,\ 90^\circ,\ 180^\circ}\]''',
    r'''\[2\sin\theta=\sqrt3\ \Rightarrow\ \sin\theta=\tfrac{\sqrt3}{2}.\]
Sine is positive in Quadrants I and II; the reference angle is \(60^\circ\).
\[
\theta=60^\circ\qquad\text{or}\qquad\theta=180^\circ-60^\circ=120^\circ.
\]
\[\boxed{\theta=60^\circ,\ 120^\circ}\]''',
    r'''\(\tan\theta=-\sqrt3\) is negative, so \(\theta\) is in Quadrants II and IV. The
reference angle is \(\tan^{-1}\sqrt3=60^\circ\).
\[
\theta=180^\circ-60^\circ=120^\circ\qquad\text{or}\qquad\theta=360^\circ-60^\circ=300^\circ.
\]
\[\boxed{\theta=120^\circ,\ 300^\circ}\]''',
]

# Q12 (index 11): solve in radians over 0 to 2 pi.
q12_working = [
    r'''\(\cot\theta=\sqrt3\) means \(\tan\theta=\dfrac{1}{\sqrt3}\), which is positive, so
\(\theta\) is in Quadrants I and III. The reference angle is \(\dfrac{\pi}{6}\).
\[
\theta=\frac{\pi}{6}\qquad\text{or}\qquad\theta=\pi+\frac{\pi}{6}=\frac{7\pi}{6}.
\]
\[\boxed{\theta=\tfrac{\pi}{6},\ \tfrac{7\pi}{6}}\]''',
    r'''\(\tan\theta=1\) is positive, so \(\theta\) is in Quadrants I and III. The reference
angle is \(\dfrac{\pi}{4}\).
\[
\theta=\frac{\pi}{4}\qquad\text{or}\qquad\theta=\pi+\frac{\pi}{4}=\frac{5\pi}{4}.
\]
\[\boxed{\theta=\tfrac{\pi}{4},\ \tfrac{5\pi}{4}}\]''',
    r'''\[2\sin\theta=\sqrt2\ \Rightarrow\ \sin\theta=\tfrac{\sqrt2}{2}.\]
Sine is positive in Quadrants I and II; the reference angle is \(\dfrac{\pi}{4}\).
\[
\theta=\frac{\pi}{4}\qquad\text{or}\qquad\theta=\pi-\frac{\pi}{4}=\frac{3\pi}{4}.
\]
\[\boxed{\theta=\tfrac{\pi}{4},\ \tfrac{3\pi}{4}}\]''',
    r'''\[2\cos\theta+1=0\ \Rightarrow\ \cos\theta=-\tfrac12.\]
Cosine is negative in Quadrants II and III; the reference angle is \(\dfrac{\pi}{3}\).
\[
\theta=\pi-\frac{\pi}{3}=\frac{2\pi}{3}\qquad\text{or}\qquad\theta=\pi+\frac{\pi}{3}=\frac{4\pi}{3}.
\]
\[\boxed{\theta=\tfrac{2\pi}{3},\ \tfrac{4\pi}{3}}\]''',
    r'''\(\cot\theta=-1\) means \(\tan\theta=-1\), which is negative, so \(\theta\) is in
Quadrants II and IV. The reference angle is \(\dfrac{\pi}{4}\).
\[
\theta=\pi-\frac{\pi}{4}=\frac{3\pi}{4}\qquad\text{or}\qquad\theta=2\pi-\frac{\pi}{4}=\frac{7\pi}{4}.
\]
\[\boxed{\theta=\tfrac{3\pi}{4},\ \tfrac{7\pi}{4}}\]''',
    r'''\[2\cos\theta=-\sqrt2\ \Rightarrow\ \cos\theta=-\tfrac{\sqrt2}{2}.\]
Cosine is negative in Quadrants II and III; the reference angle is \(\dfrac{\pi}{4}\).
\[
\theta=\pi-\frac{\pi}{4}=\frac{3\pi}{4}\qquad\text{or}\qquad\theta=\pi+\frac{\pi}{4}=\frac{5\pi}{4}.
\]
\[\boxed{\theta=\tfrac{3\pi}{4},\ \tfrac{5\pi}{4}}\]''',
]

# Q15 (index 14): solve a trig equation, showing identity/factoring and all
# solutions in the stated domain.
q15_working = [
    r'''Use the double-angle identity \(\cos 2x=1-2\sin^2x\).
\[
\begin{aligned}
2\sin^2x-\cos 2x&=2\\
2\sin^2x-(1-2\sin^2x)&=2\\
4\sin^2x-1&=2\\
4\sin^2x&=3\\
\sin x&=\pm\frac{\sqrt3}{2}.
\end{aligned}
\]
The reference angle is \(60^\circ\). \(\sin x=\dfrac{\sqrt3}{2}\Rightarrow x=60^\circ,120^\circ\);
\(\sin x=-\dfrac{\sqrt3}{2}\Rightarrow x=240^\circ,300^\circ\).
\[\boxed{x=60^\circ,\ 120^\circ,\ 240^\circ,\ 300^\circ}\]''',
    r'''\[
\begin{aligned}
2\cos^2\theta-1&=0\\
\cos^2\theta&=\frac12\\
\cos\theta&=\pm\frac{\sqrt2}{2}.
\end{aligned}
\]
The reference angle is \(45^\circ\). \(\cos\theta=\dfrac{\sqrt2}{2}\Rightarrow\theta=45^\circ,315^\circ\);
\(\cos\theta=-\dfrac{\sqrt2}{2}\Rightarrow\theta=135^\circ,225^\circ\).
\[\boxed{\theta=45^\circ,\ 135^\circ,\ 225^\circ,\ 315^\circ}\]''',
    r'''Because the argument is \(2\theta\), extend the domain: \(0^\circ\le\theta\le360^\circ\)
gives \(0^\circ\le 2\theta\le720^\circ\). With \(\sin 2\theta=\dfrac12\) the reference angle is
\(30^\circ\) and sine is positive in Quadrants I and II:
\[
\begin{aligned}
2\theta&=30^\circ,\ 150^\circ,\ 390^\circ,\ 510^\circ\\
\theta&=15^\circ,\ 75^\circ,\ 195^\circ,\ 255^\circ.
\end{aligned}
\]
\[\boxed{\theta=15^\circ,\ 75^\circ,\ 195^\circ,\ 255^\circ}\]''',
    r'''\[
\begin{aligned}
\sin^2\theta&=\frac34\\
\sin\theta&=\pm\frac{\sqrt3}{2}.
\end{aligned}
\]
The reference angle is \(60^\circ\). \(\sin\theta=\dfrac{\sqrt3}{2}\Rightarrow\theta=60^\circ,120^\circ\);
\(\sin\theta=-\dfrac{\sqrt3}{2}\Rightarrow\theta=240^\circ,300^\circ\).
\[\boxed{\theta=60^\circ,\ 120^\circ,\ 240^\circ,\ 300^\circ}\]''',
    r'''Because the argument is \(2\theta\), extend the domain: \(0^\circ\le\theta\le360^\circ\)
gives \(0^\circ\le 2\theta\le720^\circ\). With \(\cos 2\theta=-\dfrac12\) the reference angle is
\(60^\circ\) and cosine is negative in Quadrants II and III:
\[
\begin{aligned}
2\theta&=120^\circ,\ 240^\circ,\ 480^\circ,\ 600^\circ\\
\theta&=60^\circ,\ 120^\circ,\ 240^\circ,\ 300^\circ.
\end{aligned}
\]
\[\boxed{\theta=60^\circ,\ 120^\circ,\ 240^\circ,\ 300^\circ}\]''',
    r'''Treat the equation as a quadratic in \(\cos\theta\) and factor.
\[
\begin{aligned}
2\cos^2\theta+\cos\theta-1&=0\\
(2\cos\theta-1)(\cos\theta+1)&=0.
\end{aligned}
\]
So \(\cos\theta=\dfrac12\) (reference angle \(60^\circ\)) giving \(\theta=60^\circ,300^\circ\),
or \(\cos\theta=-1\) giving \(\theta=180^\circ\).
\[\boxed{\theta=60^\circ,\ 180^\circ,\ 300^\circ}\]''',
]

for i in range(6):
    trig_a[i][6] = q7_working[i]
    trig_a[i][8] = q9_working[i]
    trig_a[i][9] = q10_working[i]
    trig_a[i][10] = q11_working[i]
    trig_a[i][11] = q12_working[i]
    trig_a[i][14] = q15_working[i]

# ---------- TRIG Tests 7–8 (harder extension) ----------
# Same 15-question format, but compound angles, multi-angle equations,
# non-acute exact ratios, harder identities, and phase-shifted sketches.

_hard_t7_q1_fig = right_triangle_svg(
    'x m', '12.4 m', None, '37°15′',
    caption='Given right triangle: find the adjacent side',
    context='opposite = 12.4 m; adjacent = x')
_hard_t8_q1_fig = right_triangle_svg(
    '9.6 m', None, 'x m', '21°40′',
    caption='Given right triangle: find the hypotenuse',
    context='adjacent = 9.6 m; hypotenuse = x')

trig_q.append([
 (r'Opposite \(12.4\) m and angle \(37^\circ15\'\). Find the adjacent side to 2 d.p.' + _hard_t7_q1_fig,
  ['(A) \(9.41\) m', '(B) \(16.31\) m', '(C) \(20.52\) m', '(D) \(7.48\) m', '(E) \(15.55\) m']),
 (r'The reference angle for \(\theta=\dfrac{17\pi}{12}\) is',
  [r'(A) \(\dfrac{\pi}{12}\)', r'(B) \(\dfrac{5\pi}{12}\)', r'(C) \(\dfrac{7\pi}{12}\)', r'(D) \(\dfrac{\pi}{6}\)', r'(E) \(\dfrac{\pi}{3}\)']),
 (r'If \(\sin\theta<0\), \(\cos\theta<0\) and \(\cot\theta>0\), then \(\theta\) is in quadrant',
  ['(A) 1', '(B) 2', '(C) 3', '(D) 4', '(E) impossible']),
 (r'Convert \(-\dfrac{11\pi}{6}\) to a positive degree measure in \([0^\circ,360^\circ)\).',
  ['(A) \(330^\circ\)', '(B) \(210^\circ\)', '(C) \(150^\circ\)', '(D) \(30^\circ\)', '(E) \(390^\circ\)']),
 (r'Starting from \(y=\sin x\): amplitude \(2\), period \(\pi\), phase shift \(\dfrac{\pi}{6}\) left, down \(1\). The equation is',
  [r'(A) \(2\sin\!\left(2x+\dfrac{\pi}{3}\right)-1\)',
   r'(B) \(2\sin\!\left(2x-\dfrac{\pi}{3}\right)-1\)',
   r'(C) \(2\sin\!\left(x+\dfrac{\pi}{6}\right)-1\)',
   r'(D) \(2\sin\!\left(\dfrac{x}{2}+\dfrac{\pi}{6}\right)-1\)',
   r'(E) \(\sin\!\left(2x+\dfrac{\pi}{6}\right)-1\)']),
 (r'Simplify \(\dfrac{1-\cos 2\theta}{\sin 2\theta}\cdot\cot\theta\).',
  [r'(A) \(1\)', r'(B) \(\tan\theta\)', r'(C) \(\cot\theta\)', r'(D) \(\sin\theta\)', r'(E) \(0\)']),
 r'From a point \(85\) m from the base of a cliff, the angle of elevation to the top is \(52^\circ20\'\). Find the cliff height to the nearest metre.',
 r'If \(\sin\theta=-\dfrac{5}{13}\) and \(\theta\) is in Quadrant III: (i) draw a labelled diagram in standard position; (ii) find the exact value of \(\sec\theta\).',
 r'Find all \(x\) in degrees if \(\cos(90^\circ-3x)=\sin(2x+15^\circ)\) and \(0^\circ\le x\le90^\circ\).',
 r'Find the exact value of \(\sin 15^\circ\) using an angle-difference identity.',
 r'Solve \(2\cos 2\theta=\sqrt{3}\) for \(0^\circ\le\theta\le360^\circ\). Give exact answers in degrees.',
 r'Solve \(\tan 2\theta=-1\) for \(0\le\theta\le\pi\). Give exact answers in radians.',
 r'Sketch \(y=2\sin\!\left(2x-\dfrac{\pi}{3}\right)\) for \(0\le x\le\pi\) and state amplitude, period and phase shift.',
 r'Prove \(\dfrac{\sin 2\theta}{1+\cos 2\theta}=\tan\theta\).',
 r'Solve \(2\sin^2\theta-3\sin\theta+1=0\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
])

trig_q.append([
 (r'Adjacent \(9.6\) m and angle \(21^\circ40\'\). Find the hypotenuse to 2 d.p.' + _hard_t8_q1_fig,
  ['(A) \(8.93\) m', '(B) \(10.33\) m', '(C) \(25.96\) m', '(D) \(3.81\) m', '(E) \(9.60\) m']),
 (r'Reference angle for \(\theta=-250^\circ\)?',
  ['(A) \(70^\circ\)', '(B) \(110^\circ\)', '(C) \(250^\circ\)', '(D) \(20^\circ\)', '(E) \(40^\circ\)']),
 (r'If \(\csc\theta>0\) and \(\sec\theta<0\), \(\theta\) lies in quadrant',
  ['(A) 1', '(B) 2', '(C) 3', '(D) 4', '(E) none']),
 (r'Convert \(495^\circ\) to an equivalent radian measure in \([0,2\pi)\).',
  [r'(A) \(\dfrac{3\pi}{4}\)', r'(B) \(\dfrac{11\pi}{4}\)', r'(C) \(\dfrac{7\pi}{4}\)', r'(D) \(\dfrac{5\pi}{4}\)', r'(E) \(\dfrac{\pi}{4}\)']),
 (r'\(y=\cos x\): amplitude \(3\), period \(\dfrac{2\pi}{3}\), right shift \(\dfrac{\pi}{9}\), up \(2\):',
  [r'(A) \(3\cos\!\left(3x-\dfrac{\pi}{3}\right)+2\)',
   r'(B) \(3\cos\!\left(3x+\dfrac{\pi}{3}\right)+2\)',
   r'(C) \(3\cos\!\left(\dfrac{x}{3}-\dfrac{\pi}{9}\right)+2\)',
   r'(D) \(3\cos\!\left(3x-\dfrac{\pi}{9}\right)+2\)',
   r'(E) \(\cos\!\left(3x-\dfrac{\pi}{3}\right)+2\)']),
 (r'Simplify \(\sin(\pi-\theta)\cos\!\left(\dfrac{\pi}{2}-\theta\right)-\cos(\pi-\theta)\sin\!\left(\dfrac{\pi}{2}-\theta\right)\).',
  [r'(A) \(1\)', r'(B) \(-1\)', r'(C) \(\sin 2\theta\)', r'(D) \(\cos 2\theta\)', r'(E) \(0\)']),
 r'A wire from the top of a \(18\) m pole makes an angle of \(34^\circ\) with the ground. Find the length of the wire to the nearest \(0.1\) m.',
 r'If \(\cos\theta=\dfrac{8}{17}\) and \(\theta\) is in Quadrant IV: (i) draw a diagram; (ii) find exact \(\tan\theta\).',
 r'Find all \(x\) if \(\sin(3x-10^\circ)=\cos(2x+20^\circ)\) and \(0^\circ\le x\le90^\circ\).',
 r'Find the exact value of \(\cos 75^\circ\) using an angle-sum identity.',
 r'Solve \(\sin 2\theta=\dfrac{\sqrt{3}}{2}\) for \(0^\circ\le\theta\le180^\circ\). Exact answers in degrees.',
 r'Solve \(2\cos^2\theta+\cos\theta-1=0\) for \(0\le\theta\le 2\pi\). Exact answers in radians.',
 r'Sketch \(y=-3\cos\!\left(x+\dfrac{\pi}{4}\right)\) for \(-\pi\le x\le\pi\) and state amplitude, period and phase shift.',
 r'Prove \(\tan\theta+\cot\theta=\sec\theta\csc\theta\).',
 r'Solve \(\cos 2\theta=\cos\theta\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
])

_hard_t7_q8_svg = f'''<div class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300"
 role="img" aria-label="Quadrant three reference triangle for sine negative five thirteenths"
 style="width:100%;max-width:560px;height:auto;background:#fff;border:1px solid #d8dee7;border-radius:8px">
{_svg_text(22, 25, 'QIII reference triangle', anchor='start', size=15, weight='bold', fill='#1B3A5C')}
<line x1="35" y1="150" x2="450" y2="150" stroke="#1f2937" stroke-width="2"/>
<line x1="270" y1="275" x2="270" y2="42" stroke="#1f2937" stroke-width="2"/>
{_svg_text(454, 145, 'x', anchor='start')}{_svg_text(280, 48, 'y', anchor='start')}
<line x1="270" y1="150" x2="155" y2="250" stroke="#185FA5" stroke-width="3"/>
<line x1="155" y1="250" x2="155" y2="150" stroke="#1B3A5C" stroke-width="3"/>
<line x1="155" y1="150" x2="270" y2="150" stroke="#1B3A5C" stroke-width="3"/>
<path d="M 175 150 L 175 170 L 155 170" fill="none" stroke="#1B3A5C" stroke-width="2"/>
{_svg_text(205, 210, 'r = 13', anchor='end', fill='#185FA5')}
{_svg_text(145, 210, 'y = −5', anchor='end')}
{_svg_text(212, 140, 'x = −12')}
{_svg_text(150, 268, '(−12, −5)', anchor='end', size=13, fill='#15803d')}
</svg></div>'''

_hard_t8_q8_svg = right_triangle_svg(
    '8', '15', '17', 'θ',
    caption='QIV magnitudes for cos θ = 8/17',
    context='adj = 8, |opp| = 15, hyp = 17; tan is negative in QIV')

trig_a.append([
 r'(B) \(16.31\) m (\(12.4/\tan37^\circ15\'\)).',
 r'(B) \(\dfrac{5\pi}{12}\) (\(\dfrac{17\pi}{12}=\pi+\dfrac{5\pi}{12}\), so reference \(\dfrac{5\pi}{12}\)).',
 r'(C) Quadrant 3 (\(\sin,\cos\) both negative \(\Rightarrow\) QIII; \(\cot=\cos/\sin>0\)).',
 r'(D) \(30^\circ\) (\(-\dfrac{11\pi}{6}+2\pi=\dfrac{\pi}{6}\)).',
 r'(A) \(2\sin\!\left(2x+\dfrac{\pi}{3}\right)-1\) (period \(\pi\Rightarrow b=2\); left shift \(\pi/6\) means \(2x+\pi/3\)).',
 r'(A) \(1\) (use \(1-\cos2\theta=2\sin^2\theta\), \(\sin2\theta=2\sin\theta\cos\theta\)).',
 r'''Height \(h\) is opposite \(52^\circ20'\) with adjacent \(85\) m, so \(\tan52^\circ20'=\dfrac{h}{85}\).
\[
\begin{aligned}
h&=85\tan52^\circ20'\\
&=85\tan(52.333\ldots^\circ)\\
&=85(1.2953\ldots)\\
&=110.10\ldots
\end{aligned}
\]
\[\boxed{h\approx 110\text{ m}}\]''',
 r'''In Quadrant III, \(x<0\) and \(y<0\). With \(\sin\theta=\dfrac{y}{r}=-\dfrac{5}{13}\), take \(r=13\), \(y=-5\).
Then \(|x|=\sqrt{13^2-5^2}=12\), so \(x=-12\). Therefore
\(\displaystyle\sec\theta=\dfrac{r}{x}=-\dfrac{13}{12}\).
''' + _hard_t7_q8_svg,
 r'''Use \(\cos(90^\circ-3x)=\sin 3x\).
\[
\begin{aligned}
\sin 3x&=\sin(2x+15^\circ)\\
3x&=2x+15^\circ\quad\text{or}\quad 3x=180^\circ-(2x+15^\circ)\\
x&=15^\circ\quad\text{or}\quad 5x=165^\circ\Rightarrow x=33^\circ.
\end{aligned}
\]
Both lie in \([0^\circ,90^\circ]\).
\[\boxed{x=15^\circ,\ 33^\circ}\]''',
 r'''\[
\begin{aligned}
\sin15^\circ&=\sin(45^\circ-30^\circ)\\
&=\sin45^\circ\cos30^\circ-\cos45^\circ\sin30^\circ\\
&=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}-\frac{\sqrt2}{2}\cdot\frac12\\
&=\frac{\sqrt6-\sqrt2}{4}.
\end{aligned}
\]
\[\boxed{\sin15^\circ=\dfrac{\sqrt6-\sqrt2}{4}}\]''',
 r'''Because the argument is \(2\theta\), use \(0^\circ\le 2\theta\le720^\circ\). With \(\cos2\theta=\dfrac{\sqrt3}{2}\),
reference angle \(30^\circ\) and cosine positive in QI, QIV:
\[
\begin{aligned}
2\theta&=30^\circ,\ 330^\circ,\ 390^\circ,\ 690^\circ\\
\theta&=15^\circ,\ 165^\circ,\ 195^\circ,\ 345^\circ.
\end{aligned}
\]
\[\boxed{\theta=15^\circ,\ 165^\circ,\ 195^\circ,\ 345^\circ}\]''',
 r'''\(\tan2\theta=-1\) with \(0\le2\theta\le2\pi\). Reference \(\dfrac{\pi}{4}\); tangent negative in QII, QIV:
\[
\begin{aligned}
2\theta&=\frac{3\pi}{4},\ \frac{7\pi}{4}\\
\theta&=\frac{3\pi}{8},\ \frac{7\pi}{8}.
\end{aligned}
\]
\[\boxed{\theta=\tfrac{3\pi}{8},\ \tfrac{7\pi}{8}}\]''',
 r'''Amplitude \(=2\); period \(=\pi\); phase shift \(=\dfrac{\pi}{6}\) to the right
(rewrite \(2x-\pi/3=2\bigl(x-\pi/6\bigr)\)).''',
 r'''\[
\begin{aligned}
\text{LHS}&=\frac{\sin2\theta}{1+\cos2\theta}
=\frac{2\sin\theta\cos\theta}{2\cos^2\theta}
=\frac{\sin\theta}{\cos\theta}
=\tan\theta=\text{RHS}.
\end{aligned}
\]''',
 r'''Treat as a quadratic in \(\sin\theta\):
\[
\begin{aligned}
(2\sin\theta-1)(\sin\theta-1)&=0\\
\sin\theta&=\dfrac12\quad\text{or}\quad\sin\theta=1.
\end{aligned}
\]
\(\sin\theta=\tfrac12\Rightarrow\theta=30^\circ,150^\circ\); \(\sin\theta=1\Rightarrow\theta=90^\circ\).
\[\boxed{\theta=30^\circ,\ 90^\circ,\ 150^\circ}\]''',
])

# Sketch blank + answer graph for Test 7 Q13
_spec7 = {
    'fn': lambda x: 2 * math.sin(2*x - math.pi/3),
    'xmin': 0, 'xmax': math.pi,
    'amp': 2, 'period': math.pi, 'step': math.pi/12,
    'period_tex': r'\pi',
    'caption': r'y = 2 sin(2x − π/3),  0 ≤ x ≤ π',
    'notes': ('midline y = 0', 'phase shift = π/6 to the right'),
}
_xs7 = [_spec7['xmin'] + j * _spec7['step']
        for j in range(round((_spec7['xmax']-_spec7['xmin'])/_spec7['step']) + 1)]
trig_q[-2][12] += blank_trig_grid(_spec7['xmin'], _spec7['xmax'], _xs7,
                                  caption=f"Sketching grid: {_spec7['caption']}")
_pts7 = [(x, 0.0 if abs(_spec7['fn'](x)) < 1e-10 else _spec7['fn'](x)) for x in _xs7]
_lab7 = [(x, y) for j, (x, y) in enumerate(_pts7)
         if abs(abs(y) - _spec7['amp']) < 1e-9 or j in (0, len(_pts7)-1)]
trig_a[-1][12] = (
    r'Amplitude \(=2\); period \(=\pi\); phase shift \(=\dfrac{\pi}{6}\) to the right '
    r'(since \(2x-\pi/3=2(x-\pi/6)\)).'
    + trig_plot(_spec7['fn'], _spec7['xmin'], _spec7['xmax'],
                -_spec7['amp']-0.6, _spec7['amp']+0.6, _pts7,
                midline=0, amplitude=_spec7['amp'], period=_spec7['period'],
                caption=_spec7['caption'], extra_notes=_spec7['notes'],
                yticks=[-_spec7['amp'], 0, _spec7['amp']], xticks=_xs7,
                label_points=_lab7)
)

trig_a.append([
 r'(B) \(10.33\) m (\(9.6/\cos21^\circ40\'\)).',
 r'(A) \(70^\circ\) (\(-250^\circ+360^\circ=110^\circ\) in QII; reference \(180^\circ-110^\circ=70^\circ\)).',
 r'(B) Quadrant 2 (\(\sin>0\Rightarrow\csc>0\); \(\cos<0\Rightarrow\sec<0\)).',
 r'(A) \(\dfrac{3\pi}{4}\) (\(495^\circ-360^\circ=135^\circ=\dfrac{3\pi}{4}\)).',
 r'(A) \(3\cos\!\left(3x-\dfrac{\pi}{3}\right)+2\) (period \(2\pi/3\Rightarrow b=3\); right \(\pi/9\Rightarrow 3(x-\pi/9)=3x-\pi/3\)).',
 r'(A) \(1\) (sine of difference: \(\sin\!\bigl((\pi-\theta)-(\pi/2-\theta)\bigr)=\sin(\pi/2)=1\)).',
 r'''The \(18\) m pole is opposite \(34^\circ\) and the wire \(L\) is the hypotenuse, so \(\sin34^\circ=\dfrac{18}{L}\).
\[
\begin{aligned}
L&=\frac{18}{\sin34^\circ}
=\frac{18}{0.55919\ldots}
=32.190\ldots
\end{aligned}
\]
\[\boxed{L\approx 32.2\text{ m}}\]''',
 r'''In Quadrant IV, \(x>0\) and \(y<0\). With \(\cos\theta=\dfrac{x}{r}=\dfrac{8}{17}\), take \(r=17\), \(x=8\).
Then \(|y|=\sqrt{17^2-8^2}=15\), so \(y=-15\). Therefore
\(\displaystyle\tan\theta=\dfrac{y}{x}=-\dfrac{15}{8}\).
''' + _hard_t8_q8_svg,
 r'''Rewrite \(\cos(2x+20^\circ)=\sin(70^\circ-2x)\), so \(\sin(3x-10^\circ)=\sin(70^\circ-2x)\).
\[
\begin{aligned}
3x-10^\circ&=70^\circ-2x+360^\circ k
\quad\text{or}\quad
3x-10^\circ&=180^\circ-(70^\circ-2x)+360^\circ k.
\end{aligned}
\]
First family: \(5x=80^\circ+360^\circ k\Rightarrow x=16^\circ+72^\circ k\). In \([0^\circ,90^\circ]\): \(x=16^\circ,\ 88^\circ\).
Second family: \(x=120^\circ+360^\circ k\) (outside the interval for integer \(k\)).
\[\boxed{x=16^\circ,\ 88^\circ}\]''',
 r'''\[
\begin{aligned}
\cos75^\circ&=\cos(45^\circ+30^\circ)\\
&=\cos45^\circ\cos30^\circ-\sin45^\circ\sin30^\circ\\
&=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}-\frac{\sqrt2}{2}\cdot\frac12
=\frac{\sqrt6-\sqrt2}{4}.
\end{aligned}
\]
\[\boxed{\cos75^\circ=\dfrac{\sqrt6-\sqrt2}{4}}\]''',
 r'''With \(0^\circ\le2\theta\le360^\circ\) and \(\sin2\theta=\dfrac{\sqrt3}{2}\), reference \(60^\circ\), sine positive in QI, QII:
\[
\begin{aligned}
2\theta&=60^\circ,\ 120^\circ\\
\theta&=30^\circ,\ 60^\circ.
\end{aligned}
\]
\[\boxed{\theta=30^\circ,\ 60^\circ}\]''',
 r'''Factor: \((2\cos\theta-1)(\cos\theta+1)=0\), so \(\cos\theta=\dfrac12\) or \(\cos\theta=-1\).
\[
\theta=\frac{\pi}{3},\ \frac{5\pi}{3}\qquad\text{or}\qquad\theta=\pi.
\]
\[\boxed{\theta=\tfrac{\pi}{3},\ \pi,\ \tfrac{5\pi}{3}}\]''',
 r'''Amplitude \(=3\); period \(=2\pi\); phase shift \(=\dfrac{\pi}{4}\) to the left; reflection in the \(x\)-axis (leading minus).''',
 r'''\[
\begin{aligned}
\text{LHS}&=\frac{\sin\theta}{\cos\theta}+\frac{\cos\theta}{\sin\theta}
=\frac{\sin^2\theta+\cos^2\theta}{\sin\theta\cos\theta}
=\frac{1}{\sin\theta\cos\theta}
=\sec\theta\csc\theta=\text{RHS}.
\end{aligned}
\]''',
 r'''Use \(\cos2\theta=2\cos^2\theta-1\), so \(\cos2\theta=\cos\theta\) becomes
\(2\cos^2\theta-1=\cos\theta\), i.e. \(2\cos^2\theta-\cos\theta-1=0\Rightarrow(2\cos\theta+1)(\cos\theta-1)=0\).
\[
\cos\theta=-\dfrac12\quad\text{or}\quad\cos\theta=1
\Rightarrow\theta=120^\circ,\ 240^\circ\quad\text{or}\quad\theta=0^\circ,\ 360^\circ.
\]
\[\boxed{\theta=0^\circ,\ 120^\circ,\ 240^\circ,\ 360^\circ}\]''',
])

# Sketch for Test 8 Q13
_spec8 = {
    'fn': lambda x: -3 * math.cos(x + math.pi/4),
    'xmin': -math.pi, 'xmax': math.pi,
    'amp': 3, 'period': 2*math.pi, 'step': math.pi/4,
    'period_tex': r'2\pi',
    'caption': r'y = −3 cos(x + π/4),  −π ≤ x ≤ π',
    'notes': ('midline y = 0', 'phase shift = π/4 to the left', 'reflection in the x-axis'),
}
_xs8 = [_spec8['xmin'] + j * _spec8['step']
        for j in range(round((_spec8['xmax']-_spec8['xmin'])/_spec8['step']) + 1)]
trig_q[-1][12] += blank_trig_grid(_spec8['xmin'], _spec8['xmax'], _xs8,
                                  caption=f"Sketching grid: {_spec8['caption']}")
_pts8 = [(x, 0.0 if abs(_spec8['fn'](x)) < 1e-10 else _spec8['fn'](x)) for x in _xs8]
_lab8 = [(x, y) for j, (x, y) in enumerate(_pts8)
         if abs(abs(y) - _spec8['amp']) < 1e-9 or j in (0, len(_pts8)-1)]
trig_a[-1][12] = (
    r'Amplitude \(=3\); period \(=2\pi\); phase shift \(=\dfrac{\pi}{4}\) left; vertical reflection.'
    + trig_plot(_spec8['fn'], _spec8['xmin'], _spec8['xmax'],
                -_spec8['amp']-0.6, _spec8['amp']+0.6, _pts8,
                midline=0, amplitude=_spec8['amp'], period=_spec8['period'],
                caption=_spec8['caption'], extra_notes=_spec8['notes'],
                yticks=[-_spec8['amp'], 0, _spec8['amp']], xticks=_xs8,
                label_points=_lab8)
)

write_pair('trig', 'Trigonometry', '1 hour per test',
           '../trig/2a_Trigonometry_Exam_Sample_Public_Holiday.pdf', trig_q, trig_a, TRIG_FMT)

# ---------- LIMITS + DIFF (8 tests x 18) ----------
# Sample tags:
# MC1 Limits, MC2 powers, MC3 powers rules 1-5, MC4 any fn rules 1-5,
# MC5 mixed, MC6 tangent powers
# L7(1) limits graph, L8(4) limits evaluate a+b, L9(2) powers,
# L10(3) powers rules, L11(3) 2nd deriv, L12(3) deriv at point,
# L13(3) any fn, L14(3) log at point, L15(3) trig at point,
# L16(3) mixed, L17(3) tangent any, L18(3) application of tangent
ld_q = [
[
 (r'[Limits] \(\displaystyle\lim_{x\to-2}\dfrac{x^3+8}{x^2+5}=\)',
  ['(A) \(0\)','(B) \(-\infty\)','(C) \(-2\)','(D) \(4\)','(E) DNE']),
 (r'[Powers of \(x\)] For \(f(x)=x^2-6x-1\), \(f\'(x)=0\) when \(x=\)',
  ['(A) \(-1\)','(B) \(6\)','(C) \(-3\)','(D) \(3\)','(E) \(0\)']),
 (r'[Rules 1–5] Derivative of \(y=(x^2-1)^{1/3}\) is',
  [r'(A) \(\dfrac{2x}{3(x^2-1)^{2/3}}\)',r'(B) \(\dfrac{2x}{3(x^2-1)^{4/3}}\)',r'(C) \(-\dfrac{2x}{3(x^2-1)^{4/3}}\)',r'(D) \(\dfrac{x}{(x^2-1)^{2/3}}\)',r'(E) other']),
 (r'[Any function] \(f(x)=\dfrac{x^2+3}{x^3}\) has \(f\'(x)=\)',
  [r'(A) \(2x-3x^2\)',r'(B) \(\dfrac{2x\cdot x^3-3x^2(x^2+3)}{x^6}\)',r'(C) \(\dfrac{-x^2-9}{x^4}\)',r'(D) \(\dfrac{2}{x}\)',r'(E) \(-\dfrac{x^2+9}{x^4}\)']),
 (r'[Mixed] Derivative of \(y=e^{x}\sin(3x)\) is',
  [r'(A) \(e^x(3\cos3x+\sin3x)\)',r'(B) \(3\cos3x\,e^x\)',r'(C) \(e^x\sin3x\)',r'(D) \(e^x(\cos3x-\sin3x)\)',r'(E) other']),
 (r'[Tangent] Tangent to \(y=3x^2\) at \(x=-1\) (gradient-intercept) is',
  [r'(A) \(y=-6x-3\)',r'(B) \(y=-6x+3\)',r'(C) \(y=6x-3\)',r'(D) \(y=6x+3\)',r'(E) \(y=-6x-6\)']),
 r'[Limits] Consider the graph drawn below. Determine whether \(\displaystyle\lim_{x\to1}f(x)\) exists. Justify your answer.'
 + limit_removable(hole_x=1, hole_y=4, filled_y=2, caption='Graph of y = f(x)'),
 r'[Limits] Evaluate, if they exist: (a) \(\displaystyle\lim_{x\to2}\dfrac{x^2-4}{x-2}\) (b) \(\displaystyle\lim_{x\to\infty}\dfrac{3x^2+6}{2x^2-7}\).',
 r'[Powers of \(x\)] Find \(\dfrac{dy}{dx}\) for \(y=\sqrt{x}+x\sqrt{x}\), leaving surds.',
 r'[Rules 1–5] Expand and differentiate \(f(x)=(x-1)(2x+3)\), then simplify fully.',
 r'[2nd derivative] Find the second derivative of \(y=\sqrt{x-1}\) and simplify.',
 r'[Derivative at a point] Find \(f\'(1)\) for \(f(x)=e^{x^2+2}\).',
 r'[Any function] Differentiate \(y=\dfrac{\ln(2x)}{x}\) and simplify.',
 r'[Logarithms] Find \(f\'(2)\) if \(f(x)=\ln(2x-3)\).',
 r'[Trigonometric] Find \(y\'\left(\dfrac{1}{6}\right)\) for \(y=\tan(2\pi x)\).',
 r'[Mixed] Differentiate \(y=e^{-x}(x^2-1)\) and simplify.',
 r'[Tangent] Find the equation of the tangent to \(y=x^3-3x\) at \(x=2\).',
 r'[Application of tangent] Find the point(s) on \(y=\dfrac12 x^2+9x+4\) where the tangent is parallel to \(y=3x-1\).',
],
[
 (r'[Limits] \(\displaystyle\lim_{x\to3}\dfrac{x^2-9}{x-3}=\)',
  ['(A) \(0\)','(B) \(3\)','(C) \(6\)','(D) DNE','(E) \(\infty\)']),
 (r'[Powers of \(x\)] \(f(x)=4x^3-12x\). Stationary points when \(f\'=0\):',
  [r'(A) \(x=0\) only',r'(B) \(x=\pm1\)',r'(C) \(x=\pm\sqrt{3}\)',r'(D) \(x=1,2\)',r'(E) none']),
 (r'[Rules 1–5] Derivative of \(y=(x^2+4)^{3/2}\) is',
  [r'(A) \(3x(x^2+4)^{1/2}\)',r'(B) \(\dfrac{3}{2}(x^2+4)^{1/2}\)',r'(C) \(3x\sqrt{x^2+4}\)',r'(D) \(2x(x^2+4)^{3/2}\)',r'(E) other']),
 (r'[Any function] \(y=\ln(5x^2+1)\). Then \(y\'=\)',
  [r'(A) \(\dfrac{1}{5x^2+1}\)',r'(B) \(\dfrac{10x}{5x^2+1}\)',r'(C) \(\dfrac{5x}{5x^2+1}\)',r'(D) \(10x\)',r'(E) \(\ln(10x)\)']),
 (r'[Mixed] \(f(x)=\dfrac{e^{x}}{x}\). \(f\'(x)=\)',
  [r'(A) \(e^x\)',r'(B) \(\dfrac{e^x(x-1)}{x^2}\)',r'(C) \(\dfrac{e^x}{x^2}\)',r'(D) \(e^x(1-x)\)',r'(E) \(\dfrac{xe^x-e^x}{x}\)']),
 (r'[Tangent] Tangent to \(y=e^{2x}\) at \(x=0\):',
  [r'(A) \(y=2x+1\)',r'(B) \(y=x+1\)',r'(C) \(y=2x\)',r'(D) \(y=e^{2}x\)',r'(E) \(y=2e^{2}x+1\)']),
 r'[Limits] The graph below shows \(y=f(x)\). Does \(\displaystyle\lim_{x\to0}f(x)\) exist? Justify. (This is the graph of \(y=\dfrac{|x|}{x}\) with the usual jump.)'
 + limit_jump(a=0, y_left=-1, y_right=1, caption='Graph of y = |x|/x'),
 r'[Limits] Evaluate, if they exist: (a) \(\displaystyle\lim_{x\to-1}\dfrac{x^2-1}{x+1}\) (b) \(\displaystyle\lim_{x\to\infty}\dfrac{5x+1}{x^2+4}\).',
 r'[Powers of \(x\)] Differentiate \(y=x^4-8x^2+3\) and find all stationary points.',
 r'[Rules 1–5] Differentiate \(y=\dfrac{3x+2}{x-4}\) and simplify.',
 r'[2nd derivative] Find \(f\'\'(x)\) for \(f(x)=x^4-4x^3+2\), then solve \(f\'\'(x)=0\).',
 r'[Derivative at a point] Find \(f\'(0)\) for \(f(x)=\cos(5x^2)\).',
 r'[Any function] Differentiate \(y=x\ln x\).',
 r'[Logarithms] Find \(f\'(e)\) for \(f(x)=\dfrac{\ln x}{x}\).',
 r'[Trigonometric] Find \(y\'\) for \(y=\sin^2(4x)\), then evaluate if required in exact form.',
 r'[Mixed] Differentiate \(y=(x^2+1)e^{x}\).',
 r'[Tangent] Find the equation of the tangent to \(y=\dfrac{1}{x}\) at \(x=2\).',
 r'[Application of tangent] A particle has \(s(t)=t^3-6t^2+9t\). Find the times when velocity is zero on \([0,5]\).',
],
[
 (r'[Limits] \(\displaystyle\lim_{x\to0}\dfrac{\sin x}{x}=\)',
  ['(A) \(0\)','(B) \(1\)','(C) \(\infty\)','(D) DNE','(E) \(-1\)']),
 (r'[Powers of \(x\)] \(f(x)=x^4-4x^3+2\). \(f\'\'(x)=0\) has solution(s)',
  [r'(A) \(x=0,2\)',r'(B) \(x=1\) only',r'(C) \(x=0\) only',r'(D) \(x=3\)',r'(E) none']),
 (r'[Rules 1–5] Derivative of \(y=\dfrac{1}{(3x-1)^4}\) is',
  [r'(A) \(\dfrac{-12}{(3x-1)^5}\)',r'(B) \(\dfrac{-4}{(3x-1)^5}\)',r'(C) \(\dfrac{12}{(3x-1)^5}\)',r'(D) \(\dfrac{-3}{(3x-1)^4}\)',r'(E) other']),
 (r'[Any function] \(y=\tan(2\pi x)\). \(y\'(\tfrac16)=\)',
  [r'(A) \(2\pi\sec^2(\pi/3)\)',r'(B) \(\sec^2(\pi/3)\)',r'(C) \(2\pi\)',r'(D) \(4\)',r'(E) \(4\pi\)']),
 (r'[Mixed] \(y=\dfrac{\ln x}{x}\). Critical points from \(y\'=0\) give',
  [r'(A) \(x=e\)',r'(B) \(x=1\)',r'(C) \(x=0\)',r'(D) \(x=e^{-1}\)',r'(E) none']),
 (r'[Tangent] Tangent to \(y=\dfrac{1}{x}\) at \(x=2\):',
  [r'(A) \(y=-\tfrac14 x+1\)',r'(B) \(y=-\tfrac14x+\tfrac34\)',r'(C) \(y=-\tfrac12x+1\)',r'(D) \(y=\tfrac12x\)',r'(E) \(y=-\tfrac14 x+\tfrac12\)']),
 r'[Limits] The graph below shows \(y=\ln x\) for \(x>0\). State whether \(\displaystyle\lim_{x\to0^+} \ln x\) exists as a real number. Justify.'
 + limit_one_sided(),
 r'[Limits] Evaluate, if they exist: (a) \(\displaystyle\lim_{x\to4}\dfrac{\sqrt{x}-2}{x-4}\) (b) \(\displaystyle\lim_{x\to\infty}\left(3+\dfrac{2}{x}\right)\).',
 r'[Powers of \(x\)] Differentiate \(y=4x^{3/2}-2x^{-1/2}\).',
 r'[Rules 1–5] Differentiate \(y=(2x-1)^5\).',
 r'[2nd derivative] Find \(y\'\'\) for \(y=e^{2x}+x^2\).',
 r'[Derivative at a point] Find \(f\'(1)\) for \(f(x)=(2x+1)^5\).',
 r'[Any function] Differentiate \(y=\dfrac{x^2+2}{x^2-2}\).',
 r'[Logarithms] Find \(f\'(1)\) if \(f(x)=\ln(x^2+1)\).',
 r'[Trigonometric] Find \(y\'\) for \(y=\sin(3x)e^{x}\).',
 r'[Mixed] Differentiate \(y=x^2\ln(3x)\).',
 r'[Tangent] Find the equation of the tangent to \(y=e^{x}+x\) at \(x=0\).',
 r'[Application of tangent] Find the coordinates where the tangent to \(y=x^3-6x^2+9x+1\) is horizontal.',
],
[
 (r'[Limits] \(\displaystyle\lim_{x\to1}\dfrac{x^3-1}{x-1}=\)',
  ['(A) \(0\)','(B) \(1\)','(C) \(2\)','(D) \(3\)','(E) DNE']),
 (r'[Powers of \(x\)] \(f(x)=2x^3-15x^2+36x\). Local max/min starts from solving',
  [r'(A) \(f=0\)',r'(B) \(f\'=0\)',r'(C) \(f\'\'=0\)',r'(D) \(f\'=f\)',r'(E) \(f\'\'=f\'\)']),
 (r'[Rules 1–5] Derivative of \(y=\sqrt{2x+5}\) is',
  [r'(A) \(\dfrac{1}{\sqrt{2x+5}}\)',r'(B) \(\dfrac{2}{\sqrt{2x+5}}\)',r'(C) \(\dfrac{1}{2\sqrt{2x+5}}\)',r'(D) \(\sqrt{2x+5}\)',r'(E) other']),
 (r'[Any function] \(y=\sin^2(4x)\). \(y\'=\)',
  [r'(A) \(2\sin4x\)',r'(B) \(8\sin4x\cos4x\)',r'(C) \(\sin8x\)',r'(D) \(4\sin4x\)',r'(E) \(2\sin4x\cos4x\)']),
 (r'[Mixed] Point on \(y=\dfrac12 x^2+9x+4\) where tangent is parallel to \(y=3x-1\):',
  [r'(A) \(x=-6\)',r'(B) \(x=3\)',r'(C) \(x=-3\)',r'(D) \(x=6\)',r'(E) \(x=0\)']),
 (r'[Tangent] Tangent to \(y=x^2-4x\) at \(x=3\):',
  [r'(A) \(y=2x-9\)',r'(B) \(y=2x-3\)',r'(C) \(y=6x-15\)',r'(D) \(y=2x+3\)',r'(E) \(y=-2x+3\)']),
 r'[Limits] Use the graph to state \(\displaystyle\lim_{x\to2}f(x)\) and \(f(2)\). '
 r'Hence determine whether \(f\) is continuous at \(x=2\), and justify your conclusion.'
 + limit_removable(xmin=-1, xmax=5, ymin=-1, ymax=5, hole_x=2, hole_y=3, filled_y=1,
                   caption='Graph of y = f(x)  (open circle: limit candidate; filled: f(2))'),
 r'[Limits] Evaluate, if they exist: (a) \(\displaystyle\lim_{x\to2}\dfrac{x^3-8}{x-2}\) (b) \(\displaystyle\lim_{x\to\infty}\dfrac{4x^3-1}{2x^3+5}\).',
 r'[Powers of \(x\)] Differentiate \(y=x^{5/2}+3x^{-2}\).',
 r'[Rules 1–5] Differentiate \(y=(3x-2)^4\).',
 r'[2nd derivative] Find \(y\'\'\) for \(y=\sqrt{x-1}\).',
 r'[Derivative at a point] Find \(f\'(0)\) for \(f(x)=e^{3x}\cos x\).',
 r'[Any function] Differentiate \(y=\dfrac{2x-1}{x+3}\).',
 r'[Logarithms] Find \(f\'(1)\) if \(f(x)=\ln(3x+1)\).',
 r'[Trigonometric] Find \(y\'\) for \(y=\tan(3x)\).',
 r'[Mixed] Differentiate \(y=e^{2x}\sin x\).',
 r'[Tangent] Find the equation of the tangent to \(y=\ln x\) at \(x=e\).',
 r'[Application of tangent] A particle has \(v(t)=3t^2-12t+9\). Find the times when it is at rest, and its acceleration at the first such time.',
],
[
 (r'[Limits] \(\displaystyle\lim_{x\to5}\dfrac{x^2-25}{x-5}=\)',
  ['(A) \(0\)','(B) \(5\)','(C) \(10\)','(D) DNE','(E) \(25\)']),
 (r'[Powers of \(x\)] For \(f(x)=x^3-3x\), \(f\'(x)=0\) when \(x=\)',
  [r'(A) \(0\) only',r'(B) \(\pm1\)',r'(C) \(\pm\sqrt{3}\)',r'(D) \(1,3\)',r'(E) none']),
 (r'[Rules 1–5] Derivative of \(y=(4x-1)^{-2}\) is',
  [r'(A) \(-8(4x-1)^{-3}\)',r'(B) \(-2(4x-1)^{-3}\)',r'(C) \(8(4x-1)^{-3}\)',r'(D) \(-4(4x-1)^{-3}\)',r'(E) other']),
 (r'[Any function] \(y=\ln(3x+2)\). Then \(y\'=\)',
  [r'(A) \(\dfrac{1}{3x+2}\)',r'(B) \(\dfrac{3}{3x+2}\)',r'(C) \(3\ln(3x+2)\)',r'(D) \(\dfrac{3x}{3x+2}\)',r'(E) \(3\)']),
 (r'[Mixed] Derivative of \(y=x^2e^{3x}\) is',
  [r'(A) \(e^{3x}(2x+3x^2)\)',r'(B) \(2xe^{3x}\)',r'(C) \(3x^2e^{3x}\)',r'(D) \(e^{3x}(2x+3)\)',r'(E) other']),
 (r'[Tangent] Tangent to \(y=x^3\) at \(x=1\):',
  [r'(A) \(y=3x-2\)',r'(B) \(y=3x+2\)',r'(C) \(y=x-2\)',r'(D) \(y=3x\)',r'(E) \(y=3x-1\)']),
 r'[Limits] The graph below has a jump discontinuity at \(x=0\). Does \(\displaystyle\lim_{x\to0}f(x)\) exist? Justify.'
 + limit_jump(a=0, y_left=2, y_right=-1, caption='Graph of y = f(x)  (jump at x = 0)'),
 r'[Limits] Evaluate, if they exist: (a) \(\displaystyle\lim_{x\to1}\dfrac{x^2+x-2}{x-1}\) (b) \(\displaystyle\lim_{x\to\infty}\dfrac{7x-1}{2x+5}\).',
 r'[Powers of \(x\)] Find \(\dfrac{dy}{dx}\) for \(y=x^{3/2}-4x^{-1}\).',
 r'[Rules 1–5] Differentiate \(y=(5-2x)^6\).',
 r'[2nd derivative] Find \(y\'\) and \(y\'\'\) for \(y=x^3e^{x}\).',
 r'[Derivative at a point] Find \(f\'(1)\) for \(f(x)=(x^2+1)^4\).',
 r'[Any function] Differentiate \(y=\dfrac{\sin x}{x}\).',
 r'[Logarithms] Find \(f\'(2)\) if \(f(x)=\ln(x^2-3)\).',
 r'[Trigonometric] Find \(f\'\left(\dfrac{\pi}{6}\right)\) for \(f(x)=\cos(2x)\).',
 r'[Mixed] Differentiate \(y=e^{x}\ln x\).',
 r'[Tangent] Find the equation of the tangent to \(y=\sqrt{x}\) at \(x=4\).',
 r'[Application of tangent] Find the point on \(y=x^2-6x+5\) where the tangent is parallel to \(y=-2x+1\).',
],
[
 (r'[Limits] \(\displaystyle\lim_{x\to-3}\dfrac{x^2-9}{x+3}=\)',
  ['(A) \(0\)','(B) \(-6\)','(C) \(6\)','(D) DNE','(E) \(-3\)']),
 (r'[Powers of \(x\)] For \(f(x)=3x^2-12x+7\), \(f\'(x)=0\) when \(x=\)',
  ['(A) \(0\)','(B) \(2\)','(C) \(4\)','(D) \(3\)','(E) \(1\)']),
 (r'[Rules 1–5] Derivative of \(y=(x^3-1)^{5}\) is',
  [r'(A) \(5(x^3-1)^4\)',r'(B) \(15x^2(x^3-1)^4\)',r'(C) \(5x^2(x^3-1)^4\)',r'(D) \(15(x^3-1)^4\)',r'(E) other']),
 (r'[Any function] \(f(x)=\dfrac{2x+1}{x-1}\). \(f\'(x)=\)',
  [r'(A) \(\dfrac{-3}{(x-1)^2}\)',r'(B) \(\dfrac{3}{(x-1)^2}\)',r'(C) \(\dfrac{2}{x-1}\)',r'(D) \(\dfrac{-1}{(x-1)^2}\)',r'(E) other']),
 (r'[Mixed] Derivative of \(y=\sin x\cos x\) is',
  [r'(A) \(\cos2x\)',r'(B) \(\sin2x\)',r'(C) \(1\)',r'(D) \(-\cos2x\)',r'(E) \(\tfrac12\sin2x\)']),
 (r'[Tangent] The equation of the tangent to \(y=e^{x}\) at \(x=0\), written in gradient-intercept form, is',
  [r'(A) \(y=x\)',r'(B) \(y=x+1\)',r'(C) \(y=e x\)',r'(D) \(y=1\)',r'(E) \(y=ex+1\)']),
 r'[Limits] The graph below approaches the same height from both sides at \(x=3\) (LHL \(=\) RHL \(=2\)), with \(f(3)\) possibly different. Does \(\displaystyle\lim_{x\to3}f(x)\) exist? Justify.'
 + limit_removable(xmin=-1, xmax=6, ymin=-1, ymax=5, hole_x=3, hole_y=2, filled_y=4,
                   caption='Graph of y = f(x)  (both sides → 2 at x = 3)'),
 r'[Limits] Evaluate, if they exist: (a) \(\displaystyle\lim_{x\to0}\dfrac{(x+2)^2-4}{x}\) (b) \(\displaystyle\lim_{x\to\infty}\dfrac{x^2+1}{3x^2-4}\).',
 r'[Powers of \(x\)] Differentiate \(y=6x^{5/3}-x^{-3}\).',
 r'[Rules 1–5] Differentiate \(y=\dfrac{1}{\sqrt{4x+1}}\).',
 r'[2nd derivative] Find \(y\'\'\) for \(y=\ln(2x+1)\).',
 r'[Derivative at a point] Find \(f\'(0)\) for \(f(x)=(3x+1)^4\).',
 r'[Any function] Differentiate \(y=x\cos x\).',
 r'[Logarithms] Find \(f\'(1)\) if \(f(x)=\ln(5x)\).',
 r'[Trigonometric] Find \(f\'\left(\dfrac{\pi}{4}\right)\) for \(f(x)=\tan x\).',
 r'[Mixed] Differentiate \(y=\dfrac{e^{x}}{\sin x}\).',
 r'[Tangent] Find the equation of the tangent to \(y=x^2+1\) at \(x=-1\).',
 r'[Application of tangent] Find the equations of all tangents to \(y=x^3-x\) that are parallel to \(y=2x\).',
],
]

ld_a = [
[
 r'(A) \(0\).',
 r'(D) \(x=3\).',
 r'(C) \(-\dfrac{2x}{3(x^2-1)^{4/3}}\).',
 r'(E) \(-\dfrac{x^2+9}{x^4}\).',
 r'(A) \(e^x(3\cos3x+\sin3x)\).',
 r'(A) \(y=-6x-3\).',
 r'Yes, LHL=RHL=4.',
 r'(a) \(4\) (b) \(\dfrac{3}{2}\).',
 r'\(\dfrac{1}{2\sqrt{x}}+\dfrac{3}{2}\sqrt{x}\).',
 r'\(f\'(x)=4x+1\).',
 r'\(y\'\'=-\dfrac{1}{4(x-1)\sqrt{x-1}}\).',
 r'\(f\'(1)=2e^{3}\).',
 r'\(y\'=\dfrac{1-\ln(2x)}{x^2}\).',
 r'\(f\'(2)=2\).',
 r'\(8\pi\).',
 r'\(e^{-x}(-x^2+2x+1)\).',
 r'\(y=9x-16\).',
 r'\(x=-6\); point \((-6,-23)\).',
],
[
 r'(C) \(6\).',
 r'(B) \(x=\pm1\).',
 r'(A)/(C) \(3x\sqrt{x^2+4}\).',
 r'(B) \(\dfrac{10x}{5x^2+1}\).',
 r'(B) \(\dfrac{e^x(x-1)}{x^2}\).',
 r'(A) \(y=2x+1\).',
 r'No (LHL=\(-1\), RHL=\(1\)).',
 r'(a) \(-2\) (b) \(0\).',
 r'\(y\'=4x(x^2-4)\); points \((-2,-13),(0,3),(2,-13)\).',
 r'\(y\'=\dfrac{-14}{(x-4)^2}\).',
 r'\(f\'\'=12x^2-24x\); \(x=0,2\).',
 r'\(0\).',
 r'\(1+\ln x\).',
 r'\(0\).',
 r'\(8\sin4x\cos4x\) (or \(4\sin8x\)).',
 r'\(e^x(x^2+2x+1)\).',
 r'\(y=-\dfrac14x+1\).',
 r'\(t=1,3\).',
],
[
 r'(B) \(1\).',
 r'(A) \(x=0,2\).',
 r'(A) \(\dfrac{-12}{(3x-1)^5}\).',
 r'(A) \(8\pi\).',
 r'(A) \(x=e\).',
 r'(A) \(y=-\tfrac14x+1\).',
 r'No; diverges to \(-\infty\).',
 r'(a) \(\dfrac14\) (b) \(3\).',
 r'\(6x^{1/2}+x^{-3/2}\).',
 r'\(10(2x-1)^4\).',
 r'\(y\'\'=4e^{2x}+2\).',
 r'\(810\).',
 r'\(y\'=\dfrac{-8x}{(x^2-2)^2}\).',
 r'\(1\).',
 r'\(e^x(3\cos3x+\sin3x)\).',
 r'\(2x\ln(3x)+x\).',
 r'\(y=2x+1\).',
 r'\((1,5)\) max, \((3,1)\) min.',
],
[
 r'(D) \(3\).',
 r'(B) \(f\'=0\).',
 r'(A) \(\dfrac{1}{\sqrt{2x+5}}\).',
 r'(B) \(8\sin4x\cos4x\) (equivalently \(4\sin8x\) via double-angle identity).',
 r'(A) \(x=-6\).',
 r'(A) \(y=2x-9\).',
 r'\(\displaystyle\lim_{x\to2}f(x)=3\), while \(f(2)=1\). Since these values are unequal, \(f\) is not continuous at \(x=2\).',
 r'(a) \(12\) (b) \(2\).',
 r'\(\dfrac52 x^{3/2}-6x^{-3}\).',
 r'\(12(3x-2)^3\).',
 r'\(y\'\'=-\dfrac{1}{4(x-1)\sqrt{x-1}}\).',
 r'\(3\).',
 r'\(y\'=\dfrac{7}{(x+3)^2}\).',
 r'\(\dfrac34\).',
 r'\(3\sec^2(3x)\).',
 r'\(e^{2x}(2\sin x+\cos x)\).',
 r'\(y=x/e\).',
 r'Rest at \(t=1,3\); \(a(1)=-6\).',
],
[
 r'(C) \(10\).',
 r'(B) \(\pm1\).',
 r'(A) \(-8(4x-1)^{-3}\).',
 r'(B) \(\dfrac{3}{3x+2}\).',
 r'(A) \(e^{3x}(2x+3x^2)\).',
 r'(A) \(y=3x-2\).',
 r'No; LHL \(\ne\) RHL for a jump.',
 r'(a) \(3\) (b) \(\dfrac72\).',
 r'\(\dfrac32 x^{1/2}+4x^{-2}\).',
 r'\(-12(5-2x)^5\).',
 r'\(y\'=e^{x}(x^3+3x^2)\); \(y\'\'=e^{x}(x^3+6x^2+6x)\).',
 r'\(32\).',
 r'\(\dfrac{x\cos x-\sin x}{x^2}\).',
 r'\(4\).',
 r'\(-\sqrt{3}\).',
 r'\(e^{x}(\ln x+\dfrac1x)\).',
 r'\(y=\dfrac14 x+1\).',
 r'\(x=2\); point \((2,-3)\).',
],
[
 r'(B) \(-6\).',
 r'(B) \(2\).',
 r'(B) \(15x^2(x^3-1)^4\).',
 r'(A) \(\dfrac{-3}{(x-1)^2}\).',
 r'(A) \(\cos2x\).',
 r'(B) \(y=x+1\).',
 r'Yes; LHL=RHL=2.',
 r'(a) \(4\) (b) \(\dfrac13\).',
 r'\(10x^{2/3}+3x^{-4}\).',
 r'\(-2(4x+1)^{-3/2}\).',
 r'\(y\'=\dfrac{2}{2x+1}\); \(y\'\'=\dfrac{-4}{(2x+1)^2}\).',
 r'\(12\).',
 r'\(\cos x-x\sin x\).',
 r'\(1\).',
 r'\(2\).',
 r'\(\dfrac{e^{x}(\sin x-\cos x)}{\sin^2 x}\).',
 r'\(y=-2x\).',
 r'\(y\'=3x^2-1=2\Rightarrow x=\pm1\). At both points \(y=0\), so the tangent equations are \(y=2x-2\) and \(y=2x+2\).',
],
]

# Tests 7–8 use denser algebra and closely matched distractors. Each MC item
# still has exactly one correct answer.
ld_q.extend([
[
 (r'[Limits] \(\displaystyle\lim_{x\to0}\dfrac{\sqrt{1+x}-\sqrt{1-x}}{x}=\)',
  [r'(A) \(0\)', r'(B) \(\dfrac12\)', r'(C) \(1\)', r'(D) \(2\)', r'(E) DNE']),
 (r'[Powers of \(x\)] On \(x>0\), \(f(x)=x+\dfrac4x\) has a stationary point when',
  [r'(A) \(x=-2\)', r'(B) \(x=2\)', r'(C) \(x=\pm2\)', r'(D) \(x=4\)', r'(E) \(x=\sqrt2\)']),
 (r'[Rules 1–5] The fully simplified derivative of \(y=\dfrac{x^2-1}{x^2+1}\) is',
  [r'(A) \(\dfrac{2x}{x^2+1}\)', r'(B) \(\dfrac{4x}{(x^2+1)^2}\)',
   r'(C) \(\dfrac{-4x}{(x^2+1)^2}\)', r'(D) \(\dfrac{2x(x^2-1)}{(x^2+1)^2}\)',
   r'(E) \(\dfrac{4x^2}{(x^2+1)^2}\)']),
 (r'[Any function] If \(y=\ln\sqrt{x^2+1}\), then \(y\'=\)',
  [r'(A) \(\dfrac{2x}{x^2+1}\)', r'(B) \(\dfrac{x}{\sqrt{x^2+1}}\)',
   r'(C) \(\dfrac{x}{x^2+1}\)', r'(D) \(\dfrac1{2(x^2+1)}\)',
   r'(E) \(\dfrac1{\sqrt{x^2+1}}\)']),
 (r'[Mixed] For \(y=e^{2x}\cos(3x)\), \(y\'=\)',
  [r'(A) \(e^{2x}(2\cos3x-3\sin3x)\)', r'(B) \(e^{2x}(2\cos3x+3\sin3x)\)',
   r'(C) \(e^{2x}(\cos3x-3\sin3x)\)', r'(D) \(e^{2x}(3\cos3x-2\sin3x)\)',
   r'(E) \(2e^{2x}(\cos3x-\sin3x)\)']),
 (r'[Tangent] The tangent to \(y=x\ln x\) at \(x=e^{-1}\), written in gradient-intercept form, is',
  [r'(A) \(y=0\)', r'(B) \(y=-e^{-1}\)', r'(C) \(y=x-e^{-1}\)',
   r'(D) \(y=e^{-1}\)', r'(E) \(y=-x-e^{-1}\)']),
 r'[Limits] The graph below has a removable discontinuity at \(x=2\). State '
 r'\(\displaystyle\lim_{x\to2}f(x)\), state \(f(2)\), and decide whether \(f\) is continuous at \(x=2\).'
 + limit_removable(xmin=-1, xmax=5, ymin=-2, ymax=5, hole_x=2, hole_y=3, filled_y=-1,
                   caption='Graph of y = f(x) near x = 2'),
 r'[Limits] Evaluate: (a) \(\displaystyle\lim_{x\to2}\dfrac{x^3-8}{\sqrt{x+2}-2}\) '
 r'(b) \(\displaystyle\lim_{x\to\infty}\left(\sqrt{9x^2+1}-3x\right)\).',
 r'[Powers of \(x\)] For \(x>0\), let \(f(x)=x^{5/2}-5x^{1/2}\). Find all stationary '
 r'points and classify each as a local maximum or local minimum.',
 r'[Rules 1–5] Differentiate \(y=\dfrac{(2x-1)^3}{x^2+1}\) and simplify fully.',
 r'[2nd derivative] If \(y=x^2e^x\), find \(y\'\'\), then solve \(y\'\'=0\).',
 r'[Derivative at a point] For \(f(x)=\ln(x^2+e^x)\), find \(f\'(0)\).',
 r'[Any function] Differentiate \(y=\dfrac{e^x}{x^2+1}\) and simplify.',
 r'[Logarithms] If \(f(x)=\ln(\ln x)\), find \(f\'(e)\).',
 r'[Trigonometric] If \(y=\sin^2(3x)\), find the value of \(y\'\) at \(x=\dfrac{\pi}{12}\).',
 r'[Mixed] Differentiate \(y=(x^2+1)e^{-2x}\) and factorise your answer.',
 r'[Tangent] Find the equation of the tangent to \(y=\ln(x^2+1)\) at \(x=1\).',
 r'[Application of tangent] Find every point on \(y=x^3-3x^2+2\) where the tangent '
 r'is parallel to \(y=3x+1\).',
],
[
 (r'[Limits] \(\displaystyle\lim_{x\to0}\dfrac{e^{2x}-1}{x}=\)',
  [r'(A) \(0\)', r'(B) \(1\)', r'(C) \(2\)', r'(D) \(e^2\)', r'(E) DNE']),
 (r'[Powers of \(x\)] For \(f(x)=x^2e^{-x}\), the stationary \(x\)-values are',
  [r'(A) \(0\) only', r'(B) \(2\) only', r'(C) \(0,2\)', r'(D) \(-2,0\)',
   r'(E) \(0,e^2\)']),
 (r'[Rules 1–5] The fully simplified derivative of \(y=\dfrac{3x+1}{(x^2+1)^2}\) is',
  [r'(A) \(\dfrac{-9x^2-4x+3}{(x^2+1)^3}\)',
   r'(B) \(\dfrac{-9x^2+4x+3}{(x^2+1)^3}\)',
   r'(C) \(\dfrac{3-12x^2}{(x^2+1)^3}\)',
   r'(D) \(\dfrac{3x+1-4x}{(x^2+1)^3}\)',
   r'(E) \(\dfrac{-9x^2-4x+3}{(x^2+1)^2}\)']),
 (r'[Any function] For \(x>0\), if \(y=\ln\!\left(\dfrac{x}{x+1}\right)\), then \(y\'=\)',
  [r'(A) \(\dfrac1x+\dfrac1{x+1}\)', r'(B) \(\dfrac1{x(x+1)}\)',
   r'(C) \(-\dfrac1{x(x+1)}\)', r'(D) \(\dfrac1{x+1}\)',
   r'(E) \(\dfrac{2x+1}{x(x+1)}\)']),
 (r'[Mixed] For \(y=e^{-x}\sin(2x)\), \(y\'=\)',
  [r'(A) \(e^{-x}(2\cos2x-\sin2x)\)', r'(B) \(e^{-x}(2\cos2x+\sin2x)\)',
   r'(C) \(e^{-x}(\cos2x-2\sin2x)\)', r'(D) \(e^x(2\cos2x-\sin2x)\)',
   r'(E) \(e^{-x}(2\sin2x-\cos2x)\)']),
 (r'[Tangent] The tangent to \(y=\dfrac{e^x}{x}\) at \(x=1\), written in gradient-intercept form, is',
  [r'(A) \(y=e\)', r'(B) \(y=ex\)', r'(C) \(y=e(x-1)\)',
   r'(D) \(y=x+e-1\)', r'(E) \(y=e(x+1)\)']),
 r'[Limits] The graph below approaches \(2\) from both sides at \(x=-1\), but its '
 r'filled point is at height \(4\). Find the limit and explain why the function is not continuous there.'
 + limit_removable(xmin=-4, xmax=3, ymin=-1, ymax=5, hole_x=-1, hole_y=2, filled_y=4,
                   caption='Graph of y = f(x) near x = −1'),
 r'[Limits] Evaluate: (a) \(\displaystyle\lim_{x\to0}\dfrac{\sin(5x)}{\sin(2x)}\) '
 r'(b) \(\displaystyle\lim_{x\to\infty}x\left(\sqrt{x^2+4}-x\right)\).',
 r'[Powers of \(x\)] For \(x>0\), let \(f(x)=2x^{3/2}+3x^{-1/2}\). Find and classify '
 r'its stationary point.',
 r'[Rules 1–5] Differentiate \(y=\dfrac{(\ln x)^2}{x}\) and factorise the numerator.',
 r'[2nd derivative] Find \(y\'\'\) for \(y=e^x\sin x\).',
 r'[Derivative at a point] For \(f(x)=\ln(1+e^{2x})\), find \(f\'(0)\).',
 r'[Any function] Differentiate \(y=\dfrac{\tan(3x)}{x^2+1}\).',
 r'[Logarithms] For \(x>1\), let \(f(x)=\ln\!\left(\dfrac{x^2+1}{x^2-1}\right)\). '
 r'Find the value of \(f\'(\sqrt2)\).',
 r'[Trigonometric] If \(y=e^{\sin x}\), find the value of \(y\'(\pi)\).',
 r'[Mixed] Differentiate \(y=x^2\ln x\,e^{-x}\) and factorise your answer.',
 r'[Tangent] Find the equation of the tangent to \(y=\dfrac{x}{x+1}\) at \(x=1\).',
 r'[Application of tangent] A particle has displacement \(s(t)=te^{-t}\), \(t\ge0\). '
 r'Find when it is at rest and its acceleration at that instant.',
],
])

# Match the official sample by assigning one unambiguous requested form to
# each relevant question. Never offer alternatives such as "index or surd".
_EXACT = r'Leave your answer in exact form.'
_EXACT_EACH = r'Leave each answer in exact form. If a limit does not exist, state this clearly.'
_INDEX = r'Leave your answer in index form.'
_SURD = r'Leave your answer in surd form.'
_SIMPLIFY = r'Simplify your answer fully.'
_GRADIENT_INTERCEPT = r'Write your answer in gradient-intercept form \(y=mx+b\).'

_diff_format_directions = [
    # Test 4
    [None, None, None, None, None, _GRADIENT_INTERCEPT, None, _EXACT_EACH,
     _INDEX, _SIMPLIFY, _SURD, _EXACT, _SIMPLIFY, _EXACT, _EXACT,
     _SIMPLIFY, _GRADIENT_INTERCEPT, _EXACT],
    # Test 5
    [None, None, None, None, None, _GRADIENT_INTERCEPT, None, _EXACT_EACH,
     _INDEX, _SIMPLIFY, _SIMPLIFY, _EXACT, _SIMPLIFY, _EXACT, _SURD,
     _SIMPLIFY, _GRADIENT_INTERCEPT, _EXACT],
    # Test 6
    [None, None, None, None, None, _GRADIENT_INTERCEPT, None, _EXACT_EACH,
     _INDEX, _SIMPLIFY, _SIMPLIFY, _EXACT, _SIMPLIFY, _EXACT, _EXACT,
     _SIMPLIFY, _GRADIENT_INTERCEPT, _GRADIENT_INTERCEPT],
    # Test 7
    [None, None, None, None, None, _GRADIENT_INTERCEPT, None, _EXACT_EACH,
     _EXACT, None,
     r'Simplify \(y\'\'\) fully and leave the roots of \(y\'\'=0\) in surd form.',
     _EXACT, _SIMPLIFY, _EXACT, _EXACT, None, _GRADIENT_INTERCEPT, _SURD],
    # Test 8
    [None, None, None, None, None, _GRADIENT_INTERCEPT, None, _EXACT_EACH,
     _SURD, None, _SIMPLIFY, _EXACT, _SIMPLIFY, _SURD, _EXACT, None,
     _GRADIENT_INTERCEPT, _EXACT],
]


def _add_diff_format_direction(question, direction):
    if direction is None:
        return question
    if isinstance(question, tuple):
        stem, choices = question
        text = stem
    else:
        text = question
    lower = text.lower()
    direction_lower = direction.lower()
    # Do not repeat an instruction that is already explicit in the question.
    if (
        ('gradient-intercept' in direction_lower and 'gradient-intercept' in lower)
        or ('surd form' in direction_lower and 'surd form' in lower)
        or ('index form' in direction_lower and 'index form' in lower)
        or ('exact form' in direction_lower and 'exact' in lower)
        or ('simplify' in direction_lower and ('simplif' in lower or 'factoris' in lower))
    ):
        return question
    if isinstance(question, tuple):
        return f'{text} {direction}', choices
    # Keep graph directions before the SVG so the full question reads naturally.
    figure_at = text.find('<div class="fig">')
    if figure_at >= 0:
        return text[:figure_at] + ' ' + direction + text[figure_at:]
    return text + ' ' + direction


assert len(_diff_format_directions) == 5
for _test, _directions in zip(ld_q[3:8], _diff_format_directions):
    assert len(_test) == len(_directions) == 18
    _test[:] = [
        _add_diff_format_direction(question, direction)
        for question, direction in zip(_test, _directions)
    ]

ld_a.extend([
[
 r'''(C). Rationalise:
\[
\frac{\sqrt{1+x}-\sqrt{1-x}}x
=\frac{2x}{x\left(\sqrt{1+x}+\sqrt{1-x}\right)}
\longrightarrow \frac{2}{2}=1.
\]''',
 r'''(B). \(f'(x)=1-\dfrac4{x^2}=0\Rightarrow x^2=4\). Since \(x>0\), \(\boxed{x=2}\).''',
 r'''(B). By the quotient rule,
\[
y'=\frac{2x(x^2+1)-2x(x^2-1)}{(x^2+1)^2}
=\boxed{\frac{4x}{(x^2+1)^2}}.
\]''',
 r'''(C). Since \(y=\tfrac12\ln(x^2+1)\),
\[
y'=\frac12\frac{2x}{x^2+1}=\boxed{\frac{x}{x^2+1}}.
\]''',
 r'''(A). Product and chain rules give
\[
y'=2e^{2x}\cos3x-3e^{2x}\sin3x
=\boxed{e^{2x}(2\cos3x-3\sin3x)}.
\]''',
 r'''(B). Here \(y(e^{-1})=-e^{-1}\) and \(y'=\ln x+1\), so \(y'(e^{-1})=0\).
The tangent is \(\boxed{y=-e^{-1}}\).''',
 r'''\[
\lim_{x\to2}f(x)=3,\qquad f(2)=-1.
\]
The two-sided limit exists, but it is not equal to the function value. Therefore \(f\) is not continuous at \(x=2\).''',
 r'''(a) Factor and rationalise:
\[
\frac{x^3-8}{\sqrt{x+2}-2}
=\frac{(x-2)(x^2+2x+4)(\sqrt{x+2}+2)}{x-2}
\longrightarrow 12(4)=\boxed{48}.
\]
(b) Rationalising gives
\[
\sqrt{9x^2+1}-3x=\frac1{\sqrt{9x^2+1}+3x}\longrightarrow\boxed0.
\]''',
 r'''\[
f'(x)=\frac52x^{3/2}-\frac52x^{-1/2}
=\frac52x^{-1/2}(x^2-1).
\]
For \(x>0\), the only stationary value is \(x=1\), where \(f(1)=-4\).
The derivative changes from negative to positive, so \(\boxed{(1,-4)}\) is a local minimum.''',
 r'''\[
\begin{aligned}
y'&=\frac{6(2x-1)^2(x^2+1)-2x(2x-1)^3}{(x^2+1)^2}\\
&=\boxed{\frac{2(2x-1)^2(x^2+x+3)}{(x^2+1)^2}}.
\end{aligned}
\]''',
 r'''\[
y'=e^x(x^2+2x),\qquad
y''=e^x(x^2+4x+2).
\]
Since \(e^x\ne0\), solve \(x^2+4x+2=0\):
\[
\boxed{x=-2\pm\sqrt2}.
\]''',
 r'''\[
f'(x)=\frac{2x+e^x}{x^2+e^x},
\qquad f'(0)=\frac1{1}=\boxed1.
\]''',
 r'''\[
y'=\frac{e^x(x^2+1)-2xe^x}{(x^2+1)^2}
=\boxed{\frac{e^x(x-1)^2}{(x^2+1)^2}}.
\]''',
 r'''\[
f'(x)=\frac1{x\ln x},\qquad
f'(e)=\boxed{\frac1e}.
\]''',
 r'''\[
y'=6\sin3x\cos3x=3\sin6x.
\]
At \(x=\pi/12\), \(6x=\pi/2\), so \(\boxed{y'=3}\).''',
 r'''\[
y'=2xe^{-2x}-2(x^2+1)e^{-2x}
=\boxed{2e^{-2x}(x-x^2-1)}.
\]''',
 r'''At \(x=1\), the point is \((1,\ln2)\), and
\[
y'=\frac{2x}{x^2+1}\Rightarrow y'(1)=1.
\]
Thus \(\boxed{y=x+\ln2-1}\), in gradient-intercept form.''',
 r'''Parallel tangents require
\[
3x^2-6x=3\Rightarrow x^2-2x-1=0
\Rightarrow x=1\pm\sqrt2.
\]
Using \(x^2=2x+1\) in \(y=x^3-3x^2+2\) gives \(y=1-x\). Hence the points are
\[
\boxed{(1+\sqrt2,-\sqrt2)\ \text{and}\ (1-\sqrt2,\sqrt2)}.
\]''',
],
[
 r'''(C). Using \(\displaystyle\lim_{u\to0}\frac{e^u-1}{u}=1\),
\[
\frac{e^{2x}-1}{x}=2\frac{e^{2x}-1}{2x}\longrightarrow\boxed2.
\]''',
 r'''(C). \(f'(x)=e^{-x}(2x-x^2)=xe^{-x}(2-x)\). Since \(e^{-x}\ne0\),
\(\boxed{x=0,2}\).''',
 r'''(A). Write \(y=(3x+1)(x^2+1)^{-2}\):
\[
y'=3(x^2+1)^{-2}-4x(3x+1)(x^2+1)^{-3}
=\boxed{\frac{-9x^2-4x+3}{(x^2+1)^3}}.
\]''',
 r'''(B). Expand the logarithm and simplify:
\[
y'=\frac1x-\frac1{x+1}=\boxed{\frac1{x(x+1)}}.
\]''',
 r'''(A). Product and chain rules give
\[
y'=-e^{-x}\sin2x+2e^{-x}\cos2x
=\boxed{e^{-x}(2\cos2x-\sin2x)}.
\]''',
 r'''(A). At \(x=1\), \(y=e\), while
\[
y'=\frac{e^x(x-1)}{x^2}\Rightarrow y'(1)=0.
\]
Thus the tangent is \(\boxed{y=e}\).''',
 r'''\[
\lim_{x\to-1}f(x)=2,\qquad f(-1)=4.
\]
The limit and function value differ, so \(f\) is not continuous at \(x=-1\).''',
 r'''(a) Using the standard sine limit,
\[
\frac{\sin5x}{\sin2x}
=\frac{\sin5x}{5x}\frac{2x}{\sin2x}\frac52
\longrightarrow\boxed{\frac52}.
\]
(b) Rationalise:
\[
x(\sqrt{x^2+4}-x)
=\frac{4x}{\sqrt{x^2+4}+x}
=\frac4{\sqrt{1+4/x^2}+1}\longrightarrow\boxed2.
\]''',
 r'''\[
f'(x)=3x^{1/2}-\frac32x^{-3/2}
=\frac32x^{-3/2}(2x^2-1).
\]
Thus \(x=1/\sqrt2\). The derivative changes from negative to positive, so this is a local minimum.
\[
\boxed{x=\frac{\sqrt2}{2}}.
\]''',
 r'''\[
y'=\frac{x(2\ln x/x)-(\ln x)^2}{x^2}
=\boxed{\frac{\ln x(2-\ln x)}{x^2}}.
\]''',
 r'''\[
y'=e^x(\sin x+\cos x),\qquad
y''=e^x(\sin x+\cos x)+e^x(\cos x-\sin x)
=\boxed{2e^x\cos x}.
\]''',
 r'''\[
f'(x)=\frac{2e^{2x}}{1+e^{2x}},
\qquad f'(0)=\frac2{2}=\boxed1.
\]''',
 r'''\[
y'=\boxed{\frac{3\sec^2(3x)(x^2+1)-2x\tan(3x)}{(x^2+1)^2}}.
\]''',
 r'''\[
f'(x)=\frac{2x}{x^2+1}-\frac{2x}{x^2-1}
=\frac{-4x}{(x^2+1)(x^2-1)}.
\]
At \(x=\sqrt2\), \(\boxed{f'(\sqrt2)=-\dfrac{4\sqrt2}{3}}\).''',
 r'''\[
y'=e^{\sin x}\cos x,\qquad
y'(\pi)=e^0(-1)=\boxed{-1}.
\]''',
 r'''\[
\begin{aligned}
y'&=e^{-x}(2x\ln x+x)-x^2\ln x\,e^{-x}\\
&=\boxed{xe^{-x}\bigl(2\ln x+1-x\ln x\bigr)}.
\end{aligned}
\]''',
 r'''At \(x=1\), \(y=\tfrac12\), and \(y'=\dfrac1{(x+1)^2}\), so the slope is \(\tfrac14\).
\[
\boxed{y-\frac12=\frac14(x-1)}
\]
(equivalently \(y=\tfrac14x+\tfrac14\)).''',
 r'''\[
v(t)=s'(t)=e^{-t}(1-t).
\]
Thus the particle is at rest at \(\boxed{t=1}\). Its acceleration is
\[
a(t)=v'(t)=e^{-t}(t-2),
\qquad \boxed{a(1)=-e^{-1}}.
\]''',
],
])

write_pair('limits-diff', 'Limits & Differentiation', '1 hour 20 minutes per test',
           '../limits-diff/2a_Differentiation_Exam_Sample.pdf', ld_q, ld_a, DIFF_FMT)

# ---------- INTEGRATION (6 tests x 16) ----------
# Sample tags:
# MC1 Primitive first step, MC2 power integral, MC3 definite power,
# MC4 area setup, MC5 exp/log/trig, MC6 substitution choice
# L7(2) applications of primitive, L8(2) power, L9(2) power,
# L10(3) area, L11(4) area intersections, L12(3) exp/log/trig,
# L13(2) exp/log/trig, L14(4) definite exp/log/trig,
# L15(4) substitution, L16(3) substitution
int_q = [
[
 (r'[Primitive] Best first step for \(\displaystyle\int\left(x-\dfrac{3}{x}\right)^2 dx\)?',
  ['(A) Substitution','(B) Expand','(C) Differentiate first','(D) Common denominator','(E) none']),
 (r'[Power of \(x\)] \(\displaystyle\int\left(\sqrt{x}+\dfrac{1}{x}\right)\,dx=\)',
  [r'(A) \(\tfrac{2}{3}x^{3/2}+\ln|x|+C\)',r'(B) \(\tfrac{3}{2}x^{3/2}+\ln|x|+C\)',r'(C) \(x^{1/2}-\dfrac{1}{x}+C\)',r'(D) \(\tfrac{2}{3}x^{3/2}-\dfrac{1}{x}+C\)',r'(E) other']),
 (r'[Definite] \(\displaystyle\int_{-1}^{2}(2x^3+2)\,dx=\)',
  ['(A) \(14\)','(B) \(25/2\)','(C) \(9\)','(D) \(12\)','(E) \(27/2\)']),
 (r'[Area] Area between \(f(x)=x^3-4x^2-x+4\) and the \(x\)-axis on its roots needs',
  ['(A) one integral only','(B) split where \(f\) changes sign','(C) ignore negatives','(D) differentiate','(E) none']),
 (r'[Exp/log/trig] \(\displaystyle\int 3\cos\!\left(\dfrac{x}{3}\right)dx=\)',
  [r'(A) \(9\sin(x/3)+C\)',r'(B) \(3\sin(x/3)+C\)',r'(C) \(\sin(3x)+C\)',r'(D) \(\tfrac13\sin(x/3)+C\)',r'(E) \(-3\sin(x/3)+C\)']),
 (r'[Substitution] For \(\displaystyle\int(6x-2)\sqrt{3x^2-2x}\,dx\), a good substitution is',
  [r'(A) \(u=6x-2\)',r'(B) \(u=3x^2-2x\)',r'(C) \(u=\sqrt{x}\)',r'(D) \(u=3x\)',r'(E) \(u=x^2\)']),
 r'[Applications of primitive] If \(\dfrac{dy}{dx}=1+3x\) and the curve passes through \((4,10)\), find \(y\).',
 r'[Power of \(x\)] Find \(\displaystyle\int(9x^5+3x^2)\,dx\) in positive-index form.',
 r'[Power of \(x\)] Find \(\displaystyle\int\left(3x^3-\dfrac{4}{x}\right)dx\).',
 r'[Area] Find the area between \(y=x-x^2\) and the \(x\)-axis from \(0\) to \(1\).'
 + area_under(lambda x: x - x*x, 0, 1, xmin=-0.3, xmax=1.4, ymin=-0.3, ymax=0.5,
              caption='y = x − x²', shade_label='area'),
 r'[Area] Use algebra to show that \(y=x^2\) and \(y=2-x^2\) meet at \((\pm1,1)\), then find the area of the region bounded by the graphs shown below.'
 + area_between(lambda x: x*x, lambda x: 2 - x*x, -1, 1, xmin=-1.8, xmax=1.8, ymin=-0.4, ymax=2.4,
                caption='y = x² and y = 2 − x²', label_f='y = x²', label_g='y = 2 − x²'),
 r'[Exp/log/trig] Find \(\displaystyle\int(e^{2x}+4x)\,dx\).',
 r'[Exp/log/trig] Find \(\displaystyle\int\dfrac{1}{5+x}\,dx\).',
 r'[Definite exp/log/trig] Evaluate \(\displaystyle\int_0^{\pi/2}(1-\sin2x)\,dx\).',
 r'[Substitution] Use \(u=x^2-3\) to evaluate \(\displaystyle\int 2x(x^2-3)^3\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int\dfrac{2x}{\sqrt{x^2+9}}\,dx\).',
],
[
 (r'[Primitive] Best first step for \(\displaystyle\int(x+1)^2\,dx\)?',
  ['(A) Expand','(B) Parts','(C) Partial fractions','(D) Differentiate','(E) none']),
 (r'[Power of \(x\)] \(\displaystyle\int x^{1/2}\,dx=\)',
  [r'(A) \(\tfrac{2}{3}x^{3/2}+C\)',r'(B) \(\tfrac{1}{2}x^{-1/2}+C\)',r'(C) \(x^{3/2}+C\)',r'(D) \(\tfrac{3}{2}x^{3/2}+C\)',r'(E) \(2x^{1/2}+C\)']),
 (r'[Definite] \(\displaystyle\int_0^{\pi/2}\cos x\,dx=\)',
  ['(A) \(0\)','(B) \(1\)','(C) \(-1\)','(D) \(\pi/2\)','(E) \(2\)']),
 (r'[Area] Area under \(y=\sqrt{x}\) from \(0\) to \(4\) equals',
  ['(A) \(8/3\)','(B) \(16/3\)','(C) \(4\)','(D) \(8\)','(E) \(2\)']),
 (r'[Exp/log/trig] \(\displaystyle\int e^{3x}\,dx=\)',
  [r'(A) \(3e^{3x}+C\)',r'(B) \(\tfrac13 e^{3x}+C\)',r'(C) \(e^{3x}+C\)',r'(D) \(e^{x}/3+C\)',r'(E) \(-3e^{3x}+C\)']),
 (r'[Substitution] Best \(u\) for \(\displaystyle\int x e^{x^2}\,dx\)',
  [r'(A) \(u=x\)',r'(B) \(u=x^2\)',r'(C) \(u=e^{x}\)',r'(D) \(u=xe^{x}\)',r'(E) \(u=2x\)']),
 r'[Applications of primitive] Gradient \(\dfrac{dy}{dx}=2x-5\), curve through \((3,1)\). Find the equation of the curve.',
 r'[Power of \(x\)] \(\displaystyle\int\left(x^4-\dfrac{1}{x^2}\right)dx\).',
 r'[Power of \(x\)] \(\displaystyle\int_1^{4}\dfrac{1}{\sqrt{x}}\,dx\).',
 r'[Area] Find the area between \(y=4-x^2\) and the \(x\)-axis (full positive region).'
 + area_under(lambda x: 4 - x*x, -2, 2, xmin=-2.6, xmax=2.6, ymin=-0.5, ymax=4.5,
              caption='y = 4 − x²', shade_label='area'),
 r'[Area] Find the area between \(y=x\) and \(y=x^2\) on \([0,1]\).'
 + area_between(lambda x: x, lambda x: x*x, 0, 1, xmin=-0.3, xmax=1.4, ymin=-0.3, ymax=1.3,
                caption='y = x and y = x²', label_f='y = x', label_g='y = x²'),
 r'[Exp/log/trig] \(\displaystyle\int(3\cos2x-2\sin x)\,dx\).',
 r'[Exp/log/trig] Find \(\displaystyle\int 5e^{-x}\,dx\).',
 r'[Definite exp/log/trig] Evaluate \(\displaystyle\int_0^{1}(e^{x}+2x)\,dx\).',
 r'[Substitution] For \(\displaystyle\int\cos2x\cdot(2\sin2x)^3\,dx\), choose \(u\) and finish.',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int\dfrac{\cos x}{\sin x}\,dx\).',
],
[
 (r'[Primitive] Best first step for \(\displaystyle\int\dfrac{x^2+1}{x}\,dx\)?',
  ['(A) Expand/split','(B) Substitution \(u=x^2+1\)','(C) Parts','(D) Differentiate','(E) none']),
 (r'[Power of \(x\)] \(\displaystyle\int(2x+1)^5\,dx=\)',
  [r'(A) \(\tfrac16(2x+1)^6+C\)',r'(B) \(\tfrac{1}{12}(2x+1)^6+C\)',r'(C) \(5(2x+1)^4+C\)',r'(D) \(\tfrac15(2x+1)^6+C\)',r'(E) \((2x+1)^6+C\)']),
 (r'[Definite] \(\displaystyle\int_0^{1}(3x^2-1)\,dx=\)',
  ['(A) \(0\)','(B) \(1\)','(C) \(2\)','(D) \(-1\)','(E) \(1/2\)']),
 (r'[Area] Area under \(y=e^{x}\) from \(0\) to \(1\) is',
  [r'(A) \(e-1\)',r'(B) \(e\)',r'(C) \(1\)',r'(D) \(e+1\)',r'(E) \(1/e\)']),
 (r'[Exp/log/trig] \(\displaystyle\int\sin(3x)\,dx=\)',
  [r'(A) \(-\tfrac13\cos3x+C\)',r'(B) \(\tfrac13\cos3x+C\)',r'(C) \(-\cos3x+C\)',r'(D) \(3\cos3x+C\)',r'(E) \(\sin3x+C\)']),
 (r'[Substitution] For \(\displaystyle\int\dfrac{4x}{x^2+1}\,dx\), a good \(u\) is',
  [r'(A) \(u=4x\)',r'(B) \(u=x^2+1\)',r'(C) \(u=x\)',r'(D) \(u=\ln x\)',r'(E) \(u=x^2\)']),
 r'[Applications of primitive] Curve with \(\dfrac{dy}{dx}=\dfrac{1}{x}\) through \((e,2)\). Find \(y\).',
 r'[Power of \(x\)] \(\displaystyle\int\left(6x^{1/2}-x^{-1/2}\right)dx\).',
 r'[Power of \(x\)] \(\displaystyle\int_{-2}^{1}(3x^2)\,dx\).',
 r'[Area] Find the area between \(y=\sin x\) and the \(x\)-axis from \(0\) to \(\pi\).'
 + area_under(math.sin, 0, math.pi, xmin=-0.4, xmax=math.pi + 0.4, ymin=-0.3, ymax=1.3,
              caption='y = sin x', shade_label='area'),
 r'[Area] Find the area enclosed by \(y=x^2\) and \(y=4x-x^2\).'
 + area_between(lambda x: x*x, lambda x: 4*x - x*x, 0, 2, xmin=-0.4, xmax=2.5, ymin=-0.4, ymax=4.5,
                caption='y = x² and y = 4x − x²', label_f='y = x²', label_g='y = 4x − x²'),
 r'[Exp/log/trig] \(\displaystyle\int\dfrac{4}{2x+1}\,dx\).',
 r'[Exp/log/trig] \(\displaystyle\int(2\sec^2 x-3\cos x)\,dx\).',
 r'[Definite exp/log/trig] Evaluate \(\displaystyle\int_0^{\pi/4}\sec^2 x\,dx\).',
 r'[Substitution] Use substitution to find \(\displaystyle\int\dfrac{x}{x^2+1}\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int(3x-1)(3x^2-2x)^4\,dx\).',
],
[
 (r'[Primitive] Best first step for \(\displaystyle\int\left(2+\dfrac{1}{x}\right)^2 dx\)?',
  ['(A) Expand','(B) Substitution only','(C) Parts','(D) Differentiate','(E) none']),
 (r'[Power of \(x\)] \(\displaystyle\int\dfrac{1}{x^2}\,dx=\)',
  [r'(A) \(\ln|x|+C\)',r'(B) \(-\dfrac{1}{x}+C\)',r'(C) \(\dfrac{1}{x}+C\)',r'(D) \(x^{-3}/(-3)+C\)',r'(E) \(2/x+C\)']),
 (r'[Definite] \(\displaystyle\int_0^{2}(x^2+1)\,dx=\)',
  ['(A) \(8/3\)','(B) \(14/3\)','(C) \(4\)','(D) \(6\)','(E) \(10/3\)']),
 (r'[Area] Area between \(y=2x\) and \(y=x^2\) from their positive intersection points equals',
  ['(A) \(2/3\)','(B) \(4/3\)','(C) \(1\)','(D) \(8/3\)','(E) \(2\)']),
 (r'[Exp/log/trig] \(\displaystyle\int\cos\!\left(\dfrac{x}{2}\right)dx=\)',
  [r'(A) \(2\sin(x/2)+C\)',r'(B) \(\tfrac12\sin(x/2)+C\)',r'(C) \(-\sin(x/2)+C\)',r'(D) \(2\cos(x/2)+C\)',r'(E) \(\sin x+C\)']),
 (r'[Substitution] For \(\displaystyle\int\sin x\cos x\,dx\), a good substitution is',
  [r'(A) \(u=\sin x\)',r'(B) \(u=x\)',r'(C) \(u=\tan x\)',r'(D) \(u=\sec x\)',r'(E) \(u=\cos^2 x\)']),
 r'[Applications of primitive] If \(y\'=4x^3-2\) and \(y(1)=5\), find \(y\).',
 r'[Power of \(x\)] \(\displaystyle\int\left(x^{3}-\dfrac{2}{x^{3}}\right)dx\).',
 r'[Power of \(x\)] \(\displaystyle\int_0^{1}(4x^3-1)\,dx\).',
 r'[Area] Find the area between \(y=\sqrt{x}\) and \(y=x\) from \(0\) to \(1\).'
 + area_between(math.sqrt, lambda x: x, 0, 1, xmin=-0.2, xmax=1.3, ymin=-0.2, ymax=1.2,
                caption='y = √x and y = x', label_f='y = √x', label_g='y = x'),
 r'[Area] Find the area between \(y=x^2\) and \(y=2x\).'
 + area_between(lambda x: x*x, lambda x: 2*x, 0, 2, xmin=-0.3, xmax=2.4, ymin=-0.3, ymax=4.3,
                caption='y = x² and y = 2x', label_f='y = x²', label_g='y = 2x'),
 r'[Exp/log/trig] \(\displaystyle\int(2e^{x}-3\sin x)\,dx\).',
 r'[Exp/log/trig] \(\displaystyle\int\dfrac{3}{x}\,dx\).',
 r'[Definite exp/log/trig] Evaluate \(\displaystyle\int_0^{\pi/2}\cos2x\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int\dfrac{6x}{x^2+4}\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int 2\cos x\sin^5 x\,dx\).',
],
[
 (r'[Primitive] Best first step for \(\displaystyle\int x(x+2)\,dx\)?',
  ['(A) Expand','(B) Substitution \(u=x+2\) only','(C) Parts','(D) Differentiate','(E) none']),
 (r'[Power of \(x\)] \(\displaystyle\int\left(x^{-1/2}+x^{3}\right)dx=\)',
  [r'(A) \(2x^{1/2}+\tfrac14 x^4+C\)',r'(B) \(\tfrac12 x^{-3/2}+3x^2+C\)',r'(C) \(2\sqrt{x}+x^4+C\)',r'(D) \(-\tfrac12 x^{-3/2}+\tfrac14 x^4+C\)',r'(E) other']),
 (r'[Definite] \(\displaystyle\int_{-1}^{1}(3x^2)\,dx=\)',
  ['(A) \(0\)','(B) \(1\)','(C) \(2\)','(D) \(3\)','(E) \(6\)']),
 (r'[Area] To find area between \(y=x^2-1\) and the \(x\)-axis from \(-1\) to \(1\), you should',
  ['(A) one integral of \(x^2-1\)','(B) take absolute value / split at roots','(C) ignore negatives','(D) differentiate','(E) none']),
 (r'[Exp/log/trig] \(\displaystyle\int\dfrac{1}{x}\,dx=\)',
  [r'(A) \(x+C\)',r'(B) \(\ln|x|+C\)',r'(C) \(1/x+C\)',r'(D) \(e^{x}+C\)',r'(E) \(x\ln x+C\)']),
 (r'[Substitution] For \(\displaystyle\int\dfrac{2x}{x^2+5}\,dx\), a good \(u\) is',
  [r'(A) \(u=2x\)',r'(B) \(u=x^2+5\)',r'(C) \(u=x^2\)',r'(D) \(u=\ln x\)',r'(E) \(u=5\)']),
 r'[Applications of primitive] \(\dfrac{dy}{dx}=3x^2-4\), through \((1,2)\). Find \(y\).',
 r'[Power of \(x\)] Find \(\displaystyle\int\left(5x^4-\dfrac{3}{x^2}\right)dx\).',
 r'[Power of \(x\)] Evaluate \(\displaystyle\int_1^{8}x^{-2/3}\,dx\).',
 r'[Area] Find the area under \(y=3x-x^2\) from \(x=0\) to \(x=3\).'
 + area_under(lambda x: 3*x - x*x, 0, 3, xmin=-0.4, xmax=3.4, ymin=-0.4, ymax=2.8,
              caption='y = 3x − x²', shade_label='area'),
 r'[Area] Show the intersections of \(y=x\) and \(y=x^3\) for \(x\ge0\), then find the enclosed area on \([0,1]\).'
 + area_between(lambda x: x, lambda x: x**3, 0, 1, xmin=-0.2, xmax=1.3, ymin=-0.2, ymax=1.2,
                caption='y = x and y = x³', label_f='y = x', label_g='y = x³'),
 r'[Exp/log/trig] Find \(\displaystyle\int(4\cos x-e^{x})\,dx\).',
 r'[Exp/log/trig] Find \(\displaystyle\int\dfrac{2}{3x+1}\,dx\).',
 r'[Definite exp/log/trig] Evaluate \(\displaystyle\int_0^{\pi/6}\sin3x\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int\dfrac{x}{\sqrt{x^2+1}}\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int 3\sin x\cos^2 x\,dx\).',
],
[
 (r'[Primitive] Best first step for \(\displaystyle\int\left(\sqrt{x}-\dfrac{1}{\sqrt{x}}\right)^2 dx\)?',
  ['(A) Expand','(B) Substitution first','(C) Parts','(D) Differentiate','(E) none']),
 (r'[Power of \(x\)] \(\displaystyle\int\left(2x^{3}-\dfrac{1}{x}\right)dx=\)',
  [r'(A) \(\tfrac12 x^4-\ln|x|+C\)',r'(B) \(6x^2+\dfrac{1}{x^2}+C\)',r'(C) \(\tfrac12 x^4+\ln|x|+C\)',r'(D) \(2x^4-\ln|x|+C\)',r'(E) other']),
 (r'[Definite] \(\displaystyle\int_0^{3}(2x+1)\,dx=\)',
  ['(A) \(9\)','(B) \(12\)','(C) \(15\)','(D) \(6\)','(E) \(10\)']),
 (r'[Area] Area between \(y=1-x^2\) and the \(x\)-axis (positive region) equals',
  ['(A) \(2/3\)','(B) \(4/3\)','(C) \(1\)','(D) \(2\)','(E) \(8/3\)']),
 (r'[Exp/log/trig] \(\displaystyle\int 2\sec^2 x\,dx=\)',
  [r'(A) \(2\tan x+C\)',r'(B) \(2\sec x+C\)',r'(C) \(\tan x+C\)',r'(D) \(2\sin x+C\)',r'(E) \(-\!2\cos x+C\)']),
 (r'[Substitution] For \(\displaystyle\int(4x-1)(2x^2-x)^5\,dx\), a good \(u\) is',
  [r'(A) \(u=4x-1\)',r'(B) \(u=2x^2-x\)',r'(C) \(u=x^2\)',r'(D) \(u=2x\)',r'(E) \(u=(2x^2-x)^5\)']),
 r'[Applications of primitive] \(\dfrac{dy}{dx}=e^{x}+2\), through \((0,3)\). Find \(y\).',
 r'[Power of \(x\)] Find \(\displaystyle\int\left(x^{-3}+4x\right)dx\).',
 r'[Power of \(x\)] Evaluate \(\displaystyle\int_{-1}^{2}(x^2-x)\,dx\).',
 r'[Area] Find the area under \(y=\cos x\) from \(0\) to \(\dfrac{\pi}{2}\).'
 + area_under(math.cos, 0, math.pi/2, xmin=-0.3, xmax=math.pi/2 + 0.4, ymin=-0.3, ymax=1.3,
              caption='y = cos x', shade_label='area'),
 r'[Area] Find the area enclosed by \(y=x^2\) and \(y=3x\).'
 + area_between(lambda x: x*x, lambda x: 3*x, 0, 3, xmin=-0.4, xmax=3.4, ymin=-0.4, ymax=9.5,
                caption='y = x² and y = 3x', label_f='y = x²', label_g='y = 3x'),
 r'[Exp/log/trig] Find \(\displaystyle\int\left(3e^{2x}-\sin x\right)dx\).',
 r'[Exp/log/trig] Find \(\displaystyle\int\dfrac{5}{x}\,dx\).',
 r'[Definite exp/log/trig] Evaluate \(\displaystyle\int_0^{\ln2}e^{x}\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int\dfrac{4x}{(x^2+1)^2}\,dx\).',
 r'[Substitution] Use substitution to evaluate \(\displaystyle\int\cos x\,e^{\sin x}\,dx\).',
],
]

int_a = [
[
 r'(B) Expand first.',
 r'(A) \(\tfrac23 x^{3/2}+\ln|x|+C\).',
 r'(E) \(27/2\).',
 r'(B) Split on sign changes.',
 r'(A) \(9\sin(x/3)+C\).',
 r'(B) \(u=3x^2-2x\).',
 r'\(y=x+\tfrac32 x^2-18\).',
 r'\(\tfrac32 x^6+x^3+C\).',
 r'\(\tfrac34 x^4-4\ln|x|+C\).',
 r'\(\dfrac16\).',
 r'Area \(=\dfrac{8}{3}\).',
 r'\(\tfrac12 e^{2x}+2x^2+C\).',
 r'\(\ln|5+x|+C\).',
 r'\(\dfrac{\pi}{2}-1\).',
 r'\(\tfrac12(x^2-3)^4+C\).',
 r'\(2\sqrt{x^2+9}+C\).',
],
[
 r'(A) Expand.',
 r'(A) \(\tfrac23 x^{3/2}+C\).',
 r'(B) \(1\).',
 r'(B) \(16/3\).',
 r'(B) \(\tfrac13 e^{3x}+C\).',
 r'(B) \(u=x^2\).',
 r'\(y=x^2-5x+7\).',
 r'\(\tfrac15 x^5+\dfrac{1}{x}+C\).',
 r'\(2\).',
 r'\(\dfrac{32}{3}\).',
 r'\(\dfrac16\).',
 r'\(\tfrac32\sin2x+2\cos x+C\).',
 r'\(-5e^{-x}+C\).',
 r'\(e-\tfrac12\).',
 r'\(u=\sin2x\Rightarrow \tfrac18\sin^4(2x)+C\).',
 r'\(\ln|\sin x|+C\).',
],
[
 r'(A) Expand/split.',
 r'(B) \(\tfrac{1}{12}(2x+1)^6+C\).',
 r'(A) \(0\).',
 r'(A) \(e-1\).',
 r'(A) \(-\tfrac13\cos3x+C\).',
 r'(B) \(u=x^2+1\).',
 r'\(y=\ln|x|+1\).',
 r'\(4x^{3/2}-2x^{1/2}+C\).',
 r'\(9\).',
 r'\(2\).',
 r'Intersections \(x=0,2\); area \(=\dfrac{8}{3}\).',
 r'\(2\ln|2x+1|+C\).',
 r'\(2\tan x-3\sin x+C\).',
 r'\(1\).',
 r'\(\tfrac12\ln(x^2+1)+C\).',
 r'\(\tfrac1{10}(3x^2-2x)^5+C\).',
],
[
 r'(A) Expand.',
 r'(B) \(-1/x+C\).',
 r'(B) \(14/3\).',
 r'(B) \(4/3\).',
 r'(A) \(2\sin(x/2)+C\).',
 r'(A) \(u=\sin x\).',
 r'\(y=x^4-2x+6\).',
 r'\(\tfrac14 x^4+\dfrac{1}{x^2}+C\).',
 r'\(0\).',
 r'\(\dfrac16\).',
 r'Intersections \(0,2\); area \(=\dfrac43\).',
 r'\(2e^{x}+3\cos x+C\).',
 r'\(3\ln|x|+C\).',
 r'\(0\).',
 r'\(3\ln(x^2+4)+C\).',
 r'\(\tfrac13\sin^6 x+C\).',
],
[
 r'(A) Expand.',
 r'(A) \(2x^{1/2}+\tfrac14 x^4+C\).',
 r'(C) \(2\).',
 r'(B) take absolute value / split at roots.',
 r'(B) \(\ln|x|+C\).',
 r'(B) \(u=x^2+5\).',
 r'\(y=x^3-4x+5\).',
 r'\(x^5+\dfrac{3}{x}+C\).',
 r'\([3x^{1/3}]_1^8=6-3=3\).',
 r'\(\dfrac92\).',
 r'Intersections \(0,1\); area \(=\dfrac14\).',
 r'\(4\sin x-e^{x}+C\).',
 r'\(\tfrac23\ln|3x+1|+C\).',
 r'\(\tfrac13\).',
 r'\(\sqrt{x^2+1}+C\).',
 r'\(-\cos^3 x+C\).',
],
[
 r'(A) Expand.',
 r'(A) \(\tfrac12 x^4-\ln|x|+C\).',
 r'(B) \(12\).',
 r'(B) \(4/3\).',
 r'(A) \(2\tan x+C\).',
 r'(B) \(u=2x^2-x\).',
 r'\(y=e^{x}+2x+2\).',
 r'\(-\dfrac{1}{2x^2}+2x^2+C\).',
 r'\(\dfrac32\).',
 r'\(1\).',
 r'Intersections \(0,3\); area \(=\dfrac92\).',
 r'\(\tfrac32 e^{2x}+\cos x+C\).',
 r'\(5\ln|x|+C\).',
 r'\(1\).',
 r'\(-\dfrac{2}{x^2+1}+C\).',
 r'\(e^{\sin x}+C\).',
],
]
write_pair('integration', 'Integration', '1 hour 20 minutes per test',
           '../integration/2a_Integration_Exam_Sample.pdf', int_q, int_a, INT_FMT)

print('tests written to', TESTS)
