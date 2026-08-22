(function () {
  "use strict";

  var G = 9.8;

  function variantIndex(variant) {
    var value = String(variant == null ? "A" : variant).toUpperCase();
    return value === "B" ? 1 : value === "C" ? 2 : 0;
  }

  function hash(seed, variant, salt) {
    var text = String(seed) + "|" + String(variant || "A").toUpperCase() + "|" + salt;
    var h = 2166136261;
    for (var i = 0; i < text.length; i += 1) {
      h ^= text.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    return h >>> 0;
  }

  function choose(seed, variant, salt, values) {
    return values[hash(seed, variant, salt) % values.length];
  }

  function context(variant, choices) {
    return choices[variantIndex(variant)];
  }

  function n(value, digits) {
    var places = digits == null ? 2 : digits;
    return Number(value.toFixed(places)).toString();
  }

  function answer(tag, prompt, diagramType, labels, steps, final, check) {
    return {
      tag: tag,
      prompt: prompt,
      diagram: { type: diagramType, labels: labels },
      steps: steps,
      final: final,
      check: check
    };
  }

  function staticIncline(seed, variant) {
    var theta = choose(seed, variant, "theta", [15, 20, 25, 30, 35]);
    var mass = choose(seed, variant, "mass", [12, 16, 20, 24, 30]);
    var thetaRad = theta * Math.PI / 180;
    var weight = mass * G;
    var normal = weight * Math.cos(thetaRad);
    var friction = weight * Math.sin(thetaRad);
    var mu = friction / normal;
    var item = context(variant, ["equipment crate", "tool cabinet", "generator casing"]);
    return answer(
      "static-incline",
      "A " + mass + " kg " + item + " rests on a " + theta + "° incline. Find the minimum coefficient of static friction required to prevent it sliding.",
      "incline",
      ["incline " + theta + "°", "W = " + mass + "g downward", "N normal to plane", "f_s up the plane"],
      [
        "\\(W=mg=" + mass + "(9.8)=" + n(weight, 1) + "\\ \\mathrm{N}\\).",
        "\\(\\sum F_{\\perp}=0:\\quad N-W\\cos " + theta + "^\\circ=0\\), so \\(N=" + n(normal) + "\\ \\mathrm{N}\\).",
        "\\(\\sum F_{\\parallel}=0:\\quad f_s-W\\sin " + theta + "^\\circ=0\\), so \\(f_s=" + n(friction) + "\\ \\mathrm{N}\\).",
        "At impending slip, \\(f_s=\\mu_sN\\), hence \\(\\mu_{s,\\min}=\\dfrac{" + n(friction) + "}{" + n(normal) + "}=" + n(mu, 3) + "\\)."
      ],
      "\\(\\boxed{\\mu_{s,\\min}=" + n(mu, 3) + "}\\)",
      "The coefficient is dimensionless and equals \\(\\tan " + theta + "^\\circ\\); increasing the slope would require more friction."
    );
  }

  function kineticIncline(seed, variant) {
    var theta = choose(seed, variant, "theta", [20, 25, 30, 35, 40]);
    var mass = choose(seed, variant, "mass", [8, 12, 18, 22, 28]);
    var mu = choose(seed, variant, "mu", [0.12, 0.16, 0.2, 0.24]);
    var thetaRad = theta * Math.PI / 180;
    var weight = mass * G;
    var normal = weight * Math.cos(thetaRad);
    var friction = mu * normal;
    var drive = weight * Math.sin(thetaRad);
    var acceleration = (drive - friction) / mass;
    var item = context(variant, ["parcel", "machine part", "timber block"]);
    return answer(
      "kinetic-incline",
      "A " + mass + " kg " + item + " slides down a " + theta + "° incline with \\(\\mu_k=" + n(mu) + "\\). Find its acceleration.",
      "incline",
      ["incline " + theta + "°", "W downward", "N normal", "f_k up slope", "a down slope"],
      [
        "\\(W=mg=" + mass + "(9.8)=" + n(weight, 1) + "\\ \\mathrm{N}\\).",
        "\\(N=mg\\cos " + theta + "^\\circ=" + n(normal) + "\\ \\mathrm{N}\\).",
        "\\(f_k=\\mu_kN=" + n(mu) + "(" + n(normal) + ")=" + n(friction) + "\\ \\mathrm{N}\\).",
        "\\(\\sum F_{\\parallel}=mg\\sin\\theta-f_k=" + n(drive) + "-" + n(friction) + "=" + n(drive - friction) + "\\ \\mathrm{N}\\).",
        "\\(a=\\dfrac{\\sum F_{\\parallel}}{m}=\\dfrac{" + n(drive - friction) + "}{" + mass + "}=" + n(acceleration) + "\\ \\mathrm{m\\,s^{-2}}\\) down the incline."
      ],
      "\\(\\boxed{a=" + n(acceleration) + "\\ \\mathrm{m\\,s^{-2}}\\text{ down the incline}}\\)",
      "The result has acceleration units and is below the frictionless value \\(g\\sin " + theta + "^\\circ=" + n(G * Math.sin(thetaRad)) + "\\ \\mathrm{m\\,s^{-2}}\\)."
    );
  }

  function levelFriction(seed, variant) {
    var mass = choose(seed, variant, "mass", [10, 14, 20, 25, 32]);
    var mu = choose(seed, variant, "mu", [0.15, 0.2, 0.25, 0.3]);
    var force = choose(seed, variant, "force", [65, 80, 95, 120, 150]);
    var normal = mass * G;
    var friction = mu * normal;
    if (force <= friction) force = Math.ceil(friction + 25);
    var net = force - friction;
    var acceleration = net / mass;
    var item = context(variant, ["storage box", "workbench", "loaded trolley"]);
    return answer(
      "level-friction",
      "A horizontal force of " + force + " N pushes a " + mass + " kg " + item + " across a level floor where \\(\\mu_k=" + n(mu) + "\\). Find the acceleration.",
      "fbd",
      ["W downward", "N upward", force + " N applied right", "f_k left", "a right"],
      [
        "\\(W=mg=" + mass + "(9.8)=" + n(normal, 1) + "\\ \\mathrm{N}\\).",
        "\\(\\sum F_y=0\\Rightarrow N=W=" + n(normal, 1) + "\\ \\mathrm{N}\\).",
        "\\(f_k=\\mu_kN=" + n(mu) + "(" + n(normal, 1) + ")=" + n(friction) + "\\ \\mathrm{N}\\).",
        "\\(\\sum F_x=F-f_k=" + force + "-" + n(friction) + "=" + n(net) + "\\ \\mathrm{N}\\).",
        "\\(a=\\dfrac{\\sum F_x}{m}=\\dfrac{" + n(net) + "}{" + mass + "}=" + n(acceleration) + "\\ \\mathrm{m\\,s^{-2}}\\)."
      ],
      "\\(\\boxed{a=" + n(acceleration) + "\\ \\mathrm{m\\,s^{-2}}\\text{ in the force direction}}\\)",
      "Newtons divided by kilograms gives \\(\\mathrm{m\\,s^{-2}}\\), and friction makes the acceleration smaller than \\(F/m\\)."
    );
  }

  function belt(seed, variant) {
    var mu = choose(seed, variant, "mu", [0.18, 0.22, 0.28, 0.32]);
    var theta = choose(seed, variant, "wrap", [Math.PI / 2, 2 * Math.PI / 3, 3 * Math.PI / 4, Math.PI]);
    var slack = choose(seed, variant, "slack", [120, 160, 200, 250, 300]);
    var ratio = Math.exp(mu * theta);
    var tight = slack * ratio;
    var use = context(variant, ["brake band", "conveyor belt", "capstan rope"]);
    return answer(
      "belt",
      "A " + use + " has coefficient of friction \\(\\mu=" + n(mu) + "\\), wrap angle \\(\\theta=" + n(theta, 3) + "\\ \\mathrm{rad}\\), and slack-side tension \\(T_s=" + slack + "\\ \\mathrm{N}\\). Find the limiting tight-side tension.",
      "fbd",
      ["circular drum", "wrap θ = " + n(theta, 3) + " rad", "T_s = " + slack + " N", "T_t > T_s"],
      [
        "For impending belt slip, the capstan relation is \\(\\dfrac{T_t}{T_s}=e^{\\mu\\theta}\\), with \\(\\theta\\) in radians.",
        "\\(\\mu\\theta=" + n(mu) + "(" + n(theta, 3) + ")=" + n(mu * theta, 4) + "\\).",
        "\\(\\dfrac{T_t}{T_s}=e^{" + n(mu * theta, 4) + "}=" + n(ratio, 4) + "\\).",
        "\\(T_t=" + slack + "(" + n(ratio, 4) + ")=" + n(tight) + "\\ \\mathrm{N}\\)."
      ],
      "\\(\\boxed{T_t=" + n(tight) + "\\ \\mathrm{N}}\\)",
      "The exponential ratio is dimensionless, the wrap angle was used in radians, and \\(T_t>T_s\\) as required."
    );
  }

  function centroid(seed, variant) {
    var B = choose(seed, variant, "B", [100, 120, 140, 160]);
    var H = choose(seed, variant, "H", [120, 150, 180, 200]);
    var t = choose(seed, variant, "t", [20, 25, 30]);
    if (t >= Math.min(B, H) / 2) t = 20;
    var a1 = B * t;
    var x1 = B / 2;
    var y1 = t / 2;
    var a2 = t * (H - t);
    var x2 = t / 2;
    var y2 = t + (H - t) / 2;
    var area = a1 + a2;
    var xbar = (a1 * x1 + a2 * x2) / area;
    var ybar = (a1 * y1 + a2 * y2) / area;
    var material = context(variant, ["steel angle plate", "aluminium L-section", "timber L-lamina"]);
    return answer(
      "centroid",
      "A uniform " + material + " consists of a bottom rectangle \\(" + B + "\\times" + t + "\\ \\mathrm{mm}\\) and a left rectangle \\(" + t + "\\times" + (H - t) + "\\ \\mathrm{mm}\\) directly above it. Find \\((\\bar x,\\bar y)\\) from the lower-left corner.",
      "area-cross-section",
      ["x origin at lower-left", "y origin at lower-left", "A₁ bottom " + B + "×" + t, "A₂ upper-left " + t + "×" + (H - t), "overall height " + H + " mm"],
      [
        "\\(A_1=" + B + "(" + t + ")=" + a1 + "\\ \\mathrm{mm^2}\\), with \\((x_1,y_1)=(" + n(x1) + "," + n(y1) + ")\\ \\mathrm{mm}\\).",
        "\\(A_2=" + t + "(" + (H - t) + ")=" + a2 + "\\ \\mathrm{mm^2}\\), with \\((x_2,y_2)=(" + n(x2) + "," + n(y2) + ")\\ \\mathrm{mm}\\).",
        "\\(A= A_1+A_2=" + area + "\\ \\mathrm{mm^2}\\).",
        "\\(\\bar x=\\dfrac{\\sum A_ix_i}{\\sum A_i}=\\dfrac{" + a1 + "(" + n(x1) + ")+" + a2 + "(" + n(x2) + ")}{" + area + "}=" + n(xbar) + "\\ \\mathrm{mm}\\).",
        "\\(\\bar y=\\dfrac{\\sum A_iy_i}{\\sum A_i}=\\dfrac{" + a1 + "(" + n(y1) + ")+" + a2 + "(" + n(y2) + ")}{" + area + "}=" + n(ybar) + "\\ \\mathrm{mm}\\)."
      ],
      "\\(\\boxed{(\\bar x,\\bar y)=(" + n(xbar) + "," + n(ybar) + ")\\ \\mathrm{mm}}\\)",
      "Both coordinates lie inside the section bounds, and the centroid is pulled toward the bottom and left legs."
    );
  }

  function centroidHole(seed, variant) {
    var B = choose(seed, variant, "B", [180, 200, 240, 300]);
    var H = choose(seed, variant, "H", [140, 160, 180, 220]);
    var d = choose(seed, variant, "d", [30, 40, 50, 60]);
    var xh = choose(seed, variant, "xh", [0.3, 0.4, 0.65, 0.72]) * B;
    var yh = choose(seed, variant, "yh", [0.3, 0.42, 0.62, 0.7]) * H;
    var plateArea = B * H;
    var holeArea = -Math.PI * d * d / 4;
    var totalArea = plateArea + holeArea;
    var xbar = (plateArea * B / 2 + holeArea * xh) / totalArea;
    var ybar = (plateArea * H / 2 + holeArea * yh) / totalArea;
    var item = context(variant, ["mounting plate", "machine guard", "gusset blank"]);
    return answer(
      "centroid-hole",
      "A " + B + " mm by " + H + " mm rectangular " + item + " has a circular hole of diameter " + d + " mm centred at \\((" + n(xh) + "," + n(yh) + ")\\ \\mathrm{mm}\\) from its lower-left corner. Find the remaining area's centroid.",
      "area-cross-section",
      ["rectangle " + B + "×" + H + " mm", "origin lower-left", "hole Ø" + d + " mm", "hole centre (" + n(xh) + ", " + n(yh) + ") mm", "hole area negative"],
      [
        "\\(A_1=" + B + "(" + H + ")=" + plateArea + "\\ \\mathrm{mm^2}\\), at \\((x_1,y_1)=(" + n(B / 2) + "," + n(H / 2) + ")\\ \\mathrm{mm}\\).",
        "Treat the hole as negative: \\(A_2=-\\dfrac{\\pi(" + d + ")^2}{4}=" + n(holeArea) + "\\ \\mathrm{mm^2}\\), at \\((x_2,y_2)=(" + n(xh) + "," + n(yh) + ")\\ \\mathrm{mm}\\).",
        "\\(A=A_1+A_2=" + n(totalArea) + "\\ \\mathrm{mm^2}\\).",
        "\\(\\bar x=\\dfrac{A_1x_1+A_2x_2}{A}=" + n(xbar) + "\\ \\mathrm{mm}\\).",
        "\\(\\bar y=\\dfrac{A_1y_1+A_2y_2}{A}=" + n(ybar) + "\\ \\mathrm{mm}\\)."
      ],
      "\\(\\boxed{(\\bar x,\\bar y)=(" + n(xbar) + "," + n(ybar) + ")\\ \\mathrm{mm}}\\)",
      "The hole was assigned negative area; the centroid shifts away from the removed material and remains within the plate."
    );
  }

  function rectangleI(seed, variant) {
    var b = choose(seed, variant, "b", [40, 60, 80, 100, 120]);
    var h = choose(seed, variant, "h", [80, 100, 140, 160, 200]);
    var ix = b * Math.pow(h, 3) / 12;
    var section = context(variant, ["rectangular bar", "timber beam", "plate strip"]);
    return answer(
      "rectangle-I",
      "A " + section + " cross-section is " + b + " mm wide and " + h + " mm high. Find its second moment of area about the horizontal centroidal axis.",
      "area-cross-section",
      ["rectangle b = " + b + " mm", "h = " + h + " mm", "centroid at mid-height", "x-axis horizontal through centroid"],
      [
        "For a rectangle about its horizontal centroidal axis, \\(I_x=\\dfrac{bh^3}{12}\\).",
        "\\(h^3=(" + h + "\\ \\mathrm{mm})^3=" + Math.pow(h, 3) + "\\ \\mathrm{mm^3}\\).",
        "\\(bh^3=" + b + "(" + Math.pow(h, 3) + ")=" + b * Math.pow(h, 3) + "\\ \\mathrm{mm^4}\\).",
        "\\(I_x=\\dfrac{" + b * Math.pow(h, 3) + "}{12}=" + n(ix) + "\\ \\mathrm{mm^4}\\)."
      ],
      "\\(\\boxed{I_x=" + n(ix) + "\\ \\mathrm{mm^4}}\\)",
      "Second moment of area has units of length to the fourth power; the height is cubed because it is perpendicular to the x-axis."
    );
  }

  function compositeI(seed, variant) {
    var B = choose(seed, variant, "B", [100, 120, 150, 180]);
    var H = choose(seed, variant, "H", [160, 200, 240, 300]);
    var tf = choose(seed, variant, "tf", [15, 20, 25]);
    var tw = choose(seed, variant, "tw", [10, 12, 16, 20]);
    var hw = H - 2 * tf;
    var af = B * tf;
    var d = H / 2 - tf / 2;
    var ifCentroid = B * Math.pow(tf, 3) / 12;
    var flangeContribution = ifCentroid + af * d * d;
    var webI = tw * Math.pow(hw, 3) / 12;
    var totalI = 2 * flangeContribution + webI;
    var member = context(variant, ["rolled-style I-section", "built-up beam section", "symmetric girder section"]);
    return answer(
      "composite-I",
      "A symmetric " + member + " has overall depth " + H + " mm, two " + B + " mm by " + tf + " mm flanges, and a " + tw + " mm thick web between the flanges. Find \\(I_x\\) about its horizontal centroidal axis.",
      "area-cross-section",
      ["top flange " + B + "×" + tf, "web " + tw + "×" + hw, "bottom flange " + B + "×" + tf, "centroidal x-axis at H/2", "d = " + n(d) + " mm"],
      [
        "By symmetry, the centroidal x-axis is at mid-depth: \\(\\bar y=H/2=" + n(H / 2) + "\\ \\mathrm{mm}\\).",
        "For each flange, \\(A_f=" + B + "(" + tf + ")=" + af + "\\ \\mathrm{mm^2}\\) and \\(d=" + n(d) + "\\ \\mathrm{mm}\\).",
        "Using the parallel-axis theorem, \\(I_{f,x}=\\dfrac{" + B + "(" + tf + ")^3}{12}+A_fd^2=" + n(flangeContribution) + "\\ \\mathrm{mm^4}\\) per flange.",
        "For the centred web, \\(I_{w,x}=\\dfrac{" + tw + "(" + hw + ")^3}{12}=" + n(webI) + "\\ \\mathrm{mm^4}\\).",
        "\\(I_x=2I_{f,x}+I_{w,x}=2(" + n(flangeContribution) + ")+" + n(webI) + "=" + n(totalI) + "\\ \\mathrm{mm^4}\\)."
      ],
      "\\(\\boxed{I_x=" + n(totalI) + "\\ \\mathrm{mm^4}}\\)",
      "All component areas are positive and non-overlapping; units are \\(\\mathrm{mm^4}\\), and the distant flanges make a large contribution through \\(Ad^2\\)."
    );
  }

  function workForce(seed, variant) {
    var mass = choose(seed, variant, "mass", [8, 10, 12, 16, 20]);
    var distance = choose(seed, variant, "distance", [3, 4, 5, 6, 8]);
    var f1 = choose(seed, variant, "f1", [20, 30, 40, 50]);
    var f2 = choose(seed, variant, "f2", [70, 90, 110, 130]);
    var work = (f1 + f2) * distance / 2;
    var speed = Math.sqrt(2 * work / mass);
    var item = context(variant, ["test carriage", "warehouse cart", "lab sled"]);
    return answer(
      "work-force",
      "A " + mass + " kg " + item + " starts from rest on a frictionless level track. The applied horizontal force increases linearly from " + f1 + " N to " + f2 + " N over " + distance + " m. Find its final speed.",
      "energy",
      ["F–x graph", "F(0) = " + f1 + " N", "F(" + distance + ") = " + f2 + " N", "area under graph = work", "ΔK = work"],
      [
        "The force-displacement graph is a trapezoid, so \\(W=\\dfrac{F_1+F_2}{2}s\\).",
        "\\(W=\\dfrac{" + f1 + "+" + f2 + "}{2}(" + distance + ")=" + n(work) + "\\ \\mathrm{J}\\).",
        "The work-energy equation is \\(W=\\Delta K=\\tfrac12mv^2-0\\).",
        "\\(v=\\sqrt{\\dfrac{2W}{m}}=\\sqrt{\\dfrac{2(" + n(work) + ")}{" + mass + "}}=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}\\)."
      ],
      "\\(\\boxed{v=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}}\\)",
      "The area under an \\(F\\)-versus-\\(x\\) graph has units \\(\\mathrm{N\\,m=J}\\); positive work increases kinetic energy."
    );
  }

  function fall(seed, variant) {
    var mass = choose(seed, variant, "mass", [2, 4, 6, 10, 15]);
    var height = choose(seed, variant, "height", [3, 5, 8, 10, 12]);
    var potential = mass * G * height;
    var speed = Math.sqrt(2 * G * height);
    var object = context(variant, ["inspection tool", "test mass", "small package"]);
    return answer(
      "fall",
      "A " + mass + " kg " + object + " is released from rest " + height + " m above the ground. Neglect air resistance and find its speed immediately before impact.",
      "energy",
      ["initial height " + height + " m", "v₀ = 0", "U_g = mgh", "final datum at ground", "K_f = ½mv²"],
      [
        "Choose the ground as the zero gravitational-potential datum.",
        "\\(U_i=mgh=" + mass + "(9.8)(" + height + ")=" + n(potential) + "\\ \\mathrm{J}\\), and \\(K_i=0\\).",
        "With no non-conservative work, \\(K_i+U_i=K_f+U_f\\Rightarrow " + n(potential) + "=\\tfrac12(" + mass + ")v^2\\).",
        "\\(v=\\sqrt{2gh}=\\sqrt{2(9.8)(" + height + ")}=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}\\)."
      ],
      "\\(\\boxed{v=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}\\text{ downward}}\\)",
      "Mass cancels, as expected for free fall without air resistance, and \\(2gh\\) has units \\(\\mathrm{m^2\\,s^{-2}}\\)."
    );
  }

  function spring(seed, variant) {
    var mass = choose(seed, variant, "mass", [1.5, 2, 2.5, 3, 4]);
    var k = choose(seed, variant, "k", [250, 320, 400, 500, 650]);
    var compression = choose(seed, variant, "compression", [0.12, 0.15, 0.18, 0.2, 0.25]);
    var energy = 0.5 * k * compression * compression;
    var speed = Math.sqrt(k * compression * compression / mass);
    var object = context(variant, ["slider", "cart", "test block"]);
    return answer(
      "spring",
      "A " + mass + " kg " + object + " is launched on a frictionless horizontal surface by a spring of stiffness " + k + " N/m compressed " + n(compression) + " m. Find the speed when the spring reaches its natural length.",
      "energy",
      ["spring compressed x = " + n(compression) + " m", "k = " + k + " N/m", "v₀ = 0", "frictionless surface", "spring natural at final state"],
      [
        "Initially, \\(K_i=0\\) and the stored spring energy is \\(U_{s,i}=\\tfrac12kx^2\\).",
        "\\(U_{s,i}=\\tfrac12(" + k + ")(" + n(compression) + ")^2=" + n(energy) + "\\ \\mathrm{J}\\).",
        "At natural length \\(U_{s,f}=0\\); conservation of energy gives \\(" + n(energy) + "=\\tfrac12(" + mass + ")v^2\\).",
        "\\(v=\\sqrt{\\dfrac{kx^2}{m}}=\\sqrt{\\dfrac{" + k + "(" + n(compression) + ")^2}{" + mass + "}}=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}\\)."
      ],
      "\\(\\boxed{v=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}}\\)",
      "\\(kx^2\\) has units of joules, and all initial spring energy becomes kinetic energy on the frictionless surface."
    );
  }

  function frictionEnergy(seed, variant) {
    var mass = choose(seed, variant, "mass", [6, 8, 10, 12, 15]);
    var speed0 = choose(seed, variant, "speed0", [8, 10, 12, 14]);
    var mu = choose(seed, variant, "mu", [0.12, 0.16, 0.2, 0.24]);
    var maxDistance = speed0 * speed0 / (2 * mu * G);
    var distanceOptions = [2, 3, 4, 5, 6];
    var distance = choose(seed, variant, "distance", distanceOptions);
    if (distance >= maxDistance) distance = Math.max(1, Math.floor(maxDistance * 0.6));
    var normal = mass * G;
    var friction = mu * normal;
    var initialK = 0.5 * mass * speed0 * speed0;
    var frictionWork = -friction * distance;
    var finalK = initialK + frictionWork;
    var speed = Math.sqrt(2 * finalK / mass);
    var object = context(variant, ["maintenance sled", "sliding crate", "test puck"]);
    return answer(
      "friction-energy",
      "A " + mass + " kg " + object + " moves at " + speed0 + " m/s on a level rough surface with \\(\\mu_k=" + n(mu) + "\\). Find its speed after sliding " + distance + " m.",
      "energy",
      ["v₀ = " + speed0 + " m/s", "distance " + distance + " m", "N upward", "W downward", "f_k opposite motion", "work by friction negative"],
      [
        "\\(N=mg=" + mass + "(9.8)=" + n(normal, 1) + "\\ \\mathrm{N}\\), so \\(f_k=\\mu_kN=" + n(friction) + "\\ \\mathrm{N}\\).",
        "\\(K_i=\\tfrac12mv_0^2=\\tfrac12(" + mass + ")(" + speed0 + ")^2=" + n(initialK) + "\\ \\mathrm{J}\\).",
        "\\(W_f=-f_ks=-(" + n(friction) + ")(" + distance + ")=" + n(frictionWork) + "\\ \\mathrm{J}\\).",
        "\\(K_f=K_i+W_f=" + n(initialK) + n(frictionWork, 2) + "=" + n(finalK) + "\\ \\mathrm{J}\\).",
        "\\(v_f=\\sqrt{\\dfrac{2K_f}{m}}=\\sqrt{\\dfrac{2(" + n(finalK) + ")}{" + mass + "}}=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}\\)."
      ],
      "\\(\\boxed{v_f=" + n(speed) + "\\ \\mathrm{m\\,s^{-1}}}\\)",
      "Friction does negative work, so the final kinetic energy and speed are lower; joules divided by kilograms gives \\(\\mathrm{m^2\\,s^{-2}}\\)."
    );
  }

  window.DPEN102_FAMILIES = window.DPEN102_FAMILIES || {};
  Object.assign(window.DPEN102_FAMILIES, {
    "static-incline": staticIncline,
    "kinetic-incline": kineticIncline,
    "level-friction": levelFriction,
    "belt": belt,
    "centroid": centroid,
    "centroid-hole": centroidHole,
    "rectangle-I": rectangleI,
    "composite-I": compositeI,
    "work-force": workForce,
    "fall": fall,
    "spring": spring,
    "friction-energy": frictionEnergy
  });
}());
