# -*- coding: utf-8 -*-
"""MATH142 Engineering Mathematics 2 (UOW) — revision pack data A (T01–T09)."""

T01 = {
    'id': 'T01',
    'kind': 'topic',
    'title': 'Integration Techniques',
    'weeks': 'W1',
    'blurb': 'Substitution, integration by parts, trigonometric integrals, and trigonometric substitution.',
    'questions': [
        {
            'q': r'''Evaluate the indefinite integral
\[
\int x\sqrt{x^2+1}\,dx.
\]''',
            'a': r'''Use the substitution \(u=x^2+1\), so \(du=2x\,dx\) and \(x\,dx=\dfrac12\,du\).
\[
\int x\sqrt{x^2+1}\,dx=\frac12\int u^{1/2}\,du=\frac12\cdot\frac{2}{3}u^{3/2}+C=\frac13(x^2+1)^{3/2}+C.
\]
\[\boxed{\dfrac13(x^2+1)^{3/2}+C}\]''',
        },
        {
            'q': r'''Evaluate
\[
\int_0^1\frac{2x}{x^2+1}\,dx.
\]''',
            'a': r'''Let \(u=x^2+1\). Then \(du=2x\,dx\). When \(x=0\), \(u=1\); when \(x=1\), \(u=2\).
\[
\int_0^1\frac{2x}{x^2+1}\,dx=\int_1^2\frac{1}{u}\,du=\ln|u|\Big|_1^2=\ln2-\ln1=\ln2.
\]
\[\boxed{\ln 2}\]''',
        },
        {
            'q': r'''Use integration by parts to find
\[
\int x\,e^{2x}\,dx.
\]''',
            'a': r'''Take \(u=x\) and \(dv=e^{2x}\,dx\), so \(du=dx\) and \(v=\dfrac12 e^{2x}\).
\[
\int x\,e^{2x}\,dx=\frac{x}{2}e^{2x}-\int\frac12 e^{2x}\,dx=\frac{x}{2}e^{2x}-\frac14 e^{2x}+C=\frac{e^{2x}}{4}(2x-1)+C.
\]
\[\boxed{\dfrac{e^{2x}}{4}(2x-1)+C}\]''',
        },
        {
            'q': r'''Evaluate
\[
\int_0^{\pi/2} x\cos x\,dx.
\]''',
            'a': r'''Integrate by parts with \(u=x\), \(dv=\cos x\,dx\), so \(du=dx\), \(v=\sin x\).
\[
\int_0^{\pi/2} x\cos x\,dx=\bigl[x\sin x\bigr]_0^{\pi/2}-\int_0^{\pi/2}\sin x\,dx
=\frac{\pi}{2}-\bigl[-\cos x\bigr]_0^{\pi/2}=\frac{\pi}{2}-\bigl(0-(-1)\bigr)=\frac{\pi}{2}-1.
\]
\[\boxed{\dfrac{\pi}{2}-1}\]''',
        },
        {
            'q': r'''Evaluate
\[
\int\sin^3 x\cos^2 x\,dx.
\]''',
            'a': r'''Write \(\sin^3 x=\sin^2 x\sin x=(1-\cos^2 x)\sin x\) and set \(u=\cos x\), so \(du=-\sin x\,dx\).
\[
\int\sin^3 x\cos^2 x\,dx=\int(1-\cos^2 x)\cos^2 x\sin x\,dx=-\int(1-u^2)u^2\,du=-\int(u^2-u^4)\,du.
\]
\[
=-\frac{u^3}{3}+\frac{u^5}{5}+C=-\frac{\cos^3 x}{3}+\frac{\cos^5 x}{5}+C.
\]
\[\boxed{-\dfrac{\cos^3 x}{3}+\dfrac{\cos^5 x}{5}+C}\]''',
        },
        {
            'q': r'''Evaluate
\[
\int\cos^2 x\,dx.
\]''',
            'a': r'''Use the half-angle identity \(\cos^2 x=\dfrac{1+\cos 2x}{2}\).
\[
\int\cos^2 x\,dx=\int\frac{1+\cos 2x}{2}\,dx=\frac{x}{2}+\frac14\sin 2x+C=\frac{x}{2}+\frac12\sin x\cos x+C.
\]
\[\boxed{\dfrac{x}{2}+\dfrac14\sin 2x+C}\]''',
        },
        {
            'q': r'''Use a trigonometric substitution to evaluate
\[
\int\frac{1}{\sqrt{4-x^2}}\,dx.
\]''',
            'a': r'''Set \(x=2\sin\theta\), so \(dx=2\cos\theta\,d\theta\) and \(\sqrt{4-x^2}=2\cos\theta\) (with \(\cos\theta\ge0\)).
\[
\int\frac{1}{\sqrt{4-x^2}}\,dx=\int\frac{2\cos\theta}{2\cos\theta}\,d\theta=\int d\theta=\theta+C=\arcsin\!\Bigl(\frac{x}{2}\Bigr)+C.
\]
\[\boxed{\arcsin\!\bigl(\dfrac{x}{2}\bigr)+C}\]''',
        },
        {
            'q': r'''Evaluate the definite integral using a trigonometric substitution (or geometry)
\[
\int_0^2\sqrt{4-x^2}\,dx.
\]''',
            'a': r'''Let \(x=2\sin\theta\), so \(dx=2\cos\theta\,d\theta\) and \(\sqrt{4-x^2}=2\cos\theta\). Limits: \(x=0\Rightarrow\theta=0\); \(x=2\Rightarrow\theta=\pi/2\).
\[
\int_0^2\sqrt{4-x^2}\,dx=\int_0^{\pi/2}(2\cos\theta)(2\cos\theta)\,d\theta=4\int_0^{\pi/2}\cos^2\theta\,d\theta=4\int_0^{\pi/2}\frac{1+\cos2\theta}{2}\,d\theta
=2\Bigl[\theta+\frac12\sin2\theta\Bigr]_0^{\pi/2}=\pi.
\]
(Geometrically this is the area of a quarter-circle of radius \(2\).)
\[\boxed{\pi}\]''',
        },
    ],
}

T02 = {
    'id': 'T02',
    'kind': 'topic',
    'title': 'Partial Fractions & Improper Integrals',
    'weeks': 'W2',
    'blurb': 'Partial-fraction decompositions and improper integrals of Type I and Type II.',
    'questions': [
        {
            'q': r'''Decompose and integrate
\[
\int\frac{1}{(x-1)(x+2)}\,dx.
\]''',
            'a': r'''Write \(\dfrac{1}{(x-1)(x+2)}=\dfrac{A}{x-1}+\dfrac{B}{x+2}\). Clearing denominators: \(1=A(x+2)+B(x-1)\).
Setting \(x=1\) gives \(A=\dfrac13\); setting \(x=-2\) gives \(B=-\dfrac13\).
\[
\int\frac{1}{(x-1)(x+2)}\,dx=\frac13\int\frac{1}{x-1}\,dx-\frac13\int\frac{1}{x+2}\,dx=\frac13\ln\Bigl|\frac{x-1}{x+2}\Bigr|+C.
\]
\[\boxed{\dfrac13\ln\Bigl|\dfrac{x-1}{x+2}\Bigr|+C}\]''',
        },
        {
            'q': r'''Evaluate
\[
\int_0^1\frac{x+3}{(x+1)(x+2)}\,dx.
\]''',
            'a': r'''Decompose: \(\dfrac{x+3}{(x+1)(x+2)}=\dfrac{A}{x+1}+\dfrac{B}{x+2}\). Then \(x+3=A(x+2)+B(x+1)\).
\(x=-1\Rightarrow A=2\); \(x=-2\Rightarrow B=-1\). So the integrand is \(\dfrac{2}{x+1}-\dfrac{1}{x+2}\).
\[
\int_0^1\Bigl(\frac{2}{x+1}-\frac{1}{x+2}\Bigr)\,dx=\bigl[2\ln|x+1|-\ln|x+2|\bigr]_0^1
=(2\ln2-\ln3)-(2\ln1-\ln2)=2\ln2-\ln3+\ln2=3\ln2-\ln3=\ln\frac{8}{3}.
\]
\[\boxed{\ln\dfrac{8}{3}}\]''',
        },
        {
            'q': r'''Find
\[
\int\frac{1}{x(x-1)^2}\,dx.
\]''',
            'a': r'''Write \(\dfrac{1}{x(x-1)^2}=\dfrac{A}{x}+\dfrac{B}{x-1}+\dfrac{C}{(x-1)^2}\). Then \(1=A(x-1)^2+Bx(x-1)+Cx\).
\(x=0\Rightarrow A=1\); \(x=1\Rightarrow C=1\). Expanding and matching \(x\)-coefficients: \(B=-1\).
\[
\int\Bigl(\frac{1}{x}-\frac{1}{x-1}+\frac{1}{(x-1)^2}\Bigr)\,dx=\ln|x|-\ln|x-1|-\frac{1}{x-1}+C=\ln\Bigl|\frac{x}{x-1}\Bigr|-\frac{1}{x-1}+C.
\]
\[\boxed{\ln\Bigl|\dfrac{x}{x-1}\Bigr|-\dfrac{1}{x-1}+C}\]''',
        },
        {
            'q': r'''Evaluate
\[
\int\frac{x+1}{x^2+4}\,dx.
\]''',
            'a': r'''Split: \(\dfrac{x+1}{x^2+4}=\dfrac{x}{x^2+4}+\dfrac{1}{x^2+4}\). For the first term set \(u=x^2+4\), \(du=2x\,dx\).
\[
\int\frac{x}{x^2+4}\,dx=\frac12\ln(x^2+4),\qquad\int\frac{1}{x^2+4}\,dx=\frac12\arctan\frac{x}{2}.
\]
\[
\int\frac{x+1}{x^2+4}\,dx=\frac12\ln(x^2+4)+\frac12\arctan\frac{x}{2}+C.
\]
\[\boxed{\dfrac12\ln(x^2+4)+\dfrac12\arctan\dfrac{x}{2}+C}\]''',
        },
        {
            'q': r'''Determine whether the improper integral converges, and if so evaluate it:
\[
\int_1^\infty\frac{1}{x^2}\,dx.
\]''',
            'a': r'''This is Type I (infinite upper limit).
\[
\int_1^\infty\frac{1}{x^2}\,dx=\lim_{b\to\infty}\int_1^b x^{-2}\,dx=\lim_{b\to\infty}\Bigl[-\frac{1}{x}\Bigr]_1^b=\lim_{b\to\infty}\Bigl(-\frac{1}{b}+1\Bigr)=1.
\]
The limit is finite, so the integral converges.
\[\boxed{\text{converges to }1}\]''',
        },
        {
            'q': r'''Determine whether
\[
\int_1^\infty\frac{1}{x}\,dx
\]
converges or diverges.''',
            'a': r'''Type I improper integral:
\[
\int_1^\infty\frac{1}{x}\,dx=\lim_{b\to\infty}\bigl[\ln x\bigr]_1^b=\lim_{b\to\infty}(\ln b-\ln1)=\infty.
\]
The limit is infinite, so the integral diverges.
\[\boxed{\text{diverges}}\]''',
        },
        {
            'q': r'''Evaluate the Type II improper integral (or state that it diverges)
\[
\int_0^1\frac{1}{\sqrt{x}}\,dx.
\]''',
            'a': r'''The integrand blows up at \(x=0\). Write
\[
\int_0^1 x^{-1/2}\,dx=\lim_{a\to0^+}\int_a^1 x^{-1/2}\,dx=\lim_{a\to0^+}\bigl[2x^{1/2}\bigr]_a^1=\lim_{a\to0^+}(2-2\sqrt{a})=2.
\]
\[\boxed{\text{converges to }2}\]''',
        },
        {
            'q': r'''Does
\[
\int_0^1\frac{1}{x}\,dx
\]
converge or diverge? Justify.''',
            'a': r'''Singularity at \(x=0\) (Type II):
\[
\int_0^1\frac{1}{x}\,dx=\lim_{a\to0^+}\bigl[\ln x\bigr]_a^1=\lim_{a\to0^+}(0-\ln a)=\infty.
\]
Hence the integral diverges. (Compare with \(\int_0^1 x^{-p}\,dx\), which converges only for \(p&lt;1\).)
\[\boxed{\text{diverges}}\]''',
        },
    ],
}

T03 = {
    'id': 'T03',
    'kind': 'topic',
    'title': 'Numerical Integration',
    'weeks': 'W3',
    'blurb': 'Midpoint, Trapezoidal, and Simpson rules with error ideas and method comparison.',
    'questions': [
        {
            'q': r'''Approximate \(\displaystyle\int_0^2 x^2\,dx\) using the Midpoint Rule with \(n=4\).''',
            'a': r'''Here \(\Delta x=\dfrac{2-0}{4}=\dfrac12\). Subintervals \([0,0.5]\), \([0.5,1]\), \([1,1.5]\), \([1.5,2]\) have midpoints \(0.25,0.75,1.25,1.75\).
\[
M_4=\frac12\bigl[(0.25)^2+(0.75)^2+(1.25)^2+(1.75)^2\bigr]=\frac12(0.0625+0.5625+1.5625+3.0625)=\frac12\cdot5.25=2.625.
\]
\[\boxed{M_4=2.625}\]''',
        },
        {
            'q': r'''Approximate \(\displaystyle\int_0^2 x^2\,dx\) using the Trapezoidal Rule with \(n=4\).''',
            'a': r'''\(\Delta x=\dfrac12\). Sample points \(x_i=0,0.5,1,1.5,2\) give \(y_i=0,0.25,1,2.25,4\).
\[
T_4=\frac{\Delta x}{2}\bigl(y_0+2y_1+2y_2+2y_3+y_4\bigr)=\frac14\bigl(0+2(0.25)+2(1)+2(2.25)+4\bigr)=\frac14(0.5+2+4.5+4)=\frac{11}{4}=2.75.
\]
\[\boxed{T_4=2.75}\]''',
        },
        {
            'q': r'''Approximate \(\displaystyle\int_0^2 x^2\,dx\) using Simpson’s Rule with \(n=4\).''',
            'a': r'''With \(\Delta x=\dfrac12\) and \(y_i=0,0.25,1,2.25,4\),
\[
S_4=\frac{\Delta x}{3}\bigl(y_0+4y_1+2y_2+4y_3+y_4\bigr)=\frac{1}{6}\bigl(0+4(0.25)+2(1)+4(2.25)+4\bigr)=\frac{1}{6}(1+2+9+4)=\frac{16}{6}=\frac83.
\]
\[\boxed{S_4=\dfrac83}\]''',
        },
        {
            'q': r'''The exact value of \(\displaystyle\int_0^2 x^2\,dx\) is \(\dfrac83\). Compare your Midpoint (\(2.625\)), Trapezoidal (\(2.75\)), and Simpson (\(\dfrac83\)) approximations and comment.''',
            'a': r'''Exact value: \(\displaystyle\int_0^2 x^2\,dx=\bigl[\dfrac{x^3}{3}\bigr]_0^2=\dfrac83\approx2.666\ldots\).
Errors: Midpoint \(2.625-\dfrac83\approx-0.0417\); Trapezoidal \(2.75-\dfrac83\approx+0.0833\); Simpson is exact here.
For a quadratic, Simpson’s Rule (degree \(\le3\) polynomials exact) returns the true value. Trapezoidal overestimates a convex (\(f''&gt;0\)) integrand; Midpoint typically underestimates in that case, with roughly half the Trapezoidal error magnitude.
\[\boxed{\text{exact }\dfrac83;\ S_4\text{ exact; }|E_T|\approx2|E_M|}\]''',
        },
        {
            'q': r'''Approximate \(\displaystyle\int_0^3 (2x+1)\,dx\) using the Midpoint Rule with \(n=6\).''',
            'a': r'''\(\Delta x=\dfrac{3-0}{6}=\dfrac12\). Midpoints: \(0.25,0.75,1.25,1.75,2.25,2.75\).
\[
f(x)=2x+1\Rightarrow\text{values }1.5,2.5,3.5,4.5,5.5,6.5.
\]
\[
M_6=\frac12(1.5+2.5+3.5+4.5+5.5+6.5)=\frac12\cdot24=12.
\]
(The exact integral is also \(12\), as expected for a linear integrand under Midpoint.)
\[\boxed{M_6=12}\]''',
        },
        {
            'q': r'''Approximate \(\displaystyle\int_1^3 \dfrac{1}{x}\,dx\) using the Trapezoidal Rule with \(n=4\). Leave the answer as a decimal to 4 d.p.''',
            'a': r'''\(\Delta x=\dfrac{3-1}{4}=\dfrac12\). Points \(x=1,1.5,2,2.5,3\) give \(y=1,\dfrac23,\dfrac12,\dfrac25,\dfrac13\).
\[
T_4=\frac{1/2}{2}\Bigl(1+2\cdot\frac23+2\cdot\frac12+2\cdot\frac25+\frac13\Bigr)=\frac14\Bigl(1+\frac43+1+\frac45+\frac13\Bigr).
\]
\[
1+1+\frac43+\frac13+\frac45=2+\frac53+\frac45=\frac{30+25+12}{15}=\frac{67}{15},\quad T_4=\frac{67}{60}\approx1.1167.
\]
\[\boxed{T_4\approx1.1167}\]''',
        },
        {
            'q': r'''Approximate \(\displaystyle\int_0^{\pi} \sin x\,dx\) using Simpson’s Rule with \(n=6\). Give an exact simplified expression (or a 4 d.p. decimal).''',
            'a': r'''\(\Delta x=\dfrac{\pi}{6}\). Points \(x_k=k\pi/6\) for \(k=0,\ldots,6\): \(y=0,\dfrac12,\dfrac{\sqrt3}{2},1,\dfrac{\sqrt3}{2},\dfrac12,0\).
\[
S_6=\frac{\pi/6}{3}\Bigl(0+4\cdot\frac12+2\cdot\frac{\sqrt3}{2}+4\cdot1+2\cdot\frac{\sqrt3}{2}+4\cdot\frac12+0\Bigr)
=\frac{\pi}{18}\bigl(2+\sqrt3+4+\sqrt3+2\bigr)=\frac{\pi}{18}(8+2\sqrt3)=\frac{\pi(4+\sqrt3)}{9}.
\]
Numerically \(\approx2.0009\) (exact integral \(=2\)).
\[\boxed{S_6=\dfrac{\pi(4+\sqrt3)}{9}}\]''',
        },
        {
            'q': r'''The Trapezoidal error bound for \(\displaystyle\int_a^b f(x)\,dx\) with \(n\) subintervals is
\[
|E_T|\le\frac{(b-a)^3}{12n^2}\max_{[a,b]}|f''(x)|
\]
(when \(f''\) is continuous). For \(f(x)=e^x\) on \([0,1]\) with \(n=4\), find a bound on \(|E_T|\).''',
            'a': r'''Here \(f''(x)=e^x\), so on \([0,1]\) we have \(\max|f''|=e\). Also \(b-a=1\) and \(n=4\).
\[
|E_T|\le\frac{1^3}{12\cdot16}\,e=\frac{e}{192}\approx0.0142.
\]
So the Trapezoidal approximation with \(n=4\) is guaranteed to be within \(\dfrac{e}{192}\) of the true integral \(\int_0^1 e^x\,dx=e-1\).
\[\boxed{|E_T|\le\dfrac{e}{192}}\]''',
        },
    ],
}

T04 = {
    'id': 'T04',
    'kind': 'topic',
    'title': 'Polar Coordinates',
    'weeks': 'W4',
    'blurb': 'Polar–Cartesian conversion, cardioid sketches, polar area, and polar derivatives/tangents.',
    'questions': [
        {
            'q': r'''Convert the polar point \(\bigl(4,\dfrac{\pi}{3}\bigr)\) to Cartesian coordinates.''',
            'a': r'''Use \(x=r\cos\theta\) and \(y=r\sin\theta\).
\[
x=4\cos\frac{\pi}{3}=4\cdot\frac12=2,\qquad y=4\sin\frac{\pi}{3}=4\cdot\frac{\sqrt3}{2}=2\sqrt3.
\]
\[\boxed{(2,\,2\sqrt3)}\]''',
        },
        {
            'q': r'''Convert the Cartesian point \((-1,\sqrt3)\) to polar form with \(r&gt;0\) and \(0\le\theta&lt;2\pi\).''',
            'a': r'''\(r=\sqrt{(-1)^2+(\sqrt3)^2}=\sqrt{1+3}=2\). The point is in Quadrant II, so
\[
\theta=\pi+\arctan\Bigl(\frac{\sqrt3}{-1}\Bigr)=\pi-\frac{\pi}{3}=\frac{2\pi}{3}
\]
(using \(\arctan(\sqrt3)=\pi/3\) and adjusting for the quadrant).
\[\boxed{\bigl(2,\,\dfrac{2\pi}{3}\bigr)}\]''',
        },
        {
            'q': r'''Describe the curve \(r=2(1+\cos\theta)\). Sketch key features: intercepts and symmetry.''',
            'a': r'''This is a cardioid. Since \(\cos(-\theta)=\cos\theta\), the curve is symmetric about the polar axis.
When \(\theta=0\), \(r=4\); when \(\theta=\pi\), \(r=0\) (cusp at the origin); when \(\theta=\pm\pi/2\), \(r=2\).
It is a heart-shaped loop extending to \(r=4\) on the positive \(x\)-axis and touching the origin.
\[\boxed{\text{cardioid, symmetric about }+x\text{-axis, cusp at origin}}\]''',
        },
        {
            'q': r'''Find the area enclosed by the cardioid \(r=1+\cos\theta\).''',
            'a': r'''Area \(A=\dfrac12\int_0^{2\pi}r^2\,d\theta=\dfrac12\int_0^{2\pi}(1+\cos\theta)^2\,d\theta\).
\[
(1+\cos\theta)^2=1+2\cos\theta+\cos^2\theta=1+2\cos\theta+\frac{1+\cos2\theta}{2}=\frac32+2\cos\theta+\frac12\cos2\theta.
\]
\[
A=\frac12\int_0^{2\pi}\Bigl(\frac32+2\cos\theta+\frac12\cos2\theta\Bigr)\,d\theta=\frac12\Bigl[\frac32\theta+2\sin\theta+\frac14\sin2\theta\Bigr]_0^{2\pi}=\frac12\cdot3\pi=\frac{3\pi}{2}.
\]
\[\boxed{\dfrac{3\pi}{2}}\]''',
        },
        {
            'q': r'''Find the area of one petal of the rose \(r=3\sin2\theta\).''',
            'a': r'''Petals occur where \(r=0\) at consecutive zeros of \(\sin2\theta\). One petal runs over \(\theta\in[0,\pi/2]\) (actually \(2\theta\in[0,\pi]\), so \(\theta\in[0,\pi/2]\)).
\[
A=\frac12\int_0^{\pi/2}(3\sin2\theta)^2\,d\theta=\frac92\int_0^{\pi/2}\sin^2 2\theta\,d\theta=\frac92\int_0^{\pi/2}\frac{1-\cos4\theta}{2}\,d\theta
=\frac94\Bigl[\theta-\frac14\sin4\theta\Bigr]_0^{\pi/2}=\frac94\cdot\frac{\pi}{2}=\frac{9\pi}{8}.
\]
\[\boxed{\dfrac{9\pi}{8}}\]''',
        },
        {
            'q': r'''For \(r=2\cos\theta\), find \(\dfrac{dy}{dx}\) at \(\theta=\dfrac{\pi}{4}\).''',
            'a': r'''In polar form,
\[
\frac{dy}{dx}=\frac{\dfrac{dr}{d\theta}\sin\theta+r\cos\theta}{\dfrac{dr}{d\theta}\cos\theta-r\sin\theta}.
\]
Here \(r=2\cos\theta\) and \(\dfrac{dr}{d\theta}=-2\sin\theta\). At \(\theta=\pi/4\), \(r=\sqrt2\).
Numerator: \((-2\sin\frac{\pi}{4})\sin\frac{\pi}{4}+r\cos\frac{\pi}{4}=-2\cdot\frac12+\sqrt2\cdot\frac{\sqrt2}{2}=-1+1=0\).
Denominator: \((-2\sin\frac{\pi}{4})\cos\frac{\pi}{4}-r\sin\frac{\pi}{4}=-1-\sqrt2\cdot\frac{\sqrt2}{2}=-1-1=-2\neq0\).
So \(\dfrac{dy}{dx}=0\) (horizontal tangent).
\[\boxed{0}\]''',
        },
        {
            'q': r'''For \(r=2+2\cos\theta\), find \(\dfrac{dy}{dx}\) at \(\theta=\dfrac{\pi}{2}\).''',
            'a': r'''Use
\[
\frac{dy}{dx}=\frac{r'\sin\theta+r\cos\theta}{r'\cos\theta-r\sin\theta},\qquad r'= -2\sin\theta.
\]
At \(\theta=\pi/2\): \(r=2\), \(r'=-2\).
Numerator: \((-2)(1)+2\cdot0=-2\). Denominator: \((-2)(0)-2\cdot1=-2\).
\[
\frac{dy}{dx}=\frac{-2}{-2}=1.
\]
\[\boxed{1}\]''',
        },
        {
            'q': r'''Find the area that lies inside both \(r=2\sin\theta\) and \(r=2\cos\theta\).''',
            'a': r'''Intersection: \(2\sin\theta=2\cos\theta\Rightarrow\theta=\dfrac{\pi}{4}\) (in the first quadrant, where both are positive). The common region is
\[
A=2\cdot\frac12\int_0^{\pi/4}(2\sin\theta)^2\,d\theta=\int_0^{\pi/4}4\sin^2\theta\,d\theta=4\int_0^{\pi/4}\frac{1-\cos2\theta}{2}\,d\theta
=2\Bigl[\theta-\frac12\sin2\theta\Bigr]_0^{\pi/4}=2\Bigl(\frac{\pi}{4}-\frac12\Bigr)=\frac{\pi}{2}-1.
\]
(Equivalently, symmetry about \(\theta=\pi/4\) with one integral over the circle \(r=2\sin\theta\).)
\[\boxed{\dfrac{\pi}{2}-1}\]''',
        },
    ],
}

T05 = {
    'id': 'T05',
    'kind': 'topic',
    'title': 'Parametric Curves',
    'weeks': 'W4A',
    'blurb': 'Parametric derivatives, arc length, area under parametric curves, and eliminating the parameter.',
    'questions': [
        {
            'q': r'''For \(x=t^2\), \(y=t^3-3t\), find \(\dfrac{dy}{dx}\) in terms of \(t\).''',
            'a': r'''\(\dfrac{dx}{dt}=2t\) and \(\dfrac{dy}{dt}=3t^2-3\), so
\[
\frac{dy}{dx}=\frac{dy/dt}{dx/dt}=\frac{3t^2-3}{2t}=\frac{3(t^2-1)}{2t},\qquad t\neq0.
\]
\[\boxed{\dfrac{3(t^2-1)}{2t}\ (t\neq0)}\]''',
        },
        {
            'q': r'''For the same curve \(x=t^2\), \(y=t^3-3t\), find \(\dfrac{d^2y}{dx^2}\) at \(t=2\).''',
            'a': r'''From Q1, \(\dfrac{dy}{dx}=\dfrac{3(t^2-1)}{2t}\). Differentiate with respect to \(t\) and divide by \(\dfrac{dx}{dt}\):
\[
\frac{d}{dt}\Bigl(\frac{dy}{dx}\Bigr)=\frac{d}{dt}\Bigl(\frac{3t}{2}-\frac{3}{2t}\Bigr)=\frac{3}{2}+\frac{3}{2t^2},\qquad\frac{d^2y}{dx^2}=\frac{\frac{3}{2}+\frac{3}{2t^2}}{2t}=\frac{3(t^2+1)}{4t^3}.
\]
At \(t=2\): \(\dfrac{3(4+1)}{4\cdot8}=\dfrac{15}{32}\).
\[\boxed{\dfrac{15}{32}}\]''',
        },
        {
            'q': r'''Find the arc length of \(x=\cos t\), \(y=\sin t\) for \(0\le t\le\pi\).''',
            'a': r'''\(x'=-\sin t\), \(y'=\cos t\), so \(\sqrt{(x')^2+(y')^2}=\sqrt{\sin^2 t+\cos^2 t}=1\).
\[
L=\int_0^\pi 1\,dt=\pi.
\]
(This is a semicircle of radius \(1\).)
\[\boxed{\pi}\]''',
        },
        {
            'q': r'''Find the area under the parametric curve \(x=t^2\), \(y=t\) from \(t=0\) to \(t=2\) (i.e. between the curve, the \(x\)-axis, and the corresponding vertical lines).''',
            'a': r'''Area \(A=\displaystyle\int_{t=a}^{t=b} y(t)\,x'(t)\,dt\) when \(x\) is increasing. Here \(x'=2t\), \(y=t\).
\[
A=\int_0^2 t\cdot2t\,dt=2\int_0^2 t^2\,dt=2\cdot\frac{t^3}{3}\Big|_0^2=\frac{16}{3}.
\]
(Eliminating: \(y=\sqrt{x}\) for \(t\ge0\), and \(\int_0^4\sqrt{x}\,dx=\dfrac23 x^{3/2}\big|_0^4=\dfrac{16}{3}\).)
\[\boxed{\dfrac{16}{3}}\]''',
        },
        {
            'q': r'''Eliminate the parameter: \(x=2\cos t\), \(y=3\sin t\).''',
            'a': r'''\(\dfrac{x}{2}=\cos t\) and \(\dfrac{y}{3}=\sin t\), so
\[
\Bigl(\frac{x}{2}\Bigr)^2+\Bigl(\frac{y}{3}\Bigr)^2=\cos^2 t+\sin^2 t=1.
\]
This is the ellipse \(\dfrac{x^2}{4}+\dfrac{y^2}{9}=1\).
\[\boxed{\dfrac{x^2}{4}+\dfrac{y^2}{9}=1}\]''',
        },
        {
            'q': r'''For \(x=e^t\), \(y=te^{-t}\), find \(\dfrac{dy}{dx}\) in terms of \(t\).''',
            'a': r'''\(x'=e^t\), \(y'=e^{-t}-te^{-t}=e^{-t}(1-t)\).
\[
\frac{dy}{dx}=\frac{e^{-t}(1-t)}{e^t}=(1-t)e^{-2t}.
\]
\[\boxed{(1-t)e^{-2t}}\]''',
        },
        {
            'q': r'''Find the arc length of \(x=t^3\), \(y=\dfrac{3t^2}{2}\) from \(t=0\) to \(t=1\).''',
            'a': r'''\(x'=3t^2\), \(y'=3t\), so
\[
\sqrt{(x')^2+(y')^2}=\sqrt{9t^4+9t^2}=3|t|\sqrt{t^2+1}.
\]
For \(t\in[0,1]\),
\[
L=\int_0^1 3t\sqrt{t^2+1}\,dt.
\]
Let \(u=t^2+1\), \(du=2t\,dt\): \(L=\dfrac32\int_1^2 u^{1/2}\,du=\dfrac32\cdot\dfrac23\bigl[u^{3/2}\bigr]_1^2=(2\sqrt2-1)\).
\[\boxed{2\sqrt2-1}\]''',
        },
        {
            'q': r'''Eliminate the parameter for \(x=t+1\), \(y=t^2+2t\), and state the Cartesian equation.''',
            'a': r'''From \(x=t+1\), we get \(t=x-1\). Substitute:
\[
y=(x-1)^2+2(x-1)=x^2-2x+1+2x-2=x^2-1.
\]
So the curve is the parabola \(y=x^2-1\).
\[\boxed{y=x^2-1}\]''',
        },
    ],
}

T06 = {
    'id': 'T06',
    'kind': 'topic',
    'title': 'Areas & Volumes',
    'weeks': 'W5',
    'blurb': 'Area between curves; volumes by disk, washer, shell, and known cross-sections.',
    'questions': [
        {
            'q': r'''Find the area enclosed by \(y=x^2\) and \(y=2x\).''',
            'a': r'''Intersection: \(x^2=2x\Rightarrow x(x-2)=0\), so \(x=0,2\). For \(x\in[0,2]\), \(2x\ge x^2\).
\[
A=\int_0^2(2x-x^2)\,dx=\Bigl[x^2-\frac{x^3}{3}\Bigr]_0^2=4-\frac83=\frac43.
\]
\[\boxed{\dfrac43}\]''',
        },
        {
            'q': r'''Find the area between \(y=\sin x\) and \(y=\cos x\) from \(x=0\) to \(x=\dfrac{\pi}{4}\).''',
            'a': r'''On \([0,\pi/4]\), \(\cos x\ge\sin x\).
\[
A=\int_0^{\pi/4}(\cos x-\sin x)\,dx=\bigl[\sin x+\cos x\bigr]_0^{\pi/4}
=\Bigl(\frac{\sqrt2}{2}+\frac{\sqrt2}{2}\Bigr)-(0+1)=\sqrt2-1.
\]
\[\boxed{\sqrt2-1}\]''',
        },
        {
            'q': r'''The region under \(y=\sqrt{x}\) from \(x=0\) to \(x=4\) is rotated about the \(x\)-axis. Find the volume (disk method).''',
            'a': r'''Radius \(R=\sqrt{x}\), so
\[
V=\pi\int_0^4 (\sqrt{x})^2\,dx=\pi\int_0^4 x\,dx=\pi\Bigl[\frac{x^2}{2}\Bigr]_0^4=8\pi.
\]
\[\boxed{8\pi}\]''',
        },
        {
            'q': r'''The region bounded by \(y=x\) and \(y=x^2\) is rotated about the \(x\)-axis. Find the volume using washers.''',
            'a': r'''Intersections at \(x=0,1\). Outer radius \(R=x\), inner radius \(r=x^2\).
\[
V=\pi\int_0^1\bigl(x^2-(x^2)^2\bigr)\,dx=\pi\int_0^1(x^2-x^4)\,dx=\pi\Bigl[\frac{x^3}{3}-\frac{x^5}{5}\Bigr]_0^1=\pi\Bigl(\frac13-\frac15\Bigr)=\frac{2\pi}{15}.
\]
\[\boxed{\dfrac{2\pi}{15}}\]''',
        },
        {
            'q': r'''The region bounded by \(y=x\) and \(y=x^2\) is rotated about the \(y\)-axis. Find the volume using cylindrical shells.''',
            'a': r'''Shells: radius \(x\), height \(x-x^2\), \(x\) from \(0\) to \(1\).
\[
V=\int_0^1 2\pi x(x-x^2)\,dx=2\pi\int_0^1(x^2-x^3)\,dx=2\pi\Bigl[\frac{x^3}{3}-\frac{x^4}{4}\Bigr]_0^1=2\pi\Bigl(\frac13-\frac14\Bigr)=\frac{\pi}{6}.
\]
\[\boxed{\dfrac{\pi}{6}}\]''',
        },
        {
            'q': r'''Verify the previous volume by the washer method about the \(y\)-axis (express \(x\) in terms of \(y\)).''',
            'a': r'''Curves: \(x=y\) and \(x=\sqrt{y}\) for \(y\in[0,1]\). Outer radius \(\sqrt{y}\), inner radius \(y\).
\[
V=\pi\int_0^1\bigl((\sqrt{y})^2-y^2\bigr)\,dy=\pi\int_0^1(y-y^2)\,dy=\pi\Bigl[\frac{y^2}{2}-\frac{y^3}{3}\Bigr]_0^1=\pi\Bigl(\frac12-\frac13\Bigr)=\frac{\pi}{6}.
\]
Agrees with the shell result.
\[\boxed{\dfrac{\pi}{6}\ \text{(matches shells)}}\]''',
        },
        {
            'q': r'''The base of a solid is the region bounded by \(y=x^2\) and \(y=1\). Cross-sections perpendicular to the \(y\)-axis are squares with side in the base. Find the volume.''',
            'a': r'''For fixed \(y\in[0,1]\), \(x\) runs from \(-\sqrt{y}\) to \(\sqrt{y}\), so the base segment has length \(2\sqrt{y}\). Square side \(=2\sqrt{y}\), area \(=4y\).
\[
V=\int_0^1 4y\,dy=4\cdot\frac{y^2}{2}\Big|_0^1=2.
\]
\[\boxed{2}\]''',
        },
        {
            'q': r'''The base of a solid is the disk \(x^2+y^2\le1\). Cross-sections perpendicular to the \(x\)-axis are equilateral triangles with side in the base. Find the volume.''',
            'a': r'''At fixed \(x\in[-1,1]\), the chord length (side of the triangle) is \(2\sqrt{1-x^2}\). Area of an equilateral triangle of side \(s\) is \(\dfrac{\sqrt3}{4}s^2\).
\[
V=\int_{-1}^1\frac{\sqrt3}{4}\bigl(2\sqrt{1-x^2}\bigr)^2\,dx=\int_{-1}^1\frac{\sqrt3}{4}\cdot4(1-x^2)\,dx=\sqrt3\int_{-1}^1(1-x^2)\,dx
=2\sqrt3\int_0^1(1-x^2)\,dx=2\sqrt3\Bigl[x-\frac{x^3}{3}\Bigr]_0^1=\frac{4\sqrt3}{3}.
\]
\[\boxed{\dfrac{4\sqrt3}{3}}\]''',
        },
    ],
}

T07 = {
    'id': 'T07',
    'kind': 'topic',
    'title': 'Arc Length & Surfaces',
    'weeks': 'W6',
    'blurb': 'Arc length for y=f(x) and x=g(y); surfaces of revolution about the x- or y-axis.',
    'questions': [
        {
            'q': r'''Find the arc length of \(y=\dfrac{x^3}{6}+\dfrac{1}{2x}\) from \(x=1\) to \(x=2\).''',
            'a': r'''\(y'=\dfrac{x^2}{2}-\dfrac{1}{2x^2}\), so
\[
1+(y')^2=1+\Bigl(\frac{x^2}{2}-\frac{1}{2x^2}\Bigr)^2=\Bigl(\frac{x^2}{2}+\frac{1}{2x^2}\Bigr)^2
\]
(after expanding). Hence \(\sqrt{1+(y')^2}=\dfrac{x^2}{2}+\dfrac{1}{2x^2}\) (positive on \([1,2]\)).
\[
L=\int_1^2\Bigl(\frac{x^2}{2}+\frac{1}{2x^2}\Bigr)\,dx=\Bigl[\frac{x^3}{6}-\frac{1}{2x}\Bigr]_1^2=\Bigl(\frac43-\frac14\Bigr)-\Bigl(\frac16-\frac12\Bigr)=\frac{13}{12}-\Bigl(-\frac13\Bigr)=\frac{13}{12}+\frac{4}{12}=\frac{17}{12}.
\]
\[\boxed{\dfrac{17}{12}}\]''',
        },
        {
            'q': r'''Find the arc length of \(x=\dfrac{y^3}{3}+\dfrac{1}{4y}\) from \(y=1\) to \(y=3\).''',
            'a': r'''\(x'=\dfrac{dx}{dy}=y^2-\dfrac{1}{4y^2}\). Then
\[
\sqrt{1+(x')^2}=\sqrt{1+\Bigl(y^2-\frac{1}{4y^2}\Bigr)^2}=y^2+\frac{1}{4y^2}
\]
(on the given interval).
\[
L=\int_1^3\Bigl(y^2+\frac{1}{4y^2}\Bigr)\,dy=\Bigl[\frac{y^3}{3}-\frac{1}{4y}\Bigr]_1^3=\Bigl(9-\frac{1}{12}\Bigr)-\Bigl(\frac13-\frac14\Bigr)=\frac{107}{12}-\frac{1}{12}=\frac{106}{12}=\frac{53}{6}.
\]
\[\boxed{\dfrac{53}{6}}\]''',
        },
        {
            'q': r'''Find the surface area generated by rotating \(y=\sqrt{x}\) about the \(x\)-axis from \(x=0\) to \(x=4\).''',
            'a': r'''\(y'=\dfrac{1}{2\sqrt{x}}\), so \(\sqrt{1+(y')^2}=\sqrt{1+\dfrac{1}{4x}}=\sqrt{\dfrac{4x+1}{4x}}=\dfrac{\sqrt{4x+1}}{2\sqrt{x}}\).
\[
S=2\pi\int_0^4 y\sqrt{1+(y')^2}\,dx=2\pi\int_0^4\sqrt{x}\cdot\frac{\sqrt{4x+1}}{2\sqrt{x}}\,dx=\pi\int_0^4\sqrt{4x+1}\,dx.
\]
Let \(u=4x+1\), \(du=4\,dx\): \(S=\dfrac{\pi}{4}\int_1^{17}u^{1/2}\,du=\dfrac{\pi}{4}\cdot\dfrac23\bigl[u^{3/2}\bigr]_1^{17}=\dfrac{\pi}{6}(17^{3/2}-1)=\dfrac{\pi}{6}(17\sqrt{17}-1)\).
\[\boxed{\dfrac{\pi}{6}(17\sqrt{17}-1)}\]''',
        },
        {
            'q': r'''Find the surface area when \(y=x^3\) from \(x=0\) to \(x=1\) is rotated about the \(x\)-axis.''',
            'a': r'''\(y'=3x^2\), so
\[
S=2\pi\int_0^1 x^3\sqrt{1+9x^4}\,dx.
\]
Let \(u=1+9x^4\), \(du=36x^3\,dx\): when \(x=0\), \(u=1\); when \(x=1\), \(u=10\).
\[
S=2\pi\cdot\frac{1}{36}\int_1^{10}u^{1/2}\,du=\frac{\pi}{18}\cdot\frac{2}{3}\bigl[u^{3/2}\bigr]_1^{10}=\frac{\pi}{27}(10^{3/2}-1)=\frac{\pi}{27}(10\sqrt{10}-1).
\]
\[\boxed{\dfrac{\pi}{27}(10\sqrt{10}-1)}\]''',
        },
        {
            'q': r'''Find the arc length of \(y=\ln(\cos x)\) from \(x=0\) to \(x=\dfrac{\pi}{4}\).''',
            'a': r'''\(y'=-\tan x\), so \(1+(y')^2=1+\tan^2 x=\sec^2 x\) and \(\sqrt{1+(y')^2}=\sec x\) on \([0,\pi/4]\).
\[
L=\int_0^{\pi/4}\sec x\,dx=\bigl[\ln|\sec x+\tan x|\bigr]_0^{\pi/4}=\ln(\sqrt2+1)-\ln(1+0)=\ln(1+\sqrt2).
\]
\[\boxed{\ln(1+\sqrt2)}\]''',
        },
        {
            'q': r'''The curve \(x=\sqrt{4-y^2}\) from \(y=0\) to \(y=2\) (right semicircle) is rotated about the \(y\)-axis. Find the surface area.''',
            'a': r'''This generates a hemisphere of radius \(2\). Formula: \(S=2\pi\int_c^d x\sqrt{1+(x')^2}\,dy\).
From \(x=\sqrt{4-y^2}\), \(x'=\dfrac{-y}{\sqrt{4-y^2}}\), so \(1+(x')^2=\dfrac{4}{4-y^2}\) and \(\sqrt{1+(x')^2}=\dfrac{2}{x}\).
\[
S=2\pi\int_0^2 x\cdot\frac{2}{x}\,dy=4\pi\int_0^2 dy=8\pi.
\]
(Yes: hemisphere surface area \(2\pi R^2=2\pi\cdot4=8\pi\).)
\[\boxed{8\pi}\]''',
        },
        {
            'q': r'''Find the surface area generated by rotating \(y=x\) from \(x=0\) to \(x=1\) about the \(x\)-axis.''',
            'a': r'''Here \(y'=1\), so \(\sqrt{1+(y')^2}=\sqrt2\).
\[
S=2\pi\int_0^1 y\sqrt{1+(y')^2}\,dx=2\pi\int_0^1 x\sqrt2\,dx=2\pi\sqrt2\cdot\frac12=\pi\sqrt2.
\]
(Geometrically this is a cone frustum / cone lateral area check: slant \(\sqrt2\), average radius \(\tfrac12\), area \(\pi\sqrt2\).)
\[\boxed{\pi\sqrt2}\]''',
        },
        {
            'q': r'''Find the surface area generated by rotating \(y=x^2\) from \(x=0\) to \(x=1\) about the \(y\)-axis.''',
            'a': r'''About the \(y\)-axis with \(y=f(x)\): \(S=2\pi\int_a^b x\sqrt{1+(y')^2}\,dx\). Here \(y'=2x\).
\[
S=2\pi\int_0^1 x\sqrt{1+4x^2}\,dx.
\]
Let \(u=1+4x^2\), \(du=8x\,dx\). When \(x=0\), \(u=1\); when \(x=1\), \(u=5\).
\[
S=2\pi\cdot\frac18\int_1^5 u^{1/2}\,du=\frac{\pi}{4}\cdot\frac23\bigl[u^{3/2}\bigr]_1^5=\frac{\pi}{6}(5^{3/2}-1)=\frac{\pi}{6}(5\sqrt5-1).
\]
\[\boxed{\dfrac{\pi}{6}(5\sqrt5-1)}\]''',
        },
    ],
}

T08 = {
    'id': 'T08',
    'kind': 'topic',
    'title': 'First-Order DEs',
    'weeks': 'W7–8A',
    'blurb': 'Separable, linear (integrating factor), exact, homogeneous, Bernoulli, and one IVP application.',
    'questions': [
        {
            'q': r'''Solve the separable equation \(\dfrac{dy}{dx}=xy\) with \(y(0)=2\).''',
            'a': r'''Separate (for \(y\neq0\)): \(\dfrac{dy}{y}=x\,dx\). Integrate: \(\ln|y|=\dfrac{x^2}{2}+C_1\), so \(y=Ce^{x^2/2}\).
\(y(0)=2\Rightarrow C=2\). Thus \(y=2e^{x^2/2}\).
\[\boxed{y=2e^{x^2/2}}\]''',
        },
        {
            'q': r'''Solve \(\dfrac{dy}{dx}+2y=e^{-x}\) (linear first-order).''',
            'a': r'''Integrating factor \(\mu=e^{\int2\,dx}=e^{2x}\). Multiply through:
\[
e^{2x}y'+2e^{2x}y=e^{x}\implies\frac{d}{dx}(ye^{2x})=e^{x}\implies ye^{2x}=e^{x}+C\implies y=e^{-x}+Ce^{-2x}.
\]
\[\boxed{y=e^{-x}+Ce^{-2x}}\]''',
        },
        {
            'q': r'''Solve the IVP \(\dfrac{dy}{dx}-\dfrac{1}{x}y=x\), \(y(1)=2\) (assume \(x&gt;0\)).''',
            'a': r'''Linear; \(\mu=e^{\int-\frac1x\,dx}=e^{-\ln x}=\dfrac1x\). Multiply:
\[
\frac1x y'-\frac1{x^2}y=1\implies\frac{d}{dx}\Bigl(\frac{y}{x}\Bigr)=1\implies\frac{y}{x}=x+C\implies y=x^2+Cx.
\]
\(y(1)=2\Rightarrow1+C=2\Rightarrow C=1\). So \(y=x^2+x\).
\[\boxed{y=x^2+x}\]''',
        },
        {
            'q': r'''Show that \(M\,dx+N\,dy=0\) with \(M=2xy+1\), \(N=x^2+3y^2\) is exact, and solve it.''',
            'a': r'''\(M_y=2x\) and \(N_x=2x\), so exact. Find \(F\) with \(F_x=M\): \(F=x^2 y+x+h(y)\).
Then \(F_y=x^2+h'(y)=N=x^2+3y^2\Rightarrow h'=3y^2\Rightarrow h=y^3\).
Implicit solution: \(x^2 y+x+y^3=C\).
\[\boxed{x^2 y+x+y^3=C}\]''',
        },
        {
            'q': r'''Solve the homogeneous equation \(\dfrac{dy}{dx}=\dfrac{x+y}{x-y}\).''',
            'a': r'''Set \(v=\dfrac{y}{x}\), so \(y=vx\) and \(\dfrac{dy}{dx}=v+x\dfrac{dv}{dx}\). Then
\[
v+x\frac{dv}{dx}=\frac{1+v}{1-v}\implies x\frac{dv}{dx}=\frac{1+v}{1-v}-v=\frac{1+v-v+v^2}{1-v}=\frac{1+v^2}{1-v}.
\]
\[
\frac{1-v}{1+v^2}\,dv=\frac{dx}{x}\implies\int\frac{1-v}{1+v^2}\,dv=\ln|x|+C_1.
\]
\[
\arctan v-\frac12\ln(1+v^2)=\ln|x|+C_1.
\]
Back-substitute \(v=y/x\) (and absorb logs) for the implicit general solution.
\[\boxed{\arctan\dfrac{y}{x}-\dfrac12\ln\Bigl(1+\dfrac{y^2}{x^2}\Bigr)=\ln|x|+C}\]''',
        },
        {
            'q': r'''Solve the Bernoulli equation \(y'+y=xy^3\).''',
            'a': r'''Bernoulli with \(n=3\). Set \(z=y^{-2}\) (so \(z'=-2y^{-3}y'\)). Divide the DE by \(y^3\):
\[
y^{-3}y'+y^{-2}=x\implies -\frac12 z'+z=x\implies z'-2z=-2x.
\]
Integrating factor \(e^{-2x}\): \(\dfrac{d}{dx}(ze^{-2x})=-2xe^{-2x}\). Integrate by parts:
\[
ze^{-2x}=\int-2xe^{-2x}\,dx=xe^{-2x}+\frac12 e^{-2x}+C\implies z=x+\frac12+Ce^{2x}.
\]
Thus \(y^{-2}=x+\dfrac12+Ce^{2x}\), so \(y=\pm\bigl(x+\dfrac12+Ce^{2x}\bigr)^{-1/2}\).
\[\boxed{y^{-2}=x+\dfrac12+Ce^{2x}}\]''',
        },
        {
            'q': r'''A tank holds \(100\) L of water with \(5\) kg of salt. Brine with \(0.2\) kg/L salt enters at \(4\) L/min; the well-mixed solution exits at \(4\) L/min. Find the amount of salt \(Q(t)\) (kg) at time \(t\) minutes, and \(\lim_{t\to\infty}Q(t)\).''',
            'a': r'''Volume stays \(100\) L. Rate in: \(0.2\cdot4=0.8\) kg/min. Rate out: \(\dfrac{Q}{100}\cdot4=\dfrac{Q}{25}\) kg/min.
\[
\frac{dQ}{dt}=0.8-\frac{Q}{25},\qquad Q(0)=5.
\]
Linear: \(Q'+Q/25=0.8\). IF \(e^{t/25}\): \(Qe^{t/25}=0.8\cdot25\,e^{t/25}+C=20e^{t/25}+C\), so \(Q=20+Ce^{-t/25}\).
\(Q(0)=5\Rightarrow C=-15\). Thus \(Q(t)=20-15e^{-t/25}\), and \(\lim_{t\to\infty}Q(t)=20\).
\[\boxed{Q(t)=20-15e^{-t/25};\ \lim Q=20\text{ kg}}\]''',
        },
        {
            'q': r'''Newton’s law of cooling: \(\dfrac{dT}{dt}=-k(T-T_a)\). A body cools from \(90^\circ\mathrm{C}\) to \(60^\circ\mathrm{C}\) in \(10\) minutes in a \(20^\circ\mathrm{C}\) room. Find \(T(t)\) and the temperature at \(t=20\) min.''',
            'a': r'''Separate: \(\dfrac{dT}{T-20}=-k\,dt\Rightarrow\ln|T-20|=-kt+C_1\Rightarrow T-20=Ae^{-kt}\).
\(T(0)=90\Rightarrow A=70\), so \(T=20+70e^{-kt}\). At \(t=10\), \(T=60\): \(40=70e^{-10k}\Rightarrow e^{-10k}=\dfrac47\Rightarrow k=\dfrac1{10}\ln\dfrac74\).
\[
T(t)=20+70\exp\Bigl(-\frac{t}{10}\ln\frac74\Bigr)=20+70\Bigl(\frac47\Bigr)^{t/10}.
\]
At \(t=20\): \(T=20+70\cdot\bigl(\dfrac47\bigr)^2=20+70\cdot\dfrac{16}{49}=20+\dfrac{160}{7}=\dfrac{300}{7}\approx42.86^\circ\mathrm{C}\).
\[\boxed{T=20+70\bigl(\tfrac47\bigr)^{t/10};\ T(20)=\tfrac{300}{7}\,^\circ\mathrm{C}}\]''',
        },
    ],
}

T09 = {
    'id': 'T09',
    'kind': 'topic',
    'title': 'Second-Order DEs & SHM',
    'weeks': 'W9',
    'blurb': 'Constant-coefficient homogeneous ODEs, undetermined coefficients, IVPs, and simple harmonic motion.',
    'questions': [
        {
            'q': r'''Solve \(y''-5y'+6y=0\).''',
            'a': r'''Characteristic equation: \(r^2-5r+6=0\Rightarrow(r-2)(r-3)=0\), so \(r=2,3\) (distinct real roots).
\[
y=c_1 e^{2x}+c_2 e^{3x}.
\]
\[\boxed{y=c_1 e^{2x}+c_2 e^{3x}}\]''',
        },
        {
            'q': r'''Solve \(y''+6y'+9y=0\).''',
            'a': r'''\(r^2+6r+9=(r+3)^2=0\), repeated root \(r=-3\).
\[
y=(c_1+c_2 x)e^{-3x}.
\]
\[\boxed{y=(c_1+c_2 x)e^{-3x}}\]''',
        },
        {
            'q': r'''Solve \(y''+4y'+13y=0\).''',
            'a': r'''\(r^2+4r+13=0\Rightarrow r=\dfrac{-4\pm\sqrt{16-52}}{2}=-2\pm3i\). Complex roots \(\alpha\pm\beta i\) with \(\alpha=-2\), \(\beta=3\).
\[
y=e^{-2x}(c_1\cos3x+c_2\sin3x).
\]
\[\boxed{y=e^{-2x}(c_1\cos3x+c_2\sin3x)}\]''',
        },
        {
            'q': r'''Find a particular solution of \(y''-y'-2y=e^{3x}\) by undetermined coefficients.''',
            'a': r'''Homogeneous roots: \(r^2-r-2=(r-2)(r+1)=0\), so \(r=2,-1\). Since \(e^{3x}\) is not a homogeneous solution, try \(y_p=Ae^{3x}\).
\[
y_p'=3Ae^{3x},\ y_p''=9Ae^{3x}\implies(9A-3A-2A)e^{3x}=e^{3x}\implies4A=1\implies A=\frac14.
\]
\[\boxed{y_p=\dfrac14 e^{3x}}\]''',
        },
        {
            'q': r'''Solve the IVP \(y''+y=0\), \(y(0)=1\), \(y'(0)=0\).''',
            'a': r'''Characteristic \(r^2+1=0\Rightarrow r=\pm i\). General solution \(y=c_1\cos x+c_2\sin x\).
\(y(0)=1\Rightarrow c_1=1\). \(y'=-c_1\sin x+c_2\cos x\), so \(y'(0)=c_2=0\). Thus \(y=\cos x\).
\[\boxed{y=\cos x}\]''',
        },
        {
            'q': r'''A mass–spring system (no damping) satisfies \(x''+\omega^2 x=0\) with \(\omega=4\). If \(x(0)=3\) and \(x'(0)=0\), write \(x(t)\) and state the natural frequency (rad/s) and period.''',
            'a': r'''General solution \(x=A\cos4t+B\sin4t\). \(x(0)=3\Rightarrow A=3\); \(x'=-4A\sin4t+4B\cos4t\), \(x'(0)=4B=0\Rightarrow B=0\).
So \(x(t)=3\cos4t\). Natural (circular) frequency \(\omega=4\) rad/s; period \(T=\dfrac{2\pi}{\omega}=\dfrac{\pi}{2}\).
\[\boxed{x=3\cos4t;\ \omega=4;\ T=\pi/2}\]''',
        },
        {
            'q': r'''Write \(x(t)=3\cos2t+4\sin2t\) in the amplitude–phase form \(R\cos(\omega t-\phi)\) (with \(R&gt;0\) and \(\phi\in[0,2\pi)\)).''',
            'a': r'''Here \(\omega=2\). Amplitude \(R=\sqrt{3^2+4^2}=5\). We need \(\cos\phi=\dfrac{3}{5}\), \(\sin\phi=\dfrac{4}{5}\) so that
\[
R\cos(\omega t-\phi)=R(\cos\omega t\cos\phi+\sin\omega t\sin\phi)=3\cos2t+4\sin2t.
\]
Thus \(\phi=\arctan\dfrac45\) (first quadrant).
\[\boxed{x=5\cos(2t-\phi),\ \phi=\arctan\dfrac45}\]''',
        },
        {
            'q': r'''Briefly explain resonance for the forced undamped oscillator \(x''+\omega_0^2 x=F_0\cos\omega t\). What happens when \(\omega=\omega_0\)?''',
            'a': r'''For \(\omega\neq\omega_0\), a particular solution is of the form \(A\cos\omega t\) with \(A=\dfrac{F_0}{\omega_0^2-\omega^2}\). As \(\omega\to\omega_0\), \(|A|\to\infty\).
When \(\omega=\omega_0\), undetermined coefficients requires \(x_p=t(A\cos\omega_0 t+B\sin\omega_0 t)\); the factor of \(t\) means the oscillation amplitude grows without bound (ideal undamped resonance). In real systems, damping keeps the peak finite but large near \(\omega\approx\omega_0\).
\[\boxed{\text{when }\omega=\omega_0,\ \text{amplitude grows like }t\text{ (undamped resonance)}}\]''',
        },
    ],
}

PACKS = {
    't01-integration': T01,
    't02-partial-improper': T02,
    't03-numerical': T03,
    't04-polar': T04,
    't05-parametric': T05,
    't06-areas-volumes': T06,
    't07-arc-surfaces': T07,
    't08-first-order-de': T08,
    't09-second-order-shm': T09,
}
