"""Shared helpers for injecting diagrams into DPEN102 lesson practice answers."""
import re
from pathlib import Path
import xml.dom.minidom as _M

BASE = Path(__file__).resolve().parent
DIR = BASE / 'siddharth' / 'dpen102'

STYLE_ANCHOR = '.solution-inner p{ margin:8px 0; }'
STYLE_RULE = (
    '.solution-inner p{ margin:8px 0; }\n'
    '  .solution-inner svg{ display:block; margin:12px auto; max-width:100%; '
    'height:auto; background:#fff; border:1px solid #d6deea; border-radius:6px; }')


def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = s.replace('&nbsp;', ' ').replace('&sup2;', '2').replace('&amp;', '&')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def cards(html):
    """Yield (num, whole_segment, question_text, solution_text, seg_start, seg_end)."""
    idxs = [m.start() for m in re.finditer(r'<div class="practice-card"', html)]
    idxs.append(len(html))
    for i in range(len(idxs) - 1):
        seg = html[idxs[i]:idxs[i + 1]]
        m = re.search(r'Practice (\d+)', seg)
        num = int(m.group(1)) if m else (i + 1)
        body = re.search(r'<div class="p-body">(.*?)</div>\s*<div class="toggle-row"', seg, re.S)
        sol = re.search(r'<div class="solution-inner">(.*?)</div></div>\s*</div>', seg, re.S)
        q = clean(body.group(1)) if body else ''
        a = clean(sol.group(1)) if sol else ''
        yield num, seg, q, a, idxs[i], idxs[i + 1]


def inject(filename, builder):
    """builder(num, q, a) -> svg string or None. Injects after the Solution label."""
    path = DIR / filename
    html = path.read_text()
    if '.solution-inner svg{' not in html:
        html = html.replace(STYLE_ANCHOR, STYLE_RULE, 1)
    added = 0
    # rebuild from the back so offsets stay valid
    segs = list(cards(html))
    out = html
    for num, seg, q, a, s0, s1 in reversed(segs):
        if '<svg' in seg:
            continue
        svg = builder(num, q, a)
        if not svg:
            continue
        anchor = '<span class="label">Solution</span>'
        pos = out.find(anchor, s0, s1)
        if pos == -1:
            continue
        at = pos + len(anchor)
        out = out[:at] + '\n    ' + svg + '\n' + out[at:]
        added += 1
    path.write_text(out)
    return added


def validate(filename):
    html = (DIR / filename).read_text()
    bad, missing = [], []
    for num, seg, q, a, s0, s1 in cards(html):
        svgs = re.findall(r'<svg.*?</svg>', seg, re.S)
        if not svgs:
            missing.append(num)
            continue
        for sv in svgs:
            if 'class="diagram"' in sv:  # pre-existing teaching svg, uses HTML entities
                continue
            try:
                _M.parseString(sv.encode('utf-8'))
            except Exception as e:
                bad.append((num, str(e)[:60]))
    return missing, bad


# ----- number parsing -----

def nums(pattern, text, cast=float):
    return [cast(x) for x in re.findall(pattern, text)]


def first(pattern, text, cast=float, default=None):
    m = re.search(pattern, text)
    return cast(m.group(1)) if m else default


def g(x):
    """Trim a float to a short string."""
    if x is None:
        return ''
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ('%.2f' % x).rstrip('0').rstrip('.')


def angle_deg(text, default=20.0):
    m = re.search(r'(\d+(?:\.\d+)?)\s*(?:&deg;|\^\{?\\?circ\}?|\\,?\^?\\circ|°)', text)
    return float(m.group(1)) if m else default


def beta_deg(text, default=180.0):
    """Wrap angle in degrees from '90&deg;' or 'pi/2 rad' style text."""
    m = re.search(r'(\d+(?:\.\d+)?)\s*(?:&deg;|°|\\?circ)', text)
    if m:
        return float(m.group(1))
    m = re.search(r'(\d*)\s*\\?pi(?:\s*/\s*(\d+))?', text)
    if m:
        coef = float(m.group(1)) if m.group(1) else 1.0
        den = float(m.group(2)) if m.group(2) else 1.0
        return coef * 180.0 / den
    return default


def caption(a, limit=72):
    """Turn a LaTeX-ish solution snippet into a short, XML-safe ASCII note."""
    a = re.sub(r'^\s*Solution\s*', '', a)
    m = re.findall(r'\\boxed\{(.*?)\}', a)
    s = m[-1] if m else a
    if not m:
        # take the last clause that contains an '='
        parts = re.split(r'(?<=\.)\s+|&check;|\\Rightarrow|\\Longrightarrow', a)
        parts = [p for p in parts if '=' in p]
        if parts:
            s = parts[-1]
    # normalise common LaTeX
    s = re.sub(r'\\d?frac\{([^{}]*)\}\{([^{}]*)\}', r'\1/\2', s)
    s = s.replace('\\times', ' x ').replace('\\cdot', '.').replace('\\approx', '=')
    s = s.replace('\\text', '').replace('\\,', ' ').replace('\\ ', ' ')
    s = re.sub(r'\^\{?2\}?', '^2', s)
    s = re.sub(r'\^\{?3\}?', '^3', s)
    s = re.sub(r'_\{([A-Za-z0-9]+)\}', r'_\1', s)
    s = s.replace('\\Rightarrow', ' -> ').replace('\\to', ' -> ')
    s = re.sub(r'\\[a-zA-Z]+', ' ', s)          # drop remaining commands
    s = s.replace('\\(', ' ').replace('\\)', ' ')
    s = s.replace('{', '').replace('}', '').replace('$', '')
    s = s.replace('>', ' gt ').replace('<', ' lt ').replace('&', ' and ')
    s = re.sub(r'[^A-Za-z0-9 =+\-./,%()°_]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip(' .,')
    if len(s) > limit:
        s = s[:limit].rsplit(' ', 1)[0]
    return s or None
