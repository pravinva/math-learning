# -*- coding: utf-8 -*-
"""Generate DPEN102 Weeks 1-6 cumulative revision Set B."""
import re
from pathlib import Path

from _dpen102_kit import (
    BLUE, GREEN, NAVY, ORANGE, RED, S, arr, bar_axial, beam_fig,
    bending_section, checklist, circ, cut_segment, fbd_level, flow_steps,
    joint_fig, ln, member_sign, moment_fig, rect, resolve_fig, section_circle,
    stress_bars, t, truss_joint, truss_triangle, unit_ladder, vector_fig,
    vm_diagram,
)
from _rev_common import details, mathsafe


ROOT = Path(__file__).parent
BASE = ROOT / "siddharth" / "dpen102"
SOURCE = BASE / "Revision_W1_W6_Cumulative_24Q.html"
TARGET = BASE / "Revision_W1_W6_Cumulative_24Q_SET_B.html"
TAG = '<span class="tag">%s</span>'


def q(n, week, text):
    return "Q%d %s %s" % (n, TAG % week, text)


def prompt_wrap(svg, caption):
    return ('      <div class="question-diagram"><div class="prompt-label">Given diagram</div>'
            + svg + '<p class="prompt-caption">' + caption + "</p></div>")


def render(spec):
    block = details(spec["summary"], spec)
    if spec.get("prompt_svg"):
        block = block.replace(
            "\n      <div class=\"ans\">",
            "\n" + prompt_wrap(spec["prompt_svg"], spec["prompt_caption"])
            + "\n      <div class=\"ans\">",
            1,
        )
    return block


def load_arrow_diagram():
    body = [
        t(270, 18, "three concurrent forces at O", 12, NAVY, weight="bold"),
        ln(50, 126, 490, 126, "#8b96a6", 1.4),
        ln(270, 38, 270, 218, "#8b96a6", 1.4),
        circ(270, 126, 6, "#cbd6e6", NAVY, 1.6),
        t(280, 144, "O", 11, NAVY, anchor="start", weight="bold"),
        arr(270, 126, 402, 126, BLUE, 2.6), t(408, 120, "80 N", 11, BLUE, anchor="start", weight="bold"),
        arr(270, 126, 214, 35, GREEN, 2.6), t(206, 48, "65 N at 120&#176;", 11, GREEN, anchor="end", weight="bold"),
        arr(270, 126, 226, 202, ORANGE, 2.6), t(218, 216, "50 N at 240&#176;", 11, ORANGE, anchor="end", weight="bold"),
    ]
    return S(540, 236, "".join(body))


def couple_diagram():
    body = [
        ln(70, 122, 480, 122, NAVY, 4), circ(70, 122, 7, "#cbd6e6", NAVY, 1.8),
        t(54, 128, "O", 12, NAVY, anchor="end", weight="bold"),
        arr(250, 54, 250, 116, RED, 2.5), t(250, 44, "600 N", 12, RED, weight="bold"),
        arr(390, 190, 390, 128, GREEN, 2.5), t(390, 210, "350 N", 12, GREEN, weight="bold"),
        ln(70, 166, 250, 166, "#5b6779", 1.2), t(160, 184, "450 mm", 11, "#5b6779"),
        ln(70, 224, 390, 224, "#5b6779", 1.2), t(230, 242, "0.800 m", 11, "#5b6779"),
    ]
    return S(540, 258, "".join(body))


BEAM_PROMPT = beam_fig(
    9, loads=[(3, "18 kN")], udl=("4 kN/m", 5, 9),
    dims_=[(0, 3, "3 m"), (3, 5, "2 m"), (5, 9, "4 m")],
    note="A is a pin; B is a roller. Reaction values are deliberately not shown.",
)

def truss_force_prompt():
    """Unsolved joint data with labels kept clear of members and load arrow."""
    cx, cy = 270, 144
    body = [
        ln(cx, cy, 86, cy, NAVY, 3),
        t(142, cy - 12, "member H", 11, NAVY, weight="bold"),
        ln(cx, cy, 178, 86, NAVY, 3),
        t(166, 72, "member D (120&#176;)", 11, NAVY, weight="bold"),
        arr(198, 48, cx, cy, RED, 2.6),
        t(190, 35, "20 kN", 12, RED, weight="bold"),
        t(190, 51, "(12 right, 16 down)", 10, RED, weight="bold"),
        circ(cx, cy, 8, "#cbd6e6", NAVY, 2),
        t(cx, cy + 25, "joint J", 10, "#5b6779"),
        t(270, 226, "Assume both unknown member forces act in tension.", 11, "#5b6779"),
    ]
    return S(540, 240, "".join(body))


TRUSS_FORCE_PROMPT = truss_force_prompt()


SPECS = [
    dict(summary=q(1, "W1", "A 1200 kg lift accelerates upward at 0.80 m/s&#178;. Draw its FBD, then determine the cable tension and explain why it exceeds the weight."),
         label="FBD &mdash; accelerating lift",
         svg=fbd_level("1200 kg lift", "W = 11.76 kN", "T = 12.72 kN",
                       moving="upward acceleration 0.80 m/s&#178;",
                       caption="T &#8722; W = ma; g = 9.8 m/s&#178;"),
         convention="+y upward.", steps=[
             r"\(W=mg=1200(9.8)=11760\text{ N}\).",
             r"\(\Sigma F_y=ma:\ T-11760=1200(0.80)\).",
             r"\(T=12720\text{ N}=12.72\text{ kN}\); it exceeds \(W\) because a positive upward resultant is required."],
         final=r"Answer: \(T=12.72\text{ kN}\) upward"),

    dict(summary=q(2, "W1", "A 25 kg trolley is pushed right by 110 N against 40 N resistance. A student says it moves at constant speed. Draw the FBD, diagnose the claim, and find the actual acceleration."),
         label="FBD &mdash; equilibrium claim under audit",
         svg=fbd_level("25 kg", "W = 245 N", "N = 245 N", push=("110 N", 0),
                       friction="40 N resistance", moving="net horizontal force = 70 N right",
                       caption="a constant-speed claim requires &#8721;F = 0"),
         convention="+x right; +y upward.", steps=[
             r"Vertical forces close: \(N-W=0\).",
             r"Horizontal resultant \(=110-40=70\text{ N}\), not zero.",
             r"\(a=70/25=2.80\text{ m/s}^2\) right, so constant speed is impossible under the stated forces."],
         final=r"Answer: claim rejected; \(a=2.80\text{ m/s}^2\) right"),

    dict(summary=q(3, "W2", "The bracket shown has forces at 450 mm and 0.800 m from O. Redraw the moment diagram, convert units consistently, and find the signed net moment about O."),
         label="Moment audit &mdash; competing rotations",
         svg=couple_diagram(), prompt_svg=couple_diagram(),
         prompt_caption="The 600 N force acts downward; the 350 N force acts upward.",
         convention="Anticlockwise positive.", steps=[
             r"\(450\text{ mm}=0.450\text{ m}\).",
             r"\(M_O=-600(0.450)+350(0.800)=-270+280\).",
             r"\(M_O=+10.0\text{ N·m}\), a small anticlockwise remainder; the near-cancellation is a useful reasonableness check."],
         final=r"Answer: \(M_O=+10.0\text{ N·m}\) (anticlockwise)"),

    dict(summary=q(4, "W2", r"A 500 N force acts at 35&#176; to a 0.60 m handle. Draw the perpendicular-component sketch, find the moment about the pivot, and diagnose the error in using \(500(0.60)\)."),
         label="Moment diagram &mdash; only the perpendicular component turns",
         svg=resolve_fig("500 N", 35, "F parallel = 409.58 N", "F perp = 286.79 N",
                         note="the perpendicular component alone creates the moment"),
         convention="Anticlockwise positive.", steps=[
             r"\(F_\perp=500\sin35^\circ=286.79\text{ N}\).",
             r"\(M_O=F_\perp L=286.79(0.60)=172.07\text{ N·m}\).",
             r"\(500(0.60)\) wrongly treats the whole force as perpendicular to the handle."],
         final=r"Answer: \(M_O=172.07\text{ N·m}\); using \(FL\) directly overstates it"),

    dict(summary=q(5, "W3", "Three concurrent forces are shown. Sketch their component table and resultant on axes, then find the resultant magnitude and direction from +x."),
         label="Vector polygon &mdash; resultant of three forces",
         svg=vector_fig([(80, 0, "80 N", BLUE), (-32.5, 56.29, "65 N", GREEN),
                         (-25, -43.30, "50 N", ORANGE)],
                        resultant=(22.5, 12.99, "R"), scale=1.6,
                        note="components add to R = (22.50, 12.99) N"),
         prompt_svg=load_arrow_diagram(), prompt_caption="Angles are measured anticlockwise from +x.",
         convention="Resolve into signed x- and y-components first.", steps=[
             r"\(R_x=80+65\cos120^\circ+50\cos240^\circ=22.50\text{ N}\).",
             r"\(R_y=65\sin120^\circ+50\sin240^\circ=12.99\text{ N}\).",
             r"\(|R|=\sqrt{22.50^2+12.99^2}=25.98\text{ N}\), \(\theta=\tan^{-1}(12.99/22.50)=30.00^\circ\)."],
         final=r"Answer: \(R=25.98\text{ N}\) at \(30.00^\circ\) from +x"),

    dict(summary=q(6, "W3", r'Two forces are \((35,-20)\) N and \((-12,44)\) N. Draw the force and equilibrant vectors, then find the equilibrant in component, magnitude, and direction form.'),
         label="Vector equilibrium &mdash; resultant and opposite equilibrant",
         svg=vector_fig([(35, -20, "F1", BLUE), (-12, 44, "F2", GREEN)],
                        resultant=(23, 24, "R = (23,24) N"), scale=2.6,
                        note="equilibrant E has the same length as R and points exactly opposite"),
         convention="Direction measured anticlockwise from +x.", steps=[
             r"\(R=(35-12,\,-20+44)=(23,24)\text{ N}\).",
             r"\(E=-R=(-23,-24)\text{ N}\).",
             r"\(|E|=\sqrt{23^2+24^2}=33.24\text{ N}\); \(\theta_E=180^\circ+\tan^{-1}(24/23)=226.22^\circ\)."],
         final=r"Answer: \(E=(-23,-24)\text{ N}=33.24\text{ N at }226.22^\circ\)"),

    dict(summary=q(7, "W4", "A stepped tie carries 54 kN tension through areas 450 mm&#178; and 300 mm&#178;. Sketch both cut sections, calculate both stresses, and decide whether each passes for yield 320 MPa with FoS 2.0."),
         label="Stepped axial tie &mdash; the smaller area governs",
         svg=(bar_axial("54 kN", "stepped areas: 450 then 300 mm&#178;",
                        note="draw a cut through each segment; the same axial force crosses both")
              + stress_bars([("450 mm&#178;", 120, GREEN), ("300 mm&#178;", 180, RED)],
                            allow=("allowable = 160 MPa", 160),
                            verdict="large segment passes; small segment FAILS")),
         convention="Tension positive; use N and mm so stress is in MPa.", steps=[
             r"\(\sigma_{allow}=320/2=160\text{ MPa}\).",
             r"\(\sigma_1=54000/450=120\text{ MPa}<160\text{ MPa}\): pass.",
             r"\(\sigma_2=54000/300=180\text{ MPa}>160\text{ MPa}\): fail. A single failed segment means the tie fails."],
         final="Answer: 450 mm&#178; segment passes; 300 mm&#178; segment fails"),

    dict(summary=q(8, "W4", r"A 1.80 m steel bar, area 500 mm&#178;, carries 40 kN tension; \(E=200\) GPa. Draw the elongation sketch, calculate extension, and diagnose a reported answer of 720 mm."),
         label="Axial deformation &mdash; consistent N-mm-MPa units",
         svg=bar_axial("40 kN", "A = 500 mm&#178;", L="L = 1800 mm", dL="&#916;L = 0.72 mm",
                       note="E = 200 000 N/mm&#178;"),
         convention=r"Convert \(L\) to mm and \(E\) to N/mm&#178;.", steps=[
             r"\(\Delta L=FL/(AE)\).",
             r"\(\Delta L=40000(1800)/[500(200000)]=0.720\text{ mm}\).",
             r"The 720 mm report is \(1000\times\) too large: metres and millimetres were mixed."],
         final=r"Answer: \(\Delta L=0.720\text{ mm}\); 720 mm is a unit error"),

    dict(summary=q(9, "W5", "A 7 m simply supported beam carries 10 kN at 2 m and 18 kN at 5 m from A. Draw the loaded beam and SFD, find reactions, and verify shear closes to zero."),
         label="Loaded beam and SFD &mdash; two point-load steps",
         svg=(beam_fig(7, loads=[(2, "10 kN"), (5, "18 kN")],
                       ra="R_A = 12.286 kN", rb="R_B = 15.714 kN",
                       dims_=[(0, 2, "2 m"), (2, 5, "3 m"), (5, 7, "2 m")])
              + vm_diagram([(0, 12.286), (2/7, 12.286), (2/7, 2.286),
                            (5/7, 2.286), (5/7, -15.714), (1, -15.714), (1, 0)],
                           title="shear force V (kN)", color=BLUE,
                           labels=[(0, 12.286, "+12.286"), (2/7, 2.286, "+2.286"),
                                   (5/7, -15.714, "&#8722;15.714"), (1, 0, "0")],
                           xlabels=[(0, "A"), (2/7, "2 m"), (5/7, "5 m"), (1, "B")])),
         convention="Upward forces produce positive shear on the global sweep.", steps=[
             r"\(R_B(7)=10(2)+18(5)=110\Rightarrow R_B=15.714\text{ kN}\).",
             r"\(R_A=28-15.714=12.286\text{ kN}\).",
             r"SFD levels: \(+12.286\), then \(+2.286\), then \(-15.714\), then \(0\) after \(R_B\). Closure confirms \(\Sigma F_y=0\)."],
         final=r"Answer: \(R_A=12.286\text{ kN}\), \(R_B=15.714\text{ kN}\); SFD closes at zero"),

    dict(summary=q(10, "W5", r"An 8 m simply supported beam carries a full 3 kN/m UDL plus 12 kN at \(x=2\) m. Draw the loaded beam and SFD/BMD logic, locate \(V=0\), and find the maximum moment."),
         label="BMD &mdash; maximum found from zero shear",
         svg=(beam_fig(8, loads=[(2, "12 kN")], udl=("3 kN/m", 0, 8),
                       ra="R_A = 21 kN", rb="R_B = 15 kN",
                       dims_=[(0, 2, "2 m"), (2, 8, "6 m")])
              + vm_diagram([(0, 21), (0.25, 15), (0.25, 3), (0.375, 0), (1, -15), (1, 0)],
                           title="shear force V (kN)", color=BLUE,
                           labels=[(0, 21, "+21"), (0.25, 3, "+3"),
                                   (0.375, 0, "V = 0"), (1, -15, "&#8722;15")],
                           xlabels=[(0, "A"), (0.25, "2 m"), (0.375, "3 m"), (1, "B")])
              + vm_diagram([(0, 0), (0.25, 36), (0.375, 37.5), (1, 0)],
                           title="bending moment M (kN&#183;m), schematic piecewise parabola",
                           color=RED, fill="#f7e2de",
                           labels=[(0.375, 37.5, "M max = 37.5")],
                           xlabels=[(0, "A"), (0.25, "2 m load"), (0.375, "V=0 at 3 m"), (1, "B")])),
         convention="Sagging moment positive.", steps=[
             r"UDL resultant \(=3(8)=24\text{ kN}\) at 4 m. \(R_B(8)=24(4)+12(2)\), so \(R_B=15\text{ kN}\), \(R_A=21\text{ kN}\).",
             r"For \(x>2\): \(V=21-12-3x=9-3x\). Thus \(V=0\) at \(x=3.00\text{ m}\).",
             r"\(M(3)=21(3)-12(3-2)-3(3^2)/2=37.50\text{ kN·m}\)."],
         final=r"Answer: \(M_{\max}=37.50\text{ kN·m}\) at \(x=3.00\text{ m}\)"),

    dict(summary=q(11, "W6", "At an unloaded joint, two members are collinear and a third is diagonal. Draw the joint FBD and identify the zero-force member, explaining why the two collinear members need not be zero."),
         label="Joint FBD &mdash; zero-force member pattern",
         svg=truss_joint([(0, "collinear 1"), (180, "collinear 2"), (55, "diagonal = 0")],
                         zero=(2,), note="only the non-collinear member must vanish"),
         convention="Resolve perpendicular to the collinear pair.", steps=[
             r"Only the diagonal has a component perpendicular to the horizontal pair, so equilibrium requires \(F_d=0\).",
             "The two collinear forces can be equal and opposite, so neither is forced to zero.",
             "This conclusion depends on the joint having no external load or support reaction."],
         final="Answer: the diagonal is the zero-force member"),

    dict(summary=q(12, "W6", "A symmetric triangular truss spans 6 m, rises 2 m, and carries 18 kN downward at the apex. Draw the truss and apex/left-joint FBDs, then find each rafter force and the bottom-tie force."),
         label="Triangular truss &mdash; reactions, rafters and tie",
         svg=truss_triangle("6 m", "2 m", "18 kN", "R_A = 9 kN", "R_B = 9 kN",
                           rafter="16.225 kN C", tie="13.50 kN T",
                           height=290,
                           note="symmetry gives equal reactions and equal rafter forces"),
         convention="Assume member tension; negative results are compression.", steps=[
             "At the unloaded bottom-centre joint, the two bottom-chord members are collinear, so the vertical king-post member is zero-force.",
             r"\(\sin\theta=2/\sqrt{3^2+2^2}=2/\sqrt{13}\). At the apex, \(2F\sin\theta=18\), giving \(F=16.225\text{ kN}\) compression.",
             r"At the left support, the rafter horizontal component is \(16.225(3/\sqrt{13})=13.50\text{ kN}\).",
             r"The bottom tie balances it in tension: \(F_{tie}=13.50\text{ kN}\)."],
         final="Answer: each rafter 16.225 kN compression; bottom tie 13.50 kN tension"),

    dict(summary=q(13, "Beam chain 1/4", "For the beam shown, draw the global FBD, replace the partial UDL by its resultant, and determine both support reactions."),
         label="Beam chain &mdash; global reactions",
         svg=beam_fig(9, loads=[(3, "18 kN")], udl=("4 kN/m", 5, 9),
                      ra="R_A = 15.556 kN", rb="R_B = 18.444 kN",
                      dims_=[(0, 3, "3 m"), (3, 5, "2 m"), (5, 9, "4 m")]),
         prompt_svg=BEAM_PROMPT, prompt_caption="Use the dimensions and loads shown; solve reactions before opening the answer.",
         convention="Up positive; moments about A anticlockwise positive.", steps=[
             r"The UDL becomes \(16\text{ kN}\) at \(x=7\text{ m}\).",
             r"\(R_B(9)=18(3)+16(7)=166\Rightarrow R_B=18.444\text{ kN}\).",
             r"\(R_A=34-18.444=15.556\text{ kN}\). Check: reactions sum to \(34\text{ kN}\)."],
         final=r"Answer: \(R_A=15.556\text{ kN}\), \(R_B=18.444\text{ kN}\)"),

    dict(summary=q(14, "Beam chain 2/4", r"Using Q13, draw the left cut segment at \(x=6\) m and find the signed shear and bending moment there."),
         label="Beam chain &mdash; cut at x = 6 m",
         svg=cut_segment(reactions=[(0, "R_A = 15.556 kN")], loads=[(0.5, "18 kN")],
                         cut_x=0.78, N="N = 0", V="V = &#8722;6.444 kN",
                         M="M = 37.333 kN&#183;m", udl_label="4 kN/m over final 1 m",
                         dims_=[(0, 0.5, "3 m"), (0.5, 1, "3 m")]),
         convention="Positive shear is upward on the left cut face; sagging moment positive.", steps=[
             r"Left of the cut, the UDL covers only \(1\text{ m}\), so its resultant is \(4\text{ kN}\) at \(x=5.5\text{ m}\).",
             r"\(V=15.556-18-4=-6.444\text{ kN}\).",
             r"\(M=15.556(6)-18(3)-4(0.5)=37.333\text{ kN·m}\)."],
         final=r"Answer: \(V(6)=-6.444\text{ kN}\), \(M(6)=37.333\text{ kN·m}\)"),

    dict(summary=q(15, "Beam chain 3/4", r"At the Q14 cut, \(I=32\times10^6\) mm&#8308; and \(c=90\) mm. Sketch the section and linear stress distribution, then calculate the extreme-fibre bending stress."),
         label="Beam chain &mdash; bending stress at the cut",
         svg=bending_section("section width", "2c = 180 mm", "c = 90 mm",
                             "M = 37.333 kN&#183;m", "I = 32 &#215; 10&#8310; mm&#8308;"),
         convention="Convert kN&#183;m to N&#183;mm; use the stress magnitude.", steps=[
             r"\(M=37.333\times10^6\text{ N·mm}\).",
             r"\(\sigma_{max}=Mc/I=(37.333\times10^6)(90)/(32\times10^6)\).",
             r"\(\sigma_{max}=105.00\text{ MPa}\), tension at one extreme fibre and compression at the other."],
         final=r"Answer: \(|\sigma_{max}|=105.00\text{ MPa}\)"),

    dict(summary=q(16, "Beam chain 4/4", "The beam material yields at 280 MPa and requires FoS 2.4. Draw the working-versus-allowable check, give a pass/fail verdict, and quantify the reserve margin."),
         label="Beam chain &mdash; final safety verdict",
         svg=stress_bars([("working", 105, GREEN)], allow=("allowable = 116.667 MPa", 116.667),
                         verdict="105 MPa &lt; 116.667 MPa &#8594; PASS"),
         convention=r"Pass only when \(\sigma_{work}\leq\sigma_y/\mathrm{FoS}\).", steps=[
             r"\(\sigma_{allow}=280/2.4=116.667\text{ MPa}\).",
             r"\(105.00<116.667\), so the section passes.",
             r"Reserve relative to allowable \(=(116.667-105)/116.667=10.0\%\)."],
         final="Answer: PASS with 10.0% reserve relative to allowable"),

    dict(summary=q(17, "Truss chain 1/3", "At joint J the applied 20 kN force has components 12 kN right and 16 kN down. Redraw the prompt as a joint FBD and verify the force magnitude and direction."),
         label="Truss/vector chain &mdash; applied load resolution",
         svg=vector_fig([(12, -16, "P = (12, &#8722;16) kN", RED)],
                        scale=6.0, quadrant="load points down and right",
                        note="3-4-5 components: magnitude 20 kN"),
         prompt_svg=TRUSS_FORCE_PROMPT, prompt_caption="Member H is horizontal left; member D is at 120° from +x.",
         convention="+x right, +y upward.", steps=[
             r"\(|P|=\sqrt{12^2+(-16)^2}=20.0\text{ kN}\).",
             r"The direction is \(\tan^{-1}(16/12)=53.13^\circ\) below +x.",
             r"The signed component form \((12,-16)\) is the safest input for the joint equations."],
         final=r"Answer: \(P=20.0\text{ kN}\), \(53.13^\circ\) below +x"),

    dict(summary=q(18, "Truss chain 2/3", "Using Q17, draw tension arrows for members H (leftward horizontal) and D (120&#176; from +x), solve both member forces, and classify tension/compression."),
         label="Truss/vector chain &mdash; joint equilibrium",
         svg=joint_fig([(180, "H = 2.762 kN T", "known"), (120, "D = 18.475 kN T", "known")],
                       load=(12, -16, "P = (12, &#8722;16) kN"),
                       title="Solved joint J", note="positive values confirm the assumed tension arrows"),
         convention="Assume both unknown member forces pull away from J.", steps=[
             r"\(\Sigma F_y=0:\ F_D\sin120^\circ-16=0\Rightarrow F_D=18.475\text{ kN}\).",
             r"\(\Sigma F_x=0:\ -F_H+F_D\cos120^\circ+12=0\).",
             r"\(-F_H-9.238+12=0\Rightarrow F_H=2.762\text{ kN}\). Both are positive, so both are in tension."],
         final="Answer: D = 18.475 kN tension; H = 2.762 kN tension"),

    dict(summary=q(19, "Truss chain 3/3", "Size circular member D from Q18 for an allowable tensile stress of 150 MPa. Sketch the section, find minimum area and diameter, and state a practical rounding rule."),
         label="Truss/vector chain &mdash; axial member sizing",
         svg=section_circle("d min = 12.52 mm", "A req = 123.17 mm&#178;",
                            "F_D = 18.475 kN", stress="choose stock diameter above the calculated minimum"),
         convention=r"Use \(A\geq F/\sigma_{allow}\); never round a minimum size down.", steps=[
             r"\(A_{req}=18475/150=123.17\text{ mm}^2\).",
             r"\(d_{min}=\sqrt{4A/\pi}=\sqrt{4(123.17)/\pi}=12.52\text{ mm}\).",
             "Specify the next available stock diameter at or above 12.52 mm, for example 13 mm if available."],
         final=r"Answer: \(A_{req}=123.17\text{ mm}^2\), \(d_{min}=12.52\text{ mm}\)"),

    dict(summary=q(20, "Challenge", r"For an 8 m beam with 8 kN at 2 m and 18 kN at 6 m, a solution gives \(R_A=9\) kN and \(R_B=17\) kN. Draw the equilibrium audit, identify what check passes and what fails, then correct the reactions."),
         label="Diagnostic FBD &mdash; force closure can hide a moment error",
         svg=beam_fig(8, loads=[(2, "8 kN"), (6, "18 kN")],
                      ra="correct R_A = 10.5 kN", rb="correct R_B = 15.5 kN",
                      dims_=[(0, 2, "2 m"), (2, 6, "4 m"), (6, 8, "2 m")],
                      note="both force and moment equilibrium must close"),
         convention="Moments about A anticlockwise positive.", steps=[
             r"The claimed reactions pass force closure: \(9+17=26=8+18\text{ kN}\).",
             r"But their moment residual is \(17(8)-8(2)-18(6)=12\text{ kN·m}\neq0\).",
             r"Correctly, \(R_B=[8(2)+18(6)]/8=15.5\text{ kN}\), then \(R_A=10.5\text{ kN}\)."],
         final=r"Answer: moment check fails by 12 kN·m; \(R_A=10.5\text{ kN}\), \(R_B=15.5\text{ kN}\)"),

    dict(summary=q(21, "Challenge", "A student draws a straight-line BMD for a 6 m simply supported beam under a full 5 kN/m UDL. Sketch the correct SFD and BMD, diagnose the shape error, and mark the maximum moment."),
         label="Diagram diagnosis &mdash; UDL means linear V and parabolic M",
         svg=vm_diagram([(i / 20, 90 * (i / 20) * (1 - i / 20)) for i in range(21)],
                        title="correct BMD: parabolic sagging moment (kN&#183;m)",
                        color=RED, fill="#f7e2de",
                        labels=[(0.5, 22.5, "22.5 kN&#183;m")],
                        xlabels=[(0, "A"), (0.5, "V=0"), (1, "B")]),
         convention=r"A distributed load changes shear continuously; \(dM/dx=V\).", steps=[
             r"Reactions are \(wL/2=15\text{ kN}\), so \(V=15-5x\): a straight line from +15 to -15 kN.",
             r"Integrating linear shear gives \(M=15x-2.5x^2\), a parabola, not a straight line.",
             r"At \(V=0\), \(x=3\text{ m}\), and \(M_{max}=5(6^2)/8=22.5\text{ kN·m}\)."],
         final="Answer: linear SFD, parabolic BMD; maximum 22.5 kN·m at midspan"),

    dict(summary=q(22, "Challenge", "A 64 kN tie uses area 500 mm&#178;; yield is 250 MPa and FoS is 2.0. Sketch the inequality check, test the proposed area, and find the true minimum area."),
         label="Design diagnosis &mdash; a near miss is still a failure",
         svg=stress_bars([("500 mm&#178; design", 128, RED)], allow=("allowable = 125 MPa", 125),
                         verdict="128 MPa &gt; 125 MPa &#8594; FAIL"),
         convention=r"Design requires \(F/A\leq\sigma_y/\mathrm{FoS}\).", steps=[
             r"\(\sigma_{allow}=250/2=125\text{ MPa}\).",
             r"Proposed stress \(=64000/500=128\text{ MPa}>125\text{ MPa}\): fail.",
             r"\(A_{req}=64000/125=512\text{ mm}^2\). The selected area must be at least 512 mm&#178;."],
         final=r"Answer: 500 mm&#178; fails; \(A_{min}=512\text{ mm}^2\)"),

    dict(summary=q(23, "Challenge", "At a joint, a horizontal-right member and a 120&#176; diagonal balance a 10 kN downward load. A student reports the diagonal as 11.55 kN compression. Draw the joint FBD and use component signs to diagnose and correct both member forces."),
         label="Truss sign diagnosis &mdash; vertical equilibrium decides the sense",
         svg=joint_fig([(0, "H = 5.774 kN T", "known"), (120, "D = 11.547 kN T", "known")],
                       load=(0, -10, "10 kN down"), title="correct joint-force directions",
                       note="a compression diagonal would add downward force and cannot balance the load"),
         convention="Assume tension away from the joint.", steps=[
             r"\(\Sigma F_y=0:\ F_D\sin120^\circ-10=0\Rightarrow F_D=11.547\text{ kN}\) tension.",
             r"\(\Sigma F_x=0:\ F_H+F_D\cos120^\circ=0\Rightarrow F_H=5.774\text{ kN}\) tension.",
             "The reported compression direction gives a downward diagonal component, worsening rather than balancing the applied load."],
         final="Answer: diagonal 11.547 kN tension; horizontal 5.774 kN tension"),

    dict(summary=q(24, "Capstone", r"A 6 m simply supported beam carries 30 kN at midspan and has a 60 mm by 120 mm rectangular section. Yield is 240 MPa and FoS 2.0. Draw the loaded beam, SFD/BMD and stress sketch; find reactions, maximum moment, bending stress, verdict, and required \(I\) at the same depth."),
         label="Capstone synthesis &mdash; load to reaction to moment to design",
         svg=(beam_fig(6, loads=[(3, "30 kN")], ra="R_A = 15 kN", rb="R_B = 15 kN",
                       dims_=[(0, 3, "3 m"), (3, 6, "3 m")])
              + vm_diagram([(0, 15), (0.5, 15), (0.5, -15), (1, -15), (1, 0)],
                           title="SFD: shear V (kN)", color=BLUE,
                           labels=[(0, 15, "+15"), (0.5, -15, "&#8722;15"), (1, 0, "0")],
                           xlabels=[(0, "A"), (0.5, "midspan"), (1, "B")])
              + vm_diagram([(0, 0), (0.5, 45), (1, 0)],
                           title="BMD: moment M (kN&#183;m)", color=RED, fill="#f7e2de",
                           labels=[(0.5, 45, "M max = 45")],
                           xlabels=[(0, "A"), (0.5, "midspan"), (1, "B")])
              + bending_section("b = 60 mm", "h = 120 mm", "c = 60 mm",
                                "M max = 45 kN&#183;m",
                                "&#963; = 312.5 MPa; allowable = 120 MPa &#8594; FAIL")
              + flow_steps(["reactions", "SFD / BMD", "section I", "stress", "verdict"],
                           title="verified dependency chain")),
         convention="Sagging positive; compare stress with allowable, not directly with yield.", steps=[
             r"Symmetry gives \(R_A=R_B=15\text{ kN}\). The SFD is +15 then -15 kN; the triangular BMD peaks at \(M_{max}=15(3)=45\text{ kN·m}\).",
             r"\(I=bh^3/12=60(120^3)/12=8.64\times10^6\text{ mm}^4\), \(c=60\text{ mm}\).",
             r"\(\sigma=Mc/I=(45\times10^6)(60)/(8.64\times10^6)=312.5\text{ MPa}\).",
             r"\(\sigma_{allow}=240/2=120\text{ MPa}\), so it fails. At the same \(c\), \(I_{req}=Mc/\sigma_{allow}=22.5\times10^6\text{ mm}^4\), 2.604 times the present \(I\)."],
         final=r"Answer: \(R_A=R_B=15\text{ kN}\), \(M_{max}=45\text{ kN·m}\), \(\sigma=312.5\text{ MPa}\): FAIL; \(I_{req}=22.5\times10^6\text{ mm}^4\)"),
]


def generate():
    assert len(SPECS) == 24
    html = SOURCE.read_text()
    html = html.replace(
        "DPEN102 Cumulative Revision — Weeks 1-6 (24 Questions)",
        "DPEN102 Cumulative Revision Set B — Weeks 1-6 (24 Questions)",
    )
    html = html.replace(
        "Cumulative Revision: Weeks 1-6 (24 Questions)",
        "Cumulative Revision Set B: Weeks 1-6 (24 Questions)",
    )
    html = html.replace(
        "Integrated Newton/equilibrium, units/moments, vectors/FBD, stress/internal actions, SFD/BMD, and truss logic in one exam-style checkpoint.",
        "A second, reasoning-rich checkpoint: linked beam and truss chains, diagnostics, interpretation, design checks, and capstone synthesis.",
    )
    html = html.replace(
        "<strong>Use as a mock:</strong> 75-90 minutes total. Do Q1-12 first pass, then Q13-24 challenge pass. Show complete setup for every multi-step question.",
        "<strong>Use as a mock:</strong> 90-110 minutes. Q1-12 build foundations; Q13-19 are linked chains; Q20-23 are diagnostics; Q24 is the capstone. Use g = 9.8 m/s&#178;.",
    )
    html = html.replace(
        "    .ans{padding:0 14px 14px;line-height:1.65}\n",
        "    .ans{padding:0 14px 14px;line-height:1.65}\n"
        "    .question-diagram{margin:0 14px 12px;padding:10px;background:#f7f9fc;border:1px solid var(--line);border-radius:7px}\n"
        "    .question-diagram svg{display:block;margin:4px auto;max-width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:6px}\n"
        "    .prompt-label{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--navy);margin-bottom:5px}\n"
        "    .prompt-caption{font-size:12px;color:#5b6779;margin:6px 0 0;text-align:center}\n",
    )
    blocks = re.findall(r'<details class="q">[\s\S]*?</details>', html)
    assert len(blocks) == 24
    for old, spec in zip(blocks, SPECS):
        html = html.replace(old, render(spec), 1)
    TARGET.write_text(html)
    print("generated", TARGET)


if __name__ == "__main__":
    generate()
