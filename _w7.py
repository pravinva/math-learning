"""Week 7 (friction): level FBD, incline FBD, wedge or belt/capstan per practice answer."""
import re
import _dpen102_kit as k
import _wk_util as u


def build(num, q, a):
    ql = q.lower()
    cap = u.caption(a)

    # belt / capstan
    if any(w in ql for w in ('belt', 'wrap', 'capstan', 'drum')) or 'T_2' in q or 'T_1' in q:
        t1 = u.first(r'T_1\s*=?\s*(\d+(?:\.\d+)?)', q) or u.first(r'T_1\s*=?\s*(\d+(?:\.\d+)?)', a)
        t2 = u.first(r'T_2\s*=?\s*(\d+(?:\.\d+)?)', q) or u.first(r'T_2\s*=?\s*(\d+(?:\.\d+)?)', a)
        beta = u.beta_deg(q)
        wrap = max(60, min(330, beta))
        return k.belt_pulley(
            T1='T_1 = %s N' % u.g(t1) if t1 is not None else 'T_1',
            T2='T_2 = %s N' % u.g(t2) if t2 is not None else 'T_2',
            beta='&#946; = %s&#176;' % u.g(beta), wrap=wrap, note=cap)

    # wedge
    if 'wedge' in ql:
        th = u.angle_deg(q, 12.0)
        return k.fbd_incline(theta=th, labels={'W': 'W', 'f': 'f'},
                             mu='wedge drive P', moving=cap)

    # incline block
    if any(w in ql for w in ('incline', 'slope', 'ramp', 'repose')) or '&deg;' in q:
        th = u.angle_deg(q, 20.0)
        return k.fbd_incline(theta=th, moving=cap)

    # level floor block
    F = u.first(r'(\d+(?:\.\d+)?)\s*N\b', q)
    push = ('applied %s N' % u.g(F)) if F is not None else 'applied F'
    return k.fbd_level(mass='m', push=push, friction='f', caption=cap)


if __name__ == '__main__':
    fn = 'Lesson_Week7_Friction_Systems.html'
    n = u.inject(fn, build)
    miss, bad = u.validate(fn)
    print('week7 added', n, 'missing', miss, 'malformed', bad)
