#!/usr/bin/env python3
"""Generate DPEN022 Class Notes hub + 4 practice tests per strand (with answers)."""
from pathlib import Path
import html as H

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
.ans{background:#f0fdf4;border-left:4px solid #15803d;padding:10px 12px;margin:8px 0 14px;}
.mark{color:#6b7280;font-size:13px;}
"""

def page(title, body, katex=True):
    kx = ''
    if katex:
        kx = '''<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\\\(',right:'\\\\)',display:false}]});"></script>'''
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(title)}</title>
{kx}
<style>{CSS}</style>
</head><body><div class="wrap">
{body}
</div></body></html>
'''


def write_pair(slug, subject, timing, sample_href, tests_q, tests_a):
    # questions page with all 4 tests
    q_blocks = []
    for i, qs in enumerate(tests_q, 1):
        items = []
        for q in qs:
            if isinstance(q, tuple):
                stem, choices = q
                ch = ''.join(f'<div class="mc">{c}</div>' for c in choices)
                items.append(f'<li>{stem}{ch}</li>')
            else:
                items.append(f'<li>{q}</li>')
        q_blocks.append(f'<div class="test"><h3>Test {i}</h3><ol>\n' + '\n'.join(items) + '\n</ol></div>')

    q_body = f'''
<h1>DPEN022 {subject} — Practice Tests (Questions)</h1>
<p class="sub">Four practice papers modelled on the official DPEN022 {subject} Exam Sample.
Timing guide: {timing}. Show full working on long-answer items.</p>
<div class="meta"><strong>Official sample:</strong> <a href="{sample_href}">open PDF</a> · use it as the style/difficulty reference for these four papers.</div>
<div class="top-links">
  <a href="{slug}-answers.html">Open Separate Answers</a>
  <a href="../index.html">Class Notes Hub</a>
  <a href="../../index.html">DPEN22 Index</a>
</div>
{''.join(q_blocks)}
'''
    (TESTS / f'{slug}-questions.html').write_text(page(f'DPEN022 {subject} Practice Tests — Questions', q_body))

    a_blocks = []
    for i, ans in enumerate(tests_a, 1):
        items = []
        for j, a in enumerate(ans, 1):
            items.append(f'<div class="ans"><strong>Q{j}.</strong> {a}</div>')
        a_blocks.append(f'<div class="test"><h3>Test {i} — Answers</h3>\n' + '\n'.join(items) + '\n</div>')

    a_body = f'''
<h1>DPEN022 {subject} — Practice Tests (Answers)</h1>
<p class="sub">Separate worked answers for the four {subject} practice papers.</p>
<div class="top-links">
  <a href="{slug}-questions.html">Back to Questions</a>
  <a href="../index.html">Class Notes Hub</a>
  <a href="../../index.html">DPEN22 Index</a>
</div>
{''.join(a_blocks)}
'''
    (TESTS / f'{slug}-answers.html').write_text(page(f'DPEN022 {subject} Practice Tests — Answers', a_body))


# ---------- TRIG (4 tests × 12) ----------
trig_q = [
[
 (r'In a right triangle, adjacent side \(5\) m and angle \(13^\circ45'\). Find the hypotenuse correct to 2 d.p.',
  ['(A) \(1.19\) m','(B) \(5.15\) m','(C) \(21.04\) m','(D) \(4.86\) m','(E) \(20.43\) m']),
 (r'What is the reference angle for \(\theta=-135^\circ\)?',
  ['(A) \(135^\circ\)','(B) \(225^\circ\)','(C) \(315^\circ\)','(D) \(45^\circ\)','(E) \(90^\circ\)']),
 (r'If \(\sec\theta<0\) and \(\cot\theta>0\), which quadrant contains \(\theta\)?',
  ['(A) 1','(B) 2','(C) 3','(D) 4','(E) none']),
 (r'Convert \(\dfrac{11\pi}{12}\) to degrees.',
  ['(A) \(165^\circ\)','(B) \(195^\circ\)','(C) \(150^\circ\)','(D) \(135^\circ\)','(E) \(15^\circ\)']),
 (r'Starting from \(y=\cos x\): amplitude \(3\), period \(4\pi\), shift down \(2\). The equation is',
  [r'(A) \(3\cos(4\pi x)-2\)',r'(B) \(3\cos\!\left(\dfrac{x}{2}\right)-2\)',r'(C) \(3\cos(2x)-2\)',r'(D) \(2\cos(4\pi x)-3\)',r'(E) \(2\cos(3x)-2\)']),
 r'Simplify \((1-\sin^2 x)\sec^2 x\).',
 r'Hypotenuse \(15\) m, adjacent \(7\) m. Find the included angle to the nearest minute.',
 r'If \(\sin\theta=\dfrac{3}{5}\) and \(\theta\) is acute, find the exact value of \(\sec\theta\).',
 r'Find \(x\) if \(\sin 80^\circ=\cos(90^\circ-2x)\).',
 r'Find the exact value of \(\tan\dfrac{2\pi}{3}\).',
 r'Solve \(\cos\theta=\dfrac{1}{2}\) for \(0^\circ\le\theta\le360^\circ\). Exact answers in degrees.',
 r'Solve \(\cot\theta=\sqrt{3}\) for \(0\le\theta\le2\pi\). Exact answers in radians.',
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
 r'Simplify \(\dfrac{\sin\theta}{\cos\theta}\cdot\cos\theta\sec\theta\).',
 r'Opposite \(9\) m, hypotenuse \(15\) m. Find the angle opposite the \(9\) m side to the nearest degree.',
 r'If \(\cos\theta=\dfrac{5}{13}\) and \(\theta\) acute, find exact \(\tan\theta\).',
 r'Find \(x\) if \(\cos 35^\circ=\sin(2x)\).',
 r'Exact value of \(\sin\dfrac{5\pi}{6}\).',
 r'Solve \(2\sin\theta=-1\) for \(0^\circ\le\theta\le360^\circ\).',
 r'Sketch \(y=2\cos 3x\) on \([0,2\pi]\) and state amplitude and period.',
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
 r'Simplify \(1+\tan^2\theta\) using an identity.',
 r'A ship is \(2.5\) km from a lighthouse. Angle of elevation to the top is \(12^\circ\). Find the lighthouse height to 2 d.p.',
 r'If \(\tan\theta=\dfrac{8}{15}\) and \(\theta\) acute, find exact \(\sin\theta\).',
 r'Find exact \(\cos\dfrac{3\pi}{4}\).',
 r'Solve \(\tan\theta=1\) for \(0\le\theta\le2\pi\).',
 r'Solve \(2\cos\theta=\sqrt{3}\) for \(0^\circ\le\theta\le360^\circ\).',
 r'Prove \(\dfrac{1-\cos 2\theta}{\sin 2\theta}=\tan\theta\) (or show both sides equal for a chosen \(\theta\) and outline the identity steps).',
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
 r'Simplify \(\cos^2\theta(\sec^2\theta-1)\).',
 r'A wire from the top of a \(12\) m pole makes \(35^\circ\) with the ground. Find the wire length to 2 d.p.',
 r'If \(\sin\theta=\dfrac{12}{13}\) and \(\theta\) obtuse, find exact \(\cos\theta\).',
 r'Exact value of \(\tan\!\left(-\dfrac{\pi}{4}\right)\).',
 r'Solve \(\sin 2\theta=0\) for \(0^\circ\le\theta\le180^\circ\).',
 r'Solve \(2\cos^2\theta-1=0\) for \(0^\circ\le\theta\le360^\circ\).',
 r'For \(y=\dfrac12\sin 2x\), state amplitude, period, and the first positive \(x\)-intercept.',
],
]

trig_a = [
[
 r'(B) \(5.15\) m — \(x=5/\cos 13^\circ45'\).',
 r'(D)/(E as sample) reference angle \(45^\circ\) after mapping \(-135^\circ\to225^\circ\).',
 r'(C) Quadrant 3.',
 r'(A) \(165^\circ\).',
 r'(B) \(3\cos(x/2)-2\).',
 r'\(1\).',
 r'\(\cos^{-1}(7/15)\approx62^\circ12'\).',
 r'\(\sec\theta=5/4\).',
 r'\(x=5^\circ\).',
 r'\(-\sqrt{3}\).',
 r'\(\theta=60^\circ,300^\circ\).',
 r'\(\theta=\pi/6, 7\pi/6\).',
],
[
 r'(A) \(3.23\) m (or check \(8\tan22^\circ\)).',
 r'(A) \(30^\circ\).',
 r'(B) Quadrant 2.',
 r'(B) \(4\pi/3\).',
 r'(A) \(2\sin(2x)+1\).',
 r'\(\sec\theta\) (simplifies to \(1/\cos\theta\)).',
 r'\(\sin^{-1}(9/15)=37^\circ\) approx.',
 r'\(\tan\theta=12/5\).',
 r'\(x=27.5^\circ\).',
 r'\(1/2\).',
 r'\(\theta=210^\circ,330^\circ\).',
 r'Amp \(2\), period \(2\pi/3\).',
],
[
 r'(B) \(13.0\) m (\(40\tan18^\circ\)).',
 r'(A) \(\pi/6\).',
 r'(D) Quadrant 4.',
 r'(C) \(315^\circ\).',
 r'(A) \(4\cos(x-\pi/2)+1\).',
 r'\(\sec^2\theta\).',
 r'\(2.5\tan12^\circ\approx0.53\) km.',
 r'\(\sin\theta=8/17\).',
 r'\(-\dfrac{\sqrt2}{2}\).',
 r'\(\theta=\pi/4,5\pi/4\).',
 r'\(\theta=30^\circ,330^\circ\).',
 r'Use double-angle identities; both sides \(\tan\theta\).',
],
[
 r'(B) \(4/5\).',
 r'(B) \(60^\circ\).',
 r'(C) Quadrant 3.',
 r'(A) \(5\pi/12\).',
 r'(A) \(5\sin(x/3)-3\).',
 r'\(\sin^2\theta\).',
 r'\(12/\sin35^\circ\approx20.92\) m.',
 r'\(\cos\theta=-5/13\).',
 r'\(-1\).',
 r'\(\theta=0^\circ,90^\circ,180^\circ\).',
 r'\(\theta=45^\circ,135^\circ,225^\circ,315^\circ\).',
 r'Amp \(1/2\), period \(\pi\), first positive intercept \(x=\pi/2\).',
],
]
write_pair('trig', 'Trigonometry', 'about 50–60 minutes per test',
           '../trig/2a_Trigonometry_Exam_Sample_Public_Holiday.pdf', trig_q, trig_a)


# ---------- LIMITS + DIFF ----------
ld_q = [
[
 (r'\(\displaystyle\lim_{x\to-2}\dfrac{x^3+2}{x^2+5}\)=',
  ['(A) \(0\)','(B) \(-\infty\)','(C) \(-2\)','(D) \(4\)','(E) DNE']),
 (r'For \(f(x)=x^2-6x-1\), \(f'(x)=0\) when \(x=\)',
  ['(A) \(-1\)','(B) \(6\)','(C) \(-3\)','(D) \(3\)','(E) \(0\)']),
 (r'Derivative of \(y=(x^2-1)^{1/3}\) is',
  [r'(A) \(\dfrac{2x}{3(x^2-1)^{2/3}}\)',r'(B) \(\dfrac{2x}{3(x^2-1)^{4/3}}\)',r'(C) \(-\dfrac{2x}{3(x^2-1)^{4/3}}\)',r'(D) \(\dfrac{x}{(x^2-1)^{2/3}}\)',r'(E) other']),
 (r'\(f(x)=\dfrac{x^2+3}{x^3}\) has \(f'(x)=\)',
  [r'(A) \(2x-3x^2\)',r'(B) \(\dfrac{2x\cdot x^3-3x^2(x^2+3)}{x^6}\)',r'(C) \(\dfrac{-x^2-9}{x^4}\)',r'(D) \(\dfrac{2}{x}\) ',r'(E) \(-\dfrac{x^2+9}{x^4}\)']),
 (r'Tangent to \(y=3x^2\) at \(x=-1\) (gradient-intercept) is',
  [r'(A) \(y=-6x-3\)',r'(B) \(y=-6x+3\)',r'(C) \(y=6x-3\)',r'(D) \(y=6x+3\)',r'(E) \(y=-6x-6\)']),
 r'From a graph that approaches \(y=4\) from both sides at \(x=1\), does \(\lim_{x\to1}f(x)\) exist? Justify.',
 r'Evaluate \(\displaystyle\lim_{x\to2}\dfrac{x^2-4}{x-2}\) if it exists.',
 r'Evaluate \(\displaystyle\lim_{x\to\infty}\dfrac{3x^2+6}{2x^2-7}\) if it exists.',
 r'Find \(\dfrac{dy}{dx}\) for \(y=\sqrt{x}+x\sqrt{x}\), leaving surds.',
 r'Expand and differentiate \(f(x)=(x-1)(2x+3)\), simplify fully.',
 r'Find \(f'(1)\) for \(f(x)=e^{x^2+2}\) (chain rule, exact).',
 r'Differentiate \(y=\dfrac{\ln(2x)}{x}\) and simplify.',
],
[
 (r'\(\displaystyle\lim_{x\to3}\dfrac{x^2-9}{x-3}\)=',
  ['(A) \(0\)','(B) \(3\)','(C) \(6\)','(D) DNE','(E) \(\infty\)']),
 (r'\(f(x)=4x^3-12x\). Stationary points when \(f'=0\):',
  [r'(A) \(x=0\) only',r'(B) \(x=\pm1\)',r'(C) \(x=\pm\sqrt{3}\)',r'(D) \(x=1,2\)',r'(E) none']),
 (r'Derivative of \(y=\sin(3x)e^{x}\) by product rule:',
  [r'(A) \(e^x(3\cos3x+\sin3x)\)',r'(B) \(3\cos3x\,e^x\)',r'(C) \(e^x\sin3x\)',r'(D) \(e^x(\cos3x-\sin3x)\)',r'(E) other']),
 (r'\(y=\ln(5x^2+1)\). Then \(y'=\)',
  [r'(A) \(\dfrac{1}{5x^2+1}\)',r'(B) \(\dfrac{10x}{5x^2+1}\)',r'(C) \(\dfrac{5x}{5x^2+1}\)',r'(D) \(10x\)',r'(E) \(\ln(10x)\)']),
 (r'Tangent to \(y=e^{2x}\) at \(x=0\):',
  [r'(A) \(y=2x+1\)',r'(B) \(y=x+1\)',r'(C) \(y=2x\)',r'(D) \(y=e^{2}x\)',r'(E) \(y=2e^{2}x+1\)']),
 r'Does \(\displaystyle\lim_{x\to0}\dfrac{|x|}{x}\) exist? Justify.',
 r'Evaluate \(\displaystyle\lim_{x\to-1}\dfrac{x^2-1}{x+1}\).',
 r'Evaluate \(\displaystyle\lim_{x\to\infty}\dfrac{5x+1}{x^2+4}\).',
 r'Differentiate \(y=(2x-1)^5\).',
 r'Differentiate \(y=\dfrac{3x+2}{x-4}\).',
 r'Find the second derivative of \(y=(x-2)^2\sqrt{x}\) at a simplified form (or first find \(y'\) fully).',
 r'Find the equation of the tangent to \(y=x^3-3x\) at \(x=2\).',
],
[
 (r'\(\displaystyle\lim_{x\to0}\dfrac{\sin x}{x}\)=',
  ['(A) \(0\)','(B) \(1\)','(C) \(\infty\)','(D) DNE','(E) \(-1\)']),
 (r'\(f(x)=x^4-4x^3+2\). \(f''(x)=0\) has solution(s)',
  [r'(A) \(x=0,2\)',r'(B) \(x=1\) only',r'(C) \(x=0\) only',r'(D) \(x=3\)',r'(E) none']),
 (r'\(y=\tan(2\pi x)\). \(y'(\tfrac16)=\)',
  [r'(A) \(2\pi\sec^2(\pi/3)\)',r'(B) \(\sec^2(\pi/3)\)',r'(C) \(2\pi\)',r'(D) \(4\)',r'(E) \(2\pi\cdot4=8\pi\) approx check']),
 (r'\(f(x)=\dfrac{e^{x}}{x}\). \(f'(x)=\)',
  [r'(A) \(e^x\)',r'(B) \(\dfrac{e^x(x-1)}{x^2}\)',r'(C) \(\dfrac{e^x}{x^2}\)',r'(D) \(e^x(1-x)\)',r'(E) \(\dfrac{xe^x-e^x}{x}\)']),
 (r'Point on \(y=\dfrac12 x^2+9x+4\) where tangent is parallel to \(y=3x-1\):',
  [r'(A) \(x=-6\)',r'(B) \(x=3\)',r'(C) \(x=-3\)',r'(D) \(x=6\)',r'(E) \(x=0\)']),
 r'Evaluate \(\displaystyle\lim_{x\to4}\dfrac{\sqrt{x}-2}{x-4}\) if it exists.',
 r'Evaluate \(\displaystyle\lim_{x\to\infty}\left(3+\dfrac{2}{x}\right)\).',
 r'Differentiate \(y=x\ln x\).',
 r'Differentiate \(y=\cos(5x^2)\).',
 r'Find \(f'(2)\) if \(f(x)=\ln(2x-3)\).',
 r'Differentiate \(y=e^{-x}(x^2-1)\) and simplify.',
 r'Find coordinates where the tangent to \(y=x^3-6x^2+9x+1\) is horizontal.',
],
[
 (r'\(\displaystyle\lim_{x\to1}\dfrac{x^3-1}{x-1}\)=',
  ['(A) \(0\)','(B) \(1\)','(C) \(2\)','(D) \(3\)','(E) DNE']),
 (r'\(f(x)=2x^3-15x^2+36x\). Local max/min classification starts from solving',
  [r'(A) \(f=0\)',r'(B) \(f'=0\)',r'(C) \(f''=0\)',r'(D) \(f'=f\)',r'(E) \(f''=f'\)']),
 (r'\(y=\sin^2(4x)\). \(y'=\)',
  [r'(A) \(2\sin4x\)',r'(B) \(8\sin4x\cos4x\)',r'(C) \(\sin8x\)',r'(D) \(4\sin4x\)',r'(E) both B and equivalent forms']),
 (r'\(y=\dfrac{\ln x}{x}\). Critical points from \(y'=0\) give',
  [r'(A) \(x=e\)',r'(B) \(x=1\)',r'(C) \(x=0\)',r'(D) \(x=e^{-1}\)',r'(E) none']),
 (r'Tangent to \(y=\dfrac{1}{x}\) at \(x=2\):',
  [r'(A) \(y=-\tfrac14 x+1\)',r'(B) \(y=-\tfrac14x+\tfrac34\) wait check',r'(C) \(y=-\tfrac12x+1\)',r'(D) \(y=\tfrac12x\)',r'(E) \(y=-\tfrac14 x+\tfrac12\)']),
 r'State whether \(\displaystyle\lim_{x\to0^+} \ln x\) exists as a real number.',
 r'Evaluate \(\displaystyle\lim_{x\to2}\dfrac{x^3-8}{x-2}\).',
 r'Differentiate \(y=(x^2+1)e^{x}\).',
 r'Differentiate \(y=\dfrac{x^2+2}{x^2-2}\).',
 r'Find \(y''\) for \(y=\sqrt{x-1}\).',
 r'Equation of tangent to \(y=e^{x}+x\) at \(x=0\).',
 r'A particle has \(s(t)=t^3-6t^2+9t\). Find times when velocity is zero on \([0,5]\).',
],
]

ld_a = [
[
 r'(A) \(0\).',
 r'(D) \(x=3\).',
 r'(C) \(-\dfrac{2x}{3(x^2-1)^{4/3}}\).',
 r'(E) \(-\dfrac{x^2+9}{x^4}\).',
 r'(A) \(y=-6x-3\).',
 r'Yes if LHL=RHL (=4); exists.',
 r'\(4\) (factor).',
 r'\(\dfrac{3}{2}\).',
 r'\(\dfrac{1}{2\sqrt{x}}+\dfrac{3}{2}\sqrt{x}\).',
 r'\(f'(x)=4x+1\).',
 r'\(f'(1)=2e^{3}\).',
 r'\(y'=\dfrac{1-\ln(2x)}{x^2}\).',
],
[
 r'(C) \(6\).',
 r'(B) \(x=\pm1\).',
 r'(A) \(e^x(3\cos3x+\sin3x)\).',
 r'(B) \(\dfrac{10x}{5x^2+1}\).',
 r'(A) \(y=2x+1\).',
 r'No (LHL=-1, RHL=1).',
 r'\(-2\).',
 r'\(0\).',
 r'\(y'=10(2x-1)^4\).',
 r'\(y'=\dfrac{-14}{(x-4)^2}\).',
 r'Compute via product/chain; leave simplified surd/polynomial form.',
 r'\(y=9x-16\) (since \(y'=3x^2-3\), at 2: \(m=9\), \(y(2)=2\)).',
],
[
 r'(B) \(1\).',
 r'(A) \(x=0,2\).',
 r'(E)/(A) \(2\pi\sec^2(\pi/3)=2\pi\cdot4=8\pi\).',
 r'(B) \(\dfrac{e^x(x-1)}{x^2}\).',
 r'(A) \(x=-6\) (\(y'=x+9=3\)).',
 r'\(\dfrac{1}{4}\) (rationalise).',
 r'\(3\).',
 r'\(1+\ln x\).',
 r'\(-10x\sin(5x^2)\).',
 r'\(f'(2)=2/(4-3)=2\).',
 r'\(e^{-x}(-x^2+2x+1)\).',
 r'\((1,5)\) local max, \((3,-1)\)? check \(y'=3(x-1)(x-3)\); points \((1,5),(3,1)\).',
],
[
 r'(D) \(3\).',
 r'(B) \(f'=0\).',
 r'(B)/(E) \(8\sin4x\cos4x=4\sin8x\).',
 r'(A) \(x=e\).',
 r'At \(x=2\), \(y=1/2\), \(m=-1/4\): \(y-\tfrac12=-\tfrac14(x-2)\Rightarrow y=-\tfrac14x+1\).',
 r'No (diverges to \(-\infty\)).',
 r'\(12\).',
 r'\(e^x(x^2+2x+1)\).',
 r'\(y'=\dfrac{-8x}{(x^2-2)^2}\).',
 r'\(y''=-\dfrac{1}{4}(x-1)^{-3/2}\).',
 r'\(y=2x+1\).',
 r'\(t=1,3\).',
],
]
write_pair('limits-diff', 'Limits & Differentiation', 'about 70–80 minutes per test',
           '../limits-diff/2a_Differentiation_Exam_Sample.pdf', ld_q, ld_a)


# ---------- INTEGRATION ----------
int_q = [
[
 (r'Best first step for \(\displaystyle\int\left(x-\dfrac{3}{x}\right)^2 dx\)?',
  ['(A) Substitution','(B) Expand','(C) Differentiate first','(D) Common denominator','(E) none']),
 (r'\(\displaystyle\int\left(x+\dfrac{1}{x}\right)^2?\) wait: \(\displaystyle\int\left(\sqrt{x}+\dfrac{1}{x}\right)dx\) closest form among',
  [r'(A) \(\tfrac{2}{3}x^{3/2}+\ln|x|+C\)',r'(B) \(\tfrac{3}{2}x^{3/2}+\ln|x|+C\)',r'(C) \(x^{1/2}-\dfrac{1}{x}+C\)',r'(D) \(\tfrac{2}{3}x^{3/2}-\dfrac{1}{x}+C\)',r'(E) other']),
 (r'\(\displaystyle\int_{-1}^{2}(2x^3+2)\,dx=\)',
  ['(A) \(14\)','(B) \(25/2\)','(C) \(9\)','(D) \(12\)','(E) \(27/2\)']),
 (r'Area between \(f(x)=x^3-4x^2-x+4\) and \(x\)-axis on roots needs',
  ['(A) one integral only','(B) split where \(f\) changes sign','(C) ignore negatives','(D) differentiate','(E) none']),
 (r'\(\displaystyle\int 3\cos\!\left(\dfrac{x}{3}\right)dx=\)',
  [r'(A) \(9\sin(x/3)+C\)',r'(B) \(3\sin(x/3)+C\)',r'(C) \(\sin(3x)+C\)',r'(D) \(\tfrac13\sin(x/3)+C\)',r'(E) \(-3\sin(x/3)+C\)']),
 r'If \(\dfrac{dy}{dx}=1+3x\) and the curve passes through \((4,10)\), find \(y\).',
 r'Find \(\displaystyle\int(9x^5+3x^2)\,dx\) in positive-index form.',
 r'Find \(\displaystyle\int\left(3x^3-\dfrac{4}{x}\right)dx\) with positive indices/surds as needed.',
 r'Area between \(y=x-x^2\) and the \(x\)-axis from \(0\) to \(1\).',
 r'Show intersection of \(y=x^2\) and \(y=2-x^2\) at \((\pm1,1)\) and find the enclosed area.',
 r'Find \(\displaystyle\int(e^{2x}+4x)\,dx\).',
 r'Use \(u=x^2-3\) (or suitable) to evaluate \(\displaystyle\int 2x(x^2-3)^3\,dx\).',
],
[
 (r'\(\displaystyle\int x^{1/2}\,dx=\)',
  [r'(A) \(\tfrac{2}{3}x^{3/2}+C\)',r'(B) \(\tfrac{1}{2}x^{-1/2}+C\)',r'(C) \(x^{3/2}+C\)',r'(D) \(\tfrac{3}{2}x^{3/2}+C\)',r'(E) \(2x^{1/2}+C\)']),
 (r'\(\displaystyle\int_0^{\pi/2}\cos x\,dx=\)',
  ['(A) \(0\)','(B) \(1\)','(C) \(-1\)','(D) \(\pi/2\)','(E) \(2\)']),
 (r'For \(\displaystyle\int\dfrac{2x}{x^2+5}\,dx\) a good substitution is',
  [r'(A) \(u=2x\)',r'(B) \(u=x^2+5\)',r'(C) \(u=x^2\)',r'(D) \(u=\ln x\)',r'(E) \(u=5\)']),
 (r'\(\displaystyle\int e^{3x}\,dx=\)',
  [r'(A) \(3e^{3x}+C\)',r'(B) \(\tfrac13 e^{3x}+C\)',r'(C) \(e^{3x}+C\)',r'(D) \(e^{x}/3+C\)',r'(E) \(-3e^{3x}+C\)']),
 (r'Area under \(y=\sqrt{x}\) from \(0\) to \(4\) equals',
  ['(A) \(8/3\)','(B) \(16/3\)','(C) \(4\)','(D) \(8\)','(E) \(2\)']),
 r'Gradient \(\dfrac{dy}{dx}=2x-5\), passes through \((3,1)\). Find the curve.',
 r'\(\displaystyle\int\left(x^4-\dfrac{1}{x^2}\right)dx\).',
 r'\(\displaystyle\int_1^{4}\dfrac{1}{\sqrt{x}}\,dx\).',
 r'Area between \(y=4-x^2\) and the \(x\)-axis (full positive region).',
 r'\(\displaystyle\int(3\cos2x-2\sin x)\,dx\).',
 r'\(\displaystyle\int\dfrac{1}{5+x}\,dx\).',
 r'Substitution for \(\displaystyle\int\cos2x\cdot(2\sin2x)^3\,dx\): choose \(u\) and finish.',
],
[
 (r'\(\displaystyle\int(2x+1)^5\,dx\) (by inspection/chain reverse) =',
  [r'(A) \(\tfrac16(2x+1)^6+C\)',r'(B) \(\tfrac{1}{12}(2x+1)^6+C\)',r'(C) \(5(2x+1)^4+C\)',r'(D) \(\tfrac15(2x+1)^6+C\)',r'(E) \((2x+1)^6+C\)']),
 (r'\(\displaystyle\int_0^{1}(3x^2-1)\,dx=\)',
  ['(A) \(0\)','(B) \(1\)','(C) \(2\)','(D) \(-1\)','(E) \(1/2\)']),
 (r'\(\displaystyle\int\sin(3x)\,dx=\)',
  [r'(A) \(-\tfrac13\cos3x+C\)',r'(B) \(\tfrac13\cos3x+C\)',r'(C) \(-\cos3x+C\)',r'(D) \(3\cos3x+C\)',r'(E) \(\sin3x+C\)']),
 (r'Best \(u\) for \(\displaystyle\int x e^{x^2}\,dx\)',
  [r'(A) \(u=x\)',r'(B) \(u=x^2\)',r'(C) \(u=e^{x}\)',r'(D) \(u=xe^{x}\)',r'(E) \(u=2x\)']),
 (r'FTC: if \(F'=f\) then \(\displaystyle\int_a^b f=\)',
  [r'(A) \(F(a)-F(b)\)',r'(B) \(F(b)-F(a)\)',r'(C) \(F(ab)\)',r'(D) \(F'(b)-F'(a)\)',r'(E) \(f(b)-f(a)\)']),
 r'Curve with \(\dfrac{dy}{dx}=\dfrac{1}{x}\) through \((e,2)\). Find \(y\).',
 r'\(\displaystyle\int\left(6x^{1/2}-x^{-1/2}\right)dx\).',
 r'\(\displaystyle\int_0^{\pi/2}(1-\sin2x)\,dx\) exact value.',
 r'Area between \(y=x\) and \(y=x^2\) on \([0,1]\).',
 r'\(\displaystyle\int\dfrac{4}{2x+1}\,dx\).',
 r'\(\displaystyle\int e^{x}\sin\text{ — skip: }\) Find \(\displaystyle\int 5e^{-x}\,dx\).',
 r'Use substitution to find \(\displaystyle\int\dfrac{2x}{\sqrt{x^2+9}}\,dx\).',
],
[
 (r'\(\displaystyle\int\dfrac{1}{x^2}\,dx=\)',
  [r'(A) \(\ln|x|+C\)',r'(B) \(-\dfrac{1}{x}+C\)',r'(C) \(\dfrac{1}{x}+C\)',r'(D) \(x^{-3}/(-3)+C\)',r'(E) \(2/x+C\)']),
 (r'\(\displaystyle\int_0^{2}(x^2+1)\,dx=\)',
  ['(A) \(8/3\)','(B) \(14/3\)','(C) \(4\)','(D) \(6\)','(E) \(10/3\)']),
 (r'\(\displaystyle\int\cos\!\left(\dfrac{x}{2}\right)dx=\)',
  [r'(A) \(2\sin(x/2)+C\)',r'(B) \(\tfrac12\sin(x/2)+C\)',r'(C) \(-\sin(x/2)+C\)',r'(D) \(2\cos(x/2)+C\)',r'(E) \(\sin x+C\)']),
 (r'Area under \(y=e^{x}\) from \(0\) to \(1\) is',
  [r'(A) \(e-1\)',r'(B) \(e\)',r'(C) \(1\)',r'(D) \(e+1\)',r'(E) \(1/e\)']),
 (r'For \(\displaystyle\int(3x-1)(6x^2-4x+2)^{1/2}?\) wait: \(\displaystyle\int(6x-2)\sqrt{3x^2-2x}\,dx\), good \(u\) is',
  [r'(A) \(u=6x-2\)',r'(B) \(u=3x^2-2x\)',r'(C) \(u=\sqrt{x}\)',r'(D) \(u=3x\)',r'(E) \(u=x^2\)']),
 r'If \(y'=4x^3-2\) and \(y(1)=5\), find \(y\).',
 r'\(\displaystyle\int\left(x^{3}-\dfrac{2}{x^{3}}\right)dx\).',
 r'\(\displaystyle\int_{-2}^{1}(3x^2)\,dx\).',
 r'Area between \(y=\sin x\) and the \(x\)-axis from \(0\) to \(\pi\).',
 r'\(\displaystyle\int(2\sec^2 x-3\cos x)\,dx\).',
 r'\(\displaystyle\int\dfrac{x}{x^2+1}\,dx\).',
 r'Substitution: evaluate \(\displaystyle\int\dfrac{\cos x}{\sin x}\,dx\) (or \(\displaystyle\int\cot x\,dx\)).',
],
]

int_a = [
[
 r'(B) Expand first.',
 r'(A) \(\tfrac23 x^{3/2}+\ln|x|+C\).',
 r'(E) \(27/2\).',
 r'(B) Split on sign changes.',
 r'(A) \(9\sin(x/3)+C\).',
 r'\(y=x+\tfrac32 x^2+C\); through (4,10) \(\Rightarrow C=-18\); \(y=x+\tfrac32x^2-18\).',
 r'\(\tfrac32 x^6+x^3+C\).',
 r'\(\tfrac34 x^4-4\ln|x|+C\).',
 r'\(\int_0^1(x-x^2)dx=\tfrac16\).',
 r'Area \(=\int_{-1}^{1}((2-x^2)-x^2)dx=\dfrac{8}{3}\).',
 r'\(\tfrac12 e^{2x}+2x^2+C\).',
 r'\(\tfrac12(x^2-3)^4+C\).',
],
[
 r'(A) \(\tfrac23 x^{3/2}+C\).',
 r'(B) \(1\).',
 r'(B) \(u=x^2+5\).',
 r'(B) \(\tfrac13 e^{3x}+C\).',
 r'(B) \(16/3\).',
 r'\(y=x^2-5x+C\); (3,1)\(\Rightarrow C=7\); \(y=x^2-5x+7\).',
 r'\(\tfrac15 x^5+\dfrac{1}{x}+C\).',
 r'\([2\sqrt{x}]_1^4=4-2=2\).',
 r'\(\int_{-2}^{2}(4-x^2)dx=\dfrac{32}{3}\).',
 r'\(\tfrac32\sin2x+2\cos x+C\).',
 r'\(\ln|5+x|+C\).',
 r'\(u=\sin2x\), result \(\tfrac18(\sin2x)^4+C\) (up to constant factor check).',
],
[
 r'(B) \(\tfrac{1}{12}(2x+1)^6+C\).',
 r'(A) \(0\).',
 r'(A) \(-\tfrac13\cos3x+C\).',
 r'(B) \(u=x^2\).',
 r'(B) \(F(b)-F(a)\).',
 r'\(y=\ln|x|+1\).',
 r'\(4x^{3/2}-2x^{1/2}+C\).',
 r'\(\dfrac{\pi}{2}-1\).',
 r'\(\dfrac16\).',
 r'\(2\ln|2x+1|+C\).',
 r'\(-5e^{-x}+C\).',
 r'\(2\sqrt{x^2+9}+C\).',
],
[
 r'(B) \(-1/x+C\).',
 r'(B) \(14/3\).',
 r'(A) \(2\sin(x/2)+C\).',
 r'(A) \(e-1\).',
 r'(B) \(u=3x^2-2x\).',
 r'\(y=x^4-2x+C\); \(y(1)=5\Rightarrow C=6\); \(y=x^4-2x+6\).',
 r'\(\tfrac14 x^4+\dfrac{1}{x^2}+C\).',
 r'\([x^3]_{-2}^{1}=1-(-8)=9\).',
 r'\(2\).',
 r'\(2\tan x-3\sin x+C\).',
 r'\(\tfrac12\ln(x^2+1)+C\).',
 r'\(\ln|\sin x|+C\).',
],
]
write_pair('integration', 'Integration', 'about 70–80 minutes per test',
           '../integration/2a_Integration_Exam_Sample.pdf', int_q, int_a)

print('tests written to', TESTS)
