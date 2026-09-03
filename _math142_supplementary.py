#!/usr/bin/env python3
"""Inject source-labelled UOW MATH142 supplementary exercises into lessons."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
LESSONS = ROOT / "siddharth" / "math142"
START = "<!-- OFFICIAL_SUPPLEMENTARY_START -->"
END = "<!-- OFFICIAL_SUPPLEMENTARY_END -->"


def card(label: str, question: str, solution: str) -> str:
    return f"""
<div class="practice-card" data-card>
  <div class="p-head"><span class="p-num">{label}</span></div>
  <div class="p-body">{question}</div>
  <div class="toggle-row"><button class="toggle-btn" data-toggle>Show solution</button></div>
  <div class="solution" data-solution><div class="solution-inner">
    <span class="label">Fully worked solution</span>
    {solution}
  </div></div>
</div>"""


def official_section(groups: list[tuple[str, str, list[str]]]) -> str:
    parts = [
        START,
        '<section class="lesson-section official-supplementary" id="official-supplementary">',
        '<div class="section-title"><span class="tag">Official source</span> UOW MATH142 supplementary exercises</div>',
        '<div class="why-box"><span class="box-label">Why these are here</span>',
        "<p>These questions come from University of Wollongong MATH142 supplementary or assignment material. "
        "Their original numbering is retained so the lesson can be checked against the source. "
        "The worked solutions below show the method rather than only the final answer.</p></div>",
    ]
    for title, filename, cards in groups:
        parts.extend(
            [
                '<div class="key-box">',
                f'<span class="box-label">{title}</span>',
                f"<p><strong>Source file:</strong> <code>{filename}</code></p>",
                "</div>",
                *cards,
            ]
        )
    parts.extend(["</section>", END])
    return "\n".join(parts)


ASSIGNMENT = "math142-spring-2025-assignment-week-5-engineering-math-essentials.pdf"
ASSIGNMENT_SOLUTIONS = "w5-math142-assignment-differential-equations-solutions.pdf"
ASSIGNMENT_SOURCE = f"{ASSIGNMENT}; solutions checked against {ASSIGNMENT_SOLUTIONS}"
POLAR = "math142-polar-coordinates-supplementary-exercises.pdf"
VOLUMES = "math142-supplementary-exercises-on-integration-volumes.pdf"
SERIES = "math142-supplementary-exercises-on-series-convergence.pdf"
POWER = "math142-supplementary-exercises-on-power-series.pdf"
TAYLOR_ANSWERS = "math142-taylor-series-supplementary-exercise-answers (1).pdf"


week1 = [
    card(
        "Official Assignment Q2",
        r"""<p>Use integration by parts—and not the identity
        $1=2\sin^2x+\cos(2x)$ or a table of integrals—to find
        $$\int(\sin^2x+7)\,dx.$$</p>""",
        r"""<p>Let $I=\int\sin^2x\,dx$. Integrate by parts with
        $u=\sin x$ and $dv=\sin x\,dx$. Then $du=\cos x\,dx$ and
        $v=-\cos x$, so</p>
        <p>$$I=-\sin x\cos x+\int\cos^2x\,dx.$$</p>
        <p>Using only $\cos^2x=1-\sin^2x$,</p>
        <p>$$I=-\sin x\cos x+\int(1-\sin^2x)\,dx
        =-\sin x\cos x+x-I.$$</p>
        <p>Thus $2I=x-\sin x\cos x$ and
        $I=\tfrac{x}{2}-\tfrac12\sin x\cos x$. Therefore</p>
        <p>$$\boxed{\int(\sin^2x+7)\,dx
        =\frac{15x}{2}-\frac12\sin x\cos x+C}.$$</p>""",
    )
]


week2 = [
    card(
        "Official Assignment Q3",
        r"""<p>Compute
        $$\int_0^\infty\frac{2}{x^2+4x+8}\,dx.$$</p>""",
        r"""<p>Complete the square:
        $x^2+4x+8=(x+2)^2+4$. For a finite upper bound $B$,</p>
        <p>$$\int_0^B\frac{2\,dx}{(x+2)^2+2^2}
        =\left[\arctan\left(\frac{x+2}{2}\right)\right]_0^B.$$</p>
        <p>Taking $B\to\infty$ gives</p>
        <p>$$\frac{\pi}{2}-\arctan(1)
        =\frac{\pi}{2}-\frac{\pi}{4}
        =\boxed{\frac{\pi}{4}}.$$</p>""",
    )
]


week4 = [
    card(
        "Official Polar Q1",
        r"""<p>Plot the points
        $$(4,\tfrac\pi3),\ (2,\tfrac\pi2),\ (5,\tfrac\pi6),\
        (6,\tfrac{2\pi}3),\ (4,0),\ (0,\tfrac{11\pi}7),\
        (3,\tfrac{3\pi}2),\ (7,\tfrac{4\pi}3),\ (\tfrac\pi3,1).$$</p>""",
        r"""<p>Use $x=r\cos\theta$ and $y=r\sin\theta$. The Cartesian
        locations, which determine the plot, are respectively</p>
        <p>$$\begin{gathered}
        (2,2\sqrt3),\quad (0,2),\quad
        (\tfrac{5\sqrt3}{2},\tfrac52),\quad (-3,3\sqrt3),\\
        (4,0),\quad(0,0),\quad(0,-3),\quad
        (-\tfrac72,-\tfrac{7\sqrt3}{2}),\\
        (\tfrac\pi3\cos1,\tfrac\pi3\sin1).
        \end{gathered}$$</p>
        <p>The sixth point is the origin because $r=0$; its angle has no
        effect on its location.</p>""",
    ),
    card(
        "Official Polar Q2",
        r"""<p>Plot the points
        $$(-5,\tfrac\pi4),\ (5,-\tfrac{3\pi}4),\
        (2,-\tfrac\pi3),\ (-2,\tfrac{2\pi}3),\
        (-6,0),\ (3,-\pi),\ (-4,-\tfrac{2\pi}3),\ (-3,\pi).$$</p>""",
        r"""<p>A negative radius reverses the stated direction by $\pi$.
        Converting to Cartesian coordinates gives</p>
        <p>$$\begin{gathered}
        (-\tfrac{5\sqrt2}{2},-\tfrac{5\sqrt2}{2}),\
        (-\tfrac{5\sqrt2}{2},-\tfrac{5\sqrt2}{2}),\
        (1,-\sqrt3),\ (1,-\sqrt3),\\
        (-6,0),\ (-3,0),\ (2,2\sqrt3),\ (3,0).
        \end{gathered}$$</p>
        <p>The first two and the third and fourth pairs deliberately show
        that different polar coordinates can represent the same point.</p>""",
    ),
    card(
        "Official Polar Q3",
        r"""<p>For each point, give four other representations—two with
        positive $r$ and two with negative $r$—and find its Cartesian
        representation:</p>
        <p>(a) $(4,\pi/3)$; (b) $(-3,5\pi/4)$;
        (c) $(-5,\pi/6)$; (d) $(7,-2\pi/3)$.</p>""",
        r"""<p>Use $(r,\theta)=(r,\theta+2k\pi)=(-r,\theta+(2k+1)\pi)$.</p>
        <p><strong>(a)</strong> Positive:
        $(4,7\pi/3),(4,-5\pi/3)$; negative:
        $(-4,4\pi/3),(-4,-2\pi/3)$. Cartesian: $(2,2\sqrt3)$.</p>
        <p><strong>(b)</strong> Positive:
        $(3,\pi/4),(3,9\pi/4)$; negative:
        $(-3,-3\pi/4),(-3,13\pi/4)$. Cartesian:
        $(3\sqrt2/2,3\sqrt2/2)$.</p>
        <p><strong>(c)</strong> Positive:
        $(5,7\pi/6),(5,-5\pi/6)$; negative:
        $(-5,13\pi/6),(-5,-11\pi/6)$. Cartesian:
        $(-5\sqrt3/2,-5/2)$.</p>
        <p><strong>(d)</strong> Positive:
        $(7,4\pi/3),(7,-8\pi/3)$; negative:
        $(-7,\pi/3),(-7,-5\pi/3)$. Cartesian:
        $(-7/2,-7\sqrt3/2)$.</p>""",
    ),
    card(
        "Official Polar Q4",
        r"""<p>Find a polar representation for:</p>
        <p>(a) $(1+\sqrt2/2,\sqrt2/2)$;
        (b) $(-7\sqrt3/2,7/2)$;
        (c) $(0,-4)$; (d) $(5,-12)$.</p>""",
        r"""<p>Use $r=\sqrt{x^2+y^2}$ and choose the angle from the
        quadrant.</p>
        <p><strong>(a)</strong> $\tan\theta=\sqrt2-1=\tan(\pi/8)$ and
        $r=\sqrt{2+\sqrt2}$, so
        $(r,\theta)=(\sqrt{2+\sqrt2},\pi/8)$.</p>
        <p><strong>(b)</strong> $r=7$ and the point is in quadrant II:
        $(7,5\pi/6)$.</p>
        <p><strong>(c)</strong> $(4,3\pi/2)$ (equivalently $(4,-\pi/2)$).</p>
        <p><strong>(d)</strong> $r=13$ and
        $\theta=-\arctan(12/5)$, so
        $(13,-\arctan(12/5))$ is one representation.</p>""",
    ),
    card(
        "Official Polar Q5",
        r"""<p>Sketch each Cartesian curve and convert it to polar form:</p>
        <p>(a) $x-4y+2=0$; (b) $x=0$; (c) $y=-5$;
        (d) $x+y=0$; (e) $x^2+y^2=16$; (f) $y^2=4ax$.</p>""",
        r"""<p>Substitute $x=r\cos\theta$, $y=r\sin\theta$ and
        $x^2+y^2=r^2$.</p>
        <p><strong>(a)</strong>
        $r(\cos\theta-4\sin\theta)+2=0$, hence
        $r=\dfrac{2}{4\sin\theta-\cos\theta}$.</p>
        <p><strong>(b)</strong> $\cos\theta=0$, the $y$-axis
        (for example $\theta=\pi/2$ with signed $r$).</p>
        <p><strong>(c)</strong> $r\sin\theta=-5$.</p>
        <p><strong>(d)</strong> $\cos\theta+\sin\theta=0$, the line
        $\theta=3\pi/4$.</p>
        <p><strong>(e)</strong> $r=4$.</p>
        <p><strong>(f)</strong>
        $r^2\sin^2\theta=4ar\cos\theta$, so
        $r=\dfrac{4a\cos\theta}{\sin^2\theta}$, together with the
        vertex $r=0$.</p>""",
    ),
    card(
        "Official Polar Q6",
        r"""<p>Find the Cartesian equation corresponding to:</p>
        <p>(a) $\theta=\pi/3$; (b) $r=2$;
        (c) $r\cos\theta+6=0$; (d) $r-6\cos\theta=0$;
        (e) $r^2-8r\cos\theta-4r\sin\theta+11=0$;
        (f) $r\sin\theta-4=0$.</p>""",
        r"""<p><strong>(a)</strong> $y=\sqrt3x$.
        <strong>(b)</strong> $x^2+y^2=4$.
        <strong>(c)</strong> $x=-6$.</p>
        <p><strong>(d)</strong> $r^2=6r\cos\theta$, hence
        $x^2+y^2=6x$, or $(x-3)^2+y^2=9$.</p>
        <p><strong>(e)</strong>
        $x^2+y^2-8x-4y+11=0$, so
        $(x-4)^2+(y-2)^2=9$.</p>
        <p><strong>(f)</strong> $y=4$.</p>""",
    ),
    card(
        "Official Polar Q7",
        r"""<p>Sketch the curves:
        (a) $\theta=\pi/3$; (b) $\theta=-3\pi/4$;
        (c) $\theta=2$; (d) $r=5$.</p>""",
        r"""<p>A constant $\theta$ gives a line through the origin when
        signed radii are allowed (or a ray when $r\ge0$ is imposed).
        Thus (a), (b), and (c) are directions at $\pi/3$, $-3\pi/4$,
        and $2$ radians. The equation $r=5$ is the circle
        $x^2+y^2=25$, centred at the origin.</p>""",
    ),
    card(
        "Official Polar Q8",
        r"""<p>Sketch:
        (a) $r=-3$; (b) $\theta(\theta-1)=0$;
        (c) $\theta^2-1=0$;
        (d) $(r-2)(\theta+\pi/4)=0$.</p>""",
        r"""<p><strong>(a)</strong> As $\theta$ varies, $r=-3$ traces
        the circle $x^2+y^2=9$.</p>
        <p><strong>(b)</strong> The product is zero when $\theta=0$ or
        $\theta=1$: the union of those two radial lines/rays.</p>
        <p><strong>(c)</strong> $\theta=\pm1$: the union of two
        radial lines/rays.</p>
        <p><strong>(d)</strong> Either $r=2$ or $\theta=-\pi/4$:
        the union of the radius-$2$ circle and the stated radial line/ray.</p>""",
    ),
    card(
        "Official Polar Q9",
        r"""<p>Sketch, using Cartesian conversion:</p>
        <p>(a) $r\cos\theta=4$;
        (b) $r\sin\theta+6=0$;
        (c) $r^2\sin2\theta=0$;
        (d) $r=3\cos\theta$;
        (e) $r=6\sin\theta$.</p>""",
        r"""<p><strong>(a)</strong> $x=4$.
        <strong>(b)</strong> $y=-6$.
        <strong>(c)</strong> Since $r^2\sin2\theta=2xy$, the graph is
        $xy=0$, the union of both coordinate axes.</p>
        <p><strong>(d)</strong> $r^2=3r\cos\theta$ gives
        $(x-\tfrac32)^2+y^2=(\tfrac32)^2$.</p>
        <p><strong>(e)</strong> $r^2=6r\sin\theta$ gives
        $x^2+(y-3)^2=9$.</p>""",
    ),
]


week5 = [
    card(
        "Official Volumes Q1",
        r"""<p>Find the volume when each region is revolved about both
        the $x$-axis and the $y$-axis:</p>
        <p>(i) $x+y=2$, $x=0$, $y=0$;
        (ii) $y=\sin x$, $0\le x\le\pi$, $y=0$;
        (iii) $\sin x\le y\le1$, $0\le x\le\pi/2$;
        (iv) the first-quadrant region between $y=x^3$ and $y=x$.</p>""",
        r"""<p><strong>(i)</strong> About either axis, symmetry or direct
        integration gives
        $$V=\pi\int_0^2(2-x)^2dx=\boxed{\frac{8\pi}{3}}.$$</p>
        <p><strong>(ii)</strong> About $x$:
        $V_x=\pi\int_0^\pi\sin^2x\,dx=\boxed{\pi^2/2}$.
        About $y$:
        $$V_y=2\pi\int_0^\pi x\sin x\,dx
        =2\pi[-x\cos x+\sin x]_0^\pi=\boxed{2\pi^2}.$$</p>
        <p><strong>(iii)</strong> About $x$:
        $V_x=\pi\int_0^{\pi/2}(1-\sin^2x)dx=\boxed{\pi^2/4}$.
        About $y$:
        $$V_y=2\pi\int_0^{\pi/2}x(1-\sin x)dx
        =2\pi\left(\frac{\pi^2}{8}-1\right)
        =\boxed{\frac{\pi^3}{4}-2\pi}.$$</p>
        <p><strong>(iv)</strong> The intersections are $x=0,1$.
        About $x$:
        $V_x=\pi\int_0^1(x^2-x^6)dx=\boxed{4\pi/21}$.
        About $y$:
        $V_y=2\pi\int_0^1x(x-x^3)dx=\boxed{4\pi/15}$.</p>""",
    ),
    card(
        "Official Volumes Q2",
        r"""<p>The region bounded by $y=x^2$, $x=2$, and $y=0$ is
        revolved about (i) the $x$-axis, (ii) the $y$-axis,
        (iii) $x=2$, and (iv) $y=4$. Find each volume.</p>""",
        r"""<p>Here $0\le x\le2$ and $0\le y\le x^2$.</p>
        <p><strong>(i)</strong>
        $\pi\int_0^2x^4dx=\boxed{32\pi/5}$.</p>
        <p><strong>(ii)</strong>
        $2\pi\int_0^2x(x^2)dx=\boxed{8\pi}$.</p>
        <p><strong>(iii)</strong>
        $2\pi\int_0^2(2-x)x^2dx=\boxed{8\pi/3}$.</p>
        <p><strong>(iv)</strong> Washers have outer radius $4$ and
        inner radius $4-x^2$:
        $$\pi\int_0^2[16-(4-x^2)^2]dx
        =\boxed{\frac{224\pi}{15}}.$$</p>""",
    ),
    card(
        "Official Volumes Q3",
        r"""<p>The first-quadrant region bounded by $y=x^2$, $y=4$,
        and $x=0$ is revolved about (i) the $x$-axis,
        (ii) the $y$-axis, (iii) $x=2$, and (iv) $y=4$.
        Find each volume.</p>""",
        r"""<p>Here $0\le x\le2$ and $x^2\le y\le4$.</p>
        <p><strong>(i)</strong>
        $\pi\int_0^2(16-x^4)dx=\boxed{128\pi/5}$.</p>
        <p><strong>(ii)</strong>
        $2\pi\int_0^2x(4-x^2)dx=\boxed{8\pi}$.</p>
        <p><strong>(iii)</strong>
        $2\pi\int_0^2(2-x)(4-x^2)dx=\boxed{40\pi/3}$.</p>
        <p><strong>(iv)</strong>
        $\pi\int_0^2(4-x^2)^2dx=\boxed{256\pi/15}$.</p>""",
    ),
    card(
        "Official Volumes Q4",
        r"""<p>The region above the $x$-axis and under the ellipse
        $$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$$
        is rotated about the $x$-axis. Find the volume.</p>""",
        r"""<p>The upper ellipse has
        $y^2=b^2(1-x^2/a^2)$ for $-a\le x\le a$. The disk method gives</p>
        <p>$$V=\pi b^2\int_{-a}^{a}\left(1-\frac{x^2}{a^2}\right)dx
        =\pi b^2\left(2a-\frac{2a}{3}\right)
        =\boxed{\frac{4\pi ab^2}{3}}.$$</p>""",
    ),
    card(
        "Official Volumes Q5",
        r"""<p>The region bounded by $y=\ln x$, $x=2$, and $y=2$ is
        rotated about the $x$-axis. Find the volume.</p>""",
        r"""<p>The curve meets $y=2$ at $x=e^2$. Washers have outer
        radius $2$ and inner radius $\ln x$:</p>
        <p>$$V=\pi\int_2^{e^2}[4-(\ln x)^2]dx.$$</p>
        <p>Since
        $\int(\ln x)^2dx=x[(\ln x)^2-2\ln x+2]$,</p>
        <p>$$V=\pi\left[2e^2-4+2(\ln2)^2-4\ln2\right].$$</p>
        <p><strong>Answer:</strong>
        $\boxed{V=\pi[2e^2-4+2(\ln2)^2-4\ln2]}$.</p>""",
    ),
    card(
        "Official Volumes Q6",
        r"""<p>The region bounded by $y=1/x$, $y=\sqrt x$, and $x=4$
        is rotated about the $x$-axis. Find the volume.</p>""",
        r"""<p>The curves intersect where $x^{-1}=x^{1/2}$, so
        $x=1$. On $[1,4]$, $\sqrt x$ is the outer radius and $1/x$
        is the inner radius:</p>
        <p>$$V=\pi\int_1^4\left(x-\frac1{x^2}\right)dx
        =\pi\left[\frac{x^2}{2}+\frac1x\right]_1^4
        =\boxed{\frac{27\pi}{4}}.$$</p>""",
    ),
    card(
        "Official Volumes Q7",
        r"""<p>The first-quadrant region bounded by $y=\cos x$,
        $y=1$, and $x=\pi/2$ is revolved about $x=\pi/2$.
        Find the volume.</p>""",
        r"""<p>Use vertical shells. Their radius is $\pi/2-x$ and
        height is $1-\cos x$:</p>
        <p>$$V=2\pi\int_0^{\pi/2}(\tfrac\pi2-x)(1-\cos x)dx.$$</p>
        <p>Now
        $\int_0^{\pi/2}(\pi/2-x)dx=\pi^2/8$ and, by parts,
        $\int_0^{\pi/2}(\pi/2-x)\cos x\,dx=1$. Hence</p>
        <p>$$\boxed{V=2\pi(\pi^2/8-1)=\frac{\pi^3}{4}-2\pi}.$$</p>""",
    ),
]


week7 = [
    card(
        "Official Assignment Q5",
        r"""<p>Solve $y'=xy+9x$ (a) using separation of variables and
        (b) using the integrating-factor method. Compare the results.</p>""",
        r"""<p><strong>(a) Separation.</strong>
        $y'=x(y+9)$, so for $y\ne-9$,
        $$\frac{dy}{y+9}=x\,dx.$$
        Therefore $\ln|y+9|=x^2/2+C$ and
        $y=-9+Ce^{x^2/2}$. The equilibrium $y=-9$ is included by $C=0$.</p>
        <p><strong>(b) Integrating factor.</strong>
        Write $y'-xy=9x$. Then
        $\mu=e^{\int-x\,dx}=e^{-x^2/2}$ and</p>
        <p>$$(e^{-x^2/2}y)'=9xe^{-x^2/2}.$$</p>
        <p>Integration gives
        $e^{-x^2/2}y=-9e^{-x^2/2}+C$, hence
        $\boxed{y=-9+Ce^{x^2/2}}$.</p>
        <p>Both methods produce the same one-parameter family, as they must.</p>""",
    )
]


week9 = [
    card(
        "Official Assignment Q1(b)",
        r"""<p>Give an example of a linear differential equation with
        constant coefficients, of order at least $3$, having a solution
        that satisfies $y(0)=12$. State the solution as well.</p>""",
        r"""<p>One valid choice is
        $$y'''-y=0,\qquad y(x)=12e^x.$$</p>
        <p>The equation is linear, has constant coefficients, and is
        third order. Since $y'''=12e^x=y$, substitution gives
        $y'''-y=0$, and $y(0)=12e^0=12$. Many other examples are possible.</p>""",
    )
]


week10 = [
    card(
        "Official Assignment Q1(a)",
        r"""<p>Give an example of a function $y(x)$ such that
        $$\lim_{x\to0^-}y(x)=1,\qquad
        \lim_{x\to0^+}y(x)=-3,\qquad y(0)=17.$$</p>""",
        r"""<p>A direct piecewise example is</p>
        <p>$$y(x)=
        \begin{cases}
        1,&x&lt;0,\\
        17,&x=0,\\
        -3,&x&gt;0.
        \end{cases}$$</p>
        <p>Approaching from the left sees only the value $1$; approaching
        from the right sees only $-3$. The independently assigned value at
        the single point $x=0$ is $17$ and does not alter either limit.</p>""",
    ),
    card(
        "Official Assignment Q4",
        r"""<p>Compute
        $$\lim_{x\to0}\left(\frac1x-\frac1{\sin x}+11\right).$$</p>""",
        r"""<p>Combine the two singular fractions before taking the limit:</p>
        <p>$$\frac1x-\frac1{\sin x}
        =\frac{\sin x-x}{x\sin x}.$$</p>
        <p>This is $0/0$. Applying L'H&ocirc;pital twice gives</p>
        <p>$$\lim_{x\to0}\frac{\cos x-1}{\sin x+x\cos x}
        =\lim_{x\to0}\frac{-\sin x}{2\cos x-x\sin x}=0.$$</p>
        <p>Therefore the constant remains:
        $\boxed{11}$.</p>""",
    ),
]


week11 = [
    card(
        "Official General Series Q1",
        r"""<p>Classify each series as absolutely convergent,
        conditionally convergent, or divergent:</p>
        <p>(a) $\sum_{n=1}^\infty\dfrac{(-1)^{n+1}}{n(n+1)}$;
        (b) $\sum_{n=2}^\infty\dfrac{(-1)^n}{n\sqrt n}$;
        (c) $\sum_{n=2}^\infty\dfrac{(-1)^n}{\sqrt{n^2-1}}$;</p>
        <p>(d) $\sum_{n=1}^\infty\dfrac{(-1)^{n+1}n}{n^2+1}$;
        (e) $\dfrac1e-\dfrac{2^2}{e^2}+\dfrac{2^3}{e^3}-\cdots$;
        (f) $1-\dfrac12+\dfrac23-\dfrac34+\cdots$.</p>""",
        r"""<p><strong>(a)</strong> Absolute, since
        $\sum1/[n(n+1)]$ telescopes.
        <strong>(b)</strong> Absolute, since $\sum n^{-3/2}$ converges.</p>
        <p><strong>(c)</strong> The magnitudes decrease to $0$, so AST
        gives convergence; $\sqrt{n^2-1}\sim n$, so the absolute series
        diverges. Thus conditional.</p>
        <p><strong>(d)</strong> $n/(n^2+1)\downarrow0$, so AST applies,
        while limit comparison with $1/n$ makes the absolute series
        divergent. Thus conditional.</p>
        <p><strong>(e)</strong> Apart from its first displayed term, the
        absolute tail is geometric with ratio $2/e&lt;1$, so it converges
        absolutely.</p>
        <p><strong>(f)</strong> The term magnitudes $(n-1)/n$ tend to $1$,
        not $0$, so the series diverges by the term test.</p>""",
    ),
    card(
        "Official General Series Q2",
        r"""<p>Use the Ratio Test to determine absolute convergence or
        divergence:</p>
        <p>(a) $1-\dfrac2{2^2}+\dfrac3{2^3}-\dfrac4{2^4}+\cdots$;
        (b) $1-\dfrac1{2!}+\dfrac1{3!}-\dfrac1{4!}+\cdots$;</p>
        <p>(c) $\dfrac1{2!}-\dfrac2{3!}+\dfrac3{4!}-\dfrac4{5!}+\cdots$;
        (d) $\dfrac1e-\dfrac{2^2}{e^2}+\dfrac{2^3}{e^3}-\cdots$.</p>""",
        r"""<p>Apply the ratio test to absolute values.</p>
        <p><strong>(a)</strong> $a_n=n/2^n$ gives
        $a_{n+1}/a_n=(n+1)/(2n)\to1/2&lt;1$.</p>
        <p><strong>(b)</strong> $a_n=1/n!$ gives
        $a_{n+1}/a_n=1/(n+1)\to0$.</p>
        <p><strong>(c)</strong> $a_n=n/(n+1)!$ gives
        $a_{n+1}/a_n=(n+1)/[n(n+2)]\to0$.</p>
        <p><strong>(d)</strong> The tail has magnitude $(2/e)^n$, whose
        ratio is $2/e&lt;1$.</p>
        <p>All four series converge absolutely.</p>""",
    ),
    card(
        "Official General Series Q3",
        r"""<p>(a) State what a series is. (b) Define convergence of a
        series using partial sums. Using only those definitions, determine
        whether</p>
        <p>(c) $\sum_{k=2}^\infty\dfrac1{k^2-1}$ and
        (d) $\sum_{n=2}^\infty\ln(1-\dfrac1{n^2})$ converge.</p>""",
        r"""<p><strong>(a–b)</strong> A series is the formal sum
        $\sum a_n$. It converges to $S$ when its partial sums
        $S_N=\sum_{n=1}^N a_n$ have the finite limit $S$.</p>
        <p><strong>(c)</strong>
        $\dfrac1{k^2-1}=\tfrac12(\dfrac1{k-1}-\dfrac1{k+1})$. Hence</p>
        <p>$$S_N=\frac12\left(1+\frac12-\frac1N-\frac1{N+1}\right)
        \longrightarrow\boxed{\frac34}.$$</p>
        <p><strong>(d)</strong> Combine logarithms:</p>
        <p>$$S_N=\ln\prod_{n=2}^N\frac{(n-1)(n+1)}{n^2}
        =\ln\left(\frac{N+1}{2N}\right)
        \longrightarrow\boxed{-\ln2}.$$</p>""",
    ),
    card(
        "Official General Series Q4",
        r"""<p>For a sequence $\{u_n\}$, determine whether each statement
        is true. Prove it or give a counterexample:</p>
        <p>(a) If $u_n\to0$, then $\sum u_n$ converges.
        (b) If $\sum u_n$ converges, then $\{u_n\}$ converges.
        (c) If $\{u_n\}$ converges, then $\sum u_n$ converges.</p>""",
        r"""<p><strong>(a) False.</strong> $u_n=1/n\to0$, but the harmonic
        series diverges.</p>
        <p><strong>(b) True.</strong> If partial sums $S_n\to S$, then
        $u_n=S_n-S_{n-1}\to S-S=0$; thus $\{u_n\}$ converges.</p>
        <p><strong>(c) False.</strong> The sequence $u_n=1$ converges to
        $1$, but $\sum1$ diverges.</p>""",
    ),
    card(
        "Official General Series Q5",
        r"""<p>(a) For which real $x$ does the sequence $\{x^n\}$
        converge or diverge? (b) For which $x$ does
        $\sum_{n=1}^\infty x^{n-1}$ converge?</p>""",
        r"""<p><strong>(a)</strong> If $|x|&lt;1$, then $x^n\to0$; if
        $x=1$, it tends to $1$. At $x=-1$ it oscillates, and for
        $|x|&gt;1$ its magnitude grows. Thus the sequence converges for
        $\boxed{-1&lt;x\le1}$ and diverges otherwise.</p>
        <p><strong>(b)</strong> This is geometric with ratio $x$, so it
        converges exactly when $\boxed{|x|&lt;1}$, then sums to $1/(1-x)$.</p>""",
    ),
    card(
        "Official General Series Q6",
        r"""<p>Does $\sum_{n=1}^\infty(-1)^n\tanh n$ converge?</p>""",
        r"""<p>Since $\tanh n\to1$, the terms
        $(-1)^n\tanh n$ do not tend to zero. The term test therefore gives
        immediate divergence: $\boxed{\text{diverges}}$.</p>""",
    ),
    card(
        "Official General Series Q7",
        r"""<p>Classify the series with the following $n$th terms:</p>
        <p>(a) $\dfrac1{\ln(n+1)}$;
        (b) $\dfrac{(-1)^nn}{2(n+1)(n+2)}$;
        (c) $\dfrac{\sqrt{n+1}-\sqrt n}{\sqrt n}$;</p>
        <p>(d) $\dfrac{1+(-2)^{n-1}}{2^n}$;
        (e) $\dfrac{(-1)^nn}{1000n^2+1}$;
        (f) $\dfrac{(-1)^ne^n}{n!}$;</p>
        <p>(g) $\dfrac1{n\sqrt{n^2+1}}$;
        (h) $\dfrac{(-1)^n\ln n}{n^2}$;
        (i) $(-1)^n\dfrac{n+1}{n!}$.</p>""",
        r"""<p><strong>(a)</strong> Divergent: $\ln(n+1)\le n$, so
        $1/\ln(n+1)\ge1/n$.</p>
        <p><strong>(b)</strong> Conditional: AST applies, while the
        magnitude is asymptotic to $1/(2n)$.</p>
        <p><strong>(c)</strong> Divergent:
        rationalising gives
        $1/[\sqrt n(\sqrt{n+1}+\sqrt n)]\sim1/(2n)$.</p>
        <p><strong>(d)</strong> Divergent: its second component is
        $(-1)^{n-1}/2$, so terms do not approach $0$.</p>
        <p><strong>(e)</strong> Conditional: AST applies and the absolute
        terms are asymptotic to $1/(1000n)$.</p>
        <p><strong>(f)</strong> Absolute: the absolute ratio is
        $e/(n+1)\to0$.</p>
        <p><strong>(g)</strong> Absolute (positive): limit comparison with
        $1/n^2$ gives limit $1$.</p>
        <p><strong>(h)</strong> Absolute: eventually
        $\ln n&lt;\sqrt n$, so $\ln n/n^2&lt;1/n^{3/2}$.</p>
        <p><strong>(i)</strong> Absolute: the factorial denominator makes
        the absolute ratio tend to $0$.</p>""",
    ),
    card(
        "Official General Series Q8",
        r"""<p>Find
        $$\sum_{n=1}^\infty\frac1{(n+1)(n+2)}.$$</p>""",
        r"""<p>Use
        $\dfrac1{(n+1)(n+2)}=\dfrac1{n+1}-\dfrac1{n+2}$. Then</p>
        <p>$$S_N=\frac12-\frac1{N+2}\longrightarrow
        \boxed{\frac12}.$$</p>""",
    ),
    card(
        "Official General Series Q9",
        r"""<p>Using Q7(a) and the Alternating Series Test, classify
        $$\sum_{n=1}^\infty\frac{(-1)^n}{\ln(n+1)}.$$</p>""",
        r"""<p>The magnitudes $1/\ln(n+1)$ decrease to $0$, so the
        Alternating Series Test gives convergence. Q7(a) shows that the
        corresponding positive series diverges. Therefore the series is
        $\boxed{\text{conditionally convergent}}$.</p>""",
    ),
]


week12_power = [
    card(
        "Official Power Series Q1",
        r"""<p>Determine all real $x$ for which each power series converges:</p>
        <p>(a) $\sum_{n=1}^\infty\dfrac{(-1)^{n+1}x^n}{n(n+1)}$;
        (b) $1+x+\dfrac{x^2}{2!}+\cdots$;
        (c) $x-\dfrac{x^3}{3!}+\dfrac{x^5}{5!}-\cdots$;
        (d) $1-\dfrac{x^2}{2!}+\dfrac{x^4}{4!}-\cdots$;</p>
        <p>(e) $\sum_{n=1}^\infty n^2x^n$;
        (f) $1+\sum_{n=1}^\infty\dfrac{(-1)^nx^n}{n(n+2)}$;
        (g) $\sum_{n=1}^\infty\dfrac{(-1)^n(x-1)^n}{n}$;</p>
        <p>(h) $\sum_{n=1}^\infty\dfrac{(x-3)^n}{n\,n!}$;
        (i) $\sum_{n=1}^\infty\dfrac{(-1)^{n+1}(x+2)^n}{n}$.</p>""",
        r"""<p><strong>(a)</strong> Radius $1$. At $x=\pm1$ the absolute
        series is bounded by $\sum1/n^2$, so $\boxed{[-1,1]}$.</p>
        <p><strong>(b–d)</strong> These are $e^x$, $\sin x$, and $\cos x$;
        factorial denominators give convergence for
        $\boxed{(-\infty,\infty)}$.</p>
        <p><strong>(e)</strong> Radius $1$; at $x=\pm1$ terms do not tend
        to zero, so $\boxed{(-1,1)}$.</p>
        <p><strong>(f)</strong> Radius $1$ and both endpoints converge
        absolutely like $\sum1/n^2$, so $\boxed{[-1,1]}$.</p>
        <p><strong>(g)</strong> Let $z=x-1$. The radius is $1$.
        At $z=1$ the alternating harmonic series converges; at $z=-1$
        the harmonic series results. Thus $\boxed{(0,2]}$.</p>
        <p><strong>(h)</strong> The ratio contains a factor $1/(n+1)$,
        so it converges for every $x$: $\boxed{(-\infty,\infty)}$.</p>
        <p><strong>(i)</strong> Let $z=x+2$. At $z=1$ the alternating
        harmonic series converges; at $z=-1$ it diverges. Hence
        $\boxed{(-3,-1]}$.</p>""",
    )
]


week12_taylor = [
    card(
        "Taylor answers Q1 (reconstructed)",
        r"""<p>The supplied answer key unambiguously identifies these
        prompts. Find: (a) the degree-$4$ Taylor polynomial for $e^x$
        about $a=1$; (b) the degree-$3$ Taylor polynomial for $\cos x$
        about $a=\pi/4$; (c) the degree-$4$ Taylor polynomial for
        $\sqrt x$ about $a=9$; (d) the degree-$3$ Taylor polynomial for
        $\arctan x$ about $a=1$.</p>""",
        r"""<p>Apply
        $p_n(x)=\sum_{k=0}^nf^{(k)}(a)(x-a)^k/k!$.</p>
        <p><strong>(a)</strong>
        $e[1+(x-1)+(x-1)^2/2+(x-1)^3/6+(x-1)^4/24]$.</p>
        <p><strong>(b)</strong>
        $\dfrac1{\sqrt2}[1-(x-\pi/4)-\tfrac12(x-\pi/4)^2
        +\tfrac16(x-\pi/4)^3]$.</p>
        <p><strong>(c)</strong> With $h=x-9$,
        $$3+\frac h6-\frac{h^2}{216}+\frac{h^3}{3888}
        -\frac{5h^4}{279936}.$$</p>
        <p><strong>(d)</strong> Derivatives at $1$ are
        $1/2,-1/2,1/2$, so
        $$\frac\pi4+\frac{x-1}{2}-\frac{(x-1)^2}{4}
        +\frac{(x-1)^3}{12}.$$</p>""",
    ),
    card(
        "Taylor answers Q5 (reconstructed)",
        r"""<p>Find the degree-$1$ and degree-$4$ Taylor polynomials for
        $\ln x$ centred at $a=1$.</p>""",
        r"""<p>Write $h=x-1$. Since $\ln x=\ln(1+h)$,</p>
        <p>$$\ln(1+h)=h-\frac{h^2}{2}+\frac{h^3}{3}
        -\frac{h^4}{4}+\cdots.$$</p>
        <p>Thus $\boxed{p_1=x-1}$ and
        $$\boxed{p_4=(x-1)-\frac{(x-1)^2}{2}
        +\frac{(x-1)^3}{3}-\frac{(x-1)^4}{4}}.$$</p>""",
    ),
    card(
        "Taylor answers Q6 (reconstructed)",
        r"""<p>Write the Maclaurin series for
        (a) $1/(1-x)$, (b) $e^x$, (c) $\sin x$, (d) $\cos x$,
        (e) $\sinh x$, and (f) $\cosh x$.</p>""",
        r"""<p>From the geometric and exponential series,</p>
        <p>$$\frac1{1-x}=\sum_{n=0}^\infty x^n\quad(|x|&lt;1),\qquad
        e^x=\sum_{n=0}^\infty\frac{x^n}{n!}.$$</p>
        <p>Separating odd/even and alternating/non-alternating terms gives</p>
        <p>$$\sin x=\sum_{n=0}^\infty\frac{(-1)^nx^{2n+1}}{(2n+1)!},
        \quad
        \cos x=\sum_{n=0}^\infty\frac{(-1)^nx^{2n}}{(2n)!},$$</p>
        <p>$$\sinh x=\sum_{n=0}^\infty\frac{x^{2n+1}}{(2n+1)!},
        \quad
        \cosh x=\sum_{n=0}^\infty\frac{x^{2n}}{(2n)!}.$$</p>""",
    ),
    card(
        "Taylor answers Q7 (reconstructed)",
        r"""<p>Derive the Maclaurin series for $\ln(1+x)$ by finding its
        derivatives at $x=0$.</p>""",
        r"""<p>For $n\ge1$,
        $$\frac{d^n}{dx^n}\ln(1+x)
        =(-1)^{n+1}(n-1)!(1+x)^{-n}.$$</p>
        <p>At $x=0$, division by $n!$ gives
        $(-1)^{n+1}/n$. Therefore</p>
        <p>$$\boxed{\ln(1+x)=\sum_{n=1}^\infty
        \frac{(-1)^{n+1}x^n}{n}
        =x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots}$$
        for $-1&lt;x\le1$.</p>""",
    ),
    card(
        "Taylor answers Q8 (reconstructed)",
        r"""<p>Write Taylor series for (a) $e^x$ about $a=1$;
        (b) $\sin x$ about $a=\pi/6$;
        (c) $\cos x$ about $a=\pi/3$;
        (d) $\ln x$ about $a=1$.</p>""",
        r"""<p><strong>(a)</strong>
        $e^x=e\sum_{n=0}^\infty(x-1)^n/n!$.</p>
        <p><strong>(b)</strong> With $h=x-\pi/6$,
        $$\sin x=\frac12+\frac{\sqrt3}{2}h-\frac{h^2}{2\cdot2!}
        -\frac{\sqrt3\,h^3}{2\cdot3!}+\cdots.$$</p>
        <p><strong>(c)</strong> With $h=x-\pi/3$,
        $$\cos x=\frac12-\frac{\sqrt3}{2}h-\frac{h^2}{2\cdot2!}
        +\frac{\sqrt3\,h^3}{2\cdot3!}+\cdots.$$</p>
        <p><strong>(d)</strong>
        $\ln x=\sum_{n=1}^\infty(-1)^{n+1}(x-1)^n/n$ for $0&lt;x\le2$.</p>""",
    ),
    card(
        "Taylor answers Q12 (reconstructed)",
        r"""<p>Find a series representation of $1/(1-x)$ valid for
        $|x|&gt;1$.</p>""",
        r"""<p>Factor out $-x$ and set $u=1/x$, for which $|u|&lt;1$:</p>
        <p>$$\frac1{1-x}=-\frac1x\frac1{1-1/x}
        =-\frac1x\sum_{n=0}^\infty\frac1{x^n}
        =\boxed{-\sum_{n=1}^\infty\frac1{x^n}}.$$</p>""",
    ),
    card(
        "Taylor answers Q14 (reconstructed)",
        r"""<p>Find the Maclaurin expansion of $\tan x$ through the
        $x^7$ term.</p>""",
        r"""<p>Let
        $\tan x=a_1x+a_3x^3+a_5x^5+a_7x^7+\cdots$ and use
        $(\tan x)'=1+\tan^2x$. Matching coefficients successively gives
        $a_1=1$, $3a_3=1$, $5a_5=2/3$, and
        $7a_7=17/45$. Hence</p>
        <p>$$\boxed{\tan x=x+\frac{x^3}{3}+\frac{2x^5}{15}
        +\frac{17x^7}{315}+O(x^9)}.$$</p>""",
    ),
]


PAGES: dict[str, list[tuple[str, str, list[str]]]] = {
    "MATH142_Week1_Integration_Techniques.html": [
        ("Spring 2025 Assignment, Week 5", ASSIGNMENT_SOURCE, week1)
    ],
    "MATH142_Week2_PartialFractions_ImproperIntegrals.html": [
        ("Spring 2025 Assignment, Week 5", ASSIGNMENT_SOURCE, week2)
    ],
    "MATH142_Week4_PolarCoordinates.html": [
        ("Strand 1 — Polar Coordinates", POLAR, week4)
    ],
    "MATH142_Week5_Areas_Volumes.html": [
        ("Strand 1 — Applications of Integration: Volumes", VOLUMES, week5)
    ],
    "MATH142_Week7_SeparableDE_IntegratingFactor.html": [
        ("Spring 2025 Assignment, Week 5", ASSIGNMENT_SOURCE, week7)
    ],
    "MATH142_Week9_SecondOrderDE_SHM.html": [
        ("Spring 2025 Assignment, Week 5", ASSIGNMENT_SOURCE, week9)
    ],
    "MATH142_Week10_Limits_LHopital.html": [
        ("Spring 2025 Assignment, Week 5", ASSIGNMENT_SOURCE, week10)
    ],
    "MATH142_Week11_Sequences_Series_ConvergenceTests.html": [
        ("Strand 2 — General Series", SERIES, week11)
    ],
    "MATH142_Week12_TaylorSeries.html": [
        ("Strand 2 — Power Series", POWER, week12_power),
        (
            "Taylor and Maclaurin Series — reconstructed prompts",
            TAYLOR_ANSWERS,
            week12_taylor,
        ),
    ],
}


def inject(path: Path, groups: list[tuple[str, str, list[str]]]) -> None:
    text = path.read_text(encoding="utf-8")
    block = official_section(groups)
    if START in text:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
        text, replacements = pattern.subn(lambda _: block, text, count=1)
        if replacements != 1:
            raise RuntimeError(f"Could not replace official block in {path}")
    else:
        if "</main>" not in text:
            raise RuntimeError(f"No </main> insertion point in {path}")
        text = text.replace("</main>", block + "\n\n</main>", 1)

    total = len(re.findall(r'<div class="practice-card" data-card>', text))
    text, replacements = re.subn(
        r'(<div class="progress-label" id="progressLabel">0 / )\d+( practice solutions revealed</div>)',
        rf"\g<1>{total}\2",
        text,
        count=1,
    )
    if replacements != 1:
        raise RuntimeError(f"Could not update practice count in {path}")
    path.write_text(text, encoding="utf-8")
    print(f"{path.name}: {total} practice cards")


def main() -> None:
    for filename, groups in PAGES.items():
        inject(LESSONS / filename, groups)


if __name__ == "__main__":
    main()
