#!/usr/bin/env python3
"""Inject Q11–Q20 exam practice into DPEN103 week deep-dive pages."""

import re
from pathlib import Path

from _dpen103_exam_extra_data import EXTRA

OUT = Path(__file__).parent / 'siddharth' / 'dpen103'
H2_PATTERN = re.compile(
    r'(<h2 id="exam-practice">Exam practice — )10( questions</h2>)'
)
INTRO_PATTERN = re.compile(
    r'<p class="intro">Four multiple choice, two true/false, and four short '
    r'calculations or explanations\. Answer before opening the worked solution\.</p>'
)
NEW_INTRO = (
    '<p class="intro">Eight multiple choice, four true/false, and eight short '
    'calculations or explanations. Answer before opening the worked solution.</p>'
)
Q11_MARKER = re.compile(r'Q11 ·')
EXTRA_ARTICLES = re.compile(
    r'(\n  <article class="exam-q">\s*\n'
    r'    <div class="exam-qhead"><span>Q(?:1[1-9]|20) ·.*?</article>)+',
    re.DOTALL,
)
EXAM_SET_PATTERN = re.compile(
    r'(<div class="exam-set">)(.*?)(</div>\s*\n\n<div class="pager">)',
    re.DOTALL,
)

def render_question(num: int, q: dict) -> str:
    qtype, difficulty = q['tags']
    parts = [
        '  <article class="exam-q">',
        f'    <div class="exam-qhead"><span>Q{num} · {qtype}</span><span>{difficulty}</span></div>',
        f'    {q["stem"]}',
    ]
    if qtype == 'Multiple choice':
        opts = '\n'.join(f'      <li>{opt}</li>' for opt in q['options'])
        parts.append(f'    <ol class="options" type="A">\n{opts}\n    </ol>')
    summary = q.get('summary', 'Show answer and reasoning')
    parts.append(
        f'    <details class="q"><summary>{summary}</summary>'
        f'<div class="ans">{q["answer"]}</div></details>'
    )
    parts.append('  </article>')
    return '\n'.join(parts)


def render_week(week: int) -> str:
    return '\n'.join(
        render_question(num, q) for num, q in zip(range(11, 21), EXTRA[week])
    )


def inject(path: Path, refresh: bool = False) -> str:
    html = path.read_text(encoding='utf-8')
    has_q11 = bool(Q11_MARKER.search(html))
    if has_q11 and not refresh:
        return 'skipped'
    if has_q11 and refresh:
        html = EXTRA_ARTICLES.sub('', html, count=1)
    week = int(path.stem.split('-')[1])
    if week not in EXTRA:
        print(f'  WARN {path.name}: no EXTRA data for week {week}')
        return 'warn'
    block = render_week(week)
    match = EXAM_SET_PATTERN.search(html)
    if not match:
        print(f'  WARN {path.name}: could not find .exam-set closing tag')
        return 'warn'
    new_inner = match.group(2).rstrip() + '\n' + block + '\n'
    html = (
        html[: match.start()]
        + match.group(1)
        + new_inner
        + match.group(3)
        + html[match.end() :]
    )
    html = H2_PATTERN.sub(r'\g<1>20\2', html)
    html = INTRO_PATTERN.sub(NEW_INTRO, html)
    path.write_text(html, encoding='utf-8')
    return 'updated'


def main() -> None:
    import sys
    refresh = '--refresh' in sys.argv
    counts = {'updated': 0, 'skipped': 0, 'warn': 0}
    for week in range(1, 14):
        path = OUT / f'week-{week:02d}-deep-dive.html'
        if not path.exists():
            counts['warn'] += 1
            print(f'  WARN missing {path.name}')
            continue
        result = inject(path, refresh=refresh)
        counts[result] += 1
        print(f'  {result}: {path.name}')
    print(
        f'done — updated {counts["updated"]}, '
        f'skipped {counts["skipped"]}, warnings {counts["warn"]}'
    )


if __name__ == '__main__':
    main()
