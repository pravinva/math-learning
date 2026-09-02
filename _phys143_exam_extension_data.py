"""Exam-style extension questions for PHYS143 weeks 1-13."""

EXTENSION = {
    1: [
        {
            "topic": '§0 Charge & Coulomb',
            "problem": 'A mining survey drone carries a payload with net charge $+2.4\\,\\mu\\text{C}$. A second payload $18\\,\\text{cm}$ away has charge $-5.1\\,\\mu\\text{C}$. Find the magnitude of the electrostatic force between them and state whether the force is attractive or repulsive.',
            "solution": '<p class="step">Use Coulomb\'s law: $F = k|q_1 q_2|/r^2$ with $k = 8.99\\times 10^9\\,\\text{N\\,m}^2\\text{C}^{-2}$.</p><p class="step">$r = 0.18\\,\\text{m}$, $q_1 = 2.4\\times 10^{-6}\\,\\text{C}$, $q_2 = -5.1\\times 10^{-6}\\,\\text{C}$.</p><p class="step">$F = (8.99\\times 10^9)(2.4\\times 10^{-6})(5.1\\times 10^{-6})/(0.18)^2 = 3.4\\,\\text{N}$.</p><p class="step">Opposite signs $\\Rightarrow$ attractive. Sanity check: a few newtons over centimetre-scale separations is typical for microcoulomb charges.</p><p><strong>$F \\approx 3.4\\,\\text{N}$, attractive.</strong></p>',
        },
        {
            "topic": '§0 Charge & Coulomb',
            "problem": 'Three identical aluminium spheres $A$, $B$, $C$ are initially uncharged. $A$ is touched to $+8.0\\,\\mu\\text{C}$, then $A$ touches $B$, then $B$ touches $C$. What is the final charge on each sphere?',
            "solution": '<p class="step">Charge is shared equally when identical conductors touch.</p><p class="step">After $A$ acquires $+8.0\\,\\mu\\text{C}$, $A$–$B$ touch: each has $+4.0\\,\\mu\\text{C}$.</p><p class="step">$B$–$C$ touch: $+4.0\\,\\mu\\text{C}$ splits between $B$ and $C$, each $+2.0\\,\\mu\\text{C}$.</p><p class="step">Final: $q_A = +4.0\\,\\mu\\text{C}$, $q_B = +2.0\\,\\mu\\text{C}$, $q_C = +2.0\\,\\mu\\text{C}$. Total charge conserved at $+8.0\\,\\mu\\text{C}$.</p><p><strong>$q_A=+4.0\\,\\mu\\text{C}$, $q_B=+2.0\\,\\mu\\text{C}$, $q_C=+2.0\\,\\mu\\text{C}$.</strong></p>',
        },
        {
            "topic": '§0 Charge & Coulomb',
            "problem": 'Two protons in a particle accelerator are separated by $2.0\\,\\text{nm}$. Compare the electrostatic repulsion to their weight ($m_p g$). Which dominates, and why does the beam still need magnetic focusing?',
            "solution": '<p class="step">Electrostatic: $F_e = k e^2/r^2 = (8.99\\times 10^9)(1.6\\times 10^{-19})^2/(2.0\\times 10^{-9})^2 \\approx 5.8\\times 10^{-11}\\,\\text{N}$.</p><p class="step">Weight: $F_g = m_p g = (1.67\\times 10^{-27})(9.8) \\approx 1.6\\times 10^{-26}\\,\\text{N}$.</p><p class="step">Ratio $F_e/F_g \\sim 10^{15}$: electrostatic repulsion utterly dominates gravity.</p><p class="step">Magnetic focusing is still needed because thousands of protons in a bunch exert enormous collective electric repulsion; magnets provide centripetal force without adding net electrostatic energy to the beam.</p><p><strong>Electrostatic force exceeds weight by $\\sim 10^{15}$; magnetic focusing counters collective repulsion in the bunch.</strong></p>',
        },
        {
            "topic": '§0 Charge & Coulomb',
            "problem": 'Explain why we can treat macroscopic charge as continuous even though charge is quantised in units of $e$. A wire carries $1.0\\,\\text{A}$ for $1.0\\,\\mu\\text{s}$ — approximately how many electrons pass a cross-section?',
            "solution": '<p class="step">Quantisation matters only when $Q \\sim e$. Here $Q = It = 10^{-6}\\,\\text{C}$.</p><p class="step">$N = Q/e = 10^{-6}/(1.6\\times 10^{-19}) \\approx 6.3\\times 10^{12}$ electrons.</p><p class="step">This is $\\gg 1$, so fractional-electron fluctuations are negligible and a continuous model is valid.</p><p><strong>$\\approx 6\\times 10^{12}$ electrons; continuous approximation is excellent.</strong></p>',
        },
        {
            "topic": '§1 Point Charge Fields',
            "problem": 'Charges $+6.0\\,\\mu\\text{C}$ and $+2.0\\,\\mu\\text{C}$ lie on the $x$-axis at $x=0$ and $x=0.40\\,\\text{m}$. Where (if anywhere) on the axis between them is the net electric field zero?',
            "solution": '<p class="step">Let the zero-field point be at distance $x$ from $+6.0\\,\\mu\\text{C}$ ($0 < x < 0.40\\,\\text{m}$).</p><p class="step">Fields oppose between like charges: $k(6.0\\times 10^{-6})/x^2 = k(2.0\\times 10^{-6})/(0.40-x)^2$.</p><p class="step">Cross-multiply: $6/(0.40-x)^2 = 2/x^2 \\Rightarrow \\sqrt{3}x = 0.40-x$.</p><p class="step">$x(1+\\sqrt{3}) = 0.40 \\Rightarrow x = 0.40/(1+\\sqrt{3}) = 0.146\\,\\text{m}$ from the larger charge.</p><p class="step">Sanity: closer to the smaller charge, as expected.</p><p><strong>$x = 0.15\\,\\text{m}$ from the $+6.0\\,\\mu\\text{C}$ charge (between the charges).</strong></p>',
        },
        {
            "topic": '§1 Point Charge Fields',
            "problem": 'An electric dipole has charges $\\pm 4.0\\,\\mu\\text{C}$ separated by $6.0\\,\\text{cm}$. Find the electric field magnitude at a point on the perpendicular bisector $20\\,\\text{cm}$ from the dipole centre.',
            "solution": '<p class="step">Half-separation $a = 0.030\\,\\text{m}$, distance to point $r = 0.20\\,\\text{m}$, $p = q(2a) = 4.0\\times 10^{-6}\\times 0.060 = 2.4\\times 10^{-7}\\,\\text{C\\,m}$.</p><p class="step">On bisector: $E = \\dfrac{1}{4\\pi\\varepsilon_0}\\dfrac{p}{(r^2+a^2)^{3/2}}$.</p><p class="step">Denominator: $(0.04+0.0009)^{3/2} = (0.0409)^{1.5} \\approx 8.27\\times 10^{-3}$.</p><p class="step">$E = (8.99\\times 10^9)(2.4\\times 10^{-7})/(8.27\\times 10^{-3}) \\approx 26\\,\\text{kN/C}$.</p><p><strong>$E \\approx 2.6\\times 10^4\\,\\text{N/C}$ along the dipole moment direction.</strong></p>',
        },
        {
            "topic": '§1 Point Charge Fields',
            "problem": 'Four point charges are at the corners of a square of side $0.25\\,\\text{m}$: $+3\\,\\mu\\text{C}$, $-3\\,\\mu\\text{C}$, $+3\\,\\mu\\text{C}$, $-3\\,\\mu\\text{C}$ in alternating order. Find the net force on a $+1.0\\,\\mu\\text{C}$ test charge placed at the square centre.',
            "solution": '<p class="step">At the centre, fields from opposite corners are equal in magnitude and parallel (same sign pairings cancel in pairs for force, not field).</p><p class="step">Each corner is $r = 0.25/\\sqrt{2} = 0.177\\,\\text{m}$ away. Field from one $+3\\,\\mu\\text{C}$: $E_+ = kq/r^2 = 8.6\\times 10^5\\,\\text{N/C}$ toward centre.</p><p class="step">By symmetry, net field from $+3$ and $-3$ on one diagonal cancels; same for the other diagonal.</p><p class="step">Net field at centre is zero, so force on test charge is zero.</p><p><strong>Net force $= 0$ (symmetry cancels all contributions).</strong></p>',
        },
        {
            "topic": '§1 Point Charge Fields',
            "problem": 'A $+5.0\\,\\mu\\text{C}$ charge is at the origin. Sketch the direction of $\\vec{E}$ at $(0.30\\,\\text{m},\\,0.40\\,\\text{m})$ and find its magnitude.',
            "solution": '<p class="step">Distance $r = \\sqrt{0.30^2+0.40^2} = 0.50\\,\\text{m}$.</p><p class="step">$E = kq/r^2 = (8.99\\times 10^9)(5.0\\times 10^{-6})/0.25 = 1.80\\times 10^5\\,\\text{N/C}$.</p><p class="step">Direction: radially outward from origin, unit vector $\\hat{r} = (0.30\\hat{i}+0.40\\hat{j})/0.50 = 0.60\\hat{i}+0.80\\hat{j}$.</p><p><strong>$E = 1.8\\times 10^5\\,\\text{N/C}$ at $53^\\circ$ above $+x$.</strong></p>',
        },
        {
            "topic": '§2 Continuous Distributions',
            "problem": 'A thin rod of length $L = 0.80\\,\\text{m}$ lies on the $x$-axis from $x=0$ to $x=L$ with linear charge density $\\lambda(x) = \\lambda_0\\,x/L$ where $\\lambda_0 = 3.0\\,\\mu\\text{C/m}$. Set up (but do not evaluate) the integral for the electric field at point $P$ on the $x$-axis at $x = 2.0\\,\\text{m}$.',
            "solution": '<p class="step">Element at $x\'$ has charge $dq = \\lambda(x\')\\,dx\' = \\lambda_0 (x\'/L)\\,dx\'$.</p><p class="step">Distance from element to $P$: $r = 2.0 - x\'$ (to the right of rod).</p><p class="step">Field contribution: $dE = \\dfrac{1}{4\\pi\\varepsilon_0}\\dfrac{dq}{r^2}$ along $+x$.</p><p class="step">$E = \\dfrac{\\lambda_0}{4\\pi\\varepsilon_0 L}\\int_0^L \\dfrac{x\'}{(2.0-x\')^2}\\,dx\'$.</p><p class="step">Note: integrand blows up if $P$ is inside the rod — here $P$ is outside, so integral is well-defined.</p><p><strong>$E = \\dfrac{\\lambda_0}{4\\pi\\varepsilon_0 L}\\displaystyle\\int_0^L \\dfrac{x\'}{(2.0-x\')^2}\\,dx\'$.</strong></p>',
        },
        {
            "topic": '§2 Continuous Distributions',
            "problem": 'A uniformly charged ring of radius $R = 0.15\\,\\text{m}$ and total charge $Q = 2.0\\,\\mu\\text{C}$ lies in the $xy$-plane centred at the origin. Show that the on-axis field is maximum at $z = R/\\sqrt{2}$ and find that maximum field.',
            "solution": '<p class="step">On axis: $E(z) = \\dfrac{1}{4\\pi\\varepsilon_0}\\dfrac{Qz}{(z^2+R^2)^{3/2}}$.</p><p class="step">Set $dE/dz = 0$: numerator of derivative gives $R^2 - 2z^2 = 0 \\Rightarrow z = R/\\sqrt{2}$.</p><p class="step">At $z = R/\\sqrt{2} = 0.106\\,\\text{m}$: $E_{\\max} = kQ/(R^2\\sqrt{3})\\,(1/\\sqrt{2})^3$... simplifying: $E_{\\max} = \\dfrac{2\\sqrt{3}}{9}\\dfrac{kQ}{R^2}$.</p><p class="step">$E_{\\max} = (2\\sqrt{3}/9)(8.99\\times 10^9)(2.0\\times 10^{-6})/(0.15)^2 \\approx 1.03\\times 10^6\\,\\text{N/C}$.</p><p><strong>Maximum at $z = R/\\sqrt{2} = 0.11\\,\\text{m}$; $E_{\\max} \\approx 1.0\\times 10^6\\,\\text{N/C}$.</strong></p>',
        },
        {
            "topic": '§2 Continuous Distributions',
            "problem": 'A semicircular arc of radius $0.20\\,\\text{m}$ carries uniform line charge $\\lambda = 5.0\\,\\mu\\text{C/m}$. Find the electric field at the centre of curvature (magnitude and direction).',
            "solution": '<p class="step">By symmetry, only the vertical component survives. Element at angle $\\theta$: $dE = k\\,\\lambda\\,d\\ell/r^2 = k\\lambda\\,d\\theta/r$ with $r = 0.20\\,\\text{m}$.</p><p class="step">Vertical component: $dE_y = dE\\sin\\theta$. Integrate $\\theta$ from $0$ to $\\pi$.</p><p class="step">$E = \\dfrac{k\\lambda}{r}\\int_0^\\pi \\sin\\theta\\,d\\theta = \\dfrac{2k\\lambda}{r}$.</p><p class="step">$E = 2(8.99\\times 10^9)(5.0\\times 10^{-6})/(0.20) = 4.5\\times 10^5\\,\\text{N/C}$ downward (toward the arc).</p><p><strong>$E = 4.5\\times 10^5\\,\\text{N/C}$ toward the charged arc.</strong></p>',
        },
        {
            "topic": '§3 Symmetric Distributions',
            "problem": 'Compare qualitatively: which produces a larger field at $1.0\\,\\text{m}$ from its centre — a uniformly charged ring of radius $0.50\\,\\text{m}$ with $Q = 1\\,\\mu\\text{C}$, or a uniformly charged disk of the same radius and charge? Explain without full calculation.',
            "solution": '<p class="step">Ring: all charge is at distance $\\sqrt{1^2+0.5^2} \\approx 1.12\\,\\text{m}$ from on-axis point; field is purely axial.</p><p class="step">Disk: charge nearer the axis is closer than $1.12\\,\\text{m}$, contributing more strongly ($E \\propto 1/r^2$).</p><p class="step">Disk field at $1.0\\,\\text{m}$ on axis exceeds ring field because nearby surface charge dominates.</p><p><strong>The disk produces the larger field; nearer charge elements contribute more strongly.</strong></p>',
        },
        {
            "topic": '§3 Symmetric Distributions',
            "problem": 'An infinite line of charge has $\\lambda = 8.0\\,\\mu\\text{C/m}$. Find $|\\vec{E}|$ at $3.0\\,\\text{cm}$ from the line.',
            "solution": '<p class="step">Cylindrical symmetry: $E = \\lambda/(2\\pi\\varepsilon_0 r) = 2k\\lambda/r$.</p><p class="step">$E = 2(8.99\\times 10^9)(8.0\\times 10^{-6})/(0.030) = 4.8\\times 10^6\\,\\text{N/C}$ radially outward.</p><p class="step">Sanity: very large field close to line — realistic only for finite-length approximations.</p><p><strong>$E = 4.8\\times 10^6\\,\\text{N/C}$ radially outward.</strong></p>',
        },
        {
            "topic": '§3 Symmetric Distributions',
            "problem": 'Two infinite parallel sheets carry $\\sigma_1 = +3.0\\,\\mu\\text{C/m}^2$ and $\\sigma_2 = -5.0\\,\\mu\\text{C/m}^2$, separated by $4.0\\,\\text{cm}$. Find the electric field in the three regions: left of both, between them, and right of both.',
            "solution": '<p class="step">Each sheet: $E = \\sigma/(2\\varepsilon_0)$, directed away from positive sheet.</p><p class="step">Left region: both fields point left: $E = -(3+5)\\,\\mu/(2\\varepsilon_0) = -8\\sigma_0$ equivalent $\\Rightarrow |E| = 4.5\\times 10^5\\,\\text{N/C}$ leftward.</p><p class="step">Between sheets: fields oppose: $|3-5|/(2\\varepsilon_0) = 1.1\\times 10^5\\,\\text{N/C}$ toward the negative sheet.</p><p class="step">Right region: both point right: $8\\,\\mu/(2\\varepsilon_0) = 4.5\\times 10^5\\,\\text{N/C}$ rightward.</p><p><strong>Outer regions: $4.5\\times 10^5\\,\\text{N/C}$; between: $1.1\\times 10^5\\,\\text{N/C}$ toward the negative sheet.</strong></p>',
        },
    ],
    2: [
        {
            "topic": '§0 Capacitance',
            "problem": 'A defibrillator paddle pair forms a parallel-plate capacitor with plate area $A = 120\\,\\text{cm}^2$, separation $d = 0.80\\,\\text{mm}$, and air gap. Find its capacitance.',
            "solution": '<p class="step">Parallel-plate: $C = \\varepsilon_0 A/d$.</p><p class="step">$A = 1.20\\times 10^{-2}\\,\\text{m}^2$, $d = 8.0\\times 10^{-4}\\,\\text{m}$.</p><p class="step">$C = (8.85\\times 10^{-12})(1.20\\times 10^{-2})/(8.0\\times 10^{-4}) = 1.33\\times 10^{-10}\\,\\text{F}$.</p><p class="step">Sanity: picofarad-scale for small air-gap plates is typical.</p><p><strong>$C \\approx 133\\,\\text{pF}$.</strong></p>',
        },
        {
            "topic": '§0 Capacitance',
            "problem": 'Three capacitors $C_1 = 6.0\\,\\mu\\text{F}$, $C_2 = 3.0\\,\\mu\\text{F}$, $C_3 = 9.0\\,\\mu\\text{F}$ are connected in series across $24\\,\\text{V}$. Find the charge on each capacitor and the voltage across $C_2$.',
            "solution": '<p class="step">Series: $1/C_{\\text{eq}} = 1/6 + 1/3 + 1/9 = (3+6+2)/18 = 11/18$.</p><p class="step">$C_{\\text{eq}} = 18/11\\,\\mu\\text{F} \\approx 1.64\\,\\mu\\text{F}$.</p><p class="step">Charge on each (series shares $Q$): $Q = C_{\\text{eq}} V = 1.64\\times 10^{-6}\\times 24 = 3.9\\times 10^{-5}\\,\\text{C}$.</p><p class="step">$V_2 = Q/C_2 = 3.9\\times 10^{-5}/(3.0\\times 10^{-6}) = 13\\,\\text{V}$.</p><p><strong>$Q \\approx 39\\,\\mu\\text{C}$ on each; $V_2 = 13\\,\\text{V}$.</strong></p>',
        },
        {
            "topic": '§0 Capacitance',
            "problem": 'A coaxial cable has inner radius $a = 1.5\\,\\text{mm}$, outer radius $b = 4.5\\,\\text{mm}$, length $L = 2.0\\,\\text{m}$, and air between conductors. Set up the capacitance formula and evaluate it.',
            "solution": '<p class="step">Cylindrical capacitor: $C = 2\\pi\\varepsilon_0 L/\\ln(b/a)$.</p><p class="step">$\\ln(b/a) = \\ln(3) = 1.099$.</p><p class="step">$C = 2\\pi(8.85\\times 10^{-12})(2.0)/1.099 = 1.01\\times 10^{-10}\\,\\text{F}$.</p><p class="step">Trap: use radii, not diameters; air-filled so $\\varepsilon = \\varepsilon_0$.</p><p><strong>$C \\approx 101\\,\\text{pF}$.</strong></p>',
        },
        {
            "topic": '§0 Capacitance',
            "problem": 'Two isolated metal spheres of radii $R_1 = 5.0\\,\\text{cm}$ and $R_2 = 10.0\\,\\text{cm}$ are far apart. They are connected by a wire and charged to total $Q = +12\\,\\mu\\text{C}$. Find the final charge on each sphere.',
            "solution": '<p class="step">Connected conductors share the same potential: $q_1/R_1 = q_2/R_2$ with $q_1+q_2 = Q$.</p><p class="step">$q_1 = Q R_1/(R_1+R_2) = 12\\times 5/(15) = 4.0\\,\\mu\\text{C}$.</p><p class="step">$q_2 = 8.0\\,\\mu\\text{C}$. Smaller sphere holds less charge at equal potential.</p><p><strong>$q_1 = 4.0\\,\\mu\\text{C}$, $q_2 = 8.0\\,\\mu\\text{C}$.</strong></p>',
        },
        {
            "topic": '§1 Dielectrics & Energy',
            "problem": 'A $4.0\\,\\mu\\text{F}$ air-gap capacitor is charged to $200\\,\\text{V}$, then disconnected. A dielectric slab ($\\kappa = 3.0$) is inserted filling half the gap volume (not half the plate area — the slab covers half the area completely). Find the new voltage.',
            "solution": '<p class="step">Initial charge $Q = CV = 4.0\\times 10^{-6}\\times 200 = 8.0\\times 10^{-4}\\,\\text{C}$ (isolated).</p><p class="step">Effective capacitance: half area with dielectric $C_1 = \\kappa\\varepsilon_0 A/(2d)$, half air $C_2 = \\varepsilon_0 A/(2d)$; total $C\' = (C_1+C_2) = \\varepsilon_0 A/d\\,(1+\\kappa)/2$.</p><p class="step">Relative to air $C_0$: $C\' = C_0(1+\\kappa)/2 = 4.0\\times(4/2) = 8.0\\,\\mu\\text{F}$.</p><p class="step">$V\' = Q/C\' = 8.0\\times 10^{-4}/(8.0\\times 10^{-6}) = 100\\,\\text{V}$.</p><p><strong>$V\' = 100\\,\\text{V}$.</strong></p>',
        },
        {
            "topic": '§1 Dielectrics & Energy',
            "problem": 'Energy stored in a parallel-plate capacitor is $U = \\tfrac{1}{2}CV^2$. Show that alternatively $U = Q^2/(2C)$ and use this to find the energy stored when $Q = 50\\,\\mu\\text{C}$ on a $10\\,\\mu\\text{F}$ capacitor.',
            "solution": '<p class="step">From $C = Q/V$: $U = \\tfrac{1}{2}CV^2 = \\tfrac{1}{2}C(Q/C)^2 = Q^2/(2C)$.</p><p class="step">$U = (50\\times 10^{-6})^2/(2\\times 10\\times 10^{-6}) = 2.5\\times 10^{-9}/(2.0\\times 10^{-5}) = 1.25\\times 10^{-4}\\,\\text{J}$.</p><p class="step">Sanity: $125\\,\\mu\\text{J}$ is modest for a small capacitor.</p><p><strong>$U = 1.25\\times 10^{-4}\\,\\text{J}$ ($125\\,\\mu\\text{J}$).</strong></p>',
        },
        {
            "topic": '§1 Dielectrics & Energy',
            "problem": 'A mining-site high-voltage capacitor bank stores $5.0\\,\\text{kJ}$ at $600\\,\\text{V}$. What capacitance is required? If the dielectric fails and capacitance drops by $40\\%$ while charge is trapped, what is the new stored energy?',
            "solution": '<p class="step">$U = \\tfrac{1}{2}CV^2 \\Rightarrow C = 2U/V^2 = 2(5000)/(600)^2 = 2.78\\times 10^{-2}\\,\\text{F}$.</p><p class="step">Charge trapped: $Q = CV = 0.0278\\times 600 = 16.7\\,\\text{C}$.</p><p class="step">New $C\' = 0.60 C$: $U\' = Q^2/(2C\') = Q^2/(2\\times 0.6 C) = U/0.6 = 8.33\\,\\text{kJ}$.</p><p class="step">Trap: energy rises when $C$ falls with fixed $Q$ — dielectric failure is hazardous.</p><p><strong>$C \\approx 28\\,\\text{mF}$; trapped-charge energy rises to $\\approx 8.3\\,\\text{kJ}$.</strong></p>',
        },
        {
            "topic": '§2 Current, Resistance & Ohm',
            "problem": 'Copper wire ($\\rho = 1.7\\times 10^{-8}\\,\\Omega\\,\\text{m}$) has length $L = 15\\,\\text{m}$ and diameter $d = 2.0\\,\\text{mm}$. Find its resistance at $20^\\circ\\text{C}$.',
            "solution": '<p class="step">$A = \\pi(d/2)^2 = \\pi(1.0\\times 10^{-3})^2 = 3.14\\times 10^{-6}\\,\\text{m}^2$.</p><p class="step">$R = \\rho L/A = (1.7\\times 10^{-8})(15)/(3.14\\times 10^{-6}) = 0.081\\,\\Omega$.</p><p class="step">Sanity: low resistance for thick short copper — suitable for power leads.</p><p><strong>$R \\approx 0.08\\,\\Omega$.</strong></p>',
        },
        {
            "topic": '§2 Current, Resistance & Ohm',
            "problem": 'A $12\\,\\text{V}$ car battery delivers $80\\,\\text{A}$ to start an engine. The terminal voltage drops to $10.5\\,\\text{V}$. Find the internal resistance and the power dissipated inside the battery.',
            "solution": '<p class="step">Terminal drop: $Ir = E - V = 12 - 10.5 = 1.5\\,\\text{V}$.</p><p class="step">$r = 1.5/80 = 0.019\\,\\Omega = 19\\,\\text{m}\\Omega$.</p><p class="step">Internal power: $P_r = I^2 r = 80^2\\times 0.019 = 121\\,\\text{W}$.</p><p><strong>$r \\approx 19\\,\\text{m}\\Omega$; internal dissipation $\\approx 121\\,\\text{W}$.</strong></p>',
        },
        {
            "topic": '§2 Current, Resistance & Ohm',
            "problem": 'The current through a non-ohmic device is $I = 0.50\\,V^{1.5}$ (SI units). Find the incremental resistance $dV/dI$ at $V = 4.0\\,\\text{V}$ and the average resistance $V/I$ there.',
            "solution": '<p class="step">At $V = 4$: $I = 0.50\\times 8 = 4.0\\,\\text{A}$.</p><p class="step">Average: $R_{\\text{avg}} = V/I = 1.0\\,\\Omega$.</p><p class="step">From $I = 0.50 V^{1.5}$: $dI/dV = 0.75 V^{0.5}$; at $V=4$: $dI/dV = 1.5\\,\\text{A/V}$.</p><p class="step">Incremental $R = dV/dI = 1/(dI/dV) = 0.67\\,\\Omega$.</p><p><strong>$R_{\\text{avg}} = 1.0\\,\\Omega$; incremental $R \\approx 0.67\\,\\Omega$.</strong></p>',
        },
        {
            "topic": '§2 Current, Resistance & Ohm',
            "problem": 'Explain why the drift velocity of electrons in household wiring ($I \\approx 10\\,\\text{A}$, wire diameter $2\\,\\text{mm}$) is millimetres per second, yet a lamp switches on almost instantly when the circuit is closed.',
            "solution": '<p class="step">Drift speed $v_d = I/(nA e) \\sim 10/(10^{28}\\times 10^{-6}\\times 10^{-19}) \\sim 10^{-3}\\,\\text{m/s}$ — very slow.</p><p class="step">The electric field propagates at nearly the speed of light along the wire, pushing all electrons in the circuit almost simultaneously.</p><p class="step">Current is established by the collective motion of the already-present free electrons, not by electrons travelling from the switch to the bulb.</p><p><strong>Signal propagates at near $c$; drift speed is tiny but all electrons respond collectively.</strong></p>',
        },
        {
            "topic": '§3 Series-Parallel & Power',
            "problem": 'Resistors $R_1 = 12\\,\\Omega$, $R_2 = 18\\,\\Omega$, $R_3 = 6\\,\\Omega$ are in parallel across $36\\,\\text{V}$. Find total current, current through each branch, and total power.',
            "solution": '<p class="step">$1/R_p = 1/12 + 1/18 + 1/6 = (3+2+6)/36 = 11/36$.</p><p class="step">$R_p = 36/11 \\approx 3.27\\,\\Omega$.</p><p class="step">$I_{\\text{tot}} = 36/3.27 = 11.0\\,\\text{A}$.</p><p class="step">$I_1 = 3\\,\\text{A}$, $I_2 = 2\\,\\text{A}$, $I_3 = 6\\,\\text{A}$.</p><p class="step">$P = V^2/R_p = 36^2/(3.27) \\approx 396\\,\\text{W}$.</p><p><strong>$I_{\\text{tot}} \\approx 11\\,\\text{A}$; $P \\approx 396\\,\\text{W}$.</strong></p>',
        },
        {
            "topic": '§3 Series-Parallel & Power',
            "problem": 'A $240\\,\\text{V}$ electric kettle ($P = 2.2\\,\\text{kW}$) and a $1.1\\,\\text{kW}$ toaster run simultaneously from the same outlet. What is the combined current? If the household circuit breaker is rated $16\\,\\text{A}$, will it trip?',
            "solution": '<p class="step">$I_{\\text{kettle}} = 2200/240 = 9.17\\,\\text{A}$; $I_{\\text{toaster}} = 1100/240 = 4.58\\,\\text{A}$.</p><p class="step">Combined $I = 13.75\\,\\text{A} < 16\\,\\text{A}$ — breaker should not trip.</p><p class="step">Trap: assuming series connection would be wrong; appliances are in parallel across mains.</p><p><strong>Combined current $\\approx 13.8\\,\\text{A}$; breaker holds.</strong></p>',
        },
        {
            "topic": '§3 Series-Parallel & Power',
            "problem": "Using Kirchhoff's voltage law only (no full mesh analysis), find the voltage across the $8\\,\\Omega$ resistor in a single-loop circuit: $12\\,\\text{V}$ source, $4\\,\\Omega$ and $8\\,\\Omega$ in series.",
            "solution": '<p class="step">Series: same current $I = 12/(4+8) = 1.0\\,\\text{A}$.</p><p class="step">$V_8 = IR = 1.0\\times 8 = 8\\,\\text{V}$.</p><p class="step">KVL check: $4 + 8 = 12\\,\\text{V}$ around loop.</p><p><strong>$V_{8\\Omega} = 8\\,\\text{V}$.</strong></p>',
        },
    ],
    3: [
        {
            "topic": "§0 Kirchhoff's Laws",
            "problem": 'In the circuit: $10\\,\\text{V}$ source, $R_1 = 5\\,\\Omega$ in series with parallel pair $R_2 = 20\\,\\Omega$ and $R_3 = 30\\,\\Omega$. Find the current from the source and the voltage across $R_3$.',
            "solution": '<p class="step">Parallel: $R_{23} = (20\\times 30)/(50) = 12\\,\\Omega$.</p><p class="step">Total $R = 5 + 12 = 17\\,\\Omega$; $I_s = 10/17 = 0.588\\,\\text{A}$.</p><p class="step">$V_{23} = IR_{23} = 0.588\\times 12 = 7.06\\,\\text{V}$ (same across $R_3$).</p><p><strong>$I_s \\approx 0.59\\,\\text{A}$; $V_3 \\approx 7.1\\,\\text{V}$.</strong></p>',
        },
        {
            "topic": "§0 Kirchhoff's Laws",
            "problem": 'Two batteries $E_1 = 9\\,\\text{V}$ ($r_1 = 0.5\\,\\Omega$) and $E_2 = 3\\,\\text{V}$ ($r_2 = 0.5\\,\\Omega$) are connected in parallel across $R = 4\\,\\Omega$. Find the current through $R$ and which battery supplies it.',
            "solution": '<p class="step">Parallel source problem: $V_{\\text{term}} = (E_1/r_1 + E_2/r_2)/(1/r_1 + 1/r_2 + 1/R)$... use loop: $I_1 r_1 + I_R R = E_1$, etc.</p><p class="step">Equivalent: $V_p = (9/0.5 + 3/0.5)/(2/0.5 + 1/4) = (18+6)/(4+0.25) = 24/4.25 = 5.65\\,\\text{V}$.</p><p class="step">$I_R = 5.65/4 = 1.41\\,\\text{A}$ through $R$.</p><p class="step">Higher-voltage battery dominates; $E_1$ supplies most current.</p><p><strong>$I_R \\approx 1.4\\,\\text{A}$; mainly supplied by the $9\\,\\text{V}$ battery.</strong></p>',
        },
        {
            "topic": "§0 Kirchhoff's Laws",
            "problem": "Apply Kirchhoff's junction rule at a node where $I_1 = 3.0\\,\\text{A}$ enters, $I_2 = 1.2\\,\\text{A}$ leaves, and $I_3$ leaves. Find $I_3$. Then state Kirchhoff's loop rule in words and explain why it is a consequence of energy conservation.",
            "solution": '<p class="step">Junction: $\\sum I_{\\text{in}} = \\sum I_{\\text{out}}$: $3.0 = 1.2 + I_3 \\Rightarrow I_3 = 1.8\\,\\text{A}$.</p><p class="step">Loop rule: sum of voltage rises and drops around any closed loop is zero.</p><p class="step">Work per charge ($\\oint \\vec{E}\\cdot d\\vec{l} = 0$ in steady state) means no net energy gain per cycle — conservative path in resistive steady current.</p><p><strong>$I_3 = 1.8\\,\\text{A}$; loop rule = zero net voltage per closed loop (energy conservation).</strong></p>',
        },
        {
            "topic": "§0 Kirchhoff's Laws",
            "problem": 'A Wheatstone bridge has $R_1 = 100\\,\\Omega$, $R_2 = 200\\,\\Omega$, $R_3 = 150\\,\\Omega$, and unknown $R_4$. The galvanometer reads zero. Find $R_4$ and explain the balance condition.',
            "solution": '<p class="step">Balance: $R_1/R_2 = R_3/R_4 \\Rightarrow R_4 = R_3 R_2/R_1 = 150\\times 200/100 = 300\\,\\Omega$.</p><p class="step">At balance, potential at both galvanometer nodes is equal — no current through G.</p><p class="step">Ratios of adjacent arm resistances must match.</p><p><strong>$R_4 = 300\\,\\Omega$; arm ratios equal at balance.</strong></p>',
        },
        {
            "topic": '§1 Magnetic Force',
            "problem": 'A proton ($m = 1.67\\times 10^{-27}\\,\\text{kg}$, $q = 1.6\\times 10^{-19}\\,\\text{C}$) moves at $2.0\\times 10^6\\,\\text{m/s}$ perpendicular to $\\vec{B} = 0.40\\,\\text{T}$. Find the magnetic force magnitude and the radius of its circular path.',
            "solution": '<p class="step">$F = |q|vB = (1.6\\times 10^{-19})(2.0\\times 10^6)(0.40) = 1.28\\times 10^{-13}\\,\\text{N}$.</p><p class="step">Centripetal: $qvB = mv^2/r \\Rightarrow r = mv/(qB)$.</p><p class="step">$r = (1.67\\times 10^{-27})(2.0\\times 10^6)/((1.6\\times 10^{-19})(0.40)) = 0.052\\,\\text{m}$.</p><p><strong>$F = 1.3\\times 10^{-13}\\,\\text{N}$; $r \\approx 5.2\\,\\text{cm}$.</strong></p>',
        },
        {
            "topic": '§1 Magnetic Force',
            "problem": 'An electron travels east at $3.0\\times 10^7\\,\\text{m/s}$ in a region where $\\vec{B}$ points vertically upward. State the direction of the magnetic force (use right-hand rule) and whether the path curves north, south, up, or down.',
            "solution": '<p class="step">Force on negative charge: opposite to $\\vec{v}\\times\\vec{B}$.</p><p class="step">$\\hat{v}\\times\\hat{B}$ (east $\\times$ up) = south (into page convention for N).</p><p class="step">Electron: force toward north.</p><p class="step">Force is horizontal — path curves northward in the horizontal plane, not vertically.</p><p><strong>Force toward north; horizontal circular curvature (not vertical).</strong></p>',
        },
        {
            "topic": '§1 Magnetic Force',
            "problem": 'A straight wire of length $L = 0.25\\,\\text{m}$ carries $I = 15\\,\\text{A}$ in a uniform $\\vec{B} = 0.30\\,\\text{T}$ field at $60^\\circ$ to the wire. Find the force on the wire.',
            "solution": '<p class="step">$F = ILB\\sin\\theta = 15\\times 0.25\\times 0.30\\times \\sin 60^\\circ$.</p><p class="step">$F = 1.125\\times 0.866 = 0.97\\,\\text{N}$.</p><p class="step">Trap: use $\\sin\\theta$ between $\\vec{I}$ and $\\vec{B}$, not the complement.</p><p><strong>$F \\approx 0.97\\,\\text{N}$.</strong></p>',
        },
        {
            "topic": '§1 Magnetic Force',
            "problem": 'Compare the magnitudes of electric and magnetic forces on a $1.0\\,\\mu\\text{C}$ charge moving at $10^6\\,\\text{m/s}$ where $E = 10^3\\,\\text{V/m}$ and $B = 0.50\\,\\text{T}$, with $\\vec{v}$ perpendicular to both fields. Which dominates?',
            "solution": '<p class="step">$F_E = qE = 10^{-6}\\times 10^3 = 10^{-3}\\,\\text{N}$.</p><p class="step">$F_B = qvB = 10^{-6}\\times 10^6\\times 0.50 = 0.50\\,\\text{N}$.</p><p class="step">Magnetic force is $500\\times$ larger here — typical in strong $B$ fields at high speed.</p><p><strong>$F_E = 1\\,\\text{mN}$; $F_B = 0.5\\,\\text{N}$; magnetic dominates.</strong></p>',
        },
        {
            "topic": '§2 Biot-Savart Law',
            "problem": 'A long straight wire carries $I = 8.0\\,\\text{A}$. Find $|\\vec{B}|$ at distance $r = 5.0\\,\\text{cm}$ and state its direction for a point directly above the wire (current toward north).',
            "solution": '<p class="step">$B = \\mu_0 I/(2\\pi r) = (4\\pi\\times 10^{-7})(8.0)/(2\\pi\\times 0.050)$.</p><p class="step">$B = (1.6\\times 10^{-6})/(0.10) = 1.6\\times 10^{-5}\\,\\text{T} = 16\\,\\mu\\text{T}$.</p><p class="step">Right-hand rule: current north, point above $\\Rightarrow$ field points west.</p><p><strong>$B = 16\\,\\mu\\text{T}$, directed west.</strong></p>',
        },
        {
            "topic": '§2 Biot-Savart Law',
            "problem": 'A circular loop of radius $R = 0.10\\,\\text{m}$ carries $I = 5.0\\,\\text{A}$. Find the magnetic field at the centre and at a point on the axis $0.10\\,\\text{m}$ from the plane of the loop.',
            "solution": '<p class="step">Centre: $B_c = \\mu_0 I/(2R) = (4\\pi\\times 10^{-7})(5.0)/(0.20) = 3.14\\times 10^{-5}\\,\\text{T}$.</p><p class="step">On axis at $z = R$: $B = \\mu_0 I R^2/(2(R^2+z^2)^{3/2}) = B_c/2^{3/2} = 3.14\\times 10^{-5}/2.83 = 1.11\\times 10^{-5}\\,\\text{T}$.</p><p><strong>$B_{\\text{centre}} \\approx 31\\,\\mu\\text{T}$; on axis at $z=R$: $\\approx 11\\,\\mu\\text{T}$.</strong></p>',
        },
        {
            "topic": '§2 Biot-Savart Law',
            "problem": 'Two long parallel wires separated by $d = 0.20\\,\\text{m}$ each carry $I = 12\\,\\text{A}$ in opposite directions. Find the magnetic force per unit length on one wire (magnitude and whether attractive or repulsive).',
            "solution": '<p class="step">Field from one wire at the other: $B = \\mu_0 I/(2\\pi d) = (2\\times 10^{-7})(12)/(0.20) = 1.2\\times 10^{-5}\\,\\text{T}$.</p><p class="step">$F/L = IB = 12\\times 1.2\\times 10^{-5} = 1.44\\times 10^{-4}\\,\\text{N/m}$.</p><p class="step">Opposite currents repel.</p><p><strong>$F/L \\approx 1.4\\times 10^{-4}\\,\\text{N/m}$, repulsive.</strong></p>',
        },
        {
            "topic": '§3 Drude Model',
            "problem": 'In the Drude model, electron drift speed is $v_d = eE\\tau/m$. For copper ($n = 8.5\\times 10^{28}\\,\\text{m}^{-3}$), $\\tau = 2.5\\times 10^{-14}\\,\\text{s}$, find $v_d$ when $E = 0.10\\,\\text{V/m}$.',
            "solution": '<p class="step">$v_d = eE\\tau/m = (1.6\\times 10^{-19})(0.10)(2.5\\times 10^{-14})/(9.1\\times 10^{-31})$.</p><p class="step">$v_d = 4.0\\times 10^{-35}/(9.1\\times 10^{-31}) = 4.4\\times 10^{-5}\\,\\text{m/s}$.</p><p class="step">Sanity: drift speeds are tiny — confirms collective conduction picture.</p><p><strong>$v_d \\approx 4.4\\times 10^{-5}\\,\\text{m/s}$.</strong></p>',
        },
        {
            "topic": '§3 Drude Model',
            "problem": 'Derive the Drude expression for resistivity $\\rho = m/(ne^2\\tau)$ and estimate $\\rho$ for silver with $n = 5.8\\times 10^{28}\\,\\text{m}^{-3}$, $\\tau = 3.0\\times 10^{-14}\\,\\text{s}$. Compare to the measured value $1.6\\times 10^{-8}\\,\\Omega\\,\\text{m}$.',
            "solution": '<p class="step">From $J = ne v_d = ne^2 E\\tau/m$ and $J = E/\\rho$: $\\rho = m/(ne^2\\tau)$.</p><p class="step">$\\rho = (9.1\\times 10^{-31})/((5.8\\times 10^{28})(1.6\\times 10^{-19})^2(3.0\\times 10^{-14}))$.</p><p class="step">$\\rho \\approx 1.7\\times 10^{-8}\\,\\Omega\\,\\text{m}$ — agrees with measurement within a few per cent.</p><p><strong>$\\rho_{\\text{calc}} \\approx 1.7\\times 10^{-8}\\,\\Omega\\,\\text{m}$, matching experiment.</strong></p>',
        },
        {
            "topic": '§3 Drude Model',
            "problem": 'Copper wire ($\\rho_0 = 1.7\\times 10^{-8}\\,\\Omega\\,\\text{m}$ at $20^\\circ\\text{C}$) has temperature coefficient $\\alpha = 3.9\\times 10^{-3}\\,\\text{K}^{-1}$. A $10\\,\\text{m}$ segment at $20^\\circ\\text{C}$ has $R = 0.10\\,\\Omega$. Find $R$ when the wire heats to $80^\\circ\\text{C}$ in a fault condition.',
            "solution": '<p class="step">$R(T) = R_0[1 + \\alpha(T - T_0)]$ with $\\Delta T = 60\\,\\text{K}$.</p><p class="step">$R = 0.10[1 + 3.9\\times 10^{-3}\\times 60] = 0.10\\times 1.234 = 0.123\\,\\Omega$.</p><p class="step">Trap: resistivity and resistance both rise — current limiters must account for thermal runaway in short circuits.</p><p><strong>$R \\approx 0.123\\,\\Omega$ at $80^\\circ\\text{C}$.</strong></p>',
        },
    ],
    4: [
        {
            "topic": "§0 Faraday's Law",
            "problem": 'A coil of $N = 200$ turns and area $A = 0.040\\,\\text{m}^2$ is in a uniform field that decreases from $B_0 = 0.50\\,\\text{T}$ to zero in $\\Delta t = 0.020\\,\\text{s}$. Find the magnitude of the induced EMF.',
            "solution": '<p class="step">$\\varepsilon = -N\\,\\Delta\\Phi/\\Delta t = N A \\Delta B/\\Delta t$ (magnitude).</p><p class="step">$\\varepsilon = 200\\times 0.040\\times 0.50/0.020 = 200\\,\\text{V}$.</p><p class="step">Large EMF from rapid flux change — basis of inductive kick.</p><p><strong>$|\\varepsilon| = 200\\,\\text{V}$.</strong></p>',
        },
        {
            "topic": "§0 Faraday's Law",
            "problem": 'A metal rod of length $L = 0.80\\,\\text{m}$ moves at $v = 3.0\\,\\text{m/s}$ perpendicular to $\\vec{B} = 0.25\\,\\text{T}$. Find the motional EMF between the rod ends and which end is at higher potential if the motion is upward in a field pointing east.',
            "solution": '<p class="step">$\\varepsilon = BLv = 0.25\\times 0.80\\times 3.0 = 0.60\\,\\text{V}$.</p><p class="step">$\\vec{v}\\times\\vec{B}$: up $\\times$ east = south $\\Rightarrow$ higher potential at south end of rod.</p><p><strong>$\\varepsilon = 0.60\\,\\text{V}$; south end higher potential.</strong></p>',
        },
        {
            "topic": "§0 Faraday's Law",
            "problem": 'A square loop ($0.20\\,\\text{m}$ side) rotates at $60\\,\\text{rad/s}$ in $B = 0.15\\,\\text{T}$. Find the maximum induced EMF.',
            "solution": '<p class="step">Flux $\\Phi = BA\\cos\\omega t$; $\\varepsilon = -d\\Phi/dt = BA\\omega\\sin\\omega t$.</p><p class="step">$A = 0.04\\,\\text{m}^2$; $\\varepsilon_{\\max} = BA\\omega = 0.15\\times 0.04\\times 60 = 0.36\\,\\text{V}$.</p><p><strong>$\\varepsilon_{\\max} = 0.36\\,\\text{V}$.</strong></p>',
        },
        {
            "topic": "§0 Faraday's Law",
            "problem": "Explain Lenz's law using energy conservation. A north pole approaches a conducting loop — does the induced current circulate clockwise or anticlockwise when viewed from the approaching pole?",
            "solution": '<p class="step">Induced effects oppose the change causing them — otherwise energy would be created.</p><p class="step">Approaching north pole increases upward flux; induced field must point down to oppose.</p><p class="step">Downward field from loop means current clockwise when viewed from above (from north pole side).</p><p><strong>Clockwise when viewed from the approaching north pole (opposes flux increase).</strong></p>',
        },
        {
            "topic": '§1 Transformers',
            "problem": 'A step-down transformer has $N_p = 1200$, $N_s = 48$, and primary voltage $V_p = 240\\,\\text{V}$. Find $V_s$, and if the secondary delivers $I_s = 25\\,\\text{A}$ to a load, find $I_p$ assuming $100\\%$ efficiency.',
            "solution": '<p class="step">$V_s = V_p N_s/N_p = 240\\times 48/1200 = 9.6\\,\\text{V}$.</p><p class="step">Power balance: $V_p I_p = V_s I_s \\Rightarrow I_p = V_s I_s/V_p = 9.6\\times 25/240 = 1.0\\,\\text{A}$.</p><p><strong>$V_s = 9.6\\,\\text{V}$; $I_p = 1.0\\,\\text{A}$.</strong></p>',
        },
        {
            "topic": '§1 Transformers',
            "problem": 'A transformer is rated $50\\,\\text{Hz}$, $240\\,\\text{V}$ primary, $12\\,\\text{V}$ secondary, $2.0\\,\\text{A}$ secondary full-load current. Find the primary current, turns ratio, and primary impedance if the secondary load is purely resistive.',
            "solution": '<p class="step">$P = V_s I_s = 12\\times 2.0 = 24\\,\\text{W}$; $I_p = P/V_p = 24/240 = 0.10\\,\\text{A}$.</p><p class="step">$N_p/N_s = V_p/V_s = 20$.</p><p class="step">$R_s = V_s/I_s = 6\\,\\Omega$; reflected $Z_p = V_p/I_p = 2400\\,\\Omega = R_s (N_p/N_s)^2$.</p><p><strong>$I_p = 0.10\\,\\text{A}$; ratio $20:1$; $Z_p = 2.4\\,\\text{k}\\Omega$.</strong></p>',
        },
        {
            "topic": '§1 Transformers',
            "problem": 'Why is the core of a power transformer laminated? A solid iron core would have lower hysteresis losses but higher eddy-current losses — explain.',
            "solution": '<p class="step">Laminations slice the core perpendicular to $\\vec{B}$, breaking up large eddy current paths.</p><p class="step">Resistance of each thin sheet is high, suppressing eddy currents ($P_{\\text{eddy}} \\propto$ path area squared).</p><p class="step">Insulating layers between laminations are essential; hysteresis depends on material, not lamination.</p><p><strong>Laminations reduce eddy-current losses by restricting current path cross-section.</strong></p>',
        },
        {
            "topic": '§2 EM Waves & Spectrum',
            "problem": 'An EM wave in vacuum has frequency $f = 900\\,\\text{MHz}$ (mobile phone band). Find wavelength, angular frequency, and the ratio $E/B$ for the wave.',
            "solution": '<p class="step">$\\lambda = c/f = 3.0\\times 10^8/(9.0\\times 10^8) = 0.333\\,\\text{m}$.</p><p class="step">$\\omega = 2\\pi f = 5.65\\times 10^9\\,\\text{rad/s}$.</p><p class="step">$E/B = c = 3.0\\times 10^8\\,\\text{m/s}$ in vacuum.</p><p><strong>$\\lambda = 33\\,\\text{cm}$; $\\omega \\approx 5.7\\times 10^9\\,\\text{rad/s}$; $E/B = c$.</strong></p>',
        },
        {
            "topic": '§2 EM Waves & Spectrum',
            "problem": 'Rank by photon energy: (a) $500\\,\\text{nm}$ visible, (b) $10\\,\\mu\\text{m}$ infrared, (c) $0.10\\,\\text{nm}$ X-ray. Use $E = hf = hc/\\lambda$.',
            "solution": '<p class="step">$E \\propto 1/\\lambda$: shortest wavelength has highest energy.</p><p class="step">(c) X-ray: $E = 1240\\,\\text{eV}\\cdot\\text{nm}/0.10 = 12.4\\,\\text{keV}$.</p><p class="step">(a) Visible: $1240/500 = 2.48\\,\\text{eV}$.</p><p class="step">(b) IR: $1240/10000 = 0.124\\,\\text{eV}$.</p><p class="step">Order: X-ray $>$ visible $>$ IR.</p><p><strong>Energy order: X-ray ($12\\,\\text{keV}$) $>$ visible ($2.5\\,\\text{eV}$) $>$ IR ($0.12\\,\\text{eV}$).</strong></p>',
        },
        {
            "topic": '§2 EM Waves & Spectrum',
            "problem": 'The Poynting vector magnitude is $S = EB/(\\mu_0 c)$. For a radio wave with $E = 0.10\\,\\text{V/m}$, find $S$ and the time-averaged intensity.',
            "solution": '<p class="step">$B = E/c = 0.10/(3.0\\times 10^8) = 3.33\\times 10^{-10}\\,\\text{T}$.</p><p class="step">$S = (0.10)(3.33\\times 10^{-10})/(4\\pi\\times 10^{-7}\\times 3.0\\times 10^8) \\approx 2.65\\times 10^{-5}\\,\\text{W/m}^2$.</p><p class="step">For sinusoidal wave, average intensity $I = S/2$ if peak $E$ given... if $E$ is amplitude: $I = E^2/(2\\mu_0 c) = 1.3\\times 10^{-5}\\,\\text{W/m}^2$.</p><p><strong>$I \\approx 1.3\\times 10^{-5}\\,\\text{W/m}^2$ ($13\\,\\mu\\text{W/m}^2$).</strong></p>',
        },
        {
            "topic": '§2 EM Waves & Spectrum',
            "problem": 'Explain why visible light cannot propagate through a thick steel wall but low-frequency radio waves can penetrate building materials more easily.',
            "solution": '<p class="step">Skin depth $\\delta \\propto 1/\\sqrt{\\mu\\sigma f}$: lower frequency penetrates farther.</p><p class="step">Visible light ($f \\sim 10^{15}\\,\\text{Hz}$) is strongly absorbed/reflected by metals within nanometres.</p><p class="step">Radio ($f \\sim 10^6\\,\\text{Hz}$) has much larger skin depth in conductors and can diffract around obstacles.</p><p><strong>Lower $f$ gives larger skin depth and better diffraction; visible light is strongly attenuated in metals.</strong></p>',
        },
        {
            "topic": '§3 Modulation & Conductors',
            "problem": 'An AM signal has carrier $f_c = 1.0\\,\\text{MHz}$, modulated by a $5\\,\\text{kHz}$ audio tone. What are the frequencies present in the transmitted signal?',
            "solution": '<p class="step">AM produces sidebands: $f_c \\pm f_m$.</p><p class="step">Frequencies: $1.000\\,\\text{MHz}$, $0.995\\,\\text{MHz}$, $1.005\\,\\text{MHz}$ (carrier plus upper and lower sidebands).</p><p class="step">Bandwidth = $2f_m = 10\\,\\text{kHz}$.</p><p><strong>$995\\,\\text{kHz}$, $1.000\\,\\text{MHz}$, $1.005\\,\\text{MHz}$; bandwidth $10\\,\\text{kHz}$.</strong></p>',
        },
        {
            "topic": '§3 Modulation & Conductors',
            "problem": 'Silicon has band gap $E_g = 1.1\\,\\text{eV}$. Can photons of $\\lambda = 800\\,\\text{nm}$ promote electrons across the gap? What minimum wavelength is needed?',
            "solution": '<p class="step">$E_{800} = hc/\\lambda = 1240/800 = 1.55\\,\\text{eV} > 1.1\\,\\text{eV}$ — yes, can excite electrons to conduction band.</p><p class="step">$\\lambda_{\\min} = hc/E_g = 1240/1.1 = 1127\\,\\text{nm}$ (near infrared).</p><p><strong>$800\\,\\text{nm}$ photons can excite (1.55 eV $>$ 1.1 eV); $\\lambda_{\\min} \\approx 1127\\,\\text{nm}$.</strong></p>',
        },
        {
            "topic": '§3 Modulation & Conductors',
            "problem": 'Classify each as conductor, semiconductor, or insulator at room temperature: (i) $\\rho = 10^{-8}\\,\\Omega\\,\\text{m}$, (ii) $\\rho = 10^2\\,\\Omega\\,\\text{m}$, (iii) $\\rho = 10^{14}\\,\\Omega\\,\\text{m}$. Explain using the band model.',
            "solution": '<p class="step">(i) $\\rho \\sim 10^{-8}$: conductor — partially filled conduction band (metals).</p><p class="step">(ii) $\\rho \\sim 10^2$: semiconductor — small band gap, thermally/photo excited carriers.</p><p class="step">(iii) $\\rho \\sim 10^{14}$: insulator — large band gap, negligible intrinsic carriers at 300 K.</p><p><strong>(i) conductor; (ii) semiconductor; (iii) insulator.</strong></p>',
        },
    ],
    5: [
        {
            "topic": '§0 Week 1 Recap',
            "problem": 'Two charges $+q$ and $-3q$ are separated by $d$. Where on the line joining them (outside the pair) is the electric field zero?',
            "solution": '<p class="step">Let zero point be beyond $-3q$ at distance $x$ from it: $kq/x^2 = k(3q)/(d+x)^2$.</p><p class="step">$1/x^2 = 3/(d+x)^2 \\Rightarrow (d+x)/x = \\sqrt{3}$.</p><p class="step">$x = d/(\\sqrt{3}-1) = d(\\sqrt{3}+1)/2 \\approx 1.37d$ from $-3q$, on the far side.</p><p class="step">Trap: no zero between opposite charges (fields same direction).</p><p><strong>$x = d(\\sqrt{3}+1)/2 \\approx 1.37d$ beyond the $-3q$ charge.</strong></p>',
        },
        {
            "topic": '§0 Week 1 Recap',
            "problem": 'A uniformly charged sphere of radius $R$ and total charge $Q$ — find $|\\vec{E}|$ at $r = 2R$ and explain why a point outside cannot distinguish sphere from point charge.',
            "solution": '<p class="step">Outside ($r > R$): $E = kQ/r^2 = kQ/(4R^2)$.</p><p class="step">Gauss\'s law: enclosed flux depends only on enclosed charge; spherical symmetry gives same field as point charge.</p><p><strong>$E = kQ/(4R^2)$; exterior field identical to point charge $Q$.</strong></p>',
        },
        {
            "topic": '§0 Week 1 Recap',
            "problem": "An oil-drop suspension is used in Millikan's experiment. A drop with mass $m = 2.0\\times 10^{-15}\\,\\text{kg}$ is held stationary between plates separated $d = 1.0\\,\\text{cm}$ with voltage $V = 500\\,\\text{V}$. How many excess electrons does it carry?",
            "solution": '<p class="step">Balance: $qE = mg \\Rightarrow q = mgd/V$.</p><p class="step">$q = (2.0\\times 10^{-15})(9.8)(0.01)/500 = 3.92\\times 10^{-19}\\,\\text{C}$.</p><p class="step">$N = q/e = 3.92\\times 10^{-19}/(1.6\\times 10^{-19}) \\approx 2.5$ — not integer!</p><p class="step">Nearest integer: 2 or 3 electrons; measurement uncertainty expected in real experiment.</p><p><strong>$q \\approx 4.0\\times 10^{-19}\\,\\text{C}$ $\\approx 2.5e$; nearest integer $N = 2$ or $3$.</strong></p>',
        },
        {
            "topic": '§1 Week 2 Recap',
            "problem": 'A $10\\,\\mu\\text{F}$ capacitor charged to $100\\,\\text{V}$ is connected in parallel with an uncharged $40\\,\\mu\\text{F}$ capacitor. Find final voltage and energy lost.',
            "solution": '<p class="step">Charge conserved: $Q = 10\\times 10^{-6}\\times 100 = 10^{-3}\\,\\text{C}$.</p><p class="step">$C_{\\text{tot}} = 50\\,\\mu\\text{F}$; $V_f = Q/C_{\\text{tot}} = 20\\,\\text{V}$.</p><p class="step">$U_i = \\tfrac{1}{2}(10\\,\\mu)(100)^2 = 0.05\\,\\text{J}$.</p><p class="step">$U_f = \\tfrac{1}{2}(50\\,\\mu)(20)^2 = 0.01\\,\\text{J}$; lost $= 0.04\\,\\text{J}$ (dissipated in connecting resistance).</p><p><strong>$V_f = 20\\,\\text{V}$; energy lost $= 0.04\\,\\text{J}$.</strong></p>',
        },
        {
            "topic": '§1 Week 2 Recap',
            "problem": 'A nichrome wire ($\\rho = 1.0\\times 10^{-6}\\,\\Omega\\,\\text{m}$) must dissipate $500\\,\\text{W}$ at $240\\,\\text{V}$. Find required length if wire diameter is $1.0\\,\\text{mm}$.',
            "solution": '<p class="step">$R = V^2/P = 240^2/500 = 115.2\\,\\Omega$.</p><p class="step">$A = \\pi(0.5\\times 10^{-3})^2 = 7.85\\times 10^{-7}\\,\\text{m}^2$.</p><p class="step">$L = RA/\\rho = 115.2\\times 7.85\\times 10^{-7}/(1.0\\times 10^{-6}) = 90.4\\,\\text{m}$.</p><p><strong>$L \\approx 90\\,\\text{m}$.</strong></p>',
        },
        {
            "topic": '§1 Week 2 Recap',
            "problem": 'Three identical light bulbs rated $60\\,\\text{W}$ at $120\\,\\text{V}$ are connected: (a) all in parallel across $120\\,\\text{V}$, (b) all in series across $120\\,\\text{V}$. Which configuration glows brighter and why?',
            "solution": '<p class="step">Each bulb: $R = V^2/P = 240\\,\\Omega$.</p><p class="step">(a) Parallel: each gets $120\\,\\text{V}$, $P = 60\\,\\text{W}$ each — full brightness.</p><p class="step">(b) Series: each gets $40\\,\\text{V}$, $P = V^2/R = 1600/240 \\approx 6.7\\,\\text{W}$ each — dim.</p><p><strong>Parallel is much brighter; series divides voltage equally at far lower power.</strong></p>',
        },
        {
            "topic": '§2 Week 3 Recap',
            "problem": 'Find current through the $6\\,\\Omega$ resistor: $20\\,\\text{V}$ source, $4\\,\\Omega$ in series with parallel pair $6\\,\\Omega$ and $12\\,\\Omega$.',
            "solution": '<p class="step">$R_p = 6\\times 12/18 = 4\\,\\Omega$; total $R = 8\\,\\Omega$.</p><p class="step">$I_s = 20/8 = 2.5\\,\\text{A}$; $V_p = 2.5\\times 4 = 10\\,\\text{V}$ across parallel pair.</p><p class="step">$I_6 = V_p/6 = 10/6 = 1.67\\,\\text{A}$.</p><p><strong>$I_{6\\Omega} \\approx 1.67\\,\\text{A}$.</strong></p>',
        },
        {
            "topic": '§2 Week 3 Recap',
            "problem": 'A particle moves in a uniform $0.20\\,\\text{T}$ field. It is a deuteron ($q = +e$, $m = 3.34\\times 10^{-27}\\,\\text{kg}$) at $1.0\\times 10^6\\,\\text{m/s}$ perpendicular to $\\vec{B}$. Find cyclotron period and compare to a proton at the same speed.',
            "solution": '<p class="step">$T = 2\\pi m/(qB) = 2\\pi(3.34\\times 10^{-27})/((1.6\\times 10^{-19})(0.20))$.</p><p class="step">$T = 6.57\\times 10^{-7}\\,\\text{s}$.</p><p class="step">Proton: $T_p = 2\\pi(1.67\\times 10^{-27})/((1.6\\times 10^{-19})(0.20)) = 3.27\\times 10^{-7}\\,\\text{s}$.</p><p class="step">Period depends on $m/q$; deuteron has twice the period of proton.</p><p><strong>Deuteron $T \\approx 6.6\\times 10^{-7}\\,\\text{s}$; proton $T \\approx 3.3\\times 10^{-7}\\,\\text{s}$.</strong></p>',
        },
        {
            "topic": '§2 Week 3 Recap',
            "problem": "At what distance from a $10\\,\\text{A}$ wire is the magnetic field equal to the Earth's field ($5.0\\times 10^{-5}\\,\\text{T}$)?",
            "solution": '<p class="step">$B = \\mu_0 I/(2\\pi r) \\Rightarrow r = \\mu_0 I/(2\\pi B)$.</p><p class="step">$r = (4\\pi\\times 10^{-7})(10)/(2\\pi\\times 5.0\\times 10^{-5}) = 4.0\\times 10^{-3}/(5.0\\times 10^{-5}) = 0.08\\,\\text{m}$.</p><p><strong>$r = 8.0\\,\\text{cm}$.</strong></p>',
        },
        {
            "topic": '§3 Week 4 Recap',
            "problem": 'A transformer with $95\\%$ efficiency has $V_p = 240\\,\\text{V}$, $I_p = 2.0\\,\\text{A}$, $V_s = 12\\,\\text{V}$. Find secondary current and power lost.',
            "solution": '<p class="step">$P_{\\text{in}} = 480\\,\\text{W}$; $P_{\\text{out}} = 0.95\\times 480 = 456\\,\\text{W}$.</p><p class="step">$I_s = P_{\\text{out}}/V_s = 456/12 = 38\\,\\text{A}$.</p><p class="step">Lost $= 480 - 456 = 24\\,\\text{W}$.</p><p><strong>$I_s = 38\\,\\text{A}$; losses $= 24\\,\\text{W}$.</strong></p>',
        },
        {
            "topic": '§3 Week 4 Recap',
            "problem": 'A coil ($N = 500$, $A = 0.02\\,\\text{m}^2$, $R = 10\\,\\Omega$) has flux through it change uniformly by $0.10\\,\\text{T}$ in $0.05\\,\\text{s}$. Find induced current.',
            "solution": '<p class="step">$\\varepsilon = N\\Delta\\Phi/\\Delta t = 500\\times 0.02\\times 0.10/0.05 = 20\\,\\text{V}$.</p><p class="step">$I = \\varepsilon/R = 2.0\\,\\text{A}$.</p><p><strong>$I = 2.0\\,\\text{A}$.</strong></p>',
        },
        {
            "topic": '§3 Week 4 Recap',
            "problem": 'Light of wavelength $600\\,\\text{nm}$ has intensity $100\\,\\text{W/m}^2$. Estimate the number of photons passing through $1\\,\\text{cm}^2$ per second.',
            "solution": '<p class="step">Energy per photon: $E = hc/\\lambda = 1240\\,\\text{eV}\\cdot\\text{nm}/600 = 2.07\\,\\text{eV} = 3.31\\times 10^{-19}\\,\\text{J}$.</p><p class="step">Power through $10^{-4}\\,\\text{m}^2$: $P = 0.01\\,\\text{W}$.</p><p class="step">$N = P/E = 0.01/(3.31\\times 10^{-19}) = 3.0\\times 10^{16}$ photons/s.</p><p><strong>$\\approx 3\\times 10^{16}$ photons per second.</strong></p>',
        },
        {
            "topic": '§4 Mixed Problems',
            "problem": 'A parallel-plate capacitor ($C = 5.0\\,\\mu\\text{F}$) is charged to $200\\,\\text{V}$ and then connected across a $10\\,\\Omega$ resistor. Find initial discharge current and time constant.',
            "solution": '<p class="step">$I_0 = V/R = 200/10 = 20\\,\\text{A}$.</p><p class="step">$\\tau = RC = 10\\times 5.0\\times 10^{-6} = 50\\,\\mu\\text{s}$.</p><p class="step">Current decays as $I = I_0 e^{-t/\\tau}$.</p><p><strong>$I_0 = 20\\,\\text{A}$; $\\tau = 50\\,\\mu\\text{s}$.</strong></p>',
        },
        {
            "topic": '§4 Mixed Problems',
            "problem": 'An electron accelerates from rest through $500\\,\\text{V}$ then enters $B = 0.10\\,\\text{T}$ perpendicular to its velocity. Find speed and orbital radius.',
            "solution": '<p class="step">$\\tfrac{1}{2}mv^2 = eV \\Rightarrow v = \\sqrt{2eV/m} = \\sqrt{2(1.6\\times 10^{-19})(500)/(9.1\\times 10^{-31})}$.</p><p class="step">$v = 1.33\\times 10^7\\,\\text{m/s}$.</p><p class="step">$r = mv/(eB) = (9.1\\times 10^{-31})(1.33\\times 10^7)/((1.6\\times 10^{-19})(0.10)) = 7.6\\times 10^{-4}\\,\\text{m}$.</p><p><strong>$v \\approx 1.3\\times 10^7\\,\\text{m/s}$; $r \\approx 0.76\\,\\text{mm}$.</strong></p>',
        },
        {
            "topic": '§4 Mixed Problems',
            "problem": 'A long solenoid ($n = 500\\,\\text{turns/m}$) carries $I = 2.0\\,\\text{A}$. A small loop ($A = 2\\,\\text{cm}^2$, $N = 100$) is inserted along the axis in $0.10\\,\\text{s}$. Estimate induced EMF.',
            "solution": '<p class="step">$B = \\mu_0 n I = (4\\pi\\times 10^{-7})(500)(2.0) = 1.26\\times 10^{-3}\\,\\text{T}$.</p><p class="step">$\\Delta\\Phi = BAN = 1.26\\times 10^{-3}\\times 2\\times 10^{-4}\\times 100 = 2.52\\times 10^{-5}\\,\\text{T\\,m}^2$.</p><p class="step">$\\varepsilon = \\Delta\\Phi/\\Delta t = 2.52\\times 10^{-5}/0.10 = 2.5\\times 10^{-4}\\,\\text{V}$.</p><p><strong>$|\\varepsilon| \\approx 0.25\\,\\text{mV}$.</strong></p>',
        },
        {
            "topic": '§4 Mixed Problems',
            "problem": 'Compare energy stored in: (A) $C = 10\\,\\mu\\text{F}$ at $100\\,\\text{V}$, (B) the same capacitor at $200\\,\\text{V}$. How does energy scale with voltage?',
            "solution": '<p class="step">$U = \\tfrac{1}{2}CV^2$: scales as $V^2$.</p><p class="step">$U_A = 0.5\\times 10\\times 10^{-6}\\times 10^4 = 0.05\\,\\text{J}$.</p><p class="step">$U_B = 0.5\\times 10\\times 10^{-6}\\times 40000 = 0.20\\,\\text{J}$ — four times greater.</p><p class="step">Doubling voltage quadruples stored energy.</p><p><strong>$U_A = 0.05\\,\\text{J}$, $U_B = 0.20\\,\\text{J}$; $U \\propto V^2$.</strong></p>',
        },
    ],
    6: [
        {
            "topic": '§0 SR Postulates',
            "problem": "State Einstein's two postulates of special relativity. Why does the second postulate contradict Galilean velocity addition?",
            "solution": '<p class="step">Postulate 1: laws of physics identical in all inertial frames.</p><p class="step">Postulate 2: speed of light $c$ is same in all inertial frames, independent of source motion.</p><p class="step">Galilean addition: $c\' = c \\pm v$ for moving observer — contradicts measured constancy of $c$.</p><p><strong>Constancy of $c$ replaces Galilean velocity addition at high speeds.</strong></p>',
        },
        {
            "topic": '§0 SR Postulates',
            "problem": 'A spaceship travels at $0.60c$ relative to Earth. It fires a laser beam forward. What speed does Earth measure for the laser light?',
            "solution": '<p class="step">By postulate 2: light speed is $c$ in all inertial frames.</p><p class="step">Earth measures the laser at $c$, not $0.60c + c = 1.60c$.</p><p class="step">Trap: Galilean intuition gives wrong answer.</p><p><strong>$c$ exactly — not $1.6c$.</strong></p>',
        },
        {
            "topic": '§0 SR Postulates',
            "problem": "Explain why there is no preferred inertial frame in special relativity, and how this differs from Newton's assumption of absolute space.",
            "solution": '<p class="step">Newton: absolute rest frame exists (though undetectable) — time and space absolute.</p><p class="step">SR: all inertial frames equivalent for physical laws; no experiment can identify absolute rest.</p><p class="step">Relativity of simultaneity shows time is frame-dependent, not absolute.</p><p><strong>No absolute rest frame; all inertial frames are physically equivalent.</strong></p>',
        },
        {
            "topic": '§0 SR Postulates',
            "problem": 'Muons from cosmic rays have lab half-life $\\tau_0 = 1.5\\,\\mu\\text{s}$. At $v = 0.98c$, what fraction survive after travelling $4.6\\,\\text{km}$ in the lab? (Use time dilation, not length contraction.)',
            "solution": '<p class="step">Lab time: $t = d/v = 4600/(0.98\\times 3\\times 10^8) = 1.57\\times 10^{-5}\\,\\text{s}$.</p><p class="step">$\\gamma = 1/\\sqrt{1-0.98^2} = 5.0$.</p><p class="step">Dilated decay constant in lab: $\\tau = \\gamma\\tau_0 = 7.5\\,\\mu\\text{s}$.</p><p class="step">Survival $N/N_0 = e^{-t/\\tau} = e^{-1.57\\times 10^{-5}/(7.5\\times 10^{-6})} = e^{-2.09} = 0.12$.</p><p><strong>$\\approx 12\\%$ survive — time dilation explains atmospheric muon flux.</strong></p>',
        },
        {
            "topic": '§1 Time Dilation & Length Contraction',
            "problem": 'A clock on a spacecraft reads $5.0\\,\\mu\\text{s}$ between two events on the ship. Earth measures the spacecraft speed as $0.80c$. What time interval does Earth measure between the same events?',
            "solution": '<p class="step">$\\gamma = 1/\\sqrt{1-0.64} = 1.67$.</p><p class="step">$\\Delta t = \\gamma\\Delta t_0 = 1.67\\times 5.0 = 8.3\\,\\mu\\text{s}$.</p><p class="step">Earth sees moving clock run slow: proper time is shortest in rest frame of clock.</p><p><strong>$\\Delta t \\approx 8.3\\,\\mu\\text{s}$ on Earth.</strong></p>',
        },
        {
            "topic": '§1 Time Dilation & Length Contraction',
            "problem": 'A metre stick flies past at $v = 0.90c$. What length does a lab observer measure? Which frame measures proper length?',
            "solution": '<p class="step">$\\gamma = 1/\\sqrt{1-0.81} = 2.29$.</p><p class="step">Contracted: $L = L_0/\\gamma = 1.0/2.29 = 0.44\\,\\text{m}$.</p><p class="step">Proper length $L_0 = 1\\,\\text{m}$ is measured in the stick\'s rest frame.</p><p><strong>Lab measures $L \\approx 0.44\\,\\text{m}$; proper length in stick\'s frame.</strong></p>',
        },
        {
            "topic": '§1 Time Dilation & Length Contraction',
            "problem": 'Twin A stays on Earth; Twin B travels at $0.95c$ for $6.0$ years (Earth time) then returns at $0.95c$. How much older is A than B when they reunite?',
            "solution": '<p class="step">Each leg: Earth time $3.0$ years; $\\gamma = 1/\\sqrt{1-0.9025} = 3.20$.</p><p class="step">B\'s elapsed proper time each leg: $\\Delta t_0 = 3.0/3.20 = 0.94$ years.</p><p class="step">Total for B: $1.88$ years vs $6.0$ years for A.</p><p class="step">A is older by $6.0 - 1.88 = 4.1$ years.</p><p><strong>A is $\\approx 4.1$ years older than B.</strong></p>',
        },
        {
            "topic": '§1 Time Dilation & Length Contraction',
            "problem": 'Can length contraction be detected by photographing a passing object with a fast camera? Explain.',
            "solution": '<p class="step">Photograph captures light arriving at different times from different parts of the object.</p><p class="step">Visual appearance includes rotation (Terrell effect) and distortion — not simply contracted length.</p><p class="step">Measured length requires simultaneous measurement of both ends in the observer\'s frame.</p><p><strong>No — snapshot mixes light travel times; appearance $\\neq$ contracted proper measurement.</strong></p>',
        },
        {
            "topic": '§2 Lorentz Transforms',
            "problem": "Events in frame S: $x_1 = 0$, $t_1 = 0$ and $x_2 = 1.0\\times 10^8\\,\\text{m}$, $t_2 = 0.50\\,\\text{s}$. Frame S' moves at $v = 0.60c$ relative to S. Are the events simultaneous in S'? Find $\\Delta t'$.",
            "solution": '<p class="step">$\\gamma = 1.25$; $\\beta = 0.60$.</p><p class="step">$\\Delta t\' = \\gamma(\\Delta t - \\beta\\Delta x/c) = 1.25(0.50 - 0.60\\times 10^8/(3\\times 10^8))$.</p><p class="step">$\\Delta t\' = 1.25(0.50 - 0.20) = 0.375\\,\\text{s} \\neq 0$.</p><p class="step">Simultaneous in S but not in S\' — relativity of simultaneity.</p><p><strong>$\\Delta t\' = 0.375\\,\\text{s}$; not simultaneous in S\'.</strong></p>',
        },
        {
            "topic": '§2 Lorentz Transforms',
            "problem": 'Use velocity addition: spacecraft A moves at $0.70c$ east, spacecraft B at $0.70c$ west relative to Earth. Find relative speed of A with respect to B.',
            "solution": '<p class="step">$u\' = (u - v)/(1 - uv/c^2)$ with $u = 0.70c$, $v = -0.70c$ (B west).</p><p class="step">$u\' = (0.70c + 0.70c)/(1 + 0.49) = 1.40c/1.49 = 0.94c$.</p><p class="step">Less than $1.40c$ — relativistic addition caps at $c$.</p><p><strong>Relative speed $= 0.94c$ (not $1.4c$).</strong></p>',
        },
        {
            "topic": '§2 Lorentz Transforms',
            "problem": 'The spacetime interval $s^2 = c^2 t^2 - x^2$ is invariant. For two events with $\\Delta x = 3.0\\times 10^8\\,\\text{m}$, $\\Delta t = 2.0\\,\\text{s}$, classify as timelike, lightlike, or spacelike.',
            "solution": '<p class="step">$s^2 = c^2\\Delta t^2 - \\Delta x^2 = (3\\times 10^8)^2(2)^2 - (3\\times 10^8)^2 = (9\\times 10^{16})(4-1) = 2.7\\times 10^{17}$.</p><p class="step">$s^2 > 0$: timelike — events can be connected by slower-than-light signal.</p><p><strong>Timelike ($s^2 > 0$); causally connectable.</strong></p>',
        },
        {
            "topic": '§3 Relativistic Doppler',
            "problem": 'A galaxy recedes at $v = 0.10c$. A spectral line at $\\lambda_0 = 500\\,\\text{nm}$ in the lab is observed from Earth. Find observed wavelength (relativistic Doppler, source receding).',
            "solution": '<p class="step">Relativistic: $\\lambda = \\lambda_0\\sqrt{(1+\\beta)/(1-\\beta)}$ with $\\beta = 0.10$.</p><p class="step">$\\lambda = 500\\sqrt{1.10/0.90} = 500\\times 1.105 = 552\\,\\text{nm}$.</p><p class="step">Non-relativistic would give $550\\,\\text{nm}$ — small correction at $0.10c$.</p><p><strong>$\\lambda \\approx 552\\,\\text{nm}$ (redshifted).</strong></p>',
        },
        {
            "topic": '§3 Relativistic Doppler',
            "problem": 'A police radar gun uses $f_0 = 24\\,\\text{GHz}$. A car approaches at $30\\,\\text{m/s}$. Find approximate frequency shift $\\Delta f$ (use non-relativistic approximation, $v \\ll c$).',
            "solution": '<p class="step">$\\Delta f \\approx 2f_0 v/c = 2(24\\times 10^9)(30)/(3\\times 10^8)$.</p><p class="step">$\\Delta f = 4800\\,\\text{Hz} = 4.8\\,\\text{kHz}$.</p><p class="step">Moving source/observer doubles shift vs stationary source.</p><p><strong>$\\Delta f \\approx 4.8\\,\\text{kHz}$.</strong></p>',
        },
        {
            "topic": '§3 Relativistic Doppler',
            "problem": "A GPS satellite clock emits $f_0 = 1.575\\,\\text{GHz}$. Relative to Earth the satellite speed is $v = 3.9\\,\\text{km/s}$ and it is higher in Earth's gravitational field (gravitational redshift adds a separate correction). Using only special-relativistic Doppler for the orbital motion, estimate the fractional frequency shift $\\Delta f/f_0$.",
            "solution": '<p class="step">Non-relativistic orbital Doppler: $\\Delta f/f_0 \\approx v/c$ for transverse-dominated GPS orbit.</p><p class="step">$\\Delta f/f_0 \\approx 3900/(3.0\\times 10^8) = 1.3\\times 10^{-5}$.</p><p class="step">GPS engineering must correct both SR ($\\sim 10^{-5}$) and GR ($\\sim 10^{-5}$) shifts to maintain metre-level positioning.</p><p><strong>$\\Delta f/f_0 \\approx 1.3\\times 10^{-5}$ from SR alone.</strong></p>',
        },
    ],
    7: [
        {
            "topic": '§0 Photoelectric Effect',
            "problem": 'Light of wavelength $\\lambda = 400\\,\\text{nm}$ strikes a sodium surface (work function $W = 2.3\\,\\text{eV}$). Find the maximum kinetic energy of emitted photoelectrons and their maximum speed.',
            "solution": '<p class="step">$E_{\\text{photon}} = hc/\\lambda = 1240/400 = 3.1\\,\\text{eV}$.</p><p class="step">$K_{\\max} = E - W = 0.8\\,\\text{eV} = 1.28\\times 10^{-19}\\,\\text{J}$.</p><p class="step">$v = \\sqrt{2K/m} = \\sqrt{2(1.28\\times 10^{-19})/(9.1\\times 10^{-31})} = 5.3\\times 10^5\\,\\text{m/s}$.</p><p><strong>$K_{\\max} = 0.8\\,\\text{eV}$; $v \\approx 5.3\\times 10^5\\,\\text{m/s}$.</strong></p>',
        },
        {
            "topic": '§0 Photoelectric Effect',
            "problem": 'In a photoelectric experiment, stopping potential is $1.5\\,\\text{V}$ for $\\lambda = 300\\,\\text{nm}$. Find the work function of the metal.',
            "solution": '<p class="step">$K_{\\max} = eV_s = 1.5\\,\\text{eV}$.</p><p class="step">$E_{\\text{photon}} = 1240/300 = 4.13\\,\\text{eV}$.</p><p class="step">$W = E - K_{\\max} = 4.13 - 1.5 = 2.63\\,\\text{eV}$.</p><p><strong>$W \\approx 2.6\\,\\text{eV}$.</strong></p>',
        },
        {
            "topic": '§0 Photoelectric Effect',
            "problem": 'Explain why the photoelectric effect cannot be explained by classical wave theory, citing two independent failures.',
            "solution": '<p class="step">(1) Instantaneous emission: classical heating of electrons would take measurable time — not observed.</p><p class="step">(2) Threshold frequency: below $f_0$, no emission regardless of intensity; classical predicts emission at any frequency if intensity is high enough.</p><p class="step">(3) $K_{\\max}$ independent of intensity — classical predicts higher intensity gives more energy to electrons.</p><p><strong>Classical theory fails on threshold frequency and $K_{\\max}$ vs intensity.</strong></p>',
        },
        {
            "topic": '§0 Photoelectric Effect',
            "problem": 'A photon of energy $5.0\\,\\text{eV}$ ionises a hydrogen atom in the ground state. What kinetic energy does the freed electron carry?',
            "solution": '<p class="step">Ionisation energy of H: $13.6\\,\\text{eV}$ — photon energy $5.0\\,\\text{eV}$ is insufficient.</p><p class="step">No ionisation occurs; photon cannot be absorbed for ionisation (only excitation if $E$ matches level spacing).</p><p class="step">Trap: assuming ionisation with under-threshold photon.</p><p><strong>No ionisation — $5.0\\,\\text{eV} < 13.6\\,\\text{eV}$ binding energy.</strong></p>',
        },
        {
            "topic": '§1 X-ray Production',
            "problem": 'An X-ray tube operates at $40\\,\\text{kV}$. Find the minimum (cut-off) wavelength of emitted photons and the maximum photon energy.',
            "solution": '<p class="step">$E_{\\max} = eV = 40\\,\\text{keV}$.</p><p class="step">$\\lambda_{\\min} = hc/E = 1240\\,\\text{eV}\\cdot\\text{nm}/(40000\\,\\text{eV}) = 0.031\\,\\text{nm}$.</p><p><strong>$E_{\\max} = 40\\,\\text{keV}$; $\\lambda_{\\min} = 0.031\\,\\text{nm}$.</strong></p>',
        },
        {
            "topic": '§1 X-ray Production',
            "problem": 'Characteristic X-rays from tungsten ($Z = 74$) include a $K_\\alpha$ line at $\\lambda \\approx 0.021\\,\\text{nm}$. Estimate the energy of the $n=2$ to $n=1$ transition using the Bohr model with correction $(Z-1)^2$.',
            "solution": '<p class="step">$E \\approx 13.6\\,(Z-1)^2\\,(1 - 1/4)\\,\\text{eV} = 13.6\\times 73^2\\times 0.75$.</p><p class="step">$E \\approx 13.6\\times 5329\\times 0.75 \\approx 54.4\\,\\text{keV}$.</p><p class="step">$\\lambda = 1240/(54400) \\approx 0.023\\,\\text{nm}$ — reasonable agreement.</p><p><strong>$E \\approx 54\\,\\text{keV}$; $\\lambda \\approx 0.023\\,\\text{nm}$ (close to measured).</strong></p>',
        },
        {
            "topic": '§1 X-ray Production',
            "problem": 'Why must the target in an X-ray tube be made of a high-melting-point metal, and why is lead shielding used around the housing?',
            "solution": '<p class="step">Electron beam deposits intense local heating; tungsten withstands high temperatures.</p><p class="step">X-rays are penetrating ionising radiation — lead shielding protects operators from scatter and leakage.</p><p class="step">Bremsstrahlung and characteristic lines both produce hazardous broadband radiation.</p><p><strong>High melting point survives beam heating; lead blocks ionising X-ray leakage.</strong></p>',
        },
        {
            "topic": '§2 Hydrogen Atom',
            "problem": 'Calculate the wavelength of the H$\\alpha$ line ($n=3 \\to n=2$) using the Rydberg formula.',
            "solution": '<p class="step">$1/\\lambda = R(1/n_2^2 - 1/n_1^2) = 1.097\\times 10^7(1/4 - 1/9) = 1.097\\times 10^7\\times 5/36$.</p><p class="step">$\\lambda = 36/(1.097\\times 10^7\\times 5) = 6.56\\times 10^{-7}\\,\\text{m} = 656\\,\\text{nm}$.</p><p class="step">Red visible line — prominent in stellar spectra.</p><p><strong>$\\lambda = 656\\,\\text{nm}$ (red).</strong></p>',
        },
        {
            "topic": '§2 Hydrogen Atom',
            "problem": 'An electron in hydrogen is in the $n = 4$ state. List the possible photon energies for transitions to lower levels and identify which are in the visible range ($1.8$–$3.1\\,\\text{eV}$).',
            "solution": '<p class="step">$E_n = -13.6/n^2\\,\\text{eV}$: $E_4 = -0.85$, $E_3 = -1.51$, $E_2 = -3.40$, $E_1 = -13.6$.</p><p class="step">$4\\to 3$: $0.66\\,\\text{eV}$ (IR); $4\\to 2$: $2.55\\,\\text{eV}$ (visible); $4\\to 1$: $12.75\\,\\text{eV}$ (UV).</p><p class="step">Also $3\\to 2$: $1.89\\,\\text{eV}$ (visible red) if cascade occurs.</p><p class="step">$4\\to 2$ at $2.55\\,\\text{eV}$ and $3\\to 2$ at $1.89\\,\\text{eV}$ are in visible range.</p><p><strong>Visible: $4\\to 2$ ($2.55\\,\\text{eV}$) and $3\\to 2$ ($1.89\\,\\text{eV}$).</strong></p>',
        },
        {
            "topic": '§2 Hydrogen Atom',
            "problem": 'The Bohr radius is $a_0 = 0.529\\,\\text{nm}$. Find the radius of the $n = 3$ orbit and the electron speed in that orbit.',
            "solution": '<p class="step">$r_n = n^2 a_0 = 9\\times 0.529 = 4.76\\,\\text{nm}$.</p><p class="step">$v_n = v_1/n = (2.19\\times 10^6)/3 = 7.3\\times 10^5\\,\\text{m/s}$.</p><p><strong>$r_3 = 4.76\\,\\text{nm}$; $v_3 \\approx 7.3\\times 10^5\\,\\text{m/s}$.</strong></p>',
        },
        {
            "topic": '§2 Hydrogen Atom',
            "problem": 'Explain why the Bohr model succeeds for hydrogen but fails for multi-electron atoms.',
            "solution": '<p class="step">Bohr quantises angular momentum for a single electron in a central $1/r$ potential — works for H, He$^+$, Li$^{2+}$.</p><p class="step">Multi-electron atoms: electron-electron repulsion, no exact circular orbits, screening — energy depends on $n$ and $l$.</p><p class="step">Spectral lines show fine structure and complex splitting not predicted by Bohr.</p><p><strong>Only single-electron systems; electron interactions break simple quantised orbit picture.</strong></p>',
        },
        {
            "topic": '§3 Lasers',
            "problem": 'A He-Ne laser emits at $\\lambda = 632.8\\,\\text{nm}$ with power $5.0\\,\\text{mW}$. How many photons are emitted per second?',
            "solution": '<p class="step">$E_{\\text{photon}} = hc/\\lambda = 1240/632.8 = 1.96\\,\\text{eV} = 3.14\\times 10^{-19}\\,\\text{J}$.</p><p class="step">$N = P/E = 0.005/(3.14\\times 10^{-19}) = 1.6\\times 10^{16}$ photons/s.</p><p><strong>$\\approx 1.6\\times 10^{16}$ photons per second.</strong></p>',
        },
        {
            "topic": '§3 Lasers',
            "problem": 'Explain the three requirements for laser action: active medium, pumping, and optical cavity. Why is stimulated emission essential?',
            "solution": '<p class="step">Active medium: energy levels supporting population inversion ($E_2 > E_1$ with more atoms in $E_2$).</p><p class="step">Pumping: external energy input to create inversion (not possible in equilibrium).</p><p class="step">Optical cavity: mirrors provide feedback, amplifying stimulated emission along axis.</p><p class="step">Stimulated emission produces coherent, monochromatic, directional beam — spontaneous emission alone is random.</p><p><strong>Inversion + feedback amplify stimulated emission into coherent laser output.</strong></p>',
        },
        {
            "topic": '§3 Lasers',
            "problem": 'A ruby laser has metastable state lifetime $\\tau = 3\\,\\text{ms}$ and ground-state recovery $\\tau_g \\approx 10^{-9}\\,\\text{s}$. Why does the metastable state enable population inversion?',
            "solution": '<p class="step">Metastable state decays slowly ($3\\,\\text{ms}$) — atoms accumulate in $E_2$.</p><p class="step">Fast ground-state recovery allows rapid recycling after emission.</p><p class="step">Pump continuously fills upper levels faster than spontaneous decay empties them.</p><p class="step">Without metastable state, inversion would collapse before amplification.</p><p><strong>Slow metastable decay traps population in $E_2$, enabling inversion.</strong></p>',
        },
    ],
    8: [
        {
            "topic": '§0 de Broglie',
            "problem": 'A thermal neutron ($KE = 0.025\\,\\text{eV}$) from a research reactor moderator is used to probe crystal lattice spacings in a steel weld inspection rig. Find its de Broglie wavelength and state whether it can resolve features separated by $0.20\\,\\text{nm}$.',
            "solution": '<p class="step">$KE = 0.025\\times 1.6\\times 10^{-19} = 4.0\\times 10^{-21}\\,\\text{J}$.</p><p class="step">$p = \\sqrt{2m_n KE} = \\sqrt{2(1.67\\times 10^{-27})(4.0\\times 10^{-21})} = 3.65\\times 10^{-24}\\,\\text{kg\\,m/s}$.</p><p class="step">$\\lambda = h/p = 6.626\\times 10^{-34}/(3.65\\times 10^{-24}) = 1.81\\times 10^{-10}\\,\\text{m} = 0.181\\,\\text{nm}$.</p><p class="step">Diffraction is significant when $\\lambda \\sim$ spacing; $0.181\\,\\text{nm} < 0.20\\,\\text{nm}$, so resolution is marginal but feasible.</p><p><strong>$\\lambda \\approx 0.18\\,\\text{nm}$; comparable to atomic spacing, suitable for lattice diffraction.</strong></p>',
        },
        {
            "topic": '§0 de Broglie',
            "problem": 'An electron and a proton are each accelerated from rest through $150\\,\\text{V}$ in a semiconductor ion-implantation test bench. Find both de Broglie wavelengths and their ratio $\\lambda_e/\\lambda_p$.',
            "solution": '<p class="step">Electron shortcut: $\\lambda_e = 1.226/\\sqrt{150}\\,\\text{nm} = 0.100\\,\\text{nm}$.</p><p class="step">Proton: $KE = 150\\,\\text{eV}$, $p = \\sqrt{2m_p KE} = \\sqrt{2(1.67\\times 10^{-27})(2.4\\times 10^{-17})} = 8.95\\times 10^{-22}\\,\\text{kg\\,m/s}$.</p><p class="step">$\\lambda_p = h/p = 6.626\\times 10^{-34}/(8.95\\times 10^{-22}) = 7.4\\times 10^{-13}\\,\\text{m}$.</p><p class="step">Ratio: $\\lambda_e/\\lambda_p = \\sqrt{m_p/m_e} \\approx \\sqrt{1836} \\approx 43$.</p><p class="step">Sanity: lighter particle, longer wavelength at equal KE.</p><p><strong>$\\lambda_e \\approx 0.10\\,\\text{nm}$, $\\lambda_p \\approx 7.4\\times 10^{-4}\\,\\text{nm}$; ratio $\\approx 43$.</strong></p>',
        },
        {
            "topic": '§0 de Broglie',
            "problem": 'A scanning electron microscope accelerates electrons through $30\\,\\text{kV}$. Using the non-relativistic approximation, find the de Broglie wavelength. Would relativistic corrections ($\\gamma$) change the result by more than $5\\%$?',
            "solution": '<p class="step">$\\lambda = 1.226/\\sqrt{30000}\\,\\text{nm} = 1.226/173.2 = 7.1\\times 10^{-3}\\,\\text{nm} = 7.1\\,\\text{pm}$.</p><p class="step">Kinetic energy $30\\,\\text{keV}$ vs rest energy $m_e c^2 = 511\\,\\text{keV}$: $KE/(m_e c^2) \\approx 0.059$.</p><p class="step">Relativistic correction is small ($< 10\\%$) when $KE \\ll m_e c^2$; here $\\approx 6\\%$ correction expected.</p><p class="step">Non-relativistic estimate is adequate for order-of-magnitude but not exact at $30\\,\\text{kV}$.</p><p><strong>$\\lambda \\approx 7.1\\,\\text{pm}$; relativistic correction is $\\sim 5$–$10\\%$, borderline.</strong></p>',
        },
        {
            "topic": '§0 de Broglie',
            "problem": 'A $2.0\\,\\text{kg}$ surveying drone flies at $15\\,\\text{m/s}$. Calculate its de Broglie wavelength and explain why GPS navigation never needs to account for its wave nature.',
            "solution": '<p class="step">$\\lambda = h/(mv) = 6.626\\times 10^{-34}/(2.0\\times 15) = 2.2\\times 10^{-35}\\,\\text{m}$.</p><p class="step">This is $\\sim 10^{25}$ times smaller than a nucleus — utterly negligible.</p><p class="step">Wave effects require $\\lambda$ comparable to obstacle/aperture size; macroscopic objects always behave classically.</p><p><strong>$\\lambda \\approx 2\\times 10^{-35}\\,\\text{m}$; wave nature is unobservable at macroscopic scale.</strong></p>',
        },
        {
            "topic": '§1 Wave Functions',
            "problem": 'A quantum-dot sensor models an electron with probability density $|\\psi(x)|^2 = A e^{-x^2/(2\\sigma^2)}$ for $-\\infty < x < \\infty$, with $\\sigma = 0.50\\,\\text{nm}$. Find the normalisation constant $A$.',
            "solution": '<p class="step">Normalisation: $\\int_{-\\infty}^{\\infty} A e^{-x^2/(2\\sigma^2)}\\,dx = 1$.</p><p class="step">Standard Gaussian integral: $\\int_{-\\infty}^{\\infty} e^{-x^2/(2\\sigma^2)}\\,dx = \\sigma\\sqrt{2\\pi}$.</p><p class="step">$A \\cdot \\sigma\\sqrt{2\\pi} = 1 \\Rightarrow A = 1/(\\sigma\\sqrt{2\\pi})$.</p><p class="step">$A = 1/(0.50\\times 10^{-9}\\times\\sqrt{2\\pi}) = 8.0\\times 10^8\\,\\text{m}^{-1}$.</p><p><strong>$A = 1/(\\sigma\\sqrt{2\\pi}) \\approx 8.0\\times 10^8\\,\\text{m}^{-1}$.</strong></p>',
        },
        {
            "topic": '§1 Wave Functions',
            "problem": 'An electron in a $1.0\\,\\text{nm}$ infinite well has ground-state wave function $\\psi(x) = \\sqrt{2/L}\\sin(\\pi x/L)$. Find the probability of locating it in the central third of the well ($L/3 < x < 2L/3$).',
            "solution": '<p class="step">$P = \\int_{L/3}^{2L/3} \\frac{2}{L}\\sin^2\\!\\left(\\frac{\\pi x}{L}\\right)dx$.</p><p class="step">Let $u = \\pi x/L$: $P = \\frac{2}{\\pi}\\int_{\\pi/3}^{2\\pi/3}\\sin^2 u\\,du = \\frac{2}{\\pi}\\left[\\frac{u}{2}-\\frac{\\sin 2u}{4}\\right]_{\\pi/3}^{2\\pi/3}$.</p><p class="step">$= \\frac{2}{\\pi}\\left(\\frac{\\pi}{6} + \\frac{\\sqrt{3}}{8}\\right) = \\frac{1}{3} + \\frac{\\sqrt{3}}{4\\pi} \\approx 0.47$.</p><p class="step">Sanity: nearly half the probability in the central third, consistent with the sine-squared envelope peaking at the centre.</p><p><strong>$P \\approx 0.47$ (about $47\\%$).</strong></p>',
        },
        {
            "topic": '§1 Wave Functions',
            "problem": 'The first excited state ($n=2$) of a particle in a box has a node at the centre. Explain, using $|\\psi|^2$, why a measurement is never expected to find the particle exactly at $x = L/2$.',
            "solution": '<p class="step">For $n=2$: $\\psi(x) \\propto \\sin(2\\pi x/L)$, which is zero at $x = L/2$.</p><p class="step">Therefore $|\\psi(L/2)|^2 = 0$: the probability density vanishes at the node.</p><p class="step">A node is a point of destructive interference in the standing matter wave — the particle has zero probability of being found there.</p><p class="step">This is fundamentally different from classical mechanics, where a particle could sit at any point.</p><p><strong>$|\\psi|^2 = 0$ at the node; zero probability of detection at $x = L/2$.</strong></p>',
        },
        {
            "topic": '§2 Uncertainty & Particle in a Box',
            "problem": 'A GaN quantum-well LED confines electrons to a region of width $L = 4.0\\,\\text{nm}$. Find the ground-state ($n=1$) energy in eV.',
            "solution": '<p class="step">$E_1 = \\dfrac{h^2}{8m_e L^2} = \\dfrac{(6.626\\times 10^{-34})^2}{8(9.11\\times 10^{-31})(4.0\\times 10^{-9})^2}$.</p><p class="step">Numerator: $4.39\\times 10^{-67}$. Denominator: $1.17\\times 10^{-46}$.</p><p class="step">$E_1 = 3.75\\times 10^{-21}\\,\\text{J} = 3.75\\times 10^{-21}/(1.6\\times 10^{-19}) = 0.023\\,\\text{eV}$.</p><p class="step">Sanity: nanoscale confinement gives tens of meV — typical for visible-LED quantum wells.</p><p><strong>$E_1 \\approx 0.023\\,\\text{eV}$ ($23\\,\\text{meV}$).</strong></p>',
        },
        {
            "topic": '§2 Uncertainty & Particle in a Box',
            "problem": 'An STM tip localises an electron to $\\Delta x = 0.050\\,\\text{nm}$. Estimate the minimum momentum uncertainty $\\Delta p$ and corresponding velocity uncertainty $\\Delta v$.',
            "solution": '<p class="step">$\\Delta p \\geq \\hbar/(2\\Delta x) = 1.055\\times 10^{-34}/(2 \\times 0.050\\times 10^{-9}) = 1.06\\times 10^{-24}\\,\\text{kg\\,m/s}$.</p><p class="step">$\\Delta v = \\Delta p/m_e = 1.06\\times 10^{-24}/(9.11\\times 10^{-31}) = 1.16\\times 10^6\\,\\text{m/s}$.</p><p class="step">This is a substantial fraction of typical atomic electron speeds ($\\sim 10^6\\,\\text{m/s}$), confirming quantum confinement matters at nanometre scales.</p><p><strong>$\\Delta p \\geq 1.1\\times 10^{-24}\\,\\text{kg\\,m/s}$; $\\Delta v \\geq 1.2\\times 10^6\\,\\text{m/s}$.</strong></p>',
        },
        {
            "topic": '§2 Uncertainty & Particle in a Box',
            "problem": 'An electron in a $0.80\\,\\text{nm}$ box undergoes a transition from $n=3$ to $n=1$. Find the photon energy (eV) and wavelength (nm).',
            "solution": '<p class="step">$E_n = n^2 E_1$. With $L = 0.80\\,\\text{nm}$: $E_1 = h^2/(8m_e L^2) = 0.059\\,\\text{eV}$.</p><p class="step">$E_3 = 9 E_1 = 0.53\\,\\text{eV}$; $\\Delta E = E_3 - E_1 = 8 E_1 = 0.47\\,\\text{eV}$.</p><p class="step">$\\lambda = 1240/\\Delta E = 1240/0.47 = 2640\\,\\text{nm}$ (infrared).</p><p class="step">Sanity: larger $\\Delta n$ gives higher-energy photon; $n=3 \\to 1$ is a substantial jump.</p><p><strong>Photon energy $\\approx 0.47\\,\\text{eV}$; $\\lambda \\approx 2600\\,\\text{nm}$ (IR).</strong></p>',
        },
        {
            "topic": '§2 Uncertainty & Particle in a Box',
            "problem": 'If the width of a particle-in-a-box system is doubled ($L \\to 2L$), by what factor do the ground-state energy and the energy spacing $E_2 - E_1$ change?',
            "solution": '<p class="step">$E_n \\propto 1/L^2$. Doubling $L$ gives $E_1\' = E_1/4$.</p><p class="step">$E_2\' - E_1\' = (4-1)E_1/4 = 3E_1/4$, whereas originally $E_2 - E_1 = 3E_1$.</p><p class="step">Spacing factor: $(3E_1/4)/(3E_1) = 1/4$.</p><p class="step">Both ground-state energy and level spacing decrease by a factor of $4$.</p><p><strong>Ground-state energy $\\times\\,1/4$; spacing $E_2-E_1$ also $\\times\\,1/4$.</strong></p>',
        },
        {
            "topic": '§3 Nuclear Physics',
            "problem": 'A $^{60}\\text{Co}$ radiography source has initial activity $A_0 = 3.7\\times 10^{10}\\,\\text{Bq}$ ($1.0\\,\\text{Ci}$). Given $t_{1/2} = 5.27\\,\\text{y}$, find the activity after $10.54\\,\\text{y}$ (two half-lives).',
            "solution": '<p class="step">$A = A_0/2^n$ where $n = t/t_{1/2} = 10.54/5.27 = 2$.</p><p class="step">$A = 3.7\\times 10^{10}/4 = 9.3\\times 10^9\\,\\text{Bq}$.</p><p class="step">Alternatively: $\\lambda = \\ln 2/t_{1/2}$, $A = A_0 e^{-\\lambda t}$ gives the same result.</p><p class="step">Sanity: activity quarters after two half-lives.</p><p><strong>$A \\approx 9.3\\times 10^9\\,\\text{Bq}$ ($0.25\\,\\text{Ci}$).</strong></p>',
        },
        {
            "topic": '§3 Nuclear Physics',
            "problem": '$^{56}\\text{Fe}$ has atomic mass $55.934937\\,\\text{u}$. Given $m_p = 1.007276\\,\\text{u}$, $m_n = 1.008665\\,\\text{u}$, $m_e = 0.000549\\,\\text{u}$, find the binding energy per nucleon.',
            "solution": '<p class="step">Nuclear mass $= 55.934937 - 26(0.000549) = 55.920663\\,\\text{u}$.</p><p class="step">Constituent mass $= 26(1.007276) + 30(1.008665) = 56.4487\\,\\text{u}$.</p><p class="step">Mass defect: $\\Delta m = 56.4487 - 55.9207 = 0.528\\,\\text{u}$.</p><p class="step">$E_b = 0.528 \\times 931.5 = 492\\,\\text{MeV}$; per nucleon: $492/56 = 8.8\\,\\text{MeV/nucleon}$.</p><p class="step">Sanity: $^{56}\\text{Fe}$ sits near the peak of the binding-energy curve.</p><p><strong>Binding energy $\\approx 492\\,\\text{MeV}$; $\\approx 8.8\\,\\text{MeV/nucleon}$.</strong></p>',
        },
        {
            "topic": '§3 Nuclear Physics',
            "problem": 'A smoke-detector ionisation chamber contains $1.0\\,\\mu\\text{g}$ of $^{241}\\text{Am}$ ($t_{1/2} = 432\\,\\text{y}$). Estimate the initial decay rate (activity) in Bq. ($N_A = 6.02\\times 10^{23}\\,\\text{mol}^{-1}$, molar mass $\\approx 241\\,\\text{g/mol}$)',
            "solution": '<p class="step">$N = (10^{-6}\\,\\text{g}/241\\,\\text{g/mol})\\times 6.02\\times 10^{23} = 2.50\\times 10^{15}$ atoms.</p><p class="step">$\\lambda = \\ln 2/t_{1/2} = 0.693/(432\\times 3.16\\times 10^7\\,\\text{s}) = 5.08\\times 10^{-11}\\,\\text{s}^{-1}$.</p><p class="step">$A = \\lambda N = 5.08\\times 10^{-11}\\times 2.50\\times 10^{15} = 1.27\\times 10^5\\,\\text{Bq}$.</p><p class="step">Sanity: microgram quantities of long-lived alpha emitters give $\\sim 10^5$ Bq — consistent with commercial smoke detectors.</p><p><strong>Initial activity $\\approx 1.3\\times 10^5\\,\\text{Bq}$ ($130\\,\\text{kBq}$).</strong></p>',
        },
    ],
    9: [
        {
            "topic": '§0 Special Relativity Review',
            "problem": 'A GPS satellite orbits at $20\\,200\\,\\text{km}$ altitude with speed $3.87\\,\\text{km/s}$. Calculate the time-dilation factor $\\gamma$ and the daily time gain (in $\\mu\\text{s}$) due to special relativity alone. ($c = 3.00\\times 10^8\\,\\text{m/s}$)',
            "solution": '<p class="step">$\\beta = v/c = 3870/(3.00\\times 10^8) = 1.29\\times 10^{-5}$.</p><p class="step">$\\gamma = 1/\\sqrt{1-\\beta^2} \\approx 1 + \\beta^2/2 = 1 + 8.3\\times 10^{-11}$.</p><p class="step">Daily time difference: $\\Delta t = (\\gamma - 1)\\times 86400\\,\\text{s} = 8.3\\times 10^{-11}\\times 86400 = 7.2\\times 10^{-6}\\,\\text{s}$.</p><p class="step">SR causes the satellite clock to run slow (lose time) by $\\approx 7\\,\\mu\\text{s/day}$.</p><p><strong>$\\gamma \\approx 1.000\\,000\\,000\\,083$; SR correction $\\approx -7\\,\\mu\\text{s/day}$ (clock runs slow).</strong></p>',
        },
        {
            "topic": '§0 Special Relativity Review',
            "problem": 'A muon created in the upper atmosphere travels at $0.98c$ toward a ground-based cosmic-ray detector. The muon half-life in its rest frame is $1.56\\,\\mu\\text{s}$. How far can it travel (in the lab frame) before half of them decay?',
            "solution": '<p class="step">Lab-frame lifetime: $\\tau_{\\text{lab}} = \\gamma\\tau_0$.</p><p class="step">$\\gamma = 1/\\sqrt{1-0.98^2} = 1/\\sqrt{0.0396} = 5.03$.</p><p class="step">$\\tau_{\\text{lab}} = 5.03\\times 1.56\\,\\mu\\text{s} = 7.85\\,\\mu\\text{s}$.</p><p class="step">Distance: $d = v\\tau_{\\text{lab}} = 0.98\\times 3.00\\times 10^8\\times 7.85\\times 10^{-6} = 2300\\,\\text{m}$.</p><p class="step">Without time dilation, range would be only $0.98c\\times 1.56\\,\\mu\\text{s} = 460\\,\\text{m}$.</p><p><strong>Half-decay distance $\\approx 2.3\\,\\text{km}$ in the lab frame.</strong></p>',
        },
        {
            "topic": '§0 Special Relativity Review',
            "problem": 'A relativistic proton in the Australian Synchrotron has total energy $E = 3.0\\,\\text{GeV}$. Find its speed as a fraction of $c$ and its relativistic momentum. ($m_p c^2 = 938\\,\\text{MeV}$)',
            "solution": '<p class="step">$\\gamma = E/(m_p c^2) = 3000/938 = 3.20$.</p><p class="step">$\\gamma = 1/\\sqrt{1-\\beta^2} \\Rightarrow \\beta = \\sqrt{1-1/\\gamma^2} = \\sqrt{1-1/10.24} = 0.947$.</p><p class="step">$p = \\gamma m_p v = \\sqrt{E^2 - (m_p c^2)^2}/c = \\sqrt{9-0.880}/c \\times \\text{GeV} = 2.85\\,\\text{GeV}/c$.</p><p class="step">Sanity: at $\\gamma = 3.2$, speed is near but below $c$.</p><p><strong>$v = 0.947c$; $p \\approx 2.85\\,\\text{GeV}/c$.</strong></p>',
        },
        {
            "topic": '§1 Photons & Atomic Physics Review',
            "problem": 'A silicon solar cell has work function $\\phi = 4.6\\,\\text{eV}$. Find the threshold wavelength and the maximum kinetic energy of photoelectrons when illuminated by $\\lambda = 250\\,\\text{nm}$ UV.',
            "solution": '<p class="step">Threshold: $\\lambda_0 = hc/\\phi = 1240/4.6 = 270\\,\\text{nm}$.</p><p class="step">Photon energy: $E = hc/\\lambda = 1240/250 = 4.96\\,\\text{eV}$.</p><p class="step">$KE_{\\max} = E - \\phi = 4.96 - 4.6 = 0.36\\,\\text{eV}$.</p><p class="step">Since $250\\,\\text{nm} < 270\\,\\text{nm}$, photoelectric emission occurs.</p><p><strong>Threshold $\\lambda_0 \\approx 270\\,\\text{nm}$; $KE_{\\max} = 0.36\\,\\text{eV}$.</strong></p>',
        },
        {
            "topic": '§1 Photons & Atomic Physics Review',
            "problem": 'An X-ray tube operating at $40\\,\\text{kV}$ in a materials-testing lab produces bremsstrahlung. Find the minimum (cut-off) wavelength of the emitted X-rays.',
            "solution": '<p class="step">Cut-off when photon energy equals electron kinetic energy: $eV = hc/\\lambda_{\\min}$.</p><p class="step">$\\lambda_{\\min} = hc/(eV) = 1240\\,\\text{eV\\,nm}/40000\\,\\text{eV} = 0.031\\,\\text{nm} = 31\\,\\text{pm}$.</p><p class="step">Sanity: higher voltage $\\Rightarrow$ shorter minimum wavelength (harder X-rays).</p><p><strong>$\\lambda_{\\min} = 0.031\\,\\text{nm}$ ($31\\,\\text{pm}$).</strong></p>',
        },
        {
            "topic": '§1 Photons & Atomic Physics Review',
            "problem": 'A hydrogen atom transitions from $n=4$ to $n=2$ (Balmer series). Find the photon wavelength and specify the colour region.',
            "solution": '<p class="step">$\\Delta E = 13.6\\,(1/4 - 1/16) = 13.6\\times 3/16 = 2.55\\,\\text{eV}$.</p><p class="step">$\\lambda = 1240/2.55 = 486\\,\\text{nm}$.</p><p class="step">This is the hydrogen $H_\\beta$ line — blue-green visible light.</p><p><strong>$\\lambda = 486\\,\\text{nm}$ (blue-green, Balmer $H_\\beta$).</strong></p>',
        },
        {
            "topic": '§2 Matter Waves & Nuclear Review',
            "problem": 'A helium ion $\\text{He}^+$ (single electron) is in the $n=3$ state of a Bohr-like atom. Find the orbital radius and the ionisation energy from this level.',
            "solution": '<p class="step">Bohr radius scales as $r_n = n^2 a_0 / Z$ with $Z=2$ for $\\text{He}^+$.</p><p class="step">$r_3 = 9 \\times 0.0529/2 = 0.238\\,\\text{nm}$.</p><p class="step">Ionisation energy from $n=3$: $E = 13.6 Z^2/n^2 = 13.6\\times 4/9 = 6.04\\,\\text{eV}$.</p><p class="step">Sanity: higher $Z$ and lower $n$ give more tightly bound states.</p><p><strong>$r_3 \\approx 0.24\\,\\text{nm}$; ionisation energy $\\approx 6.0\\,\\text{eV}$.</strong></p>',
        },
        {
            "topic": '§2 Matter Waves & Nuclear Review',
            "problem": 'A $^{131}\\text{I}$ tracer ($t_{1/2} = 8.0\\,\\text{d}$) is administered for thyroid imaging. What fraction remains after $24\\,\\text{d}$? Express as a percentage.',
            "solution": '<p class="step">$n = 24/8 = 3$ half-lives.</p><p class="step">Fraction remaining: $(1/2)^3 = 1/8 = 12.5\\%$.</p><p class="step">Sanity: after three half-lives, most activity has decayed.</p><p><strong>$12.5\\%$ of the original activity remains.</strong></p>',
        },
        {
            "topic": '§2 Matter Waves & Nuclear Review',
            "problem": 'An electron is confined to a quantum dot of width $L = 6.0\\,\\text{nm}$. How many bound states have energy below $0.50\\,\\text{eV}$?',
            "solution": '<p class="step">$E_n = n^2 h^2/(8m_e L^2)$. With $L = 6.0\\,\\text{nm}$: $E_1 = 0.010\\,\\text{eV}$.</p><p class="step">$E_2 = 4 E_1 = 0.040\\,\\text{eV}$; $E_3 = 0.090\\,\\text{eV}$; $E_4 = 0.16\\,\\text{eV}$; $E_5 = 0.25\\,\\text{eV}$; $E_6 = 0.36\\,\\text{eV}$; $E_7 = 0.49\\,\\text{eV}$; $E_8 = 0.64\\,\\text{eV}$.</p><p class="step">States with $E_n < 0.50\\,\\text{eV}$: $n = 1$ through $7$.</p><p><strong>Seven bound states ($n = 1$ to $7$).</strong></p>',
        },
        {
            "topic": '§3 Mixed Modern Physics',
            "problem": 'A photon of wavelength $\\lambda = 200\\,\\text{nm}$ ejects an electron from a metal with $KE = 1.5\\,\\text{eV}$. The same metal is then used in a TEM at $100\\,\\text{kV}$. Compare the de Broglie wavelength of the TEM electron to the photon wavelength.',
            "solution": '<p class="step">Photon energy: $E = 1240/200 = 6.2\\,\\text{eV}$; work function $\\phi = 6.2 - 1.5 = 4.7\\,\\text{eV}$.</p><p class="step">TEM electron: $\\lambda_e = 1.226/\\sqrt{100000}\\,\\text{nm} = 0.0039\\,\\text{nm}$.</p><p class="step">Ratio: $\\lambda_{\\text{photon}}/\\lambda_e = 200/0.0039 \\approx 5\\times 10^4$.</p><p class="step">TEM electrons have vastly shorter wavelengths, enabling atomic-resolution imaging.</p><p><strong>TEM $\\lambda_e \\approx 0.0039\\,\\text{nm}$; about $5\\times 10^4$ times shorter than the UV photon.</strong></p>',
        },
        {
            "topic": '§3 Mixed Modern Physics',
            "problem": 'Using $E = mc^2$, find the energy equivalent of $1.0\\,\\text{g}$ of matter. How many $500\\,\\text{MW}$ power-plant hours does this represent?',
            "solution": '<p class="step">$E = mc^2 = 10^{-3}\\times (3\\times 10^8)^2 = 9\\times 10^{13}\\,\\text{J}$.</p><p class="step">Plant output: $500\\,\\text{MW} = 5\\times 10^8\\,\\text{W}$.</p><p class="step">Time: $t = 9\\times 10^{13}/(5\\times 10^8) = 1.8\\times 10^5\\,\\text{s} = 50\\,\\text{h}$.</p><p class="step">Sanity: a gram of mass-energy is enormous — this underpins nuclear power.</p><p><strong>$E = 9\\times 10^{13}\\,\\text{J}$; equivalent to $\\approx 50$ hours at $500\\,\\text{MW}$.</strong></p>',
        },
        {
            "topic": '§3 Mixed Modern Physics',
            "problem": 'Rank the de Broglie wavelengths at room temperature ($k_B T \\approx 0.025\\,\\text{eV}$) for: (a) a thermal neutron, (b) a thermal electron, (c) a dust grain ($m = 10^{-15}\\,\\text{kg}$, $v = 1\\,\\text{mm/s}$). Which shows quantum behaviour most readily?',
            "solution": '<p class="step">(a) Neutron: $\\lambda \\sim h/\\sqrt{2\\pi m k_B T} \\approx 0.2\\,\\text{nm}$ (similar to thermal neutron above).</p><p class="step">(b) Electron at $0.025\\,\\text{eV}$: $\\lambda \\sim 2\\,\\text{nm}$ — longest of the three.</p><p class="step">(c) Dust: $\\lambda = h/(mv) = 6.6\\times 10^{-34}/(10^{-15}\\times 10^{-3}) = 6.6\\times 10^{-16}\\,\\text{m}$ — negligible.</p><p class="step">Thermal electron has the longest $\\lambda$ and most readily exhibits wave behaviour.</p><p><strong>Ranking: electron $>$ neutron $\\gg$ dust grain; thermal electrons show quantum effects most readily.</strong></p>',
        },
    ],
    10: [
        {
            "topic": '§0 Harmonic Waves',
            "problem": 'A harmonic wave on a power-line cable is described by $y(x,t) = 0.03\\sin(4.0x - 1200t)$, with $x$ and $y$ in metres and $t$ in seconds. Find the amplitude, wavelength, frequency, and wave speed.',
            "solution": '<p class="step">$A = 0.03\\,\\text{m}$, $k = 4.0\\,\\text{rad/m}$, $\\omega = 1200\\,\\text{rad/s}$.</p><p class="step">$\\lambda = 2\\pi/k = 2\\pi/4.0 = 1.57\\,\\text{m}$.</p><p class="step">$f = \\omega/(2\\pi) = 1200/(2\\pi) = 191\\,\\text{Hz}$.</p><p class="step">$v = \\omega/k = 1200/4.0 = 300\\,\\text{m/s}$.</p><p class="step">Sanity: $v = f\\lambda = 191\\times 1.57 \\approx 300\\,\\text{m/s}$, consistent.</p><p><strong>$A = 3.0\\,\\text{cm}$; $\\lambda = 1.57\\,\\text{m}$; $f = 191\\,\\text{Hz}$; $v = 300\\,\\text{m/s}$.</strong></p>',
        },
        {
            "topic": '§0 Harmonic Waves',
            "problem": 'A steel wire ($\\mu = 0.80\\,\\text{kg/m}$) in a suspension bridge is under tension $T = 2.0\\times 10^5\\,\\text{N}$. Find the speed of transverse waves and the wavelength of a $50\\,\\text{Hz}$ vibration.',
            "solution": '<p class="step">$v = \\sqrt{T/\\mu} = \\sqrt{2.0\\times 10^5/0.80} = \\sqrt{2.5\\times 10^5} = 500\\,\\text{m/s}$.</p><p class="step">$\\lambda = v/f = 500/50 = 10\\,\\text{m}$.</p><p class="step">Sanity: high tension and moderate mass density give hundreds of m/s — typical for bridge cables.</p><p><strong>$v = 500\\,\\text{m/s}$; $\\lambda = 10\\,\\text{m}$ at $50\\,\\text{Hz}$.</strong></p>',
        },
        {
            "topic": '§0 Harmonic Waves',
            "problem": 'A sound wave in air at $20^\\circ\\text{C}$ has frequency $1.0\\,\\text{kHz}$ and pressure amplitude $\\Delta p = 2.0\\,\\text{Pa}$. Given $v_{\\text{sound}} = 343\\,\\text{m/s}$ and $\\rho = 1.2\\,\\text{kg/m}^3$, find the wavelength and intensity ($I = \\Delta p^2/(2\\rho v)$).',
            "solution": '<p class="step">$\\lambda = v/f = 343/1000 = 0.343\\,\\text{m}$.</p><p class="step">$I = (2.0)^2/(2\\times 1.2\\times 343) = 4.0/823 = 4.9\\times 10^{-3}\\,\\text{W/m}^2$.</p><p class="step">Sanity: conversational speech is $\\sim 10^{-5}$ to $10^{-3}\\,\\text{W/m}^2$; this is moderately loud.</p><p><strong>$\\lambda = 0.34\\,\\text{m}$; $I \\approx 4.9\\,\\text{mW/m}^2$.</strong></p>',
        },
        {
            "topic": '§0 Harmonic Waves',
            "problem": 'At $t = 0$, a wave pulse on a water channel has the form $y(x,0) = A\\cos(kx)$ with $A = 0.05\\,\\text{m}$ and $k = 2.0\\,\\text{rad/m}$. Write the full travelling-wave equation $y(x,t)$ if the pulse moves in the $+x$ direction at $2.5\\,\\text{m/s}$.',
            "solution": '<p class="step">$v = \\omega/k \\Rightarrow \\omega = vk = 2.5\\times 2.0 = 5.0\\,\\text{rad/s}$.</p><p class="step">Travelling wave in $+x$: $y(x,t) = A\\cos(kx - \\omega t)$.</p><p class="step">$y(x,t) = 0.05\\cos(2.0x - 5.0t)$.</p><p class="step">Check at $t=0$: $y = 0.05\\cos(2x)$, as required.</p><p><strong>$y(x,t) = 0.05\\cos(2.0x - 5.0t)$.</strong></p>',
        },
        {
            "topic": '§1 Standing Waves',
            "problem": 'A $3.0\\,\\text{m}$ aluminium rod clamped at both ends resonates in its third harmonic. If the longitudinal wave speed in aluminium is $6.4\\,\\text{km/s}$, find the resonant frequency.',
            "solution": '<p class="step">Third harmonic ($n=3$): $L = 3\\lambda/2 \\Rightarrow \\lambda = 2L/3 = 2.0\\,\\text{m}$.</p><p class="step">$f_3 = v/\\lambda = 6400/2.0 = 3200\\,\\text{Hz}$.</p><p class="step">Alternatively: $f_n = nv/(2L) = 3\\times 6400/6 = 3200\\,\\text{Hz}$.</p><p><strong>$f_3 = 3.2\\,\\text{kHz}$.</strong></p>',
        },
        {
            "topic": '§1 Standing Waves',
            "problem": 'Two waves $y_1 = 0.04\\sin(kx - \\omega t)$ and $y_2 = 0.04\\sin(kx + \\omega t)$ superpose on a fixed-end string. Find the standing-wave amplitude envelope and the positions of the first node beyond $x=0$.',
            "solution": '<p class="step">Using sum-to-product: $y = 0.08\\sin(kx)\\cos(\\omega t)$.</p><p class="step">Amplitude envelope: $0.08|\\sin(kx)|$.</p><p class="step">Nodes where $\\sin(kx) = 0$: $kx = n\\pi$, so $x = n\\lambda/2$.</p><p class="step">First node beyond $x=0$: $x = \\lambda/2$.</p><p><strong>Standing wave $y = 0.08\\sin(kx)\\cos(\\omega t)$; first node at $x = \\lambda/2$.</strong></p>',
        },
        {
            "topic": '§1 Standing Waves',
            "problem": 'An open-open organ pipe (both ends open) has length $0.85\\,\\text{m}$. Find the frequencies of the first three harmonics. ($v_{\\text{sound}} = 343\\,\\text{m/s}$)',
            "solution": '<p class="step">Open pipe: $f_n = nv/(2L)$, $n = 1,2,3,\\ldots$</p><p class="step">$f_1 = 343/(2\\times 0.85) = 202\\,\\text{Hz}$.</p><p class="step">$f_2 = 404\\,\\text{Hz}$; $f_3 = 605\\,\\text{Hz}$.</p><p class="step">All harmonics present (unlike closed pipe).</p><p><strong>$f_1 = 202\\,\\text{Hz}$, $f_2 = 404\\,\\text{Hz}$, $f_3 = 605\\,\\text{Hz}$.</strong></p>',
        },
        {
            "topic": '§2 Beats & Doppler',
            "problem": 'Two tuning forks in an acoustics lab produce frequencies $440.0\\,\\text{Hz}$ and $443.0\\,\\text{Hz}$. Find the beat frequency and the time between successive volume maxima.',
            "solution": '<p class="step">$f_{\\text{beat}} = |443.0 - 440.0| = 3.0\\,\\text{Hz}$.</p><p class="step">Period between maxima: $T = 1/f_{\\text{beat}} = 0.33\\,\\text{s}$.</p><p class="step">Sanity: small frequency difference gives slow, audible beats.</p><p><strong>Beat frequency $= 3.0\\,\\text{Hz}$; maxima every $0.33\\,\\text{s}$.</strong></p>',
        },
        {
            "topic": '§2 Beats & Doppler',
            "problem": 'A police radar gun transmits at $24.15\\,\\text{GHz}$. A car approaching at $110\\,\\text{km/h}$ reflects the signal. Find the frequency shift (Doppler). ($c = 3.00\\times 10^8\\,\\text{m/s}$)',
            "solution": '<p class="step">For electromagnetic Doppler (moving source and observer): $\\Delta f/f \\approx 2v/c$ for reflection.</p><p class="step">$v = 110/3.6 = 30.6\\,\\text{m/s}$.</p><p class="step">$\\Delta f = 2v f/c = 2\\times 30.6\\times 24.15\\times 10^9/(3.00\\times 10^8) = 4.93\\,\\text{kHz}$.</p><p class="step">Sanity: typical radar shifts are in the kHz range for highway speeds.</p><p><strong>Frequency shift $\\Delta f \\approx 4.9\\,\\text{kHz}$.</strong></p>',
        },
        {
            "topic": '§2 Beats & Doppler',
            "problem": 'An ambulance siren emits $800\\,\\text{Hz}$. It approaches a stationary observer at $25\\,\\text{m/s}$, then recedes at the same speed. Find the observed frequencies in each case. ($v_{\\text{sound}} = 343\\,\\text{m/s}$)',
            "solution": '<p class="step">Approaching: $f\' = f \\cdot v/(v - v_s) = 800\\times 343/(343-25) = 800\\times 1.079 = 863\\,\\text{Hz}$.</p><p class="step">Receding: $f\' = 800\\times 343/(343+25) = 800\\times 0.932 = 746\\,\\text{Hz}$.</p><p class="step">Difference: $863 - 746 = 117\\,\\text{Hz}$ — the classic passing effect.</p><p><strong>Approaching: $863\\,\\text{Hz}$; receding: $746\\,\\text{Hz}$.</strong></p>',
        },
        {
            "topic": '§2 Beats & Doppler',
            "problem": 'A conveyor-belt sensor moves toward a fixed ultrasonic transmitter at $5.0\\,\\text{m/s}$. The transmitter emits $40\\,\\text{kHz}$. Find the frequency received by the sensor. ($v_{\\text{sound}} = 343\\,\\text{m/s}$)',
            "solution": '<p class="step">Moving observer toward stationary source: $f\' = f(v + v_o)/v$.</p><p class="step">$f\' = 40000\\times (343+5)/343 = 40000\\times 1.0146 = 40585\\,\\text{Hz}$.</p><p class="step">Sanity: observer moving toward source hears higher pitch.</p><p><strong>Observed frequency $\\approx 40.6\\,\\text{kHz}$.</strong></p>',
        },
        {
            "topic": '§3 Dispersion & Wave Packets',
            "problem": 'In a non-dispersive medium, $v_p = 200\\,\\text{m/s}$ for all frequencies. A wave packet has group velocity $v_g$. What is $v_g$, and does the packet maintain its shape?',
            "solution": '<p class="step">Non-dispersive: $v_g = v_p = 200\\,\\text{m/s}$ for all components.</p><p class="step">Since all frequency components travel at the same speed, the packet maintains its shape.</p><p class="step">This is the ideal case for signal transmission (e.g. light in vacuum).</p><p><strong>$v_g = 200\\,\\text{m/s} = v_p$; the packet retains its shape.</strong></p>',
        },
        {
            "topic": '§3 Dispersion & Wave Packets',
            "problem": 'In a dispersive optical fibre, $\\omega = c k / n_0 + \\alpha k^2$ with $\\alpha = 2.0\\times 10^{-15}\\,\\text{m}^2/\\text{s}$ and $n_0 = 1.47$. Find $v_p$ and $v_g$ at $k = 8.0\\times 10^6\\,\\text{rad/m}$.',
            "solution": '<p class="step">$v_p = \\omega/k = c/n_0 + \\alpha k = 3\\times 10^8/1.47 + 2.0\\times 10^{-15}\\times 8.0\\times 10^6$.</p><p class="step">$v_p = 2.04\\times 10^8 + 1.6\\times 10^{-8} \\approx 2.04\\times 10^8\\,\\text{m/s}$.</p><p class="step">$v_g = d\\omega/dk = c/n_0 + 2\\alpha k = 2.04\\times 10^8 + 3.2\\times 10^{-8} \\approx 2.04\\times 10^8\\,\\text{m/s}$.</p><p class="step">$v_g < v_p$ when dispersion term is positive (normal dispersion).</p><p><strong>$v_p \\approx v_g \\approx 2.04\\times 10^8\\,\\text{m/s}$; slight dispersion from $\\alpha k^2$ term.</strong></p>',
        },
        {
            "topic": '§3 Dispersion & Wave Packets',
            "problem": 'A Gaussian wave packet of initial width $\\Delta x_0 = 1.0\\,\\mu\\text{m}$ in a dispersive medium spreads according to $\\Delta x(t) = \\Delta x_0\\sqrt{1 + (t/\\tau)^2}$ with $\\tau = 0.50\\,\\text{ns}$. Find the packet width after $t = 1.0\\,\\text{ns}$.',
            "solution": '<p class="step">$\\Delta x = 1.0\\sqrt{1 + (1.0/0.50)^2} = 1.0\\sqrt{1+4} = \\sqrt{5}\\,\\mu\\text{m} = 2.24\\,\\mu\\text{m}$.</p><p class="step">Spreading factor: $\\sqrt{5} \\approx 2.2$ — significant broadening after $2\\tau$.</p><p class="step">This limits the distance over which a short optical pulse can carry information without distortion.</p><p><strong>$\\Delta x \\approx 2.2\\,\\mu\\text{m}$ after $1.0\\,\\text{ns}$.</strong></p>',
        },
    ],
    11: [
        {
            "topic": '§0 Snell & Huygens',
            "problem": 'A laser beam in a surveying instrument enters a glass prism ($n = 1.52$) from air at incidence angle $35^\\circ$. Find the angle of refraction inside the glass.',
            "solution": '<p class="step">Snell\'s law: $n_1\\sin\\theta_1 = n_2\\sin\\theta_2$.</p><p class="step">$\\sin\\theta_2 = \\sin 35^\\circ/1.52 = 0.574/1.52 = 0.378$.</p><p class="step">$\\theta_2 = \\arcsin(0.378) = 22.2^\\circ$.</p><p class="step">Ray bends toward the normal entering denser medium.</p><p><strong>Refracted angle $\\theta_2 = 22^\\circ$ inside the glass.</strong></p>',
        },
        {
            "topic": '§0 Snell & Huygens',
            "problem": 'Light travels from water ($n = 1.33$) into crown glass ($n = 1.52$) at $40^\\circ$ to the normal. Find the refracted angle and state whether the ray speeds up or slows down.',
            "solution": '<p class="step">$\\sin\\theta_2 = n_1\\sin\\theta_1/n_2 = 1.33\\sin 40^\\circ/1.52 = 1.33\\times 0.643/1.52 = 0.563$.</p><p class="step">$\\theta_2 = 34.2^\\circ$.</p><p class="step">Speed $v = c/n$: higher $n$ means slower speed. The ray slows down in glass.</p><p><strong>$\\theta_2 = 34^\\circ$; the ray slows down ($v_{\\text{glass}} < v_{\\text{water}}$).</strong></p>',
        },
        {
            "topic": '§0 Snell & Huygens',
            "problem": "Using Huygens' principle, explain why a plane wavefront bends toward the normal when entering a denser medium from air.",
            "solution": '<p class="step">Each point on the wavefront acts as a secondary source of spherical wavelets.</p><p class="step">In the denser medium, wavelets travel slower ($v = c/n$, smaller $v$).</p><p class="step">The envelope of wavelets in the denser medium lags behind, bending the overall wavefront toward the normal.</p><p class="step">This geometric argument gives the same result as Snell\'s law.</p><p><strong>Slower wavelet speed in denser medium bends the wavefront toward the normal (Snell\'s law).</strong></p>',
        },
        {
            "topic": '§1 TIR & Fibre Optics',
            "problem": 'A silica optical fibre has core index $n_1 = 1.46$ and cladding $n_2 = 1.45$. Find the critical angle for total internal reflection at the core–cladding boundary.',
            "solution": '<p class="step">$\\sin\\theta_c = n_2/n_1 = 1.45/1.46 = 0.993$.</p><p class="step">$\\theta_c = \\arcsin(0.993) = 83.2^\\circ$.</p><p class="step">Light must strike the boundary at $\\theta > 83^\\circ$ (measured from normal inside core) for TIR.</p><p class="step">Small index difference gives a large critical angle — typical for multimode fibre.</p><p><strong>$\\theta_c = 83^\\circ$ (measured from normal in the core).</strong></p>',
        },
        {
            "topic": '§1 TIR & Fibre Optics',
            "problem": 'For the fibre above ($n_1 = 1.46$, $n_2 = 1.45$), find the numerical aperture and the maximum acceptance half-angle in air.',
            "solution": '<p class="step">$\\text{NA} = \\sqrt{n_1^2 - n_2^2} = \\sqrt{1.46^2 - 1.45^2} = \\sqrt{0.0291} = 0.171$.</p><p class="step">Acceptance angle in air: $\\sin\\theta_{\\max} = \\text{NA} = 0.171$.</p><p class="step">$\\theta_{\\max} = 9.8^\\circ$.</p><p class="step">Sanity: small NA means the fibre accepts only near-axial rays.</p><p><strong>NA $= 0.17$; acceptance half-angle $\\approx 9.8^\\circ$.</strong></p>',
        },
        {
            "topic": '§1 TIR & Fibre Optics',
            "problem": 'A submarine communication cable uses fibre with attenuation $0.20\\,\\text{dB/km}$. If the transmitter launches $10\\,\\text{mW}$ and the receiver needs at least $1.0\\,\\mu\\text{W}$, what is the maximum cable length?',
            "solution": '<p class="step">Required loss: $10\\log_{10}(10\\times 10^{-3}/(1.0\\times 10^{-6})) = 10\\log_{10}(10^4) = 40\\,\\text{dB}$.</p><p class="step">Length: $L = 40/0.20 = 200\\,\\text{km}$.</p><p class="step">Sanity: modern fibres with amplifiers span thousands of km; this is a single unrepeated span.</p><p><strong>Maximum unrepeated length $\\approx 200\\,\\text{km}$.</strong></p>',
        },
        {
            "topic": '§2 Dispersion & Fermat',
            "problem": 'White light enters a flint-glass prism ($n_v = 1.66$ for violet, $n_r = 1.60$ for red) at $50^\\circ$. Find the angular dispersion between red and violet emerging rays (use small-angle approximation for the exit deviation).',
            "solution": '<p class="step">Violet inside: $\\sin\\theta_v = \\sin 50^\\circ/1.66 = 0.461$, $\\theta_v = 27.5^\\circ$.</p><p class="step">Red inside: $\\sin\\theta_r = 0.766/1.60 = 0.479$, $\\theta_r = 28.6^\\circ$.</p><p class="step">Exit deviation difference (approximate): $\\delta_v - \\delta_r \\approx (n_v - n_r)\\times$ (geometry factor) $\\approx 0.06\\times 50^\\circ \\approx 3^\\circ$.</p><p class="step">More precisely, minimum deviation gives $\\Delta\\delta \\approx 2^\\circ$–$4^\\circ$ for this prism — violet bends more.</p><p><strong>Angular dispersion $\\approx 3^\\circ$–$4^\\circ$ (violet deviated more than red).</strong></p>',
        },
        {
            "topic": '§2 Dispersion & Fermat',
            "problem": "Fermat's principle states light follows the path of least time. Derive qualitatively why a ray entering a denser medium bends toward the normal.",
            "solution": '<p class="step">Light travels slower in the denser medium ($v = c/n$, lower $v$).</p><p class="step">A straight-line path would spend too long in the slow medium if it did not bend.</p><p class="step">Bending toward the normal shortens the path in the slow region and lengthens it in the fast region.</p><p class="step">The time-minimising path is exactly Snell\'s law: $n_1\\sin\\theta_1 = n_2\\sin\\theta_2$.</p><p><strong>Bending toward the normal minimises transit time through the slower medium (Fermat $\\Rightarrow$ Snell).</strong></p>',
        },
        {
            "topic": '§2 Dispersion & Fermat',
            "problem": 'A camera lens made of crown glass ($n = 1.52$) exhibits chromatic aberration: red and blue images form at different focal points separated by $2.5\\,\\text{mm}$. If the mean focal length is $50\\,\\text{mm}$, estimate the difference in refractive index $\\Delta n$ between the two wavelengths.',
            "solution": '<p class="step">Thin-lens approximation: $1/f = (n-1)(1/R_1 - 1/R_2)$.</p><p class="step">$\\Delta f/f^2 \\approx -(1/R_1 - 1/R_2)\\Delta n = -\\Delta n/(n-1) \\times 1/f$.</p><p class="step">$\\Delta n \\approx (n-1)\\times\\Delta f/f = 0.52\\times 2.5/50 = 0.026$.</p><p class="step">Sanity: typical crown glass has $\\Delta n \\sim 0.01$–$0.03$ across the visible spectrum.</p><p><strong>$\\Delta n \\approx 0.026$ (typical for crown glass dispersion).</strong></p>',
        },
        {
            "topic": '§3 Polarisation',
            "problem": 'Polarised sunglasses reduce glare from a horizontal road surface. At what Brewster angle does sunlight reflected from water ($n = 1.33$) become fully polarised?',
            "solution": '<p class="step">$\\tan\\theta_B = n_2/n_1 = 1.33/1.00 = 1.33$.</p><p class="step">$\\theta_B = \\arctan(1.33) = 53.1^\\circ$.</p><p class="step">At this angle, reflected light is entirely polarised parallel to the surface.</p><p class="step">Vertical polarisers block this component, reducing glare.</p><p><strong>Brewster angle $\\theta_B = 53^\\circ$ from the normal.</strong></p>',
        },
        {
            "topic": '§3 Polarisation',
            "problem": 'Unpolarised light of intensity $I_0 = 800\\,\\text{W/m}^2$ passes through a polariser, then a second polariser at $60^\\circ$ to the first. Find the transmitted intensity.',
            "solution": '<p class="step">After first polariser: $I_1 = I_0/2 = 400\\,\\text{W/m}^2$.</p><p class="step">Malus\'s law: $I_2 = I_1\\cos^2 60^\\circ = 400\\times (1/2)^2 = 400\\times 0.25 = 100\\,\\text{W/m}^2$.</p><p class="step">Sanity: $60^\\circ$ between polarisers transmits $1/4$ of the polarised intensity.</p><p><strong>Transmitted intensity $= 100\\,\\text{W/m}^2$.</strong></p>',
        },
        {
            "topic": '§3 Polarisation',
            "problem": 'An LCD display uses a liquid-crystal cell between crossed polarisers. With no applied voltage, the cell rotates polarisation by $90^\\circ$ and the display is bright. With voltage applied, rotation is removed. Explain why the pixel goes dark.',
            "solution": '<p class="step">Crossed polarisers alone block all light (Malus: $\\cos^2 90^\\circ = 0$).</p><p class="step">With no voltage, the LC layer rotates the polarisation by $90^\\circ$, aligning it with the second polariser — light passes (bright pixel).</p><p class="step">With voltage, the LC molecules align with the field and no longer rotate polarisation; light remains blocked by the crossed analyser.</p><p class="step">This is the basis of every LCD pixel.</p><p><strong>Without voltage, LC rotates polarisation to pass the analyser (bright); with voltage, crossed polarisers block light (dark).</strong></p>',
        },
    ],
    12: [
        {
            "topic": '§0 Mirrors',
            "problem": 'A concave security mirror has radius of curvature $R = 2.4\\,\\text{m}$. An object is placed $1.5\\,\\text{m}$ in front of it. Find the image distance, magnification, and state whether the image is real or virtual.',
            "solution": '<p class="step">$f = R/2 = 1.2\\,\\text{m}$ (concave: $f > 0$).</p><p class="step">$1/d_i = 1/f - 1/d_o = 1/1.2 - 1/1.5 = 0.833 - 0.667 = 0.167$.</p><p class="step">$d_i = 6.0\\,\\text{m}$ (positive $\\Rightarrow$ real image).</p><p class="step">$m = -d_i/d_o = -6.0/1.5 = -4.0$ (inverted, magnified).</p><p><strong>Real image at $6.0\\,\\text{m}$; $m = -4.0$ (inverted, $4\\times$ magnified).</strong></p>',
        },
        {
            "topic": '§0 Mirrors',
            "problem": 'A plane mirror is mounted vertically in a factory inspection booth. A worker stands $2.0\\,\\text{m}$ in front of it. How far behind the mirror is the image, and how far is the worker from their image?',
            "solution": '<p class="step">Plane mirror: $d_i = -d_o = -2.0\\,\\text{m}$ (virtual image behind mirror).</p><p class="step">Object-to-image distance: $2.0 + 2.0 = 4.0\\,\\text{m}$.</p><p class="step">Magnification $m = +1$ (same size, upright).</p><p><strong>Image $2.0\\,\\text{m}$ behind mirror; total separation $4.0\\,\\text{m}$.</strong></p>',
        },
        {
            "topic": '§0 Mirrors',
            "problem": 'A convex rear-view mirror has $f = -0.80\\,\\text{m}$. A car $6.0\\,\\text{m}$ behind is imaged. Find $d_i$ and $m$. Why is the image useful despite being diminished?',
            "solution": '<p class="step">$1/d_i = 1/f - 1/d_o = 1/(-0.80) - 1/6.0 = -1.25 - 0.167 = -1.417$.</p><p class="step">$d_i = -0.71\\,\\text{m}$ (virtual, behind mirror).</p><p class="step">$m = -d_i/d_o = -(-0.71)/6.0 = +0.12$ (upright, greatly diminished).</p><p class="step">Wide field of view: diminished image shows more of the road behind.</p><p><strong>Virtual image at $0.71\\,\\text{m}$ behind mirror; $m = +0.12$; wide field of view.</strong></p>',
        },
        {
            "topic": '§1 Thin Lenses',
            "problem": 'A converging lens ($f = 0.25\\,\\text{m}$) is used to focus a laser diode onto a fibre coupler. The diode is $0.40\\,\\text{m}$ from the lens. Where is the focused spot?',
            "solution": '<p class="step">$1/d_i = 1/f - 1/d_o = 1/0.25 - 1/0.40 = 4.0 - 2.5 = 1.5$.</p><p class="step">$d_i = 0.667\\,\\text{m}$ on the far side of the lens.</p><p class="step">$m = -0.667/0.40 = -1.67$ (inverted, magnified).</p><p><strong>Focused spot at $0.67\\,\\text{m}$ beyond the lens.</strong></p>',
        },
        {
            "topic": '§1 Thin Lenses',
            "problem": 'Two thin lenses ($f_1 = +0.20\\,\\text{m}$, $f_2 = -0.15\\,\\text{m}$) are separated by $0.10\\,\\text{m}$. An object is placed $0.30\\,\\text{m}$ before lens 1. Find the position of the final image.',
            "solution": '<p class="step">Lens 1: $1/d_{i1} = 1/0.20 - 1/0.30 = 1.667$, $d_{i1} = 0.60\\,\\text{m}$.</p><p class="step">Object for lens 2 is $0.10\\,\\text{m}$ to the right of lens 1, so $d_{o2} = -(0.60 - 0.10) = -0.50\\,\\text{m}$ (virtual object).</p><p class="step">Lens 2: $1/d_{i2} = 1/(-0.15) - 1/(-0.50) = -6.67 + 2.0 = -4.67$.</p><p class="step">$d_{i2} = -0.214\\,\\text{m}$ (virtual image, $0.21\\,\\text{m}$ to the left of lens 2).</p><p><strong>Final virtual image $0.21\\,\\text{m}$ to the left of lens 2.</strong></p>',
        },
        {
            "topic": '§1 Thin Lenses',
            "problem": 'A biconvex lens has radii $R_1 = +0.15\\,\\text{m}$ and $R_2 = -0.20\\,\\text{m}$ in glass ($n = 1.50$). Using the lensmaker equation, find the focal length in air.',
            "solution": '<p class="step">$\\dfrac{1}{f} = (n-1)\\left(\\dfrac{1}{R_1} - \\dfrac{1}{R_2}\\right) = 0.50\\left(\\dfrac{1}{0.15} - \\dfrac{1}{-0.20}\\right)$.</p><p class="step">$= 0.50(6.667 + 5.0) = 0.50\\times 11.667 = 5.833$.</p><p class="step">$f = 0.171\\,\\text{m} = 17.1\\,\\text{cm}$.</p><p><strong>$f = 17\\,\\text{cm}$ (converging).</strong></p>',
        },
        {
            "topic": '§2 Eye & Magnifier',
            "problem": 'A student with a near point at $25\\,\\text{cm}$ uses a magnifier of focal length $f = 5.0\\,\\text{cm}$ with the image at the near point. Find the angular magnification.',
            "solution": '<p class="step">With image at near point: $M = 1 + 25/f = 1 + 25/5.0 = 6.0$.</p><p class="step">Object distance: $1/d_o = 1/f - 1/d_i = 1/5 - 1/25 = 0.20 - 0.04 = 0.16$, $d_o = 6.25\\,\\text{cm}$.</p><p class="step">Sanity: shorter focal length gives greater magnification.</p><p><strong>Angular magnification $M = 6.0$.</strong></p>',
        },
        {
            "topic": '§2 Eye & Magnifier',
            "problem": 'A myopic (short-sighted) person has a far point at $1.5\\,\\text{m}$. What power corrective lens allows clear vision of distant objects?',
            "solution": '<p class="step">Need virtual image at far point: $d_i = -1.5\\,\\text{m}$ for object at infinity ($d_o = \\infty$).</p><p class="step">$1/f = 1/d_i = 1/(-1.5) = -0.667\\,\\text{dioptres}$.</p><p class="step">Power $P = -0.67\\,\\text{D}$ (diverging lens).</p><p class="step">Sanity: myopia requires negative (concave) lenses.</p><p><strong>Corrective lens power $P = -0.67\\,\\text{D}$ (diverging).</strong></p>',
        },
        {
            "topic": '§2 Eye & Magnifier',
            "problem": 'The relaxed eye has a near point of $25\\,\\text{cm}$. A magnifier with $f = 8.0\\,\\text{cm}$ is used with the image at infinity. Find the magnification and the object distance.',
            "solution": '<p class="step">Image at infinity: $M = 25/f = 25/8.0 = 3.1$.</p><p class="step">Object at focal point: $d_o = f = 8.0\\,\\text{cm}$.</p><p class="step">This configuration gives the least eye strain for extended viewing.</p><p><strong>$M = 3.1$; object placed at $8.0\\,\\text{cm}$ (the focal point).</strong></p>',
        },
        {
            "topic": '§3 Microscope & Telescope',
            "problem": 'A compound microscope has objective $f_o = 4.0\\,\\text{mm}$, eyepiece $f_e = 25\\,\\text{mm}$, and tube length $L = 160\\,\\text{mm}$. Estimate the total magnification.',
            "solution": '<p class="step">$M \\approx (L/f_o)(25\\,\\text{cm}/f_e) = (160/4.0)(250/25) = 40\\times 10 = 400$.</p><p class="step">Sanity: typical lab microscopes give $100\\times$–$1000\\times$.</p><p><strong>Total magnification $\\approx 400\\times$.</strong></p>',
        },
        {
            "topic": '§3 Microscope & Telescope',
            "problem": 'An astronomical telescope has objective focal length $f_o = 1.20\\,\\text{m}$ and eyepiece $f_e = 3.0\\,\\text{cm}$. Find the angular magnification and the length of the telescope (relaxed eye).',
            "solution": '<p class="step">$M = f_o/f_e = 120/3.0 = 40$.</p><p class="step">Length (relaxed): $L = f_o + f_e = 120 + 3.0 = 123\\,\\text{cm}$.</p><p class="step">Sanity: amateur telescopes typically give $20\\times$–$100\\times$.</p><p><strong>$M = 40$; telescope length $\\approx 123\\,\\text{cm}$.</strong></p>',
        },
        {
            "topic": '§3 Microscope & Telescope',
            "problem": 'The Keck telescope has an effective aperture $D = 10\\,\\text{m}$. At $\\lambda = 550\\,\\text{nm}$, estimate the angular resolution (Rayleigh criterion) in arcseconds. ($1\\,\\text{rad} = 2.06\\times 10^5\\,\\text{arcsec}$)',
            "solution": '<p class="step">$\\theta_{\\min} = 1.22\\lambda/D = 1.22\\times 550\\times 10^{-9}/10 = 6.71\\times 10^{-8}\\,\\text{rad}$.</p><p class="step">$= 6.71\\times 10^{-8}\\times 2.06\\times 10^5 = 0.014\\,\\text{arcsec}$.</p><p class="step">Sanity: large aperture gives sub-arcsecond resolution — among the best on Earth.</p><p><strong>Angular resolution $\\approx 0.014\\,\\text{arcsec}$ at $550\\,\\text{nm}$.</strong></p>',
        },
    ],
    13: [
        {
            "topic": '§0 Thin-Film Interference',
            "problem": 'A thin oil film ($n = 1.45$) on a water puddle has thickness $t = 320\\,\\text{nm}$. Light reflects from the top (air–oil) and bottom (oil–water) surfaces. For which visible wavelength is constructive reflection expected (assume phase shift at top surface only)?',
            "solution": '<p class="step">Constructive (one phase reversal): $2nt = (m + \\tfrac{1}{2})\\lambda$.</p><p class="step">$\\lambda = 2nt/(m+\\tfrac{1}{2}) = 2\\times 1.45\\times 320/(m+\\tfrac{1}{2})$.</p><p class="step">$m=0$: $\\lambda = 928\\,\\text{nm}$ (IR); $m=1$: $\\lambda = 309\\,\\text{nm}$ (UV).</p><p class="step">$m=0$ gives the dominant visible/IR reflection; nearest visible: check $m=0$ gives $\\lambda = 928\\,\\text{nm}$.</p><p class="step">For $2nt = 928\\,\\text{nm}$: visible order requires $m=1$: $\\lambda = 928/2.5 = 371\\,\\text{nm}$ (near UV-violet).</p><p class="step">Sanity: thin films produce coloured reflections from specific wavelengths.</p><p><strong>Constructive at $\\lambda \\approx 370\\,\\text{nm}$ (violet) and $928\\,\\text{nm}$ (near-IR) for $m=1,0$.</strong></p>',
        },
        {
            "topic": '§0 Thin-Film Interference',
            "problem": 'An anti-reflection coating on a camera lens uses $\\text{MgF}_2$ ($n = 1.38$) on glass ($n = 1.52$). Find the minimum coating thickness for destructive reflection at $\\lambda = 550\\,\\text{nm}$ (phase shift at both interfaces, so destructive: $2nt = m\\lambda$).',
            "solution": '<p class="step">Minimum ($m=1$): $t = \\lambda/(2n) = 550/(2\\times 1.38) = 199\\,\\text{nm}$.</p><p class="step">Quarter-wave coating: $t = \\lambda/4n$ is the standard AR design.</p><p class="step">Sanity: coatings are a few hundred nanometres thick.</p><p><strong>Minimum thickness $t = 199\\,\\text{nm}$ ($\\approx\\,\\lambda/4n$).</strong></p>',
        },
        {
            "topic": '§0 Thin-Film Interference',
            "problem": 'A soap bubble ($n = 1.33$) has wall thickness $t = 450\\,\\text{nm}$. With a phase reversal at the outer surface only, find the wavelength for destructive reflection in the visible range.',
            "solution": '<p class="step">Destructive (one reversal): $2nt = m\\lambda$.</p><p class="step">$\\lambda = 2nt/m = 2\\times 1.33\\times 450/m = 1197/m\\,\\text{nm}$.</p><p class="step">$m=2$: $\\lambda = 599\\,\\text{nm}$ (yellow-green); $m=3$: $\\lambda = 399\\,\\text{nm}$ (violet).</p><p class="step">The bubble appears coloured where reflected wavelengths destructively cancel.</p><p><strong>Destructive reflection at $\\lambda \\approx 600\\,\\text{nm}$ (yellow-green) for $m=2$.</strong></p>',
        },
        {
            "topic": '§0 Thin-Film Interference',
            "problem": 'Two glass plates ($n = 1.50$) form an air wedge of angle $\\alpha = 2.0\\times 10^{-4}\\,\\text{rad}$. At what distance $x$ from the contact point is the first bright fringe observed in reflected light ($\\lambda = 600\\,\\text{nm}$, phase shift on one reflection)?',
            "solution": '<p class="step">Bright fringe: $2t = (m+\\tfrac{1}{2})\\lambda$ with $t = x\\tan\\alpha \\approx x\\alpha$.</p><p class="step">First bright ($m=0$): $2x\\alpha = \\lambda/2$.</p><p class="step">$x = \\lambda/(4\\alpha) = 600\\times 10^{-9}/(4\\times 2.0\\times 10^{-4}) = 7.5\\times 10^{-4}\\,\\text{m}$.</p><p class="step">$x = 0.75\\,\\text{mm}$ from contact.</p><p><strong>First bright fringe at $x = 0.75\\,\\text{mm}$ from contact.</strong></p>',
        },
        {
            "topic": "§1 Michelson & Young's Slit",
            "problem": "A Young's double-slit experiment uses slit separation $d = 0.25\\,\\text{mm}$ and screen distance $L = 2.0\\,\\text{m}$ with $\\lambda = 632\\,\\text{nm}$ (He–Ne laser). Find the fringe spacing.",
            "solution": '<p class="step">$\\Delta y = \\lambda L/d = 632\\times 10^{-9}\\times 2.0/(0.25\\times 10^{-3})$.</p><p class="step">$= 5.06\\times 10^{-3}\\,\\text{m} = 5.1\\,\\text{mm}$.</p><p class="step">Sanity: millimetre-scale fringes are typical for this geometry.</p><p><strong>Fringe spacing $\\Delta y = 5.1\\,\\text{mm}$.</strong></p>',
        },
        {
            "topic": "§1 Michelson & Young's Slit",
            "problem": 'In a Michelson interferometer, one mirror is moved by $\\Delta d = 15.8\\,\\mu\\text{m}$. How many fringes pass a fixed point for $\\lambda = 632\\,\\text{nm}$?',
            "solution": '<p class="step">$N = 2\\Delta d/\\lambda = 2\\times 15.8\\times 10^{-6}/(632\\times 10^{-9})$.</p><p class="step">$= 31.6\\times 10^{-6}/(632\\times 10^{-9}) = 50.0$.</p><p class="step">Sanity: moving a mirror by many wavelengths produces many fringe shifts.</p><p><strong>$N = 50$ fringes pass.</strong></p>',
        },
        {
            "topic": "§1 Michelson & Young's Slit",
            "problem": 'Two coherent sources separated by $d = 0.40\\,\\text{mm}$ emit $\\lambda = 500\\,\\text{nm}$. At what angle $\\theta$ is the third-order bright fringe ($m=3$)?',
            "solution": '<p class="step">$d\\sin\\theta = m\\lambda$.</p><p class="step">$\\sin\\theta = 3\\lambda/d = 3\\times 500\\times 10^{-9}/(0.40\\times 10^{-3}) = 0.00375$.</p><p class="step">$\\theta = \\arcsin(0.00375) = 0.215^\\circ = 12.9\\,\\text{arcmin}$.</p><p class="step">Small-angle: $\\theta \\approx m\\lambda/d = 0.00375\\,\\text{rad}$.</p><p><strong>Third bright fringe at $\\theta = 0.22^\\circ$ ($\\approx 13\\,\\text{arcmin}$).</strong></p>',
        },
        {
            "topic": '§2 Single-Slit & Resolution',
            "problem": 'Monochromatic light ($\\lambda = 550\\,\\text{nm}$) passes through a single slit of width $a = 0.08\\,\\text{mm}$. Find the angular width of the central maximum (full width to first dark fringes on each side).',
            "solution": '<p class="step">First dark fringe: $a\\sin\\theta = \\lambda$, so $\\sin\\theta_1 = \\lambda/a = 550\\times 10^{-9}/(0.08\\times 10^{-3}) = 0.006875$.</p><p class="step">$\\theta_1 = 0.394^\\circ$. Central maximum full width: $2\\theta_1 = 0.79^\\circ$.</p><p class="step">Small angle: width $\\approx 2\\lambda/a = 0.01375\\,\\text{rad} = 0.79^\\circ$.</p><p><strong>Central maximum angular width $\\approx 0.79^\\circ$ ($2\\lambda/a$).</strong></p>',
        },
        {
            "topic": '§2 Single-Slit & Resolution',
            "problem": "Two headlights $1.5\\,\\text{m}$ apart are viewed from $4.0\\,\\text{km}$ away. Can the human eye ($D = 5.0\\,\\text{mm}$ pupil, $\\lambda = 550\\,\\text{nm}$) resolve them? Use Rayleigh's criterion.",
            "solution": '<p class="step">Angular separation: $\\theta = 1.5/4000 = 3.75\\times 10^{-4}\\,\\text{rad}$.</p><p class="step">Rayleigh limit: $\\theta_{\\min} = 1.22\\lambda/D = 1.22\\times 550\\times 10^{-9}/(5.0\\times 10^{-3}) = 1.34\\times 10^{-4}\\,\\text{rad}$.</p><p class="step">$\\theta > \\theta_{\\min}$: the headlights are resolvable.</p><p class="step">Ratio: $3.75/1.34 \\approx 2.8$ — clearly separated.</p><p><strong>Yes — angular separation ($3.8\\times 10^{-4}\\,\\text{rad}$) exceeds Rayleigh limit ($1.3\\times 10^{-4}\\,\\text{rad}$).</strong></p>',
        },
        {
            "topic": '§2 Single-Slit & Resolution',
            "problem": 'A microscope objective has numerical aperture $\\text{NA} = 0.85$ and uses $\\lambda = 450\\,\\text{nm}$ light. Estimate the smallest resolvable separation (Abbe limit: $d_{\\min} = 0.61\\lambda/\\text{NA}$).',
            "solution": '<p class="step">$d_{\\min} = 0.61\\times 450\\times 10^{-9}/0.85 = 3.23\\times 10^{-7}\\,\\text{m}$.</p><p class="step">$= 323\\,\\text{nm}$.</p><p class="step">Sanity: high-NA objectives resolve sub-micrometre features.</p><p><strong>Minimum resolvable separation $\\approx 320\\,\\text{nm}$.</strong></p>',
        },
        {
            "topic": '§2 Single-Slit & Resolution',
            "problem": 'Light of $\\lambda = 600\\,\\text{nm}$ illuminates a slit $a = 0.12\\,\\text{mm}$ wide. On a screen $2.5\\,\\text{m}$ away, find the linear width of the central bright fringe.',
            "solution": '<p class="step">$\\theta_{\\min} = \\lambda/a = 600\\times 10^{-9}/(0.12\\times 10^{-3}) = 0.005\\,\\text{rad}$.</p><p class="step">Central width (full): $w = 2L\\tan\\theta \\approx 2L\\lambda/a = 2\\times 2.5\\times 0.005 = 0.025\\,\\text{m}$.</p><p class="step">$w = 25\\,\\text{mm}$.</p><p><strong>Central bright fringe width $= 25\\,\\text{mm}$ on the screen.</strong></p>',
        },
        {
            "topic": '§3 Diffraction Gratings',
            "problem": 'A diffraction grating has $600\\,\\text{lines/mm}$. Find the slit spacing $d$ and the angle of the first-order ($m=1$) maximum for $\\lambda = 589\\,\\text{nm}$ (sodium D-line).',
            "solution": '<p class="step">$d = 1/(600\\times 10^3) = 1.667\\times 10^{-6}\\,\\text{m}$.</p><p class="step">$d\\sin\\theta = m\\lambda$: $\\sin\\theta = 589\\times 10^{-9}/(1.667\\times 10^{-6}) = 0.353$.</p><p class="step">$\\theta = 20.7^\\circ$.</p><p><strong>$d = 1.67\\,\\mu\\text{m}$; first-order angle $\\theta = 21^\\circ$.</strong></p>',
        },
        {
            "topic": '§3 Diffraction Gratings',
            "problem": 'A grating with $500\\,\\text{lines/mm}$ is illuminated with white light ($400$–$700\\,\\text{nm}$). Over what angular range does the first-order spectrum span?',
            "solution": '<p class="step">$d = 2.0\\times 10^{-6}\\,\\text{m}$.</p><p class="step">$\\theta_{\\min} = \\arcsin(400\\times 10^{-9}/(2.0\\times 10^{-6})) = \\arcsin(0.200) = 11.5^\\circ$.</p><p class="step">$\\theta_{\\max} = \\arcsin(700\\times 10^{-9}/(2.0\\times 10^{-6})) = \\arcsin(0.350) = 20.5^\\circ$.</p><p class="step">First-order span: $\\approx 11.5^\\circ$ to $20.5^\\circ$ ($\\Delta\\theta \\approx 9^\\circ$).</p><p><strong>First-order spectrum spans $\\approx 11.5^\\circ$ to $20.5^\\circ$ ($\\Delta\\theta \\approx 9^\\circ$).</strong></p>',
        },
        {
            "topic": '§3 Diffraction Gratings',
            "problem": 'A spectrometer grating ($N = 10\\,000$ lines, $d = 2.0\\,\\mu\\text{m}$) resolves two sodium lines at $589.0\\,\\text{nm}$ and $589.6\\,\\text{nm}$ in second order ($m=2$). Show that the resolving power $R = mN$ is sufficient.',
            "solution": '<p class="step">$R = mN = 2\\times 10\\,000 = 20\\,000$.</p><p class="step">Required: $R = \\lambda/\\Delta\\lambda = 589.3/0.6 = 982$.</p><p class="step">$20\\,000 \\gg 982$: the grating easily resolves the sodium doublet.</p><p class="step">Sanity: large $N$ and higher order give excellent resolution.</p><p><strong>$R = 20\\,000 \\gg 982$ required; the doublet is easily resolved.</strong></p>',
        },
    ],
}
