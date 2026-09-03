#!/usr/bin/env python3
"""Build two optional Extension 2 proof weeks for the MATH142 study hub."""

from html import escape
from pathlib import Path


OUT = Path(__file__).resolve().parent / "siddharth" / "math142"

CSS = r"""
@import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap');
:root{--navy:#1B2431;--red:#FF3621;--paper:#fff;--grid:#e3e8ef;--line:#c8d2de;--text:#1B2431;--muted:#5b6779;--blue:#eef3fb;--green:#2f8f5b;--amber:#b45309}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:'Barlow',sans-serif;color:var(--text);background:linear-gradient(var(--grid) 1px,transparent 1px) 0 0/28px 28px,linear-gradient(90deg,var(--grid) 1px,transparent 1px) 0 0/28px 28px,var(--paper);padding:0 0 80px}
header{background:var(--navy);color:#fff;padding:36px 24px 30px;border-bottom:6px solid var(--red)}
header .inner{max-width:820px;margin:auto}.eyebrow,.box-label{font-family:'Roboto Mono',monospace;font-size:11px;letter-spacing:.11em;text-transform:uppercase}
.eyebrow{color:#9fb0c9;margin-bottom:7px}header h1{margin:0;font-size:clamp(27px,4vw,36px)}header p{margin:10px 0 0;color:#c3ccdb;font-size:15.5px;line-height:1.6;max-width:740px}
.progress-wrap{max-width:820px;margin:20px auto 0}.progress-bar{height:6px;border-radius:3px;background:rgba(255,255,255,.16);overflow:hidden}.progress-fill{height:100%;width:0;background:var(--red);transition:width .25s}.progress-label{font:11px 'Roboto Mono',monospace;color:#9fb0c9;margin-top:6px}
.chiprow{max-width:820px;margin:18px auto 0;padding:0 24px;display:flex;flex-wrap:wrap;gap:8px}.chip{padding:7px 11px;border:1px solid var(--line);border-radius:6px;background:#fff;color:var(--navy);text-decoration:none;font-size:13px;font-weight:600}.chip.on{background:var(--navy);border-color:var(--navy);color:#fff}
nav.toc{max-width:820px;margin:26px auto 0;padding:16px 22px;background:#fff;border:1px solid var(--line);border-radius:6px}.toc-title{font:11px 'Roboto Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:8px}nav.toc ol{margin:0;padding-left:20px;columns:2;font-size:14px;line-height:1.9}nav.toc a{color:var(--navy);text-decoration:none;font-weight:500}
main{max-width:820px;margin:30px auto 0;padding:0 24px}section{margin-bottom:46px;scroll-margin-top:18px}.section-title{font-size:22px;font-weight:700;margin:0 0 8px;padding-bottom:8px;border-bottom:2px solid var(--navy);display:flex;align-items:baseline;gap:10px}.tag{font:11px 'Roboto Mono',monospace;letter-spacing:.1em;text-transform:uppercase;color:var(--red);background:rgba(255,54,33,.08);border-radius:4px;padding:3px 9px}
.prose{font-size:16px;line-height:1.68;margin:16px 0}.prose p{margin:12px 0}.prose ul{padding-left:22px}.prose li{margin:8px 0}.key-box,.why-box,.source-box,.warning{margin:20px 0;padding:16px 18px;border:1px solid var(--line);border-radius:6px}.key-box{background:#fff7f5;border-left:4px solid var(--red)}.why-box{background:var(--blue);border-left:4px solid var(--navy)}.source-box{background:#f2faf6;border-left:4px solid var(--green)}.warning{background:#fffbeb;border-left:4px solid var(--amber)}.key-box .box-label{color:var(--red)}.why-box .box-label{color:var(--navy)}.source-box .box-label{color:var(--green)}.warning .box-label{color:var(--amber)}.key-box p,.why-box p,.source-box p,.warning p{margin:8px 0;line-height:1.62}.source-box a{color:#185FA5}
table{width:100%;border-collapse:collapse;margin:16px 0;font-size:14px;display:block;overflow-x:auto}th{background:var(--navy);color:#fff;padding:9px 10px;text-align:left}td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.5}tr:nth-child(even) td{background:#f7f9fc}
.example{background:#f7f9fc;border:1px solid var(--line);border-left:4px solid var(--navy);border-radius:6px;padding:15px 18px;margin:18px 0}.example h3{font-size:16px;margin:0 0 8px}.example p{margin:8px 0;line-height:1.62}
.practice-card{background:#fff;border:1px solid var(--line);border-left:4px solid #33415a;border-radius:6px;margin:16px 0;overflow:hidden}.p-head{display:flex;gap:12px;padding:14px 20px 4px}.p-num{font:12px 'Roboto Mono',monospace;background:#eef1f6;border-radius:4px;padding:2px 8px;flex-shrink:0}.p-body{padding:4px 20px 14px;font-size:15.5px;line-height:1.6}.toggle-row{padding:0 20px 14px}.toggle-btn{font:600 13px 'Barlow',sans-serif;color:var(--navy);background:#fff;border:1.5px solid var(--navy);border-radius:5px;padding:8px 15px;cursor:pointer}.toggle-btn.shown{background:var(--red);border-color:var(--red);color:#fff}.solution{display:none;border-top:1px dashed var(--line)}.solution.open{display:block}.solution-inner{padding:14px 20px 18px;background:#fbfcfe;font-size:15px;line-height:1.65}.solution-inner .label{font:11px 'Roboto Mono',monospace;text-transform:uppercase;letter-spacing:.1em;color:var(--red)}
.video-box{margin:18px 0 22px;padding:15px 17px 17px;border:1px solid var(--line);border-left:4px solid var(--red);border-radius:8px;background:#fff7f5}.video-row{display:flex;flex-wrap:wrap;gap:16px}.video-item{flex:1 1 300px;min-width:280px}.video-item h4{margin:0 0 3px;font-size:15px}.video-meta{font:10.5px 'Roboto Mono',monospace;letter-spacing:.06em;text-transform:uppercase;color:#7a869a;margin:0 0 6px}.video-item .blurb{font-size:13.5px;line-height:1.5;color:var(--muted)}.video-frame{position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:6px;background:#000}.video-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.watch{display:inline-block;margin-top:8px;padding:6px 11px;border-radius:5px;background:var(--red);color:#fff;text-decoration:none;font-weight:600;font-size:12.5px}
footer{max-width:820px;margin:15px auto 0;padding:20px 24px 0;border-top:1px solid var(--line);text-align:center;color:var(--muted);font:12px 'Roboto Mono',monospace}footer a{color:#185FA5;text-decoration:none}mjx-container[display="true"]{max-width:100%;overflow-x:auto;overflow-y:hidden;padding-bottom:3px}
@media(max-width:640px){nav.toc ol{columns:1}.video-item{min-width:100%}}
"""

JS = r"""
function toggleSolution(button){
  const solution=button.closest('.practice-card').querySelector('.solution');
  const open=solution.classList.toggle('open');
  button.classList.toggle('shown',open);
  button.textContent=open?'Hide solution':'Show solution';
  updateProgress();
}
function updateProgress(){
  const all=[...document.querySelectorAll('.practice-card')];
  const open=all.filter(c=>c.querySelector('.solution.open')).length;
  document.getElementById('progressFill').style.width=(all.length?100*open/all.length:0)+'%';
  document.getElementById('progressLabel').textContent=open+' / '+all.length+' practice solutions revealed';
}
"""


def video(title: str, teacher: str, video_id: str, blurb: str) -> str:
    return f"""<div class="video-item"><h4>{escape(title)}</h4>
<p class="video-meta">{escape(teacher)}</p><p class="blurb">{escape(blurb)}</p>
<div class="video-frame"><iframe src="https://www.youtube.com/embed/{video_id}" title="{escape(title)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen loading="lazy"></iframe></div>
<a class="watch" href="https://www.youtube.com/watch?v={video_id}" target="_blank" rel="noopener">Open on YouTube ↗</a></div>"""


def practice(number: int, question: str, solution: str) -> str:
    return f"""<div class="practice-card"><div class="p-head"><span class="p-num">P{number:02}</span></div>
<div class="p-body">{question}</div><div class="toggle-row"><button class="toggle-btn" onclick="toggleSolution(this)">Show solution</button></div>
<div class="solution"><div class="solution-inner"><span class="label">Worked solution</span>{solution}</div></div></div>"""


def page(*, filename: str, week: str, title: str, subtitle: str, toc: list[tuple[str, str]],
         body: str, previous: str, next_page: str, practice_count: int) -> None:
    toc_html = "".join(f'<li><a href="#{anchor}">{escape(label)}</a></li>' for anchor, label in toc)
    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MATH142 Extension Proofs — {escape(title)}</title>
<script>window.MathJax={{tex:{{inlineMath:[['$','$'],['\\\\(','\\\\)']],displayMath:[['$$','$$'],['\\\\[','\\\\]']]}}}};</script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<style>{CSS}</style></head><body>
<header><div class="inner"><div class="eyebrow">MATH142 · Optional Extension 2 Proofs · {escape(week)}</div>
<h1>{escape(title)}</h1><p>{escape(subtitle)}</p>
<div class="progress-wrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
<div class="progress-label" id="progressLabel">0 / {practice_count} practice solutions revealed</div></div></div></header>
<div class="chiprow"><a class="chip" href="{previous}">← Previous</a><a class="chip on" href="{filename}">{escape(week)}</a>
<a class="chip" href="{next_page}">Next →</a><a class="chip" href="index.html">MATH142 home</a></div>
<nav class="toc"><div class="toc-title">Contents</div><ol>{toc_html}</ol></nav>
<main>{body}</main>
<footer>Optional Extension 2 enrichment · based on Steve Howard, <em>HSC Mathematics Extension 2</em> (December 2021), Chapters 1 and 3 · <a href="index.html">MATH142 home</a></footer>
<script>{JS}</script></body></html>"""
    (OUT / filename).write_text(html)


week_a_practice = [
    (r"""Negate: “For every real number $x$, $x^2+1>0$.”""",
     r"""<p>A negation must reverse both the quantifier and the property. “For every” becomes “there exists at least one”, while the negation of $x^2+1>0$ is $x^2+1\le0$ (not merely $\lt0$).</p>
<p>Therefore the exact negation is</p>
<p>$$\boxed{\text{There exists }x\in\mathbb R\text{ such that }x^2+1\le0.}$$</p>
<p>The negated statement happens to be false, which is consistent with the original statement being true.</p>"""),
    (r"""Write the converse and contrapositive of: “If $n$ is divisible by $6$, then $n$ is even.”""",
     r"""<p>Write the implication as $P\Rightarrow Q$, where $P$ is “$6\mid n$” and $Q$ is “$n$ is even”.</p>
<p><strong>Converse, $Q\Rightarrow P$:</strong> If $n$ is even, then $n$ is divisible by $6$. This is false; $n=2$ satisfies the hypothesis but not the conclusion.</p>
<p><strong>Contrapositive, $\neg Q\Rightarrow\neg P$:</strong> If $n$ is odd, then $n$ is not divisible by $6$. This is logically equivalent to the original. Indeed, every multiple of $6$ has the form $6k=2(3k)$ and is even.</p>"""),
    (r"""Prove that if $4\mid(a^2+b^2)$ for integers $a,b$, then both $a$ and $b$ are even.""",
     r"""<p>Every integer is even or odd. An even square is congruent to $0\pmod4$, while an odd square is congruent to $1\pmod4$.</p>
<p>If either $a$ or $b$ were odd, then $a^2+b^2$ would be congruent to $1$ or $2\pmod4$, depending on whether one or both were odd. Neither remainder is divisible by $4$.</p>
<p>Therefore both squares must be congruent to $0\pmod4$, which forces both $a$ and $b$ to be even.</p>"""),
    (r"""Let $\gcd(a,b)=1$. Prove that if $a\mid n$ and $b\mid n$, then $ab\mid n$.""",
     r"""<p>Since $a\mid n$, write $n=ar$ for some integer $r$. We also know $b\mid ar$.</p>
<p>Because $\gcd(a,b)=1$, Bézout’s identity gives integers $u,v$ satisfying $ua+vb=1$. Multiply by $r$:</p>
<p>$$r=uar+vbr.$$</p>
<p>The term $uar$ is divisible by $b$ because $b\mid ar$, and $vbr$ is visibly divisible by $b$. Hence their sum $r$ is divisible by $b$; write $r=bs$.</p>
<p>Then $n=ar=a(bs)=abs$, so $ab\mid n$. The coprimality condition is essential: $4\mid12$ and $6\mid12$, but $24\nmid12$.</p>"""),
    (r"""Prove by contraposition: if $n^2$ is divisible by $3$, then $n$ is divisible by $3$.""",
     r"""<p>Prove the contrapositive. If $3\nmid n$, then $n=3q+1$ or $n=3q+2$. Squaring gives</p>
<p>$$(3q+1)^2=3(3q^2+2q)+1,\qquad(3q+2)^2=3(3q^2+4q+1)+1.$$</p>
<p>In either case $3\nmid n^2$. Therefore, by contraposition, $3\mid n^2\Rightarrow3\mid n$.</p>"""),
    (r"""Prove by contradiction that there is no greatest integer.""",
     r"""<p>The target is a non-existence statement, so contradiction is natural. Assume its negation: suppose a greatest integer exists; call it $N$.</p>
<p>Integers are closed under addition, so $N+1$ is also an integer. But $N+1>N$, contradicting the defining property that no integer exceeds the greatest integer $N$.</p>
<p>Therefore the assumption is impossible, and there is no greatest integer.</p>"""),
    (r"""Prove by contradiction that $\sqrt5$ is irrational.""",
     r"""<p>Assume the opposite: $\sqrt5$ is rational. Then $\sqrt5=p/q$ for integers $p,q$ with $q\ne0$, chosen so that $\gcd(p,q)=1$.</p>
<p>Squaring and clearing the denominator gives $p^2=5q^2$. Hence $5\mid p^2$. Since $5$ is prime, $5\mid p$; write $p=5r$.</p>
<p>Substitute back:</p><p>$$25r^2=5q^2\Rightarrow q^2=5r^2.$$</p>
<p>Thus $5\mid q^2$, and again primality gives $5\mid q$. So $p$ and $q$ share the factor $5$, contradicting $\gcd(p,q)=1$. The rationality assumption is false; therefore $\sqrt5$ is irrational.</p>"""),
    (r"""Prove that an integer $n$ is odd if and only if $n^2$ is odd.""",
     r"""<p>An “if and only if” statement requires two separate implications.</p>
<p><strong>Forward:</strong> suppose $n$ is odd, so $n=2k+1$ for some integer $k$. Then</p>
<p>$$n^2=(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1,$$</p>
<p>which is odd because $2k^2+2k$ is an integer.</p>
<p><strong>Reverse:</strong> prove the contrapositive. If $n$ is even, write $n=2k$. Then $n^2=4k^2=2(2k^2)$ is even. Therefore, if $n^2$ is odd, $n$ cannot be even and must be odd.</p>"""),
    (r"""Disprove: “$n^2+n+41$ is prime for every positive integer $n$.”""",
     r"""<p>The statement is universal, so one positive integer producing a composite value is sufficient. The constant $41$ suggests testing a value that makes every term divisible by $41$.</p>
<p>At $n=41$:</p><p>$$n^2+n+41=41^2+41+41=41(41+2)=41\cdot43.$$</p>
<p>Both factors exceed $1$, so the value is composite. Since $41$ lies in the claimed domain, this single counterexample disproves the statement.</p>"""),
    (r"""A student writes: “$2,3,5,7$ are prime, so every integer from $2$ onward is prime.” Identify the logical error.""",
     r"""<p>The conclusion is universal—it claims something about infinitely many integers—but the evidence checks only four cases. Finite examples can motivate a conjecture; they cannot establish a statement beginning with “for every”.</p>
<p>In fact the reasoning overlooks $4$, which lies in the claimed domain and is composite. A single counterexample is enough to disprove a universal statement, so $n=4$ decisively refutes the claim.</p>"""),
    (r"""Negate precisely: “For every $\varepsilon>0$ there exists a positive integer $N$ such that, for every $n\ge N$, $|a_n-L|<\varepsilon$.”""",
     r"""<p>Reverse each quantifier in order and negate the final inequality:</p>
<p>$$\boxed{\text{There exists }\varepsilon>0\text{ such that for every }N\in\mathbb N,\text{ there exists }n\ge N\text{ with }|a_n-L|\ge\varepsilon.}$$</p>
<p>This says that some fixed tolerance is violated infinitely far along the sequence.</p>"""),
    (r"""Show that $P\Rightarrow Q$ is logically equivalent to $\neg(P\land\neg Q)$, without using a truth table.""",
     r"""<p>If $P\Rightarrow Q$ holds, then $P$ and $\neg Q$ cannot both hold, so $\neg(P\land\neg Q)$ follows.</p>
<p>Conversely, assume $\neg(P\land\neg Q)$. If $P$ is true, $\neg Q$ cannot be true; hence $Q$ is true. Therefore $P\Rightarrow Q$.</p>"""),
    (r"""Prove that $n^3-n$ is divisible by $6$ for every integer $n$.""",
     r"""<p>Factor the expression:</p><p>$$n^3-n=n(n-1)(n+1).$$</p>
<p>The factors $n-1,n,n+1$ are three consecutive integers. Among any three consecutive integers, exactly one is divisible by $3$. Also, among any two consecutive integers at least one is even, so this product is divisible by $2$.</p>
<p>Because $\gcd(2,3)=1$, divisibility by both $2$ and $3$ implies divisibility by $6$. Therefore $6\mid(n^3-n)$ for every integer $n$.</p>"""),
    (r"""Prove that $a^2+b^2$ is odd if and only if the integers $a$ and $b$ have opposite parity.""",
     r"""<p>A square has the same parity as its base: even squares are even and odd squares are odd.</p>
<p><strong>Forward:</strong> if $a^2+b^2$ is odd, the two squares cannot have the same parity, so $a,b$ have opposite parity.</p>
<p><strong>Reverse:</strong> if $a,b$ have opposite parity, one square is even and the other odd, so their sum is odd.</p>"""),
    (r"""Let $r$ be rational and $x$ irrational. Prove that $r+x$ is irrational. Explain why the corresponding claim for $rx$ needs an extra condition.""",
     r"""<p>If $r+x$ were rational, then $x=(r+x)-r$ would be a difference of rational numbers and hence rational, a contradiction.</p>
<p>For products, $r\ne0$ is required. If $r\ne0$ and $rx$ were rational, then $x=(rx)/r$ would be rational. When $r=0$, however, $rx=0$ is rational for every irrational $x$.</p>"""),
    (r"""Prove: if $x+y$ is irrational, then at least one of $x,y$ is irrational. Is the converse true?""",
     r"""<p>Use contraposition. If both $x$ and $y$ are rational, closure of the rationals under addition makes $x+y$ rational. Therefore, if $x+y$ is irrational, at least one summand is irrational.</p>
<p>The converse is false: $x=\sqrt2$ and $y=-\sqrt2$ are irrational but $x+y=0$ is rational.</p>"""),
    (r"""Prove that $\sqrt2+\sqrt3$ is irrational.""",
     r"""<p>Assume $\sqrt2+\sqrt3=r\in\mathbb Q$. Then $\sqrt3=r-\sqrt2$. Squaring gives</p>
<p>$$3=r^2+2-2r\sqrt2,\qquad 2r\sqrt2=r^2-1.$$</p>
<p>Here $r\ne0$, so $\sqrt2=(r^2-1)/(2r)$ would be rational, contradicting the irrationality of $\sqrt2$. Hence the sum is irrational.</p>"""),
    (r"""Euclid challenge: prove that there are infinitely many prime numbers.""",
     r"""<p>Assume there are only finitely many primes $p_1,\ldots,p_k$. Form</p>
<p>$$N=p_1p_2\cdots p_k+1.$$</p>
<p>Every integer greater than $1$ has a prime divisor, say $q\mid N$. But division of $N$ by any listed $p_i$ leaves remainder $1$, so $q$ is not on the complete list. This contradiction proves there are infinitely many primes.</p>"""),
    (r"""Show that there exist irrational numbers $a,b$ for which $a^b$ is rational, without needing to decide whether $\sqrt2^{\sqrt2}$ is rational.""",
     r"""<p>Let $c=\sqrt2^{\sqrt2}$. If $c$ is rational, choose $a=b=\sqrt2$.</p>
<p>If $c$ is irrational, choose $a=c$ and $b=\sqrt2$. Then</p>
<p>$$a^b=\left(\sqrt2^{\sqrt2}\right)^{\sqrt2}=\sqrt2^{\,2}=2,$$</p>
<p>which is rational. One of the two cases must hold, so the required irrational pair exists.</p>"""),
    (r"""Disprove: “If $6\mid ab$, then $6\mid a$ or $6\mid b$.” Then state a nearby true theorem.""",
     r"""<p>Take $a=2$, $b=3$. Then $6\mid ab$, but $6$ divides neither factor.</p>
<p>A nearby true theorem is Euclid’s lemma: if a <em>prime</em> $p$ divides $ab$, then $p\mid a$ or $p\mid b$. The failed claim treats the composite number $6$ as though it were prime.</p>"""),
    (r"""Prove that $4\mid n^2$ if and only if $n$ is even.""",
     r"""<p><strong>Reverse:</strong> if $n=2k$, then $n^2=4k^2$, so $4\mid n^2$.</p>
<p><strong>Forward:</strong> prove the contrapositive. If $n=2k+1$ is odd, then $n^2=4(k^2+k)+1$, which is not divisible by $4$. Thus $4\mid n^2$ implies $n$ is even.</p>"""),
    (r"""Prove that the equation $x^2-y^2=2026$ has no integer solutions.""",
     r"""<p>Every square is congruent to $0$ or $1\pmod4$. Therefore a difference of two squares is congruent to $0,1$, or $-1\equiv3\pmod4$, never $2\pmod4$.</p>
<p>But $2026\equiv2\pmod4$. Hence no integer pair $(x,y)$ can satisfy the equation.</p>"""),
    (r"""Let $p$ be prime. Prove that if $p\mid a^2$, then $p\mid a$.""",
     r"""<p>By the fundamental theorem of arithmetic, write the prime factorisation of $a$. Squaring doubles every prime exponent. If $p\mid a^2$, the exponent of $p$ in $a^2$ is positive, so the exponent of $p$ in $a$ was already positive. Hence $p\mid a$.</p>
<p>This is the prime-divisor fact used in standard irrational-square-root proofs.</p>"""),
    (r"""Find the flaw in the classic argument below:
$$a=b\Rightarrow a^2=ab\Rightarrow a^2-b^2=ab-b^2\Rightarrow(a-b)(a+b)=b(a-b)\Rightarrow a+b=b\Rightarrow2=1.$$""",
     r"""<p>The cancellation of $a-b$ is illegal. The opening assumption $a=b$ makes $a-b=0$, so that step divides both sides by zero. Every earlier algebraic line is valid; the contradiction is manufactured exactly at the cancellation.</p>"""),
    (r"""Prove for $c>0$ that $|x|<c$ if and only if $-c<x<c$.""",
     r"""<p><strong>Forward:</strong> $|x|<c$ means the distance from $x$ to $0$ is less than $c$, so $x$ lies strictly between $-c$ and $c$.</p>
<p><strong>Algebraically:</strong> $-|x|\le x\le|x|$, hence $-c<x<c$.</p>
<p><strong>Reverse:</strong> if $-c<x<c$, then for $x\ge0$, $|x|=x<c$; for $x<0$, $|x|=-x<c$ follows from $x>-c$.</p>"""),
    (r"""Prove that the equation $x^3+x=1$ has exactly one real solution.""",
     r"""<p>Let $f(x)=x^3+x-1$. Since $f(0)=-1$ and $f(1)=1$, continuity and the intermediate value theorem give at least one root in $(0,1)$.</p>
<p>For $y>x$:</p><p>$$f(y)-f(x)=(y-x)(y^2+xy+x^2+1)>0,$$</p>
<p>because $y-x>0$ and $y^2+xy+x^2=\left(y+\frac x2\right)^2+\frac34x^2\ge0$. Thus $f$ is strictly increasing and cannot have two roots. The root is therefore unique.</p>"""),
    (r"""Generalise the $\sqrt5$ argument: prove that $\sqrt p$ is irrational for every prime $p$.""",
     r"""<p>Assume $\sqrt p=a/b$ in lowest terms. Then $a^2=pb^2$, so $p\mid a^2$ and therefore $p\mid a$. Write $a=pc$. Substitution gives $p^2c^2=pb^2$, hence $b^2=pc^2$, so $p\mid b$. This contradicts $\gcd(a,b)=1$. Therefore $\sqrt p$ is irrational.</p>"""),
    (r"""Construct irrational numbers $x,y$ such that both $x+y$ and $xy$ are rational.""",
     r"""<p>Choose conjugate surds so their irrational parts cancel under addition and pair under multiplication. Let</p>
<p>$$x=\sqrt2,\qquad y=-\sqrt2.$$</p>
<p>Both numbers are irrational: changing the sign of an irrational number cannot make it rational. Yet</p>
<p>$$x+y=0,\qquad xy=-2,$$</p>
<p>and both results are rational. More generally, $\sqrt m$ and $-\sqrt m$ work for any positive nonsquare integer $m$.</p>"""),
    (r"""Prove that $\log_2 3$ is irrational.""",
     r"""<p>Assume $\log_2 3=a/b\in\mathbb Q$ in lowest terms, with $b>0$. Then</p>
<p>$$2^{a/b}=3\quad\Rightarrow\quad2^a=3^b.$$</p>
<p>The left side has only the prime factor $2$, while the right side has only the prime factor $3$. Unique prime factorisation makes equality impossible. Hence $\log_2 3$ is irrational.</p>"""),
    (r"""A student tries to prove “if $n^2$ is odd, then $n$ is odd” by writing $n^2=2k+1$ and $n=\sqrt{2k+1}$, then declaring this odd. Diagnose the failure and give a valid proof.""",
     r"""<p>The form $\sqrt{2k+1}$ is not the definition of an odd integer; it does not exhibit $n$ as $2m+1$ for an integer $m$.</p>
<p>Use contraposition. If $n$ is even, $n=2m$, then $n^2=4m^2=2(2m^2)$ is even. Therefore, if $n^2$ is odd, $n$ must be odd.</p>"""),
]

week_a_body = r"""
<section id="source"><div class="section-title"><span class="tag">Start</span> Textbook map and goal</div>
<div class="source-box"><span class="box-label">Primary source</span><p>Steve Howard, <em>HSC Mathematics Extension 2</em> (December 2021), Chapter 1: pp. 7–43 for language, direct proof, contrapositive, contradiction, equivalence and disproof; pp. 44–76 continue into inequalities and AM–GM.</p>
<p><a href="../dpen22/HSC-Mathematics-Extension-2-Textbook-v9-2021-12-03.pdf#page=8" target="_blank">Open the local textbook at Chapter 1 ↗</a></p></div>
<div class="prose"><p>The goal is not to memorise ceremonial words. It is to make every claim traceable: what is assumed, what must be shown, why each step follows, and where the conclusion is reached.</p></div></section>

<section id="language"><div class="section-title"><span class="tag">01</span> Statements, implication and quantifiers</div>
<div class="prose"><p>A <strong>statement</strong> is a sentence that is either true or false. A conditional $P\Rightarrow Q$ says that whenever $P$ is true, $Q$ must follow. It does not automatically give $Q\Rightarrow P$.</p></div>
<table><thead><tr><th>Original</th><th>Related statement</th><th>Equivalent?</th></tr></thead><tbody>
<tr><td>$P\Rightarrow Q$</td><td>Converse: $Q\Rightarrow P$</td><td>No</td></tr>
<tr><td>$P\Rightarrow Q$</td><td>Inverse: $\neg P\Rightarrow\neg Q$</td><td>No</td></tr>
<tr><td>$P\Rightarrow Q$</td><td>Contrapositive: $\neg Q\Rightarrow\neg P$</td><td>Yes</td></tr></tbody></table>
<div class="key-box"><span class="box-label">Negating quantifiers</span><p>The negation of “for every $x$, $P(x)$” is “there exists an $x$ for which $P(x)$ is false”. The negation of “there exists $x$ such that $P(x)$” is “for every $x$, $P(x)$ is false”.</p></div></section>

<section id="direct"><div class="section-title"><span class="tag">02</span> Direct proof and definitions</div>
<div class="prose"><p>A direct proof starts with the hypothesis and uses definitions and known results until the conclusion appears. For integers, definitions are your algebraic handles:</p>
<ul><li>even: $n=2k$;</li><li>odd: $n=2k+1$;</li><li>$a\mid b$: $b=ak$ for some integer $k$;</li><li>rational: $x=p/q$ for integers $p,q$, $q\ne0$.</li></ul></div>
<div class="example"><h3>Example — the square of an odd integer is odd</h3><p>Let $n=2k+1$. Then $$n^2=(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1.$$ The bracket is an integer, so $n^2$ has the form $2m+1$ and is odd.</p></div></section>

<section id="indirect"><div class="section-title"><span class="tag">03</span> Contrapositive and contradiction</div>
<div class="video-box"><span class="box-label">Watch first</span><div class="video-row">
__VIDEO_A1__
__VIDEO_A2__
__VIDEO_A3__
</div></div>
<div class="prose"><p><strong>Contrapositive:</strong> to prove $P\Rightarrow Q$, prove the equivalent statement $\neg Q\Rightarrow\neg P$. This is ideal when the negation of $Q$ has a useful algebraic form.</p>
<p><strong>Contradiction:</strong> assume the claim is false, then derive an impossibility: a number is both odd and even, a reduced fraction has a common factor, or a quantity is simultaneously $&lt;a$ and $\ge a$.</p></div>
<div class="warning"><span class="box-label">Do not confuse them</span><p>Contrapositive begins with $\neg Q$ and aims for $\neg P$. Contradiction assumes enough to negate the whole target and aims for any contradiction.</p></div></section>

<section id="equivalence"><div class="section-title"><span class="tag">04</span> Equivalence, existence and disproof</div>
<div class="prose"><p>To prove $P\Leftrightarrow Q$, prove both directions separately. To prove existence, construct one object or show why one must exist. To disprove a universal statement, give one valid counterexample and check it explicitly.</p></div>
<div class="example"><h3>Example — disprove a tempting pattern</h3><p>The claim “$n^2-n+11$ is prime for every positive integer $n$” is false. Set $n=11$: $11^2-11+11=121=11^2$.</p></div></section>

<section id="practice"><div class="section-title"><span class="tag">05</span> 30 exam-quality proof problems</div>
<div class="why-box"><span class="box-label">How to use this set</span><p>Problems 1–10 establish rigorous habits, 11–20 combine methods, and 21–30 demand counterexample design, proof repair, modular reasoning, existence or uniqueness. Attempt each proof before revealing the detailed solution. Declare variables and domains, justify every implication, and finish with the exact claim.</p></div>
__PRACTICE_A__</section>

<section id="next"><div class="section-title"><span class="tag">Next</span> Move to inequalities and induction</div>
<div class="prose"><p>Week B adds inequality machinery, AM–GM and further mathematical induction. These methods feed directly into convergence arguments in MATH142 Weeks 10–12.</p></div></section>
"""
week_a_body = (
    week_a_body
    .replace("__VIDEO_A1__", video(
        "Language and Symbols of Proof",
        "Toby McGrath · HSC Extension 2 Mathematics",
        "6qWlsXAc-EY",
        "Statements, implications, quantifiers and the formal language used throughout the NSW course.",
    ))
    .replace("__VIDEO_A2__", video(
        "Number Proofs",
        "Toby McGrath · HSC Extension 2 Mathematics",
        "SswASU4aUH0",
        "Direct algebraic proof with the integer definitions used in the worked examples below.",
    ))
    .replace("__VIDEO_A3__", video(
        "Proof by Contradiction and Counterexamples",
        "Toby McGrath · HSC Extension 2 Mathematics",
        "-oqqqtg9J0g",
        "Exact syllabus coverage of contradiction and disproving universal claims.",
    ))
    .replace("__PRACTICE_A__", "".join(
        practice(i, q, s) for i, (q, s) in enumerate(week_a_practice, 1)
    ))
)

week_b_practice = [
    (r"""Determine all real values of $\lambda$ for which
$$x^2+\lambda x+1\ge0$$
for every real $x$. Prove both necessity and sufficiency.""",
     r"""<p>Complete the square:</p>
<p>$$x^2+\lambda x+1=\left(x+\frac\lambda2\right)^2+1-\frac{\lambda^2}{4}.$$</p>
<p>The square is minimised at $x=-\lambda/2$, so the expression is non-negative for every real $x$ exactly when its minimum is non-negative:</p>
<p>$$1-\frac{\lambda^2}{4}\ge0\iff\lambda^2\le4\iff-2\le\lambda\le2.$$</p>
<p><strong>Sufficiency:</strong> if $|\lambda|\le2$, both terms in the completed-square form have non-negative total, so the inequality holds for every $x$.</p>
<p><strong>Necessity:</strong> if $|\lambda|>2$, substituting $x=-\lambda/2$ makes the value $1-\lambda^2/4<0$. Thus the complete answer is $\boxed{\lambda\in[-2,2]}$.</p>"""),
    (r"""For positive $a,b$, prove $\dfrac ab+\dfrac ba\ge2$.""",
     r"""<p>Start from the always-true inequality $(a-b)^2\ge0$. Expanding gives $a^2+b^2\ge2ab$.</p>
<p>Because $a,b>0$, their product $ab$ is positive, so division by $ab$ is legal and does not reverse the inequality:</p>
<p>$$\frac{a^2+b^2}{ab}\ge2\quad\Rightarrow\quad\frac ab+\frac ba\ge2.$$</p>
<p>Equality occurs exactly when $(a-b)^2=0$, that is, when $a=b$.</p>"""),
    (r"""Use AM–GM to find the minimum of $x+\dfrac9x$ for $x>0$.""",
     r"""<p>The domain $x>0$ makes both terms positive, so AM–GM applies:</p>
<p>$$x+\frac9x\ge2\sqrt{x\cdot\frac9x}=2\sqrt9=6.$$</p>
<p>A lower bound is a minimum only if it can be attained. Equality in AM–GM requires the two terms to be equal:</p>
<p>$$x=\frac9x\Rightarrow x^2=9.$$</p>
<p>The domain selects $x=3$. Therefore the global minimum is $\boxed6$, attained at $x=3$.</p>"""),
    (r"""Prove by induction that $1+3+\cdots+(2n-1)=n^2$ for $n\ge1$.""",
     r"""<p>Let $P(n)$ denote the proposed identity.</p>
<p><strong>Base:</strong> at $n=1$, the left side is $1$ and the right side is $1^2=1$.</p>
<p><strong>Hypothesis:</strong> assume for an arbitrary $k\ge1$ that $1+3+\cdots+(2k-1)=k^2$.</p>
<p><strong>Step:</strong> the next odd number is $2(k+1)-1=2k+1$. Therefore</p>
<p>$$1+3+\cdots+(2k-1)+(2k+1)=k^2+2k+1=(k+1)^2,$$</p>
<p>where the hypothesis was used at the equality to $k^2+2k+1$. This is precisely $P(k+1)$. Hence the identity holds for every $n\ge1$ by induction.</p>"""),
    (r"""Prove by induction that $6\mid(7^n-1)$ for every integer $n\ge1$.""",
     r"""<p>Let $P(n)$ be the claim that $7^n-1$ is divisible by $6$.</p>
<p><strong>Base:</strong> $7^1-1=6$, so $P(1)$ holds.</p>
<p><strong>Hypothesis:</strong> assume $P(k)$, meaning $7^k-1=6m$ for some integer $m$.</p>
<p><strong>Step:</strong> rewrite the next expression so the hypothesised factor appears:</p>
<p>$$7^{k+1}-1=7(7^k-1)+6=7(6m)+6=6(7m+1).$$</p>
<p>Since $7m+1$ is an integer, $6\mid(7^{k+1}-1)$. Therefore $P(n)$ holds for every $n\ge1$ by induction.</p>"""),
    (r"""Prove by induction that $2^n\ge n+1$ for all $n\ge0$.""",
     r"""<p>Let $P(n)$ denote $2^n\ge n+1$.</p>
<p><strong>Base:</strong> at $n=0$, $2^0=1=0+1$.</p>
<p><strong>Hypothesis:</strong> suppose $2^k\ge k+1$ for some $k\ge0$.</p>
<p><strong>Step:</strong> multiplying by the positive number $2$ preserves the bound:</p>
<p>$$2^{k+1}=2\cdot2^k\ge2(k+1).$$</p>
<p>Also $2(k+1)-(k+2)=k\ge0$, so $2(k+1)\ge k+2$. Chaining the inequalities gives $2^{k+1}\ge k+2$, exactly $P(k+1)$. Induction proves the result.</p>"""),
    (r"""Prove by induction that $3^n>n^2$ for every integer $n\ge3$.""",
     r"""<p><strong>Base:</strong> $3^3=27>9=3^2$.</p>
<p><strong>Hypothesis:</strong> assume $3^k>k^2$ for an arbitrary $k\ge3$.</p>
<p><strong>Step:</strong> multiply the hypothesis by $3>0$ to obtain $3^{k+1}>3k^2$. We still need to bridge this bound to the target $(k+1)^2$. Compute</p>
<p>$$3k^2-(k+1)^2=2k^2-2k-1=2k(k-1)-1>0$$</p>
<p>because $k\ge3$ makes $2k(k-1)\ge12$. Thus $3k^2>(k+1)^2$, and so</p>
<p>$$3^{k+1}>3k^2>(k+1)^2.$$</p>
<p>This proves the inductive step and hence the result for all $n\ge3$.</p>"""),
    (r"""Prove $1+\dfrac12+\cdots+\dfrac1{2^n}=2-\dfrac1{2^n}$ for $n\ge0$.""",
     r"""<p><strong>Base:</strong> at $n=0$, the sum contains only $1$, while $2-1/2^0=1$.</p>
<p><strong>Hypothesis:</strong> assume $\sum_{r=0}^{k}2^{-r}=2-2^{-k}$.</p>
<p><strong>Step:</strong> append the next term:</p>
<p>$$\begin{aligned}
\sum_{r=0}^{k+1}\frac1{2^r}
&=\left(2-\frac1{2^k}\right)+\frac1{2^{k+1}}\\
&=2-\frac2{2^{k+1}}+\frac1{2^{k+1}}\\
&=2-\frac1{2^{k+1}}.
\end{aligned}$$</p>
<p>This is the claimed formula with $k+1$ in place of $n$, so induction proves it for every $n\ge0$.</p>"""),
    (r"""What is wrong with: “Assume $2^k>k^2$. Then $2^{k+1}>2k^2>(k+1)^2$”? Repair it for $k\ge5$.""",
     r"""<p>The hypothesis justifies $2^{k+1}=2\cdot2^k>2k^2$, but it says nothing directly about $2k^2$ versus $(k+1)^2$. The omitted comparison is the gap.</p>
<p>For $k\ge5$:</p>
<p>$$2k^2-(k+1)^2=k^2-2k-1=(k-1)^2-2\ge16-2>0.$$</p>
<p>Hence $2k^2>(k+1)^2$, completing the chain. The base case must also be checked: $2^5=32>25=5^2$. With both repairs, induction proves $2^n>n^2$ for every $n\ge5$.</p>"""),
    (r"""A rectangle has positive side lengths $x,y$ and fixed area $xy=36$. Prove its perimeter is at least $24$.""",
     r"""<p>The area condition fixes a product, while perimeter depends on a sum, so AM–GM is the natural bridge:</p>
<p>$$\frac{x+y}{2}\ge\sqrt{xy}=\sqrt{36}=6.$$</p>
<p>Hence $x+y\ge12$, and the perimeter satisfies</p>
<p>$$P=2x+2y=2(x+y)\ge24.$$</p>
<p>Equality in AM–GM requires $x=y$. Combined with $xy=36$ and positivity, this gives $x=y=6$. Thus $24$ is attained by the square and is the true minimum.</p>"""),
    (r"""For real $a,b,c$, prove
$$a^2+b^2+c^2\ge ab+bc+ca,$$
and determine exactly when equality holds.""",
     r"""<p>The expression is symmetric, so compare the two sides by subtracting and seek squares:</p>
<p>$$2(a^2+b^2+c^2-ab-bc-ca)=(a-b)^2+(b-c)^2+(c-a)^2.$$</p>
<p>The right side is a sum of non-negative squares. Therefore the left side is non-negative and the required inequality follows.</p>
<p>Equality in a sum of squares occurs only when every square is zero. Thus $a=b$, $b=c$, and $c=a$; equivalently, $\boxed{a=b=c}$.</p>"""),
    (r"""Prove the two-dimensional Cauchy inequality
$$ (a^2+b^2)(c^2+d^2)\ge(ac+bd)^2 $$
for all real $a,b,c,d$. Avoid quoting Cauchy–Schwarz.""",
     r"""<p>Expand the difference between the two sides:</p>
<p>$$\begin{aligned}
(a^2+b^2)(c^2+d^2)-(ac+bd)^2
&=a^2d^2+b^2c^2-2abcd\\
&=(ad-bc)^2\ge0.
\end{aligned}$$</p>
<p>Hence the inequality holds. Equality occurs precisely when $ad=bc$, which says the pairs $(a,b)$ and $(c,d)$ are proportional (including the zero-vector cases).</p>"""),
    (r"""For positive $a,b,c$, prove Nesbitt’s inequality:
$$\frac{a}{b+c}+\frac{b}{c+a}+\frac{c}{a+b}\ge\frac32.$$""",
     r"""<p>Rewrite each numerator so that all three fractions share the sum $a+b+c$:</p>
<p>$$\frac{a}{b+c}=\frac{a+b+c}{b+c}-1.$$</p>
<p>Adding cyclically gives</p>
<p>$$S=(a+b+c)\left(\frac1{a+b}+\frac1{b+c}+\frac1{c+a}\right)-3.$$</p>
<p>For positive $x,y,z$, Cauchy’s inequality gives $(x+y+z)(1/x+1/y+1/z)\ge9$. Apply it to $x=a+b$, $y=b+c$, $z=c+a$. Since $x+y+z=2(a+b+c)$,</p>
<p>$$2(a+b+c)\left(\frac1{a+b}+\frac1{b+c}+\frac1{c+a}\right)\ge9.$$</p>
<p>Therefore $S\ge9/2-3=3/2$. Equality requires $a+b=b+c=c+a$, hence $a=b=c$.</p>"""),
    (r"""Positive numbers $x,y$ satisfy $x+y=10$. Prove $xy\le25$, then explain why the proof identifies the unique maximum.""",
     r"""<p>From $(x-y)^2\ge0$ we obtain $x^2+y^2\ge2xy$. Therefore</p>
<p>$$100=(x+y)^2=x^2+2xy+y^2\ge4xy,$$</p>
<p>so $xy\le25$. Equality in the argument requires $(x-y)^2=0$, hence $x=y$. Together with $x+y=10$, this forces $x=y=5$.</p>
<p>Thus the maximum is not merely bounded by $25$; it is attained uniquely at $(5,5)$.</p>"""),
    (r"""For $x>0$, find and prove the global minimum of
$$x^2+\frac{16}{x^2}.$$""",
     r"""<p>Both terms are positive, so AM–GM applies:</p>
<p>$$x^2+\frac{16}{x^2}\ge2\sqrt{x^2\cdot\frac{16}{x^2}}=8.$$</p>
<p>Equality in AM–GM occurs when the two terms are equal:</p>
<p>$$x^2=\frac{16}{x^2}\Rightarrow x^4=16.$$</p>
<p>Because $x>0$, $x=2$. Hence the global minimum is $\boxed8$, attained only at $x=2$.</p>"""),
    (r"""Prove for positive $a,b$ that
$$\frac{a+b}{2}\ge\frac{2ab}{a+b}.$$
Interpret the result as a comparison of means.""",
     r"""<p>The denominator $a+b$ is positive, so multiplication by $2(a+b)$ preserves the inequality. The claim is equivalent to</p>
<p>$$(a+b)^2\ge4ab.$$</p>
<p>Subtracting the right side gives $(a-b)^2\ge0$, so the inequality is proved. Equality occurs exactly when $a=b$.</p>
<p>The left side is the arithmetic mean and the right side is the harmonic mean. Thus this proves $\mathrm{AM}\ge\mathrm{HM}$ for two positive numbers.</p>"""),
    (r"""Prove by induction that
$$1^2+2^2+\cdots+n^2=\frac{n(n+1)(2n+1)}6$$
for all positive integers $n$.""",
     r"""<p>Let $P(n)$ denote the stated identity.</p>
<p><strong>Base case:</strong> for $n=1$, the left side is $1$ and the right side is $1\cdot2\cdot3/6=1$.</p>
<p><strong>Inductive hypothesis:</strong> assume for some $k\ge1$ that
$$1^2+\cdots+k^2=\frac{k(k+1)(2k+1)}6.$$</p>
<p><strong>Inductive step:</strong> add the next square:</p>
<p>$$\begin{aligned}
1^2+\cdots+k^2+(k+1)^2
&=\frac{k(k+1)(2k+1)}6+(k+1)^2\\
&=\frac{(k+1)[k(2k+1)+6(k+1)]}{6}\\
&=\frac{(k+1)(2k^2+7k+6)}6\\
&=\frac{(k+1)(k+2)(2k+3)}6.
\end{aligned}$$</p>
<p>This is the required formula with $n=k+1$. Therefore $P(n)$ holds for every positive integer $n$ by induction.</p>"""),
    (r"""Prove by induction that
$$1^3+2^3+\cdots+n^3=\left[\frac{n(n+1)}2\right]^2.$$
Your algebra must make the target structure visible.""",
     r"""<p><strong>Base case:</strong> at $n=1$, both sides equal $1$.</p>
<p><strong>Hypothesis:</strong> assume $\sum_{r=1}^k r^3=[k(k+1)/2]^2$.</p>
<p><strong>Step:</strong></p>
<p>$$\begin{aligned}
\sum_{r=1}^{k+1}r^3
&=\left[\frac{k(k+1)}2\right]^2+(k+1)^3\\
&=(k+1)^2\left(\frac{k^2}{4}+k+1\right)\\
&=(k+1)^2\frac{(k+2)^2}{4}\\
&=\left[\frac{(k+1)(k+2)}2\right]^2.
\end{aligned}$$</p>
<p>Factoring $(k+1)^2$ rather than expanding everything exposes the $k+1$ target. The result follows for all $n\ge1$ by induction.</p>"""),
    (r"""Prove by induction that $8\mid(3^{2n}-1)$ for every positive integer $n$.""",
     r"""<p><strong>Base case:</strong> $3^2-1=8$.</p>
<p><strong>Hypothesis:</strong> suppose $3^{2k}-1=8m$ for some integer $m$.</p>
<p><strong>Step:</strong> deliberately create the hypothesised expression:</p>
<p>$$\begin{aligned}
3^{2(k+1)}-1
&=9\cdot3^{2k}-1\\
&=9(3^{2k}-1)+8\\
&=9(8m)+8\\
&=8(9m+1).
\end{aligned}$$</p>
<p>Since $9m+1$ is an integer, the next expression is divisible by $8$. The result follows by induction.</p>"""),
    (r"""Prove by induction that $11\mid(3^{5n}-1)$ for every positive integer $n$.""",
     r"""<p>First note $3^5=243=22\cdot11+1$, so $3^5-1$ is divisible by $11$.</p>
<p><strong>Base:</strong> this observation proves the $n=1$ case.</p>
<p><strong>Hypothesis:</strong> assume $3^{5k}-1=11m$.</p>
<p><strong>Step:</strong></p>
<p>$$\begin{aligned}
3^{5(k+1)}-1
&=3^5\cdot3^{5k}-1\\
&=3^5(3^{5k}-1)+(3^5-1)\\
&=243(11m)+242\\
&=11(243m+22).
\end{aligned}$$</p>
<p>Thus the claim propagates from $k$ to $k+1$, completing the induction.</p>"""),
    (r"""Prove by induction that $n!>2^n$ for every integer $n\ge4$.""",
     r"""<p><strong>Base:</strong> $4!=24>16=2^4$.</p>
<p><strong>Hypothesis:</strong> assume $k!>2^k$ for some $k\ge4$.</p>
<p><strong>Step:</strong></p>
<p>$$(k+1)!=(k+1)k!>(k+1)2^k.$$</p>
<p>Since $k+1\ge5>2$, we have $(k+1)2^k>2\cdot2^k=2^{k+1}$. Hence $(k+1)!>2^{k+1}$.</p>
<p>The base and inductive step prove the result for all $n\ge4$.</p>"""),
    (r"""Let $S_n=\sum_{r=1}^n\dfrac1{\sqrt r}$. Prove by induction that $S_n>\sqrt n$ for every integer $n\ge2$.""",
     r"""<p><strong>Base:</strong> $S_2=1+1/\sqrt2>\sqrt2$ because $1>1/\sqrt2$.</p>
<p><strong>Hypothesis:</strong> assume $S_k>\sqrt k$ for some $k\ge2$.</p>
<p><strong>Step:</strong></p>
<p>$$S_{k+1}=S_k+\frac1{\sqrt{k+1}}>\sqrt k+\frac1{\sqrt{k+1}}.$$</p>
<p>It remains to show the last expression exceeds $\sqrt{k+1}$. Rationalising the gap gives</p>
<p>$$\sqrt{k+1}-\sqrt k=\frac1{\sqrt{k+1}+\sqrt k}<\frac1{\sqrt{k+1}}.$$</p>
<p>Therefore $\sqrt k+1/\sqrt{k+1}>\sqrt{k+1}$, completing the induction.</p>"""),
    (r"""A sequence is defined by $a_1=1$ and $a_{n+1}=\sqrt{2+a_n}$. Prove that $1\le a_n<2$ for all $n$, and that $(a_n)$ is strictly increasing.""",
     r"""<p><strong>Bounds:</strong> the base $1\le a_1<2$ is clear. Assume $1\le a_k<2$. Then</p>
<p>$$\sqrt3\le a_{k+1}=\sqrt{2+a_k}<\sqrt4=2,$$</p>
<p>so in particular $1\le a_{k+1}<2$. Induction establishes the bounds.</p>
<p><strong>Increase:</strong> because $a_n\ge1>0$, compare squares:</p>
<p>$$a_{n+1}>a_n\iff 2+a_n>a_n^2\iff(2-a_n)(a_n+1)>0.$$</p>
<p>The bound $a_n<2$ and positivity of $a_n+1$ make the final product positive. Hence $a_{n+1}>a_n$ for every $n$.</p>
<p>The proof illustrates a common strategy: first inductively establish an invariant interval, then use that interval to prove monotonicity.</p>"""),
    (r"""Prove the binomial theorem by induction:
$$(x+y)^n=\sum_{r=0}^n\binom nr x^{n-r}y^r.$$""",
     r"""<p><strong>Base:</strong> for $n=0$, both sides equal $1$.</p>
<p><strong>Hypothesis:</strong> assume the formula holds for $n=k$.</p>
<p><strong>Step:</strong> multiply by $x+y$:</p>
<p>$$\begin{aligned}
(x+y)^{k+1}
&=\sum_{r=0}^k\binom kr x^{k+1-r}y^r
+\sum_{r=0}^k\binom kr x^{k-r}y^{r+1}\\
&=x^{k+1}+\sum_{r=1}^k\left[\binom kr+\binom k{r-1}\right]x^{k+1-r}y^r+y^{k+1}.
\end{aligned}$$</p>
<p>Pascal’s identity, $\binom kr+\binom k{r-1}=\binom{k+1}r$, changes this to</p>
<p>$$\sum_{r=0}^{k+1}\binom{k+1}r x^{k+1-r}y^r.$$</p>
<p>That is the desired $k+1$ formula, so induction proves the theorem.</p>"""),
    (r"""Use strong induction to prove that every integer $n\ge2$ is a product of primes.""",
     r"""<p><strong>Base:</strong> $2$ is itself prime, hence a product consisting of one prime.</p>
<p><strong>Strong hypothesis:</strong> assume every integer $m$ with $2\le m\le k$ is a product of primes.</p>
<p><strong>Step:</strong> consider $k+1$. If it is prime, it is already a product of primes. If it is composite, write $k+1=ab$ with $2\le a,b\le k$. By the strong hypothesis, both $a$ and $b$ are products of primes. Their product $ab=k+1$ is therefore also a product of primes.</p>
<p>Both cases prove the claim for $k+1$, so strong induction establishes it for all $n\ge2$.</p>"""),
    (r"""The Fibonacci numbers satisfy $F_1=F_2=1$ and $F_{n+1}=F_n+F_{n-1}$. Prove $F_n<2^n$ for every positive integer $n$.""",
     r"""<p>Because the recurrence uses two earlier terms, use strong induction.</p>
<p><strong>Bases:</strong> $F_1=1<2$ and $F_2=1<4$.</p>
<p><strong>Hypothesis:</strong> assume $F_j<2^j$ for all $1\le j\le k$, where $k\ge2$.</p>
<p><strong>Step:</strong></p>
<p>$$F_{k+1}=F_k+F_{k-1}<2^k+2^{k-1}<2^k+2^k=2^{k+1}.$$</p>
<p>Thus the bound holds for the next Fibonacci number, and strong induction completes the proof.</p>"""),
    (r"""Expose the flaw in the “all horses are the same colour” induction argument: assume every set of $k$ horses has one colour; for $k+1$ horses, remove the first horse, then remove the last, and use the overlapping groups to link their colours.""",
     r"""<p>The overlap argument fails exactly in the step from $k=1$ to $k=2$. The two one-horse groups obtained by removing the first or last horse are disjoint, so there is no shared horse whose colour links the groups.</p>
<p>For $k\ge2$ the groups do overlap, but induction cannot jump over the failed $1\Rightarrow2$ link. This is why checking that the inductive mechanism works at the base boundary is essential.</p>"""),
    (r"""Prove Bernoulli’s inequality by induction: for $x\ge-1$ and every integer $n\ge0$,
$$(1+x)^n\ge1+nx.$$""",
     r"""<p><strong>Base:</strong> for $n=0$, both sides equal $1$.</p>
<p><strong>Hypothesis:</strong> assume $(1+x)^k\ge1+kx$ for a fixed $x\ge-1$.</p>
<p>Because $1+x\ge0$, multiplying by $1+x$ preserves the inequality:</p>
<p>$$\begin{aligned}
(1+x)^{k+1}
&\ge(1+kx)(1+x)\\
&=1+(k+1)x+kx^2\\
&\ge1+(k+1)x,
\end{aligned}$$</p>
<p>since $kx^2\ge0$. This proves the $k+1$ case. Equality occurs for all $n$ when $x=0$, and also in the trivial low-index cases.</p>"""),
    (r"""Prove by induction the non-obvious product identity
$$\prod_{r=2}^{n}\left(1-\frac1{r^2}\right)=\frac{n+1}{2n}\qquad(n\ge2).$$""",
     r"""<p><strong>Base:</strong> for $n=2$, the product is $1-1/4=3/4$, while $(2+1)/(2\cdot2)=3/4$.</p>
<p><strong>Hypothesis:</strong> assume the product through $r=k$ equals $(k+1)/(2k)$.</p>
<p><strong>Step:</strong> multiply by the next factor and factor its difference of squares:</p>
<p>$$\begin{aligned}
\prod_{r=2}^{k+1}\left(1-\frac1{r^2}\right)
&=\frac{k+1}{2k}\left(1-\frac1{(k+1)^2}\right)\\
&=\frac{k+1}{2k}\cdot\frac{k(k+2)}{(k+1)^2}\\
&=\frac{k+2}{2(k+1)}.
\end{aligned}$$</p>
<p>This is the target with $n=k+1$, so the identity follows by induction.</p>"""),
    (r"""A sequence satisfies $u_1=3$ and $u_{n+1}=\dfrac12\left(u_n+\dfrac5{u_n}\right)$. Prove $u_n>\sqrt5$ for every $n$, and explain the equality obstruction.""",
     r"""<p>The base case is $u_1=3>\sqrt5$.</p>
<p>Assume $u_k>\sqrt5$, so $u_k>0$. Compare the next term with $\sqrt5$:</p>
<p>$$\begin{aligned}
u_{k+1}-\sqrt5
&=\frac12\left(u_k+\frac5{u_k}-2\sqrt5\right)\\
&=\frac{(u_k-\sqrt5)^2}{2u_k}>0.
\end{aligned}$$</p>
<p>The denominator is positive and the numerator is a nonzero square, so $u_{k+1}>\sqrt5$. Induction proves the bound.</p>
<p>Equality could occur only if $u_k=\sqrt5$. Since the sequence starts strictly above $\sqrt5$, the displayed identity preserves strictness at every step.</p>"""),
]

week_b_body = r"""
<section id="source"><div class="section-title"><span class="tag">Start</span> Textbook map and goal</div>
<div class="source-box"><span class="box-label">Primary source</span><p>Steve Howard, Chapter 1.5–1.6 (inequality proofs and AM–GM, pp. 44–76) and Chapter 3 (further mathematical induction, pp. 215–245).</p>
<p><a href="../dpen22/HSC-Mathematics-Extension-2-Textbook-v9-2021-12-03.pdf#page=45" target="_blank">Open inequality proofs ↗</a> · <a href="../dpen22/HSC-Mathematics-Extension-2-Textbook-v9-2021-12-03.pdf#page=216" target="_blank">Open further induction ↗</a></p></div></section>

<section id="inequalities"><div class="section-title"><span class="tag">01</span> Inequality proof toolkit</div>
<div class="prose"><p>Most algebraic inequality proofs transform the difference between two sides into an expression known to be non-negative. The engine is usually a square:</p>
<p>$$(u-v)^2\ge0\quad\Rightarrow\quad u^2+v^2\ge2uv.$$</p>
<ul><li>Adding the same quantity preserves direction.</li><li>Multiplying by a positive quantity preserves direction.</li><li>Multiplying by a negative quantity reverses direction.</li><li>Never divide by an expression until its sign is known.</li></ul></div>
<div class="example"><h3>Example — a rational inequality</h3><p>For $x>0$, prove $x+\dfrac1x\ge2$. Since $(x-1)^2\ge0$, $x^2+1\ge2x$. Dividing by $x>0$ gives the result.</p></div></section>

<section id="amgm"><div class="section-title"><span class="tag">02</span> Arithmetic mean–geometric mean</div>
<div class="prose"><p>For positive $a,b$:</p><p>$$\frac{a+b}{2}\ge\sqrt{ab},$$</p><p>with equality exactly when $a=b$. It converts fixed-product problems into minimum-sum results and fixed-sum problems into maximum-product results.</p></div>
<div class="example"><h3>Proof from a square</h3><p>$(\sqrt a-\sqrt b)^2\ge0$ gives $a+b-2\sqrt{ab}\ge0$. Rearranging and dividing by $2$ proves AM–GM.</p></div>
<div class="source-box"><span class="box-label">Additional NSW practice</span><p><a href="https://classmathematics.com.au/resources/nsw/year-12/maths-extension-2/proof/induction-inequalities/" target="_blank" rel="noopener">Class Mathematics — induction inequalities videos and practice ↗</a></p></div></section>

<section id="induction"><div class="section-title"><span class="tag">03</span> Mathematical induction — the four-part contract</div>
<div class="video-box"><span class="box-label">Watch first</span><div class="video-row">
__VIDEO_B1__
__VIDEO_B2__
__VIDEO_B3__
</div></div>
<table><thead><tr><th>Part</th><th>What to write</th><th>Purpose</th></tr></thead><tbody>
<tr><td>1. Proposition</td><td>Define $P(n)$ and its domain.</td><td>States the exact claim.</td></tr>
<tr><td>2. Base case</td><td>Verify the smallest allowed $n$.</td><td>Starts the chain.</td></tr>
<tr><td>3. Hypothesis + step</td><td>Assume $P(k)$; use it to prove $P(k+1)$.</td><td>Links each case to the next.</td></tr>
<tr><td>4. Conclusion</td><td>Invoke induction and restate the domain.</td><td>Completes the proof.</td></tr></tbody></table>
<div class="warning"><span class="box-label">Two common failures</span><p>Do not assume $P(k+1)$; that is what you must prove. Do not merely replace every $k$ by $k+1$ in the hypothesis. Start from one side of $P(k+1)$ and deliberately make the $P(k)$ expression appear.</p></div></section>

<section id="series"><div class="section-title"><span class="tag">04</span> Induction for sums and divisibility</div>
<div class="example"><h3>Series move</h3><p>For a sum, write the $k+1$ case as “the sum to $k$ + the next term”, then substitute the inductive hypothesis.</p></div>
<div class="example"><h3>Divisibility move</h3><p>If the hypothesis says $A_k=dm$, manipulate $A_{k+1}$ until it contains a multiple of $A_k$ plus another obvious multiple of $d$.</p></div>
<div class="source-box"><span class="box-label">Structured follow-up</span><p><a href="https://www.matrix.edu.au/beginners-guide-year-12-maths-ext-1/mathematical-induction/" target="_blank" rel="noopener">Matrix Education — induction guide with series and divisibility ↗</a></p></div></section>

<section id="inductineq"><div class="section-title"><span class="tag">05</span> Induction for inequalities</div>
<div class="prose"><p>An equality hypothesis can be substituted exactly. An inequality hypothesis only supplies a bound. The inductive step therefore usually has two links:</p>
<p>$$L_{k+1}\ \ge\ \underbrace{\text{bound from }P(k)}_{\text{use the hypothesis}}\ \ge\ R_{k+1}.$$</p>
<p>You must justify both inequalities and check the range where the second one is true.</p></div>
<div class="example"><h3>Example — prove $2^n\ge n+1$ for $n\ge0$</h3><p>Base: $2^0=1$. Assume $2^k\ge k+1$. Then $2^{k+1}=2\cdot2^k\ge2(k+1)\ge k+2$ because $k\ge0$. Therefore the claim follows by induction.</p></div></section>

<section id="practice"><div class="section-title"><span class="tag">06</span> 30 exam-quality proof problems</div>
<div class="why-box"><span class="box-label">How to use this set</span><p>The sequence moves from inequality structure and equality cases into non-routine induction, proof repair, recurrences, strong induction and invariant bounds. Every revealed answer explains why the method works—not only the algebra needed to finish.</p></div>
__PRACTICE_B__</section>

<section id="bridge"><div class="section-title"><span class="tag">Bridge</span> Why this belongs before MATH142</div>
<div class="why-box"><span class="box-label">Proof habits used later</span><p>Convergence tests depend on precise implication and inequality direction. Taylor error bounds use quantified statements. Differential-equation verification separates existence from checking a candidate. These two proof weeks make the reasoning underneath Weeks 1–12 visible.</p></div></section>
"""
week_b_body = (
    week_b_body
    .replace("__VIDEO_B1__", video(
        "Inequality Proofs",
        "Toby McGrath · HSC Extension 2 Mathematics",
        "fKPGXBz05tI",
        "NSW syllabus-aligned techniques for proving inequalities from sound algebraic steps.",
    ))
    .replace("__VIDEO_B2__", video(
        "Further Induction Proofs",
        "Toby McGrath · HSC Extension 2 Mathematics",
        "qzKHER_SbRg",
        "The first Extension 2 lesson on moving beyond elementary induction proofs.",
    ))
    .replace("__VIDEO_B3__", video(
        "Applications of Mathematical Induction",
        "Toby McGrath · HSC Extension 2 Mathematics",
        "QQq7lWERixs",
        "Applies induction beyond routine finite-sum identities.",
    ))
    .replace("__PRACTICE_B__", "".join(
        practice(i, q, s) for i, (q, s) in enumerate(week_b_practice, 1)
    ))
)

page(
    filename="MATH142_Ext2Proofs_WeekA_NatureOfProof.html",
    week="Extension Week A",
    title="The Nature of Proof",
    subtitle="Statements, quantifiers, direct proof, contraposition, contradiction, equivalence and counterexamples — a rigorous bridge into university mathematics.",
    toc=[("source", "Textbook map"), ("language", "Logic and quantifiers"), ("direct", "Direct proof"),
         ("indirect", "Contrapositive and contradiction"), ("equivalence", "Equivalence and disproof"),
         ("practice", "Practice"), ("next", "Next week")],
    body=week_a_body,
    previous="MATH142_Week0_Lay_of_the_Land.html",
    next_page="MATH142_Ext2Proofs_WeekB_InductionInequalities.html",
    practice_count=len(week_a_practice),
)

page(
    filename="MATH142_Ext2Proofs_WeekB_InductionInequalities.html",
    week="Extension Week B",
    title="Inequalities and Further Mathematical Induction",
    subtitle="Build inequality proofs from non-negative squares, use AM–GM, and write complete induction proofs for sums, divisibility and inequalities.",
    toc=[("source", "Textbook map"), ("inequalities", "Inequality toolkit"), ("amgm", "AM–GM"),
         ("induction", "Induction template"), ("series", "Sums and divisibility"),
         ("inductineq", "Induction inequalities"), ("practice", "Practice"), ("bridge", "MATH142 bridge")],
    body=week_b_body,
    previous="MATH142_Ext2Proofs_WeekA_NatureOfProof.html",
    next_page="MATH142_Week1_Integration_Techniques.html",
    practice_count=len(week_b_practice),
)

print("Wrote two MATH142 Extension 2 proof lessons.")
