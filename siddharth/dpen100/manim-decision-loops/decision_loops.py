"""Narrated Manim lesson: following nested loops with if conditions.

Build:
    python make_narration.py
    manim -qm --disable_caching decision_loops.py DecisionLoops
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
        self.voice_cues = []

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
            self.play(FadeIn(box), FadeIn(new_text), run_time=0.3)
        else:
            self.play(
                Transform(self.caption_box, box),
                Transform(self.caption_text, new_text),
                run_time=0.3,
            )

    def speak(self, key, caption):
        cue_time = float(getattr(self.renderer, "time", 0.0) or 0.0)
        self.voice_cues.append({"key": key, "t": round(cue_time, 3)})
        (AUDIO / "cues.json").write_text(json.dumps(self.voice_cues, indent=2) + "\n")
        wav = AUDIO / f"{key}.wav"
        if wav.is_file():
            self.add_sound(str(wav))
        self.set_caption(caption)
        return max(self.durations[key] - 0.3, 0.5)

    def hold(self, duration, used):
        self.wait(max(duration - used, 0.35))

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

    def sync_step(self, line_marker, code_lines, line_index, extra_anims=None, run_time=0.8, color=YELLOW):
        target = SurroundingRectangle(
            code_lines[line_index],
            color=color,
            fill_color=color,
            fill_opacity=0.12,
            buff=0.05,
        )
        anims = [Transform(line_marker, target)]
        if extra_anims:
            anims.extend(extra_anims)
        self.play(*anims, run_time=run_time)
        return run_time

    def code_block(self, lines, font_size=22):
        stripped = [line.lstrip(" ") or " " for line in lines]
        indents = [len(line) - len(line.lstrip(" ")) for line in lines]
        texts = VGroup(
            *[
                Text(body, font="Menlo", font_size=font_size, color=INK)
                for body in stripped
            ]
        )
        texts.arrange(DOWN, aligned_edge=LEFT, buff=0.13)
        unit = Text("0", font="Menlo", font_size=font_size).width
        for mob, n in zip(texts, indents):
            mob.shift(RIGHT * n * unit)
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
        heading = self.title(
            "How to follow decision loops",
            "Nested for loops with if, continue and break",
        )
        duration = self.speak(
            "intro",
            "One instruction at a time. Trace each pass in order.",
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
        self.play(Write(heading), run_time=1.4)
        self.play(FadeIn(nodes), GrowArrow(arrows[0]), GrowArrow(arrows[1]), GrowArrow(arrows[2]), run_time=1.6)
        self.play(
            Succession(
                pointer.animate.next_to(nodes[1][0], UP, buff=0.13),
                pointer.animate.next_to(nodes[2][0], UP, buff=0.13),
                pointer.animate.next_to(nodes[3][0], UP, buff=0.13),
            ),
            run_time=3.2,
        )
        self.hold(duration, 6.2)

        # 2. One loop, pass by pass
        self.clear_stage()
        heading = self.title("First: one loop", "Walk each pass. Ask the if again every time.")
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
        marker = SurroundingRectangle(
            code_lines[0], color=YELLOW, fill_color=YELLOW, fill_opacity=0.12, buff=0.05
        )
        duration = self.speak(
            "single_intro",
            "Bay will be 1, then 2, then 3, then 4. The if is asked every pass.",
        )
        self.play(Write(heading), FadeIn(code), FadeIn(bay_cells), FadeIn(cursor), Create(marker), run_time=2.0)
        self.hold(duration, 2.0)

        duration = self.speak("single_bay1", "Pass 1. Bay is 1. If is false. Display 1.")
        used = 0
        used += self.sync_step(marker, code_lines, 1, extra_anims=[cursor.animate.next_to(bay_cells[0], UP, buff=0.13)], run_time=1.1)
        used += self.sync_step(
            marker, code_lines, 4,
            extra_anims=[bay_cells[0][0].animate.set_stroke(GREEN, width=4)],
            run_time=1.2, color=GREEN,
        )
        self.play(FadeIn(labels[0]), run_time=0.4)
        used += 0.4
        self.hold(duration, used)

        duration = self.speak("single_bay2", "Pass 2. Bay is 2. Continue skips display.")
        used = 0
        used += self.sync_step(marker, code_lines, 1, extra_anims=[cursor.animate.next_to(bay_cells[1], UP, buff=0.13)], run_time=1.1)
        used += self.sync_step(
            marker, code_lines, 2,
            extra_anims=[bay_cells[1][0].animate.set_stroke(CORAL, width=4).set_fill("#3A1D26")],
            run_time=1.3, color=CORAL,
        )
        skip = Text("continue → next bay", font_size=18, color=CORAL)
        skip.next_to(bay_cells[1], DOWN, buff=0.42)
        self.play(FadeIn(labels[1]), FadeIn(skip), run_time=0.5)
        used += 0.5
        self.play(FadeOut(skip), run_time=0.4)
        used += 0.4
        used += self.sync_step(marker, code_lines, 0, run_time=0.9)
        self.hold(duration, used)

        duration = self.speak("single_bay3", "Pass 3. Bay is 3. Display 3.")
        used = 0
        used += self.sync_step(marker, code_lines, 1, extra_anims=[cursor.animate.next_to(bay_cells[2], UP, buff=0.13)], run_time=1.1)
        used += self.sync_step(
            marker, code_lines, 4,
            extra_anims=[bay_cells[2][0].animate.set_stroke(GREEN, width=4)],
            run_time=1.2, color=GREEN,
        )
        self.play(FadeIn(labels[2]), run_time=0.4)
        used += 0.4
        self.hold(duration, used)

        duration = self.speak("single_bay4", "Pass 4. Bay is 4. Display 4. The loop ends.")
        used = 0
        used += self.sync_step(marker, code_lines, 1, extra_anims=[cursor.animate.next_to(bay_cells[3], UP, buff=0.13)], run_time=1.1)
        used += self.sync_step(
            marker, code_lines, 4,
            extra_anims=[bay_cells[3][0].animate.set_stroke(GREEN, width=4)],
            run_time=1.2, color=GREEN,
        )
        self.play(FadeIn(labels[3]), run_time=0.4)
        used += 0.4
        used += self.sync_step(marker, code_lines, 5, run_time=1.0)
        self.hold(duration, used)

        # 3. Nested loops, floor by floor
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
        duration = self.speak(
            "nested_intro",
            "Floor is the outer wheel. Bay is the inner wheel.",
        )
        self.play(Write(heading), FadeIn(grid), FadeIn(counters), FadeIn(pointer), run_time=2.0)
        self.hold(duration, 2.0)

        duration = self.speak(
            "nested_floor1",
            "Floor stays 1. Inner loop visits bay 1, 2, 3, then 4.",
        )
        used = 0
        for bay in (1, 2, 3, 4):
            bay_text = Text(f"bay = {bay}", font="Menlo", font_size=30, color=YELLOW).move_to(bay_counter[1])
            used_step = 1.15
            self.play(
                pointer.animate.next_to(cells[(1, bay)], LEFT, buff=0.12),
                Transform(bay_counter[1], bay_text),
                cells[(1, bay)][0].animate.set_stroke(YELLOW, width=4),
                run_time=used_step,
            )
            used += used_step
        self.hold(duration, used)

        duration = self.speak(
            "nested_floor2",
            "Inner loop finished. Floor becomes 2. Bay starts again at 1.",
        )
        used = 0
        new_floor = Text("floor = 2", font="Menlo", font_size=30, color=BLUE).move_to(floor_counter[1])
        reset_bay = Text("bay = 1", font="Menlo", font_size=30, color=YELLOW).move_to(bay_counter[1])
        self.play(
            Transform(floor_counter[1], new_floor),
            Transform(bay_counter[1], reset_bay),
            pointer.animate.next_to(cells[(2, 1)], LEFT, buff=0.12),
            run_time=1.4,
        )
        used += 1.4
        for bay in (1, 2, 3, 4):
            bay_text = Text(f"bay = {bay}", font="Menlo", font_size=30, color=YELLOW).move_to(bay_counter[1])
            self.play(
                pointer.animate.next_to(cells[(2, bay)], LEFT, buff=0.12),
                Transform(bay_counter[1], bay_text),
                cells[(2, bay)][0].animate.set_stroke(YELLOW, width=4),
                run_time=1.15,
            )
            used += 1.15
        self.hold(duration, used)

        # 4–6. Full code, then each attempted pair
        self.clear_stage()
        heading = self.title("Read from the outside in", "Then walk every inner pass, one bay at a time")
        code, code_lines = self.code_block(
            [
                "for floor = 1:2",
                "    for bay = 1:4",
                "        if bay == 2",
                "            continue",
                "        end",
                "        if floor == 2 && bay == 3",
                "            disp('Truck! Leaving floor 2')",
                "            break",
                "        end",
                "        disp([floor bay])",
                "    end",
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
        pointer = Triangle(color=YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.09)
        pointer.rotate(-PI / 2).next_to(cells[(1, 1)], LEFT, buff=0.1)
        L_FOR_FLOOR, L_FOR_BAY = 0, 1
        L_IF_BAY2, L_CONTINUE = 2, 3
        L_IF_TRUCK, L_DISP_TRUCK, L_BREAK = 5, 6, 7
        L_DISP_PAIR, L_END_BAY = 9, 10
        duration = self.speak(
            "read_code",
            "Choose floor. Choose bay. Test each if. Then loop back to the inner for.",
        )
        self.play(Write(heading), FadeIn(code), FadeIn(grid), FadeIn(pointer), Create(line_marker), run_time=2.0)
        used = 2.0
        used += self.sync_step(line_marker, code_lines, L_FOR_FLOOR, run_time=1.1)
        used += self.sync_step(line_marker, code_lines, L_FOR_BAY, run_time=1.1)
        used += self.sync_step(line_marker, code_lines, L_IF_BAY2, run_time=1.1)
        used += self.sync_step(line_marker, code_lines, L_IF_TRUCK, run_time=1.1)
        used += self.sync_step(line_marker, code_lines, L_DISP_PAIR, run_time=1.1, color=GREEN)
        used += self.sync_step(line_marker, code_lines, L_END_BAY, run_time=1.0)
        used += self.sync_step(line_marker, code_lines, L_FOR_BAY, run_time=1.0)
        self.hold(duration, used)

        output = VGroup(
            Text("OUTPUT", font_size=20, color=MUTED),
            Text("", font="Menlo", font_size=21, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        output[0].move_to([3.0, -1.75, 0])
        lines = []
        self.play(FadeIn(output[0]), run_time=0.4)

        def show_output(text, size=20):
            lines.append(text)
            new_output = Text("\n".join(lines), font="Menlo", font_size=size, color=GREEN)
            new_output.next_to(output[0], DOWN, aligned_edge=LEFT, buff=0.1)
            self.play(Transform(output[1], new_output), run_time=0.55)
            return 0.55

        duration = self.speak("f1_bay1", "Floor 1, bay 1. Display 1 1.")
        used = self.sync_step(line_marker, code_lines, L_FOR_BAY, extra_anims=[pointer.animate.next_to(cells[(1, 1)], LEFT, buff=0.1)], run_time=0.9)
        used += self.sync_step(line_marker, code_lines, L_IF_BAY2, run_time=0.9)
        used += self.sync_step(line_marker, code_lines, L_IF_TRUCK, run_time=0.9)
        used += self.sync_step(
            line_marker, code_lines, L_DISP_PAIR,
            extra_anims=[cells[(1, 1)][0].animate.set_stroke(GREEN, width=4)],
            run_time=1.1, color=GREEN,
        )
        used += show_output("     1     1")
        self.hold(duration, used)

        duration = self.speak("f1_bay2", "Floor 1, bay 2. Continue. Skip display.")
        used = self.sync_step(line_marker, code_lines, L_FOR_BAY, extra_anims=[pointer.animate.next_to(cells[(1, 2)], LEFT, buff=0.1)], run_time=0.9)
        used += self.sync_step(
            line_marker, code_lines, L_IF_BAY2,
            extra_anims=[cells[(1, 2)][0].animate.set_stroke(CORAL, width=4).set_fill("#3A1D26")],
            run_time=1.0,
        )
        used += self.sync_step(line_marker, code_lines, L_CONTINUE, run_time=1.2, color=CORAL)
        skip = Text("continue → next bay", font_size=18, color=CORAL).next_to(cells[(1, 2)], DOWN, buff=0.1)
        self.play(FadeIn(skip), run_time=0.45)
        self.play(FadeOut(skip), run_time=0.4)
        used += 0.85
        self.hold(duration, used)

        duration = self.speak("f1_bay3", "Floor 1, bay 3. Display 1 3.")
        used = self.sync_step(line_marker, code_lines, L_FOR_BAY, extra_anims=[pointer.animate.next_to(cells[(1, 3)], LEFT, buff=0.1)], run_time=0.9)
        used += self.sync_step(line_marker, code_lines, L_IF_BAY2, run_time=0.85)
        used += self.sync_step(line_marker, code_lines, L_IF_TRUCK, run_time=0.85)
        used += self.sync_step(
            line_marker, code_lines, L_DISP_PAIR,
            extra_anims=[cells[(1, 3)][0].animate.set_stroke(GREEN, width=4)],
            run_time=1.1, color=GREEN,
        )
        used += show_output("     1     3")
        self.hold(duration, used)

        duration = self.speak("f1_bay4", "Floor 1, bay 4. Display 1 4. Inner loop done.")
        used = self.sync_step(line_marker, code_lines, L_FOR_BAY, extra_anims=[pointer.animate.next_to(cells[(1, 4)], LEFT, buff=0.1)], run_time=0.9)
        used += self.sync_step(line_marker, code_lines, L_IF_BAY2, run_time=0.85)
        used += self.sync_step(line_marker, code_lines, L_IF_TRUCK, run_time=0.85)
        used += self.sync_step(
            line_marker, code_lines, L_DISP_PAIR,
            extra_anims=[cells[(1, 4)][0].animate.set_stroke(GREEN, width=4)],
            run_time=1.1, color=GREEN,
        )
        used += show_output("     1     4")
        used += self.sync_step(line_marker, code_lines, L_END_BAY, run_time=1.0)
        used += self.sync_step(line_marker, code_lines, L_FOR_FLOOR, run_time=1.0)
        self.hold(duration, used)

        duration = self.speak("f2_bay1", "Floor 2. Bay starts at 1. Display 2 1.")
        used = self.sync_step(
            line_marker, code_lines, L_FOR_BAY,
            extra_anims=[pointer.animate.next_to(cells[(2, 1)], LEFT, buff=0.1)],
            run_time=1.0,
        )
        used += self.sync_step(line_marker, code_lines, L_IF_BAY2, run_time=0.85)
        used += self.sync_step(line_marker, code_lines, L_IF_TRUCK, run_time=0.85)
        used += self.sync_step(
            line_marker, code_lines, L_DISP_PAIR,
            extra_anims=[cells[(2, 1)][0].animate.set_stroke(GREEN, width=4)],
            run_time=1.1, color=GREEN,
        )
        used += show_output("     2     1", size=17)
        self.hold(duration, used)

        duration = self.speak("f2_bay2", "Floor 2, bay 2. Continue again.")
        used = self.sync_step(line_marker, code_lines, L_FOR_BAY, extra_anims=[pointer.animate.next_to(cells[(2, 2)], LEFT, buff=0.1)], run_time=0.9)
        used += self.sync_step(line_marker, code_lines, L_IF_BAY2, run_time=0.9)
        used += self.sync_step(
            line_marker, code_lines, L_CONTINUE,
            extra_anims=[cells[(2, 2)][0].animate.set_stroke(CORAL, width=4).set_fill("#3A1D26")],
            run_time=1.2, color=CORAL,
        )
        skip = Text("continue → next bay", font_size=18, color=CORAL).next_to(cells[(2, 2)], DOWN, buff=0.1)
        self.play(FadeIn(skip), run_time=0.4)
        self.play(FadeOut(skip), run_time=0.35)
        used += 0.75
        self.hold(duration, used)

        duration = self.speak("f2_bay3", "Floor 2, bay 3. Truck. Break ends the bay loop only.")
        used = self.sync_step(line_marker, code_lines, L_FOR_BAY, extra_anims=[pointer.animate.next_to(cells[(2, 3)], LEFT, buff=0.1)], run_time=0.9)
        used += self.sync_step(line_marker, code_lines, L_IF_BAY2, run_time=0.85)
        used += self.sync_step(line_marker, code_lines, L_IF_TRUCK, run_time=1.0)
        used += self.sync_step(
            line_marker, code_lines, L_DISP_TRUCK,
            extra_anims=[cells[(2, 3)][0].animate.set_stroke(YELLOW, width=4)],
            run_time=1.2, color=YELLOW,
        )
        used += show_output("Truck! Leaving floor 2", size=17)
        used += self.sync_step(line_marker, code_lines, L_BREAK, run_time=1.2, color=CORAL)
        used += self.sync_step(line_marker, code_lines, L_END_BAY, run_time=1.1, color=CORAL)
        self.hold(duration, used)

        duration = self.speak("f2_never", "Bay 4 never starts. No floor 3, so the program stops.")
        used = 0
        cross = Cross(cells[(2, 4)], stroke_color=CORAL, stroke_width=5)
        never = Text("never reached", font_size=17, color=CORAL).next_to(cells[(2, 4)], DOWN, buff=0.08)
        self.play(Create(cross), FadeIn(never), run_time=1.1)
        used += 1.1
        break_arrow = CurvedArrow(
            code_lines[L_BREAK].get_right(),
            code_lines[L_END_BAY].get_right(),
            angle=-PI / 2,
            color=CORAL,
        )
        self.play(Create(break_arrow), run_time=1.1)
        used += 1.1
        self.hold(duration, used)

        self.clear_stage()
        heading = self.title("continue is not break", "Both change the path, but in different ways")
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
            "Break leaves the bay loop. The floor loop is still alive.",
            font_size=24,
            color=PURPLE,
        ).next_to(cards, DOWN, buff=0.38)
        duration = self.speak(
            "controls",
            "continue = next bay. break = leave the bay loop, not the floor loop.",
        )
        self.play(Write(heading), FadeIn(continue_group, shift=0.2 * RIGHT), run_time=1.5)
        self.play(FadeIn(break_group, shift=0.2 * LEFT), run_time=1.2)
        self.play(Write(nearest), run_time=1.2)
        self.play(Indicate(continue_word, color=CORAL), Indicate(break_word, color=YELLOW), run_time=1.3)
        self.hold(duration, 5.2)

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
            h_buff=0.3,
            v_buff=0.16,
        ).scale(0.95).to_edge(RIGHT, buff=0.3).shift(0.25 * UP)
        rows = table.get_rows()
        missing = Text("(2, 4) is absent: that pass never starts", font_size=20, color=CORAL)
        missing.next_to(table, DOWN, buff=0.25)

        code, code_lines = self.code_block(
            [
                "for floor = 1:2",
                "    for bay = 1:4",
                "        if bay == 2",
                "            continue",
                "        end",
                "        if floor == 2 && bay == 3",
                "            disp('Truck! Leaving floor 2')",
                "            break",
                "        end",
                "        disp([floor bay])",
                "    end",
                "end",
            ],
            font_size=15,
        )
        code.to_edge(LEFT, buff=0.3).shift(0.25 * UP)
        line_marker = SurroundingRectangle(
            code_lines[L_FOR_FLOOR], color=YELLOW, fill_color=YELLOW, fill_opacity=0.12, buff=0.05
        )

        duration = self.speak(
            "trace_intro",
            "One paper row per pass that begins: floor, bay, condition, action.",
        )
        self.play(
            Write(heading),
            FadeIn(code),
            Create(table.get_horizontal_lines()),
            Create(table.get_vertical_lines()),
            run_time=1.6,
        )
        self.play(FadeIn(rows[0]), Create(line_marker), run_time=0.9)
        row_marker = SurroundingRectangle(
            rows[1], color=YELLOW, fill_color=YELLOW, fill_opacity=0.08, buff=0.06
        )
        self.play(Create(row_marker), run_time=0.6)
        self.hold(duration, 3.1)

        # Each step: (code line, line colour, table cells written at that step)
        def normal_path(row):
            return [
                (L_FOR_BAY, YELLOW, [rows[row][0], rows[row][1]]),
                (L_IF_BAY2, YELLOW, []),
                (L_IF_TRUCK, YELLOW, [rows[row][2]]),
                (L_DISP_PAIR, GREEN, [rows[row][3]]),
            ]

        def continue_path(row):
            return [
                (L_FOR_BAY, YELLOW, [rows[row][0], rows[row][1]]),
                (L_IF_BAY2, CORAL, [rows[row][2]]),
                (L_CONTINUE, CORAL, [rows[row][3]]),
            ]

        truck_path = [
            (L_FOR_BAY, YELLOW, [rows[7][0], rows[7][1]]),
            (L_IF_BAY2, YELLOW, []),
            (L_IF_TRUCK, YELLOW, [rows[7][2]]),
            (L_DISP_TRUCK, YELLOW, []),
            (L_BREAK, CORAL, [rows[7][3]]),
            (L_END_BAY, CORAL, []),
        ]
        floor_two_start = [(L_FOR_FLOOR, BLUE, [])] + normal_path(5)

        table_beats = [
            ("trace_11", "Floor 1, bay 1. Neither if. Display 1 1.", 1, YELLOW, normal_path(1)),
            ("trace_12", "Floor 1, bay 2. Continue. Still write the row.", 2, CORAL, continue_path(2)),
            ("trace_13", "Floor 1, bay 3. Display 1 3.", 3, YELLOW, normal_path(3)),
            ("trace_14", "Floor 1, bay 4. Display 1 4. Inner values done.", 4, YELLOW, normal_path(4)),
            ("trace_21", "Floor 2, bay 1. Inner loop restarts. Display 2 1.", 5, YELLOW, floor_two_start),
            ("trace_22", "Floor 2, bay 2. Continue again. Write the row.", 6, CORAL, continue_path(6)),
            ("trace_23", "Floor 2, bay 3. Truck message, then break.", 7, GREEN, truck_path),
        ]
        for key, caption, row_index, color, steps in table_beats:
            target = SurroundingRectangle(
                rows[row_index],
                color=color,
                fill_color=color,
                fill_opacity=0.10,
                buff=0.06,
            )
            self.play(Transform(row_marker, target), run_time=0.45)
            duration = self.speak(key, caption)
            # Spread the code steps across the spoken line so the highlight
            # moves at the same pace as the voice.
            slot = max(duration * 0.9 / len(steps), 0.9)
            step_time = min(0.8, slot)
            used = 0.0
            for line_index, line_color, cells in steps:
                anims = [FadeIn(cell) for cell in cells]
                used += self.sync_step(
                    line_marker, code_lines, line_index,
                    extra_anims=anims, run_time=step_time, color=line_color,
                )
                pause = slot - step_time
                if pause > 0.05:
                    self.wait(pause)
                    used += pause
            self.hold(duration, used)

        duration = self.speak(
            "trace_missing",
            "No row for 2, 4. Break already left the bay loop. Do not invent it.",
        )
        break_arrow = CurvedArrow(
            code_lines[L_BREAK].get_right(),
            code_lines[L_END_BAY].get_right(),
            angle=-PI / 2,
            color=CORAL,
        )
        self.play(Create(break_arrow), run_time=1.0)
        self.play(Write(missing), run_time=1.1)
        self.play(Indicate(missing, color=CORAL), run_time=1.0)
        self.hold(duration, 3.1)

        # Counting the passes
        self.clear_stage()
        heading = self.title("Count the loop passes", "Possible passes, minus the ones break prevents")
        grid, cells = self.bay_grid()
        grid.scale(0.8).to_edge(LEFT, buff=0.6).shift(0.35 * UP)
        maths = VGroup()
        maths_anchor = grid.get_right() + RIGHT * 0.8 + UP * 1.3

        def add_line(text, color=INK, size=26):
            line = Text(text, font_size=size, color=color)
            if len(maths) == 0:
                line.move_to(maths_anchor, aligned_edge=LEFT)
            else:
                line.next_to(maths[-1], DOWN, aligned_edge=LEFT, buff=0.28)
            maths.add(line)
            return line

        duration = self.speak("count_intro", "Outer loop: floor = 1, 2. That is 2 outer passes.")
        self.play(Write(heading), FadeIn(grid), run_time=1.5)
        outer = add_line("outer passes = 2", BLUE)
        self.play(
            Write(outer),
            *[Indicate(grid[i][0], color=BLUE) for i in range(2)],
            run_time=1.4,
        )
        self.hold(duration, 2.9)

        duration = self.speak("count_full", "Without break: 2 floors × 4 bays = 8 possible inner passes.")
        self.play(
            LaggedStart(
                *[cells[(f, b)][0].animate.set_stroke(YELLOW, width=4) for f in (1, 2) for b in range(1, 5)],
                lag_ratio=0.18,
            ),
            run_time=2.6,
        )
        full = add_line("2 × 4 = 8 possible", YELLOW)
        self.play(Write(full), run_time=1.0)
        self.hold(duration, 3.6)

        duration = self.speak("count_continue", "Continue still counts: bay 2 began on both floors.")
        self.play(
            *[cells[(f, 2)][0].animate.set_stroke(CORAL, width=4).set_fill("#3A1D26") for f in (1, 2)],
            run_time=1.0,
        )
        cont = add_line("continue: still counted (2 passes)", CORAL, size=23)
        self.play(Write(cont), run_time=1.1)
        self.hold(duration, 2.1)

        duration = self.speak("count_break", "Break stops bay 4 on floor 2. 8 − 1 = 7 inner passes.")
        cross = Cross(cells[(2, 4)], stroke_color=CORAL, stroke_width=5)
        self.play(Create(cross), cells[(2, 4)][0].animate.set_stroke(MUTED, width=2), run_time=1.0)
        brk = add_line("break: 8 − 1 = 7 inner passes", GREEN)
        self.play(Write(brk), run_time=1.1)
        self.hold(duration, 2.1)

        duration = self.speak("count_total", "7 passes = 7 table rows. Displays = 7 − 2 − 1 = 4.")
        total_box = VGroup(
            Text("inner passes = 7 = table rows", font_size=24, color=INK),
            Text("pair displays = 7 − 2 − 1 = 4", font_size=24, color=GREEN),
            Text("outer passes = 2", font_size=24, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        frame = SurroundingRectangle(total_box, color=PURPLE, fill_color=PANEL, fill_opacity=0.95, buff=0.25, corner_radius=0.12)
        summary = VGroup(frame, total_box).next_to(grid, DOWN, buff=0.45).align_to(grid, LEFT)
        self.play(FadeIn(frame), run_time=0.5)
        for line in total_box:
            self.play(Write(line), run_time=1.0)
        self.hold(duration, 3.5)

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
        duration = self.speak(
            "recap",
            "Outer value fixed. Inner values in order. Test each if. Record the action.",
        )
        self.play(Write(heading), run_time=1.1)
        for step in steps:
            self.play(FadeIn(step, shift=0.18 * RIGHT), run_time=0.85)
        check = Text("You are tracing a path—not solving everything at once.", font_size=27, color=GREEN)
        check.next_to(steps, DOWN, buff=0.38)
        self.play(Write(check), run_time=1.2)
        self.hold(duration, 5.7)
        self.wait(0.6)
