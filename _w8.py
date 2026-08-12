"""Week 8 (centroids / second moment of area): a matching section diagram per answer."""
import re
import _dpen102_kit as k
import _wk_util as u


def build(num, q, a):
    ql = q.lower()
    cap = u.caption(a)

    # rectangle with a hole -> centroid of a composite with a void
    if 'hole' in ql or 'void' in ql or 'washer' in ql or 'tube' in ql:
        return k.rect_hole_centroid(centroid='C', note=cap)

    # parallel-axis transfer
    if ('parallel' in ql or 'transfer' in ql or re.search(r'\bd\s*=', q)
            or 'Ad^2' in q or 'own I' in ql):
        return k.parallel_axis(note=cap)

    # plain rectangle second moment I = b h^3 / 12
    if re.search(r'b\s*=\s*\d', q) and re.search(r'h\s*=\s*\d', q):
        b = u.first(r'b\s*=\s*(\d+(?:\.\d+)?)', q)
        h = u.first(r'h\s*=\s*(\d+(?:\.\d+)?)', q)
        return k.area_section(b='b = %s mm' % u.g(b), h='h = %s mm' % u.g(h),
                              axis='centroidal axis', note=cap, shape='rect')

    # T / I / channel built-up sections
    if any(w in ql for w in ('t-section', 't-shape', 'i-beam', 'i-like', 'channel', 'flange', 'web')):
        return k.area_section(b='flange', h='depth', axis='centroidal axis',
                              note=cap, shape='ibeam')

    # default: composite centroid of two rectangles
    parts = [(120, 70, 120, 60, 'A_1'), (250, 96, 96, 96, 'A_2')]
    return k.composite_shape(parts, note=cap)


if __name__ == '__main__':
    fn = 'Lesson_Week8_Centroids_Inertia.html'
    n = u.inject(fn, build)
    miss, bad = u.validate(fn)
    print('week8 added', n, 'missing', miss, 'malformed', bad)
