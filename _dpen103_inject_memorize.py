#!/usr/bin/env python3
"""Insert know-cold memorisation blocks at the top of DPEN103 week pages."""

import re
from pathlib import Path

from _dpen103_memorize import render_week

OUT = Path(__file__).parent / 'siddharth' / 'dpen103'
MARKER = 'id="memorize"'
INSERT_AFTER = re.compile(
    r'(</div>\s*\n)(<div class="spine">)',
)
MEMORIZE_SECTION = re.compile(
    r'<section class="memorize" id="memorize">.*?</section>\s*',
    re.DOTALL,
)


def inject(path: Path) -> bool:
    html = path.read_text(encoding='utf-8')
    week = int(path.stem.split('-')[1])
    block = render_week(week)
    if MARKER in html:
        new_html, n = MEMORIZE_SECTION.subn(lambda _m: block + '\n\n', html, count=1)
        if n:
            path.write_text(new_html, encoding='utf-8')
            print(f'  updated memorize in {path.name}')
            return True
        print(f'  WARN {path.name}: marker found but section not matched')
        return False
    m = INSERT_AFTER.search(html)
    if not m:
        print(f'  WARN {path.name}: could not find insertion point')
        return False
    new_html = html[: m.start(2)] + block + '\n\n' + html[m.start(2) :]
    path.write_text(new_html, encoding='utf-8')
    print(f'  added memorize to {path.name}')
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
