#!/usr/bin/env python3
"""Clean labelled SVG sketches for the DPEN022 trig graph-sketching answers.

Every element carries inline presentation attributes (no CSS classes) so the
figures render identically in browsers, PDF exports and print.
"""
import math
from fractions import Fraction

NAVY = '#1B3A5C'
BLUE = '#185FA5'
ORANGE = '#c2410c'
GREEN = '#15803d'
GREY = '#6b6762'
RED = '#b91c1c'
GRID = '#eeeae3'
SERIF = 'Georgia,\'Times New Roman\',serif'

W, H = 660, 380
ML, MR, MT, MB = 66, 92, 34, 66


def pi_label(x, zero='0'):
    """Format a multiple of pi as a readable tick label."""
    if abs(x) < 1e-9:
        return zero
    f = Fraction(x / math.pi).limit_denominator(24)
    n, d = f.numerator, f.denominator
    sign = '\u2212' if n < 0 else ''
    n = abs(n)
    num = '\u03c0' if n == 1 else f'{n}\u03c0'
    return f'{sign}{num}' if d == 1 else f'{sign}{num}/{d}'


def num_label(v):
    if abs(abs(v) - 0.5) < 1e-9:
        return '\u2212\u00bd' if v < 0 else '\u00bd'
    if abs(v - round(v)) < 1e-9:
        v = int(round(v))
        return f'\u2212{abs(v)}' if v < 0 else str(v)
    return f'{v:g}'.replace('-', '\u2212')


def _esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _text(x, y, s, *, size=12, fill=GREY, anchor='start', weight='normal'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{SERIF}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{_esc(s)}</text>')


def plot(fn, xmin, xmax, ymin, ymax, keypoints, *,
         midline=None, amplitude=None, period=None, asymptotes=(),
         caption='', extra_notes=(), yticks=None, xticks=None,
         label_points=None):
    """Return an SVG string for one sketched trig graph.

    ``keypoints`` are always drawn as marked critical points.  ``xticks`` can
    independently control the vertical grid and x-axis labels, while
    ``label_points`` controls which keypoints receive coordinate text.  The
    defaults preserve the original behaviour for existing callers.
    """
    pw, ph = W - ML - MR, H - MT - MB

    def sx(x):
        return ML + (x - xmin) / (xmax - xmin) * pw

    def sy(y):
        return MT + (ymax - y) / (ymax - ymin) * ph

    marker_suffix = sum((i + 1) * ord(ch) for i, ch in enumerate(caption)) % 100000
    marker_green = f'arG{marker_suffix}'
    marker_navy = f'arN{marker_suffix}'
    total_h = H + 14 * len(extra_notes)
    p = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {total_h}" width="{W}" height="{total_h}" '
        f'preserveAspectRatio="xMidYMid meet" role="img" aria-label="{_esc(caption)}" '
        'style="width:100%;height:auto;max-width:660px;background:#fff;border:1px solid #e8e6e0;'
        'border-radius:8px;margin:10px 0;">',
        '<defs>'
        f'<marker id="{marker_green}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" '
        f'orient="auto-start-reverse"><path d="M 0 1 L 7 5 L 0 9 z" fill="{GREEN}"/></marker>'
        f'<marker id="{marker_navy}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" '
        f'orient="auto-start-reverse"><path d="M 0 1 L 7 5 L 0 9 z" fill="{NAVY}"/></marker>'
        '</defs>',
    ]

    if caption:
        p.append(_text(ML, 20, caption, size=14, fill=NAVY, weight='bold'))

    # gridlines
    gy = math.ceil(ymin)
    while gy <= ymax:
        p.append(f'<line x1="{ML}" y1="{sy(gy):.1f}" x2="{ML+pw}" y2="{sy(gy):.1f}" '
                 f'stroke="{GRID}" stroke-width="1"/>')
        gy += 1
    x_tick_values = list(xticks) if xticks is not None else [x for x, _ in keypoints]
    for x in x_tick_values:
        p.append(f'<line x1="{sx(x):.1f}" y1="{MT}" x2="{sx(x):.1f}" y2="{MT+ph}" '
                 f'stroke="{GRID}" stroke-width="1"/>')

    # max / min envelope
    if midline is not None and amplitude:
        for lvl, name in ((midline + amplitude, 'max'), (midline - amplitude, 'min')):
            if ymin <= lvl <= ymax:
                p.append(f'<line x1="{ML}" y1="{sy(lvl):.1f}" x2="{ML+pw}" y2="{sy(lvl):.1f}" '
                         f'stroke="{GREEN}" stroke-width="1.2" stroke-dasharray="4 4"/>')
                p.append(_text(ML + pw + 6, sy(lvl) + 4, f'{name} y={num_label(lvl)}',
                               size=11, fill=GREEN))

    # midline (when it is not simply the x-axis, which is already drawn and labelled)
    if midline is not None and abs(midline) > 1e-9:
        p.append(f'<line x1="{ML}" y1="{sy(midline):.1f}" x2="{ML+pw}" y2="{sy(midline):.1f}" '
                 f'stroke="{ORANGE}" stroke-width="1.5" stroke-dasharray="6 4"/>')
        p.append(_text(ML + pw + 6, sy(midline) + 4, f'midline y={num_label(midline)}',
                       size=11, fill=ORANGE))

    # asymptotes (labelled inside the plot so they clear the caption)
    for a in asymptotes:
        if xmin <= a <= xmax:
            p.append(f'<line x1="{sx(a):.1f}" y1="{MT}" x2="{sx(a):.1f}" y2="{MT+ph}" '
                     f'stroke="{RED}" stroke-width="1.5" stroke-dasharray="5 4"/>')
            inward = 6 if a <= (xmin + xmax) / 2 else -6
            anchor = 'start' if inward > 0 else 'end'
            p.append(_text(sx(a) + inward, MT + ph - 8, f'asymptote x={pi_label(a)}',
                           size=11, fill=RED, anchor=anchor))

    # axes
    ax_y = sy(0) if ymin <= 0 <= ymax else MT + ph
    ax_x = sx(0) if xmin <= 0 <= xmax else ML
    p.append(f'<line x1="{ML}" y1="{ax_y:.1f}" x2="{ML+pw}" y2="{ax_y:.1f}" stroke="#2c2a28" stroke-width="1.4"/>')
    p.append(f'<line x1="{ax_x:.1f}" y1="{MT}" x2="{ax_x:.1f}" y2="{MT+ph}" stroke="#2c2a28" stroke-width="1.4"/>')
    p.append(_text(ML + pw + 4, ax_y - 6, 'x', size=12, fill='#2c2a28'))
    p.append(_text(ax_x - 10, MT - 6, 'y', size=12, fill='#2c2a28', anchor='end'))

    # y ticks
    ticks = yticks if yticks is not None else list(range(math.ceil(ymin), math.floor(ymax) + 1))
    for v in ticks:
        if abs(v) < 1e-9:
            continue
        p.append(f'<line x1="{ax_x-4:.1f}" y1="{sy(v):.1f}" x2="{ax_x+4:.1f}" y2="{sy(v):.1f}" '
                 'stroke="#2c2a28" stroke-width="1.2"/>')
        p.append(_text(ax_x - 9, sy(v) + 4, num_label(v), size=11, anchor='end'))

    # curve
    segs, cur = [], []
    steps = 1000
    gap = (xmax - xmin) / 200
    for i in range(steps + 1):
        x = xmin + (xmax - xmin) * i / steps
        if any(abs(x - a) < gap for a in asymptotes):
            if len(cur) > 1:
                segs.append(cur)
            cur = []
            continue
        try:
            y = fn(x)
        except (ValueError, ZeroDivisionError):
            y = None
        if y is None or not math.isfinite(y) or not (ymin - 0.02 <= y <= ymax + 0.02):
            if len(cur) > 1:
                segs.append(cur)
            cur = []
            continue
        cur.append((sx(x), sy(y)))
    if len(cur) > 1:
        segs.append(cur)
    for seg in segs:
        pts = ' '.join(f'{px:.1f},{py:.1f}' for px, py in seg)
        p.append(f'<polyline points="{pts}" fill="none" stroke="{BLUE}" stroke-width="2.6" '
                 'stroke-linejoin="round" stroke-linecap="round"/>')

    # x ticks at key points
    seen = set()
    for x in x_tick_values:
        lbl = pi_label(x)
        if lbl in seen:
            continue
        seen.add(lbl)
        p.append(f'<line x1="{sx(x):.1f}" y1="{ax_y-4:.1f}" x2="{sx(x):.1f}" y2="{ax_y+4:.1f}" '
                 'stroke="#2c2a28" stroke-width="1.2"/>')
        p.append(_text(sx(x), MT + ph + 18, lbl, size=12, anchor='middle'))

    # key points with coordinates
    labelled = keypoints if label_points is None else label_points
    labelled_keys = {(round(x, 9), round(y, 9)) for x, y in labelled}
    for x, y in keypoints:
        above = y >= (midline if midline is not None else 0)
        dy = -10 if above else 18
        # points sitting on the x-axis get pushed clear of the axis line itself
        if abs(sy(y) - ax_y) < 2:
            dy = -12 if above else 20
        p.append(f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="4" fill="{NAVY}"/>')
        if (round(x, 9), round(y, 9)) not in labelled_keys:
            continue
        tx, anchor = sx(x), 'middle'
        if tx < ML + 36:
            tx, anchor = ML + 2, 'start'
        elif tx > ML + pw - 36:
            tx, anchor = ML + pw - 2, 'end'
        p.append(_text(tx, sy(y) + dy, f'({pi_label(x)}, {num_label(y)})',
                       size=11, fill=NAVY, anchor=anchor))

    # amplitude arrow (placed a quarter-period in, away from the y-axis labels)
    if midline is not None and amplitude:
        ax = ML + pw * 0.5
        top, bot = sy(midline + amplitude), sy(midline)
        p.append(f'<line x1="{ax:.1f}" y1="{top:.1f}" x2="{ax:.1f}" y2="{bot:.1f}" '
                 f'stroke="{GREEN}" stroke-width="1.6" marker-start="url(#{marker_green})" '
                 f'marker-end="url(#{marker_green})"/>')
        p.append(_text(ax + 7, (top + bot) / 2 + 4, f'amplitude = {num_label(amplitude)}',
                       size=12, fill=GREEN, weight='bold'))

    # period arrow under the axis
    by = MT + ph + 36
    if period:
        if asymptotes and len(asymptotes) >= 2:
            start = asymptotes[0]
        else:
            start = keypoints[0][0]
        x1, x2 = sx(start), sx(start + period)
        if x2 <= ML + pw + 1:
            p.append(f'<line x1="{x1:.1f}" y1="{by}" x2="{x2:.1f}" y2="{by}" stroke="{NAVY}" '
                     f'stroke-width="1.5" marker-start="url(#{marker_navy})" '
                     f'marker-end="url(#{marker_navy})"/>')
            p.append(_text((x1 + x2) / 2, by - 5, f'period T = {pi_label(period)}',
                           size=12, fill=NAVY, anchor='middle', weight='bold'))

    for i, note in enumerate(extra_notes):
        p.append(_text(ML, by + 22 + i * 15, note, size=12, fill=NAVY))

    p.append('</svg>')
    return ''.join(p)


PI = math.pi
