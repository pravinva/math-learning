#!/usr/bin/env python3
"""Insert narrative teaching sections into DPEN103 week pages (additive only)."""

import re
from pathlib import Path

from _dpen103_teaching import TEACHING, render_week

OUT = Path(__file__).parent / 'siddharth' / 'dpen103'
MARKER = 'id="teach"'
INSERT_AFTER = re.compile(
    r'(<div class="note">.*?</div>\s*)',
    re.DOTALL,
)
TEACH_SECTION = re.compile(
    r'<section class="teach" id="teach">.*?</section>\s*',
    re.DOTALL,
)


def inject(path: Path) -> bool:
    html = path.read_text(encoding='utf-8')
    week = int(path.stem.split('-')[1])
    block = render_week(week)
    if MARKER in html:
        new_html, n = TEACH_SECTION.subn(lambda _m: block + '\n\n', html, count=1)
        if n:
            path.write_text(new_html, encoding='utf-8')
            print(f'  updated teaching in {path.name}')
            return True
        print(f'  WARN {path.name}: marker found but section not matched')
        return False
    m = INSERT_AFTER.search(html)
    if not m:
        print(f'  WARN {path.name}: could not find insertion point')
        return False
    new_html = html[: m.end()] + '\n' + block + '\n\n' + html[m.end() :]
    path.write_text(new_html, encoding='utf-8')
    print(f'  added teaching to {path.name}')
    return True


def main():
    n = 0
    for week in range(1, 14):
        path = OUT / f'week-{week:02d}-deep-dive.html'
        if path.exists():
            n += inject(path)
    print(f'done — updated {n} file(s)')


if __name__ == '__main__':
    main()
