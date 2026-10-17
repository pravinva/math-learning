"""Narrated Manim lesson: following nested loops with if conditions.

Build:
    python make_narration.py
    manim -qm decision_loops.py DecisionLoops
"""

from __future__ import annotations

import json
from pathlib import Path

from manim import *


ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "audio"

BG = "#07131F"
PANEL = "#10243A"
PANEL_2 = "#0B1D30"
INK = "#F4F7FB"
MUTED = "#AFC0D2"
BLUE = "#4EA1FF"
YELLOW = "#FFD166"
GREEN = "#55D6A5"
CORAL = "#FF7B72"
PURPLE = "#B794F4"


class DecisionLoops(Scene):
    def setup(self):
        self.camera.background_color = BG
        self.durations = json.loads((AUDIO / "durations.json").read_text())
        self.caption_box = None
        self.caption_text = None

    def title(self, heading, subheading):
        title = Text(heading, font_size=44, weight=BOLD, color=INK)
        subtitle = Text(subheading, font_size=23, color=MUTED)
        group = VGroup(title, subtitle).arrange(DOWN, buff=0.1)
        group.to_edge(UP, buff=0.24)
        return group

    def set_caption(self, text):
        new_text = Text(text, font_size=23, color=INK)
        new_text.set_max_width(11.7)
        new_text.to_edge(DOWN, buff=0.22)
        box = SurroundingRectangle(
            new_text,
            color="#29445F",
            fill_color=PANEL_2,
            fill_opacity=0.97,
            buff=0.15,
            corner_radius=0.1,
        )
        if self.caption_box is None:
            self.caption_box = box
            self.caption_text = new_text
            self.play(FadeIn(box), FadeIn(new_text), run_time=0.25)
        else:
            self.play(
                Transform(self.caption_box, box),
                Transform(self.caption_text, new_text),
                run_time=0.25,
            )

    def begin_voice(self, key, caption):
        self.add_sound(str(AUDIO / f"{key}.wav"))
        self.set_caption(caption)
        return max(self.durations[key] - 0.25, 0)

    def finish_voice(self, duration, animation_time):
        self.wait(max(duration - animation_time, 0.25))

    def clear_stage(self, *keep):
        protected = {id(item) for item in keep}
        removable = [
            item
            for item in self.mobjects
            if id(item) not in protected
            and item is not self.caption_box
            and item is not self.caption_text
        ]
        if removable:
            self.play(*[FadeOut(item) for item in removable], run_time=0.55)

    def code_block(self, lines, font_size=22):
        texts = VGroup(
            *[
                Text(line, font="Menlo", font_size=font_size, color=INK)
                for line in lines
            ]
        )
        texts.arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        bg = RoundedRectangle(
            corner_radius=0.14,
            width=texts.width + 0.5,
            height=texts.height + 0.42,
            stroke_color="#355574",
            stroke_width=1.5,
            fill_color=PANEL,
            fill_opacity=0.96,
        ).move_to(texts)
        return VGroup(bg, texts), texts

    def bay_grid(self):
        rows = VGroup()
        cells = {}
        for floor in (1, 2):
            label = Text(f"Floor {floor}", font_size=25, color=BLUE)
            row_cells = VGroup()
            for bay in range(1, 5):
                rect = RoundedRectangle(
                    width=1.15,
                    height=0.82,
                    corner_radius=0.1,
                    stroke_color=MUTED,
                    stroke_width=2,
                    fill_color=PANEL,
                    fill_opacity=1,
                )
                number = Text(str(bay), font_size=29, color=INK)
                cell = VGroup(rect, number)
                row_cells.add(cell)
                cells[(floor, bay)] = cell
            row_cells.arrange(RIGHT, buff=0.16)
            row = VGroup(label, row_cells).arrange(RIGHT, buff=0.25)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=RIGHT, buff=0.34)
        return rows, cells

    def construct(self):
        # 1. One instruction at a time
        heading = self.title(
            "How to follow decision loops",
            "Nested for loops with if, continue and break",
        )
        duration = self.begin_voice(
            "intro",
            "Track the current values. Then follow one instruction at a time.",
        )
        nodes = VGroup(
            *[
                VGroup(
                    Circle(radius=0.2, color=color, fill_color=color, fill_opacity=1),
                    Text(label, font_size=24, color=INK),
                ).arrange(DOWN, buff=0.12)
                for label, color in [
                    ("choose value", BLUE),
                    ("ask if", YELLOW),
                    ("do action", GREEN),
                    ("next pass", PURPLE),
                ]
            ]
        ).arrange(RIGHT, buff=0.72).shift(0.25 * UP)
        arrows = VGroup(
            *[
                Arrow(nodes[i][0].get_right(), nodes[i + 1][0].get_left(), buff=0.12, color=MUTED)
                for i in range(3)
            ]
        )
        pointer = Triangle(color=CORAL, fill_color=CORAL, fill_opacity=1).scale(0.11)
        pointer.rotate(-PI / 2).next_to(nodes[0][0], UP, buff=0.13)
        self.play(Write(heading), run_time=1.0)
        self.play(FadeIn(nodes), GrowArrow(arrows[0]), GrowArrow(arrows[1]), GrowArrow(arrows[2]), run_time=1.3)
        self.play(
            Succession(
                pointer.animate.next_to(nodes[1][0], UP, buff=0.13),
                pointer.animate.next_to(nodes[2][0], UP, buff=0.13),
                pointer.animate.next_to(nodes[3][0], UP, buff=0.13),
            ),
            run_time=2.0,
        )
        self.finish_voice(duration, 4.3)

        # 2. A single loop with an if decision
        self.clear_stage()
        heading = self.title("First: one loop", "The if question is asked again on every pass")
        code, code_lines = self.code_block(
            [
                "for bay = 1:4",
                "    if bay == 2",
                "        continue",
                "    end",
                "    disp(bay)",
                "end",
            ],
            font_size=23,
        )
        code.to_edge(LEFT, buff=0.55).shift(0.15 * UP)
        bay_cells = VGroup()
        for value in range(1, 5):
            square = RoundedRectangle(
                width=1.05,
                height=0.85,
                corner_radius=0.1,
                color=MUTED,
                fill_color=PANEL,
                fill_opacity=1,
            )
            number = Text(str(value), font_size=31, color=INK)
            bay_cells.add(VGroup(square, number))
        bay_cells.arrange(RIGHT, buff=0.2).to_edge(RIGHT, buff=0.55).shift(0.35 * UP)
        labels = VGroup(
            Text("use", font_size=20, color=GREEN),
            Text("skip", font_size=20, color=CORAL),
            Text("use", font_size=20, color=GREEN),
            Text("use", font_size=20, color=GREEN),
        )
        for label, cell in zip(labels, bay_cells):
            label.next_to(cell, DOWN, buff=0.13)
        cursor = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.11)
        cursor.rotate(PI).next_to(bay_cells[0], UP, buff=0.13)
        duration = self.begin_voice(
            "single_if",
            "Each new bay reaches the if statement and receives a fresh true/false answer.",
        )
        self.play(Write(heading), FadeIn(code), FadeIn(bay_cells), FadeIn(cursor), run_time=1.5)
        self.play(
            Succession(
                bay_cells[0][0].animate.set_stroke(GREEN, width=4),
                cursor.animate.next_to(bay_cells[1], UP, buff=0.13),
                bay_cells[1][0].animate.set_stroke(CORAL, width=4).set_fill("#3A1D26"),
                cursor.animate.next_to(bay_cells[2], UP, buff=0.13),
                bay_cells[2][0].animate.set_stroke(GREEN, width=4),
                cursor.animate.next_to(bay_cells[3], UP, buff=0.13),
                bay_cells[3][0].animate.set_stroke(GREEN, width=4),
            ),
            run_time=4.4,
        )
        self.play(FadeIn(labels), run_time=0.6)
        self.finish_voice(duration, 6.5)

        # 3. The odometer model for nesting
        self.clear_stage()
        heading = self.title("Now nest the loops", "Outer floor stays fixed while inner bay runs")
        grid, cells = self.bay_grid()
        grid.shift(0.1 * DOWN)
        floor_counter = VGroup(
            Text("outer", font_size=19, color=MUTED),
            Text("floor = 1", font="Menlo", font_size=30, color=BLUE),
        ).arrange(DOWN, buff=0.1)
        bay_counter = VGroup(
            Text("inner", font_size=19, color=MUTED),
            Text("bay = 1", font="Menlo", font_size=30, color=YELLOW),
        ).arrange(DOWN, buff=0.1)
        counters = VGroup(floor_counter, bay_counter).arrange(RIGHT, buff=1.0)
        counters.next_to(grid, UP, buff=0.35)
        pointer = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.1)
        pointer.rotate(-PI / 2).next_to(cells[(1, 1)], LEFT, buff=0.12)
        duration = self.begin_voice(
            "nested",
            "Think of two wheels: floor changes slowly; bay runs through all its values.",
        )
        self.play(Write(heading), FadeIn(grid), FadeIn(counters), FadeIn(pointer), run_time=1.5)
        self.play(
            Succession(
                pointer.animate.next_to(cells[(1, 2)], LEFT, buff=0.12),
                pointer.animate.next_to(cells[(1, 3)], LEFT, buff=0.12),
                pointer.animate.next_to(cells[(1, 4)], LEFT, buff=0.12),
            ),
            run_time=2.4,
        )
        new_floor = Text("floor = 2", font="Menlo", font_size=30, color=BLUE).move_to(floor_counter[1])
        self.play(
            Transform(floor_counter[1], new_floor),
            pointer.animate.next_to(cells[(2, 1)], LEFT, buff=0.12),
            run_time=1.0,
        )
        self.play(
            Succession(
                pointer.animate.next_to(cells[(2, 2)], LEFT, buff=0.12),
                pointer.animate.next_to(cells[(2, 3)], LEFT, buff=0.12),
                pointer.animate.next_to(cells[(2, 4)], LEFT, buff=0.12),
            ),
            run_time=2.4,
        )
        self.finish_voice(duration, 7.3)

        # 4. Put the complete code beside the grid
        self.clear_stage()
        heading = self.title("Read from the outside in", "Return to the inner for line after each completed pass")
        code, code_lines = self.code_block(
            [
                "for floor = 1:2",
                "  for bay = 1:4",
                "    if bay == 2",
                "      continue",
                "    end",
                "    if floor == 2 && bay == 3",
                "      disp('Truck! Leaving floor 2')",
                "      break",
                "    end",
                "    disp([floor bay])",
                "  end",
                "end",
            ],
            font_size=18,
        )
        code.to_edge(LEFT, buff=0.35).shift(0.1 * UP)
        grid, cells = self.bay_grid()
        grid.scale(0.85).to_edge(RIGHT, buff=0.35).shift(0.15 * UP)
        line_marker = SurroundingRectangle(
            code_lines[0], color=YELLOW, fill_color=YELLOW, fill_opacity=0.1, buff=0.05
        )
        duration = self.begin_voice(
            "read_code",
            "Choose floor, choose bay, test each if in order, perform the action, then loop back.",
        )
        self.play(Write(heading), FadeIn(code), FadeIn(grid), Create(line_marker), run_time=1.5)
        for index in [1, 2, 5, 9, 10, 1]:
            target = SurroundingRectangle(
                code_lines[index],
                color=YELLOW,
                fill_color=YELLOW,
                fill_opacity=0.1,
                buff=0.05,
            )
            self.play(Transform(line_marker, target), run_time=0.55)
        self.finish_voice(duration, 4.8)

        # 5. Trace floor one
        pointer = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.09)
        pointer.rotate(-PI / 2).next_to(cells[(1, 1)], LEFT, buff=0.1)
        output = VGroup(
            Text("OUTPUT", font_size=20, color=MUTED),
            Text("", font="Menlo", font_size=21, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        output[0].move_to([3.0, -1.75, 0])
        duration = self.begin_voice(
            "floor_one",
            "Floor 1 path: display bay 1; skip bay 2; display bays 3 and 4.",
        )
        self.play(FadeIn(pointer), FadeIn(output[0]), run_time=0.5)
        lines = []
        animation_time = 0.5
        for bay, action, color in [
            (1, "     1     1", GREEN),
            (2, None, CORAL),
            (3, "     1     3", GREEN),
            (4, "     1     4", GREEN),
        ]:
            self.play(pointer.animate.next_to(cells[(1, bay)], LEFT, buff=0.1), run_time=0.35)
            self.play(cells[(1, bay)][0].animate.set_stroke(color, width=4), run_time=0.35)
            animation_time += 0.7
            if action:
                lines.append(action)
                new_output = Text("\n".join(lines), font="Menlo", font_size=20, color=GREEN)
                new_output.next_to(output[0], DOWN, aligned_edge=LEFT, buff=0.1)
                self.play(Transform(output[1], new_output), run_time=0.35)
                animation_time += 0.35
            else:
                skip = Text("continue → next bay", font_size=18, color=CORAL)
                skip.next_to(cells[(1, 2)], DOWN, buff=0.1)
                self.play(FadeIn(skip), run_time=0.25)
                self.play(FadeOut(skip), run_time=0.25)
                animation_time += 0.5
        self.finish_voice(duration, animation_time)

        # 6. Trace floor two and break
        duration = self.begin_voice(
            "floor_two",
            "Floor 2 path: display bay 1; skip bay 2; truck at bay 3; break before bay 4.",
        )
        animation_time = 0
        for bay, action, color in [
            (1, "     2     1", GREEN),
            (2, None, CORAL),
            (3, "Truck! Leaving floor 2", YELLOW),
        ]:
            self.play(pointer.animate.next_to(cells[(2, bay)], LEFT, buff=0.1), run_time=0.4)
            self.play(cells[(2, bay)][0].animate.set_stroke(color, width=4), run_time=0.4)
            animation_time += 0.8
            if action:
                lines.append(action)
                new_output = Text("\n".join(lines), font="Menlo", font_size=17, color=GREEN)
                new_output.next_to(output[0], DOWN, aligned_edge=LEFT, buff=0.08)
                self.play(Transform(output[1], new_output), run_time=0.4)
                animation_time += 0.4
        cross = Cross(cells[(2, 4)], stroke_color=CORAL, stroke_width=5)
        never = Text("never reached", font_size=17, color=CORAL).next_to(cells[(2, 4)], DOWN, buff=0.08)
        self.play(Create(cross), FadeIn(never), run_time=0.7)
        break_arrow = CurvedArrow(
            code_lines[7].get_right(),
            code_lines[10].get_right(),
            angle=-PI / 2,
            color=CORAL,
        )
        self.play(Create(break_arrow), run_time=0.7)
        animation_time += 1.4
        self.finish_voice(duration, animation_time)

        # 7. Compare the two control commands
        self.clear_stage()
        heading = self.title("continue is not break", "Both change the normal path, but in different ways")
        continue_word = Text("continue", font="Menlo", font_size=38, color=CORAL)
        continue_desc = Text(
            "Skip the rest of this pass\nThen try the next bay",
            font_size=25,
            color=INK,
            line_spacing=1.15,
        )
        continue_card = VGroup(continue_word, continue_desc).arrange(DOWN, buff=0.28)
        continue_box = SurroundingRectangle(
            continue_card, color=CORAL, fill_color=PANEL, fill_opacity=1, buff=0.35, corner_radius=0.15
        )
        continue_group = VGroup(continue_box, continue_card)

        break_word = Text("break", font="Menlo", font_size=38, color=YELLOW)
        break_desc = Text(
            "End the nearest loop\nDo not try another bay",
            font_size=25,
            color=INK,
            line_spacing=1.15,
        )
        break_card = VGroup(break_word, break_desc).arrange(DOWN, buff=0.28)
        break_box = SurroundingRectangle(
            break_card, color=YELLOW, fill_color=PANEL, fill_opacity=1, buff=0.35, corner_radius=0.15
        )
        break_group = VGroup(break_box, break_card)
        cards = VGroup(continue_group, break_group).arrange(RIGHT, buff=0.7).shift(0.15 * UP)
        nearest = Text(
            "In nested loops, break leaves the loop directly around it.",
            font_size=24,
            color=PURPLE,
        ).next_to(cards, DOWN, buff=0.38)
        duration = self.begin_voice(
            "controls",
            "continue = next pass.  break = leave the nearest loop.",
        )
        self.play(Write(heading), FadeIn(continue_group, shift=0.2 * RIGHT), run_time=1.2)
        self.play(FadeIn(break_group, shift=0.2 * LEFT), run_time=1.0)
        self.play(Write(nearest), run_time=0.8)
        self.play(Indicate(continue_word, color=CORAL), Indicate(break_word, color=YELLOW), run_time=1.0)
        self.finish_voice(duration, 4.0)

        # 8. The paper tracing method
        self.clear_stage()
        heading = self.title("Trace attempted pairs on paper", "One row for each pass that actually begins")
        headers = ["floor", "bay", "condition result", "action"]
        data = [
            ["1", "1", "neither true", "display 1  1"],
            ["1", "2", "bay == 2", "continue"],
            ["1", "3", "neither true", "display 1  3"],
            ["1", "4", "neither true", "display 1  4"],
            ["2", "1", "neither true", "display 2  1"],
            ["2", "2", "bay == 2", "continue"],
            ["2", "3", "truck condition", "message; break"],
        ]
        table = Table(
            data,
            col_labels=[Text(h, font_size=21, color=BLUE) for h in headers],
            include_outer_lines=True,
            line_config={"color": "#355574", "stroke_width": 1.3},
            element_to_mobject_config={"font_size": 19, "color": INK},
            h_buff=0.35,
            v_buff=0.16,
        ).scale(0.82).shift(0.12 * UP)
        missing = Text("(2, 4) is absent: that pass never starts", font_size=23, color=CORAL)
        missing.next_to(table, DOWN, buff=0.2)
        duration = self.begin_voice(
            "trace",
            "Write only attempted pairs. Evaluate conditions before recording the action.",
        )
        self.play(Write(heading), Create(table.get_horizontal_lines()), Create(table.get_vertical_lines()), run_time=1.1)
        self.play(FadeIn(table.get_entries()), run_time=1.2)
        self.play(Write(missing), run_time=0.8)
        self.play(Indicate(table.get_rows()[-1], color=YELLOW), Indicate(missing, color=CORAL), run_time=1.0)
        self.finish_voice(duration, 4.1)

        # 9. Final rhythm
        self.clear_stage()
        heading = self.title("The tracing rhythm", "Slow the program down in your mind")
        steps = VGroup()
        for index, (text, color) in enumerate(
            [
                ("Fix one outer value", BLUE),
                ("Run inner values in order", YELLOW),
                ("Test each if top to bottom", PURPLE),
                ("Record continue or break", CORAL),
            ],
            start=1,
        ):
            circle = Circle(radius=0.26, color=color, fill_color=color, fill_opacity=1)
            number = Text(str(index), font_size=22, weight=BOLD, color=BG).move_to(circle)
            badge = VGroup(circle, number)
            label = Text(text, font_size=25, color=INK)
            steps.add(VGroup(badge, label).arrange(RIGHT, buff=0.25))
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(0.05 * UP)
        duration = self.begin_voice(
            "recap",
            "Outer value fixed. Inner values in order. Test each if. Record the action.",
        )
        self.play(Write(heading), run_time=0.8)
        for step in steps:
            self.play(FadeIn(step, shift=0.18 * RIGHT), run_time=0.55)
        check = Text("You are tracing a path—not solving everything at once.", font_size=27, color=GREEN)
        check.next_to(steps, DOWN, buff=0.38)
        self.play(Write(check), run_time=0.9)
        self.finish_voice(duration, 3.9)
        self.wait(0.5)
