#!/usr/bin/env python3
"""Set 4 and Set 5 packs for DPEN022 calc lessons (appended after set3)."""


def extend_groups(_set, LD_GROUPS, INT_GROUPS):
    """Append set4 and set5 to every LD and INT week group."""
    LD_GROUPS['2d']['sets'].extend(_ld_2d(_set))
    LD_GROUPS['3a']['sets'].extend(_ld_3a(_set))
    LD_GROUPS['3b']['sets'].extend(_ld_3b(_set))
    LD_GROUPS['3c']['sets'].extend(_ld_3c(_set))
    LD_GROUPS['3d']['sets'].extend(_ld_3d(_set))
    LD_GROUPS['4a']['sets'].extend(_ld_4a(_set))
    INT_GROUPS['4d']['sets'].extend(_int_4d(_set))
    INT_GROUPS['5a']['sets'].extend(_int_5a(_set))
    INT_GROUPS['5b']['sets'].extend(_int_5b(_set))
    INT_GROUPS['5c']['sets'].extend(_int_5c(_set))
    INT_GROUPS['5d']['sets'].extend(_int_5d(_set))
    INT_GROUPS['6a']['sets'].extend(_int_6a(_set))


# ---------------------------------------------------------------------------
# Limits + Diff
# ---------------------------------------------------------------------------

def _ld_2d(_set):
    return [
_set('w2d-set4', '2D Set 4', 'WEEK 2D · SET 4 OF 5', 'Student Notes Week 2D (filled-in)',
     'Limits requiring rationalisation',
     r'From Week 2D: multi-step \(\frac00\) limits using rationalisation, cubic factorisation, and algebraic rewrite.',
     [
         r'Substitution that yields \(\dfrac00\) needs algebra: multiply by a conjugate, factor a cubic, or rewrite radicals.',
         r'For expressions with square roots, multiply top and bottom by the conjugate so factors of \((x-a)\) appear.',
         r'For \(x^3-a^3=(x-a)(x^2+ax+a^2)\). Cancel the common factor, then substitute.',
     ],
     r'\(\displaystyle\lim_{x\to 4}\dfrac{\sqrt{x}-2}{x-4}\): multiply by \(\sqrt{x}+2\) to get \(\dfrac{1}{\sqrt{x}+2}\to\dfrac14\).',
     [r'\(\frac00\): rewrite before substituting.', 'Conjugate for nested radicals.', r'Factor \(x^3-a^3\) when useful.', 'Cancel only common factors.', 'Finish with direct substitution.'],
     [r'\(\displaystyle\lim_{x\to a}\dfrac{\sqrt{x}-\sqrt{a}}{x-a}=\dfrac{1}{2\sqrt{a}}\)', r'\(x^3-a^3=(x-a)(x^2+ax+a^2)\)', r'Conjugate: \((\sqrt{u}-\sqrt{v})(\sqrt{u}+\sqrt{v})=u-v\)'],
     [
         (r'\(\displaystyle\lim_{x\to 4}\dfrac{\sqrt{x}-2}{x-4}\)',
          r'Substitute gives \(\frac00\). Rationalise: multiply by \(\sqrt{x}+2\).'
          r'\[\lim_{x\to 4}\dfrac{\sqrt{x}-2}{x-4}=\lim_{x\to 4}\dfrac{x-4}{(x-4)(\sqrt{x}+2)}=\lim_{x\to 4}\dfrac{1}{\sqrt{x}+2}=\dfrac{1}{4}.\]'
          r'\[\boxed{\dfrac{1}{4}}\]'),
         (r'\(\displaystyle\lim_{x\to 9}\dfrac{x-9}{\sqrt{x}-3}\)',
          r'Substitute gives \(\frac00\). Multiply by \(\sqrt{x}+3\).'
          r'\[\lim_{x\to 9}\dfrac{x-9}{\sqrt{x}-3}=\lim_{x\to 9}\dfrac{(x-9)(\sqrt{x}+3)}{x-9}=\lim_{x\to 9}(\sqrt{x}+3)=6.\]'
          r'\[\boxed{6}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{\sqrt{1+x}-1}{x}\)',
          r'Substitute gives \(\frac00\). Rationalise the numerator.'
          r'\[\lim_{x\to 0}\dfrac{\sqrt{1+x}-1}{x}=\lim_{x\to 0}\dfrac{(1+x)-1}{x(\sqrt{1+x}+1)}=\lim_{x\to 0}\dfrac{1}{\sqrt{1+x}+1}=\dfrac{1}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'\(\displaystyle\lim_{x\to 2}\dfrac{x^3-8}{x-2}\)',
          r'Substitute gives \(\frac00\). Factor the difference of cubes.'
          r'\[\lim_{x\to 2}\dfrac{x^3-8}{x-2}=\lim_{x\to 2}\dfrac{(x-2)(x^2+2x+4)}{x-2}=\lim_{x\to 2}(x^2+2x+4)=12.\]'
          r'\[\boxed{12}\]'),
         (r'\(\displaystyle\lim_{x\to -1}\dfrac{x^3+1}{x+1}\)',
          r'Substitute gives \(\frac00\). Factor \(x^3+1=(x+1)(x^2-x+1)\).'
          r'\[\lim_{x\to -1}\dfrac{x^3+1}{x+1}=\lim_{x\to -1}(x^2-x+1)=1+1+1=3.\]'
          r'\[\boxed{3}\]'),
         (r'\(\displaystyle\lim_{x\to 1}\dfrac{x^3-1}{x^2-1}\)',
          r'Substitute gives \(\frac00\). Factor top and bottom.'
          r'\[\lim_{x\to 1}\dfrac{(x-1)(x^2+x+1)}{(x-1)(x+1)}=\lim_{x\to 1}\dfrac{x^2+x+1}{x+1}=\dfrac{3}{2}.\]'
          r'\[\boxed{\dfrac{3}{2}}\]'),
         (r'\(\displaystyle\lim_{x\to 3}\dfrac{\sqrt{x+1}-2}{x-3}\)',
          r'Substitute gives \(\frac00\). Rationalise.'
          r'\[\lim_{x\to 3}\dfrac{\sqrt{x+1}-2}{x-3}=\lim_{x\to 3}\dfrac{(x+1)-4}{(x-3)(\sqrt{x+1}+2)}=\lim_{x\to 3}\dfrac{1}{\sqrt{x+1}+2}=\dfrac{1}{4}.\]'
          r'\[\boxed{\dfrac{1}{4}}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{\sqrt{4+x}-2}{x}\)',
          r'Substitute gives \(\frac00\). Rationalise.'
          r'\[\lim_{x\to 0}\dfrac{\sqrt{4+x}-2}{x}=\lim_{x\to 0}\dfrac{(4+x)-4}{x(\sqrt{4+x}+2)}=\lim_{x\to 0}\dfrac{1}{\sqrt{4+x}+2}=\dfrac{1}{4}.\]'
          r'\[\boxed{\dfrac{1}{4}}\]'),
         (r'\(\displaystyle\lim_{x\to 2}\dfrac{x^3-3x^2+2x}{x-2}\)',
          r'Substitute gives \(\frac00\). Factor \(x(x^2-3x+2)=x(x-1)(x-2)\).'
          r'\[\lim_{x\to 2}\dfrac{x(x-1)(x-2)}{x-2}=\lim_{x\to 2}x(x-1)=2.\]'
          r'\[\boxed{2}\]'),
         (r'\(\displaystyle\lim_{h\to 0}\dfrac{\sqrt{9+h}-3}{h}\)',
          r'Substitute gives \(\frac00\). Rationalise (difference quotient for \(\sqrt{x}\) at \(9\)).'
          r'\[\lim_{h\to 0}\dfrac{\sqrt{9+h}-3}{h}=\lim_{h\to 0}\dfrac{h}{h(\sqrt{9+h}+3)}=\dfrac{1}{6}.\]'
          r'\[\boxed{\dfrac{1}{6}}\]'),
         (r'\(\displaystyle\lim_{x\to 1}\dfrac{x^4-1}{x-1}\)',
          r'Substitute gives \(\frac00\). Factor \(x^4-1=(x-1)(x^3+x^2+x+1)\).'
          r'\[\lim_{x\to 1}\dfrac{(x-1)(x^3+x^2+x+1)}{x-1}=1+1+1+1=4.\]'
          r'\[\boxed{4}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{1-\sqrt{1-x}}{x}\)',
          r'Substitute gives \(\frac00\). Rationalise.'
          r'\[\lim_{x\to 0}\dfrac{1-\sqrt{1-x}}{x}=\lim_{x\to 0}\dfrac{1-(1-x)}{x(1+\sqrt{1-x})}=\lim_{x\to 0}\dfrac{1}{1+\sqrt{1-x}}=\dfrac{1}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'\(\displaystyle\lim_{x\to -2}\dfrac{x^3+8}{x^2-4}\)',
          r'Substitute gives \(\frac00\). Factor cubes and difference of squares.'
          r'\[\lim_{x\to -2}\dfrac{(x+2)(x^2-2x+4)}{(x-2)(x+2)}=\lim_{x\to -2}\dfrac{x^2-2x+4}{x-2}=\dfrac{4+4+4}{-4}=-3.\]'
          r'\[\boxed{-3}\]'),
         (r'\(\displaystyle\lim_{x\to 5}\dfrac{\sqrt{x}-\sqrt{5}}{x-5}\)',
          r'Substitute gives \(\frac00\). Rationalise.'
          r'\[\lim_{x\to 5}\dfrac{\sqrt{x}-\sqrt{5}}{x-5}=\lim_{x\to 5}\dfrac{1}{\sqrt{x}+\sqrt{5}}=\dfrac{1}{2\sqrt{5}}.\]'
          r'\[\boxed{\dfrac{1}{2\sqrt{5}}}\]'),
         (r'\(\displaystyle\lim_{x\to 1}\dfrac{x^3-3x+2}{x^2-1}\)',
          r'Substitute gives \(\frac00\). Factor: \(x^3-3x+2=(x-1)^2(x+2)\) and \(x^2-1=(x-1)(x+1)\).'
          r'\[\lim_{x\to 1}\dfrac{(x-1)^2(x+2)}{(x-1)(x+1)}=\lim_{x\to 1}\dfrac{(x-1)(x+2)}{x+1}=\dfrac{0\cdot 3}{2}=0.\]'
          r'\[\boxed{0}\]'),
     ], formulas_title='Key limit results'),
_set('w2d-set5', '2D Set 5', 'WEEK 2D · SET 5 OF 5', 'Student Notes Week 2D (filled-in)',
     'One-sided limits, infinity & squeeze forms',
     r'From Week 2D: exam-style practice with one-sided limits, limits at infinity, and \(\sin x/x\) composites.',
     [
         r'One-sided limits \(x\to a^\pm\) matter near jumps and vertical asymptotes.',
         r'For limits at infinity, dominant terms (or divide by the highest power) decide the value.',
         r'Use \(\displaystyle\lim_{\theta\to 0}\dfrac{\sin\theta}{\theta}=1\) after rewriting composite arguments.',
     ],
     r'\(\displaystyle\lim_{x\to 0}\dfrac{\sin(3x)}{x}=3\cdot\lim\dfrac{\sin(3x)}{3x}=3\).',
     [r'Check left and right separately when needed.', r'Divide by highest power for \(x\to\infty\).', r'Rewrite \(\sin(kx)/x\) using \(\sin u/u\).', r'Squeeze: sandwich between known bounds.', r'State \(\pm\infty\) when unbounded.'],
     [r'\(\displaystyle\lim_{\theta\to 0}\dfrac{\sin\theta}{\theta}=1\)', r'\(\displaystyle\lim_{x\to\infty}\dfrac{\sin x}{x}=0\)', r'One-sided: \(x\to a^+\) and \(x\to a^-\)'],
     [
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{\sin(5x)}{x}\)',
          r'Rewrite using \(\sin u/u\) with \(u=5x\).'
          r'\[\lim_{x\to 0}\dfrac{\sin(5x)}{x}=\lim_{x\to 0}5\cdot\dfrac{\sin(5x)}{5x}=5\cdot 1=5.\]'
          r'\[\boxed{5}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{\sin(2x)}{\sin(3x)}\)',
          r'Write each sine over its argument.'
          r'\[\lim_{x\to 0}\dfrac{\sin(2x)}{\sin(3x)}=\lim_{x\to 0}\dfrac{\sin(2x)}{2x}\cdot\dfrac{3x}{\sin(3x)}\cdot\dfrac{2}{3}=\dfrac{2}{3}.\]'
          r'\[\boxed{\dfrac{2}{3}}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{1-\cos x}{x}\)',
          r'Multiply by \(1+\cos x\), or use \(\dfrac{1-\cos x}{x}=\dfrac{\sin^2 x}{x(1+\cos x)}\).'
          r'\[\lim_{x\to 0}\dfrac{1-\cos x}{x}=\lim_{x\to 0}\dfrac{\sin^2 x}{x(1+\cos x)}=\lim_{x\to 0}\sin x\cdot\dfrac{\sin x}{x}\cdot\dfrac{1}{1+\cos x}=0.\]'
          r'\[\boxed{0}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{\tan x}{x}\)',
          r'Write \(\tan x=\dfrac{\sin x}{\cos x}\).'
          r'\[\lim_{x\to 0}\dfrac{\tan x}{x}=\lim_{x\to 0}\dfrac{\sin x}{x}\cdot\dfrac{1}{\cos x}=1\cdot 1=1.\]'
          r'\[\boxed{1}\]'),
         (r'\(\displaystyle\lim_{x\to 0^+}\dfrac{|x|}{x}\)',
          r'For \(x>0\), \(|x|=x\).'
          r'\[\lim_{x\to 0^+}\dfrac{|x|}{x}=\lim_{x\to 0^+}\dfrac{x}{x}=1.\]'
          r'\[\boxed{1}\]'),
         (r'\(\displaystyle\lim_{x\to 0^-}\dfrac{|x|}{x}\)',
          r'For \(x<0\), \(|x|=-x\).'
          r'\[\lim_{x\to 0^-}\dfrac{|x|}{x}=\lim_{x\to 0^-}\dfrac{-x}{x}=-1.\]'
          r'\[\boxed{-1}\]'),
         (r'\(\displaystyle\lim_{x\to\infty}\dfrac{2x^3-x}{5x^3+4}\)',
          r'Divide top and bottom by \(x^3\).'
          r'\[\lim_{x\to\infty}\dfrac{2-1/x^2}{5+4/x^3}=\dfrac{2}{5}.\]'
          r'\[\boxed{\dfrac{2}{5}}\]'),
         (r'\(\displaystyle\lim_{x\to -\infty}\dfrac{3x^2+1}{x^2-x}\)',
          r'Divide by \(x^2\).'
          r'\[\lim_{x\to -\infty}\dfrac{3+1/x^2}{1-1/x}=3.\]'
          r'\[\boxed{3}\]'),
         (r'\(\displaystyle\lim_{x\to 1^+}\dfrac{x+2}{x-1}\)',
          r'As \(x\to 1^+\), numerator \(\to 3\) and denominator \(\to 0^+\).'
          r'\[\lim_{x\to 1^+}\dfrac{x+2}{x-1}=+\infty.\]'
          r'\[\boxed{+\infty}\]'),
         (r'\(\displaystyle\lim_{x\to 1^-}\dfrac{x+2}{x-1}\)',
          r'As \(x\to 1^-\), denominator \(\to 0^-\).'
          r'\[\lim_{x\to 1^-}\dfrac{x+2}{x-1}=-\infty.\]'
          r'\[\boxed{-\infty}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{\sin x}{x\cos x}\)',
          r'Split the fraction.'
          r'\[\lim_{x\to 0}\dfrac{\sin x}{x\cos x}=\lim_{x\to 0}\dfrac{\sin x}{x}\cdot\dfrac{1}{\cos x}=1.\]'
          r'\[\boxed{1}\]'),
         (r'\(\displaystyle\lim_{x\to\infty}\left(\sqrt{x^2+4x}-x\right)\)',
          r'Rationalise (or factor \(x\) out of the square root for \(x>0\)).'
          r'\[\lim_{x\to\infty}\left(\sqrt{x^2+4x}-x\right)=\lim_{x\to\infty}\dfrac{4x}{\sqrt{x^2+4x}+x}=\lim_{x\to\infty}\dfrac{4}{\sqrt{1+4/x}+1}=2.\]'
          r'\[\boxed{2}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{\sin(x^2)}{x}\)',
          r'Write \(\dfrac{\sin(x^2)}{x}=x\cdot\dfrac{\sin(x^2)}{x^2}\).'
          r'\[\lim_{x\to 0}x\cdot\dfrac{\sin(x^2)}{x^2}=0\cdot 1=0.\]'
          r'\[\boxed{0}\]'),
         (r'\(\displaystyle\lim_{x\to\infty}\dfrac{x\sin x}{x^2+1}\)',
          r'\(|x\sin x|\le|x|\) and \(\dfrac{|x|}{x^2+1}\to 0\), so by squeeze the limit is \(0\).'
          r'\[\left|\dfrac{x\sin x}{x^2+1}\right|\le\dfrac{|x|}{x^2+1}\to 0\Rightarrow\lim_{x\to\infty}\dfrac{x\sin x}{x^2+1}=0.\]'
          r'\[\boxed{0}\]'),
         (r'\(\displaystyle\lim_{x\to 0}\dfrac{x}{\sin(4x)}\)',
          r'Rewrite using \(\sin(4x)/(4x)\).'
          r'\[\lim_{x\to 0}\dfrac{x}{\sin(4x)}=\lim_{x\to 0}\dfrac{1}{4}\cdot\dfrac{4x}{\sin(4x)}=\dfrac{1}{4}.\]'
          r'\[\boxed{\dfrac{1}{4}}\]'),
     ], formulas_title='Key limit results'),
    ]


def _ld_3a(_set):
    return [
_set('w3a-set4', '3A Set 4', 'WEEK 3A · SET 4 OF 5', 'Student Notes Week 3A (filled-in)',
     'Awkward powers, roots and negative exponents',
     r'From Week 3A: differentiate fractional and negative powers using the power rule after rewriting.',
     [
         r'Rewrite roots and reciprocals as powers: \(\sqrt[n]{x}=x^{1/n}\), \(\dfrac{1}{x^k}=x^{-k}\).',
         r'Then apply \(\dfrac{d}{dx}x^n=nx^{n-1}\) and constant/sum rules.',
         r'Simplify the answer to a neat radical or fraction form when requested.',
     ],
     r'\(\dfrac{d}{dx}x^{-3}=-3x^{-4}=-\dfrac{3}{x^4}\); \(\dfrac{d}{dx}\sqrt[3]{x}=\dfrac{1}{3}x^{-2/3}\).',
     [r'Rewrite before differentiating.', r'Power rule for all real \(n\) used here.', r'Simplify negatives and fractions.', 'Constant multiples still apply.', 'Check by rewriting back.'],
     [r'\(\dfrac{d}{dx}x^n=nx^{n-1}\)', r'\(\dfrac{d}{dx}\sqrt{x}=\dfrac{1}{2\sqrt{x}}\)', r'\(\dfrac{d}{dx}x^{-1}=-x^{-2}\)'],
     [
         (r'\(\dfrac{d}{dx}\!\left(x^{-4}\right)\)',
          r'Power rule with \(n=-4\).'
          r'\[\dfrac{d}{dx}x^{-4}=-4x^{-5}=-\dfrac{4}{x^5}.\]'
          r'\[\boxed{-\dfrac{4}{x^5}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{1}{x^3}\right)\)',
          r'Write \(\dfrac{1}{x^3}=x^{-3}\).'
          r'\[\dfrac{d}{dx}x^{-3}=-3x^{-4}=-\dfrac{3}{x^4}.\]'
          r'\[\boxed{-\dfrac{3}{x^4}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\sqrt[3]{x}\right)\)',
          r'Write \(\sqrt[3]{x}=x^{1/3}\).'
          r'\[\dfrac{d}{dx}x^{1/3}=\dfrac{1}{3}x^{-2/3}=\dfrac{1}{3x^{2/3}}.\]'
          r'\[\boxed{\dfrac{1}{3x^{2/3}}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(x^{5/2}\right)\)',
          r'Power rule with \(n=\dfrac{5}{2}\).'
          r'\[\dfrac{d}{dx}x^{5/2}=\dfrac{5}{2}x^{3/2}.\]'
          r'\[\boxed{\dfrac{5}{2}x^{3/2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{3}{\sqrt{x}}\right)\)',
          r'Write \(\dfrac{3}{\sqrt{x}}=3x^{-1/2}\).'
          r'\[\dfrac{d}{dx}(3x^{-1/2})=3\cdot\left(-\dfrac{1}{2}\right)x^{-3/2}=-\dfrac{3}{2}x^{-3/2}.\]'
          r'\[\boxed{-\dfrac{3}{2x^{3/2}}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(4x^{-2}+x^{1/2}\right)\)',
          r'Differentiate term by term.'
          r'\[\dfrac{d}{dx}(4x^{-2}+x^{1/2})=-8x^{-3}+\dfrac{1}{2}x^{-1/2}=-\dfrac{8}{x^3}+\dfrac{1}{2\sqrt{x}}.\]'
          r'\[\boxed{-\dfrac{8}{x^3}+\dfrac{1}{2\sqrt{x}}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(x\sqrt{x}\right)\)',
          r'Write \(x\sqrt{x}=x^{3/2}\).'
          r'\[\dfrac{d}{dx}x^{3/2}=\dfrac{3}{2}x^{1/2}=\dfrac{3}{2}\sqrt{x}.\]'
          r'\[\boxed{\dfrac{3}{2}\sqrt{x}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{x^2+1}{x}\right)\)',
          r'Split: \(\dfrac{x^2+1}{x}=x+x^{-1}\).'
          r'\[\dfrac{d}{dx}(x+x^{-1})=1-x^{-2}=1-\dfrac{1}{x^2}.\]'
          r'\[\boxed{1-\dfrac{1}{x^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(2x^{7/3}\right)\)',
          r'Constant multiple and power rule.'
          r'\[\dfrac{d}{dx}(2x^{7/3})=2\cdot\dfrac{7}{3}x^{4/3}=\dfrac{14}{3}x^{4/3}.\]'
          r'\[\boxed{\dfrac{14}{3}x^{4/3}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{5}{x^2}-\dfrac{1}{x}\right)\)',
          r'Write as \(5x^{-2}-x^{-1}\).'
          r'\[\dfrac{d}{dx}(5x^{-2}-x^{-1})=-10x^{-3}+x^{-2}=-\dfrac{10}{x^3}+\dfrac{1}{x^2}.\]'
          r'\[\boxed{-\dfrac{10}{x^3}+\dfrac{1}{x^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\sqrt{x^3}\right)\)',
          r'For \(x\ge 0\), \(\sqrt{x^3}=x^{3/2}\).'
          r'\[\dfrac{d}{dx}x^{3/2}=\dfrac{3}{2}x^{1/2}.\]'
          r'\[\boxed{\dfrac{3}{2}\sqrt{x}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(x^{-1/2}+3x\right)\)',
          r'Term by term.'
          r'\[\dfrac{d}{dx}(x^{-1/2}+3x)=-\dfrac{1}{2}x^{-3/2}+3.\]'
          r'\[\boxed{-\dfrac{1}{2}x^{-3/2}+3}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{1}{2x^5}\right)\)',
          r'Write \(\dfrac{1}{2}x^{-5}\).'
          r'\[\dfrac{d}{dx}\!\left(\dfrac{1}{2}x^{-5}\right)=\dfrac{1}{2}(-5)x^{-6}=-\dfrac{5}{2x^6}.\]'
          r'\[\boxed{-\dfrac{5}{2x^6}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(6x^{2/5}\right)\)',
          r'Power rule.'
          r'\[\dfrac{d}{dx}(6x^{2/5})=6\cdot\dfrac{2}{5}x^{-3/5}=\dfrac{12}{5}x^{-3/5}.\]'
          r'\[\boxed{\dfrac{12}{5}x^{-3/5}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{x^3-2}{x^2}\right)\)',
          r'Split: \(x-2x^{-2}\).'
          r'\[\dfrac{d}{dx}(x-2x^{-2})=1+4x^{-3}=1+\dfrac{4}{x^3}.\]'
          r'\[\boxed{1+\dfrac{4}{x^3}}\]'),
     ]),
_set('w3a-set5', '3A Set 5', 'WEEK 3A · SET 5 OF 5', 'Student Notes Week 3A (filled-in)',
     'First principles, interpretation & tangents',
     r'From Week 3A: exam-style practice linking first principles, gradient meaning, and tangent equations with the power rule.',
     [
         r'The derivative definition \(f^{\prime}(a)=\displaystyle\lim_{h\to 0}\dfrac{f(a+h)-f(a)}{h}\) recovers slopes without memorised rules.',
         r'Once \(f^{\prime}\) is known, interpret increase/decrease and write tangent lines \(y-y_1=m(x-x_1)\).',
         r'Use the power rule for efficient tangent calculations on polynomials.',
     ],
     r"For \(f(x)=x^2\) at \(x=3\): \(m=6\), point \((3,9)\), tangent \(y-9=6(x-3)\).",
     [r'First principles: limit of difference quotient.', r"Tangent slope \(=f^{\prime}(a)\).", 'Point–gradient form.', r'Sign of \(f^{\prime}\) shows increase/decrease.', 'Power rule speeds polynomial work.'],
     [r"\(f^{\prime}(a)=\displaystyle\lim_{h\to 0}\dfrac{f(a+h)-f(a)}{h}\)", r'\(y-y_1=m(x-x_1)\)', r'\(\dfrac{d}{dx}x^n=nx^{n-1}\)'],
     [
         (r"Using first principles, find \(f^{\prime}(2)\) for \(f(x)=x^2\).",
          r'Form the difference quotient and take \(h\to 0\).'
          r'\[f^{\prime}(2)=\lim_{h\to 0}\dfrac{(2+h)^2-4}{h}=\lim_{h\to 0}\dfrac{4h+h^2}{h}=\lim_{h\to 0}(4+h)=4.\]'
          r'\[\boxed{4}\]'),
         (r"Using first principles, find \(f^{\prime}(1)\) for \(f(x)=3x\).",
          r'\[\lim_{h\to 0}\dfrac{3(1+h)-3}{h}=\lim_{h\to 0}\dfrac{3h}{h}=3.\]'
          r'\[\boxed{3}\]'),
         (r"Using first principles, find \(f^{\prime}(0)\) for \(f(x)=x^3\).",
          r'\[\lim_{h\to 0}\dfrac{h^3-0}{h}=\lim_{h\to 0}h^2=0.\]'
          r'\[\boxed{0}\]'),
         (r"\(f(x)=x^2-4x\); find the equation of the tangent at \(x=3\).",
          r'\(f(3)=-3\), \(f^{\prime}(x)=2x-4\), so \(m=2\).'
          r'\[y+3=2(x-3)\Rightarrow y=2x-9.\]'
          r'\[\boxed{y=2x-9}\]'),
         (r"\(f(x)=x^3\); equation of the tangent at \(x=-1\).",
          r'\(f(-1)=-1\), \(f^{\prime}(x)=3x^2\), \(m=3\).'
          r'\[y+1=3(x+1)\Rightarrow y=3x+2.\]'
          r'\[\boxed{y=3x+2}\]'),
         (r"\(f(x)=\sqrt{x}\); find \(f^{\prime}(4)\) and interpret the sign.",
          r'\(f^{\prime}(x)=\dfrac{1}{2\sqrt{x}}\), so \(f^{\prime}(4)=\dfrac{1}{4}>0\): \(f\) is increasing at \(x=4\).'
          r'\[\boxed{\dfrac{1}{4}\ \text{(increasing)}}\]'),
         (r"\(f(x)=x^2+1\); find average gradient on \([1,3]\) and compare with \(f^{\prime}(2)\).",
          r'Average: \(\dfrac{f(3)-f(1)}{2}=\dfrac{10-2}{2}=4\). Also \(f^{\prime}(2)=4\).'
          r'\[\boxed{\text{both equal }4}\]'),
         (r"\(s(t)=t^2-6t\); find velocity at \(t=4\) and say whether the particle is moving forward.",
          r'\(v(t)=s^{\prime}(t)=2t-6\), so \(v(4)=2>0\): moving in the positive direction.'
          r'\[\boxed{v(4)=2\ \text{(forward)}}\]'),
         (r"\(f(x)=2x^3-3x\); find \(x\) where the tangent is horizontal.",
          r'\(f^{\prime}(x)=6x^2-3=0\Rightarrow x^2=\dfrac12\Rightarrow x=\pm\dfrac{1}{\sqrt{2}}\).'
          r'\[\boxed{x=\pm\dfrac{1}{\sqrt{2}}}\]'),
         (r"\(f(x)=x^4\); equation of the tangent at \(x=1\).",
          r'\(f(1)=1\), \(m=4\).'
          r'\[y-1=4(x-1)\Rightarrow y=4x-3.\]'
          r'\[\boxed{y=4x-3}\]'),
         (r"Explain why \(f^{\prime}(a)=0\) does not by itself prove a local max or min.",
          r'A horizontal tangent can also be a point of inflection (e.g. \(f(x)=x^3\) at \(0\)). Need further tests or the second derivative.'
          r'\[\boxed{\text{could be inflection; need more info}}\]'),
         (r"\(f(x)=5-x^2\); is \(f\) decreasing at \(x=2\)?",
          r'\(f^{\prime}(x)=-2x\), so \(f^{\prime}(2)=-4<0\): yes, decreasing.'
          r'\[\boxed{\text{yes (slope }-4)}\]'),
         (r"\(f(x)=x^2+3x\); find the \(y\)-intercept of the tangent at \(x=1\).",
          r'\(f(1)=4\), \(m=5\), line \(y-4=5(x-1)\Rightarrow y=5x-1\). Intercept \(-1\).'
          r'\[\boxed{-1}\]'),
         (r"Using first principles outline: show \(f^{\prime}(x)=2x\) for \(f(x)=x^2\).",
          r'\[\lim_{h\to 0}\dfrac{(x+h)^2-x^2}{h}=\lim_{h\to 0}\dfrac{2xh+h^2}{h}=2x.\]'
          r'\[\boxed{f^{\prime}(x)=2x}\]'),
         (r"\(f(x)=\dfrac{1}{x}\); equation of the tangent at \(x=2\).",
          r'\(f(2)=\dfrac12\), \(f^{\prime}(x)=-x^{-2}\), \(m=-\dfrac14\).'
          r'\[y-\dfrac12=-\dfrac14(x-2)\Rightarrow y=-\dfrac14 x+1.\]'
          r'\[\boxed{y=-\dfrac{1}{4}x+1}\]'),
     ]),
    ]


def _ld_3b(_set):
    return [
_set('w3b-set4', '3B Set 4', 'WEEK 3B · SET 4 OF 5', 'Student Notes Week 3B (filled-in)',
     'Products of three factors & product with powers',
     r'From Week 3B: multi-step product rule with three factors or a power factor needing the chain rule.',
     [
         r'For three factors \(uvw\), \((uvw)^{\prime}=u^{\prime}vw+uv^{\prime}w+uvw^{\prime}\).',
         r'Often group as \((uv)w\) and apply the product rule twice.',
         r'When a factor is \((ax+b)^n\), combine product with chain rule.',
     ],
     r'\(\dfrac{d}{dx}[x(x+1)(x+2)]=(x+1)(x+2)+x(x+2)+x(x+1)\).',
     ['Three-factor product expands to three terms.', 'Group factors if helpful.', 'Chain rule on powered factors.', 'Factor common terms at the end.', 'Check by expanding then differentiating.'],
     [r"\((uvw)^{\prime}=u^{\prime}vw+uv^{\prime}w+uvw^{\prime}\)", r"\((uv)^{\prime}=u^{\prime}v+uv^{\prime}\)", r"\(\dfrac{d}{dx}(ax+b)^n=na(ax+b)^{n-1}\)"],
     [
         (r'\(\dfrac{d}{dx}\!\left[x(x+1)(x+2)\right]\)',
          r'Three-factor product rule.'
          r'\[(x+1)(x+2)+x(x+2)+x(x+1)=3x^2+6x+2.\]'
          r'\[\boxed{3x^2+6x+2}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x^2(2x+1)\right]\)',
          r'Product: \(u=x^2\), \(v=2x+1\).'
          r'\[2x(2x+1)+x^2\cdot 2=4x^2+2x+2x^2=6x^2+2x.\]'
          r'\[\boxed{6x^2+2x}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x(3x-1)^2\right]\)',
          r'Product + chain on \((3x-1)^2\).'
          r'\[(3x-1)^2+x\cdot 2(3x-1)\cdot 3=(3x-1)^2+6x(3x-1).\]'
          r'\[\boxed{(3x-1)^2+6x(3x-1)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(x+1)(x+2)(x+3)\right]\)',
          r'Three-factor rule.'
          r'\[(x+2)(x+3)+(x+1)(x+3)+(x+1)(x+2)=3x^2+12x+11.\]'
          r'\[\boxed{3x^2+12x+11}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x^2(x-1)^3\right]\)',
          r'Product + chain.'
          r'\[2x(x-1)^3+x^2\cdot 3(x-1)^2=2x(x-1)^3+3x^2(x-1)^2.\]'
          r'\[\boxed{2x(x-1)^3+3x^2(x-1)^2}\]'),
         (r'\(\dfrac{d}{dx}\!\left[2x(x^2+1)\right]\)',
          r'\[2(x^2+1)+2x\cdot 2x=2x^2+2+4x^2=6x^2+2.\]'
          r'\[\boxed{6x^2+2}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x\sqrt{x+1}\right]\)',
          r'Product with chain on \(\sqrt{x+1}\).'
          r'\[\sqrt{x+1}+x\cdot\dfrac{1}{2\sqrt{x+1}}=\dfrac{2(x+1)+x}{2\sqrt{x+1}}=\dfrac{3x+2}{2\sqrt{x+1}}.\]'
          r'\[\boxed{\dfrac{3x+2}{2\sqrt{x+1}}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(2x+1)^3(x-1)\right]\)',
          r'\[3(2x+1)^2\cdot 2\cdot(x-1)+(2x+1)^3=6(2x+1)^2(x-1)+(2x+1)^3.\]'
          r'\[\boxed{6(2x+1)^2(x-1)+(2x+1)^3}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x(x+1)(2x-1)\right]\)',
          r'\[(x+1)(2x-1)+x(2x-1)+x(x+1)\cdot 2=6x^2+2x-1.\]'
          r'\[\boxed{6x^2+2x-1}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x^3(4-x)\right]\)',
          r'\[3x^2(4-x)+x^3(-1)=12x^2-3x^3-x^3=12x^2-4x^3.\]'
          r'\[\boxed{12x^2-4x^3}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(x^2+1)(x^2-1)(x)\right]\)',
          r'Note \((x^2+1)(x^2-1)=x^4-1\), so product \(x(x^4-1)\).'
          r'\[\dfrac{d}{dx}(x^5-x)=5x^4-1.\]'
          r'\[\boxed{5x^4-1}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x e^x(x+1)\right]\) (treat as three factors)',
          r'Let \(u=x\), \(v=e^x\), \(w=x+1\).'
          r'\[e^x(x+1)+x e^x(x+1)+x e^x=e^x\bigl[(x+1)+x(x+1)+x\bigr]=e^x(x^2+3x+1).\]'
          r'\[\boxed{e^x(x^2+3x+1)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(3x-2)^2(2x+1)\right]\)',
          r'\[2(3x-2)\cdot 3\cdot(2x+1)+(3x-2)^2\cdot 2=6(3x-2)(2x+1)+2(3x-2)^2.\]'
          r'\[\boxed{6(3x-2)(2x+1)+2(3x-2)^2}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x^2(2x+3)^2\right]\)',
          r'\[2x(2x+3)^2+x^2\cdot 2(2x+3)\cdot 2=2x(2x+3)^2+4x^2(2x+3).\]'
          r'\[\boxed{2x(2x+3)^2+4x^2(2x+3)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(x+1)^2(x-1)^2\right]\)',
          r'Write as \([(x+1)(x-1)]^2=(x^2-1)^2\), or product of two squares.'
          r'\[2(x+1)(x-1)^2+2(x-1)(x+1)^2=2(x+1)(x-1)\bigl[(x-1)+(x+1)\bigr]=4x(x^2-1).\]'
          r'\[\boxed{4x(x^2-1)}\]'),
     ]),
_set('w3b-set5', '3B Set 5', 'WEEK 3B · SET 5 OF 5', 'Student Notes Week 3B (filled-in)',
     'Second and third derivatives with products',
     r'From Week 3B: exam-style practice finding \(f^{\prime\prime}\) and \(f^{\prime\prime\prime}\) for products and polynomials.',
     [
         r'Differentiate once with the product rule, then differentiate again for \(f^{\prime\prime}\).',
         r'Third derivatives appear in Taylor ideas and in motion (\(jerk=s^{\prime\prime\prime}\)).',
         r'Simplify after each differentiation when possible.',
     ],
     r"For \(f(x)=x e^x\): \(f^{\prime}=e^x+xe^x\), \(f^{\prime\prime}=2e^x+xe^x\).",
     [r'Differentiate step by step.', 'Re-apply product rule each time.', r'Acceleration \(=s^{\prime\prime}\).', r'Factor \(e^x\) when it appears.', 'Check by expanding polynomials.'],
     [r"\(f^{\prime\prime}=(f^{\prime})^{\prime}\)", r"\(f^{\prime\prime\prime}=(f^{\prime\prime})^{\prime}\)", r"\((uv)^{\prime}=u^{\prime}v+uv^{\prime}\)"],
     [
         (r"\(f(x)=x e^x\); find \(f^{\prime\prime}(x)\).",
          r'\(f^{\prime}=e^x+xe^x=(1+x)e^x\). Differentiate again:'
          r'\[f^{\prime\prime}=e^x+(1+x)e^x=(2+x)e^x.\]'
          r'\[\boxed{(x+2)e^x}\]'),
         (r"\(f(x)=x^2 e^x\); find \(f^{\prime\prime}(x)\).",
          r'\(f^{\prime}=2xe^x+x^2e^x=(2x+x^2)e^x\). Then'
          r'\[f^{\prime\prime}=(2+2x)e^x+(2x+x^2)e^x=(x^2+4x+2)e^x.\]'
          r'\[\boxed{(x^2+4x+2)e^x}\]'),
         (r"\(f(x)=x^4\); find \(f^{\prime\prime\prime}(x)\).",
          r'\(f^{\prime}=4x^3\), \(f^{\prime\prime}=12x^2\), \(f^{\prime\prime\prime}=24x\).'
          r'\[\boxed{24x}\]'),
         (r"\(f(x)=x(x+1)\); find \(f^{\prime\prime}(x)\).",
          r'\(f(x)=x^2+x\), \(f^{\prime}=2x+1\), \(f^{\prime\prime}=2\).'
          r'\[\boxed{2}\]'),
         (r"\(s(t)=t^2 e^{t}\); find \(s^{\prime\prime}(0)\).",
          r'From earlier pattern \(s^{\prime\prime}=(t^2+4t+2)e^t\), so \(s^{\prime\prime}(0)=2\).'
          r'\[\boxed{2}\]'),
         (r"\(f(x)=(2x+1)(x-3)\); find \(f^{\prime\prime}(x)\).",
          r'Expand: \(f=2x^2-5x-3\), \(f^{\prime}=4x-5\), \(f^{\prime\prime}=4\).'
          r'\[\boxed{4}\]'),
         (r"\(f(x)=x^3\sin x\) at \(x=0\): find \(f^{\prime\prime}(0)\) (product twice).",
          r'\(f^{\prime}=3x^2\sin x+x^3\cos x\). At \(0\), \(f^{\prime}(0)=0\). Differentiate:'
          r'\[f^{\prime\prime}=6x\sin x+3x^2\cos x+3x^2\cos x-x^3\sin x;\]'
          r'at \(x=0\), \(f^{\prime\prime}(0)=0\).'
          r'\[\boxed{0}\]'),
         (r"\(f(x)=x^5-2x^3\); find \(f^{\prime\prime\prime}(1)\).",
          r'\(f^{\prime}=5x^4-6x^2\), \(f^{\prime\prime}=20x^3-12x\), \(f^{\prime\prime\prime}=60x^2-12\).'
          r'\[f^{\prime\prime\prime}(1)=48.\]'
          r'\[\boxed{48}\]'),
         (r"\(f(x)=e^{2x}\); find \(f^{\prime\prime}(x)\) and \(f^{\prime\prime\prime}(x)\).",
          r'\(f^{\prime}=2e^{2x}\), \(f^{\prime\prime}=4e^{2x}\), \(f^{\prime\prime\prime}=8e^{2x}\).'
          r'\[\boxed{f^{\prime\prime}=4e^{2x},\ f^{\prime\prime\prime}=8e^{2x}}\]'),
         (r"\(f(x)=x\ln x\) (\(x>0\)); find \(f^{\prime\prime}(x)\).",
          r'\(f^{\prime}=\ln x+1\), \(f^{\prime\prime}=\dfrac{1}{x}\).'
          r'\[\boxed{\dfrac{1}{x}}\]'),
         (r"\(y=x^2(x+1)\); find \(\dfrac{d^2y}{dx^2}\).",
          r'\(y=x^3+x^2\), \(y^{\prime}=3x^2+2x\), \(y^{\prime\prime}=6x+2\).'
          r'\[\boxed{6x+2}\]'),
         (r"\(f(x)=(x+1)^3\); find \(f^{\prime\prime\prime}(x)\).",
          r'\(f^{\prime}=3(x+1)^2\), \(f^{\prime\prime}=6(x+1)\), \(f^{\prime\prime\prime}=6\).'
          r'\[\boxed{6}\]'),
         (r"\(s(t)=t^3-3t^2\); find acceleration at \(t=2\).",
          r'\(s^{\prime}=3t^2-6t\), \(s^{\prime\prime}=6t-6\), so \(s^{\prime\prime}(2)=6\).'
          r'\[\boxed{6}\]'),
         (r"\(f(x)=x\cos x\); find \(f^{\prime\prime}(x)\).",
          r'\(f^{\prime}=\cos x-x\sin x\). Then'
          r'\[f^{\prime\prime}=-\sin x-(\sin x+x\cos x)=-2\sin x-x\cos x.\]'
          r'\[\boxed{-2\sin x-x\cos x}\]'),
         (r"\(f(x)=x^2+xe^x\); find \(f^{\prime\prime}(0)\).",
          r'\(f^{\prime}=2x+(e^x+xe^x)=2x+(1+x)e^x\). '
          r'\(f^{\prime\prime}=2+e^x+(1+x)e^x=2+(2+x)e^x\). At \(0\): \(2+2=4\).'
          r'\[\boxed{4}\]'),
     ]),
    ]


def _ld_3c(_set):
    return [
_set('w3c-set4', '3C Set 4', 'WEEK 3C · SET 4 OF 5', 'Student Notes Week 3C (filled-in)',
     'Nested chain rule & quotients',
     r'From Week 3C: multi-step nested compositions and quotients that need careful inside/outside identification.',
     [
         r'Nested chain: differentiate the outermost function, multiply by the next inner derivative, and so on.',
         r'Quotients may contain composed numerators or denominators — apply chain inside the quotient formula.',
         r'Write intermediate steps so each rule application is clear.',
     ],
     r'\(\dfrac{d}{dx}\bigl[(2x+1)^3\bigr]^2=2(2x+1)^3\cdot 3(2x+1)^2\cdot 2\), or rewrite as \((2x+1)^6\).',
     ['Outermost first for nested chain.', r'Quotient: keep \(v^2\) in the denominator.', r'Chain inside \(u\) or \(v\) as needed.', 'Simplify powers when possible.', 'Factor common terms.'],
     [r"\(\dfrac{d}{dx}f(g(h(x)))=f'(g(h))g'(h)h'(x)\)", r"\(\dfrac{(u/v)'}=\dfrac{u'v-uv'}{v^2}\)", r'\(\dfrac{d}{dx}(ax+b)^n=na(ax+b)^{n-1}\)'],
     [
         (r'\(\dfrac{d}{dx}\!\left[(3x+1)^4\right]^3\)',
          r'Rewrite as \((3x+1)^{12}\) or nest chain.'
          r'\[\dfrac{d}{dx}(3x+1)^{12}=12(3x+1)^{11}\cdot 3=36(3x+1)^{11}.\]'
          r'\[\boxed{36(3x+1)^{11}}\]'),
         (r'\(\dfrac{d}{dx}\sqrt{(2x+1)^3}\)',
          r'Write \(((2x+1)^3)^{1/2}=(2x+1)^{3/2}\).'
          r'\[\dfrac{3}{2}(2x+1)^{1/2}\cdot 2=3\sqrt{2x+1}.\]'
          r'\[\boxed{3\sqrt{2x+1}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{(x+1)^2}{x-1}\right)\)',
          r'Quotient with chain on numerator.'
          r'\[u=(x+1)^2,\ u^{\prime}=2(x+1),\ v=x-1,\ v^{\prime}=1.\]'
          r'\[\dfrac{2(x+1)(x-1)-(x+1)^2}{(x-1)^2}=\dfrac{(x+1)\bigl[2(x-1)-(x+1)\bigr]}{(x-1)^2}=\dfrac{(x+1)(x-3)}{(x-1)^2}.\]'
          r'\[\boxed{\dfrac{(x+1)(x-3)}{(x-1)^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{1}{(x^2+1)^3}\right)\)',
          r'Chain: write \((x^2+1)^{-3}\).'
          r'\[-3(x^2+1)^{-4}\cdot 2x=-\dfrac{6x}{(x^2+1)^4}.\]'
          r'\[\boxed{-\dfrac{6x}{(x^2+1)^4}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\sqrt{x^2+2x+1}\right)\)',
          r'Note \(x^2+2x+1=(x+1)^2\), so for \(x\ge -1\), \(\sqrt{\,\cdot\,}=|x+1|\). Differentiating \((x+1)^2)^{1/2}\) via chain:'
          r'\[\dfrac{2x+2}{2\sqrt{x^2+2x+1}}=\dfrac{x+1}{|x+1|}\ \text{(or }\operatorname{sign}(x+1)\text{)}.\]'
          r'Alternatively leave as \(\dfrac{x+1}{\sqrt{(x+1)^2}}\).'
          r'\[\boxed{\dfrac{x+1}{|x+1|}\ (x\neq -1)}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{x}{(2x+1)^2}\right)\)',
          r'Quotient + chain on denominator.'
          r'\[u=x,\ u^{\prime}=1,\ v=(2x+1)^2,\ v^{\prime}=4(2x+1).\]'
          r'\[\dfrac{(2x+1)^2-x\cdot 4(2x+1)}{(2x+1)^4}=\dfrac{(2x+1)-4x}{(2x+1)^3}=\dfrac{1-2x}{(2x+1)^3}.\]'
          r'\[\boxed{\dfrac{1-2x}{(2x+1)^3}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(x^2+1)^2(3x-1)\right]\)',
          r'Product + chain.'
          r'\[2(x^2+1)\cdot 2x\cdot(3x-1)+(x^2+1)^2\cdot 3=4x(x^2+1)(3x-1)+3(x^2+1)^2.\]'
          r'\[\boxed{4x(x^2+1)(3x-1)+3(x^2+1)^2}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{(2x-1)^3}{x}\right)\)',
          r'\[u=(2x-1)^3,\ u^{\prime}=6(2x-1)^2,\ v=x.\]'
          r'\[\dfrac{6(2x-1)^2\cdot x-(2x-1)^3}{x^2}=\dfrac{(2x-1)^2\bigl[6x-(2x-1)\bigr]}{x^2}=\dfrac{(2x-1)^2(4x+1)}{x^2}.\]'
          r'\[\boxed{\dfrac{(2x-1)^2(4x+1)}{x^2}}\]'),
         (r'\(\dfrac{d}{dx}\sqrt[3]{(5x-2)^2}\)',
          r'Write \((5x-2)^{2/3}\).'
          r'\[\dfrac{2}{3}(5x-2)^{-1/3}\cdot 5=\dfrac{10}{3(5x-2)^{1/3}}.\]'
          r'\[\boxed{\dfrac{10}{3(5x-2)^{1/3}}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{\sqrt{x}}{x+2}\right)\)',
          r'\[u=x^{1/2},\ u^{\prime}=\dfrac{1}{2\sqrt{x}},\ v=x+2.\]'
          r'\[\dfrac{\dfrac{x+2}{2\sqrt{x}}-\sqrt{x}}{(x+2)^2}=\dfrac{x+2-2x}{2\sqrt{x}(x+2)^2}=\dfrac{2-x}{2\sqrt{x}(x+2)^2}.\]'
          r'\[\boxed{\dfrac{2-x}{2\sqrt{x}(x+2)^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(1-4x)^{-2}\right]\)',
          r'\[-2(1-4x)^{-3}\cdot(-4)=8(1-4x)^{-3}.\]'
          r'\[\boxed{8(1-4x)^{-3}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{x^2+1}{(x+1)^2}\right)\)',
          r'\[u^{\prime}=2x,\ v^{\prime}=2(x+1).\]'
          r'\[\dfrac{2x(x+1)^2-(x^2+1)\cdot 2(x+1)}{(x+1)^4}=\dfrac{2(x+1)\bigl[x(x+1)-(x^2+1)\bigr]}{(x+1)^4}=\dfrac{2(x-1)}{(x+1)^3}.\]'
          r'\[\boxed{\dfrac{2(x-1)}{(x+1)^3}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\bigl(x+\sqrt{x}\bigr)^4\right)\)',
          r'Chain with inner \(1+\dfrac{1}{2\sqrt{x}}\).'
          r'\[4\bigl(x+\sqrt{x}\bigr)^3\left(1+\dfrac{1}{2\sqrt{x}}\right).\]'
          r'\[\boxed{4(x+\sqrt{x})^3\left(1+\dfrac{1}{2\sqrt{x}}\right)}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{1}{\sqrt{3x+1}}\right)\)',
          r'Write \((3x+1)^{-1/2}\).'
          r'\[-\dfrac{1}{2}(3x+1)^{-3/2}\cdot 3=-\dfrac{3}{2}(3x+1)^{-3/2}.\]'
          r'\[\boxed{-\dfrac{3}{2}(3x+1)^{-3/2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{(x-1)^2}{(x+1)^3}\right)\)',
          r'\[u^{\prime}=2(x-1),\ v^{\prime}=3(x+1)^2.\]'
          r'\[\dfrac{2(x-1)(x+1)^3-(x-1)^2\cdot 3(x+1)^2}{(x+1)^6}=\dfrac{(x-1)(x+1)^2\bigl[2(x+1)-3(x-1)\bigr]}{(x+1)^6}=\dfrac{(x-1)(5-x)}{(x+1)^4}.\]'
          r'\[\boxed{\dfrac{(x-1)(5-x)}{(x+1)^4}}\]'),
     ]),
_set('w3c-set5', '3C Set 5', 'WEEK 3C · SET 5 OF 5', 'Student Notes Week 3C (filled-in)',
     'Quotient and chain on trig & polynomials',
     r'From Week 3C: exam-style practice combining quotient and chain rules on trig and polynomial composites.',
     [
         r'Trig compositions need chain on the angle: \(\dfrac{d}{dx}\sin(u)=\cos(u)\,u^{\prime}\).',
         r'Quotients of trig functions use \(\dfrac{u^{\prime}v-uv^{\prime}}{v^2}\) with trig derivatives.',
         r'Polynomial composites mix power chain with quotient as needed.',
     ],
     r'\(\dfrac{d}{dx}\dfrac{\sin(2x)}{x}=\dfrac{2x\cos(2x)-\sin(2x)}{x^2}\).',
     ['Chain on trig arguments.', 'Quotient formula carefully.', 'Product as alternative when helpful.', 'Simplify with identities only if neat.', 'Radians.'],
     [r'\(\dfrac{d}{dx}\sin(u)=\cos(u)u^{\prime}\)', r'\(\dfrac{d}{dx}\cos(u)=-\sin(u)u^{\prime}\)', r'\(\dfrac{d}{dx}\tan(u)=\sec^2(u)u^{\prime}\)'],
     [
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{\sin(2x)}{x}\right)\)',
          r'Quotient: \(u=\sin(2x)\), \(u^{\prime}=2\cos(2x)\), \(v=x\).'
          r'\[\dfrac{2x\cos(2x)-\sin(2x)}{x^2}.\]'
          r'\[\boxed{\dfrac{2x\cos(2x)-\sin(2x)}{x^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\sin(x^2+1)\right)\)',
          r'\[\cos(x^2+1)\cdot 2x=2x\cos(x^2+1).\]'
          r'\[\boxed{2x\cos(x^2+1)}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{\cos x}{x+1}\right)\)',
          r'\[\dfrac{-\sin x\cdot(x+1)-\cos x}{(x+1)^2}=-\dfrac{(x+1)\sin x+\cos x}{(x+1)^2}.\]'
          r'\[\boxed{-\dfrac{(x+1)\sin x+\cos x}{(x+1)^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\tan(3x+1)\right)\)',
          r'\[3\sec^2(3x+1).\]'
          r'\[\boxed{3\sec^2(3x+1)}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{x^2}{\sin x}\right)\)',
          r'\[\dfrac{2x\sin x-x^2\cos x}{\sin^2 x}.\]'
          r'\[\boxed{\dfrac{2x\sin x-x^2\cos x}{\sin^2 x}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\cos(2x)^3\right)\) (i.e. \(\bigl(\cos(2x)\bigr)^3\))',
          r'\[3\cos^2(2x)\cdot(-\sin(2x))\cdot 2=-6\cos^2(2x)\sin(2x).\]'
          r'\[\boxed{-6\cos^2(2x)\sin(2x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{(2x+1)^2}{\cos x}\right)\)',
          r'\[u^{\prime}=2(2x+1)\cdot 2=4(2x+1),\ v^{\prime}=-\sin x.\]'
          r'\[\dfrac{4(2x+1)\cos x+(2x+1)^2\sin x}{\cos^2 x}.\]'
          r'\[\boxed{\dfrac{4(2x+1)\cos x+(2x+1)^2\sin x}{\cos^2 x}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\sin\sqrt{x}\right)\)',
          r'\[\cos\sqrt{x}\cdot\dfrac{1}{2\sqrt{x}}.\]'
          r'\[\boxed{\dfrac{\cos\sqrt{x}}{2\sqrt{x}}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{\tan x}{x}\right)\)',
          r'\[\dfrac{x\sec^2 x-\tan x}{x^2}.\]'
          r'\[\boxed{\dfrac{x\sec^2 x-\tan x}{x^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(x^2+1)\sin(3x)\right]\)',
          r'\[2x\sin(3x)+(x^2+1)\cdot 3\cos(3x).\]'
          r'\[\boxed{2x\sin(3x)+3(x^2+1)\cos(3x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{1}{\sin(2x)}\right)\)',
          r'Write \(\csc(2x)\): derivative \(-\csc(2x)\cot(2x)\cdot 2\).'
          r'\[-\dfrac{2\cos(2x)}{\sin^2(2x)}.\]'
          r'\[\boxed{-\dfrac{2\cos(2x)}{\sin^2(2x)}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{x\cos x}{x+1}\right)\)',
          r'Product in numerator: \(u=x\cos x\), \(u^{\prime}=\cos x-x\sin x\), \(v=x+1\).'
          r'\[\dfrac{(\cos x-x\sin x)(x+1)-x\cos x}{(x+1)^2}.\]'
          r'\[\boxed{\dfrac{(\cos x-x\sin x)(x+1)-x\cos x}{(x+1)^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\cos(x^3)\right)\)',
          r'\[-\sin(x^3)\cdot 3x^2=-3x^2\sin(x^3).\]'
          r'\[\boxed{-3x^2\sin(x^3)}\]'),
         (r'\(\dfrac{d}{dx}\!\left(\dfrac{\sin x+\cos x}{\sin x-\cos x}\right)\)',
          r'Numerator of quotient: \((\cos-\sin)(\sin-\cos)-(\sin+\cos)(\cos+\sin)\).'
          r'Note \((\cos-\sin)=-(\sin-\cos)\), so first part is \(-(\sin-\cos)^2\), and second is \((\sin+\cos)^2\).'
          r'Overall numerator \(=-(\sin-\cos)^2-(\sin+\cos)^2=-2(\sin^2+\cos^2)=-2\).'
          r'\[\dfrac{-2}{(\sin x-\cos x)^2}.\]'
          r'\[\boxed{-\dfrac{2}{(\sin x-\cos x)^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left(x\tan(2x)\right)\)',
          r'\[\tan(2x)+x\cdot 2\sec^2(2x)=\tan(2x)+2x\sec^2(2x).\]'
          r'\[\boxed{\tan(2x)+2x\sec^2(2x)}\]'),
     ]),
    ]


def _ld_3d(_set):
    return [
_set('w3d-set4', '3D Set 4', 'WEEK 3D · SET 4 OF 5', 'Student Notes Week 3D (filled-in)',
     'Tangents and normals to exponential curves',
     r'From Week 3D: multi-step tangent and normal equations for \(e^{ax}\) and related exponentials.',
     [
         r'Tangent: find point \((a,f(a))\) and slope \(m=f^{\prime}(a)\), then \(y-y_1=m(x-x_1)\).',
         r'Normal is perpendicular: slope \(-\dfrac{1}{m}\) when \(m\neq 0\).',
         r'For \(y=e^{kx}\), \(y^{\prime}=ke^{kx}\), so slope equals \(k\) times the \(y\)-value.',
     ],
     r'For \(y=e^{2x}\) at \(x=0\): point \((0,1)\), \(m=2\), tangent \(y=2x+1\).',
     [r'Slope from exponential derivative.', 'Point–gradient form.', r'Normal slope \(-1/m\).', r'\(e^0=1\).', 'Simplify carefully.'],
     [r'\(\dfrac{d}{dx}e^{ax}=a e^{ax}\)', r'\(y-y_1=m(x-x_1)\)', r'Normal: \(m_n=-1/m_t\)'],
     [
         (r'\(y=e^{2x}\); equation of the tangent at \(x=0\).',
          r'Point \((0,1)\), \(y^{\prime}=2e^{2x}\), \(m=2\).'
          r'\[y-1=2(x-0)\Rightarrow y=2x+1.\]'
          r'\[\boxed{y=2x+1}\]'),
         (r'\(y=e^{x}\); equation of the tangent at \(x=1\).',
          r'Point \((1,e)\), \(m=e\).'
          r'\[y-e=e(x-1)\Rightarrow y=ex.\]'
          r'\[\boxed{y=ex}\]'),
         (r'\(y=3e^{-x}\); tangent at \(x=0\).',
          r'Point \((0,3)\), \(y^{\prime}=-3e^{-x}\), \(m=-3\).'
          r'\[y-3=-3x\Rightarrow y=-3x+3.\]'
          r'\[\boxed{y=-3x+3}\]'),
         (r'\(y=e^{x}\); equation of the normal at \(x=0\).',
          r'Point \((0,1)\), tangent slope \(1\), normal slope \(-1\).'
          r'\[y-1=-1(x-0)\Rightarrow y=-x+1.\]'
          r'\[\boxed{y=-x+1}\]'),
         (r'\(y=e^{3x}\); find the slope of the tangent at \(x=\ln 2\).',
          r'\(y^{\prime}=3e^{3x}\), so at \(x=\ln 2\): \(3e^{3\ln 2}=3\cdot 8=24\).'
          r'\[\boxed{24}\]'),
         (r'\(y=2e^{x}+1\); tangent at \(x=0\).',
          r'Point \((0,3)\), \(m=2\).'
          r'\[y-3=2x\Rightarrow y=2x+3.\]'
          r'\[\boxed{y=2x+3}\]'),
         (r'\(y=e^{x^2}\); tangent at \(x=1\).',
          r'Point \((1,e)\), \(y^{\prime}=2xe^{x^2}\), \(m=2e\).'
          r'\[y-e=2e(x-1).\]'
          r'\[\boxed{y-e=2e(x-1)}\]'),
         (r'\(y=e^{-2x}\); normal at \(x=0\).',
          r'Point \((0,1)\), \(m=-2\), normal slope \(\dfrac12\).'
          r'\[y-1=\dfrac12 x\Rightarrow y=\dfrac12 x+1.\]'
          r'\[\boxed{y=\dfrac{1}{2}x+1}\]'),
         (r'\(y=xe^{x}\); tangent at \(x=0\).',
          r'Point \((0,0)\), \(y^{\prime}=e^x+xe^x=(1+x)e^x\), \(m=1\).'
          r'\[y=x.\]'
          r'\[\boxed{y=x}\]'),
         (r'\(y=e^{x}+e^{-x}\); tangent at \(x=0\).',
          r'Point \((0,2)\), \(y^{\prime}=e^x-e^{-x}\), \(m=0\).'
          r'\[y=2.\]'
          r'\[\boxed{y=2}\]'),
         (r'\(y=5e^{4x}\); find \(x\) where the tangent slope is \(20\).',
          r'\(y^{\prime}=20e^{4x}=20\Rightarrow e^{4x}=1\Rightarrow x=0\).'
          r'\[\boxed{x=0}\]'),
         (r'\(y=e^{2x-1}\); tangent at \(x=\dfrac12\).',
          r'Point \(\bigl(\tfrac12,1\bigr)\), \(m=2e^{2x-1}=2\).'
          r'\[y-1=2\bigl(x-\tfrac12\bigr)\Rightarrow y=2x.\]'
          r'\[\boxed{y=2x}\]'),
         (r'\(y=e^{x}\); show the tangent at \(x=a\) is \(y=e^{a}(x-a+1)\).',
          r'Point \((a,e^a)\), \(m=e^a\).'
          r'\[y-e^a=e^a(x-a)\Rightarrow y=e^a(x-a+1).\]'
          r'\[\boxed{y=e^{a}(x-a+1)}\]'),
         (r'\(y=2e^{x}-x\); tangent at \(x=0\).',
          r'Point \((0,2)\), \(y^{\prime}=2e^x-1\), \(m=1\).'
          r'\[y-2=x\Rightarrow y=x+2.\]'
          r'\[\boxed{y=x+2}\]'),
         (r'\(y=e^{-x}+x\); normal at \(x=0\).',
          r'Point \((0,1)\), \(y^{\prime}=-e^{-x}+1\), \(m=0\) — horizontal tangent, so normal is vertical \(x=0\).'
          r'\[\boxed{x=0}\]'),
     ]),
_set('w3d-set5', '3D Set 5', 'WEEK 3D · SET 5 OF 5', 'Student Notes Week 3D (filled-in)',
     'Exponential growth rates & tangent links',
     r'From Week 3D: exam-style related-rates-lite and growth problems linking \(e^{kt}\) derivatives to tangents.',
     [
         r'If \(P=P_0 e^{kt}\), then \(\dfrac{dP}{dt}=kP\): rate proportional to current size.',
         r'Related-rates-lite: if \(y=e^{u(t)}\), then \(\dfrac{dy}{dt}=e^{u}u^{\prime}(t)\).',
         r'Tangent slopes on growth curves equal \(k\) times the height.',
     ],
     r'If \(P=100e^{0.2t}\), then \(P\'(t)=20e^{0.2t}=0.2P\).',
     [r'Growth: \(P^{\prime}=kP\).', r'Chain on \(e^{u(t)}\).', 'Evaluate rates at a given time.', 'Link slope to tangent line.', 'Units matter in context.'],
     [r'\(\dfrac{d}{dt}P_0 e^{kt}=kP_0 e^{kt}\)', r'\(\dfrac{d}{dt}e^{u}=e^{u}u^{\prime}\)', r'Tangent slope \(=f^{\prime}(a)\)'],
     [
         (r'If \(P=50e^{0.1t}\), find \(P\'(0)\) and interpret.',
          r'\(P^{\prime}=5e^{0.1t}\), so \(P\'(0)=5\): initially growing at \(5\) units per unit time.'
          r'\[\boxed{5}\]'),
         (r'If \(N=N_0 e^{-0.2t}\), find the relative decay rate \(\dfrac{N\'}{N}\).',
          r'\(N\'=-0.2 N_0 e^{-0.2t}\), so \(\dfrac{N\'}{N}=-0.2\).'
          r'\[\boxed{-0.2}\]'),
         (r'\(y=e^{3t}\); find the tangent to \(y\) vs \(t\) at \(t=0\).',
          r'Point \((0,1)\), \(m=3\), line \(y=3t+1\).'
          r'\[\boxed{y=3t+1}\]'),
         (r'A quantity \(Q=4e^{2t}\). When \(Q=4e^2\), find \(\dfrac{dQ}{dt}\).',
          r'\(Q=4e^2\Rightarrow e^{2t}=e^2\Rightarrow t=1\). Then \(Q^{\prime}=8e^{2t}=8e^2\).'
          r'\[\boxed{8e^2}\]'),
         (r'If \(x=e^{t}\) and \(y=e^{2t}\), find \(\dfrac{dy}{dx}\) at \(t=0\).',
          r'\(\dfrac{dy}{dt}=2e^{2t}\), \(\dfrac{dx}{dt}=e^{t}\), so \(\dfrac{dy}{dx}=2e^{t}\). At \(t=0\): \(2\).'
          r'\[\boxed{2}\]'),
         (r'\(P=100e^{kt}\) doubles when \(t=5\). Find \(k\), then \(P\'(0)\).',
          r'\(e^{5k}=2\Rightarrow k=\dfrac{\ln 2}{5}\). \(P\'(0)=100k=20\ln 2\).'
          r'\[\boxed{20\ln 2}\]'),
         (r'\(y=e^{x}+x\); rate of change of \(y\) when \(x=0\).',
          r'\(y^{\prime}=e^x+1\), so \(y^{\prime}(0)=2\).'
          r'\[\boxed{2}\]'),
         (r'If the tangent to \(y=e^{kx}\) at \(x=0\) has slope \(4\), find \(k\).',
          r'\(y^{\prime}=ke^{kx}\), at \(0\): \(k=4\).'
          r'\[\boxed{k=4}\]'),
         (r'\(s(t)=e^{t}-t\); find velocity and acceleration at \(t=0\).',
          r'\(v=e^{t}-1\), \(a=e^{t}\). At \(0\): \(v=0\), \(a=1\).'
          r'\[\boxed{v=0,\ a=1}\]'),
         (r'\(y=2e^{-t}\); equation of the tangent when \(y=1\).',
          r'\(2e^{-t}=1\Rightarrow t=\ln 2\). Point \((\ln 2,1)\), \(m=-2e^{-t}=-1\).'
          r'\[y-1=-(t-\ln 2).\]'
          r'\[\boxed{y-1=-(t-\ln 2)}\]'),
         (r'If \(u=2t\) and \(y=e^{u}\), find \(\dfrac{dy}{dt}\) in terms of \(y\).',
          r'\(\dfrac{dy}{dt}=e^{u}\cdot 2=2y\).'
          r'\[\boxed{2y}\]'),
         (r'\(P=P_0 e^{0.05t}\); percentage rate of change.',
          r'\(\dfrac{P\'}{P}=0.05=5\%\) per unit time.'
          r'\[\boxed{5\%\ \text{per unit time}}\]'),
         (r'\(y=e^{x^2}\); find \(\dfrac{dy}{dx}\) at \(x=0\) and the tangent line.',
          r'\(y^{\prime}=2xe^{x^2}\), at \(0\): slope \(0\), point \((0,1)\), tangent \(y=1\).'
          r'\[\boxed{y=1}\]'),
         (r'A bacteria count \(B=1000e^{0.3t}\). Find \(B^{\prime}(2)\) exactly.',
          r'\(B\'=300e^{0.3t}\), so \(B^{\prime}(2)=300e^{0.6}\).'
          r'\[\boxed{300e^{0.6}}\]'),
         (r'\(y=e^{t}+e^{-t}\); show \(\dfrac{d^2y}{dt^2}=y\), and find the tangent at \(t=0\).',
          r'\(y^{\prime}=e^{t}-e^{-t}\), \(y^{\prime\prime}=e^{t}+e^{-t}=y\). At \(t=0\): point \((0,2)\), \(m=0\), tangent \(y=2\).'
          r'\[\boxed{y=2}\]'),
     ]),
    ]


def _ld_4a(_set):
    return [
_set('w4a-set4', '4A Set 4', 'WEEK 4A · SET 4 OF 5', 'Student Notes Week 4A (filled-in)',
     'Logarithms with chain and product',
     r'From Week 4A: multi-step derivatives mixing \(\ln\), chain rule, and product rule.',
     [
         r"\(\dfrac{d}{dx}\ln(f)=\dfrac{f^{\prime}}{f}\); combine with product when \(\ln\) multiplies another factor.",
         r'Log laws can simplify before differentiating: \(\ln(uv)=\ln u+\ln v\).',
         r'Keep the domain \(f(x)>0\) in mind for logarithmic expressions.',
     ],
     r'\(\dfrac{d}{dx}[x\ln(x^2+1)]=\ln(x^2+1)+\dfrac{2x^2}{x^2+1}\).',
     [r'Log derivative over argument.', 'Product when factors multiply.', 'Simplify with log laws first if helpful.', 'Chain on the inside.', 'Check domain.'],
     [r"\(\dfrac{d}{dx}\ln(f)=\dfrac{f^{\prime}}{f}\)", r"\((uv)^{\prime}=u^{\prime}v+uv^{\prime}\)", r'\(\ln(uv)=\ln u+\ln v\)'],
     [
         (r'\(\dfrac{d}{dx}\!\left[x\ln(x^2+1)\right]\)',
          r'Product: \(u=x\), \(v=\ln(x^2+1)\).'
          r'\[\ln(x^2+1)+x\cdot\dfrac{2x}{x^2+1}=\ln(x^2+1)+\dfrac{2x^2}{x^2+1}.\]'
          r'\[\boxed{\ln(x^2+1)+\dfrac{2x^2}{x^2+1}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln(x)\cdot\ln(x+1)\right]\)',
          r'\[\dfrac{1}{x}\ln(x+1)+\ln x\cdot\dfrac{1}{x+1}.\]'
          r'\[\boxed{\dfrac{\ln(x+1)}{x}+\dfrac{\ln x}{x+1}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln\bigl((2x+1)^3\bigr)\right]\)',
          r'Simplify: \(3\ln|2x+1|\), then differentiate.'
          r'\[\dfrac{3\cdot 2}{2x+1}=\dfrac{6}{2x+1}.\]'
          r'\[\boxed{\dfrac{6}{2x+1}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[e^x\ln x\right]\)',
          r'\[e^x\ln x+e^x\cdot\dfrac{1}{x}=e^x\left(\ln x+\dfrac{1}{x}\right).\]'
          r'\[\boxed{e^x\left(\ln x+\dfrac{1}{x}\right)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln\dfrac{x}{x+1}\right]\)',
          r'Write \(\ln x-\ln(x+1)\).'
          r'\[\dfrac{1}{x}-\dfrac{1}{x+1}=\dfrac{1}{x(x+1)}.\]'
          r'\[\boxed{\dfrac{1}{x(x+1)}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x^2\ln(3x)\right]\)',
          r'\[2x\ln(3x)+x^2\cdot\dfrac{1}{x}=2x\ln(3x)+x.\]'
          r'\[\boxed{2x\ln(3x)+x}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln(x^2+2x)\right]\)',
          r'\[\dfrac{2x+2}{x^2+2x}=\dfrac{2(x+1)}{x(x+2)}.\]'
          r'\[\boxed{\dfrac{2(x+1)}{x(x+2)}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[(2x+1)\ln(2x+1)\right]\)',
          r'\[2\ln(2x+1)+(2x+1)\cdot\dfrac{2}{2x+1}=2\ln(2x+1)+2.\]'
          r'\[\boxed{2\ln(2x+1)+2}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln\sqrt{x^2+1}\right]\)',
          r'Write \(\dfrac12\ln(x^2+1)\).'
          r'\[\dfrac{1}{2}\cdot\dfrac{2x}{x^2+1}=\dfrac{x}{x^2+1}.\]'
          r'\[\boxed{\dfrac{x}{x^2+1}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\dfrac{\ln x}{x}\right]\)',
          r'\[\dfrac{\dfrac{1}{x}\cdot x-\ln x}{x^2}=\dfrac{1-\ln x}{x^2}.\]'
          r'\[\boxed{\dfrac{1-\ln x}{x^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln(e^{2x}+1)\right]\)',
          r'\[\dfrac{2e^{2x}}{e^{2x}+1}.\]'
          r'\[\boxed{\dfrac{2e^{2x}}{e^{2x}+1}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x\ln(x^2)\right]\) for \(x>0\)',
          r'\(\ln(x^2)=2\ln x\), so \(2x\ln x\); derivative \(2\ln x+2\).'
          r'\[\boxed{2\ln x+2}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln(x)\cdot e^{2x}\right]\)',
          r'\[\dfrac{1}{x}e^{2x}+\ln x\cdot 2e^{2x}=e^{2x}\left(\dfrac{1}{x}+2\ln x\right).\]'
          r'\[\boxed{e^{2x}\left(\dfrac{1}{x}+2\ln x\right)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln(x^2+1)^3\right]\) (i.e. \(\ln\bigl((x^2+1)^3\bigr)\))',
          r'\[3\cdot\dfrac{2x}{x^2+1}=\dfrac{6x}{x^2+1}.\]'
          r'\[\boxed{\dfrac{6x}{x^2+1}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\dfrac{x+1}{\ln x}\right]\)',
          r'\[\dfrac{\ln x-(x+1)\cdot\dfrac{1}{x}}{(\ln x)^2}=\dfrac{x\ln x-(x+1)}{x(\ln x)^2}.\]'
          r'\[\boxed{\dfrac{x\ln x-x-1}{x(\ln x)^2}}\]'),
     ]),
_set('w4a-set5', '4A Set 5', 'WEEK 4A · SET 5 OF 5', 'Student Notes Week 4A (filled-in)',
     'Trig derivatives with chain and product',
     r'From Week 4A: exam-style trig composites using chain and product (no inverse trig).',
     [
         r'Chain on angles: \(\dfrac{d}{dx}\sin(u)=\cos(u)\,u^{\prime}\), similarly for \(\cos\) and \(\tan\).',
         r'Products like \(x\sin(2x)\) need both product and chain.',
         r'Powers of trig functions are compositions: \(\sin^n x=(\sin x)^n\).',
     ],
     r'\(\dfrac{d}{dx}\sin^3(2x)=3\sin^2(2x)\cos(2x)\cdot 2\).',
     [r'Chain on the angle.', 'Product on separate factors.', r'Power rule for \(\sin^n\).', r'\(\tan^{\prime}=\sec^2\).', 'Radians.'],
     [r'\(\dfrac{d}{dx}\sin(u)=\cos(u)u^{\prime}\)', r'\(\dfrac{d}{dx}\cos(u)=-\sin(u)u^{\prime}\)', r'\(\dfrac{d}{dx}(\sin u)^n=n(\sin u)^{n-1}\cos(u)u^{\prime}\)'],
     [
         (r'\(\dfrac{d}{dx}\!\left[\sin^3(2x)\right]\)',
          r'\[3\sin^2(2x)\cdot\cos(2x)\cdot 2=6\sin^2(2x)\cos(2x).\]'
          r'\[\boxed{6\sin^2(2x)\cos(2x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x\sin(2x)\right]\)',
          r'\[\sin(2x)+x\cdot 2\cos(2x)=\sin(2x)+2x\cos(2x).\]'
          r'\[\boxed{\sin(2x)+2x\cos(2x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\cos(x)\sin(3x)\right]\)',
          r'\[-\sin x\sin(3x)+\cos x\cdot 3\cos(3x).\]'
          r'\[\boxed{-\sin x\sin(3x)+3\cos x\cos(3x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\tan(x^2)\right]\)',
          r'\[2x\sec^2(x^2).\]'
          r'\[\boxed{2x\sec^2(x^2)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\dfrac{\sin x}{\cos(2x)}\right]\)',
          r'\[\dfrac{\cos x\cos(2x)-\sin x\cdot(-2\sin(2x))}{\cos^2(2x)}=\dfrac{\cos x\cos(2x)+2\sin x\sin(2x)}{\cos^2(2x)}.\]'
          r'\[\boxed{\dfrac{\cos x\cos(2x)+2\sin x\sin(2x)}{\cos^2(2x)}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\sin(2x)\cos(2x)\right]\)',
          r'Or note \(\dfrac12\sin(4x)\). Directly:'
          r'\[2\cos(2x)\cos(2x)+\sin(2x)\cdot(-2\sin(2x))=2(\cos^2(2x)-\sin^2(2x))=2\cos(4x).\]'
          r'\[\boxed{2\cos(4x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[e^{\sin x}\right]\)',
          r'\[\cos x\, e^{\sin x}.\]'
          r'\[\boxed{\cos x\, e^{\sin x}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\ln(\sin x)\right]\) for \(\sin x>0\)',
          r'\[\dfrac{\cos x}{\sin x}=\cot x.\]'
          r'\[\boxed{\cot x}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x^2\cos(3x)\right]\)',
          r'\[2x\cos(3x)+x^2\cdot(-3\sin(3x))=2x\cos(3x)-3x^2\sin(3x).\]'
          r'\[\boxed{2x\cos(3x)-3x^2\sin(3x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\sec^2(2x)\right]\)',
          r'Write \((\sec(2x))^2\): \(2\sec(2x)\cdot\sec(2x)\tan(2x)\cdot 2=4\sec^2(2x)\tan(2x)\).'
          r'\[\boxed{4\sec^2(2x)\tan(2x)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\sin(x)\ln(\cos x)\right]\)',
          r'\[\cos x\ln(\cos x)+\sin x\cdot\dfrac{-\sin x}{\cos x}=\cos x\ln(\cos x)-\dfrac{\sin^2 x}{\cos x}.\]'
          r'\[\boxed{\cos x\ln(\cos x)-\dfrac{\sin^2 x}{\cos x}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\dfrac{\tan(2x)}{x}\right]\)',
          r'\[\dfrac{2x\sec^2(2x)-\tan(2x)}{x^2}.\]'
          r'\[\boxed{\dfrac{2x\sec^2(2x)-\tan(2x)}{x^2}}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\cos^4 x\right]\)',
          r'\[4\cos^3 x\cdot(-\sin x)=-4\cos^3 x\sin x.\]'
          r'\[\boxed{-4\cos^3 x\sin x}\]'),
         (r'\(\dfrac{d}{dx}\!\left[\sin(2x+1)\cos(2x+1)\right]\)',
          r'Use \(\dfrac12\sin(2\theta)\) with \(\theta=2x+1\): \(\dfrac12\sin(4x+2)\), derivative \(2\cos(4x+2)\).'
          r'\[\boxed{2\cos(4x+2)}\]'),
         (r'\(\dfrac{d}{dx}\!\left[x\tan x\cdot\cos x\right]\)',
          r'Note \(\tan x\cos x=\sin x\), so \(x\sin x\).'
          r'\[\sin x+x\cos x.\]'
          r'\[\boxed{\sin x+x\cos x}\]'),
     ]),
    ]


def _int_4d(_set):
    return [
_set('w4d-set4', '4D Set 4', 'WEEK 4D · SET 4 OF 5', 'Student Notes Week 4D (filled-in)',
     'Reverse chain for linear insides',
     r'From Week 4D: multi-step reverse chain rule mentally for forms like \(\int(ax+b)^n\,dx\).',
     [
         r'If the inside is linear \(ax+b\), \(\displaystyle\int(ax+b)^n\,dx=\dfrac{(ax+b)^{n+1}}{a(n+1)}+C\) for \(n\neq -1\).',
         r'Check by differentiating: chain rule brings back the factor \(a\).',
         r'Same idea for \(\displaystyle\int e^{ax+b}\,dx=\dfrac{1}{a}e^{ax+b}+C\).',
     ],
     r'\(\displaystyle\int(2x+1)^5\,dx=\dfrac{(2x+1)^6}{12}+C\).',
     [r'Reverse chain: divide by inner derivative.', r'For \(n=-1\): log form.', 'Verify by differentiating.', r'Watch the constant \(a\).', r'Add \(+C\).'],
     [r'\(\displaystyle\int(ax+b)^n\,dx=\dfrac{(ax+b)^{n+1}}{a(n+1)}+C\)', r'\(\displaystyle\int e^{ax}\,dx=\dfrac{e^{ax}}{a}+C\)'],
     [
         (r'\(\displaystyle\int(2x+1)^5\,dx\)',
          r'Reverse chain with \(a=2\), \(n=5\).'
          r'\[\dfrac{(2x+1)^6}{2\cdot 6}+C=\dfrac{(2x+1)^6}{12}+C.\]'
          r'\[\boxed{\dfrac{(2x+1)^6}{12}+C}\]'),
         (r'\(\displaystyle\int(3x-2)^4\,dx\)',
          r'\[\dfrac{(3x-2)^5}{3\cdot 5}+C=\dfrac{(3x-2)^5}{15}+C.\]'
          r'\[\boxed{\dfrac{(3x-2)^5}{15}+C}\]'),
         (r'\(\displaystyle\int(1-4x)^3\,dx\)',
          r'Inner derivative \(-4\).'
          r'\[\dfrac{(1-4x)^4}{(-4)\cdot 4}+C=-\dfrac{(1-4x)^4}{16}+C.\]'
          r'\[\boxed{-\dfrac{(1-4x)^4}{16}+C}\]'),
         (r'\(\displaystyle\int\sqrt{2x+3}\,dx\)',
          r'Write \((2x+3)^{1/2}\).'
          r'\[\dfrac{(2x+3)^{3/2}}{2\cdot\tfrac{3}{2}}+C=\dfrac{(2x+3)^{3/2}}{3}+C.\]'
          r'\[\boxed{\dfrac{(2x+3)^{3/2}}{3}+C}\]'),
         (r'\(\displaystyle\int\dfrac{1}{(5x+1)^2}\,dx\)',
          r'Write \((5x+1)^{-2}\).'
          r'\[\dfrac{(5x+1)^{-1}}{5\cdot(-1)}+C=-\dfrac{1}{5(5x+1)}+C.\]'
          r'\[\boxed{-\dfrac{1}{5(5x+1)}+C}\]'),
         (r'\(\displaystyle\int e^{3x+1}\,dx\)',
          r'\[\dfrac{1}{3}e^{3x+1}+C.\]'
          r'\[\boxed{\dfrac{1}{3}e^{3x+1}+C}\]'),
         (r'\(\displaystyle\int(4-x)^7\,dx\)',
          r'\[\dfrac{(4-x)^8}{(-1)\cdot 8}+C=-\dfrac{(4-x)^8}{8}+C.\]'
          r'\[\boxed{-\dfrac{(4-x)^8}{8}+C}\]'),
         (r'\(\displaystyle\int\dfrac{1}{2x+5}\,dx\)',
          r'\[\dfrac{1}{2}\ln|2x+5|+C.\]'
          r'\[\boxed{\dfrac{1}{2}\ln|2x+5|+C}\]'),
         (r'\(\displaystyle\int(6x+1)^{1/3}\,dx\)',
          r'\[\dfrac{(6x+1)^{4/3}}{6\cdot\tfrac{4}{3}}+C=\dfrac{(6x+1)^{4/3}}{8}+C.\]'
          r'\[\boxed{\dfrac{(6x+1)^{4/3}}{8}+C}\]'),
         (r'\(\displaystyle\int\cos(2x+1)\,dx\)',
          r'\[\dfrac{1}{2}\sin(2x+1)+C.\]'
          r'\[\boxed{\dfrac{1}{2}\sin(2x+1)+C}\]'),
         (r'\(\displaystyle\int\sin(3x)\,dx\)',
          r'\[-\dfrac{1}{3}\cos(3x)+C.\]'
          r'\[\boxed{-\dfrac{1}{3}\cos(3x)+C}\]'),
         (r'\(\displaystyle\int(5-2x)^{-1}\,dx\)',
          r'\[\dfrac{1}{-2}\ln|5-2x|+C=-\dfrac{1}{2}\ln|5-2x|+C.\]'
          r'\[\boxed{-\dfrac{1}{2}\ln|5-2x|+C}\]'),
         (r'\(\displaystyle\int(3x+4)^0\,dx\)',
          r'\((3x+4)^0=1\) where defined.'
          r'\[x+C.\]'
          r'\[\boxed{x+C}\]'),
         (r'\(\displaystyle\int 2(2x-1)^9\,dx\)',
          r'\[\dfrac{2(2x-1)^{10}}{2\cdot 10}+C=\dfrac{(2x-1)^{10}}{10}+C.\]'
          r'\[\boxed{\dfrac{(2x-1)^{10}}{10}+C}\]'),
         (r'\(\displaystyle\int\dfrac{3}{(x+2)^4}\,dx\)',
          r'\[3\cdot\dfrac{(x+2)^{-3}}{-3}+C=-\dfrac{1}{(x+2)^3}+C.\]'
          r'\[\boxed{-\dfrac{1}{(x+2)^3}+C}\]'),
     ]),
_set('w4d-set5', '4D Set 5', 'WEEK 4D · SET 5 OF 5', 'Student Notes Week 4D (filled-in)',
     'Rewrite first, then integrate',
     r'From Week 4D: exam-style practice rewriting integrands before applying reverse rules.',
     [
         r'Expand products, split fractions, or rewrite roots as powers before integrating.',
         r'Sometimes divide polynomials to simplify rational integrands.',
         r'After rewriting, use power rule / reverse chain term by term.',
     ],
     r'\(\displaystyle\int\dfrac{x^2+2x}{x}\,dx=\displaystyle\int(x+2)\,dx=\dfrac{x^2}{2}+2x+C\).',
     ['Algebra before integration.', 'Split fractions.', 'Expand brackets.', 'Then reverse power/chain.', 'Differentiate to check.'],
     [r'Simplify, then \(\int x^n\)', r'\(\dfrac{x^2+a}{x}=x+\dfrac{a}{x}\)'],
     [
         (r'\(\displaystyle\int\dfrac{x^3+2x}{x}\,dx\)',
          r'Split: \(\displaystyle\int(x^2+2)\,dx\).'
          r'\[\dfrac{x^3}{3}+2x+C.\]'
          r'\[\boxed{\dfrac{x^3}{3}+2x+C}\]'),
         (r'\(\displaystyle\int x(2x+1)^2\,dx\)',
          r'Expand \((2x+1)^2=4x^2+4x+1\), so \(x(2x+1)^2=4x^3+4x^2+x\).'
          r'\[\int(4x^3+4x^2+x)\,dx=x^4+\dfrac{4x^3}{3}+\dfrac{x^2}{2}+C.\]'
          r'\[\boxed{x^4+\dfrac{4x^3}{3}+\dfrac{x^2}{2}+C}\]'),
         (r'\(\displaystyle\int\dfrac{(x+1)^2}{x}\,dx\)',
          r'Expand: \(\dfrac{x^2+2x+1}{x}=x+2+x^{-1}\).'
          r'\[\dfrac{x^2}{2}+2x+\ln|x|+C.\]'
          r'\[\boxed{\dfrac{x^2}{2}+2x+\ln|x|+C}\]'),
         (r'\(\displaystyle\int(x^{1/2}+x^{-1/2})^2\,dx\)',
          r'Expand: \(x+2+x^{-1}\).'
          r'\[\dfrac{x^2}{2}+2x+\ln|x|+C.\]'
          r'\[\boxed{\dfrac{x^2}{2}+2x+\ln|x|+C}\]'),
         (r'\(\displaystyle\int\dfrac{2x^3-x}{x^2}\,dx\)',
          r'Split: \(2x-x^{-1}\).'
          r'\[x^2-\ln|x|+C.\]'
          r'\[\boxed{x^2-\ln|x|+C}\]'),
         (r'\(\displaystyle\int(3x+1)(x-2)\,dx\)',
          r'Expand: \(3x^2-6x+x-2=3x^2-5x-2\).'
          r'\[x^3-\dfrac{5x^2}{2}-2x+C.\]'
          r'\[\boxed{x^3-\dfrac{5x^2}{2}-2x+C}\]'),
         (r'\(\displaystyle\int\dfrac{x^2-1}{x+1}\,dx\) for \(x\neq -1\)',
          r'Polynomial division: \(x-1\).'
          r'\[\dfrac{x^2}{2}-x+C.\]'
          r'\[\boxed{\dfrac{x^2}{2}-x+C}\]'),
         (r'\(\displaystyle\int x\sqrt{x}\,dx\)',
          r'Write \(x^{3/2}\).'
          r'\[\dfrac{2}{5}x^{5/2}+C.\]'
          r'\[\boxed{\dfrac{2}{5}x^{5/2}+C}\]'),
         (r'\(\displaystyle\int\dfrac{4}{x^2}\sqrt{x}\,dx\)',
          r'\(4x^{-2}x^{1/2}=4x^{-3/2}\).'
          r'\[4\cdot\dfrac{x^{-1/2}}{-1/2}+C=-8x^{-1/2}+C.\]'
          r'\[\boxed{-8x^{-1/2}+C}\]'),
         (r'\(\displaystyle\int(e^x+1)^2\,dx\)',
          r'Expand: \(e^{2x}+2e^x+1\).'
          r'\[\dfrac{e^{2x}}{2}+2e^x+x+C.\]'
          r'\[\boxed{\dfrac{e^{2x}}{2}+2e^x+x+C}\]'),
         (r'\(\displaystyle\int\dfrac{x+2}{\sqrt{x}}\,dx\)',
          r'Write \(x^{1/2}+2x^{-1/2}\).'
          r'\[\dfrac{2}{3}x^{3/2}+4x^{1/2}+C.\]'
          r'\[\boxed{\dfrac{2}{3}x^{3/2}+4\sqrt{x}+C}\]'),
         (r'\(\displaystyle\int(2x-1)^2(x)\,dx\)',
          r'Expand \((4x^2-4x+1)x=4x^3-4x^2+x\).'
          r'\[x^4-\dfrac{4x^3}{3}+\dfrac{x^2}{2}+C.\]'
          r'\[\boxed{x^4-\dfrac{4x^3}{3}+\dfrac{x^2}{2}+C}\]'),
         (r'\(\displaystyle\int\dfrac{3x^2+6x}{x+2}\,dx\)',
          r'Factor numerator \(3x(x+2)\), cancel for \(x\neq -2\): \(3x\).'
          r'\[\dfrac{3x^2}{2}+C.\]'
          r'\[\boxed{\dfrac{3x^2}{2}+C}\]'),
         (r'\(\displaystyle\int\left(x+\dfrac{1}{x}\right)^2\,dx\)',
          r'Expand: \(x^2+2+x^{-2}\).'
          r'\[\dfrac{x^3}{3}+2x-\dfrac{1}{x}+C.\]'
          r'\[\boxed{\dfrac{x^3}{3}+2x-\dfrac{1}{x}+C}\]'),
         (r'\(\displaystyle\int\dfrac{x^3-8}{x-2}\,dx\) for \(x\neq 2\)',
          r'\(x^3-8=(x-2)(x^2+2x+4)\), so integrand \(x^2+2x+4\).'
          r'\[\dfrac{x^3}{3}+x^2+4x+C.\]'
          r'\[\boxed{\dfrac{x^3}{3}+x^2+4x+C}\]'),
     ]),
    ]


def _int_5a(_set):
    return [
_set('w5a-set4', '5A Set 4', 'WEEK 5A · SET 4 OF 5', 'Student Notes Week 5A (filled-in)',
     'Multi-piece definite integrals',
     r'From Week 5A: multi-step definite integrals that split into sums or use properties without substitution.',
     [
         r'Split \(\displaystyle\int_a^b(f+g)=\int_a^b f+\int_a^b g\) and evaluate each piece.',
         r'Use \(\displaystyle\int_a^b=-\int_b^a\) and additivity over adjacent intervals.',
         r'Combine polynomial and simple trig/exp pieces carefully with FTC.',
     ],
     r'\(\displaystyle\int_0^1(x^2+2x)\,dx+\displaystyle\int_1^2 3\,dx=\dfrac43+1+3=\dfrac{16}{3}\).',
     [r'Split sums inside the integral.', 'FTC on each antiderivative.', 'Mind the order of limits.', 'Exact fractions.', r'No \(+C\) for definite.'],
     [r"\(\displaystyle\int_a^b f=F(b)-F(a)\)", r'\(\displaystyle\int_a^c+\int_c^b=\int_a^b\)'],
     [
         (r'\(\displaystyle\int_0^2(3x^2-4x+1)\,dx\)',
          r'Antiderivative \(x^3-2x^2+x\).'
          r'\[\bigl[x^3-2x^2+x\bigr]_0^2=8-8+2=2.\]'
          r'\[\boxed{2}\]'),
         (r'\(\displaystyle\int_1^3(x^2-1)\,dx+\displaystyle\int_3^4 2\,dx\)',
          r'First: \(\bigl[\tfrac{x^3}{3}-x\bigr]_1^3=(9-3)-(\tfrac13-1)=\tfrac{14}{3}\). Second: \(2\).'
          r'\[\dfrac{14}{3}+2=\dfrac{20}{3}.\]'
          r'\[\boxed{\dfrac{20}{3}}\]'),
         (r'\(\displaystyle\int_0^{\pi}(\sin x+1)\,dx\)',
          r'\[\bigl[-\cos x+x\bigr]_0^{\pi}=(1+\pi)-(-1)=\pi+2.\]'
          r'\[\boxed{\pi+2}\]'),
         (r'\(\displaystyle\int_{-1}^1(x^3+x^2)\,dx\)',
          r'\(x^3\) is odd (integral \(0\) on symmetric interval); \(x^2\) even.'
          r'\[\bigl[\tfrac{x^4}{4}+\tfrac{x^3}{3}\bigr]_{-1}^1=\bigl(\tfrac14+\tfrac13\bigr)-\bigl(\tfrac14-\tfrac13\bigr)=\dfrac{2}{3}.\]'
          r'\[\boxed{\dfrac{2}{3}}\]'),
         (r'\(\displaystyle\int_0^1 e^{2x}\,dx+\displaystyle\int_0^1 x\,dx\)',
          r'\[\bigl[\tfrac12 e^{2x}\bigr]_0^1+\bigl[\tfrac{x^2}{2}\bigr]_0^1=\tfrac12(e^2-1)+\tfrac12.\]'
          r'\[\boxed{\dfrac{e^2}{2}}\]'),
         (r'\(\displaystyle\int_2^5\dfrac{1}{x^2}\,dx+\displaystyle\int_1^2 x\,dx\)',
          r'\[\bigl[-x^{-1}\bigr]_2^5+\bigl[\tfrac{x^2}{2}\bigr]_1^2=\bigl(-\tfrac15+\tfrac12\bigr)+\bigl(2-\tfrac12\bigr)=\dfrac{3}{10}+\dfrac{3}{2}=\dfrac{9}{5}.\]'
          r'\[\boxed{\dfrac{9}{5}}\]'),
         (r'\(\displaystyle\int_0^2|x-1|\,dx\)',
          r'Split at \(x=1\): \(\displaystyle\int_0^1(1-x)\,dx+\int_1^2(x-1)\,dx=\tfrac12+\tfrac12=1\).'
          r'\[\boxed{1}\]'),
         (r'\(\displaystyle\int_0^3(2x+1)\,dx-\displaystyle\int_0^1(2x+1)\,dx\)',
          r'Equals \(\displaystyle\int_1^3(2x+1)\,dx=\bigl[x^2+x\bigr]_1^3=(9+3)-(1+1)=10\).'
          r'\[\boxed{10}\]'),
         (r'\(\displaystyle\int_0^{\pi/2}(\cos x+\sin x)\,dx\)',
          r'\[\bigl[\sin x-\cos x\bigr]_0^{\pi/2}=(1-0)-(0-1)=2.\]'
          r'\[\boxed{2}\]'),
         (r'\(\displaystyle\int_1^e\dfrac{1}{x}\,dx+\displaystyle\int_e^{e^2}\dfrac{1}{x}\,dx\)',
          r'\[\ln e+\ln(e^2)-\ln e=1+2-1=2.\]'
          r'\[\boxed{2}\]'),
         (r'\(\displaystyle\int_0^1(4x^3-3x^2+2)\,dx\)',
          r'\[\bigl[x^4-x^3+2x\bigr]_0^1=1-1+2=2.\]'
          r'\[\boxed{2}\]'),
         (r'\(\displaystyle\int_{-2}^0(x+2)^2\,dx\)',
          r'Antiderivative \(\tfrac{(x+2)^3}{3}\).'
          r'\[\bigl[\tfrac{(x+2)^3}{3}\bigr]_{-2}^0=\dfrac{8}{3}-0=\dfrac{8}{3}.\]'
          r'\[\boxed{\dfrac{8}{3}}\]'),
         (r'\(\displaystyle\int_0^2(x^2+x+1)\,dx+\displaystyle\int_2^3 1\,dx\)',
          r'First \(\bigl[\tfrac{x^3}{3}+\tfrac{x^2}{2}+x\bigr]_0^2=\tfrac83+2+2=\tfrac{20}{3}\); plus \(1\).'
          r'\[\dfrac{23}{3}.\]'
          r'\[\boxed{\dfrac{23}{3}}\]'),
         (r'\(\displaystyle\int_0^{\pi/4}\sec^2 x\,dx+\displaystyle\int_0^{\pi/4}\cos x\,dx\)',
          r'\[\tan(\pi/4)+\sin(\pi/4)=1+\dfrac{\sqrt{2}}{2}.\]'
          r'\[\boxed{1+\dfrac{\sqrt{2}}{2}}\]'),
         (r'\(\displaystyle\int_0^1(x+1)^2\,dx\)',
          r'Expand or reverse chain: \(\bigl[\tfrac{(x+1)^3}{3}\bigr]_0^1=\dfrac{8}{3}-\dfrac{1}{3}=\dfrac{7}{3}\).'
          r'\[\boxed{\dfrac{7}{3}}\]'),
     ]),
_set('w5a-set5', '5A Set 5', 'WEEK 5A · SET 5 OF 5', 'Student Notes Week 5A (filled-in)',
     'Area under curves using intercepts',
     r'From Week 5A: exam-style area problems that need \(x\)-intercepts as limits.',
     [
         r'Find where \(y=0\) to determine the interval of integration when bounds are not given.',
         r'Ensure the curve is non-negative on that interval (or take absolute value later in Week 5B).',
         r'Sketch briefly: intercepts set \(a\) and \(b\) for \(\displaystyle\int_a^b y\,dx\).',
     ],
     r'For \(y=4-x^2\), intercepts \(x=\pm 2\); area \(\displaystyle\int_{-2}^2(4-x^2)\,dx=\dfrac{32}{3}\).',
     [r'Solve \(y=0\) for limits.', 'Integrate with FTC.', 'Area units squared.', 'Check positivity on interval.', 'Sketch intercepts.'],
     [r'Area \(=\displaystyle\int_a^b f(x)\,dx\) if \(f\ge 0\)', r'Intercepts: \(f(x)=0\)'],
     [
         (r'Area under \(y=6x-x^2\) from its positive intercepts.',
          r'Zeros: \(x(6-x)=0\Rightarrow x=0,6\).'
          r'\[\int_0^6(6x-x^2)\,dx=\bigl[3x^2-\tfrac{x^3}{3}\bigr]_0^6=108-72=36.\]'
          r'\[\boxed{36}\]'),
         (r'Area under \(y=4-x^2\) above the \(x\)-axis.',
          r'Zeros \(x=\pm 2\).'
          r'\[\int_{-2}^2(4-x^2)\,dx=\bigl[4x-\tfrac{x^3}{3}\bigr]_{-2}^2=\dfrac{32}{3}.\]'
          r'\[\boxed{\dfrac{32}{3}}\]'),
         (r'Area under \(y=x(2-x)\) from \(0\) to the other intercept.',
          r'Other intercept \(x=2\).'
          r'\[\int_0^2(2x-x^2)\,dx=\bigl[x^2-\tfrac{x^3}{3}\bigr]_0^2=\dfrac{4}{3}.\]'
          r'\[\boxed{\dfrac{4}{3}}\]'),
         (r'Area under \(y=\sin x\) from \(0\) to the first positive intercept after \(0\).',
          r'Next zero at \(x=\pi\).'
          r'\[\int_0^{\pi}\sin x\,dx=2.\]'
          r'\[\boxed{2}\]'),
         (r'Area under \(y=9-x^2\) above the axis.',
          r'Zeros \(\pm 3\).'
          r'\[\int_{-3}^3(9-x^2)\,dx=\bigl[9x-\tfrac{x^3}{3}\bigr]_{-3}^3=36.\]'
          r'\[\boxed{36}\]'),
         (r'Area under \(y=3-x\) from \(0\) to its positive intercept.',
          r'Intercept \(x=3\). On \([0,3]\), \(y\ge 0\).'
          r'\[\int_0^3(3-x)\,dx=\bigl[3x-\tfrac{x^2}{2}\bigr]_0^3=\dfrac{9}{2}.\]'
          r'\[\boxed{\dfrac{9}{2}}\]'),
         (r'Area under \(y=\sqrt{x}\) from \(0\) to \(9\).',
          r'\[\int_0^9 x^{1/2}\,dx=\bigl[\tfrac{2}{3}x^{3/2}\bigr]_0^9=18.\]'
          r'\[\boxed{18}\]'),
         (r'Area under \(y=e^x-1\) from \(0\) to \(\ln 2\).',
          r'At \(0\), \(y=0\); on the interval \(y\ge 0\).'
          r'\[\int_0^{\ln 2}(e^x-1)\,dx=\bigl[e^x-x\bigr]_0^{\ln 2}=(2-\ln 2)-1=1-\ln 2.\]'
          r'\[\boxed{1-\ln 2}\]'),
         (r'Area under \(y=2x-x^2\) between intercepts.',
          r'Zeros \(0,2\).'
          r'\[\int_0^2(2x-x^2)\,dx=\dfrac{4}{3}.\]'
          r'\[\boxed{\dfrac{4}{3}}\]'),
         (r'Area under \(y=5\) from \(x=1\) to \(x=4\).',
          r'\[\int_1^4 5\,dx=15.\]'
          r'\[\boxed{15}\]'),
         (r'Area under \(y=x^3\) from \(0\) to \(2\).',
          r'\[\int_0^2 x^3\,dx=4.\]'
          r'\[\boxed{4}\]'),
         (r'Area under \(y=4x-x^3\) for \(x\ge 0\) between intercepts.',
          r'\(x(4-x^2)=0\Rightarrow x=0,2\) (since \(x\ge 0\)).'
          r'\[\int_0^2(4x-x^3)\,dx=\bigl[2x^2-\tfrac{x^4}{4}\bigr]_0^2=8-4=4.\]'
          r'\[\boxed{4}\]'),
         (r'Area under \(y=\cos x\) from \(0\) to \(\pi/2\).',
          r'\[\int_0^{\pi/2}\cos x\,dx=1.\]'
          r'\[\boxed{1}\]'),
         (r'Area under \(y=8-2x\) from \(0\) to the intercept.',
          r'Intercept \(x=4\).'
          r'\[\int_0^4(8-2x)\,dx=\bigl[8x-x^2\bigr]_0^4=32-16=16.\]'
          r'\[\boxed{16}\]'),
         (r'Area under \(y=16-x^2\) above the \(x\)-axis.',
          r'Zeros \(\pm 4\).'
          r'\[\int_{-4}^4(16-x^2)\,dx=\bigl[16x-\tfrac{x^3}{3}\bigr]_{-4}^4=\dfrac{256}{3}.\]'
          r'\[\boxed{\dfrac{256}{3}}\]'),
     ]),
    ]


def _int_5b(_set):
    return [
_set('w5b-set4', '5B Set 4', 'WEEK 5B · SET 4 OF 5', 'Student Notes Week 5B (filled-in)',
     'Signed area traps',
     r'From Week 5B: multi-step problems where the signed integral differs from geometric area.',
     [
         r'The definite integral \(\displaystyle\int_a^b f\) is signed; geometric area uses \(\displaystyle\int_a^b|f|\).',
         r'Split at zeros when the curve crosses the axis inside the interval.',
         r'Compare the signed value with the total area to catch sign traps.',
     ],
     r'\(\displaystyle\int_{-1}^2 x\,dx=\dfrac32\), but area \(=\displaystyle\int_{-1}^0(-x)\,dx+\int_0^2 x\,dx=\dfrac52\).',
     [r'Signed integral can be smaller than area.', 'Split at roots.', 'Negate below-axis pieces for area.', 'Sketch signs.', 'State which quantity is asked.'],
     [r'Area \(=\displaystyle\int_a^b|f|\,dx\)', r'Signed: \(\displaystyle\int_a^b f\,dx\)'],
     [
         (r'Compute \(\displaystyle\int_{-2}^2 x\,dx\) and the corresponding area.',
          r'Signed: odd function \(\Rightarrow 0\). Area: \(2\displaystyle\int_0^2 x\,dx=4\).'
          r'\[\boxed{\text{signed }0,\ \text{area }4}\]'),
         (r'Area under \(y=x^2-1\) from \(-2\) to \(2\).',
          r'Zeros at \(\pm 1\). Below on \([-1,1]\), above on the outer intervals.'
          r'\[2\int_0^1(1-x^2)\,dx+2\int_1^2(x^2-1)\,dx=\dfrac{4}{3}+\dfrac{8}{3}=4.\]'
          r'\[\boxed{4}\]'),
         (r'Signed \(\displaystyle\int_0^{2\pi}\sin x\,dx\) vs area under one full period.',
          r'Signed: \(\bigl[-\cos x\bigr]_0^{2\pi}=0\). Area: \(4\).'
          r'\[\boxed{\text{signed }0,\ \text{area }4}\]'),
         (r'Area under \(y=x(x-3)\) from \(0\) to \(3\).',
          r'On \([0,3]\), \(y\le 0\), so area \(=-\displaystyle\int_0^3(x^2-3x)\,dx=-\bigl[\tfrac{x^3}{3}-\tfrac{3x^2}{2}\bigr]_0^3=\dfrac{9}{2}\).'
          r'\[\boxed{\dfrac{9}{2}}\]'),
         (r'Signed \(\displaystyle\int_0^3(x-2)\,dx\) and the area from \(0\) to \(3\).',
          r'Signed: \(\bigl[\tfrac{x^2}{2}-2x\bigr]_0^3=-\tfrac{3}{2}\). Area: \(\int_0^2(2-x)+\int_2^3(x-2)=\tfrac52\).'
          r'\[\boxed{\text{signed }-\tfrac{3}{2},\ \text{area }\tfrac{5}{2}}\]'),
         (r'Area under \(y=\cos x\) from \(0\) to \(\pi\).',
          r'Positive on \([0,\pi/2]\), negative on \([\pi/2,\pi]\); total area \(2\).'
          r'\[\boxed{2}\]'),
         (r'Area under \(y=x^2-4\) from \(0\) to \(3\).',
          r'Zero at \(x=2\). Below on \([0,2]\), above on \([2,3]\).'
          r'\[\int_0^2(4-x^2)\,dx+\int_2^3(x^2-4)\,dx=\dfrac{16}{3}+\dfrac{7}{3}=\dfrac{23}{3}.\]'
          r'\[\boxed{\dfrac{23}{3}}\]'),
         (r'Signed \(\displaystyle\int_{-1}^1(x^3-x)\,dx\).',
          r'Odd integrand on symmetric interval.'
          r'\[\boxed{0}\]'),
         (r'Area under \(y=x^3-x\) from \(-1\) to \(1\).',
          r'Zeros at \(-1,0,1\). On \([-1,0]\), \(y\ge 0\); on \([0,1]\), \(y\le 0\).'
          r'\[\int_{-1}^0(x^3-x)\,dx+\int_0^1(x-x^3)\,dx=\dfrac12.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'Area under \(y=2-x\) from \(0\) to \(4\).',
          r'Zero at \(x=2\).'
          r'\[\int_0^2(2-x)\,dx+\int_2^4(x-2)\,dx=2+2=4.\]'
          r'\[\boxed{4}\]'),
         (r'Signed \(\displaystyle\int_0^4(2-x)\,dx\).',
          r'\[\bigl[2x-\tfrac{x^2}{2}\bigr]_0^4=8-8=0.\]'
          r'\[\boxed{0}\]'),
         (r'Area under \(y=\sin(2x)\) from \(0\) to \(\pi\).',
          r'One positive and one negative hump of equal area \(1\) each; total area \(2\).'
          r'\[\boxed{2}\]'),
         (r'Area under \(y=x|x|\) from \(-2\) to \(2\).',
          r'For \(x>0\), \(y=x^2\); for \(x<0\), \(y=-x^2\). Total area \(=2\displaystyle\int_0^2 x^2\,dx=\dfrac{16}{3}\).'
          r'\[\boxed{\dfrac{16}{3}}\]'),
         (r'Area under \(y=x^2-x-2\) from \(-1\) to \(2\).',
          r'Factor \((x-2)(x+1)\); zeros \(-1,2\). On \((-1,2)\) the parabola is below the axis.'
          r'Area \(=-\displaystyle\int_{-1}^2(x^2-x-2)\,dx=-\bigl[\tfrac{x^3}{3}-\tfrac{x^2}{2}-2x\bigr]_{-1}^2=\dfrac{9}{2}\).'
          r'\[\boxed{\dfrac{9}{2}}\]'),
         (r'Signed \(\displaystyle\int_0^{2\pi}\cos x\,dx\).',
          r'\[\bigl[\sin x\bigr]_0^{2\pi}=0.\]'
          r'\[\boxed{0}\]'),
     ]),
_set('w5b-set5', '5B Set 5', 'WEEK 5B · SET 5 OF 5', 'Student Notes Week 5B (filled-in)',
     'Area between curves via intersections',
     r'From Week 5B: exam-style area between curves — find intersections, then integrate top minus bottom.',
     [
         r'Solve \(f(x)=g(x)\) to get limits; sketch to see which curve is above.',
         r'Area \(=\displaystyle\int_a^b\bigl(f_{\mathrm{top}}-f_{\mathrm{bottom}}\bigr)\,dx\).',
         r'If curves cross mid-interval, split into subintervals.',
     ],
     r'\(y=x^2\) and \(y=2x\) meet at \(0,2\); area \(\displaystyle\int_0^2(2x-x^2)\,dx=\dfrac43\).',
     [r'Find intersections first.', 'Top minus bottom.', 'Split if they cross again.', 'Exact answers.', 'Sketch quickly.'],
     [r'Area \(=\displaystyle\int_a^b|f-g|\,dx\)', r'Solve \(f=g\) for limits'],
     [
         (r'Area between \(y=x^2\) and \(y=4x-x^2\).',
          r'\(x^2=4x-x^2\Rightarrow 2x^2-4x=0\Rightarrow x=0,2\). On \([0,2]\), \(4x-x^2\) is above.'
          r'\[\int_0^2\bigl((4x-x^2)-x^2\bigr)\,dx=\int_0^2(4x-2x^2)\,dx=\bigl[2x^2-\tfrac{2x^3}{3}\bigr]_0^2=\dfrac{8}{3}.\]'
          r'\[\boxed{\dfrac{8}{3}}\]'),
         (r'Area between \(y=x\) and \(y=x^3\) from their intersections in \([-1,1]\).',
          r'\(x=x^3\Rightarrow x(x^2-1)=0\Rightarrow x=-1,0,1\).'
          r'\[\int_{-1}^0(x^3-x)\,dx+\int_0^1(x-x^3)\,dx=\dfrac12.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'Area between \(y=\sqrt{x}\) and \(y=x/2\).',
          r'\(\sqrt{x}=x/2\Rightarrow x=0\) or \(x=4\). On \([0,4]\), \(\sqrt{x}\) is above.'
          r'\[\int_0^4\bigl(\sqrt{x}-\tfrac{x}{2}\bigr)\,dx=\bigl[\tfrac{2}{3}x^{3/2}-\tfrac{x^2}{4}\bigr]_0^4=\dfrac{16}{3}-4=\dfrac{4}{3}.\]'
          r'\[\boxed{\dfrac{4}{3}}\]'),
         (r'Area between \(y=e^x\) and \(y=x+1\) from \(0\) to \(1\).',
          r'They meet at \(x=0\); on \((0,1]\), \(e^x>x+1\).'
          r'\[\int_0^1(e^x-x-1)\,dx=\bigl[e^x-\tfrac{x^2}{2}-x\bigr]_0^1=e-\tfrac{5}{2}.\]'
          r'\[\boxed{e-\dfrac{5}{2}}\]'),
         (r'Area between \(y=2x\) and \(y=x^2\) from \(0\) to \(2\).',
          r'Intersections at \(0\) and \(2\); line above the parabola.'
          r'\[\int_0^2(2x-x^2)\,dx=\bigl[x^2-\tfrac{x^3}{3}\bigr]_0^2=\dfrac{4}{3}.\]'
          r'\[\boxed{\dfrac{4}{3}}\]'),
         (r'Area between \(y=x+2\) and \(y=x^2\).',
          r'\(x^2-x-2=0\Rightarrow(x-2)(x+1)=0\Rightarrow x=-1,2\). Line above between.'
          r'\[\int_{-1}^2\bigl((x+2)-x^2\bigr)\,dx=\bigl[\tfrac{x^2}{2}+2x-\tfrac{x^3}{3}\bigr]_{-1}^2=\dfrac{9}{2}.\]'
          r'\[\boxed{\dfrac{9}{2}}\]'),
         (r'Area between \(y=\sin x\) and \(y=\cos x\) from \(0\) to \(\pi/4\).',
          r'On \([0,\pi/4]\), \(\cos x\ge\sin x\).'
          r'\[\int_0^{\pi/4}(\cos x-\sin x)\,dx=\bigl[\sin x+\cos x\bigr]_0^{\pi/4}=\sqrt{2}-1.\]'
          r'\[\boxed{\sqrt{2}-1}\]'),
         (r'Area between \(y=4\) and \(y=x^2\) from \(-2\) to \(2\).',
          r'\[\int_{-2}^2(4-x^2)\,dx=\dfrac{32}{3}.\]'
          r'\[\boxed{\dfrac{32}{3}}\]'),
         (r'Area between \(y=x^2\) and \(y=2-x^2\).',
          r'\(x^2=2-x^2\Rightarrow x=\pm 1\). Top is \(2-x^2\).'
          r'\[\int_{-1}^1(2-2x^2)\,dx=\bigl[2x-\tfrac{2x^3}{3}\bigr]_{-1}^1=\dfrac{8}{3}.\]'
          r'\[\boxed{\dfrac{8}{3}}\]'),
         (r'Area between \(y=x\) and \(y=\dfrac{2}{x}\) from \(1\) to \(2\).',
          r'They meet at \(x=\sqrt{2}\). On \([1,\sqrt{2}]\), \(\dfrac{2}{x}\ge x\); on \([\sqrt{2},2]\), \(x\ge\dfrac{2}{x}\).'
          r'\[\int_1^{\sqrt{2}}\bigl(\tfrac{2}{x}-x\bigr)\,dx+\int_{\sqrt{2}}^2\bigl(x-\tfrac{2}{x}\bigr)\,dx=\dfrac{1}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'Area between \(y=e^{-x}\) and \(y=e^{x}\) from \(0\) to \(1\).',
          r'\(e^{x}\ge e^{-x}\) on \([0,1]\).'
          r'\[\int_0^1(e^{x}-e^{-x})\,dx=\bigl[e^{x}+e^{-x}\bigr]_0^1=(e+e^{-1})-2.\]'
          r'\[\boxed{e+e^{-1}-2}\]'),
         (r'Area between \(y=3x\) and \(y=x^2\) from \(0\) to \(3\).',
          r'\[\int_0^3(3x-x^2)\,dx=\bigl[\tfrac{3x^2}{2}-\tfrac{x^3}{3}\bigr]_0^3=\dfrac{27}{2}-9=\dfrac{9}{2}.\]'
          r'\[\boxed{\dfrac{9}{2}}\]'),
         (r'Area between \(y=\sqrt{x}\) and \(y=x\) from \(0\) to \(1\).',
          r'\[\int_0^1(\sqrt{x}-x)\,dx=\bigl[\tfrac{2}{3}x^{3/2}-\tfrac{x^2}{2}\bigr]_0^1=\dfrac{2}{3}-\dfrac{1}{2}=\dfrac{1}{6}.\]'
          r'\[\boxed{\dfrac{1}{6}}\]'),
         (r'Area between \(y=x^2-1\) and \(y=1-x^2\).',
          r'Intersect: \(x^2-1=1-x^2\Rightarrow x=\pm 1\). Top \(1-x^2\).'
          r'\[\int_{-1}^1\bigl((1-x^2)-(x^2-1)\bigr)\,dx=\int_{-1}^1(2-2x^2)\,dx=\dfrac{8}{3}.\]'
          r'\[\boxed{\dfrac{8}{3}}\]'),
         (r'Area between \(y=2\sqrt{x}\) and \(y=x\) from their intersections.',
          r'\(2\sqrt{x}=x\Rightarrow x=0\) or \(x=4\). Top \(2\sqrt{x}\) on \([0,4]\).'
          r'\[\int_0^4(2\sqrt{x}-x)\,dx=\bigl[\tfrac{4}{3}x^{3/2}-\tfrac{x^2}{2}\bigr]_0^4=\dfrac{32}{3}-8=\dfrac{8}{3}.\]'
          r'\[\boxed{\dfrac{8}{3}}\]'),
     ]),
    ]


def _int_5c(_set):
    return [
_set('w5c-set4', '5C Set 4', 'WEEK 5C · SET 4 OF 5', 'Student Notes Week 5C (filled-in)',
     r'Integrals of \(\tan\), \(\sec^2\) and log forms',
     r'From Week 5C: multi-step \(\int\tan\), \(\int\sec^2\) composites, and \(\ln\) forms.',
     [
         r'\(\displaystyle\int\tan x\,dx=-\ln|\cos x|+C=\ln|\sec x|+C\).',
         r'\(\displaystyle\int\sec^2(ax)\,dx=\dfrac{1}{a}\tan(ax)+C\).',
         r'Log forms: \(\displaystyle\int\dfrac{f^{\prime}}{f}=\ln|f|+C\).',
     ],
     r'\(\displaystyle\int\tan(2x)\,dx=-\dfrac12\ln|\cos(2x)|+C\).',
     [r'Remember \(\int\tan\) log form.', r'Chain constant for \(\sec^2(ax)\).', r"\(\int f^{\prime}/f=\ln|f|\).", 'Differentiate to check.', 'Absolute values in logs.'],
     [r'\(\displaystyle\int\tan x\,dx=-\ln|\cos x|+C\)', r'\(\displaystyle\int\sec^2(ax)\,dx=\dfrac{1}{a}\tan(ax)+C\)', r"\(\displaystyle\int\dfrac{f^{\prime}}{f}=\ln|f|+C\)"],
     [
         (r'\(\displaystyle\int\tan(2x)\,dx\)',
          r'Write \(\dfrac{\sin(2x)}{\cos(2x)}\); let \(u=\cos(2x)\), \(du=-2\sin(2x)\,dx\).'
          r'\[-\dfrac{1}{2}\ln|\cos(2x)|+C.\]'
          r'\[\boxed{-\dfrac{1}{2}\ln|\cos(2x)|+C}\]'),
         (r'\(\displaystyle\int\sec^2(3x)\,dx\)',
          r'\[\dfrac{1}{3}\tan(3x)+C.\]'
          r'\[\boxed{\dfrac{1}{3}\tan(3x)+C}\]'),
         (r'\(\displaystyle\int\dfrac{2x}{x^2+4}\,dx\)',
          r'Let \(u=x^2+4\).'
          r'\[\ln(x^2+4)+C.\]'
          r'\[\boxed{\ln(x^2+4)+C}\]'),
         (r'\(\displaystyle\int\dfrac{\cos x}{\sin x}\,dx\)',
          r'\[\ln|\sin x|+C.\]'
          r'\[\boxed{\ln|\sin x|+C}\]'),
         (r'\(\displaystyle\int\tan x\sec^2 x\,dx\)',
          r'Let \(u=\tan x\), \(du=\sec^2 x\,dx\).'
          r'\[\dfrac{\tan^2 x}{2}+C.\]'
          r'\[\boxed{\dfrac{\tan^2 x}{2}+C}\]'),
         (r'\(\displaystyle\int\dfrac{1}{x\ln x}\,dx\)',
          r'Let \(u=\ln x\).'
          r'\[\ln|\ln x|+C.\]'
          r'\[\boxed{\ln|\ln x|+C}\]'),
         (r'\(\displaystyle\int\sec^2(x/2)\,dx\)',
          r'\[2\tan(x/2)+C.\]'
          r'\[\boxed{2\tan(x/2)+C}\]'),
         (r'\(\displaystyle\int\dfrac{e^{2x}}{e^{2x}+5}\,dx\)',
          r'\[\dfrac{1}{2}\ln(e^{2x}+5)+C.\]'
          r'\[\boxed{\dfrac{1}{2}\ln(e^{2x}+5)+C}\]'),
         (r'\(\displaystyle\int(1+\tan^2 x)\,dx\)',
          r'\(1+\tan^2 x=\sec^2 x\).'
          r'\[\tan x+C.\]'
          r'\[\boxed{\tan x+C}\]'),
         (r'\(\displaystyle\int\dfrac{3}{2x-1}\,dx\)',
          r'\[\dfrac{3}{2}\ln|2x-1|+C.\]'
          r'\[\boxed{\dfrac{3}{2}\ln|2x-1|+C}\]'),
         (r'\(\displaystyle\int\tan(x)\cdot 2\,dx\)',
          r'\[-2\ln|\cos x|+C.\]'
          r'\[\boxed{-2\ln|\cos x|+C}\]'),
         (r'\(\displaystyle\int\dfrac{\sec^2 x}{\tan x}\,dx\)',
          r'Let \(u=\tan x\).'
          r'\[\ln|\tan x|+C.\]'
          r'\[\boxed{\ln|\tan x|+C}\]'),
         (r'\(\displaystyle\int_0^{\pi/4}\sec^2 x\,dx\)',
          r'\[\bigl[\tan x\bigr]_0^{\pi/4}=1.\]'
          r'\[\boxed{1}\]'),
         (r'\(\displaystyle\int\dfrac{4x+2}{x^2+x}\,dx\)',
          r'Numerator is \(2(2x+1)\) and derivative of denominator is \(2x+1\).'
          r'\[2\ln|x^2+x|+C.\]'
          r'\[\boxed{2\ln|x^2+x|+C}\]'),
         (r'\(\displaystyle\int\sec x\tan x\,dx\)',
          r'\[\sec x+C.\]'
          r'\[\boxed{\sec x+C}\]'),
     ]),
_set('w5c-set5', '5C Set 5', 'WEEK 5C · SET 5 OF 5', 'Student Notes Week 5C (filled-in)',
     'Mixed log and trig integrals',
     r'From Week 5C: exam-style mixed integrals combining log and trig techniques.',
     [
         r'Identify whether the integrand is a log form, a basic trig reverse, or needs an identity.',
         r'Mixed definite integrals combine FTC with these antiderivatives.',
         r'Simplify with identities (\(\sin^2\), \(\tan=\sin/\cos\)) when helpful.',
     ],
     r'\(\displaystyle\int_0^{\pi/4}\tan x\,dx=\bigl[-\ln|\cos x|\bigr]_0^{\pi/4}=\dfrac12\ln 2\).',
     [r'Choose log vs trig reverse.', 'Identities before integrating.', 'Change of form for composites.', 'Evaluate definite carefully.', r'Check domain of \(\ln\).'],
     [r'\(\displaystyle\int\sin=\!-\!\cos\)', r'\(\displaystyle\int\cos=\sin\)', r'\(\displaystyle\int\tan=-\ln|\cos|\)'],
     [
         (r'\(\displaystyle\int_0^{\pi/4}\tan x\,dx\)',
          r'\[\bigl[-\ln|\cos x|\bigr]_0^{\pi/4}=-\ln(\tfrac{\sqrt{2}}{2})+\ln 1=\dfrac{1}{2}\ln 2.\]'
          r'\[\boxed{\dfrac{1}{2}\ln 2}\]'),
         (r'\(\displaystyle\int(\sin x+2\cos x)\,dx\)',
          r'\[-\cos x+2\sin x+C.\]'
          r'\[\boxed{-\cos x+2\sin x+C}\]'),
         (r'\(\displaystyle\int\dfrac{\cos x}{1+\sin x}\,dx\)',
          r'Let \(u=1+\sin x\).'
          r'\[\ln|1+\sin x|+C.\]'
          r'\[\boxed{\ln|1+\sin x|+C}\]'),
         (r'\(\displaystyle\int\sin^2 x\,dx\)',
          r'Use \(\sin^2 x=\dfrac{1-\cos 2x}{2}\).'
          r'\[\dfrac{x}{2}-\dfrac{\sin 2x}{4}+C.\]'
          r'\[\boxed{\dfrac{x}{2}-\dfrac{\sin 2x}{4}+C}\]'),
         (r'\(\displaystyle\int_{\pi/6}^{\pi/2}\cot x\,dx\)',
          r'\[\bigl[\ln|\sin x|\bigr]_{\pi/6}^{\pi/2}=\ln 1-\ln\tfrac12=\ln 2.\]'
          r'\[\boxed{\ln 2}\]'),
         (r'\(\displaystyle\int e^x\sin(e^x)\,dx\)',
          r'Let \(u=e^x\).'
          r'\[-\cos(e^x)+C.\]'
          r'\[\boxed{-\cos(e^x)+C}\]'),
         (r'\(\displaystyle\int\dfrac{1+\cos x}{\sin x}\,dx\)',
          r'Write \(\csc x+\dfrac{\cos x}{\sin x}=\csc x+\cot x\), or split as \(\dfrac{1}{\sin x}+\dfrac{\cos x}{\sin x}\).'
          r'\[\ln\left|\dfrac{\sin x}{1+\cos x}\right|+C.\]'
          r'\[\boxed{\ln\left|\dfrac{\sin x}{1+\cos x}\right|+C}\]'),
         (r'\(\displaystyle\int_0^{\pi/2}\cos^2 x\sin x\,dx\)',
          r'Let \(u=\cos x\), \(u:1\to 0\).'
          r'\[\int_1^0 u^2(-du)=\int_0^1 u^2\,du=\dfrac{1}{3}.\]'
          r'\[\boxed{\dfrac{1}{3}}\]'),
         (r'\(\displaystyle\int\dfrac{2\sin x\cos x}{\sin^2 x+1}\,dx\)',
          r'Let \(u=\sin^2 x+1\).'
          r'\[\ln(\sin^2 x+1)+C.\]'
          r'\[\boxed{\ln(\sin^2 x+1)+C}\]'),
         (r'\(\displaystyle\int(\sec^2 x+\tan x)\,dx\)',
          r'\[\tan x-\ln|\cos x|+C.\]'
          r'\[\boxed{\tan x-\ln|\cos x|+C}\]'),
         (r'\(\displaystyle\int_1^e\dfrac{\ln x}{x}\,dx\)',
          r'Let \(u=\ln x\): \(\displaystyle\int_0^1 u\,du=\dfrac12\).'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'\(\displaystyle\int\cos(2x)\sin(2x)\,dx\)',
          r'Let \(u=\sin(2x)\), \(du=2\cos(2x)\,dx\).'
          r'\[\dfrac{\sin^2(2x)}{4}+C.\]'
          r'\[\boxed{\dfrac{\sin^2(2x)}{4}+C}\]'),
         (r'\(\displaystyle\int\dfrac{x}{x^2+1}\,dx\)',
          r'\[\dfrac{1}{2}\ln(x^2+1)+C.\]'
          r'\[\boxed{\dfrac{1}{2}\ln(x^2+1)+C}\]'),
         (r'\(\displaystyle\int_0^{\pi/3}\sec^2 x\,dx\)',
          r'\[\bigl[\tan x\bigr]_0^{\pi/3}=\sqrt{3}.\]'
          r'\[\boxed{\sqrt{3}}\]'),
         (r'\(\displaystyle\int\dfrac{\cos(3x)}{\sin(3x)}\,dx\)',
          r'\[\dfrac{1}{3}\ln|\sin(3x)|+C.\]'
          r'\[\boxed{\dfrac{1}{3}\ln|\sin(3x)|+C}\]'),
     ]),
    ]


def _int_5d(_set):
    return [
_set('w5d-set4', '5D Set 4', 'WEEK 5D · SET 4 OF 5', 'Student Notes Week 5D (filled-in)',
     'Non-obvious substitutions',
     r'From Week 5D: multi-step substitutions where \(u\) is not the most obvious inner expression.',
     [
         r'Sometimes \(u\) is a product, a power of a trig function, or \(\ln\) of an expression.',
         r'Adjust constants so that \(du\) matches the remaining factor.',
         r'Always differentiate the answer to verify.',
     ],
     r'\(\displaystyle\int\dfrac{\ln x}{x}\,dx\): \(u=\ln x\Rightarrow\dfrac{u^2}{2}+C\).',
     [r'Hunt for \(u\) whose derivative appears.', 'Scale constants carefully.', 'Back-substitute.', 'Verify by differentiation.', r'Trig powers: try \(u=\sin\) or \(u=\cos\).'],
     [r"\(u=g(x),\ du=g^{\prime}(x)\,dx\)", r'\(\displaystyle\int f(g)g^{\prime}=\int f(u)\,du\)'],
     [
         (r'\(\displaystyle\int\dfrac{\ln(3x)}{x}\,dx\)',
          r'Let \(u=\ln(3x)\), \(du=\dfrac{1}{x}\,dx\).'
          r'\[\dfrac{(\ln(3x))^2}{2}+C.\]'
          r'\[\boxed{\dfrac{(\ln(3x))^2}{2}+C}\]'),
         (r'\(\displaystyle\int\dfrac{x}{(x^2+1)\ln(x^2+1)}\,dx\)',
          r'Let \(u=\ln(x^2+1)\), \(du=\dfrac{2x}{x^2+1}\,dx\).'
          r'\[\dfrac{1}{2}\ln|\ln(x^2+1)|+C.\]'
          r'\[\boxed{\dfrac{1}{2}\ln|\ln(x^2+1)|+C}\]'),
         (r'\(\displaystyle\int\sin^2 x\cos^3 x\,dx\)',
          r'Write \(\cos^3 x=\cos x(1-\sin^2 x)\); let \(u=\sin x\).'
          r'\[\int u^2(1-u^2)\,du=\dfrac{u^3}{3}-\dfrac{u^5}{5}+C=\dfrac{\sin^3 x}{3}-\dfrac{\sin^5 x}{5}+C.\]'
          r'\[\boxed{\dfrac{\sin^3 x}{3}-\dfrac{\sin^5 x}{5}+C}\]'),
         (r'\(\displaystyle\int\dfrac{e^{\sqrt{x}}}{\sqrt{x}}\,dx\)',
          r'Let \(u=\sqrt{x}\), \(du=\dfrac{1}{2\sqrt{x}}\,dx\).'
          r'\[2e^{\sqrt{x}}+C.\]'
          r'\[\boxed{2e^{\sqrt{x}}+C}\]'),
         (r'\(\displaystyle\int\dfrac{1}{x\sqrt{1+\ln x}}\,dx\)',
          r'Let \(u=1+\ln x\).'
          r'\[2\sqrt{1+\ln x}+C.\]'
          r'\[\boxed{2\sqrt{1+\ln x}+C}\]'),
         (r'\(\displaystyle\int x^3\sqrt{x^2+1}\,dx\)',
          r'Write \(x^2\cdot x\sqrt{x^2+1}\). Let \(u=x^2+1\), \(x^2=u-1\), \(du=2x\,dx\).'
          r'\[\dfrac{1}{2}\int(u-1)\sqrt{u}\,du=\dfrac{1}{2}\int(u^{3/2}-u^{1/2})\,du=\dfrac{1}{2}\bigl(\tfrac{2}{5}u^{5/2}-\tfrac{2}{3}u^{3/2}\bigr)+C.\]'
          r'\[\boxed{\dfrac{1}{5}(x^2+1)^{5/2}-\dfrac{1}{3}(x^2+1)^{3/2}+C}\]'),
         (r'\(\displaystyle\int\dfrac{\cos x}{1+\sin x}\,dx\)',
          r'Let \(u=1+\sin x\), \(du=\cos x\,dx\).'
          r'\[\ln|1+\sin x|+C.\]'
          r'\[\boxed{\ln|1+\sin x|+C}\]'),
         (r'\(\displaystyle\int\dfrac{2x+3}{\sqrt{x^2+3x}}\,dx\)',
          r'Let \(u=x^2+3x\), \(du=(2x+3)\,dx\).'
          r'\[2\sqrt{x^2+3x}+C.\]'
          r'\[\boxed{2\sqrt{x^2+3x}+C}\]'),
         (r'\(\displaystyle\int\tan^3 x\sec^2 x\,dx\)',
          r'Let \(u=\tan x\).'
          r'\[\dfrac{\tan^4 x}{4}+C.\]'
          r'\[\boxed{\dfrac{\tan^4 x}{4}+C}\]'),
         (r'\(\displaystyle\int\dfrac{x^2}{e^{x^3}}\,dx\)',
          r'Write \(x^2 e^{-x^3}\); let \(u=x^3\).'
          r'\[-\dfrac{1}{3}e^{-x^3}+C.\]'
          r'\[\boxed{-\dfrac{1}{3}e^{-x^3}+C}\]'),
         (r'\(\displaystyle\int\dfrac{1}{(2x+1)\ln(2x+1)}\,dx\)',
          r'Let \(u=\ln(2x+1)\), \(du=\dfrac{2}{2x+1}\,dx\).'
          r'\[\dfrac{1}{2}\ln|\ln(2x+1)|+C.\]'
          r'\[\boxed{\dfrac{1}{2}\ln|\ln(2x+1)|+C}\]'),
         (r'\(\displaystyle\int\cos x\cdot\sin(\sin x)\,dx\)',
          r'Let \(u=\sin x\).'
          r'\[-\cos(\sin x)+C.\]'
          r'\[\boxed{-\cos(\sin x)+C}\]'),
         (r'\(\displaystyle\int\dfrac{3x^2+2}{x^3+2x}\,dx\)',
          r'Derivative of denominator is \(3x^2+2\).'
          r'\[\ln|x^3+2x|+C.\]'
          r'\[\boxed{\ln|x^3+2x|+C}\]'),
         (r'\(\displaystyle\int x(1-x^2)^5\,dx\)',
          r'Let \(u=1-x^2\), \(du=-2x\,dx\).'
          r'\[-\dfrac{(1-x^2)^6}{12}+C.\]'
          r'\[\boxed{-\dfrac{(1-x^2)^6}{12}+C}\]'),
         (r'\(\displaystyle\int\dfrac{e^{2x}}{\sqrt{1+e^{2x}}}\,dx\)',
          r'Let \(u=1+e^{2x}\), \(du=2e^{2x}\,dx\).'
          r'\[\sqrt{1+e^{2x}}+C.\]'
          r'\[\boxed{\sqrt{1+e^{2x}}+C}\]'),
     ]),
_set('w5d-set5', '5D Set 5', 'WEEK 5D · SET 5 OF 5', 'Student Notes Week 5D (filled-in)',
     'Definite integrals with changed limits',
     r'From Week 5D: exam-style definite substitution with changed \(u\)-limits.',
     [
         r'When substituting on a definite integral, convert limits: \(x=a\mapsto u(a)\), \(x=b\mapsto u(b)\).',
         r'Do not mix \(x\) and \(u\) in the final evaluation.',
         r'Watch the sign if \(du\) introduces a negative constant.',
     ],
     r'\(\displaystyle\int_0^1 2x(x^2+1)^2\,dx\): \(u=x^2+1\) from \(1\) to \(2\) gives \(\dfrac73\).',
     [r'Change limits with \(u\).', r'Or back-substitute then use \(x\)-limits.', 'Include Jacobian constants.', 'Order of limits matters.', r'FTC in \(u\).'],
     [r"\(\displaystyle\int_a^b f(g)g^{\prime}=\int_{g(a)}^{g(b)} f(u)\,du\)"],
     [
         (r'\(\displaystyle\int_0^2 x\sqrt{x^2+1}\,dx\)',
          r'\(u=x^2+1\): \(1\to 5\), \(du=2x\,dx\).'
          r'\[\dfrac{1}{2}\int_1^5\sqrt{u}\,du=\dfrac{1}{3}\bigl[u^{3/2}\bigr]_1^5=\dfrac{5\sqrt{5}-1}{3}.\]'
          r'\[\boxed{\dfrac{5\sqrt{5}-1}{3}}\]'),
         (r'\(\displaystyle\int_0^{\pi/2}\sin x\cos^2 x\,dx\)',
          r'\(u=\cos x\): \(1\to 0\).'
          r'\[\int_1^0 u^2(-du)=\int_0^1 u^2\,du=\dfrac{1}{3}.\]'
          r'\[\boxed{\dfrac{1}{3}}\]'),
         (r'\(\displaystyle\int_1^e\dfrac{\ln x}{x}\,dx\)',
          r'\(u=\ln x\): \(0\to 1\).'
          r'\[\int_0^1 u\,du=\dfrac{1}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'\(\displaystyle\int_0^1\dfrac{2x}{(x^2+1)^2}\,dx\)',
          r'\(u=x^2+1\): \(1\to 2\).'
          r'\[\int_1^2 u^{-2}\,du=\bigl[-u^{-1}\bigr]_1^2=\dfrac{1}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'\(\displaystyle\int_0^{\ln 3} e^{2x}\,dx\)',
          r'\(u=2x\): \(0\to 2\ln 3\), or directly.'
          r'\[\bigl[\tfrac12 e^{2x}\bigr]_0^{\ln 3}=\tfrac12(9-1)=4.\]'
          r'\[\boxed{4}\]'),
         (r'\(\displaystyle\int_0^{\pi/4}\tan x\sec^2 x\,dx\)',
          r'\(u=\tan x\): \(0\to 1\).'
          r'\[\int_0^1 u\,du=\dfrac{1}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'\(\displaystyle\int_1^2\dfrac{x}{x^2+1}\,dx\)',
          r'\(u=x^2+1\): \(2\to 5\).'
          r'\[\dfrac{1}{2}\int_2^5\dfrac{du}{u}=\dfrac{1}{2}\ln\dfrac{5}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}\ln\dfrac{5}{2}}\]'),
         (r'\(\displaystyle\int_0^1 x e^{x^2}\,dx\)',
          r'\(u=x^2\): \(0\to 1\).'
          r'\[\dfrac{1}{2}\int_0^1 e^{u}\,du=\dfrac{e-1}{2}.\]'
          r'\[\boxed{\dfrac{e-1}{2}}\]'),
         (r'\(\displaystyle\int_0^{\pi/6}\sin(2x)\,dx\)',
          r'\(u=2x\): \(0\to\pi/3\).'
          r'\[\dfrac{1}{2}\int_0^{\pi/3}\sin u\,du=\dfrac{1}{2}.\]'
          r'\[\boxed{\dfrac{1}{2}}\]'),
         (r'\(\displaystyle\int_0^3\dfrac{x}{\sqrt{x^2+16}}\,dx\)',
          r'\(u=x^2+16\): \(16\to 25\).'
          r'\[\dfrac{1}{2}\int_{16}^{25}u^{-1/2}\,du=\bigl[\sqrt{u}\bigr]_{16}^{25}=5-4=1.\]'
          r'\[\boxed{1}\]'),
         (r'\(\displaystyle\int_0^1(2x+1)^3\,dx\)',
          r'\(u=2x+1\): \(1\to 3\).'
          r'\[\dfrac{1}{2}\int_1^3 u^3\,du=\dfrac{1}{8}\bigl[u^4\bigr]_1^3=\dfrac{80}{8}=10.\]'
          r'\[\boxed{10}\]'),
         (r'\(\displaystyle\int_1^4\dfrac{1}{\sqrt{x}(1+\sqrt{x})}\,dx\)',
          r'Let \(u=1+\sqrt{x}\), \(du=\dfrac{1}{2\sqrt{x}}\,dx\). Limits \(2\to 3\).'
          r'\[2\int_2^3\dfrac{du}{u}=2\ln\dfrac{3}{2}.\]'
          r'\[\boxed{2\ln\dfrac{3}{2}}\]'),
         (r'\(\displaystyle\int_0^{\pi/2}\dfrac{\sin x}{1+\cos x}\,dx\)',
          r'\(u=1+\cos x\): \(2\to 1\).'
          r'\[\int_2^1\dfrac{-du}{u}=\ln 2.\]'
          r'\[\boxed{\ln 2}\]'),
         (r'\(\displaystyle\int_0^1\dfrac{e^x}{e^x+1}\,dx\)',
          r'\(u=e^x+1\): \(2\to e+1\).'
          r'\[\ln(e+1)-\ln 2=\ln\dfrac{e+1}{2}.\]'
          r'\[\boxed{\ln\dfrac{e+1}{2}}\]'),
         (r'\(\displaystyle\int_0^{\sqrt{\pi}} 2x\cos(x^2)\,dx\)',
          r'\(u=x^2\): \(0\to\pi\).'
          r'\[\int_0^{\pi}\cos u\,du=0.\]'
          r'\[\boxed{0}\]'),
     ]),
    ]


def _int_6a(_set):
    return [
_set('w6a-set4', '6A Set 4', 'WEEK 6A · SET 4 OF 5', 'Student Notes Week 6A (filled-in)',
     'Harder composite substitutions',
     r'From Week 6A: multi-step composites mixing exponential, trig, and algebraic insides.',
     [
         r'Look for an inner function whose derivative (up to a constant) multiplies the outer factor.',
         r'Composites like \(e^{\sin x}\cos x\) or \(\dfrac{f^{\prime}}{\sqrt{f}}\) are standard patterns.',
         r'Scale carefully when the derivative differs by a constant factor.',
     ],
     r'\(\displaystyle\int\cos x\,e^{\sin x}\,dx=e^{\sin x}+C\).',
     [r'Match derivative of the inside.', 'Scale constants.', 'Back-substitute.', 'Trig + exp common.', 'Verify by differentiating.'],
     [r"\(\displaystyle\int f^{\prime}e^{f}=e^{f}+C\)", r"\(\displaystyle\int f^{\prime}/\sqrt{f}=2\sqrt{f}+C\)"],
     [
         (r'\(\displaystyle\int\cos(2x)\,e^{\sin(2x)}\,dx\)',
          r'Let \(u=\sin(2x)\), \(du=2\cos(2x)\,dx\).'
          r'\[\dfrac{1}{2}e^{\sin(2x)}+C.\]'
          r'\[\boxed{\dfrac{1}{2}e^{\sin(2x)}+C}\]'),
         (r'\(\displaystyle\int\dfrac{2x}{\sqrt{1+x^2}}\,dx\)',
          r'\[2\sqrt{1+x^2}+C.\]'
          r'\[\boxed{2\sqrt{1+x^2}+C}\]'),
         (r'\(\displaystyle\int x^2\cos(x^3)\,dx\)',
          r'\[\dfrac{1}{3}\sin(x^3)+C.\]'
          r'\[\boxed{\dfrac{1}{3}\sin(x^3)+C}\]'),
         (r'\(\displaystyle\int\dfrac{\sec^2 x}{1+\tan x}\,dx\)',
          r'Let \(u=1+\tan x\).'
          r'\[\ln|1+\tan x|+C.\]'
          r'\[\boxed{\ln|1+\tan x|+C}\]'),
         (r'\(\displaystyle\int\dfrac{e^{3x}}{e^{3x}+4}\,dx\)',
          r'\[\dfrac{1}{3}\ln(e^{3x}+4)+C.\]'
          r'\[\boxed{\dfrac{1}{3}\ln(e^{3x}+4)+C}\]'),
         (r'\(\displaystyle\int\sin x\cos x\,e^{\sin^2 x}\,dx\)',
          r'Let \(u=\sin^2 x\), \(du=2\sin x\cos x\,dx\).'
          r'\[\dfrac{1}{2}e^{\sin^2 x}+C.\]'
          r'\[\boxed{\dfrac{1}{2}e^{\sin^2 x}+C}\]'),
         (r'\(\displaystyle\int\dfrac{1}{x(\ln x)^2}\,dx\)',
          r'Let \(u=\ln x\).'
          r'\[-\dfrac{1}{\ln x}+C.\]'
          r'\[\boxed{-\dfrac{1}{\ln x}+C}\]'),
         (r'\(\displaystyle\int\dfrac{x+1}{(x^2+2x+5)^2}\,dx\)',
          r'Let \(u=x^2+2x+5\), \(du=(2x+2)\,dx=2(x+1)\,dx\).'
          r'\[\dfrac{1}{2}\int u^{-2}\,du=-\dfrac{1}{2(x^2+2x+5)}+C.\]'
          r'\[\boxed{-\dfrac{1}{2(x^2+2x+5)}+C}\]'),
         (r'\(\displaystyle\int e^{x}\cos(e^{x})\,dx\)',
          r'\[\sin(e^{x})+C.\]'
          r'\[\boxed{\sin(e^{x})+C}\]'),
         (r'\(\displaystyle\int\dfrac{3x^2}{\sqrt{x^3+1}}\,dx\)',
          r'\[2\sqrt{x^3+1}+C.\]'
          r'\[\boxed{2\sqrt{x^3+1}+C}\]'),
         (r'\(\displaystyle\int\tan(3x)\sec(3x)\,dx\)',
          r'\[\dfrac{1}{3}\sec(3x)+C.\]'
          r'\[\boxed{\dfrac{1}{3}\sec(3x)+C}\]'),
         (r'\(\displaystyle\int\dfrac{\cos(\ln x)}{x}\,dx\)',
          r'\[\sin(\ln x)+C.\]'
          r'\[\boxed{\sin(\ln x)+C}\]'),
         (r'\(\displaystyle\int\dfrac{2e^{2x}}{(e^{2x}+1)^3}\,dx\)',
          r'Let \(u=e^{2x}+1\).'
          r'\[-\dfrac{1}{(e^{2x}+1)^2}+C.\]'
          r'\[\boxed{-\dfrac{1}{(e^{2x}+1)^2}+C}\]'),
         (r'\(\displaystyle\int x\sin(x^2+1)\,dx\)',
          r'\[-\dfrac{1}{2}\cos(x^2+1)+C.\]'
          r'\[\boxed{-\dfrac{1}{2}\cos(x^2+1)+C}\]'),
         (r'\(\displaystyle\int\dfrac{\ln(x^2+1)\cdot 2x}{x^2+1}\,dx\)',
          r'Let \(u=\ln(x^2+1)\).'
          r'\[\dfrac{(\ln(x^2+1))^2}{2}+C.\]'
          r'\[\boxed{\dfrac{(\ln(x^2+1))^2}{2}+C}\]'),
     ]),
_set('w6a-set5', '6A Set 5', 'WEEK 6A · SET 5 OF 5', 'Student Notes Week 6A (filled-in)',
     'Exam-style mixed substitution',
     r'From Week 6A: exam-style practice mixing indefinite and definite substitutions across topics.',
     [
         r'Read each integrand for structure: power of an inside, log form, or exponential composite.',
         r'For definite integrals, prefer changed limits to reduce algebra.',
         r'Combine algebraic rewrite with substitution when needed.',
     ],
     r'\(\displaystyle\int_0^{\pi/4}\dfrac{\sec^2 x}{1+\tan x}\,dx=\ln 2\).',
     [r'Scan for \(u\) and \(du\).', 'Rewrite algebraically first if needed.', 'Change limits on definite.', 'Exact answers preferred.', 'Differentiate to check indefinite.'],
     [r'Mixed: exp, log, trig, algebraic', r'Changed limits for definite'],
     [
         (r'\(\displaystyle\int_0^{\pi/4}\dfrac{\sec^2 x}{1+\tan x}\,dx\)',
          r'\(u=1+\tan x\): \(1\to 2\).'
          r'\[\int_1^2\dfrac{du}{u}=\ln 2.\]'
          r'\[\boxed{\ln 2}\]'),
         (r'\(\displaystyle\int\dfrac{x^3}{\sqrt{x^4+1}}\,dx\)',
          r'Let \(u=x^4+1\), \(du=4x^3\,dx\).'
          r'\[\dfrac{1}{2}\sqrt{x^4+1}+C.\]'
          r'\[\boxed{\dfrac{1}{2}\sqrt{x^4+1}+C}\]'),
         (r'\(\displaystyle\int_0^1\dfrac{x}{(1+x^2)^2}\,dx\)',
          r'\(u=1+x^2\): \(1\to 2\).'
          r'\[\dfrac{1}{2}\int_1^2 u^{-2}\,du=\dfrac{1}{4}.\]'
          r'\[\boxed{\dfrac{1}{4}}\]'),
         (r'\(\displaystyle\int e^{\tan x}\sec^2 x\,dx\)',
          r'\[e^{\tan x}+C.\]'
          r'\[\boxed{e^{\tan x}+C}\]'),
         (r'\(\displaystyle\int_1^e\dfrac{1+\ln x}{x}\,dx\)',
          r'\[\bigl[\ln x+\tfrac{(\ln x)^2}{2}\bigr]_1^e=1+\tfrac12=\dfrac{3}{2}.\]'
          r'\[\boxed{\dfrac{3}{2}}\]'),
         (r'\(\displaystyle\int\dfrac{\sin(2x)}{1+\cos^2 x}\,dx\)',
          r'Note \(\sin(2x)=2\sin x\cos x\). Let \(u=\cos x\), or \(u=1+\cos^2 x\), \(du=-2\cos x\sin x\,dx=-\sin(2x)\,dx\).'
          r'\[-\ln(1+\cos^2 x)+C.\]'
          r'\[\boxed{-\ln(1+\cos^2 x)+C}\]'),
         (r'\(\displaystyle\int_0^{\ln 2} e^{x}\sqrt{e^{x}+1}\,dx\)',
          r'\(u=e^{x}+1\): \(2\to 3\).'
          r'\[\int_2^3\sqrt{u}\,du=\dfrac{2}{3}\bigl[u^{3/2}\bigr]_2^3=\dfrac{2}{3}(3\sqrt{3}-2\sqrt{2}).\]'
          r'\[\boxed{\dfrac{2}{3}(3\sqrt{3}-2\sqrt{2})}\]'),
         (r'\(\displaystyle\int\dfrac{1}{x(1+\sqrt{x})}\,dx\)',
          r'Let \(u=\sqrt{x}\), so \(x=u^2\), \(dx=2u\,du\).'
          r'\[\int\dfrac{2u\,du}{u^2(1+u)}=2\int\dfrac{du}{u(1+u)}=2\int\bigl(\tfrac{1}{u}-\tfrac{1}{1+u}\bigr)\,du=2\ln\left|\dfrac{\sqrt{x}}{1+\sqrt{x}}\right|+C.\]'
          r'\[\boxed{2\ln\left|\dfrac{\sqrt{x}}{1+\sqrt{x}}\right|+C}\]'),
         (r'\(\displaystyle\int_0^{\pi/2}\sin^3 x\cos x\,dx\)',
          r'\(u=\sin x\): \(0\to 1\).'
          r'\[\int_0^1 u^3\,du=\dfrac{1}{4}.\]'
          r'\[\boxed{\dfrac{1}{4}}\]'),
         (r'\(\displaystyle\int\dfrac{3x^2+1}{x^3+x}\,dx\)',
          r'\[\ln|x^3+x|+C.\]'
          r'\[\boxed{\ln|x^3+x|+C}\]'),
         (r'\(\displaystyle\int_0^1\dfrac{2x+1}{x^2+x+1}\,dx\)',
          r'Derivative of denominator is \(2x+1\).'
          r'\[\bigl[\ln(x^2+x+1)\bigr]_0^1=\ln 3.\]'
          r'\[\boxed{\ln 3}\]'),
         (r'\(\displaystyle\int\sin x\sin(\cos x)\,dx\)',
          r'Let \(u=\cos x\), \(du=-\sin x\,dx\).'
          r'\[\int\sin(\cos x)\sin x\,dx=-\int\sin u\,du=\cos u+C=\cos(\cos x)+C.\]'
          r'\[\boxed{\cos(\cos x)+C}\]'),
         (r'\(\displaystyle\int_0^{\sqrt{3}} \dfrac{x}{1+x^2}\,dx\)',
          r'\[\dfrac{1}{2}\bigl[\ln(1+x^2)\bigr]_0^{\sqrt{3}}=\dfrac{1}{2}\ln 4=\ln 2.\]'
          r'\[\boxed{\ln 2}\]'),
         (r'\(\displaystyle\int\dfrac{e^{2x}+e^{-2x}}{e^{2x}-e^{-2x}}\,dx\)',
          r'Let \(u=e^{2x}-e^{-2x}\), \(du=2(e^{2x}+e^{-2x})\,dx\).'
          r'\[\dfrac{1}{2}\ln|e^{2x}-e^{-2x}|+C.\]'
          r'\[\boxed{\dfrac{1}{2}\ln|e^{2x}-e^{-2x}|+C}\]'),
         (r'\(\displaystyle\int_1^2 x(x^2-1)^3\,dx\)',
          r'\(u=x^2-1\): \(0\to 3\).'
          r'\[\dfrac{1}{2}\int_0^3 u^3\,du=\dfrac{1}{8}\cdot 81=\dfrac{81}{8}.\]'
          r'\[\boxed{\dfrac{81}{8}}\]'),
     ]),
    ]
