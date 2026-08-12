"""Inject a labelled diagram into every Week 4 lesson practice answer.

Each practice card's solution is text-only; this adds a statics SVG (built from
_dpen102_kit) keyed to that specific question's numbers. Cards that already ship
a diagram (P6, P12, P36) are left untouched.
"""
import re
from pathlib import Path
import _dpen102_kit as k

BASE = Path(__file__).resolve().parent
F = BASE / 'siddharth' / 'dpen102' / 'Lesson_Week4_Stress_Strain_Internal_Actions.html'

NAVY, GREEN, RED = k.NAVY, k.GREEN, k.RED


def figs():
    """Return {practice_number: svg} for Week 4."""
    d = {}
    # ---- axial stress ----
    d[1] = k.bar_axial(F='40 kN', A='A = 500 mm&#178;', tension=True,
                       note='&#963; = F/A = 40000 / 500&#215;10&#8315;&#8310; = 80 MPa')
    d[2] = k.section_circle(d_label='d = 8 mm', area='A = 50.3 mm&#178;', force='12 kN',
                            stress='&#963; = F/A = 238.7 MPa')
    d[4] = k.bar_axial(F='500 kN', A='A = 0.02 m&#178;', tension=False,
                       note='&#963; = F/A = 25 MPa (compressive)')
    d[11] = k.stress_bars([('working', 177.0)], allow=('yield &#963;_y', 240),
                          verdict='FoS = 240 / 177 = 1.36', unit='MPa')
    d[24] = k.stress_bars([('working', 266.7)], allow=('allowable', 240),
                          verdict='266.7 > 240 &#8594; NOT SAFE', unit='MPa')
    d[29] = k.stress_bars([('working', 138.1)], allow=('yield &#963;_y', 260),
                          verdict='FoS = 260 / 138 = 1.88', unit='MPa')
    # ---- strain ----
    d[3] = k.bar_axial(F='load', A='rod', L='L&#8320; = 3 m', dL='&#916;L = 2.4 mm',
                       note='&#949; = &#916;L / L&#8320; = 8&#215;10&#8315;&#8308;')
    d[5] = k.bar_axial(F='load', A='wire', L='L&#8320; = 1.5 m', dL='&#916;L = 3.6 mm',
                       note='&#949; = 0.0036 / 1.5 = 0.0024')
    d[26] = k.bar_axial(F='service load', A='tie', L='L&#8320; = 2.4 m', dL='&#916;L = 1.8 mm',
                        note='&#949; = 7.5&#215;10&#8315;&#8308; &lt; 9.0&#215;10&#8315;&#8308; &#8594; OK')
    d[43] = k.bar_axial(F='tension', A='rod', L='L&#8320; = 1.2 m', dL='&#916;L = 1.32 mm',
                        note='&#916;L = &#949;L&#8320; = 1.32 mm, L = 1201.32 mm')
    d[23] = k.section_circle(d_label='d = 14 mm', area='A = 153.9 mm&#178;', force='42 kN',
                             stress='&#963; = 272.8 MPa, &#949; = 5.83&#215;10&#8315;&#8308;')
    # ---- allowable stress / FoS scales ----
    d[7] = k.stress_bars([('yield &#963;_y', 300), ('allowable', 100, GREEN)],
                         verdict='A_req = F/&#963;_allow = 600 mm&#178;', unit='MPa')
    d[9] = k.stress_bars([('yield &#963;_y', 350), ('allowable', 175, GREEN)],
                         verdict='A_req = 700k / 175M = 4000 mm&#178;', unit='MPa')
    d[10] = k.stress_bars([('working', 150.0)], allow=('yield &#963;_y', 400),
                          verdict='FoS = 400 / 150 = 2.67', unit='MPa')
    d[27] = k.stress_bars([('yield &#963;_y', 300), ('allowable', 125, GREEN)],
                          verdict='A_req = 125k / 125M = 1000 mm&#178;', unit='MPa')
    d[30] = k.stress_bars([('FoS old', 1.6), ('FoS new', 2.5)], unit='',
                          verdict='area factor = 2.5 / 1.6 = 1.5625 (+56.25%)')
    d[38] = k.stress_bars([('working', 116.7)], allow=('allowable (FoS 3)', 100),
                          verdict='A_req 2100 mm&#178; &#8594; add 300 mm&#178;', unit='MPa')
    # ---- circular sizing from area ----
    d[8] = k.section_circle(d_label='d = 27.6 mm', area='A_req = 600 mm&#178;', force='60 kN',
                            stress='minimum diameter for &#963;_allow = 100 MPa')
    d[19] = k.section_circle(d_label='d = 20.2 mm', area='A_req = 320 mm&#178;', force='32 kN',
                             stress='&#963;_allow = 100 MPa &#8594; A_req = 320 mm&#178;')
    d[28] = k.section_circle(d_label='d = 36 mm', area='A_req = 1000 mm&#178;', force='125 kN',
                             stress='d = 35.68 mm &#8594; choose 36 mm')
    d[37] = k.section_circle(d_label='d = 29.3 mm', area='A_req = 672 mm&#178;', force='84 kN',
                             stress='&#963;_allow = 125 MPa &#8594; A_req = 672 mm&#178;')
    d[42] = k.section_circle(d_label='d = 24 mm', area='A = 452.4 mm&#178;', force='50 kN',
                             stress='&#963;_work = 110.5 MPa, FoS = 2.53')
    d[20] = k.stress_bars([('yield &#963;_y', 300), ('allowable', 100, GREEN)],
                          verdict='A_req = N/&#963;_allow = 1800 mm&#178;', unit='MPa')
    d[25] = k.bar_axial(F='F_max = 81.3 kN', A='A = 650 mm&#178;', tension=True,
                        note='F_max = &#963;_allow&#183;A = 125&#215;650 = 81.3 kN')
    d[21] = k.area_section(b='b = 20 mm', h='h = 10 mm', axis='rectangular tie',
                           note='A_req = 200 mm&#178; &#8594; h = 200/20 = 10 mm', shape='rect')
    # ---- internal actions: beams, cantilevers, cuts ----
    d[13] = k.beam_fig(4, loads=[(2, '200 N')], ra='R_A = 100 N', rb='R_B = 100 N',
                       cut=(2, 'cut'), dims_=[(0, 2, '2 m')],
                       note='just left of load: V = 100 N, M = 200 N&#183;m')
    d[14] = k.cantilever_fig(3, tip='90 N', dims_=[(0, 1, 'cut at 1 m')],
                             note='free-end side (2 m): N = 0, V = 90 N, M = 180 N&#183;m')
    d[15] = k.cut_segment(left_label='A', reactions=[(0.0, '80 N')], cut_x=0.72,
                          N='N', V='V = 80 N', M='M = 200 N&#183;m',
                          dims_=[(0.0, 1.0, '2.5 m')],
                          note='M = 80 &#215; 2.5 = 200 N&#183;m')
    d[16] = k.beam_fig(6, loads=[(3, 'P')], ra='R_A', rb='R_B',
                       note='all loads and reactions vertical &#8594; &#931;F_x = 0 &#8594; N = 0 everywhere')
    d[17] = k.cut_segment(left_label='A', reactions=[(0.0, 'R_A')], cut_x=0.66,
                          note='either side alone is in equilibrium; cut actions equal and opposite (Newton III)')
    d[18] = k.beam_fig(8, loads=[(6, 'P')], ra='R_A = 0.25P', rb='R_B = 0.75P',
                       cut=(6, 'cut'), dims_=[(0, 6, '6 m')],
                       note='just left of load: V = 0.25P, M = 1.5P')
    d[22] = k.bending_section(b='b', h='h', c='c', M='M is largest at midspan',
                              sigma='&#963;_bending &#8733; M &#8594; check the max-moment section')
    d[31] = k.beam_fig(6, loads=[(2, '180 N')], ra='R_A = 120 N', rb='R_B = 60 N',
                       cut=(1.5, 'cut'), dims_=[(0, 1.5, '1.5 m')],
                       note='left of load: V = 120 N, M = 180 N&#183;m')
    d[32] = k.cut_segment(left_label='A', reactions=[(0.0, 'R_A = 120 N')],
                          loads=[(2.0 / 4.5, '180 N')], cut_x=0.86,
                          V='V = &#8722;60 N', M='M = 90 N&#183;m',
                          note='x = 4.5 m: V = 120 &#8722; 180 = &#8722;60 N, M = 90 N&#183;m')
    d[33] = k.cantilever_fig(2.8, tip='240 N', dims_=[(0, 1.0, 'cut at 1 m')],
                             note='free-end side (1.8 m): N = 0, V = 240 N, M = 432 N&#183;m')
    d[34] = k.resolve_fig(F='R = 30 kN', angle=53, fx='N = 18 kN', fy='V = 24 kN',
                          note='R = &#8730;(N&#178;+V&#178;) = 30 kN at 53.1&#176; to the axis')
    d[35] = k.sign_convention(note='a pure force cannot replace the removed half &#8212; you also need the couple M')
    d[39] = k.bending_section(b='b', h='h', c='c', M='N = 40 kN, M = 9 kN&#183;m',
                              sigma='&#963; = N/A misses bending Mc/I &#8212; add both')
    d[40] = k.beam_fig(10, loads=[(4, '500 N')], ra='R_A = 300 N', rb='R_B = 200 N',
                       cut=(3, 'cut'), dims_=[(0, 3, '3 m')],
                       note='cut at 3 m (left of load): N = 0, V = 300 N, M = 900 N&#183;m')
    d[41] = k.cut_segment(left_label='A', reactions=[(0.0, 'R_A = 300 N')],
                          loads=[(4.0 / 7.0, '500 N')], cut_x=0.9,
                          V='V = &#8722;200 N', M='M = 600 N&#183;m',
                          note='x = 7 m: V = 300 &#8722; 500 = &#8722;200 N, M = 600 N&#183;m')
    d[44] = k.beam_fig(6, loads=[(1.5, '160 N'), (4.5, '160 N')],
                       ra='R_A = 160 N', rb='R_B = 160 N',
                       dims_=[(1.5, 4.5, 'V = 0 here')],
                       note='M_max = 160 &#215; 1.5 = 240 N&#183;m (constant between loads)')
    return d


def inject():
    html = F.read_text()
    # add a style rule for practice-answer figures once
    if '.solution-inner svg{' not in html:
        html = html.replace(
            '.solution-inner p{ margin:8px 0; }',
            '.solution-inner p{ margin:8px 0; }\n'
            '  .solution-inner svg{ display:block; margin:12px auto; max-width:100%; '
            'height:auto; background:#fff; border:1px solid #d6deea; border-radius:6px; }',
            1)

    d = figs()
    idxs = [m.start() for m in re.finditer(r'<div class="practice-card"', html)]
    idxs.append(len(html))
    # rebuild from the back so offsets stay valid
    out = html
    for i in range(len(idxs) - 2, -1, -1):
        seg = out[idxs[i]:idxs[i + 1]]
        num = int(re.search(r'Practice (\d+)', seg).group(1))
        if num not in d:
            continue
        if '<svg' in seg:  # already has one
            continue
        anchor = '<span class="label">Solution</span>'
        pos = out.find(anchor, idxs[i], idxs[i + 1])
        if pos == -1:
            continue
        insert_at = pos + len(anchor)
        fig = '\n    ' + d[num] + '\n'
        out = out[:insert_at] + fig + out[insert_at:]
    F.write_text(out)
    added = sum(1 for n in d)
    return added


if __name__ == '__main__':
    n = inject()
    # report
    html = F.read_text()
    total_svg = html.count('<svg')
    print('figures authored:', n)
    print('total svg in file now:', total_svg)
