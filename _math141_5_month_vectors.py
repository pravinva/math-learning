from pathlib import Path


ROOT = Path(__file__).parent
OUT = ROOT / "siddharth/dpen141/MATH141_5_MONTH_VECTOR_REVISION.html"


def question(number, prompt, solution):
    return f"""
<details class="question" data-question>
  <summary><span class="q-number">{number}</span><span>{prompt}</span></summary>
  <div class="solution">
    <div class="solution-label">Worked explanation</div>
    {solution}
  </div>
</details>"""


def month(number, title, subtitle, lens, diagram, questions):
    lens = lens.strip()
    diagram = diagram.strip()
    cards = "\n".join(
        question(i, prompt, solution)
        for i, (prompt, solution) in enumerate(questions, 1)
    )
    return f"""
<section class="month" id="month-{number}">
  <div class="month-heading">
    <span class="month-number">Month {number}</span>
    <div>
      <h2>{title}</h2>
      <p>{subtitle}</p>
    </div>
  </div>
  <div class="lens">{lens}</div>
  {diagram}
  <div class="cadence">
    <strong>Four-week rhythm:</strong>
    Week 1: read the visual lesson and redraw its main picture.
    Week 2: attempt Questions 1–5.
    Week 3: attempt Questions 6–10.
    Week 4: redo the three questions that changed your picture of the topic.
  </div>
  <div class="set-heading">
    <span>Set {number}</span>
    <h3>Ten questions about geometry, meaning and calculation</h3>
  </div>
  <div class="questions">{cards}</div>
</section>"""


month_1 = [
    (
        r"""Two arrows are drawn: one from \(A=(1,2)\) to \(B=(4,6)\), and another from
        \(C=(-5,3)\) to \(D=(-2,7)\). Are they the same vector? Explain what information
        a vector remembers and what information it forgets.""",
        r"""<p>\(\overrightarrow{AB}=B-A=(3,4)\), while
        \(\overrightarrow{CD}=D-C=(3,4)\). They are the same vector.</p>
        <p>A vector remembers a change: \(3\) units in the \(x\)-direction and \(4\) in
        the \(y\)-direction. It forgets where the arrow was drawn. A translated arrow
        can therefore represent the same velocity or the same free vector.</p>
        <p>An applied force needs one extra piece of physical information: its point
        or line of application. Moving the arrow may leave the force vector unchanged
        while changing the torque on the body, so an applied force cannot in general
        be relocated without changing the physical problem.</p>""",
    ),
    (
        r"""A drone has velocity
        \(\mathbf v=6\mathbf i-2\mathbf j+3\mathbf k\ {\rm m\,s^{-1}}\).
        What are \(\mathbf i,\mathbf j,\mathbf k\), and what physical story do the
        coefficients tell?""",
        r"""<p>The symbols are unit vectors along the chosen coordinate axes:
        \(\mathbf i=(1,0,0)\), \(\mathbf j=(0,1,0)\), and
        \(\mathbf k=(0,0,1)\). They are the three measuring directions of the
        coordinate frame.</p>
        <p>Thus \(\mathbf v=(6,-2,3)\ {\rm m\,s^{-1}}\): \(6\) metres per second in the
        positive \(x\)-direction, \(2\) in the negative \(y\)-direction, and \(3\)
        upward if \(+\mathbf k\) was chosen as up. The numbers mean nothing physically
        until the axes and units are declared.</p>""",
    ),
    (
        r"""In a different basis,
        \(\mathbf e_1=(1,1)\) and \(\mathbf e_2=(1,-1)\).
        Express \(\mathbf w=(4,2)\) as \(a\mathbf e_1+b\mathbf e_2\).
        Explain how one geometric arrow can have two coordinate descriptions.""",
        r"""<p>We need
        \(a(1,1)+b(1,-1)=(a+b,a-b)=(4,2)\). Hence
        \(a+b=4\) and \(a-b=2\), giving \(a=3,\ b=1\).</p>
        <p>So \(\mathbf w=3\mathbf e_1+\mathbf e_2\). Coordinates are instructions
        relative to a chosen set of measuring arrows. A new basis gives new
        instructions for the same geometric vector. It is like describing the same
        location using north/east directions or two diagonal streets.</p>""",
    ),
    (
        r"""A walker goes \(3\) km east, \(4\) km north, then \(3\) km west.
        Find the total distance and the displacement. Why are these different kinds
        of quantities?""",
        r"""<p>The distance is the length of the travelled path:
        \(3+4+3=10\) km. The displacement is the net vector:
        \((3,0)+(0,4)+(-3,0)=(0,4)\) km, whose magnitude is \(4\) km.</p>
        <p>Distance records how much ground was covered, so it is a scalar.
        Displacement records the single arrow from start to finish. Opposite pieces
        cancel because vectors retain direction.</p>""",
    ),
    (
        r"""A cable pulls in the direction \((3,4,0)\) with tension \(50\) N.
        Find the force vector. Explain why multiplying by \((3,4,0)\) directly would
        give the wrong magnitude.""",
        r"""<p>The direction vector has length \(5\), so its unit vector is
        \(\widehat{\mathbf d}=(3/5,4/5,0)\). The force is
        \[
        \mathbf F=50\widehat{\mathbf d}=(30,40,0)\ {\rm N}.
        \]</p>
        <p>The vector \(50(3,4,0)\) would have magnitude \(250\) N because
        \((3,4,0)\) already has length \(5\). A direction vector tells us a direction,
        but only a unit direction lets the coefficient equal the physical magnitude.</p>""",
    ),
    (
        r"""A boat moves through water with velocity \((5,1)\ {\rm m\,s^{-1}}\).
        The current moves at \((-2,3)\ {\rm m\,s^{-1}}\).
        Find the velocity seen from the shore and explain the addition geometrically.""",
        r"""<p>The shore velocity is
        \[
        \mathbf v_{\rm shore}=\mathbf v_{\rm boat/water}+
        \mathbf v_{\rm water/shore}=(5,1)+(-2,3)=(3,4)\ {\rm m\,s^{-1}}.
        \]</p>
        <p>During one second the boat moves by the first arrow relative to its patch of
        water, while the patch itself moves by the second arrow. Placing those arrows
        tip to tail gives the actual start-to-finish arrow. Vector addition is the
        geometry of successive changes.</p>""",
    ),
    (
        r"""Suppose \(\mathbf i\) points east and \(\mathbf j\) points north.
        Which way must \(\mathbf k\) point in a right-handed frame? What would change
        if the third axis were chosen downward instead?""",
        r"""<p>With east as \(+\mathbf i\) and north as \(+\mathbf j\), the right-hand
        rule gives \(\mathbf i\times\mathbf j=\mathbf k\), so \(\mathbf k\) points up.</p>
        <p>If the third positive axis were chosen downward, the coordinate frame would
        be left-handed. Coordinates could still be used, but the familiar cyclic
        cross-product rules would acquire sign changes. Handedness is an orientation
        convention that keeps every later sign consistent.</p>""",
    ),
    (
        r"""A map's new origin is placed at the old-frame coordinate \((10,-4)\).
        A point has old position vector \((13,2)\). Find its coordinates in the new
        frame. Does a displacement vector between two points change?""",
        r"""<p>The new origin has old coordinate \((10,-4)\), so the point is
        \((13,2)-(10,-4)=(3,6)\) relative to it.</p>
        <p>The displacement remains unchanged. Subtracting the same translation from
        both endpoints cancels in \(Q-P\). Position vectors depend on the chosen
        origin, while a displacement records the difference between two points.</p>""",
    ),
    (
        r"""Let \(\mathbf u=(1,0,1)\) and \(\mathbf v=(0,1,1)\).
        Decide whether \(\mathbf w=(2,3,5)\) and \(\mathbf z=(2,3,4)\) lie in the span
        of \(\mathbf u,\mathbf v\). Interpret the span geometrically.""",
        r"""<p>A combination \(a\mathbf u+b\mathbf v=(a,b,a+b)\). For
        \(\mathbf w\), choosing \(a=2,b=3\) gives \(a+b=5\), so
        \(\mathbf w=2\mathbf u+3\mathbf v\).</p>
        <p>For \(\mathbf z\), the first two components force \(a=2,b=3\), but then the
        third would have to be \(5\). Therefore \(\mathbf z=(2,3,4)\) lies outside
        the span.
        Two non-parallel vectors in \(\mathbb R^3\) sweep out a plane through the
        origin; membership in their span means lying in that plane.</p>""",
    ),
    (
        r"""A calculation adds a displacement \((4,1)\) metres to a velocity
        \((2,-3)\) metres per second. The component arithmetic is possible. Why is the
        physical calculation meaningless, and how can units catch the mistake?""",
        r"""<p>The two lists have the same shape, but they measure different kinds of
        quantity. Metres cannot be added to metres per second, just as three seconds
        cannot be added to five kilograms.</p>
        <p>Components retain physical units. A velocity could first be multiplied by a
        time interval to produce a displacement; only then could the vectors be added.
        Dimensional consistency checks physical meaning alongside arithmetic.</p>""",
    ),
]


month_2 = [
    (
        r"""Without finding any angles, classify each pair as acute, perpendicular, or
        obtuse: (a) \((2,1)\) and \((3,-1)\); (b) \((2,1)\) and \((1,-2)\);
        (c) \((2,1)\) and \((-3,1)\).""",
        r"""<p>The signs of the dot products settle the question:
        \[
        (a)\ 2(3)+1(-1)=5>0,\quad
        (b)\ 2(1)+1(-2)=0,\quad
        (c)\ 2(-3)+1(1)=-5<0.
        \]</p>
        <p>Because \(\mathbf u\cdot\mathbf v=\|\mathbf u\|\|\mathbf v\|\cos\theta\),
        a positive dot product means acute, zero means \(90^\circ\), and negative
        means obtuse. The dot product is a signed test of directional agreement.</p>""",
    ),
    (
        r"""For \(\mathbf u=(3,4)\) and \(\mathbf v=(4,0)\), compute the normalised
        alignment \(\dfrac{\mathbf u\cdot\mathbf v}{\|\mathbf u\|\|\mathbf v\|}\).
        Interpret the value, then find the scalar component of \(\mathbf u\) along
        \(\mathbf v\).""",
        r"""<p>The dot product is \(12\), and the lengths are \(5\) and \(4\), so
        \[
        \frac{\mathbf u\cdot\mathbf v}{\|\mathbf u\|\|\mathbf v\|}
        =\frac{12}{20}=0.6=\cos\theta.
        \]</p>
        <p>This is a dimensionless alignment score: \(1\) means same direction,
        \(0\) means perpendicular, and \(-1\) means opposite direction. The score
        \(0.6\) is the cosine of the angle. The scalar component of
        \(\mathbf u\) along \(\mathbf v\) has length
        \(\|\mathbf u\|\cos\theta=3\).</p>""",
    ),
    (
        r"""Replace \(\mathbf u\) by \(10\mathbf u\) in the previous question.
        What happens to the dot product, the angle, and the normalised alignment?
        Explain before calculating.""",
        r"""<p>The dot product becomes ten times larger because
        \((10\mathbf u)\cdot\mathbf v=10(\mathbf u\cdot\mathbf v)\).
        The length of \(\mathbf u\) also becomes ten times larger, so the factor
        cancels in the normalised ratio. The angle and alignment remain unchanged.</p>
        <p>A raw dot product mixes two ideas: lengths and alignment. Dividing by both
        lengths removes scale and leaves only the geometry of direction.</p>""",
    ),
    (
        r"""A constant force \(\mathbf F=(10,6)\) N moves an object through displacement
        \(\mathbf d=(3,-1)\) m. Find the work done and explain which part of the force
        contributes nothing.""",
        r"""<p>
        \[
        W=\mathbf F\cdot\mathbf d=10(3)+6(-1)=24\ {\rm J}.
        \]
        Work counts force in the direction of motion. Any component perpendicular to
        the total displacement \(\mathbf d\) has dot product zero with \(\mathbf d\),
        so it contributes zero to this net work calculation. What that perpendicular
        component does during the motion cannot be inferred from the endpoints alone.</p>
        <p>The negative contribution \(6(-1)\) says the vertical component of force
        opposes the vertical part of the motion.</p>""",
    ),
    (
        r"""A ramp's uphill unit vector is
        \(\widehat{\mathbf t}=(3/5,4/5)\). Gravity on a mass is
        \(\mathbf F=(0,-100)\) N. Find the signed scalar component of gravity uphill
        and interpret its sign.""",
        r"""<p>The scalar projection is
        \[
        \mathbf F\cdot\widehat{\mathbf t}
        =0(3/5)-100(4/5)=-80\ {\rm N}.
        \]</p>
        <p>The negative sign says the component points opposite the declared uphill
        direction, so gravity pulls \(80\) N downhill. Keeping the sign is more useful
        than reporting only a magnitude: it carries the directional decision.</p>""",
    ),
    (
        r"""Decompose \(\mathbf u=(6,2)\) into a component parallel to
        \(\mathbf v=(1,1)\) and a component perpendicular to \(\mathbf v\).
        Explain the geometry of the two pieces.""",
        r"""<p>
        \[
        \operatorname{proj}_{\mathbf v}\mathbf u
        =\frac{\mathbf u\cdot\mathbf v}{\mathbf v\cdot\mathbf v}\mathbf v
        =\frac{8}{2}(1,1)=(4,4).
        \]
        The leftover is \((6,2)-(4,4)=(2,-2)\), and
        \((2,-2)\cdot(1,1)=0\).</p>
        <p>Thus \(\mathbf u=(4,4)+(2,-2)\). The first piece is the shadow along the
        line of \(\mathbf v\); the second is the shortest correction from that line to
        \(\mathbf u\).</p>""",
    ),
    (
        r"""Two sensor readings are \(\mathbf a=(1,2,2)\) and
        \(\mathbf b=(2,4,4)\). Their raw dot product is large. What does their
        normalised alignment reveal that the raw number hides?""",
        r"""<p>Since \(\mathbf b=2\mathbf a\), the vectors have exactly the same
        direction. Their normalised alignment is
        \[
        \frac{\mathbf a\cdot\mathbf b}{\|\mathbf a\|\|\mathbf b\|}=1.
        \]</p>
        <p>The raw dot product grows when either reading is scaled, even if the
        directional pattern is unchanged. Normalisation separates “same pattern” from
        “large readings”, which is why the same geometry appears as cosine similarity
        in data analysis.</p>""",
    ),
    (
        r"""Suppose nonzero vectors \(\mathbf u,\mathbf v\) satisfy
        \(\mathbf u\cdot\mathbf v=0\). Derive the right angle from
        \(\|\mathbf u-\mathbf v\|^2\) and Pythagoras.""",
        r"""<p>Expand:
        \[
        \|\mathbf u-\mathbf v\|^2
        =(\mathbf u-\mathbf v)\cdot(\mathbf u-\mathbf v)
        =\|\mathbf u\|^2+\|\mathbf v\|^2-2\mathbf u\cdot\mathbf v.
        \]
        If the dot product is zero, this becomes
        \(\|\mathbf u-\mathbf v\|^2=\|\mathbf u\|^2+\|\mathbf v\|^2\).</p>
        <p>That is Pythagoras for the triangle whose sides are
        \(\mathbf u,\mathbf v,\mathbf u-\mathbf v\). The zero dot product is the
        algebraic fingerprint of a right angle. The nonzero condition matters because
        the zero vector has no direction and therefore no angle with another vector.</p>""",
    ),
    (
        r"""A force of fixed magnitude \(F\) acts through a displacement of fixed
        length \(d\). Compare the work when the angle between them is
        \(0^\circ,60^\circ,90^\circ,120^\circ,180^\circ\). What does the sequence
        reveal about the dot product?""",
        r"""<p>Since \(W=Fd\cos\theta\), the five values are
        \[
        Fd,\quad \frac12Fd,\quad 0,\quad-\frac12Fd,\quad-Fd.
        \]
        The sign and size record whether the force assists the displacement, has no
        component along it, or opposes it.</p>
        <p>This sequence shows why work uses a dot product: work measures the signed
        component of force along the displacement.</p>""",
    ),
    (
        r"""Why is \(\operatorname{proj}_{\mathbf v}\mathbf u\) the point on the line
        spanned by a nonzero vector \(\mathbf v\) closest to \(\mathbf u\)?
        Give a geometric argument.""",
        r"""<p>Write
        \[
        \mathbf u=\operatorname{proj}_{\mathbf v}\mathbf u+\mathbf r,
        \qquad \mathbf r\perp\mathbf v.
        \]
        Any other point on the line differs from the projection by some
        \(c\mathbf v\). Its error from \(\mathbf u\) is
        \(\mathbf r-c\mathbf v\).</p>
        <p>Those two pieces are perpendicular, so Pythagoras gives
        \(\|\mathbf r-c\mathbf v\|^2=\|\mathbf r\|^2+c^2\|\mathbf v\|^2\).
        This is smallest at \(c=0\). Projection is the nearest-shadow construction
        behind least squares. The condition \(\mathbf v\ne\mathbf0\) is required
        because the projection formula divides by \(\mathbf v\cdot\mathbf v\).</p>""",
    ),
]


month_3 = [
    (
        r"""Complete the oriented cycle
        \(\mathbf i\times\mathbf j,\ \mathbf j\times\mathbf k,\ \mathbf k\times\mathbf i\),
        then reverse each product. What single rule explains all six signs?""",
        r"""<p>In a right-handed frame,
        \[
        \mathbf i\times\mathbf j=\mathbf k,\qquad
        \mathbf j\times\mathbf k=\mathbf i,\qquad
        \mathbf k\times\mathbf i=\mathbf j.
        \]
        Reversing the order reverses the sign:
        \[
        \mathbf j\times\mathbf i=-\mathbf k,\qquad
        \mathbf k\times\mathbf j=-\mathbf i,\qquad
        \mathbf i\times\mathbf k=-\mathbf j.
        \]</p>
        <p>The right-hand rule fixes the orientation. Algebraically this is
        anti-commutativity:
        \(\mathbf u\times\mathbf v=-(\mathbf v\times\mathbf u)\).</p>""",
    ),
    (
        r"""Let \(\mathbf u=(2,0,0)\) and \(\mathbf v=(0,3,0)\).
        Find \(\mathbf u\times\mathbf v\). Interpret both its direction and its
        magnitude.""",
        r"""<p>
        \[
        \mathbf u\times\mathbf v=(0,0,6)=6\mathbf k.
        \]
        Its direction is perpendicular to the \(xy\)-plane, with the positive choice
        fixed by curling from \(\mathbf u\) toward \(\mathbf v\).</p>
        <p>Its magnitude \(6\) is the area of the \(2\)-by-\(3\) parallelogram spanned
        by the vectors. The cross product packages an oriented plane and its area into
        one vector.</p>""",
    ),
    (
        r"""Why is the cross product zero for parallel vectors? Explain using both the
        area picture and \(\|\mathbf u\times\mathbf v\|
        =\|\mathbf u\|\|\mathbf v\|\sin\theta\).""",
        r"""<p>Parallel vectors span a flattened parallelogram, so its area is zero.
        In the magnitude formula their angle is \(0\) or \(\pi\), and
        \(\sin0=\sin\pi=0\).</p>
        <p>A zero cross product therefore signals that the two directions fail to
        determine a plane. There is no unique normal direction to a collapsed
        parallelogram.</p>""",
    ),
    (
        r"""A force \(\mathbf F=(0,50,0)\) N is applied at position
        \(\mathbf r=(0.4,0,0)\) m from a pivot. Find the torque
        \(\boldsymbol\tau=\mathbf r\times\mathbf F\) and interpret the result.""",
        r"""<p>
        \[
        \boldsymbol\tau=(0.4,0,0)\times(0,50,0)=(0,0,20)\ {\rm N\,m}.
        \]
        The magnitude \(20\ {\rm N\,m}\) measures turning effectiveness. The
        \(+\mathbf k\) direction records the axis and sense of the attempted rotation:
        counterclockwise in the \(xy\)-plane when viewed from \(+\mathbf k\).</p>
        <p>Torque is a cross product because the force component perpendicular to the
        lever arm determines the turning effect.</p>""",
    ),
    (
        r"""The same \(30\) N force is applied to a \(0.8\) m door handle in two ways:
        perpendicular to the door and directly toward the hinge. Compare the torques
        without component calculations.""",
        r"""<p>Perpendicular application gives
        \(\tau=rF\sin90^\circ=0.8(30)=24\ {\rm N\,m}\). A force aimed directly toward
        the hinge is parallel to the lever arm, so
        \(\tau=rF\sin180^\circ=0\).</p>
        <p>This is the cross product's sine geometry in ordinary experience. A large
        force can be useless for rotation if its line of action passes through the
        pivot.</p>""",
    ),
    (
        r"""A positive charge \(q\) moves with velocity
        \(\mathbf v=(2,0,0)\ {\rm m\,s^{-1}}\) through a magnetic field
        \(\mathbf B=(0,0,3)\ {\rm T}\). Find the direction of
        \(\mathbf F=q\,\mathbf v\times\mathbf B\). What changes for a negative charge?""",
        r"""<p>
        \[
        \mathbf v\times\mathbf B=(2\mathbf i)\times(3\mathbf k)
        =6(\mathbf i\times\mathbf k)=-6\mathbf j.
        \]
        For \(q>0\), the force points in the negative \(y\)-direction.</p>
        <p>If \(q<0\), multiplying by a negative scalar reverses the direction. The
        magnetic force is perpendicular to the velocity, which is why it bends a path
        without directly increasing the particle's speed.</p>""",
    ),
    (
        r"""A rigid body has angular velocity
        \(\boldsymbol\omega=(0,0,2)\ {\rm rad\,s^{-1}}\). Find the instantaneous
        velocity of the point \(\mathbf r=(3,0,0)\ {\rm m}\) using
        \(\mathbf v=\boldsymbol\omega\times\mathbf r\). Explain the picture.""",
        r"""<p>
        \[
        \mathbf v=(0,0,2)\times(3,0,0)=(0,6,0)\ {\rm m\,s^{-1}}.
        \]
        The velocity is tangent to the circle about the \(z\)-axis and perpendicular
        to the radius. Its speed \(6\) agrees with \(v=\omega r=2(3)\).</p>
        <p>The angular-velocity vector stores the rotation axis in its direction and
        the rotation rate in its length. Crossing it with position turns a radial
        arrow into the correct tangent arrow.</p>""",
    ),
    (
        r"""Does \(\boldsymbol\omega\times\mathbf r\) rotate \(\mathbf r\) through a
        finite angle? State precisely what it describes, and why confusing the two
        ideas causes trouble.""",
        r"""<p>No. The cross product gives the instantaneous velocity, or equivalently
        the first-order change
        \(d\mathbf r\approx(\boldsymbol\omega\times\mathbf r)\,dt\) over a tiny time.</p>
        <p>A finite rotation requires a rotation matrix, Rodrigues' formula, or an
        equivalent construction containing sine and cosine. Repeated tiny tangent
        changes build the curved motion. The cross product supplies the local
        generator of rotation.</p>""",
    ),
    (
        r"""Two directions in a plane are \(\mathbf a=(1,2,0)\) and
        \(\mathbf b=(3,-1,0)\). Find a normal vector and explain why every nonzero scalar
        multiple of it describes the same normal line.""",
        r"""<p>
        \[
        \mathbf a\times\mathbf b
        =(0,0,1(-1)-2(3))=(0,0,-7).
        \]
        This is perpendicular to both directions, so it is normal to their plane.</p>
        <p>Any nonzero multiple, such as \((0,0,-1)\) or \((0,0,14)\), points along
        the same normal line. Normal length is arbitrary. The sign selects one of the
        two orientations.</p>""",
    ),
    (
        r"""A student finds \(\mathbf u\times\mathbf v=(2,-1,4)\) and
        \(\mathbf v\times\mathbf u=(2,-1,4)\). Without recomputing components, diagnose
        the error and state a quick check.""",
        r"""<p>The two answers cannot both be correct unless the cross product is zero.
        Reversing the inputs must reverse the output:
        \[
        \mathbf v\times\mathbf u=-(2,-1,4)=(-2,1,-4).
        \]</p>
        <p>A quick check is to add the two claimed products; the sum must be zero.
        Dotting a candidate with both inputs can confirm perpendicularity, but cannot
        distinguish the two opposite normal directions: both signs are perpendicular.
        The order must be checked with anti-commutativity or the right-hand rule.</p>""",
    ),
]


month_4 = [
    (
        r"""In the cross-product determinant, why may the first row contain
        \(\mathbf i,\mathbf j,\mathbf k\) while the lower rows contain numbers?
        Explain what the expansion is constructing.""",
        r"""<p>The first-row entries are vectors: the standard unit basis
        \(\mathbf i=(1,0,0)\), \(\mathbf j=(0,1,0)\),
        \(\mathbf k=(0,0,1)\). Cofactor expansion produces three scalar minors, then
        uses them as coefficients of these basis vectors.</p>
        <p>The result is therefore a vector assembled as
        \(c_1\mathbf i+c_2\mathbf j+c_3\mathbf k\). Read the array as a compact,
        vector-valued cofactor mnemonic for obtaining the three components. An
        ordinary determinant has scalar entries.</p>""",
    ),
    (
        r"""Expand
        \[
        \begin{vmatrix}
        \mathbf i&\mathbf j&\mathbf k\\
        u_1&u_2&u_3\\
        v_1&v_2&v_3
        \end{vmatrix}.
        \]
        Why is the middle sign negative?""",
        r"""<p>Cofactor expansion along the first row gives
        \[
        (u_2v_3-u_3v_2)\mathbf i
        -(u_1v_3-u_3v_1)\mathbf j
        +(u_1v_2-u_2v_1)\mathbf k.
        \]</p>
        <p>The cofactor signs alternate \(+,-,+\) across the first row. The middle
        minus is part of the determinant's orientation bookkeeping. Omitting it
        usually produces a vector that fails
        the perpendicularity check.</p>""",
    ),
    (
        r"""Use the determinant pattern to calculate
        \(\mathbf u\times\mathbf v\) for
        \(\mathbf u=(1,2,3)\), \(\mathbf v=(4,-1,2)\).""",
        r"""<p>
        \[
        \begin{aligned}
        \mathbf u\times\mathbf v
        &=(2\cdot2-3(-1),\ 3\cdot4-1\cdot2,\ 1(-1)-2\cdot4)\\
        &=(7,10,-9).
        \end{aligned}
        \]</p>
        <p>The middle component was written in its already sign-correct form
        \(u_3v_1-u_1v_3\). This is equivalent to placing the cofactor minus outside the
        corresponding \(2\times2\) determinant.</p>""",
    ),
    (
        r"""Verify that the answer \((7,10,-9)\) from the previous question is
        perpendicular to both inputs. Why is this check stronger than checking only
        one dot product?""",
        r"""<p>
        \[
        (1,2,3)\cdot(7,10,-9)=7+20-27=0,
        \]
        \[
        (4,-1,2)\cdot(7,10,-9)=28-10-18=0.
        \]</p>
        <p>A vector perpendicular to only one input could lie anywhere in a whole
        plane. Being perpendicular to both non-parallel inputs pins it to their common
        normal line. Both checks are needed to test the defining geometry.</p>""",
    ),
    (
        r"""The \(\mathbf i,\mathbf j,\mathbf k\) array is often called a determinant,
        but its first row contains vectors. In what sense is it a useful mnemonic, and
        what deeper determinant properties make it work?""",
        r"""<p>Read the array as a mnemonic for cofactor expansion. Expanding produces
        the three scalar components multiplying the basis vectors.</p>
        <p>It works because determinants are multilinear and alternating. Linearity
        explains how scaling and addition pass through the construction; alternation
        explains why swapping the inputs reverses the sign and why parallel inputs
        give zero. Those are exactly the structural properties an oriented area vector
        must have.</p>""",
    ),
    (
        r"""Take planar vectors \(\mathbf a=(1,3)\) and \(\mathbf b=(2,4)\) as the
        columns of a \(2\times2\) matrix. Compute the determinant and interpret its
        magnitude and sign.""",
        r"""<p>
        \[
        \det\begin{pmatrix}1&2\\3&4\end{pmatrix}=1(4)-2(3)=-2.
        \]
        The magnitude \(2\) is the area of the parallelogram spanned by the columns.</p>
        <p>The negative sign says the ordered pair \((\mathbf a,\mathbf b)\) has the
        opposite orientation to the standard \((\mathbf i,\mathbf j)\) ordering.
        Determinants measure signed area; cross products extend that idea to an
        oriented area vector in three dimensions.</p>""",
    ),
    (
        r"""Find the volume of the parallelepiped generated by
        \(\mathbf a=(1,0,0)\), \(\mathbf b=(0,2,0)\),
        \(\mathbf c=(1,1,3)\) using a scalar triple product. Explain the geometry of
        “base area times height” inside the formula.""",
        r"""<p>
        \[
        \mathbf b\times\mathbf c=(6,0,-2),\qquad
        \mathbf a\cdot(\mathbf b\times\mathbf c)=6.
        \]
        Hence the volume is \(|6|=6\).</p>
        <p>The cross product supplies a normal whose length is the base parallelogram's
        area. Dotting with \(\mathbf a\) keeps only the component of \(\mathbf a\)
        perpendicular to that base: its signed height. Their product is base area
        times height.</p>""",
    ),
    (
        r"""What happens to
        \(\mathbf a\cdot(\mathbf b\times\mathbf c)\) when two vectors are swapped?
        State the effect on orientation and ordinary volume.""",
        r"""<p>Swapping any two vectors reverses the sign of the scalar triple product.
        For example,
        \(\mathbf a\cdot(\mathbf c\times\mathbf b)
        =-\mathbf a\cdot(\mathbf b\times\mathbf c)\).</p>
        <p>The absolute value, and hence ordinary volume, remains unchanged. The sign
        reverses because the ordering has switched handedness. The sign records
        orientation while the absolute value records ordinary volume.</p>""",
    ),
    (
        r"""Show that \(\mathbf a=(1,0,1)\), \(\mathbf b=(0,1,1)\), and
        \(\mathbf c=(2,3,5)\) are coplanar using a scalar triple product. Connect the
        zero to a linear-combination statement.""",
        r"""<p>First compute the normal:
        \[
        \mathbf a\times\mathbf b
        =(1,0,1)\times(0,1,1)=(-1,-1,1).
        \]
        Then
        \[
        \mathbf c\cdot(\mathbf a\times\mathbf b)
        =(2,3,5)\cdot(-1,-1,1)=-2-3+5=0.
        \]</p>
        <p>The zero says \(\mathbf c\) has no component along the plane's normal.
        Indeed, \(\mathbf c=2\mathbf a+3\mathbf b\). The zero volume and the
        linear-combination statement describe the same coplanarity.</p>""",
    ),
    (
        r"""Show that
        \(\mathbf u\times(\mathbf v+c\mathbf u)=\mathbf u\times\mathbf v\)
        for every scalar \(c\). Explain this identity by sliding one side of a
        parallelogram.""",
        r"""<p>Using distributivity and \(\mathbf u\times\mathbf u=\mathbf0\),
        \[
        \mathbf u\times(\mathbf v+c\mathbf u)
        =\mathbf u\times\mathbf v+c(\mathbf u\times\mathbf u)
        =\mathbf u\times\mathbf v.
        \]</p>
        <p>Geometrically, adding a multiple of the base vector \(\mathbf u\) slides the
        tip of the other side parallel to the base. The parallelogram is sheared, but
        its height, area, and oriented normal remain unchanged. Row replacement leaves
        a determinant unchanged for exactly the same reason.</p>""",
    ),
]


month_5 = [
    (
        r"""For each request, choose the most direct operation: (a) directional
        agreement, (b) a component along a line, (c) an oriented normal to a plane,
        (d) work, (e) torque, (f) volume from three edge vectors.""",
        r"""<p>(a) Use a normalised dot product. (b) Use projection, which is built
        from a dot product. (c) Use a cross product. (d) Use
        \(\mathbf F\cdot\mathbf d\). (e) Use
        \(\mathbf r\times\mathbf F\). (f) Use the absolute scalar triple product.</p>
        <p>The organising question is: what kind of output and geometry are required?
        Dot produces a scalar measuring along-ness; cross produces a perpendicular
        vector whose magnitude is oriented area; projection returns the along-part
        itself.</p>""",
    ),
    (
        r"""A force \(\mathbf F=(3,4,0)\) N acts at
        \(\mathbf r=(2,0,0)\) m from a pivot while the point moves through
        \(\mathbf d=(5,0,0)\) m. Find the work and torque. Explain why the same force
        is inspected in two different ways.""",
        r"""<p>
        \[
        W=\mathbf F\cdot\mathbf d=15\ {\rm J},\qquad
        \boldsymbol\tau=\mathbf r\times\mathbf F=(0,0,8)\ {\rm N\,m}.
        \]</p>
        <p>Work asks how much force lies along the motion, so it uses cosine geometry.
        Torque asks how much force lies perpendicular to the lever arm, so it uses
        sine geometry. Neither number is “the effect of the force” in general; each
        answers a different physical question.</p>""",
    ),
    (
        r"""An actuator applies \(\mathbf F=(70,10)\) N beside a rail whose unit
        direction is \(\widehat{\mathbf t}=(3/5,4/5)\).
        Decompose the force into components parallel and perpendicular to the rail.""",
        r"""<p>The tangent component is
        \[
        \mathbf F_\parallel=(\mathbf F\cdot\widehat{\mathbf t})
        \widehat{\mathbf t}
        =50(3/5,4/5)=(30,40)\ {\rm N}.
        \]
        The perpendicular component is
        \[
        \mathbf F_\perp=\mathbf F-\mathbf F_\parallel=(40,-30)\ {\rm N}.
        \]</p>
        <p>The check \((30,40)+(40,-30)=(70,10)\) reconstructs the force, while
        \((40,-30)\cdot(3/5,4/5)=0\) confirms the geometry.</p>""",
    ),
    (
        r"""An aircraft points with air velocity \((180,0)\) km/h while wind velocity
        is \((0,60)\) km/h. Find its ground velocity, speed, and drift angle. Which
        vector operation creates the ground velocity, and which extracts the angle?""",
        r"""<p>Vector addition gives
        \(\mathbf v_g=(180,60)\) km/h. Its speed is
        \(\sqrt{180^2+60^2}=60\sqrt{10}\approx189.7\) km/h, and its drift angle north
        of east is
        \(\tan^{-1}(60/180)=\tan^{-1}(1/3)\approx18.4^\circ\).</p>
        <p>Addition is required because both velocities contribute during the same
        interval. The drift angle is then the orientation of the resulting velocity
        relative to east, found by inverse trigonometry or a normalised dot product
        with the east unit vector.</p>""",
    ),
    (
        r"""A plane contains directions \(\mathbf a=(1,1,0)\) and
        \(\mathbf b=(0,1,1)\). Find a normal and then find the acute angle between the
        plane and \(\mathbf d=(1,0,0)\). Explain why both cross and dot appear.""",
        r"""<p>A normal is
        \[
        \mathbf n=\mathbf a\times\mathbf b=(1,-1,1).
        \]
        If \(\alpha\) is the angle between \(\mathbf d\) and the normal,
        \(\cos\alpha=1/\sqrt3\). The angle \(\beta\) between the line and plane is
        complementary, so
        \[
        \sin\beta=\frac{|\mathbf d\cdot\mathbf n|}
        {\|\mathbf d\|\|\mathbf n\|}=\frac1{\sqrt3},
        \qquad
        \boxed{\beta=\sin^{-1}\!\left(\frac1{\sqrt3}\right)\approx35.3^\circ}.
        \]</p>
        <p>Cross first constructs the normal; dot then measures alignment with it.
        Synthesis problems often require operations in sequence.</p>""",
    ),
    (
        r"""A line passes through the origin in direction \(\mathbf d=(2,1,0)\).
        Find the shortest distance from \(P=(1,3,0)\) to the line using a cross product.
        Explain why the formula measures the perpendicular part.""",
        r"""<p>
        \[
        \operatorname{dist}(P,L)
        =\frac{\|\overrightarrow{OP}\times\mathbf d\|}{\|\mathbf d\|}
        =\frac{\|(1,3,0)\times(2,1,0)\|}{\sqrt5}
        =\frac{5}{\sqrt5}=\sqrt5.
        \]</p>
        <p>The cross-product magnitude is
        \(\|OP\|\|d\|\sin\theta\). Dividing by \(\|d\|\) leaves
        \(\|OP\|\sin\theta\), precisely the height of the parallelogram and therefore
        the perpendicular distance to the line.</p>""",
    ),
    (
        r"""A \(0.3\) m wrench lies along \(+\mathbf i\). You need torque
        \(\boldsymbol\tau=(0,0,12)\ {\rm N\,m}\). Find the smallest-magnitude force
        that produces this torque, and explain why adding force along the wrench is
        wasted effort.""",
        r"""<p>Write \(\mathbf r=(0.3,0,0)\) m and
        \(\mathbf F=(F_x,F_y,F_z)\) N. Then
        \[
        \mathbf r\times\mathbf F=(0,-0.3F_z,0.3F_y)=(0,0,12).
        \]
        Hence \(F_z=0\) and \(F_y=40\) N, while \(F_x\) is unrestricted by the torque.</p>
        <p>The smallest magnitude occurs at \(F_x=0\), giving
        \(\boxed{\mathbf F=(0,40,0)\ {\rm N}}\). Any \(F_x\) component is parallel to
        the wrench, so its cross product with \(\mathbf r\) is zero; it increases the
        applied force without increasing the torque.</p>""",
    ),
    (
        r"""For \(\mathbf u=(3,0,0)\) and \(\mathbf v=(4,4,0)\), compute
        \(\mathbf u\cdot\mathbf v\) and
        \(\|\mathbf u\times\mathbf v\|\). Use the results to explain
        \[
        (\mathbf u\cdot\mathbf v)^2+\|\mathbf u\times\mathbf v\|^2
        =\|\mathbf u\|^2\|\mathbf v\|^2.
        \]""",
        r"""<p>The dot product is \(12\), and
        \(\mathbf u\times\mathbf v=(0,0,12)\), so the cross magnitude is also \(12\).
        The left side is \(144+144=288\). The right side is
        \(3^2(4\sqrt2)^2=9(32)=288\).</p>
        <p>The identity comes directly from
        \(\cos^2\theta+\sin^2\theta=1\) multiplied by
        \(\|\mathbf u\|^2\|\mathbf v\|^2\). Dot and cross are complementary
        measurements of the same pair: one uses the cosine of the angle and the other
        uses its sine.</p>""",
    ),
    (
        r"""Let \(\mathbf u=(1,0,0)\) and \(\mathbf v=(0,-1,0)\).
        The dot product says the angle is \(90^\circ\). What extra information does
        the cross product provide?""",
        r"""<p>
        \[
        \mathbf u\cdot\mathbf v=0,\qquad
        \mathbf u\times\mathbf v=(0,0,-1)=-\mathbf k.
        \]
        The dot product gives the unsigned angle. The negative \(z\)-direction of the
        cross product says the turn from \(\mathbf u\) to \(\mathbf v\) is clockwise
        when viewed from \(+\mathbf k\).</p>
        <p>Together, dot and cross distinguish “how far around” from “which way
        around”. This is useful in navigation, robotics, and orientation tests.</p>""",
    ),
    (
        r"""A robot faces
        \(\widehat{\mathbf f}=(1,1,0)/\sqrt2\). A target lies at displacement
        \(\mathbf d=(4,0,0)\) m. Find (i) how far ahead the target is, (ii) the
        sideways correction vector, and (iii) whether the target lies to the robot's
        left or right when viewed from \(+\mathbf k\).""",
        r"""<p>The signed forward distance is
        \[
        \mathbf d\cdot\widehat{\mathbf f}
        =\frac4{\sqrt2}=2\sqrt2\ {\rm m}.
        \]
        The forward projection is
        \(2\sqrt2\,\widehat{\mathbf f}=(2,2,0)\) m, so the sideways correction is
        \(\mathbf d-(2,2,0)=(2,-2,0)\) m.</p>
        <p>Finally,
        \[
        \widehat{\mathbf f}\times\mathbf d=(0,0,-2\sqrt2).
        \]
        The negative \(z\)-sign says the turn from facing direction to target is
        clockwise, so the target is to the robot's right. Dot measures aheadness,
        projection constructs the ahead-part, and cross supplies left-versus-right.</p>""",
    ),
]


lens_1 = r"""
<h3>An arrow is the object; coordinates are its description</h3>
<p>A vector represents a directed change. A column of numbers records its components
in a chosen coordinate system. The same arrow may begin anywhere, and its coordinates
may change when the measuring axes change.</p>
<p>The standard basis vectors \(\mathbf i,\mathbf j,\mathbf k\) are three unit arrows.
Writing \(3\mathbf i-2\mathbf j+\mathbf k\) assembles an arrow from three independent
directional moves. In physics, every coefficient answers “how much in this measuring
direction?”</p>
<p>During this month, resist the urge to begin with a formula. Draw a tail, draw a tip,
label the axes and units, and ask whether the quantity is a position, a displacement,
a velocity, or a force. Good vector work begins by knowing what the arrow means.</p>"""

lens_2 = r"""
<h3>The dot product is an alignment meter</h3>
<p>Multiplying matching components and adding looks arbitrary until you see what the
sum measures. The dot product becomes large and positive when two arrows reinforce one
another, zero when they meet at a right angle, and negative when one points partly
against the other. After dividing out both lengths, what remains is \(\cos\theta\), a
pure score of directional alignment.</p>
<p>Projection turns that score back into a vector. It asks for the shadow of one arrow
on the line of another. In mechanics this extracts force along a ramp; in work it
extracts force along motion; in data science it finds the closest approximation in a
chosen direction or subspace.</p>
<p>Keep scalar projection and vector projection distinct. One answers “how much,
signed?” The other answers “which arrow is that part?”</p>"""

lens_3 = r"""
<h3>The cross product is an oriented area vector</h3>
<p>Its magnitude is the area swept out by two arrows, and its direction is
perpendicular to their plane. That direction also remembers an ordering: swapping
the arrows reverses the normal.</p>
<p>This is exactly what torque needs. A force along a lever arm produces no turn; a
perpendicular force produces the greatest turn. It is also what rotational velocity
needs: \(\boldsymbol\omega\times\mathbf r\) points tangent to the circle traced by the
point at \(\mathbf r\).</p>
<p>A generic cross product is an oriented area vector; it acquires a rotational
meaning only in a physical construction such as
\(\mathbf r\times\mathbf F\) or \(\boldsymbol\omega\times\mathbf r\).
A finite rotation through a large angle uses a rotation matrix or Rodrigues' formula.
The cross product in \(\boldsymbol\omega\times\mathbf r\) supplies the instantaneous
tangent velocity.</p>"""

lens_4 = r"""
<h3>The determinant encodes oriented area</h3>
<p>The familiar \(\mathbf i,\mathbf j,\mathbf k\) determinant is useful because the
determinant already knows how oriented area behaves. Scale one side and the area scales.
Swap the sides and the orientation reverses. Make the sides parallel and the area
collapses to zero. These behaviours define the cross product's geometry.</p>
<p>The \(+,-,+\) cofactor pattern produces the coordinates of the unique oriented area
vector perpendicular to both inputs. The scalar triple product then adds a third arrow:
cross builds an oriented base area, dot extracts perpendicular height, and the result
is signed volume.</p>
<p>Use the determinant to calculate and dot products to check. A valid cross product
has zero dot product with both inputs.</p>"""

lens_5 = r"""
<h3>Choose an operation by the question it answers</h3>
<p>Choose the formula from the required output. A scalar measuring along-ness suggests
dot. A vector normal to a plane suggests cross. An along-component suggests projection.
Successive motions suggest addition.</p>
<p>Physical problems often need several of these in sequence. A cross product may
construct a plane normal, then a dot product may find an angle to that normal. A dot
product may locate a target ahead of a robot, then a cross product may decide whether
the target lies left or right.</p>
<p>This final month is about seeing the geometry before touching the algebra. The
calculation should feel like the consequence of a decision already made.</p>"""


diagram_1 = r"""
<figure class="diagram-card">
<svg viewBox="0 0 760 330" role="img" aria-labelledby="basisTitle basisDesc">
<title id="basisTitle">A vector decomposed into basis directions</title>
<desc id="basisDesc">A vector is shown as the sum of horizontal, vertical and depth components.</desc>
<defs><marker id="a1" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#1B3A5C"/></marker><marker id="a1r" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#E24A33"/></marker></defs>
<rect width="760" height="330" rx="14" fill="#fbfcfe"/>
<line x1="120" y1="255" x2="590" y2="255" stroke="#9aa8b8" marker-end="url(#a1)"/>
<line x1="120" y1="255" x2="120" y2="50" stroke="#9aa8b8" marker-end="url(#a1)"/>
<line x1="120" y1="255" x2="200" y2="200" stroke="#9aa8b8" marker-end="url(#a1)"/>
<polyline points="120,255 420,255 420,115 500,60" fill="none" stroke="#88a0b9" stroke-width="3" stroke-dasharray="9 7"/>
<line x1="120" y1="255" x2="500" y2="60" stroke="#E24A33" stroke-width="5" marker-end="url(#a1r)"/>
<text x="600" y="261" class="svg-label">i : one x-step</text><text x="82" y="42" class="svg-label">j : one y-step</text><text x="203" y="198" class="svg-label">k : one z-step</text>
<text x="295" y="288" class="svg-note">3i</text><text x="432" y="188" class="svg-note">2j</text><text x="485" y="104" class="svg-note">k</text>
<text x="520" y="56" class="svg-strong">v = 3i + 2j + k</text>
</svg>
<figcaption>The red arrow is one object. The broken path shows how the chosen basis describes it.</figcaption>
</figure>"""

diagram_2 = r"""
<figure class="diagram-card">
<svg viewBox="0 0 760 330" role="img" aria-labelledby="dotTitle dotDesc">
<title id="dotTitle">Projection as the shadow of one vector on another</title>
<desc id="dotDesc">A vector drops a perpendicular to a reference direction, forming a projected component and residual.</desc>
<defs><marker id="a2b" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#1B3A5C"/></marker><marker id="a2r" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#E24A33"/></marker></defs>
<rect width="760" height="330" rx="14" fill="#fbfcfe"/>
<line x1="85" y1="260" x2="680" y2="260" stroke="#a8b2bf" stroke-width="2"/>
<line x1="110" y1="260" x2="585" y2="260" stroke="#1B3A5C" stroke-width="5" marker-end="url(#a2b)"/>
<line x1="110" y1="260" x2="455" y2="75" stroke="#E24A33" stroke-width="5" marker-end="url(#a2r)"/>
<line x1="455" y1="75" x2="455" y2="260" stroke="#6f8f7b" stroke-width="3" stroke-dasharray="8 6"/>
<path d="M455 235h25v25" fill="none" stroke="#6f8f7b" stroke-width="2"/>
<text x="590" y="250" class="svg-strong">v</text><text x="456" y="62" class="svg-strong">u</text>
<text x="270" y="292" class="svg-note">projᵥu : the shadow</text><text x="470" y="165" class="svg-note">residual ⟂ v</text>
</svg>
<figcaption>Dividing the dot product by \(\|\mathbf v\|\) gives the signed length of the red arrow's shadow on the navy line.</figcaption>
</figure>"""

diagram_3 = r"""
<figure class="diagram-card">
<svg viewBox="0 0 760 350" role="img" aria-labelledby="crossTitle crossDesc">
<title id="crossTitle">Cross product as oriented area, torque and tangent velocity</title>
<desc id="crossDesc">Two vectors span a parallelogram while their cross product points normal; angular velocity crossed with radius points tangent.</desc>
<defs><marker id="a3n" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#1B3A5C"/></marker><marker id="a3r" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#E24A33"/></marker><marker id="a3g" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#2f7d5b"/></marker></defs>
<rect width="760" height="350" rx="14" fill="#fbfcfe"/>
<polygon points="80,275 315,230 420,95 185,140" fill="#dfe8f3" stroke="#9badc1" stroke-width="2"/>
<line x1="80" y1="275" x2="315" y2="230" stroke="#1B3A5C" stroke-width="5" marker-end="url(#a3n)"/>
<line x1="80" y1="275" x2="185" y2="140" stroke="#E24A33" stroke-width="5" marker-end="url(#a3r)"/>
<line x1="80" y1="275" x2="80" y2="55" stroke="#2f7d5b" stroke-width="5" marker-end="url(#a3g)"/>
<text x="323" y="229" class="svg-strong">u</text><text x="190" y="132" class="svg-strong">v</text><text x="92" y="64" class="svg-strong">u × v</text>
<circle cx="590" cy="190" r="92" fill="none" stroke="#c4ced9" stroke-width="3"/>
<circle cx="590" cy="190" r="11" fill="#fff" stroke="#2f7d5b" stroke-width="3"/>
<circle cx="590" cy="190" r="3.5" fill="#2f7d5b"/>
<text x="535" y="166" class="svg-note">ω out of page</text>
<line x1="590" y1="190" x2="675" y2="190" stroke="#1B3A5C" stroke-width="4" marker-end="url(#a3n)"/>
<line x1="675" y1="190" x2="675" y2="95" stroke="#E24A33" stroke-width="4" marker-end="url(#a3r)"/>
<text x="625" y="215" class="svg-note">r</text><text x="686" y="105" class="svg-note">ω × r</text>
</svg>
<figcaption>Left: an oriented area normal. Right: crossing angular velocity with radius produces a tangent.</figcaption>
</figure>"""

diagram_4 = r"""
<figure class="diagram-card determinant-picture">
  <div class="det-panel"><span class="det-title">The calculation</span>
  \[
  \mathbf u\times\mathbf v=
  \begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\u_1&u_2&u_3\\v_1&v_2&v_3\end{vmatrix}
  \]
  <div class="signs"><b>+</b><b>−</b><b>+</b></div></div>
  <div class="det-arrow">means</div>
  <div class="det-panel"><span class="det-title">The geometry</span>
  <p>linear in each input</p><p>zero when parallel</p><p>sign flips when order flips</p><p>length = area</p></div>
<figcaption>The determinant notation is compact because determinant behaviour already matches oriented area.</figcaption>
</figure>"""

diagram_5 = r"""
<figure class="diagram-card choice-map">
<svg viewBox="0 0 760 360" role="img" aria-labelledby="choiceTitle choiceDesc">
<title id="choiceTitle">Decision map for vector operations</title>
<desc id="choiceDesc">Questions branch to addition, dot product, projection, cross product or scalar triple product according to the output needed.</desc>
<rect width="760" height="360" rx="14" fill="#fbfcfe"/>
<g class="node"><rect x="270" y="25" width="220" height="54" rx="12"/><text x="380" y="58">What must the answer mean?</text></g>
<g class="node blue"><rect x="25" y="145" width="130" height="58" rx="10"/><text x="90" y="169">net change</text><text x="90" y="189">ADD</text></g>
<g class="node blue"><rect x="170" y="145" width="130" height="58" rx="10"/><text x="235" y="169">alignment</text><text x="235" y="189">DOT</text></g>
<g class="node blue"><rect x="315" y="145" width="130" height="58" rx="10"/><text x="380" y="169">along-part</text><text x="380" y="189">PROJECT</text></g>
<g class="node red"><rect x="460" y="145" width="130" height="58" rx="10"/><text x="525" y="169">normal / turn</text><text x="525" y="189">CROSS</text></g>
<g class="node red"><rect x="605" y="145" width="130" height="58" rx="10"/><text x="670" y="169">3D volume</text><text x="670" y="189">TRIPLE</text></g>
<g stroke="#8291a3" stroke-width="2" fill="none"><path d="M380 79V110H90V145"/><path d="M380 110H235V145"/><path d="M380 110V145"/><path d="M380 110H525V145"/><path d="M380 110H670V145"/></g>
<text x="90" y="248" class="svg-note" text-anchor="middle">successive motion</text><text x="235" y="248" class="svg-note" text-anchor="middle">angle, work</text><text x="380" y="248" class="svg-note" text-anchor="middle">shadow, nearest</text><text x="525" y="248" class="svg-note" text-anchor="middle">torque, orientation</text><text x="670" y="248" class="svg-note" text-anchor="middle">base × height</text>
<text x="380" y="318" class="svg-strong" text-anchor="middle">Let the meaning of the output choose the operation.</text>
</svg>
</figure>"""


months = [
    month(1, "Vectors before coordinates", "Arrows, bases, units, displacement and physical meaning", lens_1, diagram_1, month_1),
    month(2, "Dot product as alignment", "Angles, work, shadows, projections and closest points", lens_2, diagram_2, month_2),
    month(3, "Cross product as oriented turning", "Area, normals, torque, magnetic force and rotational velocity", lens_3, diagram_3, month_3),
    month(4, "Why the determinant computes a cross product", "The roles of i, j, k, orientation, cofactors and volume", lens_4, diagram_4, month_4),
    month(5, "Choosing the right operation", "Integrated geometry and physics: what to use, when, and why", lens_5, diagram_5, month_5),
]


html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MATH141 — 5 Month Vector Revision</title>
<script>
window.MathJax={tex:{inlineMath:[['$','$'],['\\(','\\)']],displayMath:[['$$','$$'],['\\[','\\]']]}};
</script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap');
:root{--ink:#1B2431;--red:#E24A33;--paper:#fff;--wash:#f4f7fa;--line:#cbd5df;--muted:#5d6876;--blue:#1B3A5C;--green:#2f7d5b}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--wash);color:var(--ink);font-family:Barlow,system-ui,sans-serif;line-height:1.66}
header{background:var(--ink);color:#fff;padding:54px 24px 44px;border-bottom:7px solid var(--red)}
.hero{max-width:980px;margin:auto}.eyebrow,.month-number,.solution-label,.set-heading span{font:500 11px/1.3 "Roboto Mono",monospace;letter-spacing:.12em;text-transform:uppercase}
.eyebrow{color:#aebed0}.hero h1{font-size:clamp(34px,6vw,62px);line-height:1.03;max-width:850px;margin:12px 0 18px;letter-spacing:-.035em}
.hero>p{color:#ccd5df;font-size:18px;max-width:780px;margin:0}.hero-meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:24px}.hero-meta span{border:1px solid #526070;border-radius:99px;padding:5px 11px;font-size:12px;color:#d7dee7}
.topnav{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.96);border-bottom:1px solid var(--line);backdrop-filter:blur(8px)}
.topnav-inner{max-width:980px;margin:auto;padding:10px 20px;display:flex;gap:8px;overflow-x:auto}.topnav a{white-space:nowrap;text-decoration:none;color:var(--blue);border:1px solid var(--line);border-radius:7px;padding:7px 11px;font-size:13px}.topnav a:hover{border-color:var(--red);color:var(--red)}
main{max-width:980px;margin:auto;padding:40px 20px 90px}.how{background:#fff;border:1px solid var(--line);border-left:5px solid var(--red);padding:20px 24px;border-radius:10px;margin-bottom:44px}.how h2{margin:0 0 7px;font-size:22px}.how p{margin:7px 0}
.month{scroll-margin-top:76px;margin:0 0 78px}.month-heading{display:flex;gap:20px;align-items:flex-start;border-bottom:3px solid var(--ink);padding-bottom:15px}.month-number{background:var(--red);color:#fff;padding:6px 10px;border-radius:5px;white-space:nowrap;margin-top:5px}.month-heading h2{font-size:clamp(26px,4vw,38px);line-height:1.1;margin:0}.month-heading p{margin:6px 0 0;color:var(--muted)}
.lens{font-size:17px;max-width:820px;margin:24px auto}.lens h3{font-size:23px;margin:0 0 10px;color:var(--blue)}.lens p{margin:12px 0}
.diagram-card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px;margin:24px 0;overflow-x:auto;box-shadow:0 3px 16px rgba(27,36,49,.06)}.diagram-card svg{display:block;width:100%;min-width:650px;height:auto}.diagram-card figcaption{font-size:13px;color:var(--muted);text-align:center;padding:8px 10px 2px}.svg-label,.svg-note,.svg-strong{font-family:Barlow,sans-serif;fill:#526170}.svg-label{font-size:15px}.svg-note{font-size:14px}.svg-strong{font-size:16px;font-weight:700;fill:#1B3A5C}
.cadence{background:#eaf2f9;border-left:4px solid var(--blue);padding:13px 16px;border-radius:6px;margin:24px 0;font-size:14px}.cadence strong{color:var(--blue)}
.set-heading{display:flex;gap:14px;align-items:baseline;margin:34px 0 14px}.set-heading span{color:var(--red)}.set-heading h3{margin:0;font-size:21px}
.question{background:#fff;border:1px solid var(--line);border-radius:9px;margin:11px 0;overflow:hidden}.question[open]{border-color:#97a8ba;box-shadow:0 4px 18px rgba(27,36,49,.07)}
.question summary{display:flex;gap:13px;align-items:flex-start;padding:15px 17px;cursor:pointer;font-size:16px;font-weight:600;list-style:none}.question summary::-webkit-details-marker{display:none}.question summary::after{content:"+";margin-left:auto;color:var(--red);font-size:22px;line-height:1}.question[open] summary::after{content:"−"}.q-number{font:500 12px/1.4 "Roboto Mono",monospace;background:#edf1f5;color:var(--blue);padding:3px 7px;border-radius:4px;flex:none}
.solution{padding:16px 20px 19px 57px;border-top:1px dashed var(--line);background:#fbfcfd}.solution-label{color:var(--green);margin-bottom:7px}.solution p{margin:8px 0}.solution mjx-container[display="true"]{overflow-x:auto;overflow-y:hidden;max-width:100%}
.determinant-picture{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:18px}.det-panel{background:#f5f7fa;border-radius:9px;padding:18px;text-align:center;min-width:280px}.det-title{font-weight:700;color:var(--blue)}.det-panel p{margin:5px}.signs{display:flex;justify-content:center;gap:55px;color:var(--red);font:700 20px "Roboto Mono"}.det-arrow{font-weight:700;color:var(--red)}
.determinant-picture figcaption{grid-column:1/-1}.choice-map .node rect{fill:#fff;stroke:#9aa9ba;stroke-width:2}.choice-map .node.blue rect{fill:#eaf2f9;stroke:#1B3A5C}.choice-map .node.red rect{fill:#fff0ec;stroke:#E24A33}.choice-map .node text{font:600 13px Barlow;text-anchor:middle;fill:#1B2431}
.controls{position:fixed;right:18px;bottom:18px;display:flex;gap:7px;z-index:30}.controls button{border:0;border-radius:7px;padding:9px 12px;background:var(--ink);color:#fff;font-family:Barlow;cursor:pointer;box-shadow:0 3px 12px rgba(0,0,0,.18)}.controls button:last-child{background:var(--red)}
footer{border-top:1px solid var(--line);padding:25px 0;margin-top:35px;color:var(--muted)}footer a{color:var(--blue)}
@media(max-width:700px){header{padding-top:38px}.hero>p{font-size:16px}.month-heading{display:block}.month-number{display:inline-block;margin-bottom:11px}.solution{padding:15px}.question summary{padding:14px}.determinant-picture{display:block}.det-arrow{text-align:center;margin:10px}.controls{right:10px;bottom:10px}.controls button{font-size:12px;padding:8px}.diagram-card svg{min-width:620px}}
@media print{.topnav,.controls{display:none}.question .solution{display:block}.question{break-inside:avoid}body{background:#fff}header{background:#fff;color:#000;border-bottom:3px solid #000}.hero>p,.eyebrow{color:#333}}
</style>
</head>
<body>
<header><div class="hero">
  <div class="eyebrow">MATH141 · Non-calculus revision</div>
  <h1>Five months of seeing vectors</h1>
  <p>Fifty questions arranged around five pictures: arrows, shadows, oriented area,
  determinants, and physical decisions. Each set develops a clear picture of what the
  operations measure and how they apply in geometry and physics.</p>
  <div class="hero-meta"><span>5 months</span><span>5 sets × 10 questions</span><span>worked explanations</span><span>geometry + physics</span></div>
</div></header>
<nav class="topnav"><div class="topnav-inner">
  <a href="#month-1">1 · Arrows &amp; basis</a><a href="#month-2">2 · Dot &amp; projection</a>
  <a href="#month-3">3 · Cross &amp; rotation</a><a href="#month-4">4 · Determinants</a>
  <a href="#month-5">5 · Choosing operations</a>
</div></nav>
<main>
<section class="how">
  <h2>How to use a five-month course</h2>
  <p>Spend one month revisiting each set. Begin each question with a sketch and one
  sentence naming the quantity you expect: a scalar, an along-component, a normal
  vector, an area, or a turning direction.</p>
  <p>Open a solution only after committing to a picture. When an answer surprises you,
  close it and explain the result aloud without symbols. Calculation is useful here,
  but explanation is the part that should survive five months.</p>
  <p><a href="Lesson_Vectors_Dot_Cross_Products_Projections.html">Use the full vector lesson for prerequisite techniques</a>.
  This course is the spaced conceptual follow-up.</p>
</section>
""" + "\n".join(months) + r"""
<footer>
  <a href="MATH141_LINEAR_POLY_REVISION_HUB.html">← MATH141 Revision Hub</a>
  &nbsp;·&nbsp; <a href="index.html">DPEN141 index</a>
  &nbsp;·&nbsp; <a href="Lesson_Vectors_Dot_Cross_Products_Projections.html">Full vector lesson</a>
</footer>
</main>
<div class="controls"><button type="button" id="openAll">Reveal all</button><button type="button" id="closeAll">Hide all</button></div>
<script>
const qs=[...document.querySelectorAll("[data-question]")];
document.getElementById("openAll").addEventListener("click",()=>qs.forEach(q=>q.open=true));
document.getElementById("closeAll").addEventListener("click",()=>qs.forEach(q=>q.open=false));
</script>
</body></html>
"""

assert len(month_1) == len(month_2) == len(month_3) == len(month_4) == len(month_5) == 10
assert html.count('data-question>') == 50
OUT.write_text(html, encoding="utf-8")
print(f"Wrote {OUT}")
