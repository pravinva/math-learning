(function () {
  "use strict";

  var root = typeof window !== "undefined" ? window : globalThis;
  var families = root.DPEN102_FAMILIES || {};

  function hash(value) {
    var text = String(value);
    var h = 2166136261;
    for (var i = 0; i < text.length; i += 1) {
      h ^= text.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    return h >>> 0;
  }

  function variantIndex(variant) {
    var key = String(variant || "A").trim().toUpperCase();
    return key === "B" ? 1 : key === "C" ? 2 : 0;
  }

  function choose(items, seed, variant, salt) {
    return items[(hash(String(seed) + "|" + salt) + variantIndex(variant)) % items.length];
  }

  function context(seed, variant, salt) {
    return choose(
      ["a laboratory test rig", "a lightweight access platform", "a workshop lifting frame"],
      seed,
      variant,
      salt
    );
  }

  function n(value, digits) {
    var rounded = Number(value.toFixed(digits === undefined ? 2 : digits));
    return String(rounded);
  }

  function answer(tag, prompt, type, labels, steps, final, check) {
    return {
      tag: tag,
      prompt: prompt,
      diagram: { type: type, labels: labels },
      steps: steps,
      final: final,
      check: check
    };
  }

  Object.assign(families, {
    "axial-stress": function (seed, variant) {
      var d = choose([
        { p: 48, b: 24, t: 10 },
        { p: 72, b: 30, t: 12 },
        { p: 90, b: 36, t: 10 }
      ], seed, variant, "axial-stress");
      var area = d.b * d.t;
      var stress = d.p * 1000 / area;
      return answer(
        "Axial stress",
        "In " + context(seed, variant, "as-context") + ", a flat tie of width " + d.b +
          " mm and thickness " + d.t + " mm carries a tensile load of " + d.p +
          " kN. Determine its average normal stress.",
        "section",
        ["P = " + d.p + " kN", "b = " + d.b + " mm", "t = " + d.t + " mm", "tension"],
        [
          "\\(P=" + d.p + "\\times10^3=" + (d.p * 1000) + "\\ \\mathrm{N}\\).",
          "\\(A=bt=" + d.b + "\\times" + d.t + "=" + area + "\\ \\mathrm{mm^2}\\).",
          "\\(\\sigma=P/A=" + (d.p * 1000) + "/" + area + "=" + n(stress) + "\\ \\mathrm{N/mm^2}\\).",
          "\\(1\\ \\mathrm{N/mm^2}=1\\ \\mathrm{MPa}\\), so \\(\\sigma=" + n(stress) + "\\ \\mathrm{MPa}\\) in tension."
        ],
        "\\(\\boxed{\\sigma=" + n(stress) + "\\ \\mathrm{MPa}\\text{ (tension)}}\\)",
        "The stress is positive for a tensile load and is in the expected tens-to-hundreds of MPa range for a metal tie."
      );
    },

    "strain": function (seed, variant) {
      var d = choose([
        { p: 36, l: 1200, a: 300, e: 200000 },
        { p: 54, l: 1500, a: 450, e: 200000 },
        { p: 42, l: 1800, a: 350, e: 210000 }
      ], seed, variant, "strain");
      var stress = d.p * 1000 / d.a;
      var strain = stress / d.e;
      var delta = strain * d.l;
      return answer(
        "Axial strain and extension",
        "A prismatic steel member in " + context(seed, variant, "strain-context") + " has length " +
          d.l + " mm, area " + d.a + " mm², and modulus \\(E=" + d.e +
          "\\) MPa. It carries " + d.p + " kN tension. Find strain and extension.",
        "section",
        ["P = " + d.p + " kN", "L = " + d.l + " mm", "A = " + d.a + " mm²", "E = " + d.e + " MPa"],
        [
          "\\(P=" + d.p + "\\times10^3=" + (d.p * 1000) + "\\ \\mathrm{N}\\).",
          "\\(\\sigma=P/A=" + (d.p * 1000) + "/" + d.a + "=" + n(stress) + "\\ \\mathrm{MPa}\\).",
          "\\(\\varepsilon=\\sigma/E=" + n(stress) + "/" + d.e + "=" + n(strain, 6) + "\\).",
          "\\(\\delta=\\varepsilon L=" + n(strain, 6) + "\\times" + d.l + "=" + n(delta, 3) + "\\ \\mathrm{mm}\\)."
        ],
        "\\(\\boxed{\\varepsilon=" + n(strain, 6) + ",\\quad \\delta=" + n(delta, 3) + "\\ \\mathrm{mm}}\\)",
        "The strain is much less than 1% and the extension is sub-millimetre, consistent with elastic steel."
      );
    },

    "allowable": function (seed, variant) {
      var d = choose([
        { sy: 250, fs: 2, a: 320 },
        { sy: 300, fs: 2.5, a: 450 },
        { sy: 280, fs: 2, a: 375 }
      ], seed, variant, "allowable");
      var allowable = d.sy / d.fs;
      var load = allowable * d.a / 1000;
      return answer(
        "Allowable axial load",
        "A member used in " + context(seed, variant, "allow-context") + " has yield stress " + d.sy +
          " MPa and area " + d.a + " mm². Using a factor of safety of " + d.fs +
          " against yielding, determine the allowable axial load.",
        "section",
        ["σy = " + d.sy + " MPa", "FS = " + d.fs, "A = " + d.a + " mm²", "Pallow = ?"],
        [
          "\\(\\mathrm{FS}=\\sigma_y/\\sigma_{allow}\\).",
          "\\(\\sigma_{allow}=\\sigma_y/\\mathrm{FS}=" + d.sy + "/" + d.fs + "=" + n(allowable) + "\\ \\mathrm{MPa}\\).",
          "\\(P_{allow}=\\sigma_{allow}A=" + n(allowable) + "\\times" + d.a + "=" + n(load * 1000) + "\\ \\mathrm{N}\\).",
          "\\(P_{allow}=" + n(load * 1000) + "/1000=" + n(load) + "\\ \\mathrm{kN}\\)."
        ],
        "\\(\\boxed{P_{allow}=" + n(load) + "\\ \\mathrm{kN}}\\)",
        "The allowable stress is below yield stress by exactly the stated factor of safety."
      );
    },

    "internal-cut": function (seed, variant) {
      var d = choose([
        { right: 62, left: 18, x: 1.4 },
        { right: 75, left: 25, x: 1.8 },
        { right: 84, left: 30, x: 2.1 }
      ], seed, variant, "internal-cut");
      var force = d.right - d.left;
      return answer(
        "Internal axial force",
        "Cut an axially loaded bar at section C, " + d.x + " m from its left end. To the right of C, a " +
          d.right + " kN force acts rightward and a " + d.left +
          " kN force acts leftward. Determine the internal normal force at C.",
        "cut",
        ["cut C at " + d.x + " m", d.right + " kN →", "← " + d.left + " kN", "N_C = ?"],
        [
          "\\(\\text{Isolate the right segment and take rightward as positive.}\\)",
          "\\(\\sum F_x=0:\\ -N_C+" + d.right + "-" + d.left + "=0\\).",
          "\\(N_C=" + d.right + "-" + d.left + "=" + force + "\\ \\mathrm{kN}\\).",
          "\\(N_C>0\\) under the tension-positive cut convention, so the bar is in tension at C."
        ],
        "\\(\\boxed{N_C=" + force + "\\ \\mathrm{kN}\\text{ (tension)}}\\)",
        "The internal force equals the net external force on the isolated segment and is smaller than the largest applied load."
      );
    },

    "beam-point": function (seed, variant) {
      var d = choose([
        { p: 18, l: 6, a: 2 },
        { p: 24, l: 8, a: 3 },
        { p: 30, l: 10, a: 4 }
      ], seed, variant, "beam-point");
      var b = d.l - d.a;
      var ra = d.p * b / d.l;
      var rb = d.p * d.a / d.l;
      var m = ra * d.a;
      return answer(
        "Simply supported beam: point load",
        "A simply supported beam of span " + d.l + " m carries a " + d.p +
          " kN downward point load " + d.a + " m from support A. Find both reactions and the maximum bending moment.",
        "beam",
        ["A: pin", "B: roller", "P = " + d.p + " kN", "a = " + d.a + " m"],
        [
          "\\(\\sum M_A=0:\\ R_B(" + d.l + ")-" + d.p + "(" + d.a + ")=0\\).",
          "\\(R_B=" + d.p + "\\times" + d.a + "/" + d.l + "=" + n(rb) + "\\ \\mathrm{kN}\\uparrow\\).",
          "\\(\\sum F_y=0:\\ R_A=" + d.p + "-" + n(rb) + "=" + n(ra) + "\\ \\mathrm{kN}\\uparrow\\).",
          "\\(M_{max}=M(x=" + d.a + ")=R_Aa=" + n(ra) + "\\times" + d.a + "=" + n(m) + "\\ \\mathrm{kN\\,m}\\)."
        ],
        "\\(\\boxed{R_A=" + n(ra) + "\\ \\mathrm{kN},\\ R_B=" + n(rb) + "\\ \\mathrm{kN},\\ M_{max}=" + n(m) + "\\ \\mathrm{kN\\,m}}\\)",
        "The reactions add to the applied load, and the larger reaction is nearer the load."
      );
    },

    "beam-udl": function (seed, variant) {
      var d = choose([
        { w: 4, l: 6 },
        { w: 5, l: 8 },
        { w: 6, l: 10 }
      ], seed, variant, "beam-udl");
      var total = d.w * d.l;
      var reaction = total / 2;
      var moment = d.w * d.l * d.l / 8;
      return answer(
        "Simply supported beam: UDL",
        "A simply supported beam of span " + d.l + " m carries a uniform load of " + d.w +
          " kN/m over the full span. Determine the reactions and maximum bending moment.",
        "beam",
        ["A: pin", "B: roller", "w = " + d.w + " kN/m", "L = " + d.l + " m"],
        [
          "\\(W=wL=" + d.w + "\\times" + d.l + "=" + total + "\\ \\mathrm{kN}\\), acting at midspan.",
          "\\(R_A=R_B=W/2=" + total + "/2=" + reaction + "\\ \\mathrm{kN}\\uparrow\\).",
          "\\(V(x)=R_A-wx\\), hence \\(V=0\\) at \\(x=R_A/w=" + n(reaction / d.w) + "\\ \\mathrm{m}\\).",
          "\\(M_{max}=wL^2/8=" + d.w + "\\times" + d.l + "^2/8=" + n(moment) + "\\ \\mathrm{kN\\,m}\\)."
        ],
        "\\(\\boxed{R_A=R_B=" + reaction + "\\ \\mathrm{kN},\\quad M_{max}=" + n(moment) + "\\ \\mathrm{kN\\,m}}\\)",
        "Symmetry gives equal reactions, and maximum moment occurs at midspan where shear is zero."
      );
    },

    "beam-mixed": function (seed, variant) {
      var d = choose([
        { l: 6, w: 2, p: 8, a: 2 },
        { l: 8, w: 1.5, p: 12, a: 5 },
        { l: 10, w: 2, p: 15, a: 4 }
      ], seed, variant, "beam-mixed");
      var udl = d.w * d.l;
      var rb = (udl * d.l / 2 + d.p * d.a) / d.l;
      var ra = udl + d.p - rb;
      var vLeft = ra - d.w * d.a;
      var vRight = vLeft - d.p;
      var moment = ra * d.a - d.w * d.a * d.a / 2;
      return answer(
        "Beam with mixed loading",
        "A simply supported beam of span " + d.l + " m carries " + d.w +
          " kN/m over the whole span and a " + d.p + " kN point load at " + d.a +
          " m from A. Find the reactions and maximum bending moment.",
        "beam",
        ["A: pin", "B: roller", "w = " + d.w + " kN/m", "P = " + d.p + " kN at " + d.a + " m"],
        [
          "\\(W=wL=" + d.w + "\\times" + d.l + "=" + udl + "\\ \\mathrm{kN}\\) at \\(L/2=" + n(d.l / 2) + "\\ \\mathrm{m}\\).",
          "\\(\\sum M_A=0:\\ R_B(" + d.l + ")=" + udl + "(" + n(d.l / 2) + ")+" + d.p + "(" + d.a + ")\\), so \\(R_B=" + n(rb) + "\\ \\mathrm{kN}\\).",
          "\\(R_A=W+P-R_B=" + udl + "+" + d.p + "-" + n(rb) + "=" + n(ra) + "\\ \\mathrm{kN}\\).",
          "\\(V(a^-)=" + n(vLeft) + "\\ \\mathrm{kN}\\) and \\(V(a^+)=" + n(vRight) + "\\ \\mathrm{kN}\\); the sign change locates \\(M_{max}\\) at the point load.",
          "\\(M_{max}=R_Aa-wa^2/2=" + n(ra) + "(" + d.a + ")-" + d.w + "(" + d.a + ")^2/2=" + n(moment) + "\\ \\mathrm{kN\\,m}\\)."
        ],
        "\\(\\boxed{R_A=" + n(ra) + "\\ \\mathrm{kN},\\ R_B=" + n(rb) + "\\ \\mathrm{kN},\\ M_{max}=" + n(moment) + "\\ \\mathrm{kN\\,m}}\\)",
        "The reactions sum to the UDL resultant plus point load, and shear changes from positive to negative at the reported maximum."
      );
    },

    "cantilever-sfd": function (seed, variant) {
      var d = choose([
        { l: 3, w: 2, p: 5 },
        { l: 4, w: 2.5, p: 6 },
        { l: 5, w: 3, p: 8 }
      ], seed, variant, "cantilever-sfd");
      var total = d.w * d.l;
      var shear = -(d.p + total);
      var moment = -(d.p * d.l + d.w * d.l * d.l / 2);
      return answer(
        "Cantilever shear-force diagram",
        "A cantilever fixed at A has length " + d.l + " m, a full-length UDL of " + d.w +
          " kN/m, and a downward tip load of " + d.p +
          " kN. Determine the key SFD ordinates and fixed-end moment.",
        "sfd",
        ["A: fixed", "free end", "w = " + d.w + " kN/m", "P = " + d.p + " kN"],
        [
          "\\(W=wL=" + d.w + "\\times" + d.l + "=" + total + "\\ \\mathrm{kN}\\).",
          "\\(V(L^-)=-P=-" + d.p + "\\ \\mathrm{kN}\\) immediately left of the tip load.",
          "\\(V(x)=-P-w(L-x)\\), so \\(V(0^+)=-" + d.p + "-" + total + "=" + n(shear) + "\\ \\mathrm{kN}\\).",
          "\\(M_A=-[PL+W(L/2)]=-["
            + d.p + "(" + d.l + ")+" + total + "(" + n(d.l / 2) + ")]=" + n(moment) + "\\ \\mathrm{kN\\,m}\\).",
          "\\(R_A=P+W=" + (d.p + total) + "\\ \\mathrm{kN}\\uparrow\\), balancing the total downward load."
        ],
        "\\(\\boxed{V_{tip}=-" + d.p + "\\ \\mathrm{kN},\\ V_A=" + n(shear) + "\\ \\mathrm{kN},\\ M_A=" + n(moment) + "\\ \\mathrm{kN\\,m}}\\)",
        "The SFD changes linearly under the UDL, and its fixed-end magnitude equals the total vertical reaction."
      );
    },

    "truss-triangle": function (seed, variant) {
      var d = choose([
        { p: 24, half: 3, h: 4 },
        { p: 30, half: 4, h: 3 },
        { p: 36, half: 4, h: 4 }
      ], seed, variant, "truss-triangle");
      var len = Math.sqrt(d.half * d.half + d.h * d.h);
      var sin = d.h / len;
      var cos = d.half / len;
      var diagonal = d.p / (2 * sin);
      var bottom = diagonal * cos;
      return answer(
        "Three-member triangular truss",
        "A symmetric triangular truss has pin A and roller B separated by " + (2 * d.half) +
          " m. Apex C is " + d.h + " m above midspan and carries " + d.p +
          " kN downward. Find all member forces and classify them.",
        "truss",
        ["A: pin", "B: roller", "C: " + d.p + " kN ↓", "half-span = " + d.half + " m"],
        [
          "\\(L_{AC}=L_{BC}=\\sqrt{" + d.half + "^2+" + d.h + "^2}=" + n(len, 3) + "\\ \\mathrm{m}\\), with \\(\\sin\\theta=" + n(sin, 4) + "\\).",
          "\\(A_y=B_y=P/2=" + d.p + "/2=" + n(d.p / 2) + "\\ \\mathrm{kN}\\).",
          "\\(\\sum F_y\\text{ at C}=0:\\ 2F_d\\sin\\theta=P\\), so \\(F_{AC}=F_{BC}=" + n(diagonal) + "\\ \\mathrm{kN}\\) compression.",
          "\\(\\sum F_x\\text{ at A}=0:\\ F_{AB}=F_{AC}\\cos\\theta=" + n(diagonal) + "(" + n(cos, 4) + ")=" + n(bottom) + "\\ \\mathrm{kN}\\) tension."
        ],
        "\\(\\boxed{F_{AC}=F_{BC}=" + n(diagonal) + "\\ \\mathrm{kN}\\ (C),\\quad F_{AB}=" + n(bottom) + "\\ \\mathrm{kN}\\ (T)}\\)",
        "Equal geometry and central loading give equal diagonal forces; their upward components sum to the applied load."
      );
    },

    "zero-force": function (seed, variant) {
      var d = choose([
        { p: 20, half: 3, h: 4 },
        { p: 30, half: 4, h: 3 },
        { p: 28, half: 4, h: 4 }
      ], seed, variant, "zero-force");
      var len = Math.sqrt(d.half * d.half + d.h * d.h);
      var diagonal = d.p * len / (2 * d.h);
      var chord = diagonal * d.half / len;
      return answer(
        "Zero-force member",
        "A determinate king-post truss has A–C–D collinear along the bottom, apex B directly above C, and members AB, BD, AC, CD, BC. A and D are supports; " +
          d.p + " kN acts downward at B. With AC = CD = " + d.half + " m and BC = " + d.h +
          " m, identify the zero-force member and classify the others.",
        "truss",
        ["A: pin", "D: roller", "B: " + d.p + " kN ↓", "C: unloaded joint"],
        [
          "\\(\\text{At unloaded joint C, AC and CD are collinear; therefore }F_{BC}=0.\\)",
          "\\(A_y=D_y=P/2=" + d.p + "/2=" + n(d.p / 2) + "\\ \\mathrm{kN}\\).",
          "\\(\\sin\\theta=" + d.h + "/\\sqrt{" + d.half + "^2+" + d.h + "^2}=" + n(d.h / len, 4) + "\\), so \\(F_{AB}=F_{BD}=P/(2\\sin\\theta)=" + n(diagonal) + "\\ \\mathrm{kN}\\) compression.",
          "\\(F_{AC}=F_{CD}=F_{AB}\\cos\\theta=" + n(diagonal) + "(" + n(d.half / len, 4) + ")=" + n(chord) + "\\ \\mathrm{kN}\\) tension."
        ],
        "\\(\\boxed{F_{BC}=0;\\ F_{AB}=F_{BD}=" + n(diagonal) + "\\ \\mathrm{kN}\\ (C);\\ F_{AC}=F_{CD}=" + n(chord) + "\\ \\mathrm{kN}\\ (T)}\\)",
        "The zero-force result follows locally at joint C, while symmetry makes the two rafters and two bottom-chord forces pairwise equal."
      );
    },

    "truss-joint": function (seed, variant) {
      var d = choose([
        { p: 24, hload: 4, half: 3, h: 4 },
        { p: 30, hload: 6, half: 4, h: 3 },
        { p: 36, hload: 8, half: 4, h: 4 }
      ], seed, variant, "truss-joint");
      var len = Math.sqrt(d.half * d.half + d.h * d.h);
      var sin = d.h / len;
      var cos = d.half / len;
      var sum = d.p / sin;
      var difference = d.hload / cos;
      var left = (sum - difference) / 2;
      var right = (sum + difference) / 2;
      return answer(
        "Method of joints",
        "At apex joint C of a symmetric triangular truss, members CA and CB descend left and right by " +
          d.h + " m over a horizontal run of " + d.half + " m. Loads at C are " + d.p +
          " kN downward and " + d.hload + " kN rightward. Determine CA and CB.",
        "joint",
        ["joint C", d.p + " kN ↓", d.hload + " kN →", "run:rise = " + d.half + ":" + d.h],
        [
          "\\(L=\\sqrt{" + d.half + "^2+" + d.h + "^2}=" + n(len, 3) + "\\ \\mathrm{m};\\ \\sin\\theta=" + n(sin, 4) + ",\\ \\cos\\theta=" + n(cos, 4) + "\\).",
          "\\(\\sum F_y=0:\\ (C_{CA}+C_{CB})\\sin\\theta=" + d.p + "\\), so \\(C_{CA}+C_{CB}=" + n(sum) + "\\ \\mathrm{kN}\\).",
          "\\(\\sum F_x=0:\\ C_{CA}\\cos\\theta-C_{CB}\\cos\\theta+" + d.hload + "=0\\), so \\(C_{CB}-C_{CA}=" + n(difference) + "\\ \\mathrm{kN}\\).",
          "\\(C_{CA}=(" + n(sum) + "-" + n(difference) + ")/2=" + n(left) + "\\ \\mathrm{kN}\\) compression.",
          "\\(C_{CB}=(" + n(sum) + "+" + n(difference) + ")/2=" + n(right) + "\\ \\mathrm{kN}\\) compression."
        ],
        "\\(\\boxed{F_{CA}=" + n(left) + "\\ \\mathrm{kN}\\ (C),\\quad F_{CB}=" + n(right) + "\\ \\mathrm{kN}\\ (C)}\\)",
        "Both forces remain compressive, and their vertical components exactly balance the downward load."
      );
    },

    "truss-section": function (seed, variant) {
      var d = choose([
        { w: 12, panel: 4, h: 3 },
        { w: 18, panel: 5, h: 4 },
        { w: 20, panel: 6, h: 4 }
      ], seed, variant, "truss-section");
      var ab = d.w * (d.panel / 2) / d.h;
      return answer(
        "Method of sections",
        "A two-panel determinate Warren truss has bottom joints A–B–C spaced " + d.panel +
          " m apart, top joints D and E above the two panel midpoints at height " + d.h +
          " m, and members AB, BC, AD, DB, DC, DE, EC. A is pinned, C is a roller, and " +
          d.w + " kN acts downward at each of D and E. Use a section to find member AB.",
        "cut",
        ["A: pin", "C: roller", "D,E: " + d.w + " kN ↓", "height = " + d.h + " m"],
        [
          "\\(\\sum F_y=0:\\ A_y+C_y=2(" + d.w + ")=" + (2 * d.w) + "\\ \\mathrm{kN}\\).",
          "\\(\\text{By symmetry, }A_y=C_y=" + d.w + "\\ \\mathrm{kN}.\\)",
          "\\(\\text{Cut members AB, DB and DE, then use the left section; the DB and DE lines meet at D.}\\)",
          "\\(\\sum M_D=0:\\ F_{AB}(" + d.h + ")-A_y(" + n(d.panel / 2) + ")=0\\).",
          "\\(F_{AB}=" + d.w + "(" + n(d.panel / 2) + ")/" + d.h + "=" + n(ab) + "\\ \\mathrm{kN}\\); the assumed tensile direction is positive."
        ],
        "\\(\\boxed{F_{AB}=" + n(ab) + "\\ \\mathrm{kN}\\text{ (tension)}}\\)",
        "The bottom chord is tensile under downward loading, and its moment about D balances the support-reaction moment."
      );
    }
  });

  root.DPEN102_FAMILIES = families;
}());
