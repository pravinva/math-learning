"""Weeks 10-13 (mixed synthesis): detect each question's topic and route to the
matching diagram builder, reusing the per-week modules and _dpen102_kit."""
import re
import sys
import _dpen102_kit as k
import _wk_util as u
import _w5, _w6, _w7, _w8, _w9


def has(text, *words):
    t = text.lower()
    return any(w in t for w in words)


def stress_build(num, q, a):
    cap = u.caption(a)
    d = u.first(r'diameter\s*(?:of\s*)?(\d+(?:\.\d+)?)\s*mm', q)
    A = u.first(r'area\s*(?:of\s*)?(\d+(?:\.\d+)?)\s*mm', q) or u.first(r'(\d+(?:\.\d+)?)\s*mm&sup2;', q)
    F = u.first(r'(\d+(?:\.\d+)?)\s*kN', q)
    sy = u.first(r'\\sigma_y\s*=?\s*(\d+(?:\.\d+)?)', q)
    fos = u.first(r'FoS\s*=?\s*(\d+(?:\.\d+)?)', q)

    if has(q, 'bending', 'moment') and (has(q, 'section') or 'M=' in q or '\\text{kN}\\cdot' in q):
        return k.bending_section(b='b', h='h', c='c', M='M', sigma=cap)

    if has(q, 'fos', 'allowable', 'yield', 'safe', 'margin', 'factor of safety'):
        pairs = []
        if sy is not None:
            pairs.append(('yield &#963;_y', sy))
        allow = (sy / fos) if (sy is not None and fos) else None
        if allow is not None:
            pairs.append(('allowable', allow, k.GREEN))
        if pairs:
            return k.stress_bars(pairs, verdict=cap, unit='MPa')
        return k.stress_bars([('working', 100)], verdict=cap, unit='MPa')

    if d is not None:
        return k.section_circle(d_label='d = %s mm' % u.g(d),
                                force=('%s kN' % u.g(F)) if F is not None else 'F',
                                stress=cap)
    return k.bar_axial(F=('%s kN' % u.g(F)) if F is not None else 'F',
                       A=('A = %s mm&#178;' % u.g(A)) if A is not None else 'A',
                       note=cap)


def statics_build(num, q, a):
    cap = u.caption(a)
    if q.strip().lower().startswith('convert') or has(q, 'convert '):
        m = re.search(r'convert\s+([0-9.]+\s*\w+)\s+to\s+(\w+)', q, re.I)
        if m:
            return k.unit_ladder([(m.group(1), '&#215; ?', m.group(2))], title='unit conversion')
        return k.unit_ladder([('value', '&#215; ?', 'target')], title='unit conversion')
    if has(q, 'ladder'):
        th = u.angle_deg(q, 65.0)
        return k.fbd_incline(theta=th, labels={'W': 'W', 'N': 'N_wall', 'f': 'f'}, moving=cap)
    if has(q, 'hang', 'rope', 'cable', 'ring', 'sign'):
        a1 = u.angle_deg(q, 40.0)
        return k.joint_fig([(180 - a1, 'T_1'), (a1, 'T_2')], load=(270, 'W'),
                           title='suspended load', note=cap)
    if has(q, 'component'):
        th = u.angle_deg(q, 35.0)
        return k.resolve_fig(F='F', angle=th, fx='F_x', fy='F_y', note=cap)
    if has(q, 'normal force', 'rests on', 'on a table'):
        return k.fbd_level(mass='m', caption=cap)
    if has(q, 'net force', 'accelerat'):
        return k.push_slide(F='F', note=cap)
    return k.resolve_fig(F='F', angle=30, fx='F_x', fy='F_y', note=cap)


def detect(q, a):
    if q.strip().lower().startswith('convert'):
        return 'statics'
    if has(q, 'truss', 'joint', 'method of sections', 'panel', 'chord') or re.search(r'F_\{?[A-Z]{2}', q):
        return 'truss'
    # section geometry / second moment of area / bending-stress checks
    bending = has(q, 'bending') and (has(q, 'section') or 'M=' in q or 'M ' in q or '\\cdot' in q)
    if (has(q, 'centroid', 'second moment', 'parallel axis', 'flange', 'web', 'i-section',
            'i-like', 't-section', 't-shape', 'composite', 'moment of area', 'stiffness',
            'two sections', 'material budget', 'better section')
            or '\\bar' in q or 'I_x' in q or re.search(r'\bI\s*=', q) or bending):
        return 'inertia'
    # energy / work (avoid 'pin-roller' beams by requiring 'roller coaster')
    if has(q, 'spring', 'kinetic', 'work-energy', 'net work', 'work is done', 'work done on',
           'launch', 'dropped', 'thrown', 'roller coaster', 'roller-coaster', 'speed',
           'stored pe', 'stored energy', 'max height', 'maximum height'):
        return 'energy'
    if has(q, 'belt', 'wrap', 'capstan', 'drum', 'wedge', 'incline', 'ramp', 'slope',
           'repose', 'coefficient of friction') or '\\mu' in q:
        return 'friction'
    # design / strength capacity checks (before beam, so a "beam section, FoS" is a stress check)
    if has(q, 'fos', 'factor of safety', 'allowable', 'yield', 'safe load', 'is it safe',
           'margin', 'does it pass', 'pass/fail', 'working stress', 'max safe') or '\\sigma_y' in q:
        return 'stress'
    if has(q, 'cantilever', 'simply-supported', 'simply supported', 'span', 'udl',
           'overhang', 'point load', 'm_max') or re.search(r'\bbeam\b', q.lower()):
        return 'beam'
    if has(q, 'stress', 'axial load', '\\sigma') or re.search(r'diameter[^.]*carries', q, re.I):
        return 'stress'
    return 'statics'


ROUTER = {
    'beam': _w5.build,
    'truss': _w6.build,
    'friction': _w7.build,
    'inertia': _w8.build,
    'energy': _w9.build,
    'stress': stress_build,
    'statics': statics_build,
}


def build(num, q, a):
    topic = detect(q, a)
    try:
        return ROUTER[topic](num, q, a)
    except Exception:
        return k.checklist([u.caption(a) or 'see solution'], title='result')


FILES = [
    'Lesson_Week10_Integrated_Statics_Practice.html',
    'Lesson_Week11_Design_Blocks.html',
    'Lesson_Week12_Exam_Synthesis.html',
    'Lesson_Week13_Final_Readiness.html',
]

if __name__ == '__main__':
    for fn in FILES:
        n = u.inject(fn, build)
        miss, bad = u.validate(fn)
        print(fn, 'added', n, 'missing', miss, 'malformed', bad)
