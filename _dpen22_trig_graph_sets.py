#!/usr/bin/env python3
"""Two dedicated trig graph-sketching sets (10 questions each) + hub update."""
from pathlib import Path
import html as H
from _dpen22_lesson_kit import set_page, page, CSS

OUT = Path(__file__).resolve().parent / 'siddharth' / 'dpen22' / 'class-notes' / 'trig' / 'lessons'

SETS = [
  {
    'slug': 'graph-set1',
    'short': 'Graph 1',
    'group': 'GRAPH SKETCHING',
    'source': 'Week 1D / 2A graphing skills',
    'title': 'Sketching sin and cos transformations (Set 1)',
    'blurb': r'Dedicated sketching practice: read amplitude, period, phase and midline, then list the five key points for one full cycle.',
    'lesson': [
      r'To sketch \(y=a\sin(b(x-c))+d\) or \(y=a\cos(b(x-c))+d\): first read amplitude \(|a|\), period \(\dfrac{2\pi}{|b|}\), phase shift \(c\) (right if \(c>0\)), and midline \(y=d\).',
      r'For sine with \(a>0\), one cycle’s five key \(y\)-levels (relative to the midline) are: mid → max → mid → min → mid. For cosine with \(a>0\): max → mid → min → mid → max.',
      r'Space the five \(x\)-values evenly using quarter-periods \(\dfrac{T}{4}\). Start at the phase-shifted “beginning” of the cycle, then add \(\dfrac{T}{4}\) four times.',
    ],
    'example': r'For \(y=2\sin\!\left(x-\dfrac{\pi}{2}\right)+1\): \(A=2\), \(T=2\pi\), phase right \(\dfrac{\pi}{2}\), midline \(y=1\). Key points: \(\left(\dfrac{\pi}{2},1\right),(\pi,3),\left(\dfrac{3\pi}{2},1\right),(2\pi,-1),\left(\dfrac{5\pi}{2},1\right)\).',
    'points': [
      r'Always measure max/min from the midline \(y=d\), not from \(y=0\).',
      r'Period \(T=\dfrac{2\pi}{|b|}\) for sin/cos; \(T=\dfrac{\pi}{|b|}\) for tan.',
      r'Phase: form \(b(x-c)\) shows shift \(c\) clearly.',
      r'Sketch one full cycle unless a different interval is asked.',
      r'Mark asymptotes for tangent graphs.',
    ],
    'formulas_title': 'Sketching checklist',
    'formulas': [
      r'Amplitude \(=|a|\); midline \(y=d\); range \([d-|a|,d+|a|]\).',
      r'Period of sin/cos: \(\dfrac{2\pi}{|b|}\).',
      r'Phase shift from \(a\sin(b(x-c))+d\): right by \(c\) if \(c>0\).',
      r'Quarter step: \(\dfrac{T}{4}\).',
    ],
    'problems': [
      r'Sketch one cycle of \(y=\sin x\) for \(0\le x\le 2\pi\). List the five key points.',
      r'Sketch one cycle of \(y=\cos x\) for \(0\le x\le 2\pi\). List the five key points.',
      r'Sketch \(y=2\sin x\) on \(0\le x\le 2\pi\). State amplitude and the five key points.',
      r'Sketch \(y=\sin(2x)\) on \(0\le x\le\pi\). State period and the five key points.',
      r'Sketch \(y=\cos x+2\) on \(0\le x\le 2\pi\). State midline, range and five key points.',
      r'Sketch \(y=-\sin x\) on \(0\le x\le 2\pi\). How does the pattern change?',
      r'Sketch \(y=3\cos(x)\) on \(0\le x\le 2\pi\). Give amplitude and five key points.',
      r'Sketch \(y=\sin\!\left(x-\dfrac{\pi}{2}\right)\) on \(\dfrac{\pi}{2}\le x\le\dfrac{5\pi}{2}\). Give the five key points.',
      r'Sketch \(y=2\cos(2x)\) on \(0\le x\le\pi\). State amplitude, period and five key points.',
      r'Sketch \(y=\tan x\) on \(-\dfrac{\pi}{2}<x<\dfrac{\pi}{2}\). Mark the asymptotes and the point at \(x=0\).',
    ],
    'answers': [
      r'\((0,0),\left(\dfrac{\pi}{2},1\right),(\pi,0),\left(\dfrac{3\pi}{2},-1\right),(2\pi,0)\).',
      r'\((0,1),\left(\dfrac{\pi}{2},0\right),(\pi,-1),\left(\dfrac{3\pi}{2},0\right),(2\pi,1)\).',
      r'Amplitude \(2\): \((0,0),\left(\dfrac{\pi}{2},2\right),(\pi,0),\left(\dfrac{3\pi}{2},-2\right),(2\pi,0)\).',
      r'Period \(\pi\): \((0,0),\left(\dfrac{\pi}{4},1\right),\left(\dfrac{\pi}{2},0\right),\left(\dfrac{3\pi}{4},-1\right),(\pi,0)\).',
      r'Midline \(y=2\), range \([1,3]\): \((0,3),\left(\dfrac{\pi}{2},2\right),(\pi,1),\left(\dfrac{3\pi}{2},2\right),(2\pi,3)\).',
      r'Reflection in \(x\)-axis: mid → min → mid → max → mid; points \((0,0),\left(\dfrac{\pi}{2},-1\right),(\pi,0),\left(\dfrac{3\pi}{2},1\right),(2\pi,0)\).',
      r'Amplitude \(3\): \((0,3),\left(\dfrac{\pi}{2},0\right),(\pi,-3),\left(\dfrac{3\pi}{2},0\right),(2\pi,3)\).',
      r'\(\left(\dfrac{\pi}{2},0\right),(\pi,1),\left(\dfrac{3\pi}{2},0\right),(2\pi,-1),\left(\dfrac{5\pi}{2},0\right)\).',
      r'Amp \(2\), period \(\pi\): \((0,2),\left(\dfrac{\pi}{4},0\right),\left(\dfrac{\pi}{2},-2\right),\left(\dfrac{3\pi}{4},0\right),(\pi,2)\).',
      r'Asymptotes \(x=\pm\dfrac{\pi}{2}\); passes through \((0,0)\); increasing through the origin.',
    ],
  },
  {
    'slug': 'graph-set2',
    'short': 'Graph 2',
    'group': 'GRAPH SKETCHING',
    'source': 'Week 1D / 2A graphing skills',
    'title': 'Full models and matching sketches (Set 2)',
    'blurb': r'Mixed transformations and “write the equation from features” questions — still with explicit key-point lists for sketching.',
    'lesson': [
      r'When several transformations appear together, peel them in a fixed order: amplitude and midline first, then period, then phase.',
      r'If the angle is written \(bx-c\) rather than \(b(x-c)\), the phase shift is \(\dfrac{c}{b}\) (right when positive).',
      r'For matching / writing equations: identify which parent (sin or cos), then read \(a,b,c,d\) from the sketch description.',
    ],
    'example': r'\(y=4\sin\!\left(2\left(x-\dfrac{\pi}{4}\right)\right)-1\): amp \(4\), period \(\pi\), right \(\dfrac{\pi}{4}\), midline \(y=-1\). First key point \(\left(\dfrac{\pi}{4},-1\right)\).',
    'points': [
      r'Factor \(b\) out of the angle before reading phase.',
      r'Negative \(a\) reverses the usual max/min order.',
      r'Tangent has no amplitude; mark asymptotes every period.',
      r'Check one easy substituted point to validate a sketch.',
    ],
    'formulas_title': 'Useful identities for sketching',
    'formulas': [
      r'\(\cos x=\sin\!\left(x+\dfrac{\pi}{2}\right)\).',
      r'\(-\sin x=\sin(x+\pi)\).',
      r'Period of \(a\tan(bx)\): \(\dfrac{\pi}{|b|}\); asymptotes where \(\cos(bx)=0\).',
      r'Range of sin/cos models: \([d-|a|,d+|a|]\).',
    ],
    'problems': [
      r'Sketch \(y=2\sin\!\left(x+\dfrac{\pi}{2}\right)\) for one cycle starting at the phase-shifted start. List five key points.',
      r'Sketch \(y=\cos\!\left(x-\pi\right)+1\) on \(\pi\le x\le 3\pi\). List five key points.',
      r'Sketch \(y=-2\cos x\) on \(0\le x\le 2\pi\). List five key points.',
      r'Sketch \(y=3\sin(2x)+1\) on \(0\le x\le\pi\). State amp, period, midline and five key points.',
      r'Sketch \(y=\sin\!\left(2\left(x-\dfrac{\pi}{6}\right)\right)\) for one cycle. Give start \(x\) and five key points.',
      r'Sketch \(y=2\tan x\) on \(-\dfrac{\pi}{2}<x<\dfrac{\pi}{2}\). State asymptotes and \((0,0)\).',
      r'A sine wave has amplitude \(5\), period \(\pi\), midline \(y=2\), and starts a rising midline-crossing at \(x=0\). Write a possible equation and list five key points on \(0\le x\le\pi\).',
      r'A cosine wave has amplitude \(1\), period \(2\pi\), no phase shift, and midline \(y=-3\). Write the equation and five key points on \(0\le x\le 2\pi\).',
      r'Sketch \(y=4\cos(3x)\) for one period starting at \(x=0\). State period and five key points.',
      r'Sketch \(y=-\sin(2x)+2\) on \(0\le x\le\pi\). List five key points.',
    ],
    'answers': [
      r'Start at \(x=-\dfrac{\pi}{2}\): \(\left(-\dfrac{\pi}{2},0\right),(0,2),\left(\dfrac{\pi}{2},0\right),(\pi,-2),\left(\dfrac{3\pi}{2},0\right)\) (or shift the window to \([0,2\pi]\) equivalently). Note \(\sin(x+\pi/2)=\cos x\), so same shape as \(2\cos x\).',
      r'\((\pi,2),\left(\dfrac{3\pi}{2},1\right),(2\pi,0),\left(\dfrac{5\pi}{2},1\right),(3\pi,2)\).',
      r'Max/min swapped vs \(2\cos x\): \((0,-2),\left(\dfrac{\pi}{2},0\right),(\pi,2),\left(\dfrac{3\pi}{2},0\right),(2\pi,-2)\).',
      r'Amp \(3\), period \(\pi\), midline \(1\): \((0,1),\left(\dfrac{\pi}{4},4\right),\left(\dfrac{\pi}{2},1\right),\left(\dfrac{3\pi}{4},-2\right),(\pi,1)\).',
      r'Start \(x=\dfrac{\pi}{6}\): \(\left(\dfrac{\pi}{6},0\right),\left(\dfrac{5\pi}{12},1\right),\left(\dfrac{2\pi}{3},0\right),\left(\dfrac{11\pi}{12},-1\right),\left(\dfrac{7\pi}{6},0\right)\).',
      r'Asymptotes \(x=\pm\dfrac{\pi}{2}\); steeper than \(\tan x\); through \((0,0)\).',
      r'e.g. \(y=5\sin(2x)+2\); points \((0,2),\left(\dfrac{\pi}{4},7\right),\left(\dfrac{\pi}{2},2\right),\left(\dfrac{3\pi}{4},-3\right),(\pi,2)\).',
      r'\(y=\cos x-3\); \((0,-2),\left(\dfrac{\pi}{2},-3\right),(\pi,-4),\left(\dfrac{3\pi}{2},-3\right),(2\pi,-2)\).',
      r'Period \(\dfrac{2\pi}{3}\): \((0,4),\left(\dfrac{\pi}{6},0\right),\left(\dfrac{\pi}{3},-4\right),\left(\dfrac{\pi}{2},0\right),\left(\dfrac{2\pi}{3},4\right)\).',
      r'\((0,2),\left(\dfrac{\pi}{4},1\right),\left(\dfrac{\pi}{2},2\right),\left(\dfrac{3\pi}{4},3\right),(\pi,2)\).',
    ],
  },
]


def patch_hub():
    hub = OUT / 'index.html'
    text = hub.read_text()
    card = '''<div class="summary" style="margin-bottom:16px;">
<h3 style="margin-top:0;">Graph sketching — 2 sets (10 questions each)</h3>
<p class="sub" style="margin:0 0 10px;">Dedicated sketching practice: amplitude, period, phase, midline and five key points per cycle. Answers on separate pages.</p>
<div class="chiprow"><a class="chip" href="graph-set1.html">Graph 1: Sketching sin and cos transformations (Set 1)</a><a class="chip on" href="graph-set1-answers.html">Graph 1 answers</a><a class="chip" href="graph-set2.html">Graph 2: Full models and matching sketches (Set 2)</a><a class="chip on" href="graph-set2-answers.html">Graph 2 answers</a></div>
</div>'''
    if 'graph-set1.html' in text:
        return
    # insert before closing of wrap content — after last summary card block, before end
    marker = '</div>\n</body></html>'
    # find last </div> of cards area: insert before final wrap close
    if '<!--GRAPHSETS-->' not in text:
        text = text.replace(
            '<p class="sub">Built from the filled-in student notes:',
            '<p class="sub">Built from the filled-in student notes:'
        )
        # insert card after nav block's following content — append before last two closing divs of wrap
        idx = text.rfind('</div>\n</body>')
        if idx == -1:
            idx = text.rfind('</div></body>')
        text = text[:idx] + card + '\n' + text[idx:]
        hub.write_text(text)
        print('hub patched')


def main():
    for s in SETS:
        set_page(OUT, 'Trigonometry', s, SETS)
        print('wrote', s['slug'])
    patch_hub()


if __name__ == '__main__':
    main()
