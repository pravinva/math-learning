"""Week 9 (work / energy): drop, spring-launch, incline-slide or level work-energy per answer."""
import _dpen102_kit as k
import _wk_util as u


def build(num, q, a):
    ql = q.lower()
    cap = u.caption(a)

    if 'spring' in ql:
        return k.energy_track('spring', labels={'v': 'v = ?'}, note=cap)

    if any(w in ql for w in ('incline', 'ramp', 'slope')):
        th = u.angle_deg(q, 20.0)
        return k.energy_track('incline', labels={'theta': th}, note=cap)

    if any(w in ql for w in ('drop', 'dropped', 'falls', 'fall', 'lowered', 'thrown upward', 'height')):
        return k.energy_track('drop', note=cap)

    return k.push_slide(note=cap)


if __name__ == '__main__':
    fn = 'Lesson_Week9_Work_Energy.html'
    n = u.inject(fn, build)
    miss, bad = u.validate(fn)
    print('week9 added', n, 'missing', miss, 'malformed', bad)
