(() => {
  "use strict";

  const NS = "http://www.w3.org/2000/svg";
  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined) node.textContent = String(text);
    return node;
  };
  const svgEl = (tag, attrs = {}) => {
    const node = document.createElementNS(NS, tag);
    Object.entries(attrs).forEach(([key, value]) => node.setAttribute(key, String(value)));
    return node;
  };

  function seedFor(week, index) {
    let h = 2166136261;
    `${week}:${index}:DPEN102`.split("").forEach((char) => {
      h ^= char.charCodeAt(0);
      h = Math.imul(h, 16777619);
    });
    return h >>> 0;
  }

  function diagram(type = "system", labels = []) {
    const wrap = el("div", "diagram-wrap");
    const title = labels.length ? labels.join(", ") : `${type} mechanics diagram`;
    const svg = svgEl("svg", {
      viewBox: "0 0 420 210", role: "img",
      "aria-label": `${type} diagram labelled ${title}`,
      focusable: "false", class: "mechanics-diagram"
    });
    const defs = svgEl("defs");
    const marker = svgEl("marker", { id: `arrow-${Math.random().toString(36).slice(2)}`, viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 7, markerHeight: 7, orient: "auto-start-reverse" });
    marker.append(svgEl("path", { d: "M 0 0 L 10 5 L 0 10 z", fill: "currentColor" }));
    defs.append(marker);
    svg.append(defs);
    const arrow = marker.id;
    const line = (x1, y1, x2, y2, cls = "diagram-line") => svg.append(svgEl("line", { x1, y1, x2, y2, class: cls, "marker-end": cls.includes("arrow") ? `url(#${arrow})` : "" }));
    const path = (d, cls = "diagram-line") => svg.append(svgEl("path", { d, class: cls, fill: "none", "marker-end": cls.includes("arrow") ? `url(#${arrow})` : "" }));
    const rect = (x, y, width, height, cls = "diagram-body") => svg.append(svgEl("rect", { x, y, width, height, rx: 4, class: cls }));
    const circle = (cx, cy, r, cls = "diagram-body") => svg.append(svgEl("circle", { cx, cy, r, class: cls }));

    const drawBeam = () => {
      line(55, 110, 365, 110, "diagram-line heavy");
      path("M80 110 L65 140 L95 140 Z");
      circle(335, 128, 10);
      line(320, 140, 350, 140);
    };
    const drawBody = () => {
      rect(165, 80, 90, 60);
      line(210, 80, 210, 30, "diagram-line arrow");
      line(210, 140, 210, 190, "diagram-line arrow");
      line(165, 110, 95, 110, "diagram-line arrow");
      line(255, 110, 325, 70, "diagram-line arrow");
    };

    switch (type) {
      case "beam": case "sfd": case "cut":
        drawBeam();
        if (type === "cut") line(210, 70, 210, 155, "diagram-line dashed");
        if (type === "sfd") path("M65 175 L130 140 L250 165 L350 120", "diagram-accent");
        break;
      case "cantilever":
        line(60, 45, 60, 170, "diagram-line heavy"); line(60, 105, 350, 105, "diagram-line heavy");
        for (let y = 50; y < 170; y += 18) line(40, y + 10, 60, y);
        line(330, 40, 330, 103, "diagram-line arrow");
        break;
      case "vector": case "components": case "resultant": case "equilibrant":
        line(80, 165, 340, 165); line(80, 165, 80, 35);
        line(80, 165, 320, 55, "diagram-line arrow");
        line(80, 165, 320, 165, "diagram-accent arrow");
        line(320, 165, 320, 55, "diagram-accent arrow");
        break;
      case "section": case "area":
        rect(120, 35, 180, 140);
        if (type === "section") { rect(155, 65, 110, 80, "diagram-hole"); line(90, 105, 330, 105, "diagram-line dashed"); }
        else { line(210, 25, 210, 185, "diagram-line dashed"); line(100, 105, 320, 105, "diagram-line dashed"); }
        break;
      case "truss": case "joint":
        line(70, 160, 210, 45, "diagram-line heavy"); line(210, 45, 350, 160, "diagram-line heavy"); line(70, 160, 350, 160, "diagram-line heavy");
        [ [70,160], [210,45], [350,160] ].forEach(([x,y]) => circle(x,y,6,"diagram-joint"));
        if (type === "joint") { line(210, 45, 210, 15, "diagram-line arrow"); line(210, 45, 165, 82, "diagram-line arrow"); }
        break;
      case "incline":
        path("M55 170 L360 170 L360 50 Z"); rect(215, 97, 66, 45); line(248, 98, 290, 55, "diagram-line arrow");
        break;
      case "belt":
        circle(125, 105, 52); circle(295, 105, 52); path("M125 53 L295 53 M125 157 L295 157", "diagram-line heavy");
        break;
      case "energy":
        rect(55, 125, 55, 40); path("M110 145 C125 115 140 175 155 145 C170 115 185 175 200 145 C215 115 230 175 245 145", "diagram-accent");
        line(245,145,350,145,"diagram-line arrow");
        break;
      case "couple":
        circle(210,105,55); path("M160 85 A55 55 0 0 1 252 72","diagram-line arrow"); path("M260 125 A55 55 0 0 1 168 138","diagram-line arrow");
        break;
      case "fbd": case "system": default:
        drawBody();
    }
    labels.slice(0, 6).forEach((label, index) => {
      const t = svgEl("text", { x: 24 + (index % 3) * 142, y: index < 3 ? 22 : 202, class: "diagram-label" });
      t.textContent = String(label);
      svg.append(t);
    });
    wrap.append(svg);
    return wrap;
  }

  function assertAnswer(answer) {
    const checks = [
      [answer.querySelector("svg"), "SVG diagram"],
      [answer.querySelector(".steps"), "worked steps"],
      [answer.querySelector(".final"), "final answer"],
      [answer.querySelector(".check"), "check"]
    ];
    checks.forEach(([value, label]) => {
      console.assert(Boolean(value), `Every answer requires ${label}.`);
      if (!value) throw new Error(`Invalid family output: missing ${label}.`);
    });
  }

  function renderCard({ familyId, seed, variant, number, showAnswer }) {
    const factory = window.DPEN102_FAMILIES && window.DPEN102_FAMILIES[familyId];
    if (typeof factory !== "function") throw new Error(`Question family “${familyId}” is not loaded.`);
    const item = factory(seed, variant);
    const article = el("article", "question-card");
    const heading = el("div", "question-heading");
    heading.append(el("span", "question-number", `Q${number}`), el("span", "question-tag", item.tag || familyId));
    article.append(heading, el("p", "prompt", item.prompt));

    if (showAnswer) {
      const details = el("details", "worked-answer");
      const summary = el("summary", "", "Show fully worked answer");
      const answer = el("div", "answer-body");
      answer.append(diagram(item.diagram?.type, item.diagram?.labels || []));
      const steps = el("ol", "steps");
      (item.steps || []).forEach((step) => steps.append(el("li", "", step)));
      answer.append(steps, el("p", "final", item.final), el("p", "check", `Check: ${item.check}`));
      details.append(summary, answer);
      article.append(details);
      assertAnswer(answer);
    }
    return article;
  }

  function typeset(container) {
    if (window.MathJax?.typesetPromise) window.MathJax.typesetPromise([container]).catch(console.error);
  }

  window.DPEN102_CORE = Object.freeze({ el, seedFor, diagram, renderCard, typeset });
})();
