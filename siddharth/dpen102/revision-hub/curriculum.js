(() => {
  "use strict";

  const F = {
    dynamics: ["dynamics", "equilibrium", "inclined-pull", "connected", "moments", "beam-reactions", "couple", "cantilever", "components", "resultant", "cable-joint", "equilibrant"],
    structures: ["axial-stress", "strain", "allowable", "internal-cut", "beam-point", "beam-udl", "beam-mixed", "cantilever-sfd", "truss-triangle", "zero-force", "truss-joint", "truss-section"],
    applied: ["static-incline", "kinetic-incline", "level-friction", "belt", "centroid", "centroid-hole", "rectangle-I", "composite-I", "work-force", "fall", "spring", "friction-energy"]
  };

  const week = (number, title, phase, focus, families) =>
    Object.freeze({ number, title, phase, focus, families: Object.freeze(families) });

  window.DPEN102_CURRICULUM = Object.freeze([
    week(1, "Forces & Motion", "Foundations", "Newton’s laws, free-body diagrams and equilibrium", F.dynamics),
    week(2, "Components & Resultants", "Foundations", "Resolve forces and close equilibrium systems", ["components","resultant","equilibrium","equilibrant","dynamics","inclined-pull","connected","moments","beam-reactions","cable-joint","couple","cantilever"]),
    week(3, "Moments & Supports", "Foundations", "Moments, couples and reaction models", ["moments","couple","beam-reactions","cantilever","equilibrium","components","resultant","cable-joint","equilibrant","dynamics","inclined-pull","connected"]),
    week(4, "Stress, Strain & Cuts", "Structures", "Axial response and internal actions", F.structures),
    week(5, "Loaded Beams", "Structures", "Point, distributed and mixed beam loading", ["beam-point","beam-udl","beam-mixed","cantilever-sfd","internal-cut","beam-reactions","cantilever","moments","couple","equilibrium","components","resultant"]),
    week(6, "Truss Analysis", "Structures", "Zero-force members, joints and sections", ["truss-triangle","zero-force","truss-joint","truss-section","equilibrium","components","resultant","moments","cable-joint","axial-stress","internal-cut","allowable"]),
    week(7, "Friction Systems", "Applied", "Static, kinetic, level and belt friction", ["static-incline","kinetic-incline","level-friction","belt","inclined-pull","connected","equilibrium","components","resultant","work-force","friction-energy","spring"]),
    week(8, "Centroids & Inertia", "Applied", "Area centroids and second moments of area", ["centroid","centroid-hole","rectangle-I","composite-I","components","resultant","moments","beam-reactions","axial-stress","strain","beam-mixed","internal-cut"]),
    week(9, "Work & Energy", "Applied", "Work, falling bodies, springs and friction losses", ["work-force","fall","spring","friction-energy","dynamics","connected","kinetic-incline","level-friction","static-incline","components","resultant","equilibrium"]),
    week(10, "Targeted Energy Synthesis", "Applied", "Integrate statics, friction and energy", F.applied),
    week(11, "Statics + Materials", "Combined", "Foundations with stress and strain", ["equilibrium","moments","beam-reactions","components","resultant","cable-joint","axial-stress","strain","allowable","internal-cut","beam-point","beam-udl"]),
    week(12, "Beams + Trusses", "Combined", "Structural analysis across major sections", F.structures),
    week(13, "Statics + Applied Mechanics", "Combined", "Forces, friction, geometry and work", ["dynamics","equilibrium","inclined-pull","connected","moments","components","static-incline","kinetic-incline","level-friction","belt","centroid","work-force"]),
    week(14, "Structures + Energy", "Combined", "Loaded structures and energy methods", ["axial-stress","internal-cut","beam-mixed","cantilever-sfd","truss-joint","truss-section","centroid-hole","composite-I","work-force","fall","spring","friction-energy"]),
    week(15, "Full Syllabus I", "Full syllabus", "Balanced recall across every major section", ["dynamics","moments","beam-reactions","resultant","axial-stress","beam-point","truss-joint","static-incline","centroid","rectangle-I","work-force","spring"]),
    week(16, "Full Syllabus II", "Full syllabus", "Broaden methods and improve selection", ["equilibrium","inclined-pull","couple","cable-joint","strain","beam-udl","truss-section","kinetic-incline","centroid-hole","composite-I","fall","friction-energy"]),
    week(17, "Full Syllabus III", "Full syllabus", "Multi-step reasoning under time pressure", ["connected","cantilever","components","equilibrant","allowable","beam-mixed","zero-force","level-friction","belt","centroid","work-force","friction-energy"]),
    week(18, "Full Syllabus IV", "Full syllabus", "Exam-level method switching and checking", ["dynamics","beam-reactions","moments","resultant","internal-cut","cantilever-sfd","truss-triangle","truss-joint","static-incline","rectangle-I","fall","spring"]),
    week(19, "Mock Mix I", "Mock", "Complete a balanced full-syllabus rehearsal", ["equilibrium","inclined-pull","couple","cable-joint","axial-stress","beam-mixed","truss-section","belt","centroid-hole","composite-I","work-force","friction-energy"]),
    week(20, "Mock Mix II", "Mock", "Final mixed rehearsal and error-proofing", ["connected","moments","cantilever","components","allowable","internal-cut","beam-udl","zero-force","kinetic-incline","centroid","fall","spring"])
  ]);

  const allowed = new Set([...F.dynamics, ...F.structures, ...F.applied]);
  console.assert(window.DPEN102_CURRICULUM.length === 20, "Curriculum must contain 20 weeks.");
  window.DPEN102_CURRICULUM.forEach((w) => {
    console.assert(w.families.length === 12, `Week ${w.number} must contain 12 families.`);
    console.assert(w.families.every((id) => allowed.has(id)), `Week ${w.number} contains an unknown family.`);
  });
})();
