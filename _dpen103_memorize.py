"""Know-cold memorisation blocks for DPEN103 weekly lessons (additive only)."""

MEMORIZE = {
    1: [
        r"What is this material made of, and what does that predict?",
        r"Metallic bonding → delocalised electrons, conducts electricity, ductile and formable.",
        r"Ionic bonding → hard, brittle, electrical insulator.",
        r"Covalent bonding → very stiff, brittle, very high melting point.",
        r"FCC: \(n=4\) atoms per cell, APF \(0.74\), 12 neighbours. BCC: \(n=2\), APF \(0.68\), 8 neighbours.",
        r"\(\rho = nA/(V_c N_A)\) with \(V_c=a^3\) and lattice parameter \(a\) in centimetres.",
        r"Design path: function → property targets with numbers → candidate materials.",
    ],
    2: [
        r"How much load can this material take, and what happens on the way to failure?",
        r"\(\sigma = F/A\) and \(\varepsilon = \Delta L/L_0\).",
        r"Young's modulus \(E\) is the slope of the elastic line — stiffness.",
        r"Yield strength \(\sigma_y\) is the design limit; UTS is the peak; fracture follows necking.",
        r"Resilience = area under the elastic part. Toughness = full area to fracture.",
        r"Engineering stress uses the original area; true stress uses the current area in the neck.",
    ],
    3: [
        r"Why is a real metal so much weaker than a perfect crystal, and how do we use that?",
        r"Dislocations move along slip planes — that motion is plastic deformation.",
        r"Vacancy concentration rises with temperature, so diffusion speeds up when hot.",
        r"Hall–Petch: yield strength scales with \(1/\sqrt{d}\) for grain size \(d\).",
        r"Strengthening blocks dislocations: grain refinement, solid solution, strain hardening, precipitation.",
    ],
    4: [
        r"Cracks and fatigue cause failure while nominal stress stays below yield strength.",
        r"A crack concentrates stress at its tip.",
        r"\(K = \sigma\sqrt{\pi a}\). Fast fracture when \(K \ge K_{Ic}\).",
        r"Fatigue: a crack grows under repeated load below yield. Steel has an endurance limit on the S–N curve.",
        r"Fatigue resistance: smooth surface finish, compressive residual stress, generous fillet radii.",
    ],
    5: [
        r"What does heat do to a part that is already carrying load?",
        r"Creep: slow extension under steady load at high \(T/T_m\). Design uses the secondary (steady) slope.",
        r"Thermal expansion \(\Delta L/L = \alpha \Delta T\). Full restraint gives \(\sigma \approx E\alpha\Delta T\).",
        r"Thermal shock resistance is higher when conductivity is high and the material can yield.",
        r"A phase is a uniform region; microstructure is how those regions are arranged.",
    ],
    6: [
        r"At this composition and this temperature, what is actually in there?",
        r"Plot composition and temperature, then read the phase label for that region.",
        r"In a two-phase field, draw a horizontal tie-line; phase compositions sit at the endpoints.",
        r"Lever rule: fraction of a phase = length of opposite segment ÷ full tie-line length.",
        r"The eutectic is the lowest-melting composition; it freezes as two solid phases at one temperature.",
    ],
    7: [
        r"How much freedom do the chains have at the service temperature?",
        r"Below \(T_g\): glassy and brittle. Above \(T_g\): rubbery and tough. Solid on both sides.",
        r"Linear chains slide and melt; branched chains pack poorly; cross-linked chains form a network solid.",
        r"Polymers creep under constant load and relax under constant stretch at room temperature.",
        r"Polymer design includes load duration and operating temperature.",
    ],
    8: [
        r"Which material fits, and which alternatives were ruled out?",
        r"Function → failure modes → property targets → shortlist → process and cost → decide.",
        r"Steel and aluminium share similar stiffness-to-weight; corrosion, formability and cost break the tie.",
        r"Name the failure mode first; the screening property follows from it.",
        r"Justify the choice: rejected candidates, the constraint each failed, the trade-off accepted, a backup.",
    ],
    9: [
        r"How freely can charge move through this material, and what changes that?",
        r"Conductivity \(\sigma = n q \mu\) — carrier count, charge and mobility.",
        r"Resistivity \(\rho\) is a material property; resistance \(R = \rho L/A\) belongs to the object.",
        r"Metal conductivity falls when heated (mobility drops). Semiconductor conductivity rises (more carriers).",
        r"Hall voltage balances the magnetic push on carriers → carrier sign and concentration.",
    ],
    10: [
        r"What shape is the B–H loop, and what job does that shape suit?",
        r"Saturation, remanence and coercivity are read from the hysteresis loop.",
        r"Loop area = energy lost as heat per magnetising cycle.",
        r"Soft magnetic materials: narrow loop, low coercivity — transformers and motors.",
        r"Hard magnetic materials: wide loop, high remanence and coercivity — permanent magnets.",
    ],
    11: [
        r"How much does each ingredient contribute, and in which direction?",
        r"Longitudinal stiffness: \(E_c \approx V_f E_f + V_m E_m\).",
        r"Transverse stiffness: reciprocals add; the matrix dominates.",
        r"Critical fibre length \(l_c = \sigma_f d / (2\tau_i)\).",
        r"Composites: high stiffness per weight along fibres; watch anisotropy, joining, delamination and cost.",
    ],
    12: [
        r"How big is the worst flaw, and is the part in tension?",
        r"Ceramics fracture when a crack tip stress reaches the fracture toughness limit.",
        r"\(\sigma_f \approx K_{Ic}/\sqrt{\pi a}\) — larger flaw \(a\) means lower failure stress.",
        r"Ceramics carry far more load in compression than in tension.",
        r"Ceramic design: fine surface finish, compressive loading, prestressed surface, rounded corners, proof testing.",
    ],
    13: [
        r"What kind of question is this, and which week does it belong to?",
        r"Read the signal words → name the topic week → choose the governing equation.",
        r"Full answer: classify the problem → state assumptions and units → compute → check the trend → design implication.",
        r"Formula families: \(\sqrt{a}\) for cracks, \(1/\sqrt{d}\) for grains, Arrhenius for temperature, volume fractions for mixtures.",
        r"Revision rhythm: test cold, keep cards that collapse, space repeats at 2, 7 and 21 days, shuffle the topics.",
    ],
}


def render_week(week_num: int) -> str:
    items = MEMORIZE[week_num]
    lis = "\n".join(f"  <li>{text}</li>" for text in items)
    return f'''<section class="memorize" id="memorize">
<h2>Know cold — say these from memory</h2>
<p class="intro">Cover the list and recite each line aloud. Then open the page and check. Five minutes, once per study session.</p>
<ol class="mem-list">
{lis}
</ol>
</section>
'''
