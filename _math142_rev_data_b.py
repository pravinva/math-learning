# -*- coding: utf-8 -*-
"""MATH142 revision pack data — Set B (topic T10 + quarters, mids, fulls)."""

PACKS = {
    # ------------------------------------------------------------------ T10
    "t10-limits-series-taylor": {
        "id": "T10",
        "kind": "topic",
        "title": "Limits, Series & Taylor (W10–12)",
        "weeks": "W10–12",
        "blurb": "Mixed practice on L'Hôpital, sequence limits, series tests, power-series radius, and Taylor/Maclaurin approximations.",
        "questions": [
            {
                "q": r"""<p>Evaluate \(\displaystyle\lim_{x\to 0}\frac{e^{2x}-1-2x}{x^2}\).</p>""",
                "a": r"""<p>As \(x\to 0\) the form is \(\frac{0}{0}\). Apply L'Hôpital:</p>
\[
\lim_{x\to 0}\frac{2e^{2x}-2}{2x}=\lim_{x\to 0}\frac{e^{2x}-1}{x},
\]
still \(\frac{0}{0}\). Differentiate again:</p>
\[
\lim_{x\to 0}\frac{2e^{2x}}{1}=2.
\]
\[\boxed{2}\]""",
            },
            {
                "q": r"""<p>Evaluate \(\displaystyle\lim_{x\to\infty}\frac{\ln(1+3x)}{\sqrt{x}}\).</p>""",
                "a": r"""<p>As \(x\to\infty\) the form is \(\frac{\infty}{\infty}\). L'Hôpital gives</p>
\[
\lim_{x\to\infty}\frac{\frac{3}{1+3x}}{\frac{1}{2\sqrt{x}}}=\lim_{x\to\infty}\frac{3\cdot 2\sqrt{x}}{1+3x}=\lim_{x\to\infty}\frac{6\sqrt{x}}{3x+1}=0,
\]
since the denominator grows like \(3x\).</p>
\[\boxed{0}\]""",
            },
            {
                "q": r"""<p>Determine \(\displaystyle\lim_{n\to\infty} a_n\) where \(a_n=\dfrac{n^2+5n}{3n^2-n+2}\).</p>""",
                "a": r"""<p>Divide numerator and denominator by \(n^2\):</p>
\[
a_n=\frac{1+5/n}{3-1/n+2/n^2}\to\frac{1+0}{3-0+0}=\frac{1}{3}.
\]
\[\boxed{1/3}\]""",
            },
            {
                "q": r"""<p>Does \(\displaystyle\sum_{n=0}^{\infty}\Bigl(\frac{2}{5}\Bigr)^n\) converge? If so, find its sum.</p>""",
                "a": r"""<p>Geometric series with first term \(a=1\) and ratio \(r=2/5\). Since \(|r|&lt;1\),</p>
\[
S=\frac{a}{1-r}=\frac{1}{1-2/5}=\frac{1}{3/5}=\frac{5}{3}.
\]
\[\boxed{5/3}\]""",
            },
            {
                "q": r"""<p>Classify the convergence of \(\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^{4/3}}\) and \(\displaystyle\sum_{n=1}^{\infty}\frac{1}{\sqrt{n}}\).</p>""",
                "a": r"""<p>Both are \(p\)-series \(\sum n^{-p}\).</p>
<ul>
<li>\(p=4/3&gt;1\) \(\Rightarrow\) \(\sum n^{-4/3}\) converges.</li>
<li>\(p=1/2\le 1\) \(\Rightarrow\) \(\sum n^{-1/2}\) diverges.</li>
</ul>
\[\boxed{\sum n^{-4/3}\ \text{converges};\ \sum n^{-1/2}\ \text{diverges}}\]""",
            },
            {
                "q": r"""<p>Use the ratio test to decide whether \(\displaystyle\sum_{n=1}^{\infty}\frac{n!}{3^n}\) converges or diverges.</p>""",
                "a": r"""<p>Compute</p>
\[
L=\lim_{n\to\infty}\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\lim_{n\to\infty}\frac{(n+1)!/3^{n+1}}{n!/3^n}=\lim_{n\to\infty}\frac{n+1}{3}=\infty.
\]
Since \(L&gt;1\), the series diverges.</p>
\[\boxed{\text{diverges (ratio test, }L=\infty)}\]""",
            },
            {
                "q": r"""<p>Apply the root test to \(\displaystyle\sum_{n=1}^{\infty}\Bigl(\frac{2n+1}{5n}\Bigr)^n\).</p>""",
                "a": r"""<p>\(\displaystyle L=\lim_{n\to\infty}\sqrt[n]{|a_n|}=\lim_{n\to\infty}\frac{2n+1}{5n}=\frac{2}{5}&lt;1\), so the series converges absolutely.</p>
\[\boxed{\text{converges (root test, }L=2/5)}\]""",
            },
            {
                "q": r"""<p>Show that \(\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n+2}\) converges conditionally. Does the alternating series test apply?</p>""",
                "a": r"""<p>Let \(b_n=1/(n+2)\). Then \(b_n&gt;0\), decreasing, and \(b_n\to 0\), so AST gives (conditional) convergence of the alternating series.</p>
<p>The absolute series \(\sum 1/(n+2)\) is a shifted harmonic series, hence diverges. Therefore convergence is conditional, not absolute.</p>
\[\boxed{\text{AST applies; converges conditionally}}\]""",
            },
            {
                "q": r"""<p>Find the radius of convergence of \(\displaystyle\sum_{n=0}^{\infty}\frac{(x-1)^n}{4^n(n+1)}\).</p>""",
                "a": r"""<p>Ratio test:</p>
\[
L=\lim_{n\to\infty}\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\lim_{n\to\infty}\frac{|x-1|}{4}\cdot\frac{n+1}{n+2}=\frac{|x-1|}{4}.
\]
Need \(L&lt;1\), i.e. \(|x-1|&lt;4\). Radius \(R=4\).</p>
\[\boxed{R=4}\]""",
            },
            {
                "q": r"""<p>(a) Write the Maclaurin series for \(e^x\), \(\sin x\), and \(\dfrac{1}{1-x}\) (state the interval for the geometric one).<br>
(b) Use the degree-3 Maclaurin polynomial for \(e^{-x^2}\) to approximate \(\displaystyle\int_0^{0.2}e^{-x^2}\,dx\).</p>""",
                "a": r"""<p>(a) Standard expansions:</p>
\[
e^x=\sum_{n=0}^{\infty}\frac{x^n}{n!},\quad
\sin x=\sum_{n=0}^{\infty}\frac{(-1)^n x^{2n+1}}{(2n+1)!},\quad
\frac{1}{1-x}=\sum_{n=0}^{\infty}x^n\ (|x|&lt;1).
\]
<p>(b) \(e^u=\sum u^n/n!\) with \(u=-x^2\):</p>
\[
e^{-x^2}=1-x^2+\frac{x^4}{2}-\cdots.
\]
Up to degree 3 in \(x\), keep \(1-x^2\) (the \(x^4\) term has degree 4). Then</p>
\[
\int_0^{0.2}(1-x^2)\,dx=\Bigl[x-\frac{x^3}{3}\Bigr]_0^{0.2}=0.2-\frac{0.008}{3}=0.2-\frac{2}{750}=\frac{148}{750}=\frac{74}{375}\approx 0.1973.
\]
\[\boxed{(a)\ e^x,\sin x,\ 1/(1-x)\text{ as above};\ (b)\ 74/375\ \approx 0.1973}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ Q1
    "q1-weeks1-3": {
        "id": "Q1",
        "kind": "quarter",
        "title": "Quarter 1 (W1–3)",
        "weeks": "W1–3",
        "blurb": "Mixed integration techniques, partial fractions, improper integrals, and Trapezoidal/Simpson numerical methods.",
        "questions": [
            {
                "q": r"""<p>Evaluate \(\displaystyle\int\frac{x}{\sqrt{4+x^2}}\,dx\).</p>""",
                "a": r"""<p>Substitute \(u=4+x^2\), \(du=2x\,dx\):</p>
\[
\int\frac{x}{\sqrt{4+x^2}}\,dx=\frac12\int u^{-1/2}\,du=\sqrt{u}+C=\sqrt{4+x^2}+C.
\]
\[\boxed{\sqrt{4+x^2}+C}\]""",
            },
            {
                "q": r"""<p>Compute \(\displaystyle\int x\cos(3x)\,dx\) using integration by parts.</p>""",
                "a": r"""<p>Let \(u=x\), \(dv=\cos(3x)\,dx\), so \(du=dx\), \(v=\frac13\sin(3x)\).</p>
\[
\int x\cos(3x)\,dx=\frac{x}{3}\sin(3x)-\frac13\int\sin(3x)\,dx=\frac{x}{3}\sin(3x)+\frac{1}{9}\cos(3x)+C.
\]
\[\boxed{\dfrac{x}{3}\sin(3x)+\dfrac{1}{9}\cos(3x)+C}\]""",
            },
            {
                "q": r"""<p>Evaluate \(\displaystyle\int\sin^3 x\cos^2 x\,dx\).</p>""",
                "a": r"""<p>Write \(\sin^3 x=\sin x(1-\cos^2 x)\):</p>
\[
\int\sin^3 x\cos^2 x\,dx=\int\sin x(1-\cos^2 x)\cos^2 x\,dx.
\]
Let \(u=\cos x\), \(du=-\sin x\,dx\):</p>
\[
-\int(1-u^2)u^2\,du=-\int(u^2-u^4)\,du=-\frac{u^3}{3}+\frac{u^5}{5}+C=-\frac{\cos^3 x}{3}+\frac{\cos^5 x}{5}+C.
\]
\[\boxed{-\dfrac{\cos^3 x}{3}+\dfrac{\cos^5 x}{5}+C}\]""",
            },
            {
                "q": r"""<p>Use a trigonometric substitution to find \(\displaystyle\int\frac{1}{x^2\sqrt{x^2-9}}\,dx\) for \(x&gt;3\).</p>""",
                "a": r"""<p>Let \(x=3\sec\theta\), \(dx=3\sec\theta\tan\theta\,d\theta\), \(\sqrt{x^2-9}=3\tan\theta\).</p>
\[
\int\frac{3\sec\theta\tan\theta}{9\sec^2\theta\cdot 3\tan\theta}\,d\theta=\frac19\int\cos\theta\,d\theta=\frac19\sin\theta+C.
\]
Since \(\sin\theta=\sqrt{x^2-9}/x\),</p>
\[
\frac{\sqrt{x^2-9}}{9x}+C.
\]
\[\boxed{\dfrac{\sqrt{x^2-9}}{9x}+C}\]""",
            },
            {
                "q": r"""<p>Decompose and integrate \(\displaystyle\int\frac{5x+1}{(x-1)(x+2)}\,dx\).</p>""",
                "a": r"""<p>Write \(\dfrac{5x+1}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}\).</p>
\[
A(x+2)+B(x-1)=5x+1\implies A=2,\ B=3.
\]
\[
\int\Bigl(\frac{2}{x-1}+\frac{3}{x+2}\Bigr)\,dx=2\ln|x-1|+3\ln|x+2|+C.
\]
\[\boxed{2\ln|x-1|+3\ln|x+2|+C}\]""",
            },
            {
                "q": r"""<p>Evaluate the improper integral \(\displaystyle\int_1^{\infty}\frac{1}{(2x+1)^2}\,dx\), or show it diverges.</p>""",
                "a": r"""<p>\(\displaystyle\int_1^{\infty}\frac{1}{(2x+1)^2}\,dx=\lim_{b\to\infty}\int_1^b(2x+1)^{-2}\,dx\).</p>
\[
\int(2x+1)^{-2}\,dx=-\frac{1}{2(2x+1)},
\]
so</p>
\[
\lim_{b\to\infty}\Bigl[-\frac{1}{2(2x+1)}\Bigr]_1^b=\lim_{b\to\infty}\Bigl(-\frac{1}{2(2b+1)}+\frac{1}{6}\Bigr)=\frac16.
\]
\[\boxed{1/6}\]""",
            },
            {
                "q": r"""<p>Does \(\displaystyle\int_0^1\frac{1}{\sqrt{x}(1+x)}\,dx\) converge? Justify briefly and evaluate if possible.</p>""",
                "a": r"""<p>Near \(x=0\), \(\frac{1}{\sqrt{x}(1+x)}\sim x^{-1/2}\), and \(\int_0^1 x^{-1/2}\,dx\) converges, so the integral converges.</p>
<p>Substitute \(u=\sqrt{x}\), \(x=u^2\), \(dx=2u\,du\):</p>
\[
\int_0^1\frac{2u\,du}{u(1+u^2)}=2\int_0^1\frac{du}{1+u^2}=2\arctan u\Big|_0^1=2\cdot\frac{\pi}{4}=\frac{\pi}{2}.
\]
\[\boxed{\pi/2}\]""",
            },
            {
                "q": r"""<p>Approximate \(\displaystyle\int_0^2 e^{-x}\,dx\) using the Trapezoidal rule with \(n=4\). Leave the answer in exact exponential form, then give 4 d.p.</p>""",
                "a": r"""<p>\(h=(2-0)/4=1/2\). Nodes \(x=0,0.5,1,1.5,2\).</p>
\[
T=\frac{h}{2}\bigl(y_0+2y_1+2y_2+2y_3+y_4\bigr)=\frac14\bigl(1+2e^{-0.5}+2e^{-1}+2e^{-1.5}+e^{-2}\bigr).
\]
Numerically \(T\approx 0.8950\) (4 d.p.).</p>
\[\boxed{\tfrac14\bigl(1+2e^{-1/2}+2e^{-1}+2e^{-3/2}+e^{-2}\bigr)\approx 0.8950}\]""",
            },
            {
                "q": r"""<p>Use Simpson's rule with \(n=4\) to approximate \(\displaystyle\int_0^{\pi}\sin x\,dx\). Compare with the exact value \(2\).</p>""",
                "a": r"""<p>\(h=\pi/4\). Values: \(y_0=0\), \(y_1=\sin(\pi/4)=\sqrt{2}/2\), \(y_2=1\), \(y_3=\sqrt{2}/2\), \(y_4=0\).</p>
\[
S=\frac{h}{3}\bigl(y_0+4y_1+2y_2+4y_3+y_4\bigr)=\frac{\pi}{12}\bigl(0+4\cdot\tfrac{\sqrt{2}}{2}+2+4\cdot\tfrac{\sqrt{2}}{2}+0\bigr)=\frac{\pi}{12}(2+4\sqrt{2}).
\]
\(\approx 2.0046\), close to exact \(2\).</p>
\[\boxed{\dfrac{\pi}{12}(2+4\sqrt{2})\approx 2.0046}\]""",
            },
            {
                "q": r"""<p>Evaluate \(\displaystyle\int\frac{x^2+3x+3}{(x+1)(x^2+1)}\,dx\).</p>""",
                "a": r"""<p>Partial fractions: \(\dfrac{x^2+3x+3}{(x+1)(x^2+1)}=\dfrac{A}{x+1}+\dfrac{Bx+C}{x^2+1}\).</p>
\[
A(x^2+1)+(Bx+C)(x+1)=x^2+3x+3.
\]
Setting \(x=-1\): \(A(2)=1-3+3\Rightarrow A=1/2\). Expanding and matching coefficients yields \(B=1/2\), \(C=5/2\).</p>
\[
\int\Bigl(\frac{1/2}{x+1}+\frac{(1/2)x+5/2}{x^2+1}\Bigr)\,dx=\frac12\ln|x+1|+\frac14\ln(x^2+1)+\frac52\arctan x+C.
\]
\[\boxed{\dfrac12\ln|x+1|+\dfrac14\ln(x^2+1)+\dfrac52\arctan x+C}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ Q2
    "q2-weeks4-6": {
        "id": "Q2",
        "kind": "quarter",
        "title": "Quarter 2 (W4–6)",
        "weeks": "W4–6",
        "blurb": "Mixed polar and parametric calculus, areas and volumes of revolution, and arc length.",
        "questions": [
            {
                "q": r"""<p>Convert the polar equation \(r=4\cos\theta\) to Cartesian form and identify the curve.</p>""",
                "a": r"""<p>Multiply by \(r\): \(r^2=4r\cos\theta\Rightarrow x^2+y^2=4x\).</p>
\[
(x-2)^2+y^2=4,
\]
a circle centre \((2,0)\) radius \(2\).</p>
\[\boxed{(x-2)^2+y^2=4}\]""",
            },
            {
                "q": r"""<p>Find the area enclosed by one loop of \(r=3\sin(2\theta)\).</p>""",
                "a": r"""<p>One loop occurs for \(0\le\theta\le\pi/2\).</p>
\[
A=\frac12\int_0^{\pi/2}9\sin^2(2\theta)\,d\theta=\frac94\int_0^{\pi/2}\frac{1-\cos(4\theta)}{2}\,d\theta=\frac98\Bigl[\theta-\frac14\sin(4\theta)\Bigr]_0^{\pi/2}=\frac{9\pi}{16}.
\]
\[\boxed{9\pi/16}\]""",
            },
            {
                "q": r"""<p>For \(x=t^2-1\), \(y=t^3-3t\), find \(\dfrac{dy}{dx}\) and the points where the tangent is horizontal.</p>""",
                "a": r"""<p>\(\dfrac{dx}{dt}=2t\), \(\dfrac{dy}{dt}=3t^2-3\), so</p>
\[
\frac{dy}{dx}=\frac{3(t^2-1)}{2t}\quad(t\neq 0).
\]
Horizontal tangent when \(dy/dt=0\) and \(dx/dt\neq 0\): \(t=\pm 1\).</p>
\[
(t=1):\ (0,-2);\quad(t=-1):\ (0,2).
\]
\[\boxed{\dfrac{dy}{dx}=\dfrac{3(t^2-1)}{2t};\ \text{pts }(0,-2),\ (0,2)}\]""",
            },
            {
                "q": r"""<p>Find the area under \(y=\sqrt{x}\) from \(x=0\) to \(x=4\), then the volume of the solid obtained by rotating that region about the \(x\)-axis (disk method).</p>""",
                "a": r"""<p>Area: \(\displaystyle\int_0^4 x^{1/2}\,dx=\frac23 x^{3/2}\Big|_0^4=\frac{16}{3}\).</p>
<p>Volume: \(\displaystyle V=\pi\int_0^4 x\,dx=\pi\cdot\frac{x^2}{2}\Big|_0^4=8\pi\).</p>
\[\boxed{\text{area }=16/3;\ V=8\pi}\]""",
            },
            {
                "q": r"""<p>The region bounded by \(y=x^2\), \(y=0\), \(x=1\) is rotated about the \(y\)-axis. Find the volume using cylindrical shells.</p>""",
                "a": r"""<p>\(\displaystyle V=\int_0^1 2\pi x\cdot x^2\,dx=2\pi\int_0^1 x^3\,dx=2\pi\cdot\frac14=\dfrac{\pi}{2}\).</p>
\[\boxed{\pi/2}\]""",
            },
            {
                "q": r"""<p>Find the arc length of \(y=\dfrac{2}{3}x^{3/2}\) from \(x=0\) to \(x=3\).</p>""",
                "a": r"""<p>\(y'=\sqrt{x}\), so \(\sqrt{1+(y')^2}=\sqrt{1+x}\).</p>
\[
L=\int_0^3\sqrt{1+x}\,dx=\frac23(1+x)^{3/2}\Big|_0^3=\frac23\bigl(8-1\bigr)=\frac{14}{3}.
\]
\[\boxed{14/3}\]""",
            },
            {
                "q": r"""<p>Find the arc length of the parametric curve \(x=3\cos t\), \(y=3\sin t\), \(0\le t\le\pi\).</p>""",
                "a": r"""<p>\(\dot x=-3\sin t\), \(\dot y=3\cos t\), so \(\sqrt{\dot x^2+\dot y^2}=3\).</p>
\[
L=\int_0^{\pi}3\,dt=3\pi
\]
(semicircle of radius \(3\)).</p>
\[\boxed{3\pi}\]""",
            },
            {
                "q": r"""<p>Find the area common to the circles \(r=2\cos\theta\) and \(r=2\sin\theta\).</p>""",
                "a": r"""<p>The circles meet when \(2\cos\theta=2\sin\theta\Rightarrow\theta=\pi/4\) (first quadrant). The common area is</p>
\[
A=\int_0^{\pi/4}2\sin^2\theta\,d\theta+\int_{\pi/4}^{\pi/2}2\cos^2\theta\,d\theta.
\]
\[
\int_0^{\pi/4}2\sin^2\theta\,d\theta=\int_0^{\pi/4}(1-\cos 2\theta)\,d\theta=\frac{\pi}{4}-\frac12,
\]
and the second integral equals the first by symmetry, so \(A=\dfrac{\pi}{2}-1\).</p>
\[\boxed{\pi/2-1}\]""",
            },
            {
                "q": r"""<p>A region is bounded by \(y=e^{-x}\), \(y=0\), \(x=0\), \(x=1\). Find the volume when this region is rotated about the \(x\)-axis.</p>""",
                "a": r"""<p>Disk method:</p>
\[
V=\pi\int_0^1 e^{-2x}\,dx=\pi\Bigl[-\frac12 e^{-2x}\Bigr]_0^1=\pi\Bigl(-\frac12 e^{-2}+\frac12\Bigr)=\frac{\pi}{2}(1-e^{-2}).
\]
\[\boxed{\dfrac{\pi}{2}(1-e^{-2})}\]""",
            },
            {
                "q": r"""<p>For the polar curve \(r=\theta\), \(0\le\theta\le\pi\), set up and evaluate the arc-length integral.</p>""",
                "a": r"""<p>\(L=\displaystyle\int_0^{\pi}\sqrt{r^2+(dr/d\theta)^2}\,d\theta=\int_0^{\pi}\sqrt{\theta^2+1}\,d\theta\).</p>
<p>Using the standard formula \(\int\sqrt{\theta^2+1}\,d\theta=\dfrac{\theta}{2}\sqrt{\theta^2+1}+\dfrac12\ln\bigl|\theta+\sqrt{\theta^2+1}\bigr|\):</p>
\[
L=\frac{\pi}{2}\sqrt{\pi^2+1}+\frac12\ln\bigl(\pi+\sqrt{\pi^2+1}\bigr).
\]
\[\boxed{\dfrac{\pi}{2}\sqrt{\pi^2+1}+\dfrac12\ln\bigl(\pi+\sqrt{\pi^2+1}\bigr)}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ Q3
    "q3-weeks7-9": {
        "id": "Q3",
        "kind": "quarter",
        "title": "Quarter 3 (W7–9)",
        "weeks": "W7–9",
        "blurb": "Mixed first-order DEs (separable, linear, exact/homogeneous), second-order linear DEs, and SHM.",
        "questions": [
            {
                "q": r"""<p>Solve \(\dfrac{dy}{dx}=xy\) with \(y(0)=2\).</p>""",
                "a": r"""<p>Separate: \(\dfrac{dy}{y}=x\,dx\) (assuming \(y\neq 0\)).</p>
\[
\ln|y|=\frac{x^2}{2}+C\implies y=Ae^{x^2/2}.
\]
\(y(0)=2\Rightarrow A=2\), so \(y=2e^{x^2/2}\).</p>
\[\boxed{y=2e^{x^2/2}}\]""",
            },
            {
                "q": r"""<p>Solve the linear DE \(y'+2y=e^{-x}\), \(y(0)=1\).</p>""",
                "a": r"""<p>Integrating factor \(\mu=e^{\int 2\,dx}=e^{2x}\).</p>
\[
\frac{d}{dx}(ye^{2x})=e^{x}\implies ye^{2x}=e^{x}+C\implies y=e^{-x}+Ce^{-2x}.
\]
\(y(0)=1\Rightarrow 1+C=1\Rightarrow C=0\). Thus \(y=e^{-x}\).</p>
\[\boxed{y=e^{-x}}\]""",
            },
            {
                "q": r"""<p>Show that \(M\,dx+N\,dy=0\) with \(M=2xy+y^2\), \(N=x^2+2xy\) is exact, and find the general solution.</p>""",
                "a": r"""<p>\(M_y=2x+2y=N_x\), so exact. Seek \(F\) with \(F_x=M\):</p>
\[
F=x^2 y+xy^2+g(y).
\]
Then \(F_y=x^2+2xy+g'(y)=N=x^2+2xy\Rightarrow g'=0\). Solution \(x^2 y+xy^2=C\), or \(xy(x+y)=C\).</p>
\[\boxed{xy(x+y)=C}\]""",
            },
            {
                "q": r"""<p>Solve the homogeneous equation \(\dfrac{dy}{dx}=\dfrac{y}{x}+1\) for \(x&gt;0\).</p>""",
                "a": r"""<p>Let \(v=y/x\), so \(y=vx\), \(y'=v+xv'\). Then</p>
\[
v+xv'=v+1\implies xv'=1\implies v=\ln|x|+C.
\]
Hence \(y=x\ln x+Cx\) (for \(x&gt;0\)).</p>
\[\boxed{y=x\ln x+Cx}\]""",
            },
            {
                "q": r"""<p>Solve \(y''-5y'+6y=0\).</p>""",
                "a": r"""<p>Characteristic equation \(r^2-5r+6=0\Rightarrow(r-2)(r-3)=0\).</p>
\[
y=c_1 e^{2x}+c_2 e^{3x}.
\]
\[\boxed{y=c_1 e^{2x}+c_2 e^{3x}}\]""",
            },
            {
                "q": r"""<p>Solve \(y''+4y'+4y=0\).</p>""",
                "a": r"""<p>\(r^2+4r+4=(r+2)^2=0\), repeated root \(r=-2\).</p>
\[
y=(c_1+c_2 x)e^{-2x}.
\]
\[\boxed{y=(c_1+c_2 x)e^{-2x}}\]""",
            },
            {
                "q": r"""<p>Solve \(y''+9y=0\), \(y(0)=2\), \(y'(0)=0\).</p>""",
                "a": r"""<p>General solution \(y=A\cos 3x+B\sin 3x\).</p>
\[
y(0)=A=2;\quad y'=-3A\sin 3x+3B\cos 3x,\quad y'(0)=3B=0\Rightarrow B=0.
\]
So \(y=2\cos 3x\).</p>
\[\boxed{y=2\cos 3x}\]""",
            },
            {
                "q": r"""<p>A mass–spring system satisfies \(\ddot x+4x=0\) with \(x(0)=3\), \(\dot x(0)=-2\). Write \(x(t)\) in the form \(R\cos(\omega t-\phi)\) (find \(R\), \(\omega\), \(\phi\)).</p>""",
                "a": r"""<p>\(\omega=2\), \(x=A\cos 2t+B\sin 2t\). IC: \(A=3\), \(\dot x=-2A\sin 2t+2B\cos 2t\), \(\dot x(0)=2B=-2\Rightarrow B=-1\).</p>
\[
R=\sqrt{A^2+B^2}=\sqrt{10},\quad\cos\phi=\frac{A}{R}=\frac{3}{\sqrt{10}},\quad\sin\phi=\frac{B}{R}=-\frac{1}{\sqrt{10}}.
\]
Thus \(x(t)=\sqrt{10}\cos(2t-\phi)\) with \(\phi=\arctan(-1/3)\) in QIV (or equivalently \(\phi=-\arctan(1/3)\)).</p>
\[\boxed{x=\sqrt{10}\cos(2t-\phi),\ \phi=-\arctan(1/3)}\]""",
            },
            {
                "q": r"""<p>For undamped SHM \(\ddot x+\omega^2 x=0\), the amplitude is \(5\) and the period is \(\pi\). Find \(\omega\) and write a general solution.</p>""",
                "a": r"""<p>Period \(T=2\pi/\omega=\pi\Rightarrow\omega=2\). General solution</p>
\[
x(t)=5\cos(2t-\phi)=c_1\cos 2t+c_2\sin 2t
\]
(amplitude constraint absorbed into constants when IC are given).</p>
\[\boxed{\omega=2;\ x=c_1\cos 2t+c_2\sin 2t\ \text{(amp. }5\text{ when }c_1^2+c_2^2=25)}\]""",
            },
            {
                "q": r"""<p>Solve \(y''-y=e^{2x}\) by undetermined coefficients.</p>""",
                "a": r"""<p>Homogeneous: \(y_h=c_1 e^x+c_2 e^{-x}\). Particular: try \(y_p=Ae^{2x}\).</p>
\[
4Ae^{2x}-Ae^{2x}=e^{2x}\Rightarrow 3A=1\Rightarrow A=\frac13.
\]
\[
y=c_1 e^x+c_2 e^{-x}+\frac13 e^{2x}.
\]
\[\boxed{y=c_1 e^x+c_2 e^{-x}+\dfrac13 e^{2x}}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ Q4
    "q4-weeks10-12": {
        "id": "Q4",
        "kind": "quarter",
        "title": "Quarter 4 (W10–12)",
        "weeks": "W10–12",
        "blurb": "Mixed L'Hôpital limits, series convergence tests, and Taylor/Maclaurin applications.",
        "questions": [
            {
                "q": r"""<p>Evaluate \(\displaystyle\lim_{x\to 0}\frac{\tan x-x}{x^3}\).</p>""",
                "a": r"""<p>\(\frac{0}{0}\) form. After two applications of L'Hôpital (or using series \(\tan x=x+x^3/3+\cdots\)):</p>
\[
\lim_{x\to 0}\frac{\tan x-x}{x^3}=\frac13.
\]
(Series: \(\tan x-x\sim x^3/3\).)</p>
\[\boxed{1/3}\]""",
            },
            {
                "q": r"""<p>Find \(\displaystyle\lim_{x\to\infty} x\bigl(e^{1/x}-1\bigr)\).</p>""",
                "a": r"""<p>Write as \(\displaystyle\lim_{x\to\infty}\frac{e^{1/x}-1}{1/x}\). Let \(t=1/x\to 0^+\):</p>
\[
\lim_{t\to 0^+}\frac{e^t-1}{t}=1.
\]
\[\boxed{1}\]""",
            },
            {
                "q": r"""<p>Does \(\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}\) converge? Use the integral test.</p>""",
                "a": r"""<p>\(\displaystyle\int_2^{\infty}\frac{1}{x\ln x}\,dx=\lim_{b\to\infty}\ln(\ln x)\Big|_2^b=\infty\). The integral diverges, so the series diverges.</p>
\[\boxed{\text{diverges}}\]""",
            },
            {
                "q": r"""<p>Use the ratio test on \(\displaystyle\sum_{n=1}^{\infty}\frac{(-3)^n}{n!}\).</p>""",
                "a": r"""<p>\(\displaystyle L=\lim_{n\to\infty}\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\lim_{n\to\infty}\frac{3}{n+1}=0&lt;1\), so the series converges absolutely.</p>
\[\boxed{\text{converges absolutely}}\]""",
            },
            {
                "q": r"""<p>Test \(\displaystyle\sum_{n=1}^{\infty}(-1)^{n+1}\frac{n}{n^2+1}\) for absolute and conditional convergence.</p>""",
                "a": r"""<p>Absolute series behaves like \(\sum 1/n\) (limit comparison with \(1/n\)), so diverges. For AST: \(b_n=n/(n^2+1)\) decreases for large \(n\) and \(b_n\to 0\), so the alternating series converges. Hence conditionally convergent.</p>
\[\boxed{\text{conditionally convergent}}\]""",
            },
            {
                "q": r"""<p>Find the interval of convergence of \(\displaystyle\sum_{n=1}^{\infty}\frac{(x+2)^n}{n\cdot 3^n}\).</p>""",
                "a": r"""<p>Ratio test: \(\dfrac{|x+2|}{3}&lt;1\Rightarrow |x+2|&lt;3\Rightarrow -5&lt;x&lt;1\).</p>
<p>At \(x=1\): \(\sum 1/n\) diverges. At \(x=-5\): \(\sum(-1)^n/n\) converges (alternating harmonic). Interval: \([-5,1)\).</p>
\[\boxed{[-5,1)}\]""",
            },
            {
                "q": r"""<p>Find the Maclaurin polynomial of degree \(4\) for \(f(x)=\cos x\), and use it to approximate \(\cos(0.1)\).</p>""",
                "a": r"""<p>\(\cos x=1-\dfrac{x^2}{2!}+\dfrac{x^4}{4!}-\cdots\), so</p>
\[
P_4(x)=1-\frac{x^2}{2}+\frac{x^4}{24}.
\]
\[
P_4(0.1)=1-0.005+\frac{0.0001}{24}=0.995+\frac{1}{240000}=0.9950041\bar6.
\]
\[\boxed{P_4(x)=1-\frac{x^2}{2}+\frac{x^4}{24};\ \cos(0.1)\approx 0.99500417}\]""",
            },
            {
                "q": r"""<p>Using \(\dfrac{1}{1-x}=\sum_{n=0}^{\infty}x^n\) for \(|x|&lt;1\), find a power series for \(\dfrac{1}{(1-x)^2}\) and state its radius.</p>""",
                "a": r"""<p>Differentiate termwise:</p>
\[
\frac{1}{(1-x)^2}=\sum_{n=1}^{\infty} n x^{n-1}=\sum_{k=0}^{\infty}(k+1)x^k,\quad |x|&lt;1\ (R=1).
\]
\[\boxed{\sum_{n=0}^{\infty}(n+1)x^n,\ R=1}\]""",
            },
            {
                "q": r"""<p>Use the first three nonzero terms of the Maclaurin series for \(\sin x\) to approximate \(\displaystyle\int_0^{0.5}\frac{\sin x}{x}\,dx\).</p>""",
                "a": r"""<p>\(\sin x=x-\dfrac{x^3}{6}+\dfrac{x^5}{120}-\cdots\), so \(\dfrac{\sin x}{x}=1-\dfrac{x^2}{6}+\dfrac{x^4}{120}-\cdots\).</p>
\[
\int_0^{0.5}\Bigl(1-\frac{x^2}{6}+\frac{x^4}{120}\Bigr)\,dx=\Bigl[x-\frac{x^3}{18}+\frac{x^5}{600}\Bigr]_0^{1/2}=\frac12-\frac{1}{144}+\frac{1}{19200}.
\]
\[
=\frac{7200-100+0.75}{14400}=\frac{7100.75}{14400}\approx 0.4931.
\]
Exact combination: \(\dfrac12-\dfrac{1}{144}+\dfrac{1}{19200}=\dfrac{9600-133.3\ldots}{19200}\); better leave as \(\dfrac{1}{2}-\dfrac{1}{144}+\dfrac{1}{19200}\).</p>
\[\boxed{\tfrac12-\tfrac1{144}+\tfrac1{19200}\approx 0.4931}\]""",
            },
            {
                "q": r"""<p>Find the Taylor series for \(f(x)=\ln(1+x)\) about \(a=0\) up to the \(x^3\) term, and approximate \(\ln(1.2)\).</p>""",
                "a": r"""<p>\(\ln(1+x)=x-\dfrac{x^2}{2}+\dfrac{x^3}{3}-\cdots\) for \(|x|&lt;1\).</p>
\[
\ln(1.2)\approx 0.2-\frac{0.04}{2}+\frac{0.008}{3}=0.2-0.02+\frac{0.008}{3}=0.1826\bar6.
\]
\[\boxed{\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}+\cdots;\ \ln(1.2)\approx 0.1827}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ M1
    "m1-exam1-style": {
        "id": "M1",
        "kind": "mid",
        "title": "Mid A (W1–6)",
        "weeks": "W1–6",
        "blurb": "Exam-1 style paper spanning integration techniques through areas, volumes, and arc length (no differential equations).",
        "questions": [
            {
                "q": r"""<p>Evaluate \(\displaystyle\int\frac{\ln x}{x}\,dx\).</p>""",
                "a": r"""<p>Let \(u=\ln x\), \(du=dx/x\): \(\int u\,du=\dfrac{u^2}{2}+C=\dfrac{(\ln x)^2}{2}+C\).</p>
\[\boxed{\dfrac{(\ln x)^2}{2}+C}\]""",
            },
            {
                "q": r"""<p>Compute \(\displaystyle\int_0^{\pi/4}\tan^3\theta\sec\theta\,d\theta\).</p>""",
                "a": r"""<p>Let \(u=\sec\theta\), \(du=\sec\theta\tan\theta\,d\theta\). Write \(\tan^2\theta=\sec^2\theta-1\):</p>
\[
\int\tan^2\theta\cdot\tan\theta\sec\theta\,d\theta=\int(u^2-1)\,du=\frac{u^3}{3}-u.
\]
Limits \(\theta=0\to u=1\), \(\theta=\pi/4\to u=\sqrt{2}\):</p>
\[
\Bigl[\frac{\sec^3\theta}{3}-\sec\theta\Bigr]_0^{\pi/4}=\Bigl(\frac{2\sqrt{2}}{3}-\sqrt{2}\Bigr)-\Bigl(\frac13-1\Bigr)=\frac{2\sqrt{2}}{3}-\sqrt{2}+\frac23=\frac{2-3\sqrt{2}+2\sqrt{2}}{3}=\frac{2-\sqrt{2}}{3}.
\]
\[\boxed{\dfrac{2-\sqrt{2}}{3}}\]""",
            },
            {
                "q": r"""<p>Use integration by parts twice to find \(\displaystyle\int e^{2x}\sin(3x)\,dx\).</p>""",
                "a": r"""<p>Standard result after two parts and solving for \(I\):</p>
\[
I=\int e^{2x}\sin(3x)\,dx=e^{2x}\frac{2\sin(3x)-3\cos(3x)}{13}+C.
\]
\[\boxed{e^{2x}\dfrac{2\sin(3x)-3\cos(3x)}{13}+C}\]""",
            },
            {
                "q": r"""<p>Decompose \(\dfrac{4x^2-3x+2}{(x-1)^2(x+1)}\) into partial fractions and integrate.</p>""",
                "a": r"""<p>\(\dfrac{A}{x-1}+\dfrac{B}{(x-1)^2}+\dfrac{C}{x+1}\). Clearing denominators:</p>
\[
A(x-1)(x+1)+B(x+1)+C(x-1)^2=4x^2-3x+2.
\]
At \(x=1\): \(2B=3\Rightarrow B=3/2\). At \(x=-1\): \(4C=9\Rightarrow C=9/4\). Matching \(x^2\) gives \(A+C=4\Rightarrow A=7/4\).</p>
\[
\int\Bigl(\frac{7/4}{x-1}+\frac{3/2}{(x-1)^2}+\frac{9/4}{x+1}\Bigr)\,dx=\frac74\ln|x-1|-\frac{3/2}{x-1}+\frac94\ln|x+1|+C.
\]
\[\boxed{\dfrac74\ln|x-1|-\dfrac{3}{2(x-1)}+\dfrac94\ln|x+1|+C}\]""",
            },
            {
                "q": r"""<p>Determine whether \(\displaystyle\int_2^{\infty}\frac{x}{x^3+1}\,dx\) converges, and bound or evaluate as appropriate.</p>""",
                "a": r"""<p>For large \(x\), \(\dfrac{x}{x^3+1}\sim\dfrac{1}{x^2}\). By limit comparison with \(\sum\)-style \(p=2\) integral \(\int_2^{\infty}x^{-2}\,dx&lt;\infty\), the integral converges. (Exact antiderivative via PF is optional; convergence is the key exam ask.)</p>
\[\boxed{\text{converges (compare with }x^{-2})}\]""",
            },
            {
                "q": r"""<p>Approximate \(\displaystyle\int_1^2\frac{1}{x}\,dx\) by Simpson's rule with \(n=4\). Compare with \(\ln 2\).</p>""",
                "a": r"""<p>\(h=1/4\). Nodes \(1, 5/4, 3/2, 7/4, 2\). Values \(1, 4/5, 2/3, 4/7, 1/2\).</p>
\[
S=\frac{h}{3}\bigl(1+4\cdot\tfrac45+2\cdot\tfrac23+4\cdot\tfrac47+\tfrac12\bigr)=\frac{1}{12}\Bigl(1+\frac{16}{5}+\frac{4}{3}+\frac{16}{7}+\frac12\Bigr).
\]
\[
1+\frac{16}{5}+\frac{4}{3}+\frac{16}{7}+\frac12=\frac{1747}{210},\quad
S=\frac{1747}{2520}\approx 0.6933
\]
(compare with \(\ln 2\approx 0.6931\)).</p>
\[\boxed{1747/2520\approx 0.6933}\]""",
            },
            {
                "q": r"""<p>Sketch/identify \(r=1+2\cos\theta\) and find the area of the inner loop.</p>""",
                "a": r"""<p>Limacon with inner loop; loop when \(r=0\Rightarrow\cos\theta=-1/2\Rightarrow\theta=2\pi/3,4\pi/3\).</p>
\[
A=\frac12\int_{2\pi/3}^{4\pi/3}(1+2\cos\theta)^2\,d\theta.
\]
Expanding and integrating yields \(A=\pi-3\sqrt{3}/2\). (Standard textbook value for this limacon.)</p>
\[\boxed{\pi-\dfrac{3\sqrt{3}}{2}}\]""",
            },
            {
                "q": r"""<p>Find \(\dfrac{d^2y}{dx^2}\) for \(x=\cos t\), \(y=\sin(2t)\).</p>""",
                "a": r"""<p>\(\dot x=-\sin t\), \(\dot y=2\cos(2t)\), \(\dfrac{dy}{dx}=\dfrac{2\cos(2t)}{-\sin t}\).</p>
<p>\(\dfrac{dy}{dx}=-\dfrac{2\cos 2t}{\sin t}\). Differentiating with respect to \(t\) and dividing by \(\dot x=-\sin t\):</p>
\[
\frac{d^2y}{dx^2}=\frac{2(2\sin 2t\sin t+\cos 2t\cos t)}{\sin^3 t}.
\]
\[\boxed{\dfrac{dy}{dx}=-\dfrac{2\cos 2t}{\sin t};\ \dfrac{d^2y}{dx^2}=\dfrac{2(2\sin 2t\sin t+\cos 2t\cos t)}{\sin^3 t}}\]""",
            },
            {
                "q": r"""<p>Find the volume of the solid formed by rotating the region under \(y=\sin x\) from \(0\) to \(\pi\) about the \(x\)-axis.</p>""",
                "a": r"""<p>\(\displaystyle V=\pi\int_0^{\pi}\sin^2 x\,dx=\pi\int_0^{\pi}\frac{1-\cos 2x}{2}\,dx=\frac{\pi}{2}\bigl[x-\tfrac12\sin 2x\bigr]_0^{\pi}=\dfrac{\pi^2}{2}\).</p>
\[\boxed{\pi^2/2}\]""",
            },
            {
                "q": r"""<p>Use washers to find the volume when the region between \(y=x\) and \(y=x^2\) is rotated about the \(x\)-axis.</p>""",
                "a": r"""<p>Intersection at \(x=0,1\).</p>
\[
V=\pi\int_0^1\bigl(x^2-(x^2)^2\bigr)\,dx=\pi\int_0^1(x^2-x^4)\,dx=\pi\Bigl[\frac{x^3}{3}-\frac{x^5}{5}\Bigr]_0^1=\pi\Bigl(\frac13-\frac15\Bigr)=\frac{2\pi}{15}.
\]
\[\boxed{2\pi/15}\]""",
            },
            {
                "q": r"""<p>Find the arc length of \(y=\ln(\cos x)\) from \(x=0\) to \(x=\pi/4\).</p>""",
                "a": r"""<p>\(y'=-\tan x\), \(\sqrt{1+\tan^2 x}=\sec x\) (for \(0\le x\le\pi/4\)).</p>
\[
L=\int_0^{\pi/4}\sec x\,dx=\ln|\sec x+\tan x|\Big|_0^{\pi/4}=\ln(\sqrt{2}+1)-\ln(1)=\ln(1+\sqrt{2}).
\]
\[\boxed{\ln(1+\sqrt{2})}\]""",
            },
            {
                "q": r"""<p>Find the surface area generated by rotating \(y=\sqrt{x}\), \(1\le x\le 4\), about the \(x\)-axis.</p>""",
                "a": r"""<p>\(y'=1/(2\sqrt{x})\), \(\sqrt{1+(y')^2}=\sqrt{1+1/(4x)}=\dfrac{\sqrt{4x+1}}{2\sqrt{x}}\).</p>
\[
S=2\pi\int_1^4\sqrt{x}\cdot\frac{\sqrt{4x+1}}{2\sqrt{x}}\,dx=\pi\int_1^4\sqrt{4x+1}\,dx=\pi\cdot\frac{1}{6}(4x+1)^{3/2}\Big|_1^4=\frac{\pi}{6}\bigl(17^{3/2}-5^{3/2}\bigr).
\]
\[\boxed{\dfrac{\pi}{6}\bigl(17\sqrt{17}-5\sqrt{5}\bigr)}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ M2
    "m2-exam2-style": {
        "id": "M2",
        "kind": "mid",
        "title": "Mid B (W7–12)",
        "weeks": "W7–12",
        "blurb": "Exam-2 style paper spanning first- and second-order DEs, SHM, L'Hôpital, series tests, and Taylor series.",
        "questions": [
            {
                "q": r"""<p>Solve \(\dfrac{dy}{dx}=\dfrac{y^2}{x+1}\), \(y(0)=1\).</p>""",
                "a": r"""<p>\(\dfrac{dy}{y^2}=\dfrac{dx}{x+1}\Rightarrow -\dfrac{1}{y}=\ln|x+1|+C\).</p>
\[
y(0)=1\Rightarrow -1=C,\quad -\frac{1}{y}=\ln|x+1|-1,\quad y=\frac{1}{1-\ln|x+1|}.
\]
\[\boxed{y=\dfrac{1}{1-\ln|x+1|}}\]""",
            },
            {
                "q": r"""<p>Solve \(xy'+2y=x^3\), \(x&gt;0\), \(y(1)=2\).</p>""",
                "a": r"""<p>Write \(y'+\dfrac{2}{x}y=x^2\). IF \(\mu=x^2\).</p>
\[
\frac{d}{dx}(x^2 y)=x^4\implies x^2 y=\frac{x^5}{5}+C\implies y=\frac{x^3}{5}+\frac{C}{x^2}.
\]
\(y(1)=2\Rightarrow 1/5+C=2\Rightarrow C=9/5\). So \(y=\dfrac{x^3}{5}+\dfrac{9}{5x^2}\).</p>
\[\boxed{y=\dfrac{x^3}{5}+\dfrac{9}{5x^2}}\]""",
            },
            {
                "q": r"""<p>Solve the Bernoulli equation \(y'+y=xy^3\).</p>""",
                "a": r"""<p>Divide by \(y^3\): \(y^{-3}y'+y^{-2}=x\). Let \(v=y^{-2}\), \(v'=-2y^{-3}y'\).</p>
\[
-\frac12 v'+v=x\implies v'-2v=-2x.
\]
IF \(e^{-2x}\): \(\dfrac{d}{dx}(ve^{-2x})=-2xe^{-2x}\). Integrating by parts:</p>
\[
ve^{-2x}=xe^{-2x}+\frac12 e^{-2x}+C,\quad v=x+\frac12+Ce^{2x}.
\]
\[
y^{-2}=x+\frac12+Ce^{2x}.
\]
\[\boxed{y^{-2}=x+\dfrac12+Ce^{2x}}\]""",
            },
            {
                "q": r"""<p>Solve \(y''-2y'+5y=0\).</p>""",
                "a": r"""<p>\(r^2-2r+5=0\Rightarrow r=1\pm 2i\).</p>
\[
y=e^{x}(c_1\cos 2x+c_2\sin 2x).
\]
\[\boxed{y=e^{x}(c_1\cos 2x+c_2\sin 2x)}\]""",
            },
            {
                "q": r"""<p>Find the general solution of \(y''+y=\cos x\).</p>""",
                "a": r"""<p>\(y_h=c_1\cos x+c_2\sin x\). Since \(\cos x\) is a homogeneous solution, try \(y_p=x(A\cos x+B\sin x)\).</p>
<p>Computing \(y_p''+y_p=\cos x\) yields \(A=0\), \(B=1/2\). Thus \(y_p=\dfrac{x}{2}\sin x\).</p>
\[
y=c_1\cos x+c_2\sin x+\frac{x}{2}\sin x.
\]
\[\boxed{y=c_1\cos x+c_2\sin x+\dfrac{x}{2}\sin x}\]""",
            },
            {
                "q": r"""<p>A unit mass on a spring with \(k=16\) (no damping) is released from \(x=1\) with zero initial velocity. Find \(x(t)\).</p>""",
                "a": r"""<p>\(\ddot x+16x=0\), \(\omega=4\). \(x=A\cos 4t+B\sin 4t\). IC: \(A=1\), \(\dot x(0)=4B=0\Rightarrow B=0\).</p>
\[
x(t)=\cos 4t.
\]
\[\boxed{x(t)=\cos 4t}\]""",
            },
            {
                "q": r"""<p>Evaluate \(\displaystyle\lim_{x\to 0^+ }x^x\).</p>""",
                "a": r"""<p>Write \(x^x=e^{x\ln x}\). \(\lim_{x\to 0^+}x\ln x=\lim\dfrac{\ln x}{1/x}=\lim\dfrac{1/x}{-1/x^2}=0\) (L'Hôpital). Hence \(x^x\to e^0=1\).</p>
\[\boxed{1}\]""",
            },
            {
                "q": r"""<p>Determine the convergence of \(\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{2^n}\) using the ratio test.</p>""",
                "a": r"""<p>\(\displaystyle L=\lim\dfrac{(n+1)^2/2^{n+1}}{n^2/2^n}=\dfrac12\lim\Bigl(\dfrac{n+1}{n}\Bigr)^2=\dfrac12&lt;1\). Converges absolutely.</p>
\[\boxed{\text{converges}}\]""",
            },
            {
                "q": r"""<p>Does \(\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^n}{\sqrt{n}}\) converge absolutely, conditionally, or diverge?</p>""",
                "a": r"""<p>Absolute series is a \(p\)-series with \(p=1/2\le 1\), diverges. AST applies (\(b_n=n^{-1/2}\downarrow 0\)), so conditionally convergent.</p>
\[\boxed{\text{conditionally convergent}}\]""",
            },
            {
                "q": r"""<p>Find the radius of convergence of \(\displaystyle\sum_{n=0}^{\infty}n!(x-2)^n\).</p>""",
                "a": r"""<p>\(\displaystyle L=\lim n!\,|x-2|\cdot\dfrac{(n+1)!}{n!}=\lim(n+1)|x-2|=\infty\) unless \(x=2\). Radius \(R=0\).</p>
\[\boxed{R=0}\]""",
            },
            {
                "q": r"""<p>Find the Taylor polynomial of degree \(2\) for \(f(x)=\sqrt{x}\) about \(a=4\), and use it to approximate \(\sqrt{4.1}\).</p>""",
                "a": r"""<p>\(f(4)=2\), \(f'(x)=\dfrac12 x^{-1/2}\), \(f'(4)=\dfrac14\), \(f''(x)=-\dfrac14 x^{-3/2}\), \(f''(4)=-\dfrac{1}{32}\).</p>
\[
P_2(x)=2+\frac14(x-4)-\frac{1}{64}(x-4)^2.
\]
\[
\sqrt{4.1}\approx 2+\frac14(0.1)-\frac{1}{64}(0.01)=2.025-0.00015625=2.02484375.
\]
\[\boxed{P_2(x)=2+\frac14(x-4)-\frac1{64}(x-4)^2;\ \sqrt{4.1}\approx 2.02484}\]""",
            },
            {
                "q": r"""<p>Using the Maclaurin series for \(e^x\), approximate \(\displaystyle\int_0^{0.5}e^{-x^2}\,dx\) with error less than \(0.001\) by estimating the next term.</p>""",
                "a": r"""<p>\(e^{-x^2}=1-x^2+\dfrac{x^4}{2}-\dfrac{x^6}{6}+\cdots\).</p>
\[
\int_0^{1/2}\Bigl(1-x^2+\frac{x^4}{2}\Bigr)\,dx=\Bigl[x-\frac{x^3}{3}+\frac{x^5}{10}\Bigr]_0^{1/2}=\frac12-\frac{1}{24}+\frac{1}{320}=\frac{443}{960}\approx 0.46146.
\]
The next term satisfies \(\displaystyle\int_0^{1/2}\frac{x^6}{6}\,dx=\frac{1}{2688}&lt;0.001\), so this truncation meets the error goal.</p>
\[\boxed{443/960\approx 0.4615}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ F1
    "f1-full-a": {
        "id": "F1",
        "kind": "full",
        "title": "Full A",
        "weeks": "W1–12",
        "blurb": "Whole-subject mixed paper A covering integration, applications, DEs, limits, series, and Taylor.",
        "questions": [
            {
                "q": r"""<p>Evaluate \(\displaystyle\int\frac{x+2}{\sqrt{x^2+4x+5}}\,dx\).</p>""",
                "a": r"""<p>Complete the square: \(x^2+4x+5=(x+2)^2+1\). Let \(u=x+2\), \(du=dx\):</p>
\[
\int\frac{u}{\sqrt{u^2+1}}\,du=\sqrt{u^2+1}+C=\sqrt{x^2+4x+5}+C.
\]
\[\boxed{\sqrt{x^2+4x+5}+C}\]""",
            },
            {
                "q": r"""<p>Find \(\displaystyle\int_0^1\frac{x^2}{1+x}\,dx\).</p>""",
                "a": r"""<p>Polynomial division: \(\dfrac{x^2}{1+x}=x-1+\dfrac{1}{1+x}\).</p>
\[
\int_0^1\Bigl(x-1+\frac{1}{1+x}\Bigr)\,dx=\Bigl[\frac{x^2}{2}-x+\ln|1+x|\Bigr]_0^1=\frac12-1+\ln 2=\ln 2-\frac12.
\]
\[\boxed{\ln 2-\dfrac12}\]""",
            },
            {
                "q": r"""<p>Use the Trapezoidal rule with \(n=2\) to approximate \(\displaystyle\int_0^{\pi}\sin x\,dx\), and find the absolute error versus the exact value \(2\).</p>""",
                "a": r"""<p>\(h=\pi/2\). Values \(0,1,0\).</p>
\[
T=\frac{\pi}{4}(0+2\cdot 1+0)=\frac{\pi}{2}\approx 1.5708.
\]
Error \(|2-\pi/2|=2-\pi/2\approx 0.4292\).</p>
\[\boxed{T=\pi/2;\ |E|\approx 0.4292}\]""",
            },
            {
                "q": r"""<p>Find the area inside \(r=2+2\cos\theta\).</p>""",
                "a": r"""<p>Cardioid; \(\displaystyle A=\frac12\int_0^{2\pi}(2+2\cos\theta)^2\,d\theta=2\int_0^{2\pi}(1+\cos\theta)^2\,d\theta=2\int_0^{2\pi}(1+2\cos\theta+\cos^2\theta)\,d\theta\).</p>
\[
=2\Bigl[2\pi+0+\pi\Bigr]=6\pi.
\]
\[\boxed{6\pi}\]""",
            },
            {
                "q": r"""<p>For \(x=t-\sin t\), \(y=1-\cos t\) (cycloid), find the arc length for one arch \(0\le t\le 2\pi\).</p>""",
                "a": r"""<p>\(\dot x=1-\cos t\), \(\dot y=\sin t\), \(\sqrt{\dot x^2+\dot y^2}=\sqrt{2-2\cos t}=2\sin(t/2)\) on \([0,2\pi]\).</p>
\[
L=\int_0^{2\pi}2\sin\frac{t}{2}\,dt=-4\cos\frac{t}{2}\Big|_0^{2\pi}=8.
\]
\[\boxed{8}\]""",
            },
            {
                "q": r"""<p>Find the volume generated by rotating \(y=\dfrac{1}{x}\), \(1\le x\le 2\), about the \(y\)-axis (shells).</p>""",
                "a": r"""<p>\(\displaystyle V=\int_1^2 2\pi x\cdot\frac{1}{x}\,dx=2\pi\int_1^2 dx=2\pi\).</p>
\[\boxed{2\pi}\]""",
            },
            {
                "q": r"""<p>Solve \(\dfrac{dy}{dx}+y\tan x=\sec x\), \(y(0)=0\).</p>""",
                "a": r"""<p>IF \(\mu=\sec x\). Then \(\dfrac{d}{dx}(y\sec x)=\sec^2 x\), so \(y\sec x=\tan x+C\).</p>
\[
y=\sin x+C\cos x;\quad y(0)=0\Rightarrow C=0;\quad y=\sin x.
\]
\[\boxed{y=\sin x}\]""",
            },
            {
                "q": r"""<p>Solve \(y''-y'-2y=0\), \(y(0)=1\), \(y'(0)=0\).</p>""",
                "a": r"""<p>\((r-2)(r+1)=0\). \(y=c_1 e^{2x}+c_2 e^{-x}\).</p>
\[
c_1+c_2=1,\quad 2c_1-c_2=0\implies c_1=\frac13,\ c_2=\frac23.
\]
\[
y=\frac13 e^{2x}+\frac23 e^{-x}.
\]
\[\boxed{y=\dfrac13 e^{2x}+\dfrac23 e^{-x}}\]""",
            },
            {
                "q": r"""<p>Write the equation of undamped SHM with period \(4\) and amplitude \(3\), given \(x(0)=0\) and \(\dot x(0)&gt;0\).</p>""",
                "a": r"""<p>\(T=2\pi/\omega=4\Rightarrow\omega=\pi/2\). \(x=3\sin\bigl(\frac{\pi}{2}t\bigr)\) satisfies \(x(0)=0\) and positive initial velocity.</p>
\[\boxed{x=3\sin\bigl(\dfrac{\pi}{2}t\bigr)}\]""",
            },
            {
                "q": r"""<p>Evaluate \(\displaystyle\lim_{x\to\infty}\frac{x^2+e^x}{e^x+x}\).</p>""",
                "a": r"""<p>Divide by \(e^x\): \(\dfrac{x^2 e^{-x}+1}{1+x e^{-x}}\to\dfrac{0+1}{1+0}=1\) (polynomials grow slower than \(e^x\)).</p>
\[\boxed{1}\]""",
            },
            {
                "q": r"""<p>Test \(\displaystyle\sum_{n=1}^{\infty}\frac{2^n}{n^n}\) with the root test.</p>""",
                "a": r"""<p>\(\sqrt[n]{a_n}=\dfrac{2}{n}\to 0&lt;1\), so the series converges.</p>
\[\boxed{\text{converges}}\]""",
            },
            {
                "q": r"""<p>Find the Maclaurin series for \(f(x)=\dfrac{1}{1+x^2}\) up to \(x^4\), and approximate \(\arctan(0.2)\) using \(\arctan x=\int_0^x\dfrac{1}{1+t^2}\,dt\).</p>""",
                "a": r"""<p>\(\dfrac{1}{1+x^2}=1-x^2+x^4-\cdots\) (\(|x|&lt;1\)).</p>
\[
\arctan(0.2)\approx\int_0^{0.2}(1-t^2+t^4)\,dt=\Bigl[t-\frac{t^3}{3}+\frac{t^5}{5}\Bigr]_0^{0.2}=0.2-\frac{0.008}{3}+\frac{0.00032}{5}\approx 0.1974.
\]
\[\boxed{\approx 0.1974}\]""",
            },
            {
                "q": r"""<p>Determine whether \(\displaystyle\int_0^1\frac{\ln x}{\sqrt{x}}\,dx\) converges, and evaluate it if so.</p>""",
                "a": r"""<p>Improper at \(0\). Let \(I=\lim_{\varepsilon\to 0^+}\int_\varepsilon^1 x^{-1/2}\ln x\,dx\). Integrate by parts: \(u=\ln x\), \(dv=x^{-1/2}dx\), \(du=dx/x\), \(v=2x^{1/2}\).</p>
\[
\bigl[2\sqrt{x}\ln x\bigr]_\varepsilon^1-\int_\varepsilon^1 2x^{1/2}\cdot\frac{1}{x}\,dx=0-2\sqrt{\varepsilon}\ln\varepsilon-2\int_\varepsilon^1 x^{-1/2}\,dx.
\]
\(\sqrt{\varepsilon}\ln\varepsilon\to 0\), and \(-2\cdot 2x^{1/2}\big|_\varepsilon^1=-4+4\sqrt{\varepsilon}\to -4\). So \(I=-4\).</p>
\[\boxed{-4}\]""",
            },
            {
                "q": r"""<p>Solve \(y''+4y'+5y=0\) and identify the damping type for the corresponding mass–spring model \(\ddot x+4\dot x+5x=0\).</p>""",
                "a": r"""<p>\(r^2+4r+5=0\Rightarrow r=-2\pm i\). Solution \(y=e^{-2x}(c_1\cos x+c_2\sin x)\). Discriminant \(16-20&lt;0\) and damping present: underdamped.</p>
\[\boxed{y=e^{-2x}(c_1\cos x+c_2\sin x);\ \text{underdamped}}\]""",
            },
            {
                "q": r"""<p>Find the interval of convergence of \(\displaystyle\sum_{n=0}^{\infty}\frac{(-1)^n(x-3)^n}{2^n}\).</p>""",
                "a": r"""<p>Geometric with ratio \(\dfrac{-(x-3)}{2}\). Need \(\dfrac{|x-3|}{2}&lt;1\Rightarrow |x-3|&lt;2\Rightarrow 1&lt;x&lt;5\). Endpoints: at \(x=5\), \(\sum(-1)^n\) diverges; at \(x=1\), \(\sum 1\) diverges. Interval \((1,5)\).</p>
\[\boxed{(1,5)}\]""",
            },
        ],
    },

    # ------------------------------------------------------------------ F2
    "f2-full-b": {
        "id": "F2",
        "kind": "full",
        "title": "Full B",
        "weeks": "W1–12",
        "blurb": "Whole-subject mixed paper B with a different difficulty mix across integration, geometry of curves, DEs, and series/Taylor.",
        "questions": [
            {
                "q": r"""<p>Evaluate \(\displaystyle\int\cos^2(3x)\,dx\).</p>""",
                "a": r"""<p>\(\cos^2(3x)=\dfrac{1+\cos(6x)}{2}\).</p>
\[
\int\cos^2(3x)\,dx=\frac{x}{2}+\frac{1}{12}\sin(6x)+C.
\]
\[\boxed{\dfrac{x}{2}+\dfrac{1}{12}\sin(6x)+C}\]""",
            },
            {
                "q": r"""<p>Compute \(\displaystyle\int\frac{2x+3}{x^2+3x+2}\,dx\).</p>""",
                "a": r"""<p>Denominator \((x+1)(x+2)\). PF: \(\dfrac{A}{x+1}+\dfrac{B}{x+2}\) with \(A=1\), \(B=1\).</p>
\[
\int\Bigl(\frac{1}{x+1}+\frac{1}{x+2}\Bigr)\,dx=\ln|x+1|+\ln|x+2|+C=\ln|(x+1)(x+2)|+C.
\]
(Alternatively recognize nearly \(d(x^2+3x+2)\).)</p>
\[\boxed{\ln|x^2+3x+2|+C}\]""",
            },
            {
                "q": r"""<p>Show that \(\displaystyle\int_1^{\infty}\frac{\ln x}{x^2}\,dx\) converges and evaluate it.</p>""",
                "a": r"""<p>Parts: \(u=\ln x\), \(dv=x^{-2}dx\), \(du=dx/x\), \(v=-1/x\).</p>
\[
\Bigl[-\frac{\ln x}{x}\Bigr]_1^{b}+\int_1^{b}\frac{1}{x^2}\,dx=\Bigl(-\frac{\ln b}{b}+0\Bigr)+\Bigl[-\frac{1}{x}\Bigr]_1^{b}.
\]
As \(b\to\infty\), \(\ln b/b\to 0\), and \(-1/b+1\to 1\). Value \(=1\).</p>
\[\boxed{1}\]""",
            },
            {
                "q": r"""<p>Use Simpson's rule with \(n=2\) on \(\displaystyle\int_0^2\sqrt{1+x^3}\,dx\) (leave in exact radical form).</p>""",
                "a": r"""<p>\(h=1\). Nodes \(0,1,2\); values \(1\), \(\sqrt{2}\), \(\sqrt{9}=\sqrt{1+8}=3\).</p>
\[
S=\frac{1}{3}\bigl(1+4\sqrt{2}+3\bigr)=\frac{4+4\sqrt{2}}{3}=\frac{4(1+\sqrt{2})}{3}.
\]
\[\boxed{\dfrac{4(1+\sqrt{2})}{3}}\]""",
            },
            {
                "q": r"""<p>Find the slope \(\dfrac{dy}{dx}\) for the polar curve \(r=2\theta\) at \(\theta=\pi/2\).</p>""",
                "a": r"""<p>\(\dfrac{dy}{dx}=\dfrac{\frac{dr}{d\theta}\sin\theta+r\cos\theta}{\frac{dr}{d\theta}\cos\theta-r\sin\theta}\). Here \(dr/d\theta=2\).</p>
\[
\frac{dy}{dx}=\frac{2\sin\theta+2\theta\cos\theta}{2\cos\theta-2\theta\sin\theta}=\frac{\sin\theta+\theta\cos\theta}{\cos\theta-\theta\sin\theta}.
\]
At \(\theta=\pi/2\): \(\dfrac{1+0}{0-(\pi/2)\cdot 1}=-\dfrac{2}{\pi}\).</p>
\[\boxed{-2/\pi}\]""",
            },
            {
                "q": r"""<p>The region bounded by \(y=x^2\) and \(y=4\) is rotated about \(y=4\). Find the volume (disks/washers or shells).</p>""",
                "a": r"""<p>Using washers with respect to \(x\), from \(x=-2\) to \(2\): radius \(4-x^2\).</p>
\[
V=\pi\int_{-2}^{2}(4-x^2)^2\,dx=2\pi\int_0^2(16-8x^2+x^4)\,dx=2\pi\Bigl[16x-\frac{8x^3}{3}+\frac{x^5}{5}\Bigr]_0^2=2\pi\Bigl(32-\frac{64}{3}+\frac{32}{5}\Bigr)=\frac{512\pi}{15}.
\]
\[\boxed{512\pi/15}\]""",
            },
            {
                "q": r"""<p>Find the arc length of \(x=\dfrac{y^3}{6}+\dfrac{1}{2y}\) from \(y=1\) to \(y=2\).</p>""",
                "a": r"""<p>\(\dfrac{dx}{dy}=\dfrac{y^2}{2}-\dfrac{1}{2y^2}\), \(\sqrt{1+(x')^2}=\dfrac{y^2}{2}+\dfrac{1}{2y^2}\) (perfect square).</p>
\[
L=\int_1^2\Bigl(\frac{y^2}{2}+\frac{1}{2y^2}\Bigr)\,dy=\Bigl[\frac{y^3}{6}-\frac{1}{2y}\Bigr]_1^2=\Bigl(\frac{8}{6}-\frac{1}{4}\Bigr)-\Bigl(\frac16-\frac12\Bigr)=\frac{17}{12}.
\]
\[\boxed{17/12}\]""",
            },
            {
                "q": r"""<p>Solve the exact equation \((2x+y)\,dx+(x+2y)\,dy=0\).</p>""",
                "a": r"""<p>\(M_y=1=N_x\). \(F=x^2+xy+g(y)\), \(F_y=x+g'=x+2y\Rightarrow g'=2y\), \(g=y^2\).</p>
\[
x^2+xy+y^2=C.
\]
\[\boxed{x^2+xy+y^2=C}\]""",
            },
            {
                "q": r"""<p>Solve \(y''-6y'+9y=e^{3x}\).</p>""",
                "a": r"""<p>\(y_h=(c_1+c_2 x)e^{3x}\). For particular solution, resonance of order 2: try \(y_p=Ax^2 e^{3x}\).</p>
<p>Computing gives \(A=1/2\). Thus \(y=(c_1+c_2 x)e^{3x}+\dfrac12 x^2 e^{3x}\).</p>
\[\boxed{y=(c_1+c_2 x+\tfrac12 x^2)e^{3x}}\]""",
            },
            {
                "q": r"""<p>A mass–spring–dashpot system has equation \(\ddot x+6\dot x+5x=0\). Classify the damping and solve with \(x(0)=2\), \(\dot x(0)=0\).</p>""",
                "a": r"""<p>\(r^2+6r+5=(r+1)(r+5)=0\), two negative real roots: overdamped.</p>
\[
x=c_1 e^{-t}+c_2 e^{-5t};\quad c_1+c_2=2,\ -c_1-5c_2=0\implies c_1=\frac52,\ c_2=-\frac12.
\]
\[
x=\frac52 e^{-t}-\frac12 e^{-5t}.
\]
\[\boxed{x=\dfrac52 e^{-t}-\dfrac12 e^{-5t};\ \text{overdamped}}\]""",
            },
            {
                "q": r"""<p>Evaluate \(\displaystyle\lim_{x\to 0}\frac{1-\cos(2x)}{x\sin x}\).</p>""",
                "a": r"""<p>Use \(1-\cos(2x)=2\sin^2 x\):</p>
\[
\lim_{x\to 0}\frac{2\sin^2 x}{x\sin x}=\lim_{x\to 0}\frac{2\sin x}{x}=2.
\]
\[\boxed{2}\]""",
            },
            {
                "q": r"""<p>Use the alternating series estimation theorem to approximate \(\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n^2}\) with error less than \(0.05\), and give the corresponding partial sum.</p>""",
                "a": r"""<p>Need first omitted term \(1/(N+1)^2&lt;0.05\Rightarrow (N+1)^2&gt;20\Rightarrow N+1\ge 5\Rightarrow N\ge 4\).</p>
\[
s_4=1-\frac14+\frac19-\frac{1}{16}=\frac{144-36+16-9}{144}=\frac{115}{144}\approx 0.7986.
\]
\[\boxed{s_4=115/144\ (|E|&lt;1/25=0.04)}\]""",
            },
            {
                "q": r"""<p>Find a power series centred at \(0\) for \(\displaystyle\int\frac{1}{1+x^3}\,dx\) (formal, first four nonzero terms of the integrand expansion for \(|x|&lt;1\)).</p>""",
                "a": r"""<p>For \(|x|&lt;1\), \(\dfrac{1}{1+x^3}=1-x^3+x^6-x^9+\cdots\).</p>
\[
\int\frac{1}{1+x^3}\,dx=C+x-\frac{x^4}{4}+\frac{x^7}{7}-\frac{x^{10}}{10}+\cdots.
\]
\[\boxed{C+x-\dfrac{x^4}{4}+\dfrac{x^7}{7}-\dfrac{x^{10}}{10}+\cdots}\]""",
            },
            {
                "q": r"""<p>Find the Taylor series of \(f(x)=e^{2x}\) about \(a=1\) up to the quadratic term.</p>""",
                "a": r"""<p>\(f(1)=e^2\), \(f'=2e^{2x}\), \(f'(1)=2e^2\), \(f''=4e^{2x}\), \(f''(1)=4e^2\).</p>
\[
e^{2x}=e^2+2e^2(x-1)+2e^2(x-1)^2+\cdots=e^2\bigl(1+2(x-1)+2(x-1)^2+\cdots\bigr).
\]
\[\boxed{e^2\bigl(1+2(x-1)+2(x-1)^2+\cdots\bigr)}\]""",
            },
            {
                "q": r"""<p>A tank holds \(100\) L of brine with \(5\) kg salt. Pure water enters at \(2\) L/min and the well-mixed solution leaves at \(2\) L/min. How much salt remains after \(30\) minutes?</p>""",
                "a": r"""<p>Let \(Q(t)\) be kg of salt. \(Q'= -\dfrac{2}{100}Q=-\dfrac{1}{50}Q\), \(Q(0)=5\).</p>
\[
Q(t)=5e^{-t/50};\quad Q(30)=5e^{-30/50}=5e^{-3/5}.
\]
\[\boxed{5e^{-3/5}\text{ kg}}\]""",
            },
        ],
    },
}
