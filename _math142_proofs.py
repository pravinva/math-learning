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
     r"""<p>The negation of “for every” is “there exists”, and $>0$ becomes $\le0$:</p>
<p>$$\boxed{\text{There exists }x\in\mathbb R\text{ such that }x^2+1\le0.}$$</p>"""),
    (r"""Write the converse and contrapositive of: “If $n$ is divisible by $6$, then $n$ is even.”""",
     r"""<p><strong>Converse:</strong> If $n$ is even, then $n$ is divisible by $6$ (false: $n=2$).</p>
<p><strong>Contrapositive:</strong> If $n$ is not even, then $n$ is not divisible by $6$ (true and equivalent to the original).</p>"""),
    (r"""Prove directly that the sum of two odd integers is even.""",
     r"""<p>Let the odd integers be $2a+1$ and $2b+1$, where $a,b\in\mathbb Z$. Then</p>
<p>$$(2a+1)+(2b+1)=2(a+b+1).$$</p><p>Since $a+b+1\in\mathbb Z$, the sum is twice an integer and is therefore even.</p>"""),
    (r"""Prove directly: if $3\mid a$ and $3\mid b$, then $9\mid ab$.""",
     r"""<p>Write $a=3r$ and $b=3s$ for integers $r,s$. Then $ab=9rs$. Since $rs\in\mathbb Z$, $9\mid ab$.</p>"""),
    (r"""Prove by contraposition: if $n^2$ is divisible by $3$, then $n$ is divisible by $3$.""",
     r"""<p>Prove the contrapositive. If $3\nmid n$, then $n=3q+1$ or $n=3q+2$. Squaring gives</p>
<p>$$(3q+1)^2=3(3q^2+2q)+1,\qquad(3q+2)^2=3(3q^2+4q+1)+1.$$</p>
<p>In either case $3\nmid n^2$. Therefore, by contraposition, $3\mid n^2\Rightarrow3\mid n$.</p>"""),
    (r"""Prove by contradiction that there is no greatest integer.""",
     r"""<p>Assume there is a greatest integer $N$. But $N+1$ is also an integer and $N+1>N$, contradicting the choice of $N$. Hence no greatest integer exists.</p>"""),
    (r"""Prove by contradiction that $\sqrt5$ is irrational.""",
     r"""<p>Assume $\sqrt5=p/q$ in lowest terms, with integers $p,q$ and $q\ne0$. Then $p^2=5q^2$, so $5\mid p$; write $p=5r$. Substitution gives $q^2=5r^2$, so $5\mid q$. This contradicts $p/q$ being in lowest terms. Thus $\sqrt5$ is irrational.</p>"""),
    (r"""Prove that an integer $n$ is odd if and only if $n^2$ is odd.""",
     r"""<p><strong>Forward:</strong> if $n=2k+1$, then $n^2=2(2k^2+2k)+1$, so $n^2$ is odd.</p>
<p><strong>Reverse:</strong> if $n^2$ is odd, then $n$ cannot be even, because $n=2k$ would give $n^2=4k^2$, even. Hence $n$ is odd.</p>"""),
    (r"""Disprove: “$n^2+n+41$ is prime for every positive integer $n$.”""",
     r"""<p>One counterexample is enough. At $n=41$:</p><p>$$41^2+41+41=41(41+2)=41\cdot43,$$</p><p>which is composite. Therefore the universal statement is false.</p>"""),
    (r"""A student writes: “$2,3,5,7$ are prime, so every integer from $2$ onward is prime.” Identify the logical error.""",
     r"""<p>Checking examples can suggest a conjecture but cannot prove a universal statement. The claim is also false: $4$ is a counterexample.</p>"""),
]

week_a_body = r"""
<section id="source"><div class="section-title"><span class="tag">Start</span> Textbook map and goal</div>
<div class="source-box"><span class="box-label">Primary source</span><p>Steve Howard, <em>HSC Mathematics Extension 2</em> (December 2021), Chapter 1: pp. 7–43 for language, direct proof, contrapositive, contradiction, equivalence and disproof; pp. 44–76 continue into inequalities and AM–GM.</p>
<p><a href="../dpen22/HSC-Mathematics-Extension-2-Textbook-v9-2021-12-03.pdf#page=7" target="_blank">Open the local textbook at Chapter 1 ↗</a></p></div>
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
</div></div>
<div class="prose"><p><strong>Contrapositive:</strong> to prove $P\Rightarrow Q$, prove the equivalent statement $\neg Q\Rightarrow\neg P$. This is ideal when the negation of $Q$ has a useful algebraic form.</p>
<p><strong>Contradiction:</strong> assume the claim is false, then derive an impossibility: a number is both odd and even, a reduced fraction has a common factor, or a quantity is simultaneously $&lt;a$ and $\ge a$.</p></div>
<div class="warning"><span class="box-label">Do not confuse them</span><p>Contrapositive begins with $\neg Q$ and aims for $\neg P$. Contradiction assumes enough to negate the whole target and aims for any contradiction.</p></div></section>

<section id="equivalence"><div class="section-title"><span class="tag">04</span> Equivalence, existence and disproof</div>
<div class="prose"><p>To prove $P\Leftrightarrow Q$, prove both directions separately. To prove existence, construct one object or show why one must exist. To disprove a universal statement, give one valid counterexample and check it explicitly.</p></div>
<div class="example"><h3>Example — disprove a tempting pattern</h3><p>The claim “$n^2-n+11$ is prime for every positive integer $n$” is false. Set $n=11$: $11^2-11+11=121=11^2$.</p></div></section>

<section id="practice"><div class="section-title"><span class="tag">05</span> Practice — write complete arguments</div>
<div class="why-box"><span class="box-label">Proof checklist</span><p>Declare variables and domains; name the method; state assumptions; justify each implication; use full sentences; finish with the exact claim.</p></div>
__PRACTICE_A__</section>

<section id="next"><div class="section-title"><span class="tag">Next</span> Move to inequalities and induction</div>
<div class="prose"><p>Week B adds inequality machinery, AM–GM and further mathematical induction. These methods feed directly into convergence arguments in MATH142 Weeks 10–12.</p></div></section>
"""
week_a_body = (
    week_a_body
    .replace("__VIDEO_A1__", video(
        "Proof by Contrapositive — method and first example",
        "Dr. Trefor Bazett · Discrete Mathematics",
        "0YqZIHFmVzg",
        "Shows why proving not-Q implies not-P can be cleaner than attacking P implies Q directly.",
    ))
    .replace("__VIDEO_A2__", video(
        "Proof by Contradiction (1 of 2): How does it work?",
        "Eddie Woo · Wootube",
        "rV9esU9gHO8",
        "An Australian classroom explanation of assuming the negation and forcing an impossibility.",
    ))
    .replace("__PRACTICE_A__", "".join(
        practice(i, q, s) for i, (q, s) in enumerate(week_a_practice, 1)
    ))
)

week_b_practice = [
    (r"""Prove that $x^2+4x+7>0$ for every real $x$.""",
     r"""<p>Complete the square: $x^2+4x+7=(x+2)^2+3$. Since $(x+2)^2\ge0$, the expression is at least $3$, hence strictly positive.</p>"""),
    (r"""For positive $a,b$, prove $\dfrac ab+\dfrac ba\ge2$.""",
     r"""<p>Because $(a-b)^2\ge0$, $a^2+b^2\ge2ab$. Divide by $ab>0$ (so the direction is unchanged): $\dfrac ab+\dfrac ba\ge2$. Equality occurs at $a=b$.</p>"""),
    (r"""Use AM–GM to find the minimum of $x+\dfrac9x$ for $x>0$.""",
     r"""<p>AM–GM gives $x+\dfrac9x\ge2\sqrt{x(9/x)}=6$. Equality requires $x=9/x$, so $x=3$. The minimum is $\boxed6$.</p>"""),
    (r"""Prove by induction that $1+3+\cdots+(2n-1)=n^2$ for $n\ge1$.""",
     r"""<p><strong>Base:</strong> $n=1$: $1=1^2$.</p><p><strong>Hypothesis:</strong> assume $1+3+\cdots+(2k-1)=k^2$.</p>
<p><strong>Step:</strong> add the next odd number: $k^2+[2(k+1)-1]=k^2+2k+1=(k+1)^2$.</p><p>Therefore the identity holds for all $n\ge1$ by induction.</p>"""),
    (r"""Prove by induction that $6\mid(7^n-1)$ for every integer $n\ge1$.""",
     r"""<p><strong>Base:</strong> $7^1-1=6$.</p><p>Assume $7^k-1=6m$. Then</p>
<p>$$7^{k+1}-1=7(7^k-1)+6=7(6m)+6=6(7m+1).$$</p><p>Thus it is divisible by $6$, completing the induction.</p>"""),
    (r"""Prove by induction that $2^n\ge n+1$ for all $n\ge0$.""",
     r"""<p><strong>Base:</strong> $2^0=1=0+1$.</p><p>Assume $2^k\ge k+1$. Then $2^{k+1}=2\cdot2^k\ge2(k+1)\ge k+2$ because $k\ge0$. Hence the result follows by induction.</p>"""),
    (r"""Prove by induction that $3^n>n^2$ for every integer $n\ge3$.""",
     r"""<p><strong>Base:</strong> $3^3=27>9$.</p><p>Assume $3^k>k^2$ for $k\ge3$. Then $3^{k+1}>3k^2$. Also</p>
<p>$$3k^2-(k+1)^2=2k^2-2k-1>0\quad(k\ge3).$$</p><p>Therefore $3^{k+1}>(k+1)^2$, and induction completes the proof.</p>"""),
    (r"""Prove $1+\dfrac12+\cdots+\dfrac1{2^n}=2-\dfrac1{2^n}$ for $n\ge0$.""",
     r"""<p><strong>Base:</strong> at $n=0$, both sides equal $1$.</p><p>Assume the result for $k$. Then</p>
<p>$$\left(2-\frac1{2^k}\right)+\frac1{2^{k+1}}
=2-\frac2{2^{k+1}}+\frac1{2^{k+1}}
=2-\frac1{2^{k+1}}.$$</p><p>The result follows by induction.</p>"""),
    (r"""What is wrong with: “Assume $2^k>k^2$. Then $2^{k+1}>2k^2>(k+1)^2$”? Repair it for $k\ge5$.""",
     r"""<p>The second inequality is not automatic and must be proved. For $k\ge5$:</p>
<p>$$2k^2-(k+1)^2=k^2-2k-1=(k-1)^2-2>0.$$</p><p>With this extra justification, the inductive step is valid (after checking the base case $n=5$).</p>"""),
    (r"""A rectangle has positive side lengths $x,y$ and fixed area $xy=36$. Prove its perimeter is at least $24$.""",
     r"""<p>By AM–GM, $x+y\ge2\sqrt{xy}=12$. Thus the perimeter $2x+2y=2(x+y)\ge24$. Equality occurs when $x=y=6$.</p>"""),
]

week_b_body = r"""
<section id="source"><div class="section-title"><span class="tag">Start</span> Textbook map and goal</div>
<div class="source-box"><span class="box-label">Primary source</span><p>Steve Howard, Chapter 1.5–1.6 (inequality proofs and AM–GM, pp. 44–76) and Chapter 3 (further mathematical induction, pp. 215–245).</p>
<p><a href="../dpen22/HSC-Mathematics-Extension-2-Textbook-v9-2021-12-03.pdf#page=44" target="_blank">Open inequality proofs ↗</a> · <a href="../dpen22/HSC-Mathematics-Extension-2-Textbook-v9-2021-12-03.pdf#page=215" target="_blank">Open further induction ↗</a></p></div></section>

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

<section id="practice"><div class="section-title"><span class="tag">06</span> Practice — from foundations to Extension 2</div>
__PRACTICE_B__</section>

<section id="bridge"><div class="section-title"><span class="tag">Bridge</span> Why this belongs before MATH142</div>
<div class="why-box"><span class="box-label">Proof habits used later</span><p>Convergence tests depend on precise implication and inequality direction. Taylor error bounds use quantified statements. Differential-equation verification separates existence from checking a candidate. These two proof weeks make the reasoning underneath Weeks 1–12 visible.</p></div></section>
"""
week_b_body = (
    week_b_body
    .replace("__VIDEO_B1__", video(
        "Proof by induction",
        "Khan Academy",
        "wblW_M_HVQ8",
        "A clear first pass through the base case, hypothesis and inductive step for a finite sum.",
    ))
    .replace("__VIDEO_B2__", video(
        "Mathematical Induction Practice Problems",
        "The Organic Chemistry Tutor",
        "tHNVX3e9zd0",
        "Worked induction examples with the algebra written out carefully.",
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
