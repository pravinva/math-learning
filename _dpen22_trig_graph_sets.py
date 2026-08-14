#!/usr/bin/env python3
"""Two dedicated trig graph-sketching sets (10 questions each) + hub update."""
from pathlib import Path
import math
import html as H
from _dpen22_lesson_kit import set_page, page, CSS
from _figkit_trig import plot, PI

OUT = Path(__file__).resolve().parent / 'siddharth' / 'dpen22' / 'class-notes' / 'trig' / 'lessons'


def kp(*pairs):
    return list(pairs)


# One labelled sketch per answer: (function, xmin, xmax, ymin, ymax, kwargs)
FIGURES = {
  'graph-set1': [
    (math.sin, 0, 2*PI, -1.6, 1.6,
     dict(keypoints=kp((0, 0), (PI/2, 1), (PI, 0), (3*PI/2, -1), (2*PI, 0)),
          midline=0, amplitude=1, period=2*PI, caption='y = sin x')),
    (math.cos, 0, 2*PI, -1.6, 1.6,
     dict(keypoints=kp((0, 1), (PI/2, 0), (PI, -1), (3*PI/2, 0), (2*PI, 1)),
          midline=0, amplitude=1, period=2*PI, caption='y = cos x')),
    (lambda x: 2*math.sin(x), 0, 2*PI, -2.8, 2.8,
     dict(keypoints=kp((0, 0), (PI/2, 2), (PI, 0), (3*PI/2, -2), (2*PI, 0)),
          midline=0, amplitude=2, period=2*PI, caption='y = 2 sin x')),
    (lambda x: math.sin(2*x), 0, PI, -1.6, 1.6,
     dict(keypoints=kp((0, 0), (PI/4, 1), (PI/2, 0), (3*PI/4, -1), (PI, 0)),
          midline=0, amplitude=1, period=PI, caption='y = sin 2x')),
    (lambda x: math.cos(x)+2, 0, 2*PI, 0.4, 3.6,
     dict(keypoints=kp((0, 3), (PI/2, 2), (PI, 1), (3*PI/2, 2), (2*PI, 3)),
          midline=2, amplitude=1, period=2*PI, caption='y = cos x + 2  (range [1, 3])')),
    (lambda x: -math.sin(x), 0, 2*PI, -1.6, 1.6,
     dict(keypoints=kp((0, 0), (PI/2, -1), (PI, 0), (3*PI/2, 1), (2*PI, 0)),
          midline=0, amplitude=1, period=2*PI,
          caption='y = -sin x  (reflected: mid, min, mid, max, mid)')),
    (lambda x: 3*math.cos(x), 0, 2*PI, -4, 4,
     dict(keypoints=kp((0, 3), (PI/2, 0), (PI, -3), (3*PI/2, 0), (2*PI, 3)),
          midline=0, amplitude=3, period=2*PI, caption='y = 3 cos x')),
    (lambda x: math.sin(x - PI/2), PI/2, 5*PI/2, -1.6, 1.6,
     dict(keypoints=kp((PI/2, 0), (PI, 1), (3*PI/2, 0), (2*PI, -1), (5*PI/2, 0)),
          midline=0, amplitude=1, period=2*PI,
          caption='y = sin(x - π/2)  (shift right π/2)')),
    (lambda x: 2*math.cos(2*x), 0, PI, -2.8, 2.8,
     dict(keypoints=kp((0, 2), (PI/4, 0), (PI/2, -2), (3*PI/4, 0), (PI, 2)),
          midline=0, amplitude=2, period=PI, caption='y = 2 cos 2x')),
    (math.tan, -PI/2, PI/2, -4.2, 4.2,
     dict(keypoints=kp((-PI/4, -1), (0, 0), (PI/4, 1)),
          asymptotes=(-PI/2, PI/2), caption='y = tan x  (period π, no amplitude)',
          extra_notes=('Asymptotes at x = ±π/2; increasing through the origin.',))),
  ],
  'graph-set2': [
    (lambda x: 2*math.sin(x + PI/2), -PI/2, 3*PI/2, -2.8, 2.8,
     dict(keypoints=kp((-PI/2, 0), (0, 2), (PI/2, 0), (PI, -2), (3*PI/2, 0)),
          midline=0, amplitude=2, period=2*PI,
          caption='y = 2 sin(x + π/2) = 2 cos x')),
    (lambda x: math.cos(x - PI) + 1, PI, 3*PI, -0.6, 2.6,
     dict(keypoints=kp((PI, 2), (3*PI/2, 1), (2*PI, 0), (5*PI/2, 1), (3*PI, 2)),
          midline=1, amplitude=1, period=2*PI, caption='y = cos(x - π) + 1')),
    (lambda x: -2*math.cos(x), 0, 2*PI, -2.8, 2.8,
     dict(keypoints=kp((0, -2), (PI/2, 0), (PI, 2), (3*PI/2, 0), (2*PI, -2)),
          midline=0, amplitude=2, period=2*PI,
          caption='y = -2 cos x  (max and min swapped)')),
    (lambda x: 3*math.sin(2*x) + 1, 0, PI, -2.8, 4.8,
     dict(keypoints=kp((0, 1), (PI/4, 4), (PI/2, 1), (3*PI/4, -2), (PI, 1)),
          midline=1, amplitude=3, period=PI, caption='y = 3 sin 2x + 1')),
    (lambda x: math.sin(2*(x - PI/6)), PI/6, 7*PI/6, -1.6, 1.6,
     dict(keypoints=kp((PI/6, 0), (5*PI/12, 1), (2*PI/3, 0), (11*PI/12, -1), (7*PI/6, 0)),
          midline=0, amplitude=1, period=PI,
          caption='y = sin(2(x - π/6))  (start x = π/6)')),
    (lambda x: 2*math.tan(x), -PI/2, PI/2, -5, 5,
     dict(keypoints=kp((-PI/4, -2), (0, 0), (PI/4, 2)),
          asymptotes=(-PI/2, PI/2), caption='y = 2 tan x  (steeper than tan x)',
          extra_notes=('Asymptotes at x = ±π/2; passes through (0, 0).',))),
    (lambda x: 5*math.sin(2*x) + 2, 0, PI, -4, 8,
     dict(keypoints=kp((0, 2), (PI/4, 7), (PI/2, 2), (3*PI/4, -3), (PI, 2)),
          midline=2, amplitude=5, period=PI,
          caption='y = 5 sin 2x + 2  (amp 5, period π, midline y = 2)')),
    (lambda x: math.cos(x) - 3, 0, 2*PI, -4.6, -1.4,
     dict(keypoints=kp((0, -2), (PI/2, -3), (PI, -4), (3*PI/2, -3), (2*PI, -2)),
          midline=-3, amplitude=1, period=2*PI, caption='y = cos x - 3')),
    (lambda x: 4*math.cos(3*x), 0, 2*PI/3, -5.2, 5.2,
     dict(keypoints=kp((0, 4), (PI/6, 0), (PI/3, -4), (PI/2, 0), (2*PI/3, 4)),
          midline=0, amplitude=4, period=2*PI/3, caption='y = 4 cos 3x')),
    (lambda x: -math.sin(2*x) + 2, 0, PI, 0.4, 3.6,
     dict(keypoints=kp((0, 2), (PI/4, 1), (PI/2, 2), (3*PI/4, 3), (PI, 2)),
          midline=2, amplitude=1, period=PI,
          caption='y = -sin 2x + 2  (reflected, midline y = 2)')),
  ],
  'graph-tan': [
    (math.tan, -PI/2, PI/2, -4.2, 4.2,
     dict(keypoints=kp((-PI/4, -1), (0, 0), (PI/4, 1)),
          asymptotes=(-PI/2, PI/2), period=PI,
          caption='y = tan x  (period π, no amplitude)',
          extra_notes=('Asymptotes where cos x = 0: x = ±π/2.',))),
    (lambda x: 3*math.tan(x), -PI/2, PI/2, -5.5, 5.5,
     dict(keypoints=kp((-PI/4, -3), (0, 0), (PI/4, 3)),
          asymptotes=(-PI/2, PI/2), period=PI,
          caption='y = 3 tan x  (steeper; same asymptotes)',
          extra_notes=('Vertical stretch by 3; asymptotes still x = ±π/2.',))),
    (lambda x: math.tan(2*x), -PI/4, PI/4, -4.2, 4.2,
     dict(keypoints=kp((-PI/8, -1), (0, 0), (PI/8, 1)),
          asymptotes=(-PI/4, PI/4), period=PI/2,
          caption='y = tan 2x  (period π/2)',
          extra_notes=('Asymptotes: 2x = ±π/2 ⇒ x = ±π/4.',))),
    (lambda x: math.tan(x - PI/4), -PI/4, 3*PI/4, -4.2, 4.2,
     dict(keypoints=kp((0, -1), (PI/4, 0), (PI/2, 1)),
          asymptotes=(-PI/4, 3*PI/4), period=PI,
          caption='y = tan(x − π/4)  (shift right π/4)',
          extra_notes=('Asymptotes move with the phase: x = −π/4 and x = 3π/4.',))),
    (lambda x: -math.tan(x) + 1, -PI/2, PI/2, -4.2, 5.2,
     dict(keypoints=kp((-PI/4, 2), (0, 1), (PI/4, 0)),
          asymptotes=(-PI/2, PI/2), period=PI, midline=1,
          caption='y = −tan x + 1  (reflected; midline y = 1)',
          extra_notes=('Reflection in the x-axis, then up 1; asymptotes unchanged.',))),
  ],
}

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
  {
    'slug': 'graph-tan',
    'short': 'Tan graphs',
    'group': 'GRAPH SKETCHING · TAN',
    'source': 'Week 1D / 2A graphing skills',
    'title': 'Sketching tangent graphs (5 questions)',
    'blurb': r'Focused practice on \(y=a\tan(b(x-c))+d\): period, asymptotes, vertical stretch, phase and vertical shift — with labelled sketches in the answers.',
    'lesson': [
      r'Tangent has <strong>no amplitude</strong> and range \(\mathbb{R}\). The period of \(y=a\tan(bx)\) is \(\dfrac{\pi}{|b|}\).',
      r'Vertical asymptotes occur where \(\cos(bx)=0\), i.e. \(bx=\dfrac{\pi}{2}+k\pi\). Always mark them before drawing the curve.',
      r'A factor \(a\) stretches vertically (steeper if \(|a|>1\)). A phase \(c\) in \(b(x-c)\) shifts the whole pattern (including asymptotes) right by \(c\). Adding \(d\) lifts the curve so it crosses \(y=d\) where \(\tan=0\).',
    ],
    'example': r'For \(y=2\tan(2x)\): period \(\dfrac{\pi}{2}\); asymptotes \(x=\pm\dfrac{\pi}{4}\); through \((0,0)\); steeper than \(\tan 2x\). Key mid-points: \(\left(-\dfrac{\pi}{8},-2\right),\ (0,0),\ \left(\dfrac{\pi}{8},2\right)\).',
    'points': [
      r'Period of tan: \(\dfrac{\pi}{|b|}\) (half of sin/cos with the same \(b\)).',
      r'Mark asymptotes first — the curve never crosses them.',
      r'Negative \(a\) reflects (decreasing through the intercept instead of increasing).',
      r'Vertical shift \(+d\) moves the \(x\)-intercept up to the midline \(y=d\).',
    ],
    'formulas_title': 'Tangent sketching checklist',
    'formulas': [
      r'Period of \(a\tan(bx)\): \(\dfrac{\pi}{|b|}\).',
      r'Asymptotes: \(\cos(bx)=0\Rightarrow bx=\dfrac{\pi}{2}+k\pi\).',
      r'Key mid-points of one branch: where \(\tan=\pm1\), i.e. angle \(=\pm\dfrac{\pi}{4}\) (then apply \(a\) and \(d\)).',
      r'Phase form \(a\tan(b(x-c))+d\): shift right by \(c\).',
    ],
    'problems': [
      r'Sketch \(y=\tan x\) on \(-\dfrac{\pi}{2}<x<\dfrac{\pi}{2}\). Mark the asymptotes, the point at \(x=0\), and the points where \(y=\pm1\).',
      r'Sketch \(y=3\tan x\) on \(-\dfrac{\pi}{2}<x<\dfrac{\pi}{2}\). State the asymptotes and the three key points (where \(\tan=\pm1\) and the intercept).',
      r'Sketch \(y=\tan(2x)\) on \(-\dfrac{\pi}{4}<x<\dfrac{\pi}{4}\). State the period, asymptotes and three key points.',
      r'Sketch \(y=\tan\!\left(x-\dfrac{\pi}{4}\right)\) between its consecutive asymptotes. State the asymptotes and three key points.',
      r'Sketch \(y=-\tan x+1\) on \(-\dfrac{\pi}{2}<x<\dfrac{\pi}{2}\). State the asymptotes, midline and three key points.',
    ],
    'answers': [
      r'Asymptotes \(x=\pm\dfrac{\pi}{2}\); period \(\pi\); points \(\left(-\dfrac{\pi}{4},-1\right),\ (0,0),\ \left(\dfrac{\pi}{4},1\right)\); increasing.',
      r'Asymptotes still \(x=\pm\dfrac{\pi}{2}\); period \(\pi\); points \(\left(-\dfrac{\pi}{4},-3\right),\ (0,0),\ \left(\dfrac{\pi}{4},3\right)\) — steeper vertical stretch.',
      r'Period \(\dfrac{\pi}{2}\); asymptotes \(x=\pm\dfrac{\pi}{4}\); points \(\left(-\dfrac{\pi}{8},-1\right),\ (0,0),\ \left(\dfrac{\pi}{8},1\right)\).',
      r'Asymptotes \(x=-\dfrac{\pi}{4}\) and \(x=\dfrac{3\pi}{4}\); period \(\pi\); points \((0,-1),\ \left(\dfrac{\pi}{4},0\right),\ \left(\dfrac{\pi}{2},1\right)\).',
      r'Asymptotes \(x=\pm\dfrac{\pi}{2}\); midline \(y=1\); decreasing through \((0,1)\); points \(\left(-\dfrac{\pi}{4},2\right),\ (0,1),\ \left(\dfrac{\pi}{4},0\right)\).',
    ],
  },
]


def patch_hub():
    hub = OUT / 'index.html'
    text = hub.read_text()
    card = '''<div class="summary" style="margin-bottom:16px;" id="graph-sketching">
<h3 style="margin-top:0;">Graph sketching — sin/cos (2×10) + tan (1×5)</h3>
<p class="sub" style="margin:0 0 10px;">Dedicated sketching practice with labelled answer diagrams: amplitude, period, phase, midline, asymptotes and key points.</p>
<div class="chiprow">
<a class="chip" href="graph-set1.html">Graph 1: sin &amp; cos (10)</a>
<a class="chip on" href="graph-set1-answers.html">Graph 1 answers</a>
<a class="chip" href="graph-set2.html">Graph 2: full models (10)</a>
<a class="chip on" href="graph-set2-answers.html">Graph 2 answers</a>
<a class="chip" href="graph-tan.html">Tan graphs (5)</a>
<a class="chip on" href="graph-tan-answers.html">Tan answers</a>
</div>
</div>'''
    if 'id="graph-sketching"' in text or 'graph-tan.html' in text:
        # replace existing graph card if present
        import re
        text2, n = re.subn(
            r'<div class="summary"[^>]*>\s*<h3[^>]*>Graph sketching.*?</div>\s*</div>',
            card,
            text,
            count=1,
            flags=re.S,
        )
        if n:
            hub.write_text(text2)
            print('hub graph card updated')
            return
    idx = text.rfind('</div>\n</body>')
    if idx == -1:
        idx = text.rfind('</div></body>')
    hub.write_text(text[:idx] + card + '\n' + text[idx:])
    print('hub patched')


def attach_figures():
    """Append a labelled sketch to every answer."""
    for s in SETS:
        figs = FIGURES[s['slug']]
        assert len(figs) == len(s['answers']), \
            f"{s['slug']}: {len(figs)} figures vs {len(s['answers'])} answers"
        s['answers'] = [
            ans + plot(fn, xmin, xmax, ymin, ymax, **kw)
            for ans, (fn, xmin, xmax, ymin, ymax, kw) in zip(s['answers'], figs)
        ]


def main():
    attach_figures()
    # Keep sin/cos sets as siblings; tan set stands alone for chip nav
    sin_cos = [s for s in SETS if s['slug'] != 'graph-tan']
    tan = [s for s in SETS if s['slug'] == 'graph-tan']
    for s in sin_cos:
        set_page(OUT, 'Trigonometry', s, sin_cos)
        print('wrote', s['slug'])
    for s in tan:
        set_page(OUT, 'Trigonometry', s, tan)
        print('wrote', s['slug'])
    patch_hub()


if __name__ == '__main__':
    main()
