#!/usr/bin/env python3
"""Generate DPEN100 Engineering Analysis projects (questions + full worked answers)."""
from pathlib import Path
import html as H
import shutil

OUT = Path(__file__).resolve().parent / 'siddharth' / 'dpen100' / 'projects'
STUDY = Path('/Users/pravin.varma/Documents/Study/DPEN100')

CSS = r'''
:root{--navy:#1B3A5C;--orange:#FF3621;--blue:#185FA5;--bg:#fafaf8;--text:#2c2a28;--muted:#6b6762;--line:#e8e6e0;--green:#15803d;--amber:#b45309;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Georgia,"Times New Roman",serif;background:var(--bg);color:var(--text);line-height:1.65;padding:28px 18px 80px}
.wrap{max-width:940px;margin:0 auto;background:#fff;border:1px solid var(--line);padding:28px 30px 42px;border-radius:10px}
.eyebrow{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
h1{font-size:clamp(24px,3.2vw,34px);color:var(--navy);margin-bottom:8px}
h2{font-size:20px;color:var(--navy);margin:28px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--navy)}
h3{font-size:16px;color:var(--blue);margin:16px 0 8px}
.sub{color:var(--muted);margin-bottom:14px}
.tag{display:inline-block;background:var(--orange);color:#fff;font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;margin-bottom:8px}
.chiprow{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}
.chip{display:inline-block;padding:8px 12px;border-radius:6px;text-decoration:none;font-size:13px;font-weight:600;border:1px solid #c9dff7;background:#eef6ff;color:var(--blue)}
.chip.on{background:var(--navy);border-color:var(--navy);color:#fff}
.chip.pdf{background:#fff7ed;border-color:#f0b429;color:var(--amber)}
.chip.ans{background:#f0fdf4;border-color:#86efac;color:var(--green)}
.prep{background:#eef6ff;border:1px solid #c9dff7;border-radius:10px;padding:16px 18px;margin:16px 0 22px}
.prep h2{margin:0 0 10px;border:0;padding:0;font-size:18px;color:var(--navy)}
.prep h3{margin:14px 0 6px;font-size:14px;color:var(--blue);text-transform:uppercase;letter-spacing:.04em}
.prep ul{margin:0 0 0 18px}.prep li{margin:4px 0}
.prep .ml{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.prep .ml code{background:#fff;border:1px solid #c9dff7;padding:3px 8px;border-radius:4px;font-size:12.5px;color:var(--navy)}
.card{background:#f8fafc;border:1px solid var(--line);border-radius:10px;padding:16px 18px;margin:0 0 14px}
.q{background:#f8fafc;border:1px solid var(--line);border-radius:8px;padding:14px 16px;margin:12px 0}
.q ol{margin:8px 0 0 22px}.q li{margin:5px 0}
.deliv{background:#fff7ed;border-left:4px solid #f0b429;padding:10px 12px;margin-top:10px;border-radius:0 6px 6px 0;font-size:14px}
.ans{background:#f0fdf4;border-left:4px solid var(--green);padding:12px 14px;margin:10px 0;border-radius:0 6px 6px 0;overflow-x:auto}
.ans h3{margin-top:0}
code,pre{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px}
pre{background:#1e293b;color:#e2e8f0;padding:12px 14px;border-radius:8px;overflow-x:auto;margin:10px 0;line-height:1.45}
.note{background:#fffbeb;border:1px solid #fde68a;border-radius:8px;padding:12px 14px;margin:12px 0;font-size:14px}
.meta{font-size:13px;color:var(--muted);margin:4px 0 10px}
table.data{border-collapse:collapse;width:100%;margin:10px 0;font-size:14px}
table.data th,table.data td{border:1px solid #c9dff7;padding:7px 8px;text-align:center}
table.data th{background:#eef6ff;color:var(--navy)}
.figcap{font-size:13px;color:var(--muted);text-align:center;margin:4px 0 12px}
@media(max-width:640px){.wrap{padding:18px 14px 32px}}
'''


def page(title, body):
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{H.escape(title)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'\\\\[',right:'\\\\]',display:true}},{{left:'\\\\(',right:'\\\\)',display:false}}]}});"></script>
<style>{CSS}</style>
</head><body><div class="wrap">
{body}
</div></body></html>
'''


def nav(current=''):
    items = [
        ('../github-setup.html', 'GitHub setup'),
        ('index.html', 'Projects hub'),
        ('project1.html', 'Project 1'),
        ('project1-answers.html', 'P1 answers'),
        ('project2.html', 'Project 2'),
        ('project2-answers.html', 'P2 answers'),
        ('../practicals/index.html', 'Practicals'),
        ('../index.html', 'DPEN100 home'),
    ]
    chips = []
    for href, lab in items:
        cls = 'chip'
        if href == current:
            cls += ' on'
        if 'answers' in href:
            cls += ' ans'
        chips.append(f'<a class="{cls}" href="{href}">{lab}</a>')
    return f'<div class="chiprow">{"".join(chips)}</div>'


def prep_box(ideas, matlab, also=None):
    idea_li = ''.join(f'<li>{x}</li>' for x in ideas)
    ml = ''.join(f'<code>{x}</code>' for x in matlab)
    also_html = ''
    if also:
        also_html = '<h3>Also useful</h3><ul>' + ''.join(f'<li>{x}</li>' for x in also) + '</ul>'
    return f'''<div class="prep">
<h2>Before you start — key ideas &amp; MATLAB</h2>
<h3>Concepts &amp; ideas</h3>
<ul>{idea_li}</ul>
<h3>MATLAB functionality you will use</h3>
<div class="ml">{ml}</div>
{also_html}
</div>'''


# ───────────────────── Project 1 ─────────────────────

def build_project1():
    prep = prep_box(
        ideas=[
            r'<strong>Engineering Analysis (ENGG100/DPEN100):</strong> use MATLAB to analyse rectilinear and curvilinear motion — track position, velocity, acceleration and produce professional plots.',
            r'<strong>Rectilinear:</strong> 1-D motion along a path; \(v=\mathrm{d}s/\mathrm{d}t\), \(a=\mathrm{d}v/\mathrm{d}t\); SUVAT when \(a\) is constant.',
            r'<strong>Path distance:</strong> cumulative distance from successive coordinate samples \(\sum\sqrt{(\Delta E)^2+(\Delta N)^2+(\Delta z)^2}\).',
            r'<strong>Curvilinear / projectile:</strong> independent \(x\) and \(y\) motion with constant \(a_x=0\), \(a_y=-g\).',
            r'<strong>Vectorisation:</strong> compute velocity for all samples at once with <code>diff</code> / array ops — not one scalar at a time in a slow nested style.',
        ],
        matlab=['plot', 'plot3', 'subplot', 'xlabel', 'ylabel', 'zlabel', 'title', 'legend', 'grid', 'diff', 'cumsum', 'sqrt', 'hold on', 'yyaxis', 'linspace', 'max', 'min', 'trapz'],
        also=[
            'Label every graph (units in axis labels)',
            'Comment your script: Input / Operations / Output',
            'Save figures (File → Save As / <code>saveas</code>) for your report',
        ],
    )

    qs = r'''
<div class="note"><strong>Context.</strong> UOW’s Engineering Analysis focus in ENGG100/DPEN100 is using MATLAB on kinematics of rectilinear and curvilinear motion.
This project mirrors the <em>Major Project</em> style (kinematic plots &amp; analysis) using a compact synthetic “GPS ride” dataset so you can finish without GPX parsing.
A sample student major-project PDF is linked on the hub for comparison.</div>

{prep}

<h2>Given data — synthetic bike segment</h2>
<p>Eastings \(E\), Northings \(N\) and elevation \(z\) are already relative to the start (origin). Time \(t\) is in seconds.</p>
<table class="data">
<tr><th>\(t\) (s)</th><th>\(E\) (m)</th><th>\(N\) (m)</th><th>\(z\) (m)</th></tr>
<tr><td>0</td><td>0</td><td>0</td><td>20</td></tr>
<tr><td>20</td><td>80</td><td>30</td><td>22</td></tr>
<tr><td>40</td><td>170</td><td>55</td><td>28</td></tr>
<tr><td>60</td><td>260</td><td>70</td><td>35</td></tr>
<tr><td>80</td><td>340</td><td>95</td><td>33</td></tr>
<tr><td>100</td><td>400</td><td>130</td><td>30</td></tr>
<tr><td>120</td><td>450</td><td>180</td><td>26</td></tr>
</table>
<p>Store these as row or column vectors in MATLAB, e.g.</p>
<pre>t = [0 20 40 60 80 100 120];
E = [0 80 170 260 340 400 450];   % m
N = [0 30 55 70 95 130 180];      % m
z = [20 22 28 35 33 30 26];       % m</pre>

<div class="q" id="q1">
<h3>Part A — 3D path &amp; elevation (rectilinear path description)</h3>
<ol type="a">
<li>Convert \(E\) and \(N\) to kilometres. Plot a 3-D path of Easting (km) vs Northing (km) vs elevation (m) using <code>plot3</code>. Label all axes and add a title and grid.</li>
<li>On one figure with a secondary axis (<code>yyaxis</code>), plot elevation \(z\) (m) vs \(t\) on the left, and elevation grade (%) vs \(t\) on the right.
Define grade between samples as
\[G_i = 100\cdot\frac{{z_{{i+1}}-z_i}}{{\Delta s_{{xy,i}}}},\quad
\Delta s_{{xy,i}}=\sqrt{{(E_{{i+1}}-E_i)^2+(N_{{i+1}}-N_i)^2}}.\]
Plot grade at the mid-time of each interval (or at \(t(1:end-1)\)).</li>
</ol>
<div class="deliv"><strong>Deliverable.</strong> Script <code>proj1_partA.m</code> + two labelled figures.</div>
</div>

<div class="q" id="q2">
<h3>Part B — Cumulative distance &amp; speed</h3>
<ol type="a">
<li>Compute segment lengths in 3-D:
\[\Delta s_i=\sqrt{{(\Delta E_i)^2+(\Delta N_i)^2+(\Delta z_i)^2}}\]
and the cumulative distance \(s(t)\) in km (<code>cumsum</code>). Plot \(s\) (km) vs \(t\) (s).</li>
<li>Estimate average speed on each segment \(v_i=\Delta s_i/\Delta t_i\) in km/h. Plot \(v\) vs \(t\) (use interval mid-times) and \(v\) vs cumulative distance.</li>
<li>Report numerically: total path length (km), mean speed (km/h), max segment speed (km/h).</li>
</ol>
<div class="deliv"><strong>Deliverable.</strong> Script <code>proj1_partB.m</code>, three plots, and a short numeric summary printed with <code>fprintf</code>.</div>
</div>

<div class="q" id="q3">
<h3>Part C — Curvilinear projectile (challenge analysis)</h3>
<p>A drone is launched from the origin with speed \(v_0=28\,\mathrm{{m/s}}\) at \(\theta=40^\circ\) above horizontal. Take \(g=9.81\,\mathrm{{m/s^2}}\), flat ground.</p>
<ol type="a">
<li>Using vectorisation, create \(t=\texttt{{linspace}}(0,T,200)\) up to the landing time \(T\), and arrays
\[x(t)= (v_0\cos\theta)\,t,\qquad y(t)= (v_0\sin\theta)\,t - \tfrac12 g t^2.\]</li>
<li>Plot the trajectory \(y\) vs \(x\). Mark the apex and landing point.</li>
<li>Compute analytically (and confirm from the arrays): time of flight, range, maximum height.</li>
</ol>
<div class="deliv"><strong>Deliverable.</strong> Script <code>proj1_partC.m</code> + trajectory figure + printed analytic results.</div>
</div>

<div class="q" id="q4">
<h3>Part D — Brief engineering write-up</h3>
<ol type="a">
<li>In ≤150 words: which segments of the ride are uphill / downhill based on grade, and where is speed highest? Relate to the elevation plot.</li>
<li>Explain why differentiating noisy GPS position with <code>diff</code> can amplify noise, and one practical remedy (e.g. smoothing / larger \(\Delta t\)).</li>
</ol>
<div class="deliv"><strong>Deliverable.</strong> Short answers in comments at the bottom of your main script, or a half-page <code>proj1_writeup.txt</code>.</div>
</div>
'''

    body = r'''
<div class="eyebrow">DPEN100 · ENGG100 · Engineering Analysis</div>
<span class="tag">PROJECT 1</span>
<h1>Kinematic plots &amp; analysis — ride data + projectile</h1>
<p class="sub">Major-project style: convert coordinate samples into distance, speed and elevation plots, then analyse a curvilinear projectile with vectorised MATLAB.</p>
__NAV__
<p><a class="chip ans" href="project1-answers.html">✅ Full worked answers (separate page)</a>
<a class="chip pdf" href="pdfs/engg100-major-project-group-p314-kinematic-plots-and-analysis.pdf" target="_blank" rel="noopener">Sample major project PDF</a></p>
{qs}'''.replace('__NAV__', nav('project1.html'))
    qs = qs.replace('{{', '{').replace('}}', '}').replace('{prep}', prep)
    body = body.replace('{qs}', qs)
    (OUT / 'project1.html').write_text(page('DPEN100 Project 1 — Questions', body))


def build_project1_answers():
    # Precomputed numbers for the synthetic data
    body = r'''
<div class="eyebrow">DPEN100 · ENGG100 · Engineering Analysis</div>
<span class="tag">PROJECT 1 · ANSWERS</span>
<h1>Project 1 — Full worked answers</h1>
<p class="sub">Complete MATLAB solutions, numeric results and discussion points. Attempt the questions before reading.</p>
__NAV__

<div class="ans"><h3>Part A — Model MATLAB</h3>
<pre>%% proj1_partA.m
t = [0 20 40 60 80 100 120];
E = [0 80 170 260 340 400 450];   % m
N = [0 30 55 70 95 130 180];
z = [20 22 28 35 33 30 26];

E_km = E/1000; N_km = N/1000;

figure(1)
plot3(E_km, N_km, z, '-o', 'LineWidth', 2)
xlabel('Easting (km)'); ylabel('Northing (km)'); zlabel('Elevation (m)')
title('3D path of bike segment'); grid on

dEx = diff(E); dNy = diff(N); dz = diff(z);
ds_xy = sqrt(dEx.^2 + dNy.^2);
grade = 100 * dz ./ ds_xy;          % %
t_mid = t(1:end-1) + diff(t)/2;

figure(2)
yyaxis left
plot(t, z, '-o', 'LineWidth', 2); ylabel('Elevation (m)')
yyaxis right
plot(t_mid, grade, '-s', 'LineWidth', 2); ylabel('Grade (%)')
xlabel('Time (s)'); title('Elevation and grade vs time'); grid on
legend('Elevation','Grade','Location','best')</pre>
<p>Grades (%): approximately \(2.34\), \(6.42\), \(7.67\), \(-2.39\), \(-4.32\), \(-5.66\)
→ climb through the first three intervals, then descent.</p>
</div>

<div class="ans"><h3>Part B — Distance &amp; speed</h3>
<pre>%% proj1_partB.m  (continue from Part A vectors)
dE = diff(E); dN = diff(N); dz = diff(z);
ds = sqrt(dE.^2 + dN.^2 + dz.^2);     % m
s_m = [0, cumsum(ds)];
s_km = s_m/1000;

figure(3)
plot(t, s_km, '-o', 'LineWidth', 2)
xlabel('Time (s)'); ylabel('Cumulative distance (km)')
title('Cumulative distance vs time'); grid on

dt = diff(t);
v_ms = ds ./ dt;           % m/s
v_kmh = v_ms * 3.6;        % km/h
t_mid = t(1:end-1) + dt/2;
s_mid = (s_km(1:end-1)+s_km(2:end))/2;

figure(4)
plot(t_mid, v_kmh, '-o', 'LineWidth', 2)
xlabel('Time (s)'); ylabel('Speed (km/h)')
title('Segment speed vs time'); grid on

figure(5)
plot(s_mid, v_kmh, '-o', 'LineWidth', 2)
xlabel('Cumulative distance (km)'); ylabel('Speed (km/h)')
title('Speed vs distance'); grid on

fprintf('Total path length = %.3f km\n', s_km(end));
fprintf('Mean speed = %.2f km/h\n', mean(v_kmh));
fprintf('Max segment speed = %.2f km/h\n', max(v_kmh));</pre>
<p><strong>Numeric results</strong> (2 d.p. where helpful):</p>
<ul>
<li>Segment lengths \(\Delta s\) (m): \(85.46\), \(93.60\), \(91.51\), \(83.84\), \(69.53\), \(70.82\)</li>
<li>Total path length \(s\approx 0.495\,\mathrm{km}\) (\(494.8\,\mathrm{m}\))</li>
<li>Speeds (km/h): \(15.4\), \(16.8\), \(16.5\), \(15.1\), \(12.5\), \(12.7\)</li>
<li>Mean speed \(\approx 14.8\,\mathrm{km/h}\); max \(\approx 16.8\,\mathrm{km/h}\) (second segment)</li>
</ul>
\[\boxed{s_{\mathrm{tot}}\approx 0.495\,\mathrm{km},\ \bar v\approx 14.8\,\mathrm{km/h},\ v_{\max}\approx 16.8\,\mathrm{km/h}}\]
</div>

<div class="ans"><h3>Part C — Projectile (analytic + MATLAB)</h3>
<p>With \(v_0=28\), \(\theta=40^\circ\), \(g=9.81\):</p>
\[
T=\frac{2v_0\sin\theta}{g}=\frac{2\cdot 28\cdot\sin 40^\circ}{9.81}\approx 3.669\,\mathrm{s}
\]
\[
R=(v_0\cos\theta)\,T\approx 78.70\,\mathrm{m},\qquad
H=\frac{(v_0\sin\theta)^2}{2g}\approx 16.51\,\mathrm{m}.
\]
<pre>%% proj1_partC.m
v0 = 28; th = 40*pi/180; g = 9.81;
T = 2*v0*sin(th)/g;
R = v0*cos(th)*T;
H = (v0*sin(th))^2/(2*g);

t = linspace(0, T, 200);
x = (v0*cos(th))*t;
y = (v0*sin(th))*t - 0.5*g*t.^2;

figure(6)
plot(x, y, 'LineWidth', 2); hold on
[~,k] = max(y);
plot(x(k), y(k), 'rs', 'MarkerSize', 8, 'LineWidth', 2)
plot(R, 0, 'ko', 'MarkerSize', 8, 'LineWidth', 2)
xlabel('x (m)'); ylabel('y (m)'); grid on
title('Projectile trajectory')
legend('Path','Apex','Landing','Location','best')

fprintf('T=%.3f s, Range=%.2f m, Hmax=%.2f m\n', T, R, H);</pre>
\[\boxed{T\approx 3.67\,\mathrm{s},\ R\approx 78.7\,\mathrm{m},\ H_{\max}\approx 16.5\,\mathrm{m}}\]
</div>

<div class="ans"><h3>Part D — Write-up (model)</h3>
<p><strong>(a)</strong> Positive grade on the first three intervals shows climbing while elevation rises from \(20\) to \(35\,\mathrm{m}\).
After \(t=60\,\mathrm{s}\) grade is negative and elevation falls — downhill. Segment speeds are highest mid-climb
(\(\approx 16.8\,\mathrm{km/h}\)) and drop on the steeper descent near the end (shorter \(\Delta s\) and more vertical change).</p>
<p><strong>(b)</strong> Finite differences \(\Delta s/\Delta t\) amplify high-frequency GPS jitter because noise in position is divided by a small \(\Delta t\).
Remedies: larger sampling interval, moving-average / Savitzky–Golay smoothing of \(E,N,z\) before <code>diff</code>, or fitting a smooth spline and differentiating the fit.</p>
</div>'''.replace('__NAV__', nav('project1-answers.html'))
    (OUT / 'project1-answers.html').write_text(page('DPEN100 Project 1 — Answers', body))


# ───────────────────── Project 2 ─────────────────────

def build_project2():
    prep = prep_box(
        ideas=[
            r'<strong>Piecewise rectilinear motion:</strong> constant \(a\) on successive phases (accel → cruise → brake); \(v\)–\(t\) areas give distance.',
            r'<strong>Erratic motion from graphs:</strong> slope of \(v\)–\(t\) = \(a\); area under \(v\)–\(t\) = \(\Delta s\).',
            r'<strong>Force vectors:</strong> resolve a cable/force \(F\) at angle \(\alpha\) into \(F_x=F\cos\alpha\), \(F_y=F\sin\alpha\).',
            r'<strong>Coupled story:</strong> a vehicle braking problem + a package projectile launch from a moving platform — typical Engineering Analysis mix.',
            r'<strong>Professional plots:</strong> always <code>xlabel</code>/<code>ylabel</code>/<code>title</code>/<code>legend</code>/<code>grid</code>.',
        ],
        matlab=['linspace', 'plot', 'hold on', 'xlabel', 'ylabel', 'title', 'legend', 'grid', 'subplot', 'fprintf', 'max', 'find', 'cumtrapz', 'gradient'],
        also=[
            'Choose a sign convention (forward +x, upward +y) and stick to it',
            'Use vectorisation for the projectile; loops are fine for piecewise vehicle phases if clearer',
        ],
    )

    qs = r'''
<div class="note"><strong>Context.</strong> A second Engineering Analysis mini-project: combine <em>rectilinear vehicle motion</em>, <em>projectile (curvilinear) delivery</em>, and <em>force resolution</em>.
No GPS file needed — all data is specified below.</div>

{prep}

<div class="q" id="q1">
<h3>Part A — Delivery van (piecewise rectilinear)</h3>
<p>A van starts from rest and must travel \(900\,\mathrm{{m}}\) then stop. It can accelerate at \(+2.0\,\mathrm{{m/s^2}}\), cruise at most \(20\,\mathrm{{m/s}}\), and brake at \(-4.0\,\mathrm{{m/s^2}}\).</p>
<ol type="a">
<li>Determine the shortest time to complete the trip (accel → cruise → brake). Draw / plot the \(v\)–\(t\) graph.</li>
<li>In MATLAB, build time arrays for each phase with \(\Delta t=0.05\,\mathrm{{s}}\) and concatenate \(t\), \(v(t)\), \(s(t)\). Plot \(s\), \(v\), \(a\) vs \(t\) in a \(3\times 1\) <code>subplot</code>.</li>
<li>Print total time and distance check (\(s_{{\mathrm{{final}}}}\) should be \(900\,\mathrm{{m}}\)).</li>
</ol>
<div class="deliv"><strong>Deliverable.</strong> <code>proj2_partA.m</code> + subplot figure + printed totals.</div>
</div>

<div class="q" id="q2">
<h3>Part B — Package tossed from the moving van (curvilinear)</h3>
<p>At the instant the van finishes accelerating (first reaches \(20\,\mathrm{{m/s}}\)), a package is tossed rearward relative to the van with relative speed \(8\,\mathrm{{m/s}}\) at \(35^\circ\) above the horizontal (relative to ground axes: use van velocity + relative velocity vector).
Release height is \(1.6\,\mathrm{{m}}\). Take \(g=9.81\,\mathrm{{m/s^2}}\).</p>
<ol type="a">
<li>Find the absolute initial velocity components \(v_{{0x}}\), \(v_{{0y}}\) of the package.</li>
<li>Simulate the flight until \(y=0\) with vectorised MATLAB. Plot the trajectory in the ground frame.</li>
<li>Report time of flight and landing position \(x_{{\mathrm{{land}}}}\) relative to the release point.</li>
</ol>
<div class="deliv"><strong>Deliverable.</strong> <code>proj2_partB.m</code> + trajectory plot + numeric flight results.</div>
</div>

<div class="q" id="q3">
<h3>Part C — Tow cable force resolution</h3>
<p>While parked, the van is held by a cable of tension \(T=2.5\,\mathrm{{kN}}\) at \(\alpha=25^\circ\) above the horizontal, attached to a bollard.</p>
<ol type="a">
<li>Resolve \(T\) into horizontal and vertical components.</li>
<li>In MATLAB, draw a simple 2-D arrow diagram of the force (plot the cable vector from the origin) and print \(T_x\), \(T_y\).</li>
</ol>
<div class="deliv"><strong>Deliverable.</strong> <code>proj2_partC.m</code> + force figure.</div>
</div>

<div class="q" id="q4">
<h3>Part D — Analysis questions</h3>
<ol type="a">
<li>If the cruise speed limit were reduced to \(15\,\mathrm{{m/s}}\), would the trip time increase or decrease? Explain using the \(v\)–\(t\) area idea (no full re-solve required, but a one-line estimate is welcome).</li>
<li>Why does tossing the package <em>rearward</em> relative to the van reduce its ground speed \(v_{{0x}}\)? Connect to vector addition of velocities.</li>
</ol>
</div>
'''

    body = r'''
<div class="eyebrow">DPEN100 · ENGG100 · Engineering Analysis</div>
<span class="tag">PROJECT 2</span>
<h1>Van logistics — rectilinear motion, projectile &amp; forces</h1>
<p class="sub">Second Engineering Analysis project: piecewise vehicle kinematics, a curvilinear package toss, and cable force components — all in MATLAB with full worked answers on a separate page.</p>
__NAV__
<p><a class="chip ans" href="project2-answers.html">✅ Full worked answers (separate page)</a></p>
{qs}'''.replace('__NAV__', nav('project2.html'))
    qs = qs.replace('{{', '{').replace('}}', '}').replace('{prep}', prep)
    body = body.replace('{qs}', qs)
    (OUT / 'project2.html').write_text(page('DPEN100 Project 2 — Questions', body))


def build_project2_answers():
    body = r'''
<div class="eyebrow">DPEN100 · ENGG100 · Engineering Analysis</div>
<span class="tag">PROJECT 2 · ANSWERS</span>
<h1>Project 2 — Full worked answers</h1>
<p class="sub">Complete analytic working and MATLAB. Attempt the project before reading.</p>
__NAV__

<div class="ans"><h3>Part A — Shortest time &amp; plots</h3>
<p><strong>Distance to reach \(v_{\max}=20\):</strong>
\[s_a=\frac{v^2}{2a}=\frac{400}{4}=100\,\mathrm{m},\quad t_a=\frac{v}{a}=10\,\mathrm{s}.\]
<strong>Braking distance:</strong>
\[s_b=\frac{v^2}{2|a|}=\frac{400}{8}=50\,\mathrm{m},\quad t_b=\frac{20}{4}=5\,\mathrm{s}.\]
<strong>Cruise:</strong> \(s_c=900-100-50=750\,\mathrm{m}\), \(t_c=750/20=37.5\,\mathrm{s}\).</p>
\[t_{\mathrm{tot}}=10+37.5+5=52.5\,\mathrm{s}.\]
\[\boxed{t_{\mathrm{tot}}=52.5\,\mathrm{s}}\]
<pre>%% proj2_partA.m
a_acc = 2; a_brk = -4; vmax = 20; S = 900; dt = 0.05;
sa = vmax^2/(2*a_acc); sb = vmax^2/(2*abs(a_brk));
sc = S - sa - sb;
ta = vmax/a_acc; tb = vmax/abs(a_brk); tc = sc/vmax;

% Phase 1: accel
t1 = 0:dt:ta;
v1 = a_acc*t1; s1 = 0.5*a_acc*t1.^2;
% Phase 2: cruise
t2 = (t1(end)+dt):dt:(t1(end)+tc);
v2 = vmax*ones(size(t2));
s2 = s1(end) + vmax*(t2 - t1(end));
% Phase 3: brake
t3 = (t2(end)+dt):dt:(t2(end)+tb);
v3 = vmax + a_brk*(t3 - t2(end));
s3 = s2(end) + vmax*(t3 - t2(end)) + 0.5*a_brk*(t3 - t2(end)).^2;

t = [t1 t2 t3]; v = [v1 v2 v3]; s = [s1 s2 s3];
a = [a_acc*ones(size(t1)), zeros(size(t2)), a_brk*ones(size(t3))];

figure(1)
subplot(3,1,1); plot(t,s,'LineWidth',1.5); grid on
ylabel('s (m)'); title('Van motion'); xlim([0 t(end)])
subplot(3,1,2); plot(t,v,'LineWidth',1.5); grid on; ylabel('v (m/s)')
subplot(3,1,3); plot(t,a,'LineWidth',1.5); grid on
xlabel('t (s)'); ylabel('a (m/s^2)')
fprintf('Total time = %.2f s, final s = %.2f m\n', t(end), s(end));</pre>
</div>

<div class="ans"><h3>Part B — Package projectile</h3>
<p>Van velocity at release: \(\mathbf{v}_{\mathrm{van}}=20\,\mathbf{i}\) m/s.
Relative toss (rearward &amp; up): magnitude \(8\,\mathrm{m/s}\) at \(35^\circ\), rearward means negative \(x\):</p>
\[
v_{\mathrm{rel},x}=-8\cos 35^\circ,\qquad v_{\mathrm{rel},y}=8\sin 35^\circ.
\]
\[
v_{0x}=20-8\cos 35^\circ\approx 13.45\,\mathrm{m/s},\qquad
v_{0y}=8\sin 35^\circ\approx 4.59\,\mathrm{m/s}.
\]
Flight from \(y_0=1.6\):
\[0=1.6 + v_{0y}t - \tfrac12 g t^2\]
\[4.905 t^2 - 4.59 t - 1.6 = 0 \Rightarrow t\approx 1.206\,\mathrm{s}\]
(positive root). Landing:
\[x_{\mathrm{land}}=v_{0x} t\approx 16.22\,\mathrm{m}.\]
<pre>%% proj2_partB.m
g = 9.81; y0 = 1.6;
v0x = 20 - 8*cosd(35);
v0y = 8*sind(35);
% solve 0.5*g*t^2 - v0y*t - y0 = 0
T = (v0y + sqrt(v0y^2 + 2*g*y0))/g;
t = linspace(0, T, 250);
x = v0x*t;
y = y0 + v0y*t - 0.5*g*t.^2;

figure(2)
plot(x, y, 'LineWidth', 2); grid on; hold on
plot(x(end), 0, 'ko', 'MarkerFaceColor', 'k')
xlabel('x from release (m)'); ylabel('y (m)')
title('Package trajectory (ground frame)')
fprintf('v0x=%.2f, v0y=%.2f, T=%.3f s, x_land=%.2f m\n', v0x, v0y, T, x(end));</pre>
\[\boxed{v_{0x}\approx 13.45\,\mathrm{m/s},\ v_{0y}\approx 4.59\,\mathrm{m/s},\ T\approx 1.21\,\mathrm{s},\ x_{\mathrm{land}}\approx 16.2\,\mathrm{m}}\]
</div>

<div class="ans"><h3>Part C — Cable components</h3>
\[T=2500\,\mathrm{N},\ \alpha=25^\circ\]
\[T_x=T\cos 25^\circ\approx 2265.8\,\mathrm{N},\qquad T_y=T\sin 25^\circ\approx 1056.5\,\mathrm{N}.\]
<pre>%% proj2_partC.m
T = 2500; a = 25;
Tx = T*cosd(a); Ty = T*sind(a);
figure(3)
quiver(0,0, Tx, Ty, 0, 'LineWidth', 2, 'MaxHeadSize', 0.4); hold on
plot(0,0,'ko','MarkerFaceColor','k')
axis equal; grid on
xlabel('F_x (N)'); ylabel('F_y (N)')
title('Cable tension components')
text(Tx*0.5, Ty*0.5, sprintf('T = 2.5 kN at 25^\\circ'), 'FontSize', 11)
fprintf('Tx = %.1f N, Ty = %.1f N\n', Tx, Ty);</pre>
\[\boxed{T_x\approx 2.27\,\mathrm{kN},\ T_y\approx 1.06\,\mathrm{kN}}\]
</div>

<div class="ans"><h3>Part D — Discussion</h3>
<p><strong>(a)</strong> Lower \(v_{\max}\) means a taller fraction of the \(900\,\mathrm{m}\) must be covered at a smaller cruise speed, and the triangular accel/brake ends change.
Overall the area under \(v\)–\(t\) must still equal \(900\,\mathrm{m}\), so the base (time) must grow → <strong>trip time increases</strong>.
Rough check: \(s_a=v^2/4\), \(s_b=v^2/8\) shrink, but cruise at \(15\,\mathrm{m/s}\) over a longer \(s_c\) dominates.</p>
<p><strong>(b)</strong> Absolute velocity is the vector sum \(\mathbf{v}_{\mathrm{pkg}}=\mathbf{v}_{\mathrm{van}}+\mathbf{v}_{\mathrm{rel}}\).
A rearward relative component subtracts from the van’s forward speed, so \(v_{0x}&lt;20\,\mathrm{m/s}\). That shortens the downrange landing distance versus tossing forward.</p>
</div>'''.replace('__NAV__', nav('project2-answers.html'))
    (OUT / 'project2-answers.html').write_text(page('DPEN100 Project 2 — Answers', body))


def build_hub():
    body = r'''
<div class="eyebrow">DPEN100 · ENGG100</div>
<span class="tag">ENGINEERING ANALYSIS PROJECTS</span>
<h1>Kinematic analysis projects</h1>
<p class="sub">Engineering Analysis in this subject means using MATLAB to analyse rectilinear and curvilinear motion — calculating and plotting position, velocity, acceleration and related forces.
These two projects practise that skill with full worked answers on separate pages.</p>
__NAV__

<div class="card" style="border-color:#93c5fd;background:#eef6ff">
<h3>Before you start — GitHub (Windows)</h3>
<p><strong>Siddharth:</strong> create a GitHub account with <strong>your Gmail</strong>, then make a repo for your MATLAB scripts and push from Windows (GitHub Desktop is easiest).</p>
<div class="chiprow">
  <a class="chip on" href="../github-setup.html">Open GitHub setup guide</a>
  <a class="chip pdf" href="https://www.youtube.com/watch?v=8Dd7KRpKeaE" target="_blank" rel="noopener">▶ Video walkthrough</a>
</div>
</div>

<div class="card">
<h3>What “Engineering Analysis” covers here</h3>
<ul style="margin-left:18px">
<li><strong>Physics prep:</strong> SUVAT / rectilinear motion; projectile (curvilinear) motion; resolving forces with \(\sin/\cos\).</li>
<li><strong>MATLAB prep:</strong> <code>plot</code> / labels / legends; vectorisation (<code>diff</code>, array arithmetic) for many samples at once.</li>
<li><strong>Course project flavour:</strong> kinematic plots &amp; analysis similar to the ENGG100 major project (GPS/ride style reporting).</li>
</ul>
<p class="meta">Handbook focus: <a href="https://courses.uow.edu.au/subjects/2027/engg100" target="_blank" rel="noopener">UOW ENGG100</a> · Onramp: <a href="https://matlabacademy.mathworks.com/" target="_blank" rel="noopener">MathWorks MATLAB Onramp</a></p>
</div>

<div class="card">
<h3>Project 1 — Kinematic plots &amp; analysis (ride + projectile)</h3>
<p class="meta">Major-project style · synthetic GPS segment · curvilinear challenge</p>
<p>Build 3-D path, elevation/grade, cumulative distance and speed plots from coordinate samples, then analyse a drone projectile with vectorised MATLAB.</p>
<div class="chiprow">
  <a class="chip on" href="project1.html">Open Project 1</a>
  <a class="chip ans" href="project1-answers.html">Full worked answers</a>
  <a class="chip pdf" href="pdfs/engg100-major-project-group-p314-kinematic-plots-and-analysis.pdf" target="_blank" rel="noopener">Sample major project PDF</a>
</div>
</div>

<div class="card">
<h3>Project 2 — Van logistics (rectilinear + projectile + forces)</h3>
<p class="meta">Second project · piecewise vehicle motion · package toss · cable components</p>
<p>Design a minimum-time accel/cruise/brake profile, simulate a package tossed from the moving van, and resolve a tow-cable force — all plotted in MATLAB.</p>
<div class="chiprow">
  <a class="chip on" href="project2.html">Open Project 2</a>
  <a class="chip ans" href="project2-answers.html">Full worked answers</a>
</div>
</div>

<div class="note">Work Project 1 first if you are preparing for the major kinematic-plots assignment; use Project 2 to stretch into coupled vehicle + projectile + force analysis.</div>'''.replace('__NAV__', nav('index.html'))
    (OUT / 'index.html').write_text(page('DPEN100 Engineering Analysis Projects', body))


def ensure_pdf():
    pdf_dir = OUT / 'pdfs'
    pdf_dir.mkdir(parents=True, exist_ok=True)
    src = STUDY / 'engg100-major-project-group-p314-kinematic-plots-and-analysis.pdf'
    if src.exists():
        shutil.copy2(src, pdf_dir / src.name)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    ensure_pdf()
    build_project1()
    build_project1_answers()
    build_project2()
    build_project2_answers()
    build_hub()
    print('wrote projects to', OUT)


if __name__ == '__main__':
    main()
