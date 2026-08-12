"""Week 5 (SFD/BMD): a labelled beam or cantilever diagram for each practice answer."""
import re
import _dpen102_kit as k
import _wk_util as u


def span(q):
    return u.first(r'(?:span|L\s*=|length)\s*(\d+(?:\.\d+)?)\s*(?:\\text\{\s*)?m', q)


def point_loads(q):
    out = []
    for val, pos in re.findall(r'(\d+(?:\.\d+)?)\s*N\b[^.]*?at\s*\\?\(?x\s*=?\s*(\d+(?:\.\d+)?)', q):
        out.append((float(pos), float(val)))
    for val in re.findall(r'(\d+(?:\.\d+)?)\s*N\s*(?:downward\s*)?(?:point\s*)?load\s*at\s*the\s*free\s*end', q):
        out.append(('tip', float(val)))
    return out


def udl(q):
    return u.first(r'w\s*=?\s*(\d+(?:\.\d+)?)\s*(?:\\text\{\s*)?N\s*/\s*m', q)


# capture the final computed value: skip through any "...=" chain, stop at N
_FINAL = r'\s*=\s*(?:[^.N]*=\s*)?(-?\d+(?:\.\d+)?)\s*(?:\\text\{)?\s*N'


def reactions(a):
    ra = u.first(r'R_A' + _FINAL, a)
    rb = u.first(r'R_B' + _FINAL, a)
    if ra is None:
        ra = u.first(r'R_\{?Ay\}?' + _FINAL, a)
    return ra, rb


def mmax(a):
    return u.first(r'M_\{?max\}?' + _FINAL, a)


def build(num, q, a):
    L = span(q) or 6.0
    pl = point_loads(q)
    w = udl(q)
    ra, rb = reactions(a)
    mm = mmax(a)
    is_cant = 'cantilever' in q.lower()

    note_bits = []
    if ra is not None and rb is not None:
        note_bits.append('R_A = %s N, R_B = %s N' % (u.g(ra), u.g(rb)))
    elif ra is not None:
        note_bits.append('R_A = %s N' % u.g(ra))
    if mm is not None:
        note_bits.append('M_max = %s N.m' % u.g(mm))
    note = ';  '.join(note_bits) if note_bits else None

    if is_cant:
        tip = None
        udl_lab = None
        for pos, val in pl:
            if pos == 'tip':
                tip = '%s N' % u.g(val)
        if w is not None:
            udl_lab = 'w = %s N/m' % u.g(w)
        if ra is not None and note is None:
            note = 'fixed-end R = %s N' % u.g(ra)
        return k.cantilever_fig(L, udl=udl_lab, tip=tip, note=note)

    loads = [(pos, '%s N' % u.g(val)) for pos, val in pl if pos != 'tip' and pos <= L]
    udl_arg = ('w = %s N/m' % u.g(w),) if w is not None else None
    cut = None
    mcut = re.search(r'at\s*\\?\(?x\s*=?\s*(\d+(?:\.\d+)?)\s*(?:\\text\{)?m\)?', q)
    ra_s = 'R_A = %s N' % u.g(ra) if ra is not None else 'R_A'
    rb_s = 'R_B = %s N' % u.g(rb) if rb is not None else 'R_B'
    return k.beam_fig(L, loads=loads, udl=udl_arg, ra=ra_s, rb=rb_s, note=note)


if __name__ == '__main__':
    fn = 'Lesson_Week5_SFD_BMD.html'
    n = u.inject(fn, build)
    miss, bad = u.validate(fn)
    print('week5 added', n, 'missing', miss, 'malformed', bad)
