"""Narrative teaching sections to add to DPEN103 weekly lessons (additive only)."""

TEACHING = {
1: [
 ("Why bonding comes first",
  r"""<p>Before you look up any property in a handbook, ask what is holding the atoms together. That single question narrows the field dramatically. Metals share their outer electrons across the whole solid, so charge can move and layers of atoms can slide — that is what bending a bar actually is. Ionic solids transfer electrons completely, which locks the ions into a rigid pattern with no free charge. Covalent solids share electrons in fixed directions, which makes them stiff and hard to break apart. Polymers are held together mainly by weak forces between long molecules, which is why they soften and melt at temperatures metals would not notice.</p>
<p>The exam rarely asks you to draw electron orbitals. It asks you to predict behaviour from the bond type. If someone tells you a ceramic is ionic, you should already expect hard, brittle and insulating before you are given a single number.</p>"""),
 ("From atoms to a repeating stack",
  r"""<p>Most engineering metals are crystalline: the atoms sit in a pattern that repeats. Think of stacking oranges in a crate — the pattern matters. Face-centred cubic (FCC) puts an atom on each corner of a cube and one in the centre of every face. Body-centred cubic (BCC) uses the corners plus one atom at the centre. Hexagonal close-packed (HCP) stacks hexagonal layers in an ABAB pattern.</p>
<p>The table in the cards gives atoms per cell, neighbours touched and packing factor. Those numbers are geometry. What changes how a metal behaves in service is how many easy sliding directions the pattern offers. FCC metals such as aluminium and copper tend to be easier to press and draw because they have more slip systems. HCP metals such as magnesium can be strong but less forgiving to form at room temperature.</p>"""),
 ("Density as a counting exercise",
  r"""<p>Once you know what is inside the unit cell and how big the cell is, density is just mass divided by volume. The formula \(\rho = nA/(V_c N_A)\) looks intimidating only because of the units. \(n\) counts atoms in one cell (4 for FCC, 2 for BCC — memorise those). \(A\) is atomic mass in g/mol. \(V_c\) is cell volume, and for a cubic cell \(V_c = a^3\) with \(a\) in centimetres, not nanometres.</p>
<p>Work through one full calculation slowly, with units on every line. After that, many questions only need proportionality reasoning: same structure and same atomic mass, but a 2% larger lattice parameter means about 6% less density because volume scales as \(a^3\).</p>"""),
 ("Turning a design job into numbers",
  r"""<p>Week 1 also introduces the habit you will use in Week 8 and in the exam: translate what the part must do into measurable targets before naming a material. "Strong" is not a target — yield strength in MPa is. "Stiff" means a value of \(E\). "Light" means density once strength and stiffness are satisfied.</p>
<p>Practice writing one sentence of function, then a short list of property targets with numbers or inequalities. The cards below turn that habit into a table you can revise from.</p>"""),
],
2: [
 ("What the test machine is actually measuring",
  r"""<p>Take a standard tensile specimen and pull it until it breaks. The machine records force and extension. Divide force by the original cross-sectional area and you get engineering stress \(\sigma\). Divide extension by the original length and you get engineering strain \(\varepsilon\). Those two definitions exist so that a result from a small lab sample applies to a larger part carrying the same stress level.</p>
<p>Plot stress against strain and you get the curve that dominates this subject. Every landmark on that curve — the slope, the yield point, the peak, the fracture point — has a name, a formula and a design meaning. Exam questions usually want all three.</p>"""),
 ("Reading the straight part first",
  r"""<p>The first straight section is elastic behaviour: load it, unload it, and the bar returns to its original length. The slope is Young's modulus \(E\), stiffness. Steel near 210 GPa deflects much less than aluminium near 70 GPa for the same stress. Stiffness controls sag and vibration; it does not tell you when permanent damage starts.</p>
<p>A common mistake in design is to specify a "stronger" alloy when the problem is deflection. If the beam sags too much, raising yield strength does not help — you need higher \(E\) or a different shape (more depth, second moment of area from DPEN102).</p>"""),
 ("Yield, peak and fracture — in order",
  r"""<p>Past the elastic limit the metal flows. Yield strength \(\sigma_y\) is where permanent set begins; for design this is usually the working limit. The curve then rises to a peak: ultimate tensile strength (UTS). After the peak the bar necks — one region thins — so the engineering stress falls even though the true stress in the neck is still rising.</p>
<p>Fracture is where the bar separates, often at a lower engineering stress than the UTS because the load is carried on a much smaller area. When the yield point is rounded, use the 0.2% offset construction: a line parallel to the elastic slope starting at 0.002 strain; where it cuts the curve is \(\sigma_y\).</p>"""),
 ("Energy under the curve",
  r"""<p>Area under the stress–strain curve is energy absorbed per unit volume. The triangle under the elastic part alone is resilience — energy stored and returned, what a spring needs. The full area to fracture is toughness — energy absorbed before breaking, what a crash structure needs.</p>
<p>A high-strength brittle alloy can enclose less area than a softer ductile one. Strength and toughness pull in different directions. That tension reappears in Weeks 4 and 12.</p>"""),
],
3: [
 ("Why perfect crystals are not the whole story",
  r"""<p>Calculate the strength of a perfect crystal from bond stiffness and you get enormous numbers — far above any real metal. Real metals are weak by comparison because their crystals contain defects. The most important for strength and ductility is the dislocation: an extra half-plane of atoms wedged into the lattice. Under stress, dislocations move. That motion is plastic deformation.</p>
<p>Without movable dislocations a metal would be brittle like a ceramic. With too many dislocations pinned in place it becomes hard but less ductile. Materials engineering is largely about managing defects, not eliminating them.</p>"""),
 ("Vacancies and diffusion",
  r"""<p>A vacancy is a missing atom site. At any temperature above absolute zero some sites are empty, and the concentration rises with temperature. Atoms can jump into vacant sites, so vacancies enable diffusion — atoms migrating through the solid. That matters for carburising, homogenising alloys and creep at high temperature.</p>
<p>Do not treat vacancies as a separate topic from dislocations. Both are departures from perfection, and both change properties in predictable ways.</p>"""),
 ("Strengthening by blocking motion",
  r"""<p>If dislocation motion is what makes metals yield, stopping or slowing that motion raises strength. Solid-solution strengthening puts oversized or undersized atoms in the lattice so dislocations cannot glide easily. Grain boundaries block dislocations because the crystal orientation changes across the boundary. Cold working creates so many dislocations that they tangle and jam each other.</p>
<p>Each method trades ductility for strength. That trade-off is the central pattern of Week 4 as well.</p>"""),
],
4: [
 ("When yield is not the failure mode",
  r"""<p>Week 2 taught you to design below yield. Many failures happen while the nominal stress is still below \(\sigma_y\). Two mechanisms dominate: a sharp crack concentrating stress, and cyclic loading that damages the material a little on each cycle.</p>
<p>Linear elastic fracture mechanics asks: given a crack of length \(a\) in a part under stress \(\sigma\), what is the stress intensity \(K\)? When \(K\) reaches the material's fracture toughness \(K_{Ic}\), fast fracture follows. A small crack can be fatal at a stress the uncracked material would survive.</p>"""),
 ("Fatigue: death by repetition",
  r"""<p>Apply a stress once and the part may be fine. Apply it a million times at half the yield stress and it may still fail. Fatigue limit and S–N curves describe life versus stress amplitude. The curve has an endurance limit for steels — below it, life is effectively infinite — but many alloys have no such knee.</p>
<p>Surface finish, stress concentration and mean stress all shift the curve. Design against fatigue means keeping working stress below the allowable for the required life, not just below yield.</p>"""),
 ("Strengthening mechanisms revisited",
  r"""<p>Cold work, solid solution, precipitation hardening and grain refinement all raise yield by impeding dislocations. Each makes the stress–strain curve taller and often narrower — more strength, less ductility. Pick a process to match the failure mode you fear: do not cold-work a part that must absorb impact energy.</p>"""),
],
5: [
 ("Creep: slow motion at high temperature",
  r"""<p>Hold a metal below yield but at high temperature (high relative to its melting point) and it slowly extends. Creep curves show strain versus time: primary (decelerating), secondary (steady rate), tertiary (accelerating to failure). Design extrapolations usually use the secondary slope.</p>
<p>Polymers creep at room temperature; steels do not notice room temperature. Always think in \(T/T_m\), not absolute comfort temperature.</p>"""),
 ("Thermal expansion and constrained stress",
  r"""<p>Heating makes most solids expand by \(\Delta L/L = \alpha \Delta T\). If a bar is free to expand, no stress appears. If it is clamped, expansion is prevented and stress builds: \(\sigma \approx E \alpha \Delta T\) for full restraint. A 100 °C rise in a restrained steel bar can produce stress near yield.</p>
<p>Thermal mismatch between joined materials (steel bolt in aluminium, ceramic coating on metal) creates stress even when each piece alone would be fine.</p>"""),
 ("Phases as a preview",
  r"""<p>Week 5 introduces phase as a region with uniform structure and composition. Microstructure is how those regions are arranged. Same phases, different arrangement — different properties. That distinction becomes the whole of Week 6 on phase diagrams.</p>"""),
],
6: [
 ("A phase diagram is a map",
  r"""<p>For a binary alloy, composition is the horizontal axis and temperature the vertical. Each region is labelled with the phase(s) stable there. Boundaries are where reactions occur: liquid freezes, solid solutions dissolve or precipitate. Given a composition and temperature, locate the point and read the phases.</p>"""),
 ("The tie-line and lever rule",
  r"""<p>In a two-phase field the tie-line connects the compositions of the two coexisting phases at that temperature. The lever rule finds the fraction of each: the lengths on the tie-line are inversely proportional to the amounts. This is not algebra for its own sake — it answers "how much pro-eutectic solid versus eutectic microconstituent?"</p>"""),
 ("Reading cooling paths",
  r"""<p>Follow a vertical line (fixed composition, falling temperature) and narrate what forms at each crossing. The microstructure you predict on the way down is what you see in the exam sketch questions. Label phases, estimate fractions, then connect to expected properties.</p>"""),
],
7: [
 ("Long chains, not small molecules",
  r"""<p>Polymers are macromolecules — repeating units strung into chains thousands of units long. Properties come from chain chemistry, how folded or aligned the chains are, and how much they can move at the service temperature.</p>"""),
 ("Glass transition and melting",
  r"""<p>Below the glass transition temperature \(T_g\), amorphous regions are rigid; above \(T_g\) they soften dramatically. Crystalline regions melt at \(T_m\). A rubber ball is above its \(T_g\); a PVC pipe is below. The same polymer family can span both behaviours depending on chemistry and processing.</p>"""),
 ("Viscoelasticity",
  r"""<p>Polymers creep and stress-relax at room temperature. Load them and they continue to deform. Fix the deflection and the reaction force drops over time. Design with polymers must specify temperature and time, not just stress.</p>"""),
],
8: [
 ("The question engineers actually get",
  r"""<p>Week 8 is synthesis: given a function and constraints, pick a material and defend it. The marks are in the rejection of alternatives. "Use aluminium" scores little. "Aluminium because density must stay below X, yield above Y, and steel fails on corrosion in this environment" scores.</p>"""),
 ("A workable order of steps",
  r"""<p>State function and constraints in numbers. List failure modes (yield, fatigue, creep, fracture, corrosion, wear, deflection). Turn each into a property target. Shortlist candidates that meet all targets. Compare on cost, manufacture and environment. Reject each loser with a specific property it fails.</p>"""),
 ("Ashby charts without mystique",
  r"""<p>Log-log plots of properties (strength vs density, \(E\) vs \(\rho\)) let you see trade-offs. A material on the upper-left of strength–density is attractive for light strong parts. Charts do not replace calculations — they narrow the search before you calculate.</p>"""),
],
9: [
 ("Back to free electrons",
  r"""<p>Metallic bonding left electrons free to move. Apply a voltage and they drift — electrical conduction. Resistivity \(\rho\) (or conductivity \(\sigma = 1/\rho\)) measures how easily. Impurities, temperature and crystal defects scatter electrons and raise resistivity.</p>"""),
 ("Metals vs semiconductors vs insulators",
  r"""<p>Metals have partially filled bands — many empty states at the same energy, so electrons move easily. Insulators have a large gap with no states available. Semiconductors have a small gap; heating promotes electrons across the gap, so conductivity rises with temperature — opposite to metals.</p>"""),
 ("Hall effect and carrier type",
  r"""<p>The Hall voltage tells you whether the main carriers are electrons or holes and gives carrier concentration. It connects measured voltage to the physics of conduction in doped semiconductors.</p>"""),
],
10: [
 ("Magnetism from aligned moments",
  r"""<p>Atomic magnetic moments align in ferromagnetic materials (iron, nickel, cobalt) below the Curie temperature. Paramagnetic materials weakly follow a field; diamagnetic materials weakly oppose it. Engineering use is almost always ferromagnetic or ferrite-based.</p>"""),
 ("The B–H loop tells the application",
  r"""<p>Magnetise and demagnetise a ferromagnetic sample and plot flux density \(B\) against field \(H\). The loop's area is energy lost per cycle — hysteresis loss. Narrow loops suit transformer cores (frequent reversal, low loss). Wide loops suit permanent magnets (high remanence, high coercivity).</p>"""),
 ("Soft vs hard magnetic materials",
  r"""<p>Soft magnetic: easy to magnetise and demagnetise, low coercivity, used where the field reverses often. Hard magnetic: high coercivity and remanence, used where the magnet must stay magnetised. Read the loop shape; it predicts the job.</p>"""),
],
11: [
 ("Why combine materials",
  r"""<p>Fibres are stiff and strong in tension but cannot be shaped alone. A matrix binds fibres, transfers load into them and protects the surface. Together they beat either component — provided the load direction matches the fibre direction.</p>"""),
 ("Rule of mixtures — longitudinal",
  r"""<p>For loading along the fibres, \(E_c \approx V_f E_f + V_m E_m\) and strength follows similar volume-fraction weighting (with fibre alignment and packing assumptions stated). The composite inherits most of the fibre stiffness in that direction.</p>"""),
 ("Direction matters",
  r"""<p>Transverse and shear properties are matrix-dominated and much lower. Critical fibre length ensures load transfers into the fibre before it pulls out. A composite question always asks: which direction is loaded, and what fraction is fibre?</p>"""),
],
12: [
 ("Strong in compression, risky in tension",
  r"""<p>Ceramics and glasses excel in compression but fail easily in tension because cracks open and propagate. Their tensile strength is not a fixed material constant — it depends on the largest flaw present, described by Griffith's approach.</p>"""),
 ("Flaw size controls strength",
  r"""<p>\(\sigma_f \approx K_{Ic}/\sqrt{\pi a}\): larger flaw \(a\), lower failure stress. Surface finish and handling matter. Design keeps ceramics in compression, avoids shock, and rounds corners to reduce stress concentration.</p>"""),
 ("Thermal shock",
  r"""<p>Low thermal conductivity gives steep temperature gradients; restraint gives thermal stress; lack of ductility means no relief by yielding. Ceramics fail in thermal shock when \(\Delta T\) exceeds a material- and geometry-dependent limit.</p>"""),
],
13: [
 ("Classification before calculation",
  r"""<p>In the exam, read the question and classify it: stress–strain? phase diagram? fatigue? selection? polymer \(T_g\)? composite rule of mixtures? Misclassification sends you to the wrong equations even if your maths is sound.</p>"""),
 ("Building the solution in layers",
  r"""<p>State what is given and what is asked. Draw the diagram if one applies. Write the governing relation before numbers. Substitute with units. Check magnitude and units on the answer. For selection questions, write property targets before material names.</p>"""),
 ("Cross-week links to watch",
  r"""<p>Stress from DPEN102 meets yield from Week 2. Dislocations from Week 3 explain strengthening in Week 4. Phase diagrams from Week 6 explain heat-treated microstructures in selection questions. Electrical and magnetic weeks both return to Week 1 bonding. Revision is seeing one chain, not thirteen separate lists.</p>"""),
],
}


def render_week(week_num):
    blocks = TEACHING[week_num]
    articles = []
    for title, html in blocks:
        articles.append(f'<article class="teach-block"><h3>{title}</h3>\n{html}</article>')
    body = '\n'.join(articles)
    return f'''<section class="teach" id="teach">
<h2>Working through the week</h2>
<p class="intro">Read this section first if the topic is new. It builds the ideas in order. Everything below — the glossary, cards, worked examples and exam practice — stays as your summary and drill.</p>
{body}
</section>
'''
