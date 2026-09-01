"""Narrative teaching sections for DPEN103 weekly lessons."""

TEACHING = {
1: [
 ("The four ways atoms bond",
  r"""<p>Every solid is held together by forces between its atoms. Engineers classify these forces into four bond types, and the type largely determines what the material will do in service.</p>
<p>In a <b>metallic</b> bond, the outer electrons are shared across the whole solid rather than belonging to individual atoms. Those delocalised electrons carry electric current, reflect light (which is why metals look shiny), and allow atomic planes to slide past one another. That sliding is what we call plastic deformation — a metal bar bends because its layers can move.</p>
<p>In an <b>ionic</b> bond, one atom gives up an electron and another takes it. The resulting positive and negative ions lock into a rigid three-dimensional pattern. With no free electrons, ionic solids are electrical insulators. The locked geometry also resists sliding, so ionic ceramics tend to be hard and brittle.</p>
<p>In a <b>covalent</b> bond, electrons are shared between specific neighbouring atoms in fixed directions. Diamond is the extreme case: every carbon atom is tied to four neighbours in a stiff network, giving enormous hardness and a very high melting point. Most engineering ceramics contain strong covalent character.</p>
<p><b>Secondary bonds</b> — van der Waals forces and hydrogen bonding — are much weaker. They hold polymer chains to one another. Because the forces are weak, polymers soften and melt at temperatures far below those of metals.</p>
<p>Knowing the bond type lets you predict conductivity, stiffness, ductility and melting behaviour before opening a data book.</p>"""),
 ("How metal atoms pack in crystals",
  r"""<p>Most engineering metals are <b>crystalline</b>: their atoms sit in a repeating three-dimensional pattern. The smallest repeating box is the <b>unit cell</b>. Copy that box in all directions and the whole crystal is built.</p>
<p>Three packing patterns dominate metals. In <b>face-centred cubic (FCC)</b>, atoms sit on each corner of a cube and at the centre of every face. Aluminium, copper and nickel use this structure. In <b>body-centred cubic (BCC)</b>, atoms occupy the eight corners plus one at the cube centre — iron at room temperature and chromium are examples. In <b>hexagonal close-packed (HCP)</b>, atoms form hexagonal layers stacked in an ABAB sequence; magnesium, zinc and titanium crystallise this way.</p>
<p>Each structure has a characteristic number of atoms per unit cell, a coordination number (how many neighbours each atom touches), and an atomic packing factor (APF) — the fraction of cell volume actually filled by atoms. FCC and HCP both reach APF 0.74, the maximum for equal spheres; BCC reaches 0.68.</p>
<p>Packing geometry also influences how easily a metal deforms. FCC metals offer many slip systems — directions along which atomic planes can glide — and are therefore relatively easy to press, draw and forge. HCP metals have fewer slip systems at room temperature and can be harder to form, even though their packing fraction matches FCC.</p>"""),
 ("Density from the unit cell",
  r"""<p>Theoretical density follows directly from what sits inside the unit cell and how large that cell is:</p>
<p class="fml">\[\rho=\frac{nA}{V_c N_A}\]</p>
<p>Here \(n\) is the number of atoms belonging to one cell (4 for FCC, 2 for BCC, 6 for HCP), \(A\) is the atomic mass in g/mol, \(V_c\) is the cell volume, and \(N_A = 6.022\times10^{23}\) mol\(^{-1}\) converts between atom scale and gram scale.</p>
<p>For a cubic cell, \(V_c = a^3\), where \(a\) is the lattice parameter. Because volume depends on the cube of length, the lattice parameter must be converted to centimetres before cubing — a value quoted in nanometres must be multiplied by \(10^{-7}\) to obtain centimetres.</p>
<p>A worked calculation proceeds line by line: identify \(n\) from the crystal structure, convert \(a\), compute \(V_c\), find the mass of atoms in the cell, then divide. Sanity checks matter: aluminium is near 2.7 g/cm³, iron near 7.9 g/cm³, and lead near 11 g/cm³. An answer orders of magnitude away usually means a unit conversion or a wrong value of \(n\).</p>
<p>When two alloys share the same structure and similar chemistry, density scales inversely with \(a^3\). A lattice parameter only 2% larger lowers density by roughly 6%.</p>"""),
 ("Translating design requirements into properties",
  r"""<p>Materials selection begins with what the part must do, not with a material name. Each function maps to a measurable property.</p>
<p>A bracket that must return to shape after loading is controlled by <b>yield strength</b> — the stress at which permanent deformation begins. A beam that must limit sag is controlled by <b>Young's modulus</b> \(E\), which governs elastic deflection. A component where mass matters is controlled by <b>density</b> \(\rho\), once strength and stiffness targets are met. A part exposed to salt spray needs <b>corrosion resistance</b>. A grounding strap needs <b>electrical conductivity</b>.</p>
<p>Each target should be written with a number or an inequality: yield strength above 250 MPa, deflection below 2 mm, density below 3 g/cm³. With targets stated, candidate materials can be screened systematically and alternatives rejected on specific grounds.</p>"""),
],
2: [
 ("Engineering stress and strain",
  r"""<p>A standard tensile test pulls a machined specimen until it fractures while recording force and extension. Two normalised quantities are defined so that results from a small laboratory coupon apply to a full-size component carrying the same stress level.</p>
<p><b>Engineering stress</b> is force divided by the original cross-sectional area: \(\sigma = F/A_0\). When force is in newtons and area in square millimetres, stress comes out directly in megapascals (MPa).</p>
<p><b>Engineering strain</b> is extension divided by the original gauge length: \(\varepsilon = (L - L_0)/L_0\). Strain is a ratio of lengths, so it has no units. A strain of 0.01 means the bar has stretched by 1% of its original length.</p>
<p>Plotting engineering stress against engineering strain gives the tensile curve — the central diagram of mechanical metallurgy. Every feature on that curve corresponds to a physical event inside the material and to a design limit.</p>"""),
 ("Elastic deformation and Young's modulus",
  r"""<p>At low stress the relationship between stress and strain is linear. Load the bar, unload it, and it returns to its original length. This reversible region is <b>elastic deformation</b>.</p>
<p>The slope of the elastic line is <b>Young's modulus</b> \(E\), also called the modulus of elasticity or stiffness. Hooke's law states \(\sigma = E\varepsilon\) within this region. Steel has \(E \approx 210\) GPa; aluminium has \(E \approx 70\) GPa. For the same stress, steel deflects about one third as much.</p>
<p>Stiffness governs how much a structure sags, vibrates or flexes under load. It is set mainly by bonding and crystal structure, so heat treatment changes yield strength dramatically while leaving \(E\) almost unchanged. When a design problem is dominated by excessive deflection, the remedy is higher \(E\), a stiffer section shape, or both — not simply a higher-yield alloy.</p>"""),
 ("Yield, necking and fracture",
  r"""<p>Beyond the elastic limit the metal undergoes <b>plastic deformation</b> — permanent shape change. The stress at which this begins is the <b>yield strength</b> \(\sigma_y\), and it is the usual design limit for ductile metals.</p>
<p>When the stress–strain curve shows a gradual bend rather than a sharp corner, yield is defined by the <b>0.2% offset method</b>: draw a line parallel to the elastic slope starting at a strain of 0.002 (0.2%); the stress where this line crosses the curve is \(\sigma_y\).</p>
<p>After yielding the curve rises to a maximum called the <b>ultimate tensile strength (UTS)</b>. Beyond the peak the specimen <b>necks</b> — one region becomes visibly thinner. Engineering stress falls after the peak because force is still divided by the original area, even though the true stress in the narrowing neck continues to rise. Fracture eventually occurs at a lower engineering stress than the UTS.</p>"""),
 ("Resilience, toughness and safety factors",
  r"""<p>The area under the stress–strain curve represents energy absorbed per unit volume. Two quantities are read from different portions of that area.</p>
<p><b>Resilience</b> is the elastic triangle alone: \(U_r = \sigma_y^2/(2E)\). It is the energy stored and returned on unloading — the property a spring needs.</p>
<p><b>Toughness</b> is the full area to fracture. It measures how much energy the material absorbs before breaking — the property a crash structure or impact zone needs. A high-strength alloy can have high yield yet low toughness if the curve is tall and narrow.</p>
<p>In design, working stress is compared with yield through a <b>safety factor</b> \(N = \sigma_y / \sigma_{\text{working}}\). The factor accounts for load uncertainty, material variability, environmental degradation and the consequence of failure. Yield strength is the appropriate strength for this calculation because it marks the end of elastic, recoverable behaviour.</p>"""),
],
3: [
 ("The strength of real crystals",
  r"""<p>Theoretical strength calculated from bond stiffness across a perfect crystal plane gives values far above any measured metal. Real metals are weaker because their crystals contain <b>defects</b> — departures from perfect periodic order.</p>
<p>The most important defect for mechanical behaviour is the <b>dislocation</b>: an extra half-plane of atoms inserted into the lattice. Under stress, dislocations move along slip planes, allowing layers of atoms to shift incrementally. That collective motion is <b>plastic deformation</b>. A metal bends because billions of dislocations glide, breaking only a few bonds at a time rather than an entire plane at once.</p>
<p>Materials without mobile dislocations — most ceramics and glasses — cannot deform plastically and fracture when stress concentrates at a flaw. Metals owe their combination of strength and ductility to controllable dislocation motion.</p>"""),
 ("Vacancies and atomic diffusion",
  r"""<p>A <b>vacancy</b> is a lattice site where an atom is missing. At any temperature above absolute zero some vacancies exist, and their concentration increases with temperature according to an Arrhenius relationship.</p>
<p>Atoms can jump into vacant neighbouring sites, so vacancies enable <b>diffusion</b> — the gradual migration of atoms through a solid. Diffusion underpins carburising and nitriding of steel surfaces, homogenisation of cast alloys, and high-temperature creep. Vacancies and dislocations together describe how real crystals depart from perfection and how processing changes properties.</p>"""),
 ("Grain boundaries and the Hall–Petch relation",
  r"""<p>Most engineering metals are polycrystalline: they consist of many small crystals (grains) meeting at <b>grain boundaries</b>. Across a boundary the crystal orientation changes, so a dislocation moving through one grain cannot simply continue into the next. Boundaries act as obstacles to dislocation motion.</p>
<p>Finer grains mean more boundaries per unit volume and higher yield strength. The <b>Hall–Petch</b> relation captures this: yield strength increases as grain size \(d\) decreases, scaling approximately as \(1/\sqrt{d}\). Grain refinement is therefore a standard strengthening route, used alone or combined with other methods.</p>"""),
 ("Mechanisms that strengthen metals",
  r"""<p>Because plastic flow requires dislocation motion, any process that impedes dislocations raises strength. Four mechanisms appear repeatedly in engineering alloys.</p>
<p><b>Solid-solution strengthening</b> adds solute atoms of different size into the lattice, distorting it locally and pinning dislocations. <b>Strain hardening (cold working)</b> plastically deforms the metal at room temperature, multiplying and tangling dislocations until further motion is difficult. <b>Precipitation hardening</b> forms fine second-phase particles that dislocations must bypass. <b>Grain refinement</b> adds boundary obstacles as described above.</p>
<p>Each mechanism raises yield strength and often reduces ductility — the stress–strain curve becomes taller and narrower. The choice of strengthening route depends on the service conditions the part must survive.</p>"""),
],
4: [
 ("Fracture mechanics and stress intensity",
  r"""<p>Many engineering failures occur while the nominal stress remains below yield. A pre-existing crack concentrates stress at its tip, and the local stress field is described by the <b>stress intensity factor</b> \(K\). For a through-thickness crack in an infinite plate under uniform tension, \(K = \sigma\sqrt{\pi a}\), where \(\sigma\) is the remote stress and \(a\) is half the crack length.</p>
<p>Each material has a critical value \(K_{Ic}\), the <b>plane-strain fracture toughness</b>. When \(K\) reaches \(K_{Ic}\), rapid unstable fracture follows. Rearranging gives an estimate of failure stress: \(\sigma_f \approx K_{Ic}/\sqrt{\pi a}\). A small crack can therefore cause fracture at a stress the uncracked material would easily sustain.</p>
<p>Fracture toughness is a material property measured under standard test conditions. Flaw size and geometry are properties of the part. Safe design requires both the applied \(K\) and the material's \(K_{Ic}\) to be known.</p>"""),
 ("Fatigue and the S–N curve",
  r"""<p><b>Fatigue</b> is failure under repeated loading. A stress applied once may be harmless; the same stress applied millions of times can initiate and grow a crack until final fracture. Fatigue is governed by the stress <em>range</em> and the number of cycles, not simply by whether yield is exceeded.</p>
<p>The <b>S–N curve</b> plots stress amplitude against cycles to failure. For many steels a horizontal <b>endurance limit</b> appears: below that stress, life is effectively unlimited. Aluminium and many non-ferrous alloys show no clear endurance limit; life continues to fall as stress decreases.</p>
<p>Fatigue cracks usually initiate at the surface — at machining marks, corrosion pits or geometric stress concentrations. Surface finish, compressive residual stress from shot peening, and generous fillet radii all extend fatigue life. High-strength alloys are particularly sensitive because small surface defects become critical at the stress intensities they allow.</p>"""),
 ("Strengthening and its effect on fracture resistance",
  r"""<p>The strengthening mechanisms introduced earlier — cold work, solid solution, precipitation hardening, grain refinement — all raise yield by restricting dislocation motion. They also tend to lower ductility and, in many cases, fracture toughness.</p>
<p>A high-strength martensitic steel may carry a much higher yield than a softer pearlitic grade yet be more susceptible to brittle fracture from a weld defect. Strengthening is therefore matched to the dominant failure mode: a component threatened by fatigue needs surface quality and endurance data; one threatened by fast fracture needs toughness; one threatened by overload needs yield margin.</p>"""),
],
5: [
 ("Creep at elevated temperature",
  r"""<p>When a metal is held under constant stress at high temperature — high relative to its melting point — it continues to deform slowly with time. This time-dependent extension is <b>creep</b>.</p>
<p>A creep curve plots strain against time at fixed stress and temperature. Three stages appear. In <b>primary creep</b> the strain rate decreases as the material strain-hardens. In <b>secondary creep</b> a steady strain rate is reached; this stage is used for design extrapolation. In <b>tertiary creep</b> the strain rate accelerates as necking or internal damage develops, leading to rupture.</p>
<p>Creep becomes significant when homologous temperature \(T/T_m\) exceeds about 0.4 for metals. Polymers can creep appreciably at room temperature because their glass transition lies near ambient conditions. Design against creep specifies a maximum allowable strain or rupture life at the service temperature and stress.</p>"""),
 ("Thermal expansion and thermal stress",
  r"""<p>Heating a solid produces thermal strain \(\Delta L / L_0 = \alpha \Delta T\), where \(\alpha\) is the coefficient of linear thermal expansion. If the solid is free to expand, no stress develops. If expansion is prevented — because the part is clamped, bolted or bonded to a stiffer member — elastic stress builds up.</p>
<p>For full restraint the approximate relation is \(\sigma \approx E\alpha\Delta T\). A temperature rise of 100 °C in a fully restrained steel bar can generate stress approaching yield. <b>Thermal mismatch</b> between joined materials produces similar effects: a steel bolt in an aluminium housing, or a ceramic coating on a metal substrate, develops stress on heating or cooling even when each material alone would be stress-free.</p>"""),
 ("Thermal shock and the concept of a phase",
  r"""<p><b>Thermal shock</b> occurs when rapid temperature change creates large internal temperature gradients. Low thermal conductivity allows steep gradients; restraint generates thermal stress; and materials that cannot yield to relieve that stress — ceramics and glasses — are especially vulnerable. Thermal shock resistance improves with higher conductivity, higher toughness and lower expansion coefficient.</p>
<p>This week also introduces the idea of a <b>phase</b>: a region of material with uniform structure and composition. <b>Microstructure</b> describes how phases are distributed — their size, shape and arrangement. Two samples with identical phases can have very different properties if the microstructure differs. Phase diagrams, developed in the next week, map which phases are stable at each composition and temperature.</p>"""),
],
6: [
 ("Reading a binary phase diagram",
  r"""<p>A binary phase diagram is a map with composition on the horizontal axis and temperature on the vertical axis. Each region is labelled with the phase or combination of phases stable at that composition and temperature. Boundaries mark where phase transformations occur — melting begins or completes, solid solutions dissolve or precipitate, eutectic reactions take place.</p>
<p>To use the diagram, plot the alloy composition and temperature as a point and read the phase label for that region. A single-phase region means the entire microstructure is one solid solution or one liquid. A two-phase region means two phases coexist, each with its own composition at that temperature.</p>
<p>The overall composition \(C_0\) of the alloy is fixed by what was melted together. It does not change on cooling; only the distribution of atoms between phases changes.</p>"""),
 ("Tie-lines and the lever rule",
  r"""<p>In a two-phase field a horizontal <b>tie-line</b> connects the compositions of the coexisting phases at that temperature. The left endpoint gives \(C_\alpha\); the right endpoint gives \(C_\beta\).</p>
<p>The <b>lever rule</b> converts these compositions into mass fractions. The fraction of phase \(\alpha\) is the length of the opposite arm divided by the full tie-line length:</p>
<p class="fml">\[W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha}\]</p>
<p>The fraction of \(\beta\) uses the other arm as numerator. The two fractions sum to unity. A useful check: the phase whose composition lies closer to \(C_0\) must be the dominant phase.</p>"""),
 ("Cooling paths and microstructure",
  r"""<p>Following a vertical line on the diagram — fixed composition, falling temperature — traces the solidification history. Each time the path crosses a boundary, a new phase forms or an existing phase changes composition.</p>
<p>For a hypoeutectic alloy, primary \(\alpha\) solidifies first in the two-phase liquid-plus-solid region; the remaining liquid enriches until it reaches the eutectic composition and transforms at the eutectic temperature into a fine \(\alpha + \beta\) mixture. The final microstructure is primary \(\alpha\) grains embedded in eutectic.</p>
<p>The <b>eutectic point</b> is the lowest-melting composition in the system. At that composition the liquid freezes entirely at one temperature into two solid phases. Eutectic alloys are widely used as solders because of their sharp melting behaviour.</p>
<p>Predicting microstructure from a cooling path connects phase diagram reading to mechanical properties: the amount, distribution and composition of each phase determine strength, ductility and corrosion resistance.</p>"""),
],
7: [
 ("Polymer structure and molecular architecture",
  r"""<p>Polymers are macromolecules built from repeating <b>mer</b> units joined into long chains. Chain length is described by the <b>degree of polymerisation</b> — the number of repeat units — or by molecular weight. Longer chains entangle more strongly, generally increasing toughness and melt viscosity.</p>
<p><b>Linear</b> chains can slide past one another when heated and are thermoplastic — they melt and can be reprocessed. <b>Branched</b> chains pack less efficiently and often have lower density and stiffness. <b>Cross-linked</b> chains are tied together into a three-dimensional network; the material cannot melt and is called a thermoset. Vulcanised rubber is cross-linked; polyethylene milk bottles are linear.</p>
<p>Many polymers are partly <b>crystalline</b> (ordered chain segments) and partly <b>amorphous</b> (disordered). Higher crystallinity generally increases stiffness, density and chemical resistance while reducing transparency.</p>"""),
 ("The glass transition and melting",
  r"""<p>Amorphous regions in a polymer respond to temperature through the <b>glass transition temperature</b> \(T_g\). Below \(T_g\) segmental chain motion is frozen and the material is glassy and relatively brittle. Above \(T_g\) chains gain mobility and the material becomes rubbery and tough. The polymer remains solid on both sides of \(T_g\); only its mechanical response changes.</p>
<p>Crystalline regions melt at the <b>melting temperature</b> \(T_m\), which lies above \(T_g\) when both are present. Service temperature must be chosen relative to these transitions: a rubber ball operates above its \(T_g\); a PVC drain pipe operates below it.</p>"""),
 ("Viscoelastic behaviour",
  r"""<p>Polymers exhibit <b>viscoelasticity</b>: their response depends on time as well as stress and temperature. Under constant load a polymer continues to deform — <b>creep</b>. Under constant deformation the reaction force gradually decreases — <b>stress relaxation</b>. Both effects are significant at room temperature for many polymers.</p>
<p>Design with polymers therefore specifies load duration and operating temperature alongside stress level. A snap-fit that works at assembly may relax over months; a seal may lose contact pressure while the deformation remains fixed.</p>"""),
],
8: [
 ("The materials selection process",
  r"""<p>Engineering design specifies what a component must do before naming a material. The selection process moves from function to measurable requirements, then to candidate materials, then to a justified choice.</p>
<p>First state the <b>function</b> and all <b>constraints</b> — maximum mass, maximum cost, operating temperature, environment, manufacturing route. Next identify <b>failure modes</b>: yielding, fracture, fatigue, creep, corrosion, excessive deflection, wear. Each failure mode maps to a <b>property target</b> with a numerical value or limit.</p>
<p>Materials that fail any constraint are eliminated. Those that pass all constraints form a shortlist, ranked on an <b>objective</b> — usually minimising mass or cost. The final answer names the chosen material, states which alternatives were considered, identifies the constraint each rejected candidate failed, acknowledges the trade-off accepted, and offers a backup if the main risk materialises.</p>"""),
 ("Performance indices and property charts",
  r"""<p>Many design problems reduce to maximising a ratio of properties. A tie rod limited by stiffness and weight is optimised on <b>specific stiffness</b> \(E/\rho\). A beam in bending benefits from \(E^{1/2}/\rho\) or \(E^{1/3}/\rho\) depending on whether the section can be redesigned. A strength-limited tie uses \(\sigma_y/\rho\).</p>
<p><b>Ashby charts</b> plot properties on logarithmic axes so entire material families appear as clusters. A light, stiff panel seeks the upper-left region of an \(E\) versus \(\rho\) chart. Steel and aluminium have similar specific stiffness even though steel's absolute modulus is three times higher, because steel is also three times denser.</p>
<p>Charts screen families efficiently; calculations on shortlisted candidates then confirm that all constraints are met. A chart shows what is possible in principle; manufacturing, joining, environment and cost determine what is possible in practice.</p>"""),
 ("Lifecycle cost and environmental screening",
  r"""<p>Purchase price is often a small fraction of lifecycle cost. A coated carbon steel component may cost little to buy but require repeated recoating in a corrosive environment, with each maintenance event carrying labour and downtime costs. Stainless steel with a higher initial price may be cheaper over twenty years if maintenance is eliminated.</p>
<p>Environmental screening asks whether a candidate survives the service medium — marine salt, acids, UV exposure, elevated temperature. Galvanic compatibility between joined materials matters: dissimilar metals in electrical contact in an electrolyte can accelerate corrosion of the more anodic member.</p>
<p>Selection is complete only when function, properties, process, cost and environment have all been addressed in the justification.</p>"""),
],
9: [
 ("Electrical conduction in solids",
  r"""<p>Electrical conductivity \(\sigma\) measures how easily charge moves through a material. In metals, conduction is dominated by free electrons left over from metallic bonding. The relation \(\sigma = nq\mu\) connects conductivity to carrier concentration \(n\), charge \(q\) and mobility \(\mu\).</p>
<p><b>Resistivity</b> \(\rho = 1/\sigma\) is a material property with units \(\Omega\cdot\)m. <b>Resistance</b> \(R = \rho L/A\) belongs to a particular object and depends on its length \(L\) and cross-sectional area \(A\). Doubling the length doubles the resistance; doubling the area halves it.</p>
<p>Impurities, crystal defects and thermal vibrations scatter electrons and raise resistivity. In pure metals, resistivity increases with temperature because lattice vibrations intensify. Alloying also lowers conductivity because solute atoms disrupt the regular lattice — the same disruption that strengthens the alloy impedes electron flow.</p>"""),
 ("Metals, semiconductors and insulators",
  r"""<p>The band structure of a solid determines its electrical behaviour. In a <b>metal</b>, conduction and valence bands overlap or the conduction band is partially filled, so electrons move freely under an applied field.</p>
<p>In an <b>insulator</b>, a large <b>band gap</b> separates filled valence states from empty conduction states at ordinary temperatures, so conduction is negligible.</p>
<p>A <b>semiconductor</b> has a small band gap. At low temperature it behaves as an insulator; as temperature rises, thermal energy promotes electrons across the gap, increasing conductivity. Semiconductor conductivity therefore rises with temperature — the opposite trend to metals. Doping introduces controlled impurity levels that set whether electrons or holes dominate conduction.</p>"""),
 ("The Hall effect",
  r"""<p>When a current-carrying conductor sits in a magnetic field perpendicular to the current, charge carriers are deflected sideways. A transverse <b>Hall voltage</b> builds up until it balances the magnetic force. The sign of the Hall voltage reveals whether the dominant carriers are electrons or holes; its magnitude, together with the magnetic field and current, gives carrier concentration.</p>
<p>The Hall effect is a standard characterisation tool for semiconductors and a basis for magnetic field sensors in engineering instrumentation.</p>"""),
],
10: [
 ("Magnetic behaviour of materials",
  r"""<p>Atoms carry magnetic moments from electron spin and orbital motion. In most materials these moments cancel or align only weakly. Three classes matter in engineering.</p>
<p><b>Diamagnetic</b> materials weakly oppose an applied field. <b>Paramagnetic</b> materials weakly align with it. <b>Ferromagnetic</b> materials — iron, nickel, cobalt and their alloys — show strong spontaneous alignment below the <b>Curie temperature</b>, above which thermal energy destroys the alignment and ferromagnetism disappears.</p>
<p>Ferrites and other ceramic magnets are ferrimagnetic: unequal opposing sublattice moments produce a net magnetisation with low electrical conductivity, which suppresses eddy-current losses in alternating fields.</p>"""),
 ("The hysteresis loop",
  r"""<p>Cycling a ferromagnetic material through magnetisation and demagnetisation traces a <b>B–H loop</b>, plotting magnetic flux density \(B\) against applied field \(H\).</p>
<p><b>Saturation</b> is where \(B\) reaches its maximum for the material. <b>Remanence</b> \(B_r\) is the flux density remaining when \(H\) returns to zero — the strength of a permanent magnet. <b>Coercivity</b> \(H_c\) is the reverse field needed to drive \(B\) to zero — a measure of resistance to demagnetisation.</p>
<p>The area enclosed by the loop equals energy dissipated as heat per magnetising cycle. At mains frequency this hysteresis loss can dominate heating in transformer cores and motors.</p>"""),
 ("Soft and hard magnetic materials",
  r"""<p><b>Soft magnetic</b> materials have narrow loops, low coercivity and low remanence. They magnetise and demagnetise easily, minimising energy loss per cycle. Silicon steel laminations in transformers and motor cores are the principal application.</p>
<p><b>Hard magnetic</b> materials have wide loops, high coercivity and high remanence. They retain magnetisation after the external field is removed. Alnico, ferrite and rare-earth magnets serve in loudspeakers, sensors and electric motors.</p>
<p>Choosing a magnetic material begins with whether the application requires frequent field reversal (soft) or permanent magnetisation (hard). Eddy-current losses in alternating fields are reduced by laminating the core or using high-resistivity ferrite.</p>"""),
],
11: [
 ("The structure of fibre composites",
  r"""<p>A composite combines two or more materials to achieve properties neither delivers alone. In a <b>fibre-reinforced composite</b>, high-strength fibres carry tensile load while a <b>matrix</b> — polymer, metal or ceramic — binds the fibres, transfers load into them through shear at the interface, and protects the surface.</p>
<p>Properties depend strongly on fibre orientation. A unidirectional laminate loaded along the fibres behaves very differently from the same laminate loaded across them or in shear. Design always begins by identifying the principal load direction.</p>"""),
 ("The rule of mixtures",
  r"""<p>For loading parallel to continuous aligned fibres, stiffness follows the <b>rule of mixtures</b>:</p>
<p class="fml">\[E_c \approx V_f E_f + V_m E_m\]</p>
<p>where \(V_f\) and \(V_m\) are volume fractions of fibre and matrix and \(E_f\) and \(E_m\) are their elastic moduli. Strength in the fibre direction follows similar volume-fraction weighting when fibres are well bonded and aligned.</p>
<p>Transverse stiffness is matrix-dominated: the reciprocal relation \(1/E_c \approx V_f/E_f + V_m/E_m\) shows that the softer phase controls the response, and transverse modulus can be an order of magnitude below the longitudinal value.</p>"""),
 ("Critical fibre length and design trade-offs",
  r"""<p>Load enters a fibre through interfacial shear stress over a distance from each end. If the fibre is shorter than the <b>critical length</b> \(l_c = \sigma_f d / (2\tau_i)\), it pulls out of the matrix before reaching its tensile strength. Chopped-fibre mouldings therefore cannot exploit the full fibre strength unless fibres are long enough or the interface is strong enough.</p>
<p>Composites offer exceptional stiffness and strength per unit mass along the fibre direction. They also introduce anisotropy, sensitivity to impact and delamination, difficulty in joining, and higher processing cost. Selection weighs the performance gain in the load direction against these practical constraints.</p>"""),
],
12: [
 ("Mechanical behaviour of ceramics and glasses",
  r"""<p>Ceramics and glasses are strong in compression but weak in tension. Their ionic and covalent bonds resist compression well, but a tensile stress opens microcracks and allows rapid propagation. Without mobile dislocations to blunt a crack tip, fracture occurs at stresses far below the theoretical strength of a flawless crystal.</p>
<p>Measured tensile strength therefore depends on the size of the largest flaw present — surface scratches, pores, or inclusions — rather than on bulk chemistry alone. Handling, machining and environmental exposure all influence the flaw population and hence the strength of a given part.</p>"""),
 ("Griffith's approach to brittle fracture",
  r"""<p>Griffith showed that the condition for a crack to propagate is that the release of elastic strain energy exceeds the energy required to create new fracture surfaces. This leads to the practical estimate:</p>
<p class="fml">\[\sigma_f \approx \frac{K_{Ic}}{Y\sqrt{\pi a}}\]</p>
<p>where \(K_{Ic}\) is fracture toughness, \(a\) is flaw size and \(Y\) is a geometry factor. Larger flaws lower the failure stress. Surface finish and proof testing — loading to a level that eliminates weak specimens — are standard strategies for ceramic components.</p>
<p>Design keeps ceramics in compression where possible, avoids sharp corners that concentrate stress, and accounts for scatter in strength by designing to a low percentile of the measured distribution.</p>"""),
 ("Thermal shock in brittle materials",
  r"""<p>Rapid heating or cooling sets up temperature gradients within a component. Low thermal conductivity allows steep gradients; thermal expansion mismatch and restraint generate stress; and the inability to deform plastically means that stress cannot be relieved by yielding. When the thermal stress exceeds the material's strength, <b>thermal shock</b> fracture results.</p>
<p>Thermal shock resistance improves with higher thermal conductivity (flatter gradients), lower thermal expansion coefficient (smaller strain for a given \(\Delta T\)), and higher fracture toughness. Sudden quenching of a hot ceramic vessel illustrates the failure mode: the cold surface contracts while the interior remains hot, placing the surface in tension.</p>"""),
],
13: [
 ("Recognising the topic from the question",
  r"""<p>Problems in materials science span mechanical behaviour, phase equilibria, polymers, electrical and magnetic properties, composites, ceramics and design selection. Each topic has characteristic language and governing relationships.</p>
<p>A question mentioning stress, strain, yield or a tensile curve belongs to mechanical properties. References to composition, temperature and phase fractions point to phase diagrams. Cyclic loading and life in cycles indicate fatigue. A crack and fracture toughness direct attention to linear elastic fracture mechanics. Polymer behaviour below or above a transition temperature involves \(T_g\). Volume fractions of fibre and matrix signal composites. A brief asking for material choice with constraints is a selection problem.</p>
<p>Identifying the topic first determines which equations, diagrams and property data are relevant.</p>"""),
 ("Building a complete solution",
  r"""<p>A structured solution proceeds in layers. State what is given and what is required. Draw or sketch the relevant diagram — a stress–strain curve, a phase diagram, a crack geometry. Write the governing relationship before substituting numbers. Carry units on every line of calculation. Compare the result with handbook values or physical expectations as a magnitude check.</p>
<p>Calculation problems in this subject usually end with a sentence of engineering interpretation: what the number means for the design, which material is favoured, or which failure mode governs.</p>
<p>Selection problems state property targets with numbers before naming materials, then justify each rejection with the specific constraint failed.</p>"""),
 ("The connected structure of the subject",
  r"""<p>The topics of this course form a single chain. Bonding type from Week 1 explains electrical conduction in Week 9 and magnetic behaviour in Week 10. Crystal structure and dislocations from Weeks 1 and 3 explain strengthening and fracture in Weeks 3 and 4. Phase diagrams from Week 6 explain heat-treated microstructures encountered in selection problems. Thermal expansion from Week 5 links to thermal shock in Week 12. Polymer transitions from Week 7 and composite rules from Week 11 appear alongside metals and ceramics in integrated design questions.</p>
<p>Revision that traces these connections — structure to properties to processing to performance — is more durable than memorising isolated formula lists.</p>"""),
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
<p class="intro">This section develops the week's ideas in order — from first principles through to how they are used in engineering practice.</p>
{body}
</section>
'''
