"""Manim examples for recognising and choosing integration methods.

Render all three scenes with:

    manim -qm integration_intuition.py \
        DerivativeFingerprints SubstitutionAsRescaling IntegrationByPartsFromProductRule
"""

from manim import *


BG = "#081421"
INK = "#F4F7FB"
MUTED = "#A9B7C8"
BLUE = "#4EA1FF"
YELLOW = "#FFD166"
GREEN = "#55D6A5"
CORAL = "#FF7B72"
PURPLE = "#B794F4"


class IntegrationScene(Scene):
    def setup(self):
        self.camera.background_color = BG

    def heading(self, title, subtitle):
        heading = Text(title, font_size=46, weight=BOLD, color=INK)
        heading.to_edge(UP, buff=0.32)
        sub = Text(subtitle, font_size=24, color=MUTED)
        sub.next_to(heading, DOWN, buff=0.12)
        self.play(Write(heading), FadeIn(sub, shift=0.15 * DOWN))
        return VGroup(heading, sub)

    def rule_card(self, formula, cue, color=BLUE):
        expression = MathTex(formula, font_size=38, color=INK)
        cue_text = Text(cue, font_size=26, color=MUTED)
        cue_text.next_to(expression, DOWN, buff=0.16)
        card = VGroup(expression, cue_text)
        box = SurroundingRectangle(
            card, color=color, fill_color="#10243A", fill_opacity=0.72,
            buff=0.24, corner_radius=0.14,
        )
        return VGroup(box, card)


class DerivativeFingerprints(IntegrationScene):
    """A logarithmic primitive recognised from its derivative."""

    def construct(self):
        title = self.heading(
            "Recognising derivative fingerprints",
            "Match the integrand to a derivative you already know",
        )

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 2.5, 0.5],
            x_length=5.6,
            y_length=3.25,
            axis_config={"color": MUTED, "stroke_width": 1.5},
            tips=False,
        ).to_edge(LEFT, buff=0.55).shift(0.42 * DOWN)
        curve = axes.plot(lambda x: np.log(x * x + 1), color=BLUE, stroke_width=4)
        graph_label = MathTex(r"F(x)=\ln(x^2+1)", color=BLUE, font_size=30)
        graph_label.next_to(axes, DOWN, buff=0.15)

        integral = MathTex(
            r"\int", r"\frac{2x}{x^2+1}", r"\,dx",
            font_size=48, color=INK,
        ).to_edge(RIGHT, buff=0.75).shift(1.05 * UP)
        integral.set_color_by_tex("2x", YELLOW)
        integral.set_color_by_tex("x^2+1", BLUE)

        inner = MathTex(r"g(x)=x^2+1", font_size=33, color=BLUE)
        derivative = MathTex(r"g'(x)=2x", font_size=33, color=YELLOW)
        pair = VGroup(inner, derivative).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        pair.next_to(integral, DOWN, buff=0.38)

        fingerprint = self.rule_card(
            r"\frac{g'(x)}{g(x)}\ \longrightarrow\ \ln|g(x)|+C",
            "denominator + its derivative",
            GREEN,
        )
        fingerprint.scale(0.82).next_to(pair, DOWN, buff=0.38)

        self.play(Create(axes), Create(curve), FadeIn(graph_label))
        self.play(Write(integral))
        self.play(
            Indicate(integral[1], color=PURPLE),
            FadeIn(inner, shift=0.12 * DOWN),
            FadeIn(derivative, shift=0.12 * DOWN),
        )
        self.play(FadeIn(fingerprint, shift=0.18 * UP))
        self.wait(0.8)

        answer = MathTex(
            r"\int\frac{2x}{x^2+1}\,dx",
            r"=",
            r"\ln(x^2+1)+C",
            font_size=45,
        )
        answer.set_color_by_tex("2x", YELLOW)
        answer.set_color_by_tex("x^2+1", BLUE)
        answer.set_color_by_tex(r"\ln", GREEN)
        answer.to_edge(RIGHT, buff=0.45).shift(1.35 * DOWN)
        self.play(FadeOut(graph_label), Write(answer))

        verify = MathTex(
            r"\frac{d}{dx}\ln(x^2+1)=\frac{2x}{x^2+1}",
            font_size=34, color=GREEN,
        ).move_to(integral)
        self.play(
            FadeOut(integral),
            FadeOut(pair),
            FadeOut(fingerprint),
            FadeIn(verify, shift=0.2 * UP),
        )
        check = Text("Differentiate to verify", font_size=22, color=GREEN)
        check.next_to(verify, DOWN, buff=0.2)
        self.play(FadeIn(check))
        self.wait(2)


class SubstitutionAsRescaling(IntegrationScene):
    """Substitution shown as a change of horizontal measuring scale."""

    def construct(self):
        title = self.heading(
            "Substitution",
            "Rename a repeated inner quantity and carry its differential",
        )

        x_line = NumberLine(
            x_range=[0, 2, 0.5], length=3,
            color=MUTED, include_numbers=True, font_size=24,
        ).shift(1.65 * UP)
        u_line = NumberLine(
            x_range=[1, 5, 1], length=6,
            color=MUTED, include_numbers=True, font_size=24,
        ).shift(0.15 * UP)
        x_name = MathTex("x", color=YELLOW).next_to(x_line, LEFT, buff=0.25)
        u_name = MathTex(r"u=x^2+1", color=BLUE).next_to(u_line, LEFT, buff=0.25)

        tracker = ValueTracker(0)
        x_dot = always_redraw(
            lambda: Dot(x_line.n2p(tracker.get_value()), color=YELLOW, radius=0.08)
        )
        u_dot = always_redraw(
            lambda: Dot(
                u_line.n2p(tracker.get_value() ** 2 + 1),
                color=BLUE,
                radius=0.08,
            )
        )
        mapping = CurvedArrow(
            x_line.n2p(1.05) + 0.08 * DOWN,
            u_line.n2p(2.1) + 0.08 * UP,
            color=PURPLE,
            angle=-TAU / 8,
        )
        rate = MathTex(r"du=2x\,dx", color=YELLOW, font_size=30)
        rate.next_to(mapping, RIGHT, buff=0.15)

        self.play(Create(x_line), Create(u_line), FadeIn(x_name), FadeIn(u_name))
        self.add(x_dot, u_dot)
        self.play(Create(mapping), FadeIn(rate))
        self.play(tracker.animate.set_value(2), run_time=2.6, rate_func=smooth)
        self.wait(0.4)

        visual = VGroup(x_line, u_line, x_name, u_name, mapping, rate)
        self.play(visual.animate.scale(0.78).to_edge(LEFT, buff=0.45).shift(0.2 * UP))

        steps = VGroup(
            MathTex(
                r"\int 2x\cos(x^2+1)\,dx",
                font_size=39,
            ),
            MathTex(
                r"u=x^2+1,\qquad du=2x\,dx",
                font_size=34,
            ),
            MathTex(
                r"\int\cos u\,du=\sin u+C",
                font_size=37,
            ),
            MathTex(
                r"\boxed{\sin(x^2+1)+C}",
                font_size=40,
                color=GREEN,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.to_edge(RIGHT, buff=0.5).shift(0.28 * DOWN)
        steps[0].set_color_by_tex("2x", YELLOW)
        steps[0].set_color_by_tex("x^2+1", BLUE)
        steps[1].set_color_by_tex("u", BLUE)
        steps[1].set_color_by_tex("2x", YELLOW)

        self.play(Write(steps[0]))
        self.play(TransformFromCopy(steps[0], steps[1]))
        self.play(TransformFromCopy(steps[1], steps[2]))
        self.play(TransformFromCopy(steps[2], steps[3]))

        verify = MathTex(
            r"\frac{d}{dx}\sin(x^2+1)=2x\cos(x^2+1)",
            font_size=34, color=GREEN,
        ).to_edge(DOWN, buff=1.7)
        self.play(Write(verify))
        self.wait(2)


class IntegrationByPartsFromProductRule(IntegrationScene):
    """Integration by parts derived from the product rule."""

    def construct(self):
        title = self.heading(
            "Integration by parts",
            "The product rule rearranged for antiderivatives",
        )

        product = MathTex(
            r"d(uv)", r"=", r"u\,dv", r"+", r"v\,du",
            font_size=48,
        ).shift(1.7 * UP)
        product.set_color_by_tex("u", BLUE)
        product.set_color_by_tex("v", YELLOW)
        self.play(Write(product))

        rearranged = MathTex(
            r"u\,dv", r"=", r"d(uv)", r"-", r"v\,du",
            font_size=48,
        ).move_to(product)
        rearranged.set_color_by_tex("u", BLUE)
        rearranged.set_color_by_tex("v", YELLOW)
        self.play(TransformMatchingTex(product, rearranged))

        rule = MathTex(
            r"\boxed{\int u\,dv=uv-\int v\,du+C}",
            font_size=48, color=GREEN,
        ).move_to(rearranged)
        self.play(TransformMatchingTex(rearranged, rule))
        cue = Text(
            "Choose u so du is simpler, and dv so v is easy to find",
            font_size=28, color=MUTED,
        ).next_to(rule, DOWN, buff=0.22)
        self.play(FadeIn(cue))

        self.play(VGroup(rule, cue).animate.scale(0.78).to_edge(LEFT, buff=0.55))

        example = MathTex(r"\int x e^x\,dx", font_size=44)
        choices = MathTex(
            r"u=x,\quad dv=e^x\,dx",
            r"\qquad",
            r"du=dx,\quad v=e^x",
            font_size=32,
        )
        working = MathTex(
            r"\int xe^x\,dx",
            r"=",
            r"xe^x",
            r"-",
            r"\int e^x\,dx",
            font_size=38,
        )
        result = MathTex(
            r"\boxed{e^x(x-1)+C}",
            font_size=43, color=GREEN,
        )
        stack = VGroup(example, choices, working, result)
        stack.arrange(DOWN, aligned_edge=LEFT, buff=0.34)
        stack.to_edge(RIGHT, buff=0.55).shift(0.25 * DOWN)
        choices.set_color_by_tex("u=x", BLUE)
        choices.set_color_by_tex("v=e^x", YELLOW)
        working.set_color_by_tex("x", BLUE)
        working.set_color_by_tex("e^x", YELLOW)

        self.play(Write(example))
        self.play(FadeIn(choices, shift=0.15 * UP))
        self.play(TransformFromCopy(example, working))
        self.play(Write(result))

        verify = MathTex(
            r"\frac{d}{dx}\!\left[e^x(x-1)\right]=xe^x",
            font_size=34, color=GREEN,
        ).to_edge(LEFT, buff=0.75).shift(1.65 * DOWN)
        self.play(Write(verify))
        self.wait(2)
