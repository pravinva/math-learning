"""Week 6 (trusses): joint / section / reaction / resolve diagrams per practice answer."""
import re
import _dpen102_kit as k
import _wk_util as u

FINAL = r'\s*=\s*(?:[^.N]*=\s*)?(-?\d+(?:\.\d+)?)\s*(?:\\text\{)?\s*N'


def build(num, q, a):
    ql, al = q.lower(), a.lower()
    cap = u.caption(a)

    # 1) resolving a force into components
    if 'resolve' in ql or '3-4-5' in q or 'direction cosine' in al or 'component' in ql:
        fx = u.first(r'F_x\s*=\s*(?:[^.N]*=\s*)?(-?\d+(?:\.\d+)?)', a)
        fy = u.first(r'F_y\s*=\s*(?:[^.N]*=\s*)?(-?\d+(?:\.\d+)?)', a)
        ang = 37 if '3-4-5' in q else 37
        return k.resolve_fig(F='F', angle=ang,
                             fx='F_x = %s N' % u.g(fx) if fx is not None else 'F_x',
                             fy='F_y = %s N' % u.g(fy) if fy is not None else 'F_y',
                             note=cap)

    # 2) single pin joint / zero-force reasoning (no cut, no reactions)
    joint = any(w in ql for w in ('joint', 'zero-force', 'collinear'))
    if joint and 'cut' not in ql and 'section' not in ql and 'reaction' not in ql:
        loaded = ('load' in ql and 'unloaded' not in ql) or 'IS an external load' in q
        if 'two members' in ql or 'only two' in ql:
            members = [(200, 'a', 'zero'), (340, 'b', 'zero')]
            load = None
        else:
            zero = 'zero' in al and not loaded
            members = [(180, 'DE'), (0, 'DF'), (90, 'DG', 'zero' if zero else '')]
            load = (270, 'P') if loaded else None
        return k.joint_fig(members, load=load, note=cap)

    # reactions present in the answer
    ra = u.first(r'R_A' + FINAL, a)
    rb = u.first(r'R_B' + FINAL, a)
    ri = u.first(r'R_I' + FINAL, a)
    right = rb if rb is not None else ri
    right_lab = 'R_B = %s N' % u.g(rb) if rb is not None else (
        'R_I = %s N' % u.g(ri) if ri is not None else 'R_B')
    ra_lab = 'R_A = %s N' % u.g(ra) if ra is not None else 'R_A'

    # 3) reaction-only questions: no section cut needed
    if ('reaction' in ql and 'cut' not in ql and 'section' not in ql
            and 'method of sections' not in ql):
        loads = []
        for val, pos in re.findall(r'(\d+(?:\.\d+)?)\s*N\b[^.]*?at\s*(\d+(?:\.\d+)?)\s*m', q):
            loads.append((float(pos) / 3.5 + 0.5, '%s N' % u.g(float(val))))
        if not loads:
            loads = [(2.0, 'P')]
        return k.truss_cut(loads=loads[:3], ra=ra_lab, rb=right_lab,
                           show_cut=False, note=cap)

    # 4) everything else: a section cut through three members (sign, symmetry, method)
    members = ('F_top', 'F_diag', 'F_bot')
    m = re.search(r'F_\{?([A-Z]{2})\}?', a)
    return k.truss_cut(loads=[(2.0, 'load')], ra=ra_lab, rb=right_lab,
                       members=members, show_cut=True, note=cap)


if __name__ == '__main__':
    fn = 'Lesson_Week6_Truss_Method_of_Sections.html'
    n = u.inject(fn, build)
    miss, bad = u.validate(fn)
    print('week6 added', n, 'missing', miss, 'malformed', bad)
