#!/usr/bin/env python3
"""Replace auto-generated PHYS143 exam extension sections with quality questions."""

import re
from pathlib import Path

from _phys143_exam_extension_data import EXTENSION

DIR = Path(__file__).parent / 'siddharth' / 'dpen143'
WEEK_FILES = {
    1: DIR / 'PHYS143_Week1_Electrostatics.html',
    2: DIR / 'PHYS143_Week2_Capacitance_Current_Resistance.html',
    3: DIR / 'PHYS143_Week3_Kirchhoff_Magnetism.html',
    4: DIR / 'PHYS143_Week4_Faraday_EMWaves.html',
    5: DIR / 'PHYS143_Week5_Module1_Review_ExamPrep.html',
    6: DIR / 'PHYS143_Week6_SpecialRelativity.html',
    7: DIR / 'PHYS143_Week7_Photoelectric_Xray_Hydrogen_Laser.html',
    8: DIR / 'PHYS143_Week8_MatterWaves_Uncertainty_Nuclear.html',
    9: DIR / 'PHYS143_Week9_Module2_Review_ExamPrep.html',
    10: DIR / 'PHYS143_Week10_WaveMotion_Beats_Doppler.html',
    11: DIR / 'PHYS143_Week11_Snell_TIR_Dispersion_Polarization.html',
    12: DIR / 'PHYS143_Week12_Mirrors_Lenses_OpticalInstruments.html',
    13: DIR / 'PHYS143_Week13_Interference_Diffraction.html',
}

BLOCK = re.compile(
    r'<!-- AUTO-ADDED PHYS143 EXAM EXTENSION -->\s*'
    r'<section class="topic" id="sec-extension-exam">.*?</section>',
    re.DOTALL,
)
PRACTICE_NUM = re.compile(r'<span class="p-num">Practice (\d+)</span>')


def next_practice_num(html: str) -> int:
    nums = [int(n) for n in PRACTICE_NUM.findall(html)]
    return max(nums) + 1 if nums else 1


def render_card(num: int, q: dict) -> str:
    topic = q.get('topic', '')
    topic_line = f'<p class="topic-tag"><strong>{topic}</strong></p>' if topic else ''
    return f'''<div class="practice-card" data-card>
 <div class="p-head"><span class="p-num">Practice {num}</span></div>
 <div class="p-body">{topic_line}<p>{q["problem"]}</p></div>
 <div class="toggle-row"><button class="toggle-btn" data-toggle>Show solution</button></div>
 <div class="solution" data-solution>
 <div class="solution-inner">
 <span class="label">Solution</span>
 {q["solution"]}
 </div>
 </div>
</div>'''


def render_section(week: int, start_num: int) -> str:
    questions = EXTENSION[week]
    cards = '\n'.join(
        render_card(start_num + i, q) for i, q in enumerate(questions)
    )
    n = len(questions)
    return f'''<!-- AUTO-ADDED PHYS143 EXAM EXTENSION -->
<section class="topic" id="sec-extension-exam">
 <div class="section-title"><span class="tag">X</span> Exam-Style Extension Set ({n} questions)</div>
 <div class="prose"><p>Exam-grade problems covering every topic in this week. Each question targets a different skill — method selection, multi-step calculation, or physical interpretation. Work closed-book first, then check the solution.</p></div>

{cards}

</section>'''


def inject(path: Path, week: int) -> bool:
    html = path.read_text(encoding='utf-8')
    if week not in EXTENSION:
        print(f'  WARN no data for week {week}')
        return False
    if not BLOCK.search(html):
        print(f'  WARN no extension block in {path.name}')
        return False
    pre = BLOCK.split(html)[0]
    start = next_practice_num(pre)
    block = render_section(week, start)
    new_html = BLOCK.sub(lambda m: block, html, count=1)
    path.write_text(new_html, encoding='utf-8')
    print(f'  updated {path.name} (+{len(EXTENSION[week])} questions, from Practice {start})')
    return True


def main():
    n = 0
    for week, path in WEEK_FILES.items():
        if path.exists() and inject(path, week):
            n += 1
    print(f'done — {n} week(s)')


if __name__ == '__main__':
    main()
