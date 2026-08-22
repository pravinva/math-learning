/* DPEN102 Revision Hub — Foundations question families (Weeks 1–3 core statics).
   Standalone browser script: no modules, no imports, no DOM access.
   Each family is a deterministic generator with signature (seed, variant) where
   variant is "A", "B" or "C", returning:
     { tag, prompt, diagram:{ type, labels }, steps, final, check }
   All mechanics uses g = 9.8 m/s². */
(function () {
  'use strict';

  var G = 9.8;
  var FAM = (window.DPEN102_FAMILIES = window.DPEN102_FAMILIES || {});

  /* ---------- internal helpers: deterministic picks, rounding, escaping ---------- */

  function hash(str) {
    var h = 2166136261;
    for (var i = 0; i < str.length; i++) {
      h ^= str.charCodeAt(i);
      h = Math.imul(h, 16777619);
    }
    return h >>> 0;
  }

  // Variant offsets the index, so A/B/C always land on different list entries.
  function vIdx(variant) {
    var i = 'ABC'.indexOf(String(variant == null ? 'A' : variant).trim().toUpperCase());
    return i < 0 ? 0 : i;
  }

  function pick(list, seed, salt, variant) {
    var base = hash(String(seed) + '::' + salt) % list.length;
    return list[(base + vIdx(variant)) % list.length];
  }

  function rnd(x, d) {
    var p = Math.pow(10, d);
    var r = Math.round(x * p + (x >= 0 ? 1e-9 : -1e-9)) / p;
    return r === 0 ? 0 : r;
  }

  function f(x, d) {
    return rnd(x, d).toFixed(d);
  }

  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function sin(deg) { return Math.sin(deg * Math.PI / 180); }
  function cos(deg) { return Math.cos(deg * Math.PI / 180); }
  function tan(deg) { return Math.tan(deg * Math.PI / 180); }

  function dirDeg(x, y) {
    return (Math.atan2(y, x) * 180 / Math.PI + 360) % 360;
  }

  function quadName(deg) {
    var d = ((deg % 360) + 360) % 360;
    if (d === 0 || d === 90 || d === 180 || d === 270) return 'on a coordinate axis';
    if (d < 90) return 'quadrant I';
    if (d < 180) return 'quadrant II';
    if (d < 270) return 'quadrant III';
    return 'quadrant IV';
  }

  function senseWord(m) {
    return m > 0 ? 'anticlockwise' : (m < 0 ? 'clockwise' : 'balanced');
  }

  /* ---------------------------- 1. dynamics ---------------------------- */
  /* Objective: apply Newton's second law to a body with vertical acceleration. */
  FAM['dynamics'] = function (seed, variant) {
    var ctx = pick([
      { site: 'goods lift', body: 'lift car' },
      { site: 'mine winder', body: 'cage' },
      { site: 'tower crane', body: 'concrete skip' },
      { site: 'construction hoist', body: 'material platform' },
      { site: 'shaft winch', body: 'spoil bucket' },
      { site: 'workshop gantry', body: 'engine cradle' }
    ], seed, 'dynamics.ctx', variant);
    var m = pick([600, 750, 900, 1050, 1200, 1400], seed, 'dynamics.m', variant);
    var a = pick([1, 2, 3], seed, 'dynamics.a', variant);
    var up = pick([true, false], seed, 'dynamics.dir', variant);

    var ay = up ? a : -a;
    var W = m * G;
    var T = m * (G + ay);
    var motion = up ? 'accelerates upward' : 'accelerates downward';
    var site = esc(ctx.site);
    var body = esc(ctx.body);

    return {
      tag: 'dynamics',
      prompt: 'A ' + m + ' kg ' + body + ' on a ' + site + ' ' + motion +
        ' at ' + a + '.00 m/s\u00B2 on a single vertical cable. Draw the free-body diagram of the ' +
        body + ' and determine the cable tension. Take g = 9.8 m/s\u00B2.',
      diagram: {
        type: 'fbd',
        labels: [
          'T = ? (cable, up)',
          'm = ' + m + ' kg',
          'W = mg = ' + f(W, 0) + ' N',
          'a = ' + a + ' m/s\u00B2 ' + (up ? '\u2191' : '\u2193')
        ]
      },
      steps: [
        'Isolate the ' + body + '. Only two forces act on it: cable tension \\(T\\) upward and weight \\(W\\) downward. Take upward as positive, so \\(a_y=' + (up ? '+' : '-') + a + '\\text{ m/s}^2\\).',
        'Weight: \\(W=mg=' + m + '(9.8)=' + f(W, 0) + '\\text{ N}\\).',
        'Newton\u2019s second law in the vertical direction: \\(\\Sigma F_y=ma_y\\Rightarrow T-' + f(W, 0) + '=' + m + '(' + (up ? '' : '-') + a + ')\\).',
        'Inertia term: \\(ma_y=' + m + '(' + (up ? '' : '-') + a + ')=' + (ay < 0 ? '-' : '') + f(Math.abs(m * ay), 0) + '\\text{ N}\\).',
        'Solve: \\(T=' + f(W, 0) + (ay < 0 ? '-' : '+') + f(Math.abs(m * ay), 0) + '=' + f(T, 0) + '\\text{ N}=' + f(T / 1000, 2) + '\\text{ kN}\\).'
      ],
      final: '\\(T=' + f(T, 0) + '\\text{ N}=' + f(T / 1000, 2) + '\\text{ kN}\\)',
      check: 'Units: N = kg\u00B7m/s\u00B2, correct for a force. The tension is ' +
        (up ? 'larger' : 'smaller') + ' than the static weight \\(' + f(W, 0) + '\\text{ N}\\) by exactly \\(|ma_y|=' +
        f(Math.abs(m * ay), 0) + '\\text{ N}\\), which is what ' + (up ? 'upward' : 'downward') +
        ' acceleration demands. At \\(a=0\\) the result would collapse back to \\(T=W\\).'
    };
  };

  /* --------------------------- 2. equilibrium --------------------------- */
  /* Objective: particle equilibrium on a horizontal plane with an inclined pull. */
  FAM['equilibrium'] = function (seed, variant) {
    var ctx = pick([
      { obj: 'timber crate', place: 'a workshop floor' },
      { obj: 'steel toolbox', place: 'a level loading dock' },
      { obj: 'packing case', place: 'a concrete slab' },
      { obj: 'machine base', place: 'a level workbench' },
      { obj: 'pallet of tiles', place: 'a warehouse floor' },
      { obj: 'transformer housing', place: 'a level steel deck' }
    ], seed, 'equilibrium.ctx', variant);
    var m = pick([40, 50, 60, 70, 80, 90], seed, 'equilibrium.m', variant);
    var P = pick([200, 250, 300, 350], seed, 'equilibrium.P', variant);
    var th = pick([20, 25, 30, 35, 40], seed, 'equilibrium.th', variant);

    var W = m * G;
    var Px = P * cos(th);
    var Py = P * sin(th);
    var N = W - Py;
    var fr = Px;
    var muReq = fr / N;
    var obj = esc(ctx.obj);
    var place = esc(ctx.place);

    return {
      tag: 'equilibrium',
      prompt: 'A ' + m + ' kg ' + obj + ' rests on ' + place + ' and stays at rest while a rope pulls it with ' +
        P + ' N at ' + th + '\u00B0 above the horizontal. Draw the free-body diagram and find the normal reaction and the friction force required for equilibrium.',
      diagram: {
        type: 'fbd',
        labels: [
          'N = ? (up)',
          'P = ' + P + ' N at ' + th + '\u00B0',
          'W = ' + f(W, 0) + ' N',
          'f = ? (opposes pull)'
        ]
      },
      steps: [
        'The ' + obj + ' is at rest, so both equilibrium equations apply: \\(\\Sigma F_x=0\\) and \\(\\Sigma F_y=0\\).',
        'Resolve the rope pull: \\(P_x=' + P + '\\cos' + th + '^\\circ=' + f(Px, 2) + '\\text{ N}\\) and \\(P_y=' + P + '\\sin' + th + '^\\circ=' + f(Py, 2) + '\\text{ N}\\).',
        'Weight: \\(W=mg=' + m + '(9.8)=' + f(W, 0) + '\\text{ N}\\) downward.',
        'Vertical equilibrium: \\(N+P_y-W=0\\Rightarrow N=' + f(W, 0) + '-' + f(Py, 2) + '=' + f(N, 2) + '\\text{ N}\\).',
        'Horizontal equilibrium: \\(f-P_x=0\\Rightarrow f=' + f(Px, 2) + '\\text{ N}\\), acting horizontally opposite to the pull.'
      ],
      final: '\\(N=' + f(N, 1) + '\\text{ N}\\) upward and \\(f=' + f(fr, 1) + '\\text{ N}\\) opposing the pull',
      check: 'Both answers are forces in N. The reaction is less than the weight \\(' + f(W, 0) +
        '\\text{ N}\\) because the rope lifts part of the load, which is physically sensible; a horizontal rope would give \\(N=W\\). For the case to hold without slipping the surface must supply \\(\\mu_s\\) of at least \\(f/N=' +
        f(muReq, 3) + '\\).'
    };
  };

  /* -------------------------- 3. inclined-pull -------------------------- */
  /* Objective: equilibrium on an incline with kinetic friction, force along the slope. */
  FAM['inclined-pull'] = function (seed, variant) {
    var ctx = pick([
      { obj: 'drum', where: 'a loading ramp' },
      { obj: 'crate', where: 'a timber skid ramp' },
      { obj: 'trolley', where: 'a car-park ramp' },
      { obj: 'stone block', where: 'an excavation ramp' },
      { obj: 'toolbox', where: 'a scaffold ramp' },
      { obj: 'pallet', where: 'a factory ramp' }
    ], seed, 'incline.ctx', variant);
    var m = pick([25, 30, 40, 50, 60, 75], seed, 'incline.m', variant);
    var th = pick([15, 20, 25, 30], seed, 'incline.th', variant);
    var mu = pick([0.20, 0.25, 0.30, 0.35], seed, 'incline.mu', variant);

    var W = m * G;
    var Wn = W * cos(th);
    var Wt = W * sin(th);
    var fk = mu * Wn;
    var P = Wt + fk;
    var obj = esc(ctx.obj);
    var where = esc(ctx.where);

    return {
      tag: 'inclined-pull',
      prompt: 'A ' + m + ' kg ' + obj + ' is hauled up ' + where + ' inclined at ' + th +
        '\u00B0 to the horizontal at constant speed by a force P acting parallel to the slope. The coefficient of kinetic friction is ' +
        f(mu, 2) + '. Draw the free-body diagram on slope axes and find P.',
      diagram: {
        type: 'incline',
        labels: [
          'P = ? (up the slope)',
          'W = ' + f(W, 0) + ' N at ' + th + '\u00B0 slope',
          'N = ' + f(Wn, 2) + ' N',
          'f\u2096 = ' + f(fk, 2) + ' N (down slope)'
        ]
      },
      steps: [
        'Constant speed means zero acceleration, so this is an equilibrium problem. Use axes along and normal to the slope.',
        'Resolve the weight \\(W=mg=' + m + '(9.8)=' + f(W, 0) + '\\text{ N}\\): normal component \\(W\\cos' + th + '^\\circ=' + f(Wn, 2) + '\\text{ N}\\), down-slope component \\(W\\sin' + th + '^\\circ=' + f(Wt, 2) + '\\text{ N}\\).',
        'Normal direction: \\(N=W\\cos' + th + '^\\circ=' + f(Wn, 2) + '\\text{ N}\\) (P has no normal component because it is parallel to the slope).',
        'Sliding friction opposes the upward motion, so it acts down the slope: \\(f_k=\\mu_kN=' + f(mu, 2) + '(' + f(Wn, 2) + ')=' + f(fk, 2) + '\\text{ N}\\).',
        'Slope direction: \\(P-W\\sin' + th + '^\\circ-f_k=0\\Rightarrow P=' + f(Wt, 2) + '+' + f(fk, 2) + '=' + f(P, 2) + '\\text{ N}\\).'
      ],
      final: '\\(P=' + f(P, 1) + '\\text{ N}\\) up the slope',
      check: 'Units are N throughout. P must exceed the gravity component \\(' + f(Wt, 2) +
        '\\text{ N}\\) because friction also resists the motion, and it stays well below the full weight \\(' +
        f(W, 0) + '\\text{ N}\\) \u2014 both are the expected trends for a shallow ramp. Setting \\(\\mu_k=0\\) would recover \\(P=' +
        f(Wt, 1) + '\\text{ N}\\).'
    };
  };

  /* --------------------------- 4. connected --------------------------- */
  /* Objective: connected bodies over a pulley — system acceleration and cord tension. */
  FAM['connected'] = function (seed, variant) {
    var ctx = pick([
      { top: 'trolley', bench: 'a smooth horizontal bench' },
      { top: 'test block', bench: 'a low-friction air table' },
      { top: 'slider', bench: 'a smooth horizontal rail' },
      { top: 'carriage', bench: 'a smooth machine bed' },
      { top: 'sample block', bench: 'a polished horizontal plate' },
      { top: 'runner', bench: 'a smooth horizontal track' }
    ], seed, 'connected.ctx', variant);
    var m1 = pick([5, 6, 8, 10, 12, 15], seed, 'connected.m1', variant);
    var m2 = pick([3, 4, 5, 7, 9], seed, 'connected.m2', variant);

    var W2 = m2 * G;
    var a = W2 / (m1 + m2);
    var T = m1 * a;
    var top = esc(ctx.top);
    var bench = esc(ctx.bench);

    return {
      tag: 'connected',
      prompt: 'A ' + m1 + ' kg ' + top + ' on ' + bench + ' is joined by a light inextensible cord running over a frictionless pulley to a ' +
        m2 + ' kg mass hanging freely. The system is released from rest. Find the acceleration of the system and the tension in the cord.',
      diagram: {
        type: 'system',
        labels: [
          'm\u2081 = ' + m1 + ' kg (bench)',
          'T = ? (cord)',
          'm\u2082 = ' + m2 + ' kg (hanging)',
          'W\u2082 = ' + f(W2, 1) + ' N \u2193'
        ]
      },
      steps: [
        'The cord is inextensible, so both bodies share the same acceleration magnitude \\(a\\); the pulley only changes the direction of the cord force.',
        'Treat the two masses as one system. The only unbalanced external force is the hanging weight \\(m_2g=' + m2 + '(9.8)=' + f(W2, 1) + '\\text{ N}\\); the bench is smooth, so no friction opposes it.',
        'System equation: \\(m_2g=(m_1+m_2)a\\Rightarrow a=' + f(W2, 1) + '/(' + m1 + '+' + m2 + ')=' + f(W2, 1) + '/' + (m1 + m2) + '=' + f(a, 3) + '\\text{ m/s}^2\\).',
        'Now isolate the ' + top + ' on the bench, where the cord tension is the only horizontal force: \\(T=m_1a=' + m1 + '(' + f(a, 3) + ')=' + f(T, 2) + '\\text{ N}\\).',
        'Verify with the hanging mass: \\(m_2g-T=' + f(W2, 1) + '-' + f(T, 2) + '=' + f(W2 - T, 2) + '\\text{ N}\\), and \\(m_2a=' + m2 + '(' + f(a, 3) + ')=' + f(m2 * a, 2) + '\\text{ N}\\); the two agree.'
      ],
      final: '\\(a=' + f(a, 2) + '\\text{ m/s}^2\\) and \\(T=' + f(T, 2) + '\\text{ N}\\)',
      check: 'Acceleration is in m/s\u00B2 and tension in N. The acceleration is less than \\(g=9.8\\text{ m/s}^2\\) because the bench mass must also be accelerated, and the tension \\(' +
        f(T, 2) + '\\text{ N}\\) is less than the hanging weight \\(' + f(W2, 1) +
        '\\text{ N}\\) \u2014 if they were equal the hanging mass could not accelerate downward.'
    };
  };

  /* ---------------------------- 5. moments ---------------------------- */
  /* Objective: signed net moment of two forces about a point. */
  FAM['moments'] = function (seed, variant) {
    var ctx = pick([
      'a wall bracket',
      'a bolted lever mechanism',
      'a control linkage',
      'a fabricated steel bracket',
      'a hinged inspection frame',
      'a crank assembly'
    ], seed, 'moments.ctx', variant);
    var F1 = pick([500, 600, 800, 900, 1000, 1200], seed, 'moments.F1', variant);
    var d1 = pick([250, 300, 350, 400], seed, 'moments.d1', variant);
    var F2 = pick([200, 300, 400, 500], seed, 'moments.F2', variant);
    var d2 = pick([800, 900, 1000, 1200], seed, 'moments.d2', variant);

    var M1 = -F1 * (d1 / 1000);
    var M2 = F2 * (d2 / 1000);
    var M = M1 + M2;
    var arm = esc(ctx);

    return {
      tag: 'moments',
      prompt: 'A horizontal arm on ' + arm + ' is pinned at O. A ' + F1 + ' N downward force acts ' + d1 +
        ' mm from O and a ' + F2 + ' N upward force acts ' + d2 +
        ' mm from O, both on the same side of O and both perpendicular to the arm. Taking anticlockwise as positive, find the net moment about O and state its sense.',
      diagram: {
        type: 'beam',
        labels: [
          'O (pin)',
          F1 + ' N \u2193 @ ' + d1 + ' mm',
          F2 + ' N \u2191 @ ' + d2 + ' mm',
          'anticlockwise positive'
        ]
      },
      steps: [
        'Convert the lever arms to metres so the moment comes out in N\u00B7m: \\(d_1=' + d1 + '\\text{ mm}=' + f(d1 / 1000, 3) + '\\text{ m}\\), \\(d_2=' + d2 + '\\text{ mm}=' + f(d2 / 1000, 3) + '\\text{ m}\\).',
        'Both forces are perpendicular to the arm, so each moment is simply \\(M=Fd\\) with the sign set by its sense.',
        'The downward force on the loaded side of O turns the arm clockwise: \\(M_1=-' + F1 + '(' + f(d1 / 1000, 3) + ')=' + f(M1, 2) + '\\text{ N\u00B7m}\\).',
        'The upward force on the same side turns the arm anticlockwise: \\(M_2=+' + F2 + '(' + f(d2 / 1000, 3) + ')=' + f(M2, 2) + '\\text{ N\u00B7m}\\).',
        'Add the signed moments: \\(M_O=' + f(M1, 2) + '+' + f(M2, 2) + '=' + f(M, 2) + '\\text{ N\u00B7m}\\)' +
          (M === 0 ? ', so the two load moments exactly balance and the arm has no tendency to rotate about O.'
                   : ', so the resultant sense is ' + senseWord(M) + '.')
      ],
      final: M === 0
        ? '\\(M_O=0\\text{ N\u00B7m}\\) \u2014 the two load moments cancel exactly'
        : '\\(M_O=' + f(M, 2) + '\\text{ N\u00B7m}\\), i.e. \\(' + f(Math.abs(M), 2) + '\\text{ N\u00B7m}\\) ' + senseWord(M),
      check: 'Units are N\u00B7m (force \u00D7 perpendicular distance). The answer must lie between the two individual moments \\(' +
        f(M1, 2) + '\\text{ N\u00B7m}\\) and \\(' + f(M2, 2) + '\\text{ N\u00B7m}\\) because they oppose each other, and ' +
        (M === 0 ? 'the zero result is consistent with \\(F_1d_1=F_2d_2\\), i.e. equal and opposite turning effects.'
                 : 'the sign correctly follows the larger contribution, giving a ' + senseWord(M) + ' resultant.')
    };
  };

  /* ------------------------- 6. beam-reactions ------------------------- */
  /* Objective: support reactions of a simply supported beam with two point loads. */
  FAM['beam-reactions'] = function (seed, variant) {
    var lay = pick([
      { L: 6, a: 2, b: 4 },
      { L: 8, a: 2, b: 5 },
      { L: 9, a: 3, b: 6 },
      { L: 10, a: 3, b: 7 },
      { L: 12, a: 4, b: 8 },
      { L: 7, a: 2, b: 5 }
    ], seed, 'beam.lay', variant);
    var P1 = pick([10, 12, 15, 18, 20, 24], seed, 'beam.P1', variant);
    var P2 = pick([8, 14, 16, 22, 25], seed, 'beam.P2', variant);
    var ctx = pick([
      'a simply supported floor beam',
      'a simply supported gantry beam',
      'a pin-and-roller supported bridge girder',
      'a simply supported crane runway beam',
      'a simply supported platform beam',
      'a simply supported roof purlin'
    ], seed, 'beam.ctx', variant);

    var L = lay.L, a = lay.a, b = lay.b;
    var total = P1 + P2;
    var mA = P1 * a + P2 * b;
    var RB = mA / L;
    var RA = total - RB;
    var beam = esc(ctx);

    return {
      tag: 'beam-reactions',
      prompt: beam + ' of span ' + L + ' m carries point loads of ' + P1 + ' kN at ' + a + ' m and ' + P2 +
        ' kN at ' + b + ' m from support A. Support B is at the far end. Draw the beam free-body diagram and find both vertical reactions.',
      diagram: {
        type: 'beam',
        labels: [
          'A: R_A = ? (x = 0)',
          P1 + ' kN \u2193 @ ' + a + ' m',
          P2 + ' kN \u2193 @ ' + b + ' m',
          'B: R_B = ? (x = ' + L + ' m)'
        ]
      },
      steps: [
        'Both supports carry vertical reactions only (pin plus roller, no horizontal load), so two equations are enough.',
        'Vertical equilibrium: \\(\\Sigma F_y=0\\Rightarrow R_A+R_B=' + P1 + '+' + P2 + '=' + total + '\\text{ kN}\\).',
        'Take moments about A so \\(R_A\\) drops out: \\(\\Sigma M_A=0\\Rightarrow ' + L + 'R_B=' + P1 + '(' + a + ')+' + P2 + '(' + b + ')=' + f(mA, 1) + '\\text{ kN\u00B7m}\\).',
        'Hence \\(R_B=' + f(mA, 1) + '/' + L + '=' + f(RB, 3) + '\\text{ kN}\\) upward.',
        'Back-substitute: \\(R_A=' + total + '-' + f(RB, 3) + '=' + f(RA, 3) + '\\text{ kN}\\) upward.',
        'Independent check with moments about B: \\(' + P1 + '(' + (L - a) + ')+' + P2 + '(' + (L - b) + ')=' + f(P1 * (L - a) + P2 * (L - b), 1) + '\\text{ kN\u00B7m}\\), and \\(R_A L=' + f(RA * L, 1) + '\\text{ kN\u00B7m}\\); they match.'
      ],
      final: '\\(R_A=' + f(RA, 2) + '\\text{ kN}\\) and \\(R_B=' + f(RB, 2) + '\\text{ kN}\\), both upward',
      check: 'Reactions are forces in kN and they sum to the applied total \\(' + total +
        '\\text{ kN}\\). The larger reaction is at the support nearer the heavier resultant of the loading, which matches intuition, and neither reaction is negative so no support is being pulled down.'
    };
  };

  /* ----------------------------- 7. couple ----------------------------- */
  /* Objective: couple moment M = Fd and its independence of the moment centre. */
  FAM['couple'] = function (seed, variant) {
    var ctx = pick([
      { tool: 'a box spanner', sense: 'clockwise' },
      { tool: 'a valve handwheel', sense: 'anticlockwise' },
      { tool: 'a tap wrench', sense: 'clockwise' },
      { tool: 'a steering handwheel', sense: 'anticlockwise' },
      { tool: 'a pipe wrench pair', sense: 'clockwise' },
      { tool: 'a capstan bar', sense: 'anticlockwise' }
    ], seed, 'couple.ctx', variant);
    var F = pick([300, 350, 400, 450, 500, 600], seed, 'couple.F', variant);
    var d = pick([200, 250, 280, 320, 350], seed, 'couple.d', variant);
    var off = pick([100, 150, 200], seed, 'couple.off', variant);

    var dm = d / 1000;
    var offm = off / 1000;
    var M = F * dm;
    var tool = esc(ctx.tool);
    var sense = esc(ctx.sense);

    return {
      tag: 'couple',
      prompt: tool + ' is turned by two equal and opposite ' + F + ' N forces whose parallel lines of action are ' + d +
        ' mm apart, giving a ' + sense + ' turning effect. Find the couple moment, and show that the answer is unchanged if moments are taken about a point ' + off +
        ' mm outside one line of action.',
      diagram: {
        type: 'couple',
        labels: [
          F + ' N (one way)',
          F + ' N (opposite way)',
          'd = ' + d + ' mm = ' + f(dm, 3) + ' m',
          'M = ? (' + sense + ')'
        ]
      },
      steps: [
        'The two forces are equal, parallel and opposite, so \\(\\Sigma F=0\\): the system has no resultant force and produces a pure couple.',
        'For a couple the moment is the force times the perpendicular separation: \\(M=Fd=' + F + '(' + f(dm, 3) + ')=' + f(M, 2) + '\\text{ N\u00B7m}\\), acting ' + sense + '.',
        'Take moments about a point on the first line of action. That force has zero lever arm, so only the second contributes: \\(M=' + F + '(' + f(dm, 3) + ')=' + f(M, 2) + '\\text{ N\u00B7m}\\).',
        'Now take moments about a point ' + off + ' mm beyond that line: the arms become \\(' + f(offm, 3) + '\\text{ m}\\) and \\(' + f(offm + dm, 3) + '\\text{ m}\\), and the senses oppose, giving \\(M=' + F + '(' + f(offm + dm, 3) + ')-' + F + '(' + f(offm, 3) + ')=' + f(M, 2) + '\\text{ N\u00B7m}\\).',
        'The reference point has cancelled out, confirming that a couple is a free vector: the same moment acts anywhere on the body.'
      ],
      final: '\\(M=' + f(M, 2) + '\\text{ N\u00B7m}\\) ' + sense + ', independent of the moment centre',
      check: 'Units are N\u00B7m. Both moment centres give identical values, as required for a couple, and the magnitude is of the order of a hand-applied torque on ' +
        tool + ' \u2014 hundreds of newtons on a lever arm of a few hundred millimetres.'
    };
  };

  /* --------------------------- 8. cantilever --------------------------- */
  /* Objective: fixed-end shear and moment of a cantilever with UDL plus tip load. */
  FAM['cantilever'] = function (seed, variant) {
    var lay = pick([
      { L: 2.0, w: 4, P: 6 },
      { L: 2.4, w: 3, P: 5 },
      { L: 3.0, w: 5, P: 8 },
      { L: 3.5, w: 4, P: 10 },
      { L: 4.0, w: 6, P: 12 },
      { L: 2.5, w: 8, P: 9 }
    ], seed, 'cant.lay', variant);
    var ctx = pick([
      'a steel cantilever balcony beam',
      'a cantilevered canopy beam',
      'a bolted cantilever bracket beam',
      'a cantilevered walkway beam',
      'a cantilever sign support beam',
      'a cantilevered plant-support beam'
    ], seed, 'cant.ctx', variant);

    var L = lay.L, w = lay.w, P = lay.P;
    var Wu = w * L;
    var V = Wu + P;
    var Mu = Wu * (L / 2);
    var Mp = P * L;
    var M = Mu + Mp;
    var beam = esc(ctx);

    return {
      tag: 'cantilever',
      prompt: beam + ' of length ' + f(L, 1) + ' m is built in at A and carries a uniformly distributed load of ' + w +
        ' kN/m over its whole length plus a ' + P +
        ' kN downward point load at the free end. Draw the free-body diagram and find the reaction force and fixing moment at A.',
      diagram: {
        type: 'beam',
        labels: [
          'A: fixed (V\u2090, M\u2090 = ?)',
          'UDL w = ' + w + ' kN/m',
          'P = ' + P + ' kN \u2193 at tip',
          'L = ' + f(L, 1) + ' m'
        ]
      },
      steps: [
        'A built-in end supplies both a vertical reaction and a fixing moment, so use \\(\\Sigma F_y=0\\) and \\(\\Sigma M_A=0\\).',
        'Replace the UDL by its resultant: \\(W_{udl}=wL=' + w + '(' + f(L, 1) + ')=' + f(Wu, 2) + '\\text{ kN}\\), acting at mid-length \\(L/2=' + f(L / 2, 2) + '\\text{ m}\\) from A.',
        'Vertical equilibrium: \\(V_A=W_{udl}+P=' + f(Wu, 2) + '+' + P + '=' + f(V, 2) + '\\text{ kN}\\) upward.',
        'Moments about A: the UDL resultant gives \\(' + f(Wu, 2) + '(' + f(L / 2, 2) + ')=' + f(Mu, 3) + '\\text{ kN\u00B7m}\\) and the tip load gives \\(' + P + '(' + f(L, 1) + ')=' + f(Mp, 3) + '\\text{ kN\u00B7m}\\), both turning the beam the same way.',
        'The fixing moment must balance their sum: \\(M_A=' + f(Mu, 3) + '+' + f(Mp, 3) + '=' + f(M, 3) + '\\text{ kN\u00B7m}\\), i.e. hogging over the support.'
      ],
      final: '\\(V_A=' + f(V, 2) + '\\text{ kN}\\) upward and \\(M_A=' + f(M, 2) + '\\text{ kN\u00B7m}\\) (hogging)',
      check: 'The reaction is a force in kN and the fixing moment is in kN\u00B7m \u2014 dimensionally distinct, as expected. \\(M_A\\) exceeds the tip-load moment \\(' +
        f(Mp, 2) + '\\text{ kN\u00B7m}\\) but is smaller than \\(V_AL=' + f(V * L, 2) +
        '\\text{ kN\u00B7m}\\), because the distributed load acts at mid-span rather than at the tip.'
    };
  };

  /* -------------------------- 9. components -------------------------- */
  /* Objective: resolve a single force into Cartesian components with correct signs. */
  FAM['components'] = function (seed, variant) {
    var ctx = pick([
      'a guy wire on a mast',
      'a hydraulic ram on a linkage',
      'a bracing strut at a node',
      'a tow rope on a stalled vehicle',
      'a jib stay on a hoist',
      'a tie rod on a signal gantry'
    ], seed, 'comp.ctx', variant);
    var F = pick([300, 400, 500, 600, 700, 800], seed, 'comp.F', variant);
    var th = pick([35, 55, 140, 215, 250, 310], seed, 'comp.th', variant);

    var Fx = F * cos(th);
    var Fy = F * sin(th);
    var mag = Math.sqrt(Fx * Fx + Fy * Fy);
    var src = esc(ctx);

    return {
      tag: 'components',
      prompt: 'A force of ' + F + ' N from ' + src + ' acts at ' + th +
        '\u00B0 measured anticlockwise from the positive x-axis. Sketch the vector and resolve it into its Cartesian components, stating the signs correctly.',
      diagram: {
        type: 'vector',
        labels: [
          '+x axis (datum)',
          '\u03B8 = ' + th + '\u00B0 anticlockwise',
          'F = ' + F + ' N',
          'F\u2093, F_y = ? (' + quadName(th) + ')'
        ]
      },
      steps: [
        'The angle is measured anticlockwise from \\(+x\\), so the standard projections apply directly: \\(F_x=F\\cos\\theta\\) and \\(F_y=F\\sin\\theta\\).',
        'The direction \\(\\theta=' + th + '^\\circ\\) places the vector in ' + quadName(th) + ', which fixes the expected signs before any arithmetic.',
        'x-component: \\(F_x=' + F + '\\cos' + th + '^\\circ=' + f(Fx, 2) + '\\text{ N}\\).',
        'y-component: \\(F_y=' + F + '\\sin' + th + '^\\circ=' + f(Fy, 2) + '\\text{ N}\\).',
        'Write the vector form: \\(\\mathbf F=(' + f(Fx, 2) + '\\,\\mathbf i' + (Fy < 0 ? '' : '+') + f(Fy, 2) + '\\,\\mathbf j)\\text{ N}\\).'
      ],
      final: '\\(F_x=' + f(Fx, 1) + '\\text{ N}\\), \\(F_y=' + f(Fy, 1) + '\\text{ N}\\)',
      check: 'Recombining gives \\(\\sqrt{(' + f(Fx, 2) + ')^2+(' + f(Fy, 2) + ')^2}=' + f(mag, 1) +
        '\\text{ N}\\), which returns the original ' + F +
        ' N magnitude, and each component is smaller in magnitude than the force itself \u2014 both necessary for a correct resolution. The signs agree with ' +
        quadName(th) + '.'
    };
  };

  /* --------------------------- 10. resultant --------------------------- */
  /* Objective: resultant of concurrent coplanar forces by components. */
  FAM['resultant'] = function (seed, variant) {
    var set = pick([
      { where: 'a gusset plate', v: [{ F: 300, t: 0 }, { F: 250, t: 120 }, { F: 180, t: 225 }] },
      { where: 'a lifting ring', v: [{ F: 400, t: 30 }, { F: 300, t: 150 }, { F: 200, t: 270 }] },
      { where: 'a bracket node', v: [{ F: 500, t: 20 }, { F: 350, t: 110 }, { F: 250, t: 200 }] },
      { where: 'a towing eye', v: [{ F: 600, t: 45 }, { F: 400, t: 135 }, { F: 300, t: 240 }] },
      { where: 'a mast fixing', v: [{ F: 250, t: 15 }, { F: 450, t: 100 }, { F: 350, t: 210 }] },
      { where: 'a pin connection', v: [{ F: 350, t: 60 }, { F: 500, t: 160 }, { F: 150, t: 300 }] }
    ], seed, 'res.set', variant);

    var v = set.v;
    var Rx = 0, Ry = 0, sumMag = 0, i;
    var xTerms = [], yTerms = [];
    for (i = 0; i < v.length; i++) {
      Rx += v[i].F * cos(v[i].t);
      Ry += v[i].F * sin(v[i].t);
      sumMag += v[i].F;
      xTerms.push(v[i].F + '\\cos' + v[i].t + '^\\circ');
      yTerms.push(v[i].F + '\\sin' + v[i].t + '^\\circ');
    }
    var R = Math.sqrt(Rx * Rx + Ry * Ry);
    var dir = dirDeg(Rx, Ry);
    var where = esc(set.where);
    var list = v.map(function (q) { return q.F + ' N at ' + q.t + '\u00B0'; }).join(', ');

    return {
      tag: 'resultant',
      prompt: 'Three concurrent coplanar forces act at ' + where + ': ' + list +
        ', all angles measured anticlockwise from the positive x-axis. Sketch the vectors and find the magnitude and direction of the resultant.',
      diagram: {
        type: 'vector',
        labels: [
          v[0].F + ' N at ' + v[0].t + '\u00B0',
          v[1].F + ' N at ' + v[1].t + '\u00B0',
          v[2].F + ' N at ' + v[2].t + '\u00B0',
          'R = ? at \u03B8 from +x'
        ]
      },
      steps: [
        'Because the forces are concurrent, add them by components rather than graphically: \\(R_x=\\Sigma F\\cos\\theta\\), \\(R_y=\\Sigma F\\sin\\theta\\).',
        'x-components: \\(R_x=' + xTerms.join('+') + '=' + f(Rx, 2) + '\\text{ N}\\).',
        'y-components: \\(R_y=' + yTerms.join('+') + '=' + f(Ry, 2) + '\\text{ N}\\).',
        'Magnitude: \\(R=\\sqrt{(' + f(Rx, 2) + ')^2+(' + f(Ry, 2) + ')^2}=' + f(R, 2) + '\\text{ N}\\).',
        'Direction: \\(\\theta=\\tan^{-1}\\!\\left(' + f(Ry, 2) + '/' + f(Rx, 2) + '\\right)\\), and since \\((R_x,R_y)\\) lies in ' + quadName(dir) + ' the correct bearing is \\(\\theta=' + f(dir, 2) + '^\\circ\\) from \\(+x\\).'
      ],
      final: '\\(R=' + f(R, 1) + '\\text{ N}\\) at \\(' + f(dir, 1) + '^\\circ\\) anticlockwise from \\(+x\\)',
      check: 'Units are N and the direction is an angle. The resultant \\(' + f(R, 1) +
        '\\text{ N}\\) is smaller than the arithmetic sum \\(' + sumMag +
        '\\text{ N}\\), as it must be when the forces are not parallel, and the quadrant of \\((R_x,R_y)\\) confirms the quoted angle rather than the raw calculator value.'
    };
  };

  /* -------------------------- 11. cable-joint -------------------------- */
  /* Objective: two-member joint equilibrium — inclined cable plus horizontal tie. */
  FAM['cable-joint'] = function (seed, variant) {
    var ctx = pick([
      { joint: 'a wall-mounted hoist bracket', load: 'a suspended motor' },
      { joint: 'a signage support node', load: 'a hanging sign' },
      { joint: 'a pipe-hanger joint', load: 'a filled pipe run' },
      { joint: 'a jib connection point', load: 'a lifted pallet' },
      { joint: 'a balcony tie node', load: 'a plant unit' },
      { joint: 'a davit head joint', load: 'a suspended cradle' }
    ], seed, 'joint.ctx', variant);
    var W = pick([6, 8, 10, 12, 15, 18], seed, 'joint.W', variant);
    var al = pick([30, 35, 40, 45, 50], seed, 'joint.al', variant);

    var T = W / sin(al);
    var H = T * cos(al);
    var joint = esc(ctx.joint);
    var load = esc(ctx.load);

    return {
      tag: 'cable-joint',
      prompt: 'At ' + joint + ', ' + load + ' applies a ' + W +
        ' kN vertical downward load. The joint is held by a cable running to the wall at ' + al +
        '\u00B0 above the horizontal and by a horizontal tie. Draw the joint free-body diagram and find the force in the cable and in the tie.',
      diagram: {
        type: 'joint',
        labels: [
          'load = ' + W + ' kN \u2193',
          'cable at ' + al + '\u00B0',
          'horizontal tie H = ?',
          'joint: \u03A3F\u2093 = \u03A3F_y = 0'
        ]
      },
      steps: [
        'Isolate the joint as a particle. Three forces act on it: the ' + W + ' kN load, the inclined cable force \\(T\\) and the horizontal tie force \\(H\\).',
        'Only the cable has a vertical component, so vertical equilibrium alone gives \\(T\\): \\(T\\sin' + al + '^\\circ=' + W + '\\).',
        'Solve: \\(T=' + W + '/\\sin' + al + '^\\circ=' + W + '/' + f(sin(al), 4) + '=' + f(T, 3) + '\\text{ kN}\\).',
        'Horizontal equilibrium balances the cable\u2019s horizontal pull against the tie: \\(H=T\\cos' + al + '^\\circ=' + f(T, 3) + '(' + f(cos(al), 4) + ')=' + f(H, 3) + '\\text{ kN}\\).',
        'Cross-check with the geometry shortcut \\(H=W/\\tan' + al + '^\\circ=' + W + '/' + f(tan(al), 4) + '=' + f(W / tan(al), 3) + '\\text{ kN}\\), which agrees.'
      ],
      final: 'Cable \\(T=' + f(T, 2) + '\\text{ kN}\\) (tension), horizontal tie \\(H=' + f(H, 2) + '\\text{ kN}\\)',
      check: 'Both are forces in kN. The cable force exceeds the ' + W +
        ' kN load because only its vertical component carries the load, and the tie force follows the geometry: a shallower cable angle would raise both values sharply, while a vertical cable would give \\(T=' +
        W + '\\text{ kN}\\) and \\(H=0\\).'
    };
  };

  /* -------------------------- 12. equilibrant -------------------------- */
  /* Objective: equilibrant of a force system in component, magnitude and direction form. */
  FAM['equilibrant'] = function (seed, variant) {
    var set = pick([
      { where: 'a ring bolt', a: [120, -50], b: [-40, 130] },
      { where: 'a pinned bracket', a: [200, 90], b: [-60, -150] },
      { where: 'a cable junction', a: [-80, 140], b: [180, -40] },
      { where: 'a towing bridle', a: [150, 160], b: [90, -60] },
      { where: 'a rigging shackle', a: [-110, -70], b: [-50, 190] },
      { where: 'a strut node', a: [240, -80], b: [-100, -40] }
    ], seed, 'eq.set', variant);

    var x1 = set.a[0], y1 = set.a[1], x2 = set.b[0], y2 = set.b[1];
    var Rx = x1 + x2, Ry = y1 + y2;
    var Ex = -Rx, Ey = -Ry;
    var Emag = Math.sqrt(Ex * Ex + Ey * Ey);
    var Edir = dirDeg(Ex, Ey);
    var where = esc(set.where);
    var sx = function (n) { return (n < 0 ? '' : '+') + n; };

    return {
      tag: 'equilibrant',
      prompt: 'Two forces act at ' + where + ': F\u2081 = (' + x1 + ', ' + y1 + ') N and F\u2082 = (' + x2 + ', ' + y2 +
        ') N. Find the single force (the equilibrant) that must be added to hold the point in equilibrium, giving it in component form and as a magnitude with a direction from the positive x-axis.',
      diagram: {
        type: 'vector',
        labels: [
          'F\u2081 = (' + x1 + ', ' + y1 + ') N',
          'F\u2082 = (' + x2 + ', ' + y2 + ') N',
          'R = (' + Rx + ', ' + Ry + ') N',
          'E = \u2212R = (' + Ex + ', ' + Ey + ') N'
        ]
      },
      steps: [
        'First combine the given forces by adding components: \\(R_x=' + x1 + sx(x2) + '=' + Rx + '\\text{ N}\\) and \\(R_y=' + y1 + sx(y2) + '=' + Ry + '\\text{ N}\\).',
        'Equilibrium of the point requires \\(\\Sigma F=0\\), so the extra force must be equal and opposite to the resultant: \\(\\mathbf E=-\\mathbf R=(' + Ex + ',' + Ey + ')\\text{ N}\\).',
        'Magnitude: \\(|\\mathbf E|=\\sqrt{(' + Ex + ')^2+(' + Ey + ')^2}=\\sqrt{' + (Ex * Ex + Ey * Ey) + '}=' + f(Emag, 2) + '\\text{ N}\\).',
        'Direction: \\((' + Ex + ',' + Ey + ')\\) lies in ' + quadName(Edir) + ', so measuring anticlockwise from \\(+x\\) gives \\(\\theta=' + f(Edir, 2) + '^\\circ\\).',
        'The resultant \\(\\mathbf R\\) has the same magnitude \\(' + f(Emag, 2) + '\\text{ N}\\) but points at \\(' + f((Edir + 180) % 360, 2) + '^\\circ\\), exactly opposite the equilibrant.'
      ],
      final: '\\(\\mathbf E=(' + Ex + ',' + Ey + ')\\text{ N}=' + f(Emag, 1) + '\\text{ N at }' + f(Edir, 1) + '^\\circ\\)',
      check: 'Components are in N. Adding all three forces returns \\((' + x1 + sx(x2) + sx(Ex) + ',' + y1 + sx(y2) + sx(Ey) +
        ')=(0,0)\\text{ N}\\), so equilibrium is genuinely satisfied, and the equilibrant is the resultant reversed \u2014 same magnitude, direction turned through \\(180^\\circ\\).'
    };
  };
}());
