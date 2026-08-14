#!/usr/bin/env python3
"""Generate DPEN022 Trig short-lesson practice sets from Weeks 1A–2A notes."""
from pathlib import Path
import html as H

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
.problems ol{margin-left:22px;}
.problems li{margin:10px 0;}
.ans{background:#f0fdf4;border-left:4px solid var(--green);padding:8px 12px;margin:8px 0;border-radius:0 6px 6px 0;}
details{margin-top:10px;}
summary{cursor:pointer;font-weight:600;color:var(--navy);}
.tag{display:inline-block;background:var(--orange);color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;margin-bottom:8px;}
.chiprow{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 18px;}
.chip{display:inline-block;padding:7px 11px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:600;border:1px solid #c9dff7;background:#eef6ff;color:var(--blue);}
.chip.on{background:var(--navy);border-color:var(--navy);color:#fff;}
'''

def page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}]}});"></script>
<style>{CSS}</style>
</head><body><div class="wrap">
{body}
</div></body></html>
'''.replace("\\'", "'")


def set_page(meta, siblings):
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
    ans = ''.join(f'<div class="ans"><strong>Q{i}.</strong> {a}</div>' for i,a in enumerate(meta['answers'],1))
    body = f'''
<div class="eyebrow">DPEN022 Trigonometry · {meta["source"]}</div>
<span class="tag">{meta["group"]}</span>
<h1>{meta["title"]}</h1>
<p class="sub">{meta["blurb"]}</p>
<div class="nav">
  <a href="index.html">← Lesson sets hub</a>
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

<h2>5. Answers</h2>
<details>
<summary>Show answers</summary>
<div class="answers">{ans}</div>
</details>
'''
    (OUT / f'{meta["slug"]}.html').write_text(page(meta['title'], body))


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
    'slug': 'w1ab-set1', 'short': '1A+1B Set 1', 'group': 'WEEKS 1A + 1B · SET 1 OF 3',
    'source': 'Student Notes Week 1A (filled-in)',
    'title': 'Right triangles & trigonometric ratios',
    'blurb': 'From Week 1A: naming sides, SOH-CAH-TOA, reciprocal ratios, and complementary angles.',
    'lesson': [
      'Trigonometry studies the relationship between sides and angles in triangles. In a right-angled triangle the <strong>hypotenuse</strong> is opposite the \(90^\circ\) angle and is the longest side. Relative to a chosen acute angle \(\theta\), the other sides are the <strong>opposite</strong> and <strong>adjacent</strong>.',
      'In similar right triangles the side ratios are constant for a fixed \(\theta\). Those constant ratios are \(\sin\theta\), \(\cos\theta\) and \(\tan\theta\). Their reciprocals are \(\csc\theta\), \(\sec\theta\) and \(\cot\theta\).',
      'Complementary angles add to \(90^\circ\). This gives the co-function identities \(\sin\theta=\cos(90^\circ-\theta)\) and \(\cos\theta=\sin(90^\circ-\theta)\).',
    ],
    'example': 'In a \(3\)-\(4\)-\(5\) triangle, if the opposite to \(\theta\) is \(3\) and the hypotenuse is \(5\), then \(\sin\theta=\dfrac35\), \(\cos\theta=\dfrac45\), \(\tan\theta=\dfrac34\), \(\csc\theta=\dfrac53\), \(\sec\theta=\dfrac54\), \(\cot\theta=\dfrac43\).',
    'points': [
      'Hypotenuse is always opposite the right angle.',
      'Opposite/adjacent depend on which acute angle you choose.',
      'Remember <strong>SOH-CAH-TOA</strong>.',
      '\(\\sin\\theta\) and \(\\cos\\theta\) are never greater than \(1\) in a right triangle.',
      'Reciprocals: \(\\csc=1/\\sin\), \(\\sec=1/\\cos\), \(\\cot=1/\\tan\).',
      'Complementary: \(\\sin\\theta=\\cos(90^\\circ-\\theta)\).',
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
    'slug': 'w1ab-set2', 'short': '1A+1B Set 2', 'group': 'WEEKS 1A + 1B · SET 2 OF 3',
    'source': 'Student Notes Week 1A (filled-in)',
    'title': 'Exact ratios & right-triangle applications',
    'blurb': 'From Week 1A: exact values for \(30^\circ,45^\circ,60^\circ\), calculator use, and standard right-triangle problems (including elevation).',
    'lesson': [
      'Exact trig values come from two special triangles: the isosceles right triangle (\(45^\circ\)-\(45^\circ\)-\(90^\circ\)) with sides \(1:1:\sqrt2\), and the half-equilateral triangle (\(30^\circ\)-\(60^\circ\)-\(90^\circ\)) with sides \(1:\sqrt3:2\).',
      'These give exact \(\sin,\cos,\tan\) of \(30^\circ,45^\circ,60^\circ\) without a calculator. For other acute angles, use a calculator in <strong>degree</strong> mode and round as required.',
      'Right-triangle applications: choose the ratio that links the known side/angle to the unknown. Elevation/depression problems are just right triangles standing upright.',
    ],
    'example': r'\(\sin 30^\circ=\dfrac12\), \(\cos 30^\circ=\dfrac{\sqrt3}{2}\), \(\tan 30^\circ=\dfrac{1}{\sqrt3}\); \(\sin 45^\circ=\cos 45^\circ=\dfrac{\sqrt2}{2}\), \(\tan 45^\circ=1\); \(\sin 60^\circ=\dfrac{\sqrt3}{2}\), \(\cos 60^\circ=\dfrac12\), \(\tan 60^\circ=\sqrt3\).',
    'points': [
      r'\(45^\circ\)-\(45^\circ\)-\(90^\circ\) sides: \(1:1:\sqrt2\).',
      r'\(30^\circ\)-\(60^\circ\)-\(90^\circ\) sides: \(1:\sqrt3:2\) (short leg opposite \(30^\circ\)).',
      'Memorise exact sin/cos/tan of \(30^\circ,45^\circ,60^\circ\).',
      'Check calculator is in degrees for degree problems.',
      'Elevation: angle up from horizontal; depression: angle down from horizontal.',
    ],
    'formulas': [
      r'\(\sin30^\circ=\dfrac12,\ \cos30^\circ=\dfrac{\sqrt3}{2},\ \tan30^\circ=\dfrac{1}{\sqrt3}\)',
      r'\(\sin45^\circ=\dfrac{\sqrt2}{2},\ \cos45^\circ=\dfrac{\sqrt2}{2},\ \tan45^\circ=1\)',
      r'\(\sin60^\circ=\dfrac{\sqrt3}{2},\ \cos60^\circ=\dfrac12,\ \tan60^\circ=\sqrt3\)',
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
    'slug': 'w1ab-set3', 'short': '1A+1B Set 3', 'group': 'WEEKS 1A + 1B · SET 3 OF 3',
    'source': 'Student Notes Week 1B (filled-in)',
    'title': 'Angles of any magnitude (degrees)',
    'blurb': 'From Week 1B: unit circle, CAST signs, reference angles, exact values beyond \(90^\circ\), and solving trig equations in degrees.',
    'lesson': [
      'On the unit circle, a point \(P\) at angle \(\theta\) (from the positive \(x\)-axis, anticlockwise positive) has coordinates \((\cos\theta,\sin\theta)\). This extends trig ratios to any magnitude, including negatives.',
      'Signs by quadrant (CAST / ASTC): All positive in Q1; Sin positive in Q2; Tan positive in Q3; Cos positive in Q4.',
      'A <strong>reference angle</strong> is the acute angle between the terminal ray and the \(x\)-axis. Exact values for non-acute angles = (sign from quadrant) × (exact acute value).',
      'To solve equations like \(\sin\theta=k\) on \(0^\circ\le\theta\le360^\circ\): find the reference angle, then list all solutions in the correct quadrants.',
    ],
    'example': r'\(\sin 150^\circ=\sin 30^\circ=\dfrac12\) (Q2, sin +). \(\cos 210^\circ=-\cos 30^\circ=-\dfrac{\sqrt3}{2}\) (Q3, cos −).',
    'points': [
      r'\(P(\cos\theta,\sin\theta)\) on the unit circle.',
      'Positive angles anticlockwise; negative clockwise.',
      'Remember CAST for signs.',
      'Reference angle is always acute.',
      'Axis angles: \(0^\circ,90^\circ,180^\circ,270^\circ,360^\circ\) have simple coordinates.',
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
]}

GROUPS['1c'] = {
  'label': 'Week 1C',
  'sets': [
  {
    'slug': 'w1c-set1', 'short': '1C Set 1', 'group': 'WEEK 1C · SET 1 OF 3',
    'source': 'Student Notes Week 1C (filled-in)',
    'title': 'Radian measure & conversion',
    'blurb': 'From Week 1C: what a radian is, and converting between degrees and radians (exact and approximate).',
    'lesson': [
      'One radian is the central angle subtended by an arc of length equal to the radius. On a unit circle, a full turn is circumference \(2\pi\), so \(2\pi\) radians \(=360^\circ\) and \(\pi\) radians \(=180^\circ\).',
      'When no unit is written, angles are assumed to be in radians in higher mathematics. Degree problems must be marked with \(^\circ\).',
      'Convert degrees → radians by multiplying by \(\dfrac{\pi}{180}\). Convert radians → degrees by multiplying by \(\dfrac{180}{\pi}\).',
    ],
    'example': r'\(90^\circ=\dfrac{\pi}{2}\) rad. \(\dfrac{\pi}{4}\) rad \(=45^\circ\). \(156^\circ\approx 2.72\) rad (2 d.p.).',
    'points': [
      r'\(\pi\) rad \(=180^\circ\) is the master conversion.',
      'Full turn: \(2\pi\) rad \(=360^\circ\).',
      'Anticlockwise positive; clockwise negative (same as degrees).',
      'Leave exact answers in terms of \(\pi\) unless asked for decimals.',
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
      r'\(2\) rad \(\approx 114.6^\circ>100^\circ\).',
      r'\(\dfrac{\pi}{3}\) rad \(=60^\circ\).',
      r'\(\dfrac{3\pi}{2}\); point \((0,-1)\).',
    ],
  },
  {
    'slug': 'w1c-set2', 'short': '1C Set 2', 'group': 'WEEK 1C · SET 2 OF 3',
    'source': 'Student Notes Week 1C (filled-in)',
    'title': 'Exact ratios & quadrants in radians',
    'blurb': 'From Week 1C: exact trig values using radian arguments, and identifying quadrants for angles in terms of \(\pi\).',
    'lesson': [
      'The same special-triangle values apply with radian arguments: replace \(30^\circ,45^\circ,60^\circ\) by \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\).',
      'Quadrants for \(0<\theta<2\pi\): Q1 \(0<\theta<\dfrac{\pi}{2}\); Q2 \(\dfrac{\pi}{2}<\theta<\pi\); Q3 \(\pi<\theta<\dfrac{3\pi}{2}\); Q4 \(\dfrac{3\pi}{2}<\theta<2\pi\).',
      'Angles differing by \(2\pi k\) land on the same unit-circle point. Reduce first, then find the quadrant and reference angle.',
    ],
    'example': r'\(\sin\dfrac{5\pi}{6}=\sin\dfrac{\pi}{6}=\dfrac12\) (Q2). \(\cos\dfrac{4\pi}{3}=-\dfrac12\) (Q3).',
    'points': [
      r'Memorise \(\sin,\cos,\tan\) of \(\dfrac{\pi}{6},\dfrac{\pi}{4},\dfrac{\pi}{3}\) and axis angles.',
      'Reduce by \(\pm 2\pi\) to get into \([0,2\pi)\).',
      'Reference angle in radians is still the acute angle to the \(x\)-axis.',
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
    'slug': 'w1c-set3', 'short': '1C Set 3', 'group': 'WEEK 1C · SET 3 OF 3',
    'source': 'Student Notes Week 1C (filled-in)',
    'title': 'Solving trig equations in radians',
    'blurb': 'From Week 1C: solve sine/cosine/tangent equations on a given radian interval with exact answers.',
    'lesson': [
      'Working in radians is the same process as degrees: find a reference angle, place solutions in the correct quadrants, and list every solution inside the required interval (often \(0\le\theta\le 2\pi\)).',
      'Write answers as exact multiples of \(\pi\) whenever possible. Check calculator mode only for decimal approximations.',
      'For equations like \(2\sin\theta=-1\), first isolate the trig function: \(\sin\theta=-\dfrac12\), then solve.',
    ],
    'example': r'Solve \(\sin\theta=\dfrac12\) for \(0\le\theta\le 2\pi\): \(\theta=\dfrac{\pi}{6},\dfrac{5\pi}{6}\).',
    'points': [
      'Isolate the trig ratio first.',
      'Reference angle from the acute inverse (exact where possible).',
      'Use CAST to choose quadrants.',
      'Include all solutions in the interval.',
      'Answers usually in terms of \(\pi\).',
    ],
    'formulas': [
      r'If \(\sin\theta=k\): solutions in Q1/Q2 (or Q3/Q4 if \(k<0\)).',
      r'If \(\cos\theta=k\): solutions in Q1/Q4 (or Q2/Q3 if \(k<0\)).',
      r'If \(\tan\theta=k\): solutions in Q1/Q3 (or Q2/Q4 if \(k<0\)), period \(\pi\).',
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
]}

GROUPS['1d'] = {
  'label': 'Week 1D',
  'sets': [
  {
    'slug': 'w1d-set1', 'short': '1D Set 1', 'group': 'WEEK 1D · SET 1 OF 3',
    'source': 'Student Notes Week 1D (filled-in)',
    'title': 'Graphs of sin, cos and tan',
    'blurb': 'From Week 1D: basic graphs in radians, period, amplitude, and key features of \(y=\sin x\), \(y=\cos x\), \(y=\tan x\).',
    'lesson': [
      'Plotting unit-circle \(y\)-coordinates as \(x\) varies produces \(y=\sin x\). Plotting \(x\)-coordinates produces \(y=\cos x\). Both are continuous, amplitude \(1\), period \(2\pi\).',
      'The cosine graph is a horizontal shift of the sine graph (by \(\dfrac{\pi}{2}\)).',
      '\(y=\tan x\) has period \(\pi\), vertical asymptotes at \(x=\dfrac{\pi}{2}+k\pi\), and no amplitude (range all real \(y\)).',
    ],
    'example': r'For \(y=\sin x\): at \(x=0,\dfrac{\pi}{2},\pi,\dfrac{3\pi}{2},2\pi\) the values are \(0,1,0,-1,0\).',
    'points': [
      r'\(\sin\) and \(\cos\): period \(2\pi\), amplitude \(1\), range \([-1,1]\).',
      r'\(\tan\): period \(\pi\), range \(\mathbb{R}\), asymptotes odd multiples of \(\dfrac{\pi}{2}\).',
      r'\(\sin(x+2k\pi)=\sin x\); \(\tan(x+k\pi)=\tan x\).',
      'Cosine is sine shifted left by \(\dfrac{\pi}{2}\): \(\cos x=\sin\!\left(x+\dfrac{\pi}{2}\right)\).',
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
    'slug': 'w1d-set2', 'short': '1D Set 2', 'group': 'WEEK 1D · SET 2 OF 3',
    'source': 'Student Notes Week 1D (filled-in)',
    'title': 'Amplitude, period & the general sine/cosine model',
    'blurb': 'From Week 1D: transformations \(y=a\sin(bx)+d\) and \(y=a\cos(bx)+d\) — reading amplitude, period and midline.',
    'lesson': [
      'For \(y=a\sin(bx)\) or \(y=a\cos(bx)\): amplitude is \(|a|\); period is \(\dfrac{2\pi}{|b|}\). The graph is stretched vertically by \(|a|\) and horizontally by \(\dfrac{1}{|b|}\).',
      'A vertical shift \(+d\) moves the midline to \(y=d\). Range becomes \([d-|a|, d+|a|]\).',
      'Always state amplitude, period, midline/range when describing a transformed wave.',
    ],
    'example': r'\(y=3\sin(2x)\): amp \(3\), period \(\pi\). \(y=2\cos\!\left(\dfrac{x}{2}\right)-1\): amp \(2\), period \(4\pi\), midline \(y=-1\), range \([-3,1]\).',
    'points': [
      r'Amplitude \(=|a|\).',
      r'Period \(=\dfrac{2\pi}{|b|}\) for sine/cosine.',
      r'Midline \(y=d\); range \([d-|a|,d+|a|]\).',
      'Larger \(|b|\) → shorter period (more cycles).',
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
    'slug': 'w1d-set3', 'short': '1D Set 3', 'group': 'WEEK 1D · SET 3 OF 3',
    'source': 'Student Notes Week 1D (filled-in)',
    'title': 'Phase shift & full transformations',
    'blurb': 'From Week 1D: horizontal shifts / phase, and reading/writing full models \(y=a\sin(b(x-c))+d\).',
    'lesson': [
      'A phase shift appears when the angle is \(b(x-c)\) or \(bx-c\). In the form \(a\sin(b(x-c))+d\), the graph shifts right by \(c\) if \(c>0\).',
      'If written as \(a\sin(bx-c)+d\), the phase shift is \(\dfrac{c}{b}\) (to the right if \(\dfrac{c}{b}>0\)).',
      'When sketching: mark midline, amplitude envelope, period length, then place one key point using the phase shift.',
    ],
    'example': r'\(y=2\sin\!\left(3x-\dfrac{\pi}{2}\right)+1\): amp \(2\), period \(\dfrac{2\pi}{3}\), phase shift \(\dfrac{\pi}{6}\) right, midline \(y=1\).',
    'points': [
      'Factor \(b\) out of the angle to read phase cleanly.',
      'Right shift for \((x-c)\); left for \((x+c)\).',
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
]}

GROUPS['2a'] = {
  'label': 'Week 2A',
  'sets': [
  {
    'slug': 'w2a-set1', 'short': '2A Set 1', 'group': 'WEEK 2A · SET 1 OF 3',
    'source': 'Student Notes Week 2A (filled-in)',
    'title': 'Pythagorean trigonometric identities',
    'blurb': 'From Week 2A: deriving and using \(\sin^2\theta+\cos^2\theta=1\) and the companion identities.',
    'lesson': [
      'On the unit circle, \(x=\cos\theta\), \(y=\sin\theta\) and \(x^2+y^2=1\). Substituting gives the fundamental identity \(\sin^2\theta+\cos^2\theta=1\).',
      'Divide by \(\cos^2\theta\) (where defined) to get \(1+\tan^2\theta=\sec^2\theta\). Divide by \(\sin^2\theta\) to get \(1+\cot^2\theta=\csc^2\theta\).',
      'These identities are true for all \(\theta\) where the functions exist. Use them to rewrite expressions and find exact ratios.',
    ],
    'example': r'If \(\sin\theta=\dfrac{2}{\sqrt{29}}\) and \(\theta\) obtuse, then \(\cos\theta=-\sqrt{1-\sin^2\theta}=-\dfrac{5}{\sqrt{29}}\) (negative in Q2).',
    'points': [
      r'Primary: \(\sin^2+\cos^2=1\).',
      r'Then: \(1+\tan^2=\sec^2\) and \(1+\cot^2=\csc^2\).',
      'Choose the sign of the square root using the quadrant.',
      'Identities hold for all valid \(\theta\), not just acute angles.',
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
      r'If \(\sec\theta=-\dfrac{17}{8}\) and \(\dfrac{\pi}{2}<\theta<\pi\), find \(\tan\theta\).',
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
    'slug': 'w2a-set2', 'short': '2A Set 2', 'group': 'WEEK 2A · SET 2 OF 3',
    'source': 'Student Notes Week 2A (filled-in)',
    'title': 'Simplifying & proving identities',
    'blurb': 'From Week 2A: rewrite trig expressions and prove identities by moving from one side to the other.',
    'lesson': [
      'To simplify: expand products, factor, rewrite everything in \(\sin\) and \(\cos\), then apply Pythagorean identities.',
      'To prove an identity: start from the more complicated side and transform it into the other side. Do not move terms across the equals sign as if solving an equation.',
      'Common moves: \(1-\sin^2=\cos^2\), factor \(\sin^2\) or \(\cos^2\), and rewrite tan/sec in sin/cos.',
    ],
    'example': r'Simplify \(\sin^4\theta+\sin^2\theta\cos^2\theta=\sin^2\theta(\sin^2\theta+\cos^2\theta)=\sin^2\theta\).',
    'points': [
      'Complicated side → simpler side.',
      'Prefer \(\sin/\cos\) form for algebra.',
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
    'slug': 'w2a-set3', 'short': '2A Set 3', 'group': 'WEEK 2A · SET 3 OF 3',
    'source': 'Student Notes Week 2A (filled-in)',
    'title': 'Equations that need identities',
    'blurb': 'From Week 2A: solve trig equations by rewriting with Pythagorean identities, then solving on a stated interval.',
    'lesson': [
      'Some equations are not solvable until rewritten. Classic pattern: replace \(\cos^2\theta\) by \(1-\sin^2\theta\) (or vice versa) to get a quadratic in one trig function.',
      'After rewriting, solve the quadratic for \(\sin\theta\) or \(\cos\theta\), discard impossible roots (\(|k|>1\)), then find angles in the interval.',
      'Always check solutions in the original equation if you squared or used reciprocal steps.',
    ],
    'example': r'Solve \(2\sin^2\theta-\sin\theta-1=0\) on \(0^\circ\le\theta\le360^\circ\): \((2\sin\theta+1)(\sin\theta-1)=0\) → \(\sin\theta=-\dfrac12\) or \(1\) → \(\theta=90^\circ,210^\circ,330^\circ\).',
    'points': [
      'Rewrite to one trig function when possible.',
      'Quadratic in \(\sin\) or \(\cos\) is common.',
      'Reject roots with absolute value \(>1\).',
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
]}


def write_hub():
    cards = []
    for key, g in GROUPS.items():
        links = ''.join(
            f'<a class="chip" href="{s["slug"]}.html">{s["short"]}: {H.escape(s["title"])}</a>'
            for s in g['sets']
        )
        cards.append(f'''<div class="summary" style="margin-bottom:16px;">
<h3 style="margin-top:0;">{H.escape(g["label"])} — 3 sets</h3>
<p class="sub" style="margin:0 0 10px;">Each set: short lesson · key points · formulas/identities · 15 problems + answers</p>
<div class="chiprow">{links}</div>
</div>''')
    body = f'''
<div class="eyebrow">DPEN022 Trigonometry</div>
<span class="tag">LESSON SETS</span>
<h1>Trig lesson packs from Weeks 1A–2A</h1>
<p class="sub">Built from the filled-in student notes: Weeks <strong>1A + 1B</strong> (3 sets), then <strong>1C</strong>, <strong>1D</strong> and <strong>2A</strong> (3 sets each).</p>
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
