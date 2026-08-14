#!/usr/bin/env python3
"""Exam-style SVG diagrams for DPEN022 limits / area practice questions."""
import math

NAVY = '#1B3A5C'
BLUE = '#185FA5'
ORANGE = '#c2410c'
GREEN = '#15803d'
FILL = '#93c5fd'
FILL2 = '#fcd34d'
GREY = '#6b6762'
GRID = '#eef1f5'
SERIF = "Georgia,'Times New Roman',serif"

W, H = 420, 300
ML, MR, MT, MB = 42, 28, 22, 34


def _esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _text(x, y, s, *, size=11, fill=GREY, anchor='middle', weight='normal'):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{SERIF}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{_esc(s)}</text>')


def _axes(sx, sy, xmin, xmax, ymin, ymax, pw, ph):
    parts = []
    # light grid
    for i in range(math.ceil(xmin), math.floor(xmax) + 1):
        parts.append(f'<line x1="{sx(i):.1f}" y1="{MT}" x2="{sx(i):.1f}" y2="{MT+ph}" '
                     f'stroke="{GRID}" stroke-width="1"/>')
    for j in range(math.ceil(ymin), math.floor(ymax) + 1):
        parts.append(f'<line x1="{ML}" y1="{sy(j):.1f}" x2="{ML+pw}" y2="{sy(j):.1f}" '
                     f'stroke="{GRID}" stroke-width="1"/>')
    ax_y = sy(0) if ymin <= 0 <= ymax else MT + ph
    ax_x = sx(0) if xmin <= 0 <= xmax else ML
    parts.append(f'<line x1="{ML}" y1="{ax_y:.1f}" x2="{ML+pw}" y2="{ax_y:.1f}" stroke="#111" stroke-width="1.3"/>')
    parts.append(f'<line x1="{ax_x:.1f}" y1="{MT}" x2="{ax_x:.1f}" y2="{MT+ph}" stroke="#111" stroke-width="1.3"/>')
    parts.append(_text(ML + pw + 2, ax_y - 4, 'x', size=12, fill='#111', anchor='start'))
    parts.append(_text(ax_x - 8, MT + 2, 'y', size=12, fill='#111', anchor='end'))
    # ticks
    for i in range(math.ceil(xmin), math.floor(xmax) + 1):
        if abs(i) < 1e-9:
            continue
        parts.append(f'<line x1="{sx(i):.1f}" y1="{ax_y-3:.1f}" x2="{sx(i):.1f}" y2="{ax_y+3:.1f}" stroke="#111"/>')
        parts.append(_text(sx(i), ax_y + 14, str(i), size=10))
    for j in range(math.ceil(ymin), math.floor(ymax) + 1):
        if abs(j) < 1e-9:
            continue
        parts.append(f'<line x1="{ax_x-3:.1f}" y1="{sy(j):.1f}" x2="{ax_x+3:.1f}" y2="{sy(j):.1f}" stroke="#111"/>')
        parts.append(_text(ax_x - 7, sy(j) + 3, str(j), size=10, anchor='end'))
    return ''.join(parts), ax_x, ax_y


def _wrap(inner, caption=''):
    cap = _text(ML, 14, caption, size=12, fill=NAVY, anchor='start', weight='bold') if caption else ''
    return (
        f'<div class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'preserveAspectRatio="xMidYMid meet" role="img" aria-label="{_esc(caption)}" '
        'style="width:100%;max-width:420px;height:auto;background:#fff;border:1px solid #d1d5db;'
        'border-radius:6px;margin:8px 0 4px;">'
        f'{cap}{inner}</svg></div>'
    )


def _polyline(sx, sy, xs, ys, color=BLUE, width=2.4):
    pts = ' '.join(f'{sx(x):.1f},{sy(y):.1f}' for x, y in zip(xs, ys))
    return (f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}" '
            'stroke-linejoin="round" stroke-linecap="round"/>')


def _sample(fn, a, b, n=200):
    xs, ys = [], []
    for i in range(n + 1):
        x = a + (b - a) * i / n
        try:
            y = fn(x)
        except (ValueError, ZeroDivisionError):
            continue
        if math.isfinite(y):
            xs.append(x)
            ys.append(y)
    return xs, ys


def limit_removable(*, xmin=-2, xmax=6, ymin=-1, ymax=6, hole_x=1, hole_y=4, filled_y=2,
                    caption='Graph of y = f(x)'):
    """Smooth rising curve with open circle at (hole_x, hole_y) and filled point at (hole_x, filled_y)."""
    pw, ph = W - ML - MR, H - MT - MB

    def sx(x):
        return ML + (x - xmin) / (xmax - xmin) * pw

    def sy(y):
        return MT + (ymax - y) / (ymax - ymin) * ph

    # gentle cubic-ish rise with a soft dip then up: designed so y(hole_x)≈hole_y
    def f(x):
        # affine map of a smooth bump: passes near hole_y at hole_x
        return 0.08 * (x + 1) ** 2 + 0.35 * x + 2.6

    # rescale so f(hole_x)=hole_y approximately by shifting
    shift = hole_y - f(hole_x)
    fn = lambda x: f(x) + shift  # noqa: E731

    axes, _, _ = _axes(sx, sy, xmin, xmax, ymin, ymax, pw, ph)
    xs, ys = _sample(fn, xmin + 0.05, xmax - 0.05)
    curve = _polyline(sx, sy, xs, ys)
    # open circle
    open_c = (f'<circle cx="{sx(hole_x):.1f}" cy="{sy(hole_y):.1f}" r="5.5" fill="#fff" '
              f'stroke="{BLUE}" stroke-width="2.2"/>')
    # filled value
    filled = f'<circle cx="{sx(hole_x):.1f}" cy="{sy(filled_y):.1f}" r="4.5" fill="{BLUE}"/>'
    labels = (
        _text(sx(hole_x) + 10, sy(hole_y) - 8, f'({hole_x}, {hole_y})', size=11, fill=NAVY, anchor='start')
        + _text(sx(hole_x) + 10, sy(filled_y) + 14, f'f({hole_x})={filled_y}', size=11, fill=ORANGE, anchor='start')
    )
    # dashed vertical at hole_x
    vline = (f'<line x1="{sx(hole_x):.1f}" y1="{MT}" x2="{sx(hole_x):.1f}" y2="{MT+ph}" '
             f'stroke="{ORANGE}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    return _wrap(axes + vline + curve + open_c + filled + labels, caption)


def limit_jump(*, xmin=-3, xmax=3, ymin=-2, ymax=3, a=0, y_left=1, y_right=-1,
               slope=0.0, caption='Graph of y = f(x)'):
    """Jump discontinuity at x=a: left branch ends open at y_left, right starts open at y_right."""
    pw, ph = W - ML - MR, H - MT - MB

    def sx(x):
        return ML + (x - xmin) / (xmax - xmin) * pw

    def sy(y):
        return MT + (ymax - y) / (ymax - ymin) * ph

    axes, _, _ = _axes(sx, sy, xmin, xmax, ymin, ymax, pw, ph)

    def left(x):
        return y_left + slope * (x - a)

    def right(x):
        return y_right + slope * (x - a)

    xs1, ys1 = _sample(left, xmin + 0.05, a - 0.02)
    xs2, ys2 = _sample(right, a + 0.02, xmax - 0.05)
    curve = _polyline(sx, sy, xs1, ys1) + _polyline(sx, sy, xs2, ys2)
    open_l = (f'<circle cx="{sx(a):.1f}" cy="{sy(y_left):.1f}" r="5.5" fill="#fff" '
              f'stroke="{BLUE}" stroke-width="2.2"/>')
    open_r = (f'<circle cx="{sx(a):.1f}" cy="{sy(y_right):.1f}" r="5.5" fill="#fff" '
              f'stroke="{BLUE}" stroke-width="2.2"/>')
    vline = (f'<line x1="{sx(a):.1f}" y1="{MT}" x2="{sx(a):.1f}" y2="{MT+ph}" '
             f'stroke="{ORANGE}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    labels = (
        _text(sx(a) - 8, sy(y_left) - 8, f'y→{y_left}', size=11, fill=NAVY, anchor='end')
        + _text(sx(a) + 8, sy(y_right) + 14, f'y→{y_right}', size=11, fill=NAVY, anchor='start')
        + _text(sx(a), MT + ph + 16, f'x={a}', size=11, fill=ORANGE)
    )
    return _wrap(axes + vline + curve + open_l + open_r + labels, caption)


def limit_one_sided(*, xmin=-0.5, xmax=4, ymin=-4, ymax=2, caption='Graph of y = ln x (x > 0)'):
    """ln-style curve → −∞ as x→0+."""
    pw, ph = W - ML - MR, H - MT - MB

    def sx(x):
        return ML + (x - xmin) / (xmax - xmin) * pw

    def sy(y):
        return MT + (ymax - y) / (ymax - ymin) * ph

    axes, _, _ = _axes(sx, sy, xmin, xmax, ymin, ymax, pw, ph)
    xs, ys = _sample(math.log, 0.05, xmax - 0.05)
    # clip to window
    pts = [(x, y) for x, y in zip(xs, ys) if ymin <= y <= ymax]
    xs, ys = zip(*pts) if pts else ([], [])
    curve = _polyline(sx, sy, xs, ys) if xs else ''
    note = _text(sx(0.6), sy(-2.5), 'as x → 0⁺,  y → −∞', size=11, fill=ORANGE, anchor='start')
    return _wrap(axes + curve + note, caption)


def area_under(fn, a, b, *, xmin=None, xmax=None, ymin=None, ymax=None,
               caption='', shade_label='shaded region', n=220):
    """Shade area between curve and x-axis from a to b (absolute: only where curve ≥ 0 by default)."""
    xs_f, ys_f = _sample(fn, a, b, n)
    if xmin is None:
        xmin = min(a, 0) - 0.5
    if xmax is None:
        xmax = max(b, 0) + 0.5
    if ymin is None:
        ymin = min(0, min(ys_f) - 0.5)
    if ymax is None:
        ymax = max(0, max(ys_f) + 0.5)
    pw, ph = W - ML - MR, H - MT - MB

    def sx(x):
        return ML + (x - xmin) / (xmax - xmin) * pw

    def sy(y):
        return MT + (ymax - y) / (ymax - ymin) * ph

    axes, _, ax_y = _axes(sx, sy, xmin, xmax, ymin, ymax, pw, ph)
    # shade polygon
    poly = [f'{sx(a):.1f},{ax_y:.1f}']
    for x, y in zip(xs_f, ys_f):
        poly.append(f'{sx(x):.1f},{sy(y):.1f}')
    poly.append(f'{sx(b):.1f},{ax_y:.1f}')
    shade = f'<polygon points="{" ".join(poly)}" fill="{FILL}" fill-opacity="0.55" stroke="none"/>'
    # full curve a bit wider
    xs_c, ys_c = _sample(fn, max(xmin, a - 0.8), min(xmax, b + 0.8), 300)
    curve = _polyline(sx, sy, xs_c, ys_c)
    # endpoint ticks
    marks = (
        f'<line x1="{sx(a):.1f}" y1="{ax_y-4:.1f}" x2="{sx(a):.1f}" y2="{ax_y+4:.1f}" stroke="{ORANGE}" stroke-width="1.6"/>'
        + f'<line x1="{sx(b):.1f}" y1="{ax_y-4:.1f}" x2="{sx(b):.1f}" y2="{ax_y+4:.1f}" stroke="{ORANGE}" stroke-width="1.6"/>'
        + _text(sx(a), ax_y + 14, _fmt(a), size=11, fill=ORANGE)
        + _text(sx(b), ax_y + 14, _fmt(b), size=11, fill=ORANGE)
        + _text((sx(a) + sx(b)) / 2, sy(max(ys_f)) - 10, shade_label, size=11, fill=NAVY)
    )
    return _wrap(axes + shade + curve + marks, caption)


def area_between(f, g, a, b, *, xmin=None, xmax=None, ymin=None, ymax=None,
                 caption='', label_f='y = f(x)', label_g='y = g(x)', n=220):
    """Shade region between two curves from a to b."""
    xs, ys_f, ys_g = [], [], []
    for i in range(n + 1):
        x = a + (b - a) * i / n
        y1, y2 = f(x), g(x)
        if math.isfinite(y1) and math.isfinite(y2):
            xs.append(x)
            ys_f.append(y1)
            ys_g.append(y2)
    if xmin is None:
        xmin = min(a, 0) - 0.6
    if xmax is None:
        xmax = max(b, 0) + 0.6
    all_y = ys_f + ys_g + [0]
    if ymin is None:
        ymin = min(all_y) - 0.6
    if ymax is None:
        ymax = max(all_y) + 0.6
    pw, ph = W - ML - MR, H - MT - MB

    def sx(x):
        return ML + (x - xmin) / (xmax - xmin) * pw

    def sy(y):
        return MT + (ymax - y) / (ymax - ymin) * ph

    axes, _, _ = _axes(sx, sy, xmin, xmax, ymin, ymax, pw, ph)
    # shaded band: along f then back along g
    poly = [f'{sx(x):.1f},{sy(y):.1f}' for x, y in zip(xs, ys_f)]
    poly += [f'{sx(x):.1f},{sy(y):.1f}' for x, y in zip(reversed(xs), reversed(ys_g))]
    shade = f'<polygon points="{" ".join(poly)}" fill="{FILL}" fill-opacity="0.55" stroke="none"/>'
    # curves slightly beyond
    pad = 0.5
    xs1, ys1 = _sample(f, max(xmin, a - pad), min(xmax, b + pad), 280)
    xs2, ys2 = _sample(g, max(xmin, a - pad), min(xmax, b + pad), 280)
    c1 = _polyline(sx, sy, xs1, ys1, BLUE)
    c2 = _polyline(sx, sy, xs2, ys2, ORANGE)
    # intersection markers
    marks = ''
    for x in (a, b):
        y = f(x)
        marks += f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="3.8" fill="{NAVY}"/>'
        marks += _text(sx(x), sy(y) - 10, f'({_fmt(x)}, {_fmt(y)})', size=10, fill=NAVY)
    labels = (
        _text(sx(xs1[-1]) - 4, sy(ys1[-1]) - 6, label_f, size=11, fill=BLUE, anchor='end')
        + _text(sx(xs2[-1]) - 4, sy(ys2[-1]) + 14, label_g, size=11, fill=ORANGE, anchor='end')
    )
    return _wrap(axes + shade + c1 + c2 + marks + labels, caption)


def _fmt(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return f'{v:g}'
