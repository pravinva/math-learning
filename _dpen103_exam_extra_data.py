"""Extra exam questions Q11–Q20 for DPEN103 weeks 1–13."""

EXTRA = {}

# ---------------------------------------------------------------------------
# Week 1 — bonding, crystals, density, APF, FCC/BCC/HCP, design targets
# ---------------------------------------------------------------------------
EXTRA[1] = [
    {
        "tags": ("Multiple choice", "Quick"),
        "stem": "<p>Which row best describes covalent bonding in a ceramic such as silicon carbide?</p>",
        "options": [
            "Electrons are shared between specific atom pairs; the solid is hard, stiff and an electrical insulator",
            "Positive and negative ions attract; the solid conducts heat well but is brittle",
            "Delocalised electrons hold the lattice together; the solid is ductile and conducts electricity",
            "Weak secondary forces between molecules; the solid melts at low temperature",
        ],
        "answer": (
            "<b>Answer: A.</b> Covalent bonding shares electrons between neighbouring atoms in "
            "fixed directions, which gives very strong, directional bonds. The electrons are localised "
            "in those bonds, so conductivity is poor, and the locked directions give high stiffness "
            "with little plastic deformation. Option B is ionic, option C is metallic, option D is "
            "secondary bonding in polymers. <b>Design meaning:</b> a covalent ceramic is chosen "
            "when stiffness and hardness at high temperature matter more than toughness or conductivity."
        ),
    },
    {
        "tags": ("Multiple choice", "Quick"),
        "stem": "<p>Hexagonal close-packed (HCP) metals have which coordination number and atomic packing factor?</p>",
        "options": [
            "8 nearest neighbours, APF 0.68",
            "12 nearest neighbours, APF 0.74",
            "6 nearest neighbours, APF 0.52",
            "4 atoms per unit cell, APF 0.74",
        ],
        "answer": (
            "<b>Answer: B.</b> HCP is a close-packed structure with 12 nearest neighbours and "
            "APF 0.74, the same geometric packing as FCC. Option A is BCC, option C confuses "
            "coordination with a simple cubic arrangement, and option D mixes atoms per cell with "
            "packing factor. <b>Design meaning:</b> HCP shares the tight packing of FCC but "
            "offers fewer easy slip systems, which affects formability at room temperature."
        ),
    },
    {
        "tags": ("Multiple choice", "One step"),
        "stem": (
            "<p>An FCC metal has \\(A=63.55\\) g/mol and lattice parameter \\(a=0.361\\) nm. "
            "Using \\(N_A=6.022\\times10^{23}\\) mol\\(^{-1}\\), which density is closest?</p>"
        ),
        "options": [
            "2.2 g/cm³",
            "4.5 g/cm³",
            "8.9 g/cm³",
            "17.8 g/cm³",
        ],
        "answer": (
            "<b>Answer: C.</b> FCC has \\(n=4\\). Convert \\(a=0.361\\) nm \\(=3.61\\times10^{-8}\\) cm, "
            "so \\(V_c=a^3=4.71\\times10^{-23}\\) cm³. Mass per cell \\(=4(63.55)/(6.022\\times10^{23})"
            "=4.22\\times10^{-22}\\) g, giving \\(\\rho=8.96\\) g/cm³ — copper. "
            "<b>Sanity check:</b> copper is about 8.9 g/cm³, so the answer sits in the right band. "
            "Option A uses \\(n=1\\), option D uses \\(n=8\\). <b>Design meaning:</b> copper's density "
            "is three times aluminium's for the same volume, which matters in weight-sensitive "
            "conductors even when strength is adequate."
        ),
    },
    {
        "tags": ("Multiple choice", "Trap"),
        "stem": (
            "<p>Two metals are both close-packed with coordination number 12. Metal P is FCC and "
            "metal Q is HCP. A design brief requires deep drawing into a hemispherical dome at "
            "room temperature. Which statement is safest?</p>"
        ),
        "options": [
            "Either is equally suitable because both have APF 0.74",
            "P is the better choice because FCC offers more slip systems for plastic forming",
            "Q is the better choice because HCP packs atoms more efficiently along the draw axis",
            "Both will fail equally because close-packed structures cannot be formed",
        ],
        "answer": (
            "<b>Answer: B.</b> Identical packing fraction and coordination number describe geometry "
            "only. Formability depends on how many independent slip systems are available, and FCC "
            "metals typically offer more at room temperature. Magnesium and zinc (HCP) are harder "
            "to deep-draw than aluminium and copper (FCC) despite similar packing. "
            "<b>Design meaning:</b> when the brief says 'press' or 'draw', check crystal structure "
            "and slip, not just the numbers in the packing-factor table."
        ),
    },
    {
        "tags": ("True/false", "Quick"),
        "stem": "<p><b>True or false:</b> metallic bonding relies on a sea of delocalised electrons that carry both mechanical load transfer and electrical current.</p>",
        "answer": (
            "<b>Answer: True.</b> In a metal, valence electrons are shared across the whole lattice. "
            "They allow planes to slide while maintaining cohesion, and they move freely under an "
            "electric field. <b>Design meaning:</b> any part that must be both formed and earthed "
            "points straight at a metallic solid."
        ),
    },
    {
        "tags": ("True/false", "Trap"),
        "stem": (
            "<p><b>True or false:</b> once the crystal structure of a metal is known, its yield "
            "strength, electrical conductivity and corrosion resistance are fully determined.</p>"
        ),
        "answer": (
            "<b>Answer: False.</b> Structure fixes geometry — atoms per cell, packing factor, slip "
            "systems — but mechanical and environmental behaviour also depend on composition, "
            "grain size, defects and temperature. Two FCC metals, aluminium and gold, share a "
            "structure yet differ enormously in strength and chemistry. <b>Design meaning:</b> "
            "structure is a starting prediction, not a complete specification; always state the "
            "property targets you still need to verify."
        ),
    },
    {
        "tags": ("Short calculation", "Written"),
        "stem": (
            "<p>HCP titanium has \\(A=47.87\\) g/mol, \\(a=0.295\\) nm and \\(c=0.468\\) nm. The "
            "unit-cell volume is \\(V_c=\\tfrac{\\sqrt{3}}{2}a^2c\\). Find the theoretical density "
            "in g/cm³. HCP has \\(n=6\\) atoms per cell. Take \\(N_A=6.022\\times10^{23}\\) mol\\(^{-1}\\) "
            "and give one sanity check.</p>"
        ),
        "answer": (
            "<b>Answer: \\(\\rho\\approx4.5\\) g/cm³.</b><br>"
            "1. Convert lengths to cm: \\(a=2.95\\times10^{-8}\\) cm, \\(c=4.68\\times10^{-8}\\) cm.<br>"
            "2. \\(V_c=\\tfrac{\\sqrt{3}}{2}(2.95\\times10^{-8})^2(4.68\\times10^{-8})=3.53\\times10^{-23}\\) cm³.<br>"
            "3. Cell mass \\(=6(47.87)/(6.022\\times10^{23})=4.77\\times10^{-22}\\) g.<br>"
            "4. \\(\\rho=4.77\\times10^{-22}/3.53\\times10^{-23}=4.51\\) g/cm³.<br>"
            "<b>Sanity check:</b> titanium handbook value is about 4.5 g/cm³ — lighter than steel, "
            "heavier than aluminium.<br>"
            "<b>Design meaning:</b> titanium buys strength-to-weight in aerospace because this density "
            "sits well below steel while stiffness remains high."
        ),
    },
    {
        "tags": ("Short calculation", "Written"),
        "stem": (
            "<p>Two FCC alloys share the same atomic mass \\(A=58.7\\) g/mol. Alloy X has "
            "\\(a=0.352\\) nm; alloy Y has \\(a=0.362\\) nm. Without full working, which is denser "
            "and by roughly what percentage? Then verify with \\(\\rho=nA/(V_cN_A)\\), \\(n=4\\).</p>"
        ),
        "answer": (
            "<b>Answer: X is denser; about 8.5% higher density than Y.</b><br>"
            "1. With \\(n\\) and \\(A\\) fixed, \\(\\rho\\propto1/a^3\\). Y's edge is 2.8% larger, so "
            "volume is \\((1.028)^3=1.087\\) times bigger and density is lower by about 8%.<br>"
            "2. X: \\(a=3.52\\times10^{-8}\\) cm, \\(V_c=4.36\\times10^{-23}\\) cm³, \\(\\rho=8.94\\) g/cm³.<br>"
            "3. Y: \\(a=3.62\\times10^{-8}\\) cm, \\(V_c=4.74\\times10^{-23}\\) cm³, \\(\\rho=8.24\\) g/cm³.<br>"
            "4. Ratio \\(8.94/8.24=1.08\\).<br>"
            "<b>Sanity check:</b> a few percent change in lattice parameter moves density by "
            "roughly three times that percentage — believable for a small alloying shift.<br>"
            "<b>Design meaning:</b> composition changes that swell the lattice lighten the part "
            "even when the chemistry looks similar on a data sheet."
        ),
    },
    {
        "tags": ("Diagram interpretation", "Written"),
        "stem": (
            "<p>A table lists four solids with measured properties:</p>"
            "<p><b>Material 1:</b> shiny, \\(\\sigma\\approx10^7\\) S/m, deforms plastically.<br>"
            "<b>Material 2:</b> transparent, \\(\\sigma&lt;10^{-12}\\) S/m, hard, shatters without yield.<br>"
            "<b>Material 3:</b> opaque, \\(\\sigma&lt;10^{-10}\\) S/m, very high compressive strength.<br>"
            "<b>Material 4:</b> flexible film, \\(\\sigma&lt;10^{-14}\\) S/m, low \\(T_m\\), melts before 200 °C.</p>"
            "<p>For each, name the dominant bonding family and one engineering application that "
            "fits those properties.</p>"
        ),
        "answer": (
            "<b>Answer:</b><br>"
            "<b>1 — metallic:</b> delocalised electrons explain conductivity and ductility; e.g. "
            "busbar or formed bracket.<br>"
            "<b>2 — covalent/ionic glass or ceramic:</b> no free electrons, no slip; e.g. "
            "optical window (if flaw-tolerant design allows).<br>"
            "<b>3 — ionic/covalent ceramic:</b> strong bonds, poor tension, good compression; "
            "e.g. kiln brick or bearing race in compression.<br>"
            "<b>4 — polymer with secondary bonding:</b> weak intermolecular forces, low melting "
            "point; e.g. packaging film.<br>"
            "<b>Design meaning:</b> the table is read bond type → properties → application, the "
            "same chain used when rewriting vague briefs into measurable targets."
        ),
    },
    {
        "tags": ("Short explanation", "Written"),
        "stem": (
            "<p>A satellite antenna reflector must be stiff, lightweight, corrosion-resistant in "
            "salt air, and manufacturable as a thin shell. A colleague writes 'use stainless steel "
            "because it is strong.' Rewrite the brief as property targets, name two measurable "
            "constraints the steel may fail, and suggest what information you would look up next.</p>"
        ),
        "answer": (
            "<b>Answer:</b> replace 'strong' with <b>specific stiffness</b> \\(E/\\rho\\), "
            "<b>yield strength</b> for handling loads without permanent set, <b>corrosion "
            "resistance</b> in marine exposure, and <b>minimum shell thickness</b> for forming.<br>"
            "Stainless steel may fail the <b>mass budget</b> because \\(\\rho\\approx7.8\\) g/cm³ "
            "limits \\(E/\\rho\\) compared with aluminium or CFRP, and it may fail <b>forming</b> "
            "limits if the required shell is thinner than the mill can roll reliably.<br>"
            "Next lookups: handbook \\(E\\), \\(\\rho\\), \\(\\sigma_y\\) for candidates; galvanic "
            "compatibility in the stack; and manufacturing gauge limits.<br>"
            "<b>Design meaning:</b> 'strong' hides whether the driver is weight, stiffness or "
            "environment — writing targets first is what makes rejection of steel (or acceptance) "
            "defensible."
        ),
    },
]

# ---------------------------------------------------------------------------
# Week 2 — stress-strain, E, yield, UTS, resilience, toughness, safety factor
# ---------------------------------------------------------------------------
EXTRA[2] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>During necking in a tensile test, engineering stress falls while true stress '
          'continues to rise. Why?</p>',
  'options': ['The load drops faster than the cross-sectional area shrinks',
              'The load may fall slightly but the instantaneous area shrinks faster, so true '
              'stress rises',
              'True stress and engineering stress must stay equal by definition after yield',
              'Necking reduces both stresses because the material has softened'],
  'answer': '<b>Answer: B.</b> Engineering stress uses the original area \\(A_0\\); true stress '
            'uses the current area. After necking, force may decrease a little, but area contracts '
            'more quickly, so \\(\\sigma_t=F/A\\) climbs above the engineering peak. <b>Sanity '
            'check:</b> the engineering curve must turn down at necking — that is how you spot it '
            'on a plot. <b>Design meaning:</b> local stress at fracture can exceed the UTS read '
            'from a standard engineering curve.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Modulus of resilience \\(U_r\\) is defined as:</p>',
  'options': ['The total area under the stress–strain curve to fracture',
              'The elastic energy stored per unit volume up to the yield point, '
              '\\(\\sigma_y^2/(2E)\\)',
              'The stress at which necking begins',
              'The ratio of ultimate tensile strength to yield strength'],
  'answer': '<b>Answer: B.</b> Resilience is the elastic triangle only — energy returned on '
            'unloading. Option A is toughness. Option C is UTS-related behaviour, not an energy '
            'measure. <b>Design meaning:</b> springs and energy-absorbing clips are sized on '
            '\\(U_r\\), not on UTS.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>A tensile bar of gauge length 80 mm stretches to 80.384 mm under load. What is the '
          'engineering strain?</p>',
  'options': ['0.00048', '0.0048', '0.048', '0.48'],
  'answer': '<b>Answer: B.</b> \\(\\varepsilon=(80.384-80)/80=0.384/80=0.0048\\). <b>Sanity check:</b> 0.384 mm on 80 mm '
            'is just under 0.5%, so a strain near 0.005 is believable. <b>Design meaning:</b> '
            'strain is dimensionless, so this value transfers directly to a structural member of '
            'any length.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>Two ductile alloys share the same yield strength. Alloy X fractures at 12% '
          'elongation; alloy Y at 28%. A guard rail must absorb impact energy by plastic '
          'deformation before separating. Which alloy is preferable, and on what property?</p>',
  'options': ['X, because lower elongation means higher strength',
              'Y, because greater elongation usually means higher toughness',
              'Either, because yield strength is the same',
              'X, because shorter elongation means stiffer response in impact'],
  'answer': '<b>Answer: B.</b> Equal yield does not imply equal energy absorption. Toughness is '
            'area under the curve; a material that deforms further before fracture generally '
            'absorbs more energy. <b>Design meaning:</b> impact guards are chosen on toughness and '
            'ductility, not yield alone.'},
 {'tags': ('True/false', 'Quick'),
  'stem': "<p><b>True or false:</b> Poisson's ratio \\(\n"
          'u\\) for an isotropic metal in tension is typically about 0.3, meaning lateral '
          'contraction is roughly 30% of the axial extension strain.</p>',
  'answer': '<b>Answer: True.</b> \\(\\varepsilon_{\\text{lateral}}=-\n'
            'u\\varepsilon_{\\text{axial}}\\). For \\(\n'
            'u\\approx0.3\\) and \\(\\varepsilon_{\\text{axial}}=0.01\\), lateral strain is about \\(-0.003\\). <b>Design '
            'meaning:</b> a tensile bolt tightens clearance holes and a compressed gasket spreads '
            '— \\(\n'
            'u\\) sets that coupling.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because fracture stress on a ductile tensile specimen is read '
          'below the ultimate tensile strength on an engineering curve, the material must have '
          'weakened during the test.</p>',
  'answer': '<b>Answer: False.</b> The material has not lost strength; the engineering stress '
            'divides by \\(A_0\\) while the neck carries load on a smaller area. True stress at '
            'fracture is often above UTS. <b>Design meaning:</b> do not interpret a falling '
            'engineering curve as softening — it is a geometry artefact.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>A steel rod \\(A_0=120\\) mm², \\(L_0=500\\) mm, \\(E=200\\) GPa, '
          '\\(\\sigma_y=350\\) MPa carries 36 kN. Find engineering stress, elastic strain, '
          'extension in mm, and state whether it springs back on unloading.</p>',
  'answer': '<b>Answer: \\(\\sigma=300\\) MPa, \\(\\varepsilon=0.0015\\), \\(\\Delta L=0.75\\) mm, springs back.</b><br>1. '
            '\\(\\sigma=36{,}000/120=300\\) MPa.<br>2. \\(300<350\\) MPa → elastic.<br>3. \\(\\varepsilon=\\sigma/E=300/200{,}000=0.0015\\).<br>4. \\(\\Delta L=0.0015\\times500=0.75\\) mm.<br><b>Sanity check:</b> sub-millimetre extension on half a metre '
            'is typical of elastic metal straining. <b>Design meaning:</b> margin to yield is '
            '\\(350/300=1.17\\) — thin for a safety-critical tie.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Calculate toughness as the approximate area under a simplified stress–strain curve: '
          'linear elastic to \\(\\sigma_y=400\\) MPa at \\(\\varepsilon_y=0.002\\), then constant stress to fracture at \\(\\varepsilon_f=0.20\\). Compare with modulus of resilience.</p>',
  'answer': '<b>Answer: \\(U_r=0.40\\) MJ/m³; toughness \\(\\approx80\\) MJ/m³.</b><br>1. '
            '\\(U_r=\\sigma_y^2/(2E)\\) needs \\(E=\\sigma_y/\\varepsilon_y=400/0.002=200\\) GPa.<br>2. \\(U_r=400^2/(2\\times200{,}000)=0.40\\) '
            'MJ/m³.<br>3. Triangle \\(=\\tfrac12(400)(0.002)=0.40\\) MJ/m³; rectangle '
            '\\(400(0.20-0.002)=79.2\\) MJ/m³; total \\(\\approx79.6\\) MJ/m³.<br><b>Sanity '
            'check:</b> toughness must dwarf resilience when plastic strain is large. <b>Design '
            'meaning:</b> a high-yield spring steel stores little energy elastically but may still '
            'be poor in impact if elongation is small.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Two engineering stress–strain curves share the same yield (\\(250\\) MPa) and UTS '
          '(\\(500\\) MPa). Curve 1 reaches fracture at \\(\\varepsilon=0.08\\); curve 2 at \\(\\varepsilon=0.25\\). Identify which is likely work-hardened vs annealed, which is '
          'tougher, and which suits a crumple zone.</p>',
  'answer': '<b>Answer:</b> curve 2 is tougher and suits a crumple zone; it is likely annealed or '
            'low-alloy with more ductility, while curve 1 may be heavily cold-worked or higher '
            'strength with less elongation.<br>Toughness \\(\\propto\\) area: \\(500\\times0.08\\approx40\\) vs \\(500\\times0.25\\approx125\\) MJ/m³ (rough rectangles). '
            '<b>Design meaning:</b> matching UTS does not match energy absorption — read '
            'elongation and area, not peak stress alone.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>A crane hook is proof-tested once at 1.25× working load with no visible deformation. '
          'After \\(10^5\\) cycles at 0.6× working load it fails suddenly. Explain how both '
          'observations coexist and what design check the proof test cannot replace.</p>',
  'answer': '<b>Answer:</b> the proof test checked single-cycle strength below yield; failure was '
            'fatigue — a surface crack growing each cycle until fast fracture.<br>Nominal stress '
            'stayed below yield throughout, so no permanent bending was visible. The proof test '
            'cannot show initiation sites, cycle count, or stress range. <b>Design meaning:</b> '
            'cyclic components need S–N or fracture mechanics assessment, not static proof load '
            'alone.'}]

# ---------------------------------------------------------------------------
# Week 3 — dislocations, vacancies, diffusion, Hall-Petch, strengthening
# ---------------------------------------------------------------------------
EXTRA[3] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Which defect type is a one-dimensional line along which slip occurs?</p>',
  'options': ['Vacancy', 'Edge or screw dislocation', 'Grain boundary', 'Interstitial atom'],
  'answer': '<b>Answer: B.</b> Dislocations are line defects; their motion is plastic deformation. '
            'Vacancies and interstitials are point defects; grain boundaries are area defects. '
            '<b>Design meaning:</b> strengthening targets dislocation motion, not bond breaking '
            'across the whole crystal.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Solid-solution strengthening works mainly because solute atoms:</p>',
  'options': ['Increase the lattice parameter until the crystal collapses',
              'Create local lattice distortions that obstruct moving dislocations',
              'Convert the structure from FCC to BCC',
              'Remove all vacancies so diffusion stops'],
  'answer': '<b>Answer: B.</b> Foreign atoms distort the lattice and pin dislocations. <b>Design '
            'meaning:</b> alloying trades conductivity and ductility for strength — the price must '
            'be named in the recommendation.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>Self-diffusion coefficient follows \\(D=D_0\\exp(-Q/RT)\\). If \\(Q\\) doubles while '
          'temperature is fixed, by what factor does \\(D\\) change?</p>',
  'options': ['Doubles',
              'Halves',
              'Multiplies by \\(e^{-Q/RT}\\) with the new \\(Q\\) — a much smaller \\(D\\)',
              'Stays the same because \\(D_0\\) adjusts'],
  'answer': '<b>Answer: C.</b> At fixed \\(T\\), doubling \\(Q\\) makes the exponent more '
            'negative, so \\(D\\) falls sharply (not by a simple factor of 2). <b>Sanity '
            'check:</b> higher activation energy means harder diffusion. <b>Design meaning:</b> '
            'carburising and homogenising schedules are exponentially sensitive to temperature.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>A brass rod is cold-drawn to raise strength, then lightly re-annealed to restore '
          'some ductility without losing all the gain. Which microstructural outcome is '
          'intended?</p>',
  'options': ['Full recrystallisation and coarse grains for maximum softness',
              'Recovery only — dislocations rearrange, strength largely retained',
              'Precipitation of a second phase from the melt',
              'Conversion of dislocations into vacancies'],
  'answer': '<b>Answer: B.</b> A light anneal targets recovery: reduced dislocation density and '
            'internal stress with partial retention of cold-work strength. Full recrystallisation '
            'removes most strengthening. <b>Design meaning:</b> process temperature and time are '
            'strength specifications, not just finishing steps.'},
 {'tags': ('True/false', 'Quick'),
  'stem': "<p><b>True or false:</b> in Fick's first law \\(J=-D\\,dC/dx\\), the minus sign means "
          'diffusion occurs down the concentration gradient.</p>',
  'answer': '<b>Answer: True.</b> Atoms spread from high to low concentration, opposite to the '
            'slope of \\(C(x)\\). <b>Design meaning:</b> case-depth profiles in surface hardening '
            'are read from this direction rule.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> cold working increases dislocation density, which raises yield '
          'strength and usually reduces ductility.</p>',
  'answer': '<b>Answer: True.</b> Tangled dislocations obstruct each other — work hardening. '
            'Ductility falls because fewer dislocations can move cooperatively. <b>Design '
            'meaning:</b> formed parts are often work-hardened at the surface; subsequent heating '
            'can anneal that gain away.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Steel obeys \\(\\sigma_y=50+0.55\\,d^{-1/2}\\) (MPa, \\(d\\) in m). Find '
          '\\(\\sigma_y\\) at \\(d=16\\) µm and at \\(d=64\\) µm, and state the trend.</p>',
  'answer': '<b>Answer: 188 MPa at 16 µm; 119 MPa at 64 µm.</b><br>1. \\(d=16\\times10^{-6}\\) m → '
            '\\(d^{-1/2}=250\\) m\\(^{-1/2}\\) → \\(50+0.55(250)=188\\) MPa.<br>2. \\(d=64\\times10^{-6}\\) m → \\(d^{-1/2}=125\\) → \\(50+69=119\\) MPa.<br><b>Sanity check:</b> '
            'coarser grains give lower strength — Hall–Petch direction. <b>Design meaning:</b> '
            'overheating after processing can halve strength by grain growth.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Copper wire is cold-drawn from 4.0 mm to 3.2 mm diameter. Assuming uniform '
          'deformation, find the cold-work percentage and state one property change expected.</p>',
  'answer': '<b>Answer: CW \\(\\approx36\\%\\); higher \\(\\sigma_y\\), lower '
            'ductility.</b><br>1. Area \\(\\propto d^2\\): \\(A_f/A_0=(3.2/4.0)^2=0.64\\).<br>2. '
            'CW% \\(=(A_0-A_f)/A_0\\times100=36\\%\\).<br><b>Sanity check:</b> meaningful drawing '
            'reduces area noticeably — 36% is plausible. <b>Design meaning:</b> drawn wire '
            'strength is a process product; specify temper or cold-work level on the drawing.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>A log–log plot shows diffusion coefficient \\(D\\) vs temperature \\(1/T\\) as a '
          "straight line with negative slope for two metals A and B. Metal A's line sits above B's "
          'at every temperature. Interpret the slopes and relative \\(Q\\), and state which '
          'diffuses faster at 800 °C.</p>',
  'answer': "<b>Answer:</b> slope \\(=-Q/R\\); steeper magnitude → larger \\(Q\\). A's higher "
            '\\(D\\) line means faster diffusion at all \\(T\\). At 800 °C (1073 K), A has the '
            'larger \\(D\\). <b>Design meaning:</b> a coating that relies on diffusion will bond '
            'faster with metal A — or need lower temperature for B.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>A turbine blade alloy is precipitation-hardened. Explain in one mechanism chain why '
          'solution treatment plus ageing raises strength, and why overheating the aged blade '
          'destroys the gain.</p>',
  'answer': '<b>Answer:</b> solution treatment dissolves solute; quench traps a supersaturated '
            'solid solution; ageing precipitates fine particles that pin dislocations → higher '
            '\\(\\sigma_y\\). Overheating coarsens precipitates (Ostwald ripening), spacing grows, '
            'pinning weakens. <b>Design meaning:</b> service temperature must stay below the '
            'over-ageing threshold, not just below melting.'}]

# ---------------------------------------------------------------------------
# Week 4 — fracture mechanics K, fatigue S-N, endurance limit
# ---------------------------------------------------------------------------
EXTRA[4] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>The stress intensity factor \\(K_I\\) has SI units of:</p>',
  'options': ['MPa', 'MPa·√m', 'J/m²', 'm⁻¹'],
  'answer': '<b>Answer: B.</b> \\(K=Y\\sigma\\sqrt{\\pi a}\\) combines stress with \\(\\\\sqrt{\\pi a}'
            'ext{length}}\\). <b>Design meaning:</b> mixing mm and m in \\(a\\) is the classic '
            'unit trap.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>On an S–N diagram, decreasing stress amplitude generally:</p>',
  'options': ['Shortens fatigue life',
              'Lengthens fatigue life',
              'Has no effect on life',
              'Raises the endurance limit for aluminium'],
  'answer': '<b>Answer: B.</b> Lower amplitude → more cycles to failure. <b>Design meaning:</b> '
            'stress relief grooves and lower loads buy life — often logarithmically on the N '
            'axis.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>\\(\\sigma=150\\) MPa, \\(a=8\\) mm, \\(Y=1.1\\), \\(K_{IC}=40\\) MPa·√m. Find '
          '\\(K_I\\) and state whether fracture is imminent.</p>',
  'options': ['\\(K_I\\approx9.8\\) MPa·√m — safe',
              '\\(K_I\\approx26\\) MPa·√m — safe',
              '\\(K_I\\approx26\\) MPa·√m — fracture',
              '\\(K_I\\approx260\\) MPa·√m — fracture'],
  'answer': '<b>Answer: B.</b> \\(a=0.008\\) m → \\(K_I=1.1(150)\\sqrt{\\pi(0.008)}\\approx26\\) '
            'MPa·√m \\(<40\\). Option D uses mm in \\(a\\). <b>Sanity check:</b> margin '
            '\\(40/26\\approx1.5\\). <b>Design meaning:</b> growing the crack from 8 mm toward 12 '
            'mm erodes margin quickly (\\(\\propto\\sqrt a\\)).'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>A designer doubles the wall thickness of a pressure vessel to reduce stress, leaving '
          'material and flaw size unchanged. How does the allowable flaw size change if fracture '
          'governs?</p>',
  'options': ['Doubles',
              'Quadruples',
              'Unchanged — thickness does not appear in \\(K_I\\) for through-thickness cracks the '
              'same way',
              'Halves'],
  'answer': '<b>Answer: C.</b> For a given remote \\(\\sigma\\) and geometry, \\(K_I\\) depends on '
            '\\(\\sigma\\) and \\(a\\), not directly on thickness (for the idealised through '
            'crack). Halving stress (roughly, for same pressure) raises allowable \\(a\\) '
            'quadratically. <b>Design meaning:</b> thicker wall lowers \\(\\sigma\\), which buys '
            'larger tolerable flaws — but weight and cost rise.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> for many steels an endurance limit exists — below it, fatigue '
          'failure is not expected regardless of cycle count.</p>',
  'answer': '<b>Answer: True.</b> The S–N curve flattens. Aluminium alloys lack this plateau. '
            '<b>Design meaning:</b> infinite-life design is possible for steel but not for typical '
            'aluminium brackets without a stated retirement life.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because fatigue cracks initiate at the surface, polishing the '
          'interior bore of a rotating shaft is the most effective way to extend life.</p>',
  'answer': '<b>Answer: False.</b> Initiation is at the highest-stressed surface — for a shaft, '
            'the outer diameter under bending. Bore polishing ignores the critical location. '
            '<b>Design meaning:</b> fix fillets, finish and compressive surface treatment where '
            'stress and exposure coincide.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Plate: \\(K_{IC}=50\\) MPa·√m, \\(Y=1.0\\), working \\(\\sigma=180\\) MPa. Find '
          'maximum allowable crack length \\(2a\\) and compare with yield-based design at '
          '\\(\\sigma_y=400\\) MPa.</p>',
  'answer': '<b>Answer: \\(2a\\approx9.8\\) mm; fracture governs well below yield.</b><br>1. '
            '\\(a_c=\\f'
            'rac1\\pi(K_{IC}/(Y\\sigma))^2=\\f'
            'rac1\\pi(50/180)^2=4.9\\times10^{-3}\\) m.<br>2. \\(2a=9.8\\) mm. Yield allows 400 MPa '
            '\\(\\gg180\\) MPa.<br><b>Sanity check:</b> millimetre-scale critical flaws are '
            'typical for high-\\(K_{IC}\\) steel. <b>Design meaning:</b> inspection must resolve '
            'flaws \\(\\ll10\\) mm.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>A component sees \\(2\\times10^5\\) cycles at 280 MPa amplitude then \\(5\\times10^5\\) at 200 MPa. Steel has endurance limit 260 MPa. Will Miner\'s rule predict '
          'failure if each block alone is below the limit?</p>',
  'answer': '<b>Answer: No cumulative damage from those blocks if each amplitude is below 260 MPa '
            'and life is infinite there.</b><br>At \\(\\sigma_a<\\) endurance limit, \\(N\\rightarrow\\infty\\) so \\(n/N=0\\). <b>Sanity check:</b> Miner\'s rule sums \\(n_i/N_i\\); '
            'infinite life terms vanish. <b>Design meaning:</b> variable amplitude needs a '
            'rainflow or spectrum analysis — one peak below yield does not excuse a damaging cycle '
            'count above endurance.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Fracture surfaces: (A) cup-and-cone with shear lip; (B) flat, featureless, '
          'perpendicular to tensile axis. Assign ductile vs brittle, state likely temperature or '
          'material class, and one design response for each.</p>',
  'answer': '<b>Answer:</b> A — ductile overload, metals at moderate \\(T\\); design for toughness '
            'and redundancy. B — brittle cleavage, cold ceramic or embrittled steel; design for '
            '\\(K_{IC}\\), flaw size, and temperature shift (DBTT). <b>Design meaning:</b> '
            'fractography names the governing failure mode after the event.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>A welded joint uses a high-strength filler. Explain why fatigue life may be worse '
          'than the parent plate despite higher \\(\\sigma_y\\), and list two design '
          'mitigations.</p>',
  'answer': '<b>Answer:</b> weld toe is a stress concentrator and often tensile residual stress; '
            'high-strength weld metal can have lower \\(K_{IC}\\). Mitigations: grind toe profile, '
            'shot-peen for compressive residual stress, use lower-strength tougher filler, '
            'full-penetration and inspectable geometry. <b>Design meaning:</b> fatigue follows '
            'stress range at defects — strength without toughness and geometry control fails.'}]

# ---------------------------------------------------------------------------
# Week 5 — creep, thermal expansion, thermal shock, phases preview
# ---------------------------------------------------------------------------
EXTRA[5] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Secondary (steady-state) creep rate is read from a creep curve as:</p>',
  'options': ['The initial steep slope at zero time',
              'The slope of the nearly straight middle portion',
              'The vertical drop at rupture',
              'The total strain divided by elastic modulus'],
  'answer': '<b>Answer: B.</b> Secondary creep has constant \\(\\dot\\varepsilon\\). Primary is decelerating; tertiary accelerates to failure. <b>Design '
            'meaning:</b> extrapolate life from secondary slope, not the primary knee.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Thermal shock resistance improves when a ceramic has:</p>',
  'options': ['High \\(E\\), high \\(\\alpha\\), low strength',
              'Low \\(E\\), low \\(\\alpha\\), high strength',
              'High conductivity and high \\(\\alpha\\)',
              'Low density only'],
  'answer': '<b>Answer: B.</b> Shock parameter \\(R\\propto\\sigma_f/(E\\alpha)\\) — low '
            'stiffness and expansion, high strength. <b>Design meaning:</b> quench-cracking '
            'favours low-\\(E\\) porous refractories over dense stiff ones.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>A 2.0 m steel rail (\\(\\alpha=12\\times10^{-6}\\)/°C) is installed at 15 °C and '
          'reaches 45 °C in summer. Find free expansion in mm.</p>',
  'options': ['0.36 mm', '0.72 mm', '1.44 mm', '7.2 mm'],
  'answer': '<b>Answer: B.</b> \\(\\Delta L=\\alpha L_0\\Delta T=12\\times10^{-6}(2000)(30)=0.72\\) mm. <b>Sanity check:</b> sub-millimetre per metre per '
            '30 °C is typical for steel. <b>Design meaning:</b> expansion joints must swallow this '
            'movement.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>Two ceramics have the same \\(\\alpha\\) but ceramic P has \\(E=400\\) GPa and '
          'ceramic Q has \\(E=200\\) GPa. Which develops lower thermal stress when quenched into '
          'rigid constraint?</p>',
  'options': ['P, because higher \\(E\\) resists cracking',
              'Q, because \\(\\sigma\\approx E\\alpha\\Delta T\\) is halved',
              'Equal, because \\(\\alpha\\) matches',
              'P, because stiff materials distribute stress better'],
  'answer': '<b>Answer: B.</b> At equal \\(\\Delta T\\) and constraint, \\(\\sigma\\propto E\\). '
            'Lower \\(E\\) halves thermal stress. <b>Design meaning:</b> thermal shock favours '
            'compliant microstructures, not stiffer ones.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> creep becomes significant when service temperature exceeds '
          'roughly 40% of the melting temperature in kelvin.</p>',
  'answer': '<b>Answer: True.</b> Homologous temperature \\(T/T_m\\) sets creep urgency. <b>Design '
            'meaning:</b> polymers and lead creep near room temperature; steel does not.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> a fully constrained bar heated by \\(\\Delta T\\) develops '
          'zero strain and stress \\(\\sigma=E\\alpha\\Delta T\\).</p>',
  'answer': '<b>Answer: True.</b> Thermal expansion is suppressed; elastic strain balances it. '
            'Length cancels from \\(\\sigma\\). <b>Design meaning:</b> fixed pipe supports see '
            'temperature as load — size expansion loops or sliding bearings.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Creep data: \\(\\varepsilon=0.40\\%\\) at 2,000 h and 1.00% at 10,000 h on the secondary line. Find '
          '\\(\\dot\\varepsilon\\) in %/h and predict strain at 25,000 h.</p>',
  'answer': '<b>Answer: \\(\\dot\\varepsilon=7.5\\times10^{-5}\\) %/h; \\(\\varepsilon\\approx2.13\\%\\) at 25,000 h.</b><br>1. \\(\\dot\\varepsilon=(1.00-0.40)/(10{,}000-2{,}000)=0.60/8000=7.5\\times10^{-5}\\) %/h.<br>2. '
            '\\(\\varepsilon=1.00+7.5\\times10^{-5}(25{,}000-10{,}000)=2.125\\%\\).<br><b>Sanity '
            'check:</b> strain grows linearly on secondary portion. <b>Design meaning:</b> a 2% '
            'distortion limit fails before rupture — strain and time-to-rupture are separate '
            'checks.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Brass bar \\(L=1.5\\) m, \\(\\alpha=20\\times10^{-6}\\)/°C, \\(E=110\\) GPa, '
          '\\(\\Delta T=60\\) °C. Find free \\(\\Delta L\\) and fully fixed stress.</p>',
  'answer': '<b>Answer: \\(\\Delta L=1.8\\) mm; \\(\\sigma=132\\) MPa.</b><br>1. \\(\\Delta L=20\\times10^{-6}(1500)(60)=1.8\\) mm.<br>2. \\(\\sigma=E\\alpha\\Delta T=110\\times10^9(20\\times10^{-6})(60)=132\\) MPa.<br><b>Sanity check:</b> 132 MPa is a real '
            'load — comparable to working stresses. <b>Design meaning:</b> rigid clamps on a 60 °C '
            'swing need slip joints or the bar yields.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Sketch description: Gibbs phase rule regions on a unary diagram — single-phase '
          'solid, liquid, and two-phase solid+liquid band. A vertical line at fixed composition '
          'crosses liquid, then L+S, then solid. Name phases present in each segment and state '
          'what happens at each boundary crossing.</p>',
  'answer': '<b>Answer:</b> above liquidus — all liquid; between liquidus and solidus — L+S '
            'coexist; below solidus — solid only. At liquidus, solid nucleates; at solidus, liquid '
            'disappears. <b>Design meaning:</b> this unary picture previews binary lever-rule '
            'thinking — temperature fixes which phases can exist.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>A polymer gear and a steel gear both operate at 120 °C in an oven conveyor. Explain '
          'why creep may govern the polymer while steel is unaffected, using homologous '
          'temperature.</p>',
  'answer': '<b>Answer:</b> polymer \\(T_m\\) or \\(T_g\\) may be only 150–250 °C, so 120 °C is '
            '0.5–0.8 \\(T_m\\) — deep in the creep regime. Steel \\(T_m\\approx1800\\) K; 393 K '
            "is \\(<0.25\\,T_m\\) — negligible creep. <b>Design meaning:</b> 'same oven "
            "temperature' is not the same material experience — always compare \\(T/T_m\\)."}]

# ---------------------------------------------------------------------------
# Week 6 — phase diagrams, tie-line, lever rule, eutectic
# ---------------------------------------------------------------------------
EXTRA[6] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>The lever rule denominator is always:</p>',
  'options': ['\\(C_0\\)',
              'The full tie-line length \\(C_\\beta-C_\\alpha\\)',
              'The distance from \\(C_0\\) to the nearest phase boundary only',
              'The melting temperature of the alloy'],
  'answer': '<b>Answer: B.</b> Both phase fractions share \\(C_\\beta-C_\\alpha\\). <b>Design '
            'meaning:</b> if fractions do not sum to 1, check the denominator first.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>A hypereutectic alloy lies:</p>',
  'options': ['To the left of the eutectic composition',
              'To the right of the eutectic composition',
              'Exactly at the eutectic point',
              'Outside the diagram'],
  'answer': '<b>Answer: B.</b> Hyper = above eutectic composition on the diagram. <b>Design '
            'meaning:</b> primary phase on cooling is \\(\\beta\\), not \\(\\alpha\\).'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>Tie-line: \\(C_\\alpha=20\\) wt%, \\(C_\\beta=80\\) wt%, \\(C_0=50\\) wt%. Find '
          '\\(W_\\beta\\).</p>',
  'options': ['0.25', '0.50', '0.75', '0.80'],
  'answer': '<b>Answer: B.</b> '
            '\\(W_\\beta=(C_0-C_\\alpha)/(C_\\beta-C_\\alpha)=(50-20)/60=0.50\\). <b>Sanity '
            'check:</b> \\(C_0\\) is mid-tie-line → 50/50. <b>Design meaning:</b> half the '
            'microstructure is the \\(\\beta\\) phase — property mix follows that fraction.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>During slow cooling of a hypoeutectic alloy, the liquid composition moves along the '
          'liquidus. Does the overall alloy composition \\(C_0\\) change?</p>',
  'options': ['Yes — it enriches in the solute rejected by the solid',
              'Yes — it depletes as solid forms',
              'No — \\(C_0\\) is fixed; only phase fractions and phase compositions change',
              'Only if the crucible leaks'],
  'answer': '<b>Answer: C.</b> Overall composition is conserved; local liquid enriches but the '
            'bulk \\(C_0\\) does not. <b>Design meaning:</b> lever rule uses fixed \\(C_0\\) at '
            'each temperature — a common exam inversion trap.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> at the eutectic composition, the liquid transforms to two '
          'solid phases at a single temperature.</p>',
  'answer': '<b>Answer: True.</b> \\(L\\rightarrow\\alpha+\\beta\\) is isothermal at the eutectic point. <b>Design '
            'meaning:</b> eutectic solders melt sharply — desirable for assembly control.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because the lever rule gives mass fractions, multiplying by '
          'total mass gives the mass of each phase present.</p>',
  'answer': '<b>Answer: True.</b> \\(m_\\alpha=W_\\alpha m_{\\text{total}}\\). <b>Design '
            'meaning:</b> converting to kg is how you cost alloying elements locked in a brittle '
            'phase.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>\\(C_0=28\\) wt% B, tie-line \\(C_\\alpha=5\\) wt%, \\(C_\\beta=75\\) wt%. Find '
          '\\(W_\\alpha\\), \\(W_\\beta\\) and verify \\(W_\\alpha C_\\alpha+W_\\beta '
          'C_\\beta=C_0\\).</p>',
  'answer': '<b>Answer: \\(W_\\alpha=0.67\\), \\(W_\\beta=0.33\\).</b><br>1. Tie-line length '
            '\\(=75-5=70\\) wt%.<br>2. \\(W_\\alpha=(75-28)/70=47/70=0.67\\); '
            '\\(W_\\beta=(28-5)/70=23/70=0.33\\).<br>3. Check: '
            '\\(0.67(5)+0.33(75)=3.35+24.75=28.0\\) wt%.<br><b>Sanity check:</b> \\(C_0=28\\) is '
            'nearer \\(C_\\alpha=5\\) → mostly \\(\\alpha\\). <b>Design meaning:</b> mass '
            'balance recovers \\(C_0\\) — best check against inverted arms.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>3.5 kg casting, \\(C_0=60\\) wt% B, \\(C_\\alpha=10\\) wt%, \\(C_\\beta=90\\) wt%. '
          'Find mass of each phase and total B in each phase.</p>',
  'answer': '<b>Answer: \\(m_\\alpha=1.31\\) kg, \\(m_\\beta=2.19\\) kg; total B = 2.10 '
            'kg.</b><br>1. \\(W_\\beta=(60-10)/80=0.625\\), \\(W_\\alpha=0.375\\).<br>2. '
            '\\(m_\\beta=0.625(3.5)=2.19\\) kg; \\(m_\\alpha=1.31\\) kg.<br>3. B balance: '
            '\\(1.31(0.10)+2.19(0.90)=0.131+1.971=2.10\\) kg \\(=0.60\\times3.5\\).<br><b>Sanity '
            'check:</b> fractions sum to 1 and masses sum to 3.5 kg. <b>Design meaning:</b> most '
            'solute ends in the \\(\\beta\\) phase when \\(C_0\\) is high.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Binary eutectic diagram: describe microstructure of a hypoeutectic alloy cooled '
          'slowly from liquid — primary phase, eutectic constituent, and where each forms on the '
          'diagram path.</p>',
  'answer': '<b>Answer:</b> above liquidus — L; in L+\\(\\alpha\\) — primary \\(\\alpha\\) '
            'dendrites; at eutectic \\(T\\) remaining liquid (enriched to eutectic comp.) → '
            'lamellar \\(\\alpha+\\beta\\); below — primary \\(\\alpha\\) in eutectic matrix. '
            '<b>Design meaning:</b> property is a mix of ductile primary and harder eutectic — '
            'composition sets the proportions.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>Explain how a falling solvus on a phase diagram enables precipitation hardening of '
          'an aluminium alloy, naming the heat-treatment steps.</p>',
  'answer': '<b>Answer:</b> solvus shows \\(\\alpha\\) solubility falls with \\(T\\). Solutionise '
            'above solvus to dissolve solute; quench to trap supersaturation; age to nucleate fine '
            'precipitates that pin dislocations. <b>Design meaning:</b> peak strength is a process '
            'window — over-ageing coarsens precipitates and softens the alloy.'}]

# ---------------------------------------------------------------------------
# Week 7 — polymers Tg, Tm, structure, viscoelasticity, crystallinity
# ---------------------------------------------------------------------------
EXTRA[7] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Above \\(T_g\\), an amorphous polymer is best described as:</p>',
  'options': ['Liquid melt with zero strength',
              'Rubbery solid — chains can slide but material remains cohesive',
              'Crystalline ceramic',
              'Metallic glass with dislocations'],
  'answer': '<b>Answer: B.</b> Above \\(T_g\\) is rubbery, not necessarily molten. <b>Design '
            'meaning:</b> service above \\(T_g\\) means compliance and creep — not automatic '
            'failure, but a different design regime.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Cross-linking between polymer chains produces a:</p>',
  'options': ['Thermoplastic that melts on reheating',
              'Thermoset that cannot be remelted',
              'Metal with higher conductivity',
              'Ceramic with higher \\(K_{IC}\\)'],
  'answer': '<b>Answer: B.</b> Cross-links lock the network; thermosets char rather than flow. '
            '<b>Design meaning:</b> epoxy housings cannot be reprocessed like PE offcuts.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>\\(DP_n=4{,}000\\), repeat unit \\(m=28\\) g/mol. Find \\(M_n\\).</p>',
  'options': ['112 g/mol', '1,428 g/mol', '112,000 g/mol', '4,028 g/mol'],
  'answer': '<b>Answer: C.</b> \\(M_n=4000\\times28=112{,}000\\) g/mol. <b>Sanity check:</b> chains '
            'must be far heavier than one repeat unit. <b>Design meaning:</b> long chains entangle '
            '→ tougher melt-processed parts.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>A datasheet lists \\(E=3.0\\) GPa at 23 °C. A shelf load is applied for five years '
          'at 35 °C (\\(T_g=80\\) °C). Is 3.0 GPa the right modulus for deflection check?</p>',
  'options': ['Yes — modulus is a material constant',
              'Yes — 35 °C is below \\(T_g\\)',
              'No — use creep or long-term modulus at service temperature and duration',
              'No — multiply by \\(T_g/T\\) only'],
  'answer': '<b>Answer: C.</b> Polymers are viscoelastic; short-term room-temperature \\(E\\) '
            'underpredicts long-term deflection. <b>Design meaning:</b> load duration and '
            'temperature belong in the specification, not footnotes.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> higher crystallinity in a semi-crystalline polymer generally '
          'increases stiffness and density.</p>',
  'answer': '<b>Answer: True.</b> Ordered regions pack tighter and resist chain motion. <b>Design '
            'meaning:</b> processing that raises crystallinity (slow cooling) trades transparency '
            'for stiffness.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because polymers have low melting points, they cannot be used '
          'above 100 °C under any circumstances.</p>',
  'answer': '<b>Answer: False.</b> High-performance thermoplastics (PEEK, PI) and thermosets serve '
            'well above 100 °C if \\(T_g\\) or decomposition limit allows. <b>Design meaning:</b> '
            "grade and cross-link density matter more than the word 'polymer'."},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>PP sample \\(\\rho_s=0.905\\) g/cm³, \\(\\rho_c=0.936\\), \\(\\rho_a=0.853\\). Find volume fraction crystallinity \\(X_c\\) from the density formula '
          'and comment on clarity.</p>',
  'answer': '<b>Answer: \\(X_c\\approx0.62\\) '
            '(62%).</b><br>\\(X_c=0.936(0.905-0.853)/(0.905(0.936-0.853))=0.0487/0.0751=0.649\\).<br><b>Sanity '
            'check:</b> between 0 and 1, closer to crystal end. <b>Design meaning:</b> ~65% '
            'crystalline PP is semi-opaque — not window-grade.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Short-term deflection 2.0 mm at \\(E=2.5\\) GPa. After 1 year \\(E_{\\text{app}}=0.83\\) GPa. Find long-term deflection and pass/fail against 4.0 mm '
          'limit.</p>',
  'answer': '<b>Answer: 6.0 mm — fails.</b><br>\\(\\delta\\propto1/E\\) → '
            '\\(\\delta_{1y}=2.0(2.5/0.83)=6.0\\) mm \\(>4.0\\) mm.<br><b>Sanity check:</b> '
            'modulus drop by 3× triples deflection. <b>Design meaning:</b> rib the section or pick '
            'a grade with higher creep resistance.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Log modulus vs temperature: high plateau, steep drop (~3 decades), low rubbery '
          'plateau, then flow. Identify \\(T_g\\), regions, and approximate modulus change across '
          '\\(T_g\\) for an amorphous thermoplastic.</p>',
  'answer': '<b>Answer:</b> steep drop = \\(T_g\\); glassy → rubbery → viscous flow. Modulus falls '
            '~1000× across \\(T_g\\). <b>Design meaning:</b> a part at 0.1× glassy modulus is '
            'effectively failed structurally even if not melted.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>Compare LDPE and HDPE for a chemical tank liner requiring weldability, flexibility '
          'and chemical resistance. Recommend one and cite structure.</p>',
  'answer': '<b>Answer:</b> LDPE — branched chains, lower crystallinity, more flexible, easier to '
            'weld/form; HDPE stiffer and more creep-resistant but less conformable. For a flexible '
            'liner, LDPE (or LLDPE). <b>Design meaning:</b> same repeat unit, different '
            "architecture — always specify grade, not just 'polyethylene'."}]

# ---------------------------------------------------------------------------
# Week 8 — materials selection, Ashby, constraints, lifecycle cost
# ---------------------------------------------------------------------------
EXTRA[8] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>In Ashby chart screening, a <em>constraint</em> is:</p>',
  'options': ['A property to minimise, such as mass',
              'A pass/fail requirement that eliminates candidates',
              'The slope of a tie-line',
              'The cost per kilogram only'],
  'answer': '<b>Answer: B.</b> Constraints gate the shortlist; objectives rank survivors. '
            '<b>Design meaning:</b> optimising mass before checking corrosion rejects nothing that '
            'should never have been listed.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>For a tie loaded in tension with minimum mass, maximise:</p>',
  'options': ['\\(E\\)', '\\(E/\\rho\\)', '\\(\\sigma_y/\\(\\rho\\)', '\\(K_{IC}\\)'],
  'answer': '<b>Answer: C.</b> Strength-limited tie → specific strength \\(\\sigma_y/\\(\\rho\\). \\(E/\\rho\\) is stiffness-limited. <b>Design meaning:</b> the index follows the failure mode '
            'named in the brief.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>Beam bending, stiffness-limited, minimum mass: compare \\(E^{1/2}/\\(\\rho\\) for aluminium (\\(E=70\\) GPa, \\(\\rho=2.7\\)) and titanium (\\(E=110\\) GPa, \\(\\rho=4.5\\)).</p>',
  'options': ['Aluminium wins',
              'Titanium wins',
              'Equal',
              'Neither — use \\(\\sigma_y/\\(\\rho\\) instead'],
  'answer': '<b>Answer: A.</b> Al: \\(\\sqrt{70}/2.7=3.10\\); Ti: \\(\\sqrt{110}/4.5=2.33\\) '
            '(GPa\\(^{1/2}\\)/(g/cm³)). <b>Sanity check:</b> lighter metal with decent \\(E\\) '
            'often wins bending screens. <b>Design meaning:</b> titanium wins tension strength '
            'screens but not always bending stiffness.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>The cheapest material by purchase price is selected for a coastal outdoor bracket. '
          'Which failure mode is most likely overlooked?</p>',
  'options': ['Elastic deflection',
              'Corrosion and pit-assisted fatigue',
              'Colour mismatch',
              'Magnetic saturation'],
  'answer': '<b>Answer: B.</b> Coastal service needs environmental resistance; pits initiate '
            'fatigue. <b>Design meaning:</b> lifecycle cost and failure-mode screening beat '
            'catalogue price.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> performance indices are derived from the governing design '
          'equation for a stated loading case and objective.</p>',
  'answer': '<b>Answer: True.</b> Tie in tension → \\(\\sigma_y/\\(\\rho\\); beam in bending → \\(E^{1/2}/\\(\\rho\\). <b>Design meaning:</b> memorising one index without the loading case inverts '
            'rankings.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because CFRP has very high \\(E/\\rho\\), it can always replace steel in any shape without redesign.</p>',
  'answer': '<b>Answer: False.</b> CFRP is anisotropic, notch-sensitive, and not weldable; '
            'geometry and load direction must be redesigned. <b>Design meaning:</b> substitution '
            'is a redesign project, not a drop-in swap.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Compare \\(\\sigma_y/\\(\\rho\\) (MPa·cm³/g) for stainless (\\(\\sigma_y=520\\) MPa, \\(\\rho=8.0\\)) and high-strength Al (\\(\\sigma_y=450\\) MPa, \\(\\rho=2.8\\)). Which wins for a mass-minimised tie?</p>',
  'answer': '<b>Answer: Al wins: 161 vs 65.</b><br>Steel: \\(520/8.0=65\\); Al: '
            '\\(450/2.8=161\\).<br><b>Sanity check:</b> Al is ~2.5× better on this index though '
            'steel has higher \\(\\sigma_y\\). <b>Design meaning:</b> still check corrosion, '
            'joining and fatigue before selecting Al outdoors.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Component life 15 years. Painted steel: $200 install + repaint every 3 years ($80 '
          'paint + $400 downtime). Stainless: $900 once. Compare 15-year cost.</p>',
  'answer': '<b>Answer: painted steel $2,120; stainless $900 over 15 years.</b><br>1. Repaints at '
            'years 3, 6, 9 and 12 → four events.<br>2. Cost per repaint '
            '\\(=\\$80+\\$400=\\$480\\).<br>3. Steel total \\(=\\$200+4(\\$480)=\\$2{,}120\\). '
            'Stainless \\(=\\$900\\).<br><b>Sanity check:</b> both totals exceed purchase price; '
            'stainless wins by \\$1,220. <b>Design meaning:</b> downtime cost dominates — not '
            'sticker price.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Ashby chart: \\(E\\) vs \\(\\rho\\) log-log. Metals upper-right, foams lower-left, CFRP upper-left diagonal. For '
          'minimum-mass stiffness in tension, which direction on the chart is desirable and why is '
          'CFRP attractive?</p>',
  'answer': '<b>Answer:</b> desirable = up-left (high \\(E\\), low \\(\\rho\\)) → high \\(E/\\rho\\). CFRP sits on a favourable diagonal with very high specific stiffness. '
            '<b>Design meaning:</b> chart screens families before grade-level data entry.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': "<p>A brief says 'pick the lightest metal.' Rewrite as constraints + objective, name two "
          'constraints a light magnesium casting might fail, and one index to screen on.</p>',
  'answer': '<b>Answer:</b> objective: minimise mass. Constraints: yield/strength, stiffness, '
            'corrosion, temperature, manufacturability. Mg may fail corrosion in marine service '
            'and creep near 150 °C. Screen \\(\\sigma_y/\\(\\rho\\) or \\(E/\\rho\\) depending on whether strength or stiffness limits. <b>Design meaning:</b> '
            "'lightest' without constraints selects foam — constraints make the question "
            'engineering.'}]

# ---------------------------------------------------------------------------
# Week 9 — conductivity, resistivity, semiconductors, Hall effect
# ---------------------------------------------------------------------------
EXTRA[9] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Electrical conductivity \\(\\sigma\\) and resistivity \\(\\rho\\) are related by:</p>',
  'options': ['\\(\\sigma=\\(\\rho\\)',
              '\\(\\sigma=1/\\(\\rho\\)',
              '\\(\\sigma=\\(\\rho^2\\)',
              '\\(\\sigma=E/\\rho\\)'],
  'answer': '<b>Answer: B.</b> Reciprocals — a 10% drop in \\(\\sigma\\) is an 11% rise in \\(\\rho\\). <b>Design meaning:</b> asymmetry across the reciprocal is a favourite exam '
            'trap.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>In metals, resistivity rises with temperature mainly because:</p>',
  'options': ['Electron concentration \\(n\\) falls to zero',
              'Lattice vibrations scatter electrons — mobility \\(\\mu\\) falls',
              'Atoms evaporate',
              'Magnetic domains align'],
  'answer': '<b>Answer: B.</b> \\( \\(\\rho=1/(n e \\mu)\\); \\(n\\) is nearly constant, \\(\\mu\\) drops with phonon '
            'scattering. <b>Design meaning:</b> hot busbars need larger section than '
            'room-temperature tables suggest.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>Copper wire \\(\\rho=1.7\\times10^{-8}\\) Ω·m, length 40 m, diameter 2.0 mm. Find \\(R\\).</p>',
  'options': ['0.022 Ω', '0.22 Ω', '2.2 Ω', '22 Ω'],
  'answer': '<b>Answer: B.</b> \\(A=\\pi(1\\times10^{-3})^2=3.14\\times10^{-6}\\) m²; \\(R=\\(\\rho L/A=1.7\\times10^{-8}(40)/(3.14\\times10^{-6})=0.22\\) Ω. <b>Sanity check:</b> short '
            'thick copper — fraction of an ohm. <b>Design meaning:</b> geometry converts handbook '
            '\\(\\rho\\) to circuit \\(R\\).'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>Intrinsic silicon has resistivity rising as temperature falls. A student concludes '
          'doping will always lower resistivity at every temperature. Safest response?</p>',
  'options': ['Correct — dopants always help',
              'Doping raises carrier concentration but mobility and freeze-out can complicate '
              'low-T behaviour',
              'Resistivity is independent of doping',
              'Only insulators respond to temperature'],
  'answer': '<b>Answer: B.</b> Doping adds carriers, but \\(\\rho(T)\\) still varies; at very low \\(T\\) freeze-out can occur. <b>Design '
            'meaning:</b> sensor design must use \\(\\rho(T)\\) curves for the actual dopant and range.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> in the Hall effect, a magnetic field deflects carriers and '
          'builds a transverse Hall voltage proportional to the current and field.</p>',
  'answer': '<b>Answer: True.</b> Hall voltage reveals carrier type and concentration. <b>Design '
            'meaning:</b> Hall sensors turn magnetic fields into measurable voltages in motor '
            'controllers.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because semiconductors have a band gap, they are always '
          'insulators at room temperature.</p>',
  'answer': '<b>Answer: False.</b> Pure Si is a semiconductor at 300 K — resistivity between '
            'metals and insulators; doping tunes it over orders of magnitude. <b>Design '
            "meaning:</b> 'semiconductor' means controllable conductivity, not zero conduction."},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Wire \\(R=1.2\\) Ω at 20 °C. \\(\\alpha_R=0.0040\\)/°C. Find \\(R\\) at 80 °C and '
          'percent change.</p>',
  'answer': '<b>Answer: \\(R_{80}=1.49\\) Ω; '
            '+24%.</b><br>\\(R_{80}=1.2[1+0.004(60)]=1.2(1.24)=1.49\\) Ω.<br><b>Sanity check:</b> '
            'resistance rises with temperature for metals. <b>Design meaning:</b> motor winding '
            'hot resistance affects start-up current calculations.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Conductivity falls from \\(\\sigma_0\\) to \\(0.80\\sigma_0\\). Find fractional '
          'change in resistivity and state direction.</p>',
  'answer': '<b>Answer: \\(\\rho\\) rises by 25%.</b><br>\\(\\rho\\propto1/\\sigma\\) → \\(\\rho/\\(\\rho_0=1/0.80=1.25\\).<br><b>Sanity check:</b> 20% conductivity loss is more than 20% '
            'resistivity gain. <b>Design meaning:</b> alloy additions that cut conductivity have a '
            'disproportionate effect on heating in conductors.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Plot \\(\\rho\\) vs \\(T\\): metal line slopes up; intrinsic semiconductor slopes down; n-type '
          'extrinsic falls then rises at high \\(T\\). Assign each curve and explain the '
          'high-temperature upturn for doped Si.</p>',
  'answer': '<b>Answer:</b> metal — phonon scattering; intrinsic — thermal carriers dominate at '
            'high \\(T\\); extrinsic — donors ionise at moderate \\(T\\) (fall), then intrinsic '
            'generation takes over (rise). <b>Design meaning:</b> devices have a temperature '
            'window where doping controls \\(\\rho\\).'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>A power cable must minimise \\(I^2R\\) losses but stay flexible. Compare copper and '
          'aluminium on conductivity, density and joining. Recommend one with trade-offs.</p>',
  'answer': '<b>Answer:</b> Cu higher \\(\\sigma\\) → lower loss for same size; heavier. Al '
            'lighter and cheaper per amp if section enlarged; needs reliable Al–Cu joints and '
            'oxide control. Overhead lines often Al (AAAC); flexible appliance cord Cu. <b>Design '
            'meaning:</b> conductivity, mass and joint integrity are coupled — not \\(\\sigma\\) '
            'alone.'}]

# ---------------------------------------------------------------------------
# Week 10 — magnetism, B-H loop, soft/hard magnetic materials
# ---------------------------------------------------------------------------
EXTRA[10] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Magnetic flux density \\(B\\) in tesla measures:</p>',
  'options': ['Magnetisation per unit mass',
              'Magnetic flux per unit area normal to the field',
              'Coercivity of the material',
              'Electrical resistivity in a field'],
  'answer': '<b>Answer: B.</b> \\(B\\) is flux/area. \\(H\\) is magnetising field; \\(M\\) is '
            'magnetisation. <b>Design meaning:</b> transformer cores are rated in \\(B\\) swing to '
            'limit core loss.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Soft magnetic materials are chosen for:</p>',
  'options': ['Permanent magnets in loudspeakers',
              'Transformer cores and motor laminations — easy magnetisation reversal, low '
              'hysteresis loss',
              'Cutting tools',
              'Thermal insulation'],
  'answer': '<b>Answer: B.</b> Low coercivity, high \\(\\mu_r\\), low core loss. Hard magnets have '
            'high coercivity. <b>Design meaning:</b> AC applications need soft grades — silicon '
            'steel.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>In free space \\(B=\\mu_0 H\\) with \\(\\mu_0=4\\pi\\times10^{-7}\\) H/m. If '
          '\\(H=1000\\) A/m, find \\(B\\) in mT.</p>',
  'options': ['0.40 mT', '1.26 mT', '12.6 mT', '126 mT'],
  'answer': '<b>Answer: B.</b> \\(B=4\\pi\\times10^{-7}(1000)=1.26\\times10^{-3}\\) T \\(=1.26\\) '
            'mT. <b>Sanity check:</b> millitesla scale for modest \\(H\\). <b>Design meaning:</b> '
            'ferromagnets multiply this by \\(\\mu_r\\) — often thousands.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': "<p>A motor designer selects a hard magnetic alloy for the stator laminations to 'keep "
          "flux trapped.' What is wrong?</p>",
  'options': ['Nothing — harder is better for motors',
              'Stator needs soft magnetic material that reverses magnetisation easily each cycle',
              'Laminations should be ceramic',
              'Coercivity should match rotor speed only'],
  'answer': '<b>Answer: B.</b> Hard magnets resist reversal → huge hysteresis loss in AC cores. '
            '<b>Design meaning:</b> permanent magnets are hard; AC cores are soft — opposite '
            'requirements.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> hysteresis loop area per cycle equals energy dissipated as '
          'heat in the core per unit volume.</p>',
  'answer': '<b>Answer: True.</b> \\(\\oint H\\,dB\\) is core loss per cycle. <b>Design '
            'meaning:</b> thin laminations and silicon reduce area — motor efficiency depends on '
            'it.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> above the Curie temperature a ferromagnet retains strong '
          'permanent magnetisation because domains remain aligned.</p>',
  'answer': '<b>Answer: False.</b> Above \\(T_C\\), ferromagnetic order is lost — paramagnetic '
            'behaviour. Permanent magnetism disappears. <b>Design meaning:</b> motor magnets must '
            'stay below their Curie point in service.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Core volume 0.004 m³, hysteresis loss 120 J/m³ per cycle, frequency 50 Hz. Find '
          'average hysteresis power in watts.</p>',
  'answer': '<b>Answer: 24 W.</b><br>Energy/cycle \\(=120(0.004)=0.48\\) J; power '
            '\\(=0.48(50)=24\\) W.<br><b>Sanity check:</b> tens of watts for a small core at line '
            'frequency is plausible. <b>Design meaning:</b> core material grade sets standing loss '
            'even at no load.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Material has \\(\\mu_r=2000\\). Find \\(B\\) when \\(H=50\\) A/m (\\(\\mu_0=4\\pi\\times10^{-7}\\) H/m).</p>',
  'answer': '<b>Answer: \\(B=126\\) mT.</b><br>\\(B=\\mu_0\\mu_r H=4\\pi\\times10^{-7}(2000)(50)=0.126\\) T.<br><b>Sanity check:</b> high \\(\\mu_r\\) gives '
            'hundreds of mT for small \\(H\\). <b>Design meaning:</b> saturation eventually limits '
            '\\(B\\) — check \\(B\\)–\\(H\\) curve knee.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Two B–H loops: narrow slim loop (material S) and wide fat loop (material H). '
          'Identify soft vs hard magnetic material, compare coercivity and core loss, and assign '
          'to transformer core vs permanent magnet.</p>',
  'answer': '<b>Answer:</b> S — soft, low \\(H_c\\), low loss → transformer. H — hard, high '
            '\\(H_c\\), high loss if used AC → permanent magnet. <b>Design meaning:</b> loop width '
            'is money lost as heat every cycle.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>Explain why motor laminations are thin sheets insulated from each other, linking '
          'eddy currents and frequency.</p>',
  'answer': '<b>Answer:</b> changing \\(B\\) induces circulating currents in bulk metal — eddy '
            'loss \\(\\propto\\) thickness² and frequency². Laminations break paths and raise '
            'resistance. <b>Design meaning:</b> higher speed/frequency motors need thinner '
            'laminations or powder cores.'}]

# ---------------------------------------------------------------------------
# Week 11 — composites, rule of mixtures, critical fibre length, anisotropy
# ---------------------------------------------------------------------------
EXTRA[11] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Longitudinal modulus of a continuous-fibre composite along fibres often follows:</p>',
  'options': ['Rule of mixtures on volume fractions',
              'Average of fibre and matrix densities only',
              'Fibre modulus alone, ignoring matrix',
              'Square root of matrix modulus only'],
  'answer': '<b>Answer: A.</b> \\(E_c\\approx V_f E_f+V_m E_m\\) in parallel model along fibres. '
            '<b>Design meaning:</b> fibres carry most axial load — align them with the primary '
            'stress.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Critical fibre length \\(l_c\\) is the length below which:</p>',
  'options': ['Fibres dissolve in the matrix',
              'Fibres pull out rather than fracture — poor load transfer',
              'The composite becomes isotropic',
              'Thermal expansion vanishes'],
  'answer': '<b>Answer: B.</b> Short fibres debond — ineffective reinforcement. <b>Design '
            'meaning:</b> chopped fibre composites need length well above \\(l_c\\).'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>CFRP: \\(V_f=0.60\\), \\(E_f=230\\) GPa, \\(E_m=3.5\\) GPa. Estimate \\(E_c\\) along '
          'fibres.</p>',
  'options': ['3.5 GPa', '139 GPa', '230 GPa', '233 GPa'],
  'answer': '<b>Answer: B.</b> \\(E_c=0.60(230)+0.40(3.5)=138+1.4=139.4\\) GPa. <b>Sanity '
            'check:</b> between \\(E_m\\) and \\(E_f\\), nearer fibre value. <b>Design '
            'meaning:</b> off-axis loading uses much lower modulus — anisotropy matters.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>A plate is quasi-isotropic in-plane because it uses woven fabric. A bolted joint '
          'loads the plate through-thickness. Is strength likely isotropic?</p>',
  'options': ['Yes — woven fabric removes all anisotropy',
              'No — through-thickness strength is matrix-dominated and much lower',
              'Yes — bolts load all directions equally',
              'Only if fibres are ceramic'],
  'answer': '<b>Answer: B.</b> In-plane quasi-isotropy does not fix interlaminar or bearing '
            'strength. <b>Design meaning:</b> specify bearing and interlaminar shear for bolted '
            'CFRP joints.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> composites can be tailored so stiffness is high in one '
          'direction and low in another by fibre orientation.</p>',
  'answer': '<b>Answer: True.</b> Anisotropy is a design freedom. <b>Design meaning:</b> laminates '
            'are built ply-by-ply — wrong angle wastes fibres.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because CFRP has excellent tensile strength, it will always '
          'outperform steel in compression in a slender strut.</p>',
  'answer': '<b>Answer: False.</b> Fibre buckling and microbuckling limit compression; joint '
            'bearing and instability matter. <b>Design meaning:</b> name the loading mode before '
            'screening on tensile data sheet values.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Glass fibre: \\(\\sigma_f=1.8\\) GPa, \\(d=12\\) µm, \\(\\tau_c=40\\) MPa. Estimate '
          'critical length \\(l_c=\\sigma_f d/(2\\tau_c)\\) in mm.</p>',
  'answer': '<b>Answer: \\(l_c\\approx0.27\\) mm \\(=270\\) µm.</b><br>\\(l_c=1.8\\times10^9(12\\times10^{-6})/(2\\times40\\times10^6)=0.00027\\) m.<br><b>Sanity check:</b> hundreds of '
            'microns — chopped fibres below this pull out. <b>Design meaning:</b> '
            'injection-moulded short glass must exceed \\(l_c\\) for decent strength.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Laminate: 50% 0° plies, 50% 90° plies, same \\(E\\) and thickness per ply. Estimate '
          'in-plane modulus \\(E_x\\) and \\(E_y\\) vs single-ply \\(E_0\\).</p>',
  'answer': '<b>Answer: \\(E_x=E_y\\approx0.5E_0\\) for equal thickness fractions (simplified '
            'ROM).</b><br>Equal bidirectional split averages axial response → quasi-isotropic '
            'in-plane, modulus about half the 0° value. <b>Design meaning:</b> ±45° and 0/90 '
            'stacks trade stiffness against shear and bearing response.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Stress–strain curves: bare matrix ductile low slope; unidirectional composite high '
          'initial slope then knee as matrix cracks; cross-ply lower slope. Explain knee and why '
          'cross-ply is less stiff on-axis.</p>',
  'answer': '<b>Answer:</b> knee — matrix microcracking, fibres still carry load. Cross-ply shares '
            'load between orientations → lower effective \\(E_x\\). <b>Design meaning:</b> '
            'first-ply failure is not final failure — but design limit often is taken there for '
            'stiffness.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>A drone arm needs high \\(E/\\rho\\) and fatigue resistance. Compare aluminium tube vs CFRP tube on index, anisotropy '
          'and joint design.</p>',
  'answer': '<b>Answer:</b> CFRP wins \\(E/\\rho\\) along fibres; requires lay-up aligned with bending axis; joints need bonded '
            'inserts or careful bearing design — not welded like Al. Al simpler to prototype and '
            'inspect. <b>Design meaning:</b> composite win is conditional on load path and '
            'manufacturability.'}]

# ---------------------------------------------------------------------------
# Week 12 — ceramics, Griffith, flaw size, thermal shock
# ---------------------------------------------------------------------------
EXTRA[12] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Griffith theory links brittle fracture stress to:</p>',
  'options': ['Flaw size and surface energy',
              'Melting temperature only',
              'Magnetic permeability',
              'Polymer \\(T_g\\)'],
  'answer': '<b>Answer: A.</b> \\(\\sigma_f\\propto1/\\sqrt{a}\\) — larger flaws lower strength. '
            '<b>Design meaning:</b> ceramic strength is flaw statistics, not a single handbook '
            'number.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Ceramics typically fail in tension because:</p>',
  'options': ['They yield then neck',
              'Cracks open — no plastic blunting',
              'They melt at room temperature',
              'They are magnetic'],
  'answer': '<b>Answer: B.</b> Low \\(K_{IC}\\), no dislocation plasticity — tensile cracks '
            'propagate. <b>Design meaning:</b> use ceramics in compression or with compressive '
            'prestress.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>Griffith: if flaw depth doubles, by what factor does theoretical \\(\\sigma_f\\) '
          'change?</p>',
  'options': ['Halves', 'Divides by \\(\\sqrt2\\approx0.71\\)', 'Doubles', 'Unchanged'],
  'answer': '<b>Answer: B.</b> \\(\\sigma_f\\propto a^{-1/2}\\). Double \\(a\\) → multiply by '
            '\\(1/\\sqrt2\\). <b>Sanity check:</b> same square-root logic as \\(K_I\\). <b>Design '
            'meaning:</b> grinding damage that doubles flaw depth costs ~30% strength.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>A ceramic tile has high compressive strength and is used as a floor tile. A thin '
          'ceramic shell is proposed for a tensile pressure vessel. What is the main concern?</p>',
  'options': ['Compressive strength will be too low',
              'Tensile flaw sensitivity — biaxial tension opens surface cracks',
              'Ceramics conduct electricity too well',
              'Density is too low'],
  'answer': '<b>Answer: B.</b> Compressive success does not transfer to tension-dominated pressure '
            'vessels. <b>Design meaning:</b> match ceramic architecture to stress sign — '
            'compression yes, tension only with massive quality control.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> thermal shock resistance of a brittle ceramic improves when '
          '\\(E\\) and \\(\\alpha\\) are low and fracture strength is high.</p>',
  'answer': '<b>Answer: True.</b> \\(R\\propto\\sigma_f/(E\\alpha)\\). <b>Design meaning:</b> '
            'firebricks are porous and compliant — not dense alumina blocks.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> because ceramics are hard, they are always tough in '
          'impact.</p>',
  'answer': '<b>Answer: False.</b> Hardness \\(\n'
            'eq\\) toughness; ceramics absorb little energy before crack growth. <b>Design '
            'meaning:</b> armour ceramics are paired with ductile backing — hardness alone '
            'shatters.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Alumina: \\(\\sigma_f=300\\) MPa with flaw \\(a=50\\) µm. If processing improves to '
          '\\(a=25\\) µm, estimate new \\(\\sigma_f\\) (Griffith scaling).</p>',
  'answer': '<b>Answer: \\(\\approx424\\) '
            'MPa.</b><br>\\(\\sigma_2/\\sigma_1=\\sqrt{a_1/a_2}=\\sqrt2\\) → \\(300\\sqrt2=424\\) '
            'MPa.<br><b>Sanity check:</b> halving flaw size raises strength ~41%. <b>Design '
            'meaning:</b> surface finish and handling are strength specifications.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Ceramic \\(\\sigma_f=200\\) MPa, \\(E=300\\) GPa, \\(\\alpha=8\\times10^{-6}\\)/°C. '
          'Compare thermal stress at \\(\\Delta T=200\\) °C if fully constrained '
          '(\\(\\sigma=E\\alpha\\Delta T\\)) to \\(\\sigma_f\\).</p>',
  'answer': '<b>Answer: \\(\\sigma=480\\) MPa \\(>200\\) MPa — thermal shock fracture '
            'risk.</b><br>\\(\\sigma=300\\times10^9(8\\times10^{-6})(200)=480\\) MPa.<br><b>Sanity '
            'check:</b> large \\(\\Delta T\\) on stiff low-\\(\\alpha\\) ceramic still exceeds '
            'strength. <b>Design meaning:</b> allow expansion or use graded / porous '
            'microstructure.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Weibull plot: ceramic A steep slope (high \\(m\\)), ceramic B shallow slope (low '
          '\\(m\\)). Interpret scatter in strength, reliability at 150 MPa design stress, and '
          'quality control implication.</p>',
  'answer': '<b>Answer:</b> high \\(m\\) — less scatter, predictable failure stress; low \\(m\\) — '
            'wide distribution, design must use low fractile strength. B needs more proof testing. '
            '<b>Design meaning:</b> ceramic design stress is statistical — not mean strength.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>Window glass is strong in compression in a frame but shatters on impact. Explain '
          'using flaw size, stress state and toughening options (tempered / laminated).</p>',
  'answer': '<b>Answer:</b> surface flaws in tension open easily; frame puts edge in compression. '
            'Impact bends pane → tensile surface stress. Tempering introduces compressive surface '
            'layer; lamination contains shards. <b>Design meaning:</b> glass design is flaw and '
            'stress-sign management, not average strength.'}]

# ---------------------------------------------------------------------------
# Week 13 — mixed classification, revision synthesis across weeks
# ---------------------------------------------------------------------------
EXTRA[13] = [{'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>A part must carry load, resist corrosion and minimise mass. The first selection step '
          'is:</p>',
  'options': ['Pick the cheapest metal',
              'List failure modes and translate to measurable property constraints',
              'Maximise hardness',
              'Choose the highest melting point'],
  'answer': '<b>Answer: B.</b> Failure modes → properties → screen. <b>Design meaning:</b> Week 13 '
            'synthesis is the six-step selection workflow end-to-end.'},
 {'tags': ('Multiple choice', 'Quick'),
  'stem': '<p>Which pairing is correct?</p>',
  'options': ['Creep — cyclic stress below yield',
              'Fatigue — steady load at high homologous temperature',
              'Fracture mechanics — flaw size and \\(K_{IC}\\)',
              'Hall–Petch — polymer \\(T_g\\)'],
  'answer': '<b>Answer: C.</b> A is fatigue; B is creep; D is grain size vs yield. <b>Design '
            'meaning:</b> naming the mechanism selects the correct week and property.'},
 {'tags': ('Multiple choice', 'One step'),
  'stem': '<p>Steel beam: yield governs at 280 MPa working stress (\\(\\sigma_y=350\\) MPa). A 2 '
          'mm deep crack is found; \\(K_{IC}=55\\) MPa·√m, \\(Y=1.2\\), \\(\\sigma=280\\) MPa. '
          'Does fracture govern instead?</p>',
  'options': ['No — \\(K_I\\approx27\\) MPa·√m \\(<55\\)',
              'Yes — \\(K_I\\approx85\\) MPa·√m',
              'No — yield always governs',
              'Yes — any crack causes instant failure'],
  'answer': '<b>Answer: A.</b> \\(a=0.002\\) m → \\(K_I=1.2(280)\\sqrt{\\pi(0.002)}\\approx27\\) '
            'MPa·√m \\(<55\\). Yield margin is thin; fracture margin is also finite. <b>Design '
            'meaning:</b> revision combines Weeks 2 and 4 — compare governing modes.'},
 {'tags': ('Multiple choice', 'Trap'),
  'stem': '<p>A student screens a vibrating aluminium bracket on \\(\\sigma_y\\) only because '
          'static stress is 30% of yield. Best critique?</p>',
  'options': ['Correct — yield margin is ample',
              'Missed fatigue — need stress range vs S–N or endurance approach for Al',
              'Should use \\(E/\\rho\\) only',
              'Aluminium cannot vibrate'],
  'answer': '<b>Answer: B.</b> No endurance limit in Al — cyclic life must be quoted. <b>Design '
            'meaning:</b> synthesis questions punish single-property screening.'},
 {'tags': ('True/false', 'Quick'),
  'stem': '<p><b>True or false:</b> polymers, metals and ceramics can all be classified by bond '
          'type, which predicts whether they are likely to be ductile, creep-prone or '
          'flaw-sensitive.</p>',
  'answer': '<b>Answer: True.</b> Metallic — ductile conductors; ionic/covalent ceramics — '
            'brittle; polymers — viscoelastic, temperature-sensitive. <b>Design meaning:</b> Week '
            '1 bonding still frames Week 13 integration.'},
 {'tags': ('True/false', 'Trap'),
  'stem': '<p><b>True or false:</b> a material with the highest specific stiffness always wins the '
          'final selection once constraints are met.</p>',
  'answer': '<b>Answer: False.</b> Cost, toughness, corrosion, process and anisotropy may '
            'eliminate the index winner. <b>Design meaning:</b> defend the choice with constraints '
            'satisfied and trade-offs named.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Synthesis: tie rod — Ti (\\(\\sigma_y/\\(\\rho=184\\)) vs Al (\\(104\\)) vs steel (\\(45\\)). Service 200 MPa, marine corrosion, '
          'weld required. Rank technically on index, then state likely winner after '
          'constraints.</p>',
  'answer': '<b>Answer:</b> index: Ti \\(>\\) Al \\(>\\) steel. Marine + weld may favour Al alloy '
            '(protected or marine grade) or Ti if budget allows; plain steel needs coating '
            'maintenance. <b>Design meaning:</b> calculation plus environment decides — not index '
            'alone.'},
 {'tags': ('Short calculation', 'Written'),
  'stem': '<p>Plate \\(\\sigma_y=500\\) MPa, \\(K_{IC}=40\\) MPa·√m, working \\(\\sigma=200\\) '
          'MPa, \\(Y=1.0\\). Find \\(a_c\\) and safety factor on flaw size if inspection finds 2 '
          'mm.</p>',
  'answer': '<b>Answer: \\(a_c\\approx12.7\\) mm; flaw 2 mm gives safety factor 6.4 on crack '
            'length.</b><br>1. \\(a_c=\\f'
            'rac1\\pi(40/200)^2=0.01273\\) m \\(=12.7\\) mm.<br>2. SF on length '
            '\\(=a_c/a=12.7/2=6.4\\) (SF on \\(a\\) is 40.5).<br>3. Yield margin '
            '\\(=500/200=2.5\\) — fracture not governing at 2 mm.<br><b>Sanity check:</b> critical '
            'flaw is an order of magnitude above inspection finding. <b>Design meaning:</b> '
            'combine strength and fracture in one design check.'},
 {'tags': ('Diagram interpretation', 'Written'),
  'stem': '<p>Mixed figure: stress–strain metal curve, S–N steel line with endurance limit, and '
          'Ashby \\(E\\)–\\(\\rho\\) chart marked. A automotive crash rail must absorb energy in bending with minimum '
          'mass. Which diagram feature guides material choice and which failure mode is '
          'irrelevant?</p>',
  'answer': '<b>Answer:</b> Ashby → light alloys / AHSS by \\(E^{1/2}/\\(\\rho\\) or energy metrics; stress–strain area → toughness for crumple. S–N largely '
            'irrelevant — single or few impacts, not high-cycle fatigue. <b>Design meaning:</b> '
            'revision is matching tool to failure mode.'},
 {'tags': ('Short explanation', 'Written'),
  'stem': '<p>Write a six-line materials selection argument for a kitchen saucepan base: function, '
          'constraints, properties, two candidates, trade-off, decision.</p>',
  'answer': '<b>Answer:</b> Function — even heating on induction/gas. Constraints — food contact, '
            '\\(\\Delta T\\) cycling, manufacturable disc. Properties — thermal conductivity, '
            'thermal shock, corrosion, joinability. Candidates — copper-clad stainless '
            '(conductivity + corrosion) vs thick aluminium (lighter, anodised). Trade-off — Cu '
            'cost and weight vs Al softness. Decision — clad stainless for durability and '
            'induction compatibility if ferritic layer included. <b>Design meaning:</b> full-mark '
            'Week 13 answers read as a structured defence, not a material name.'}]
