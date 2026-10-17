"""Generate the narration clips used by the decision-loops Manim scene.

macOS's built-in ``say`` command creates the speech. FFmpeg converts each
clip to a WAV file that Manim can place on the animation timeline.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


VOICE = "Karen"
RATE = "165"
ROOT = Path(__file__).resolve().parent
AUDIO_DIR = ROOT / "audio"

NARRATION = {
    "intro": (
        "A loop can look like a wall of code, but the computer is only ever "
        "following one instruction at a time. To understand it, keep your "
        "attention on the current values, and trace the arrows."
    ),
    "single_if": (
        "In a for loop, the loop variable receives one value on each pass. "
        "An if statement inside the loop asks its question again for every "
        "new value. Here, bay two is closed, so that pass follows a different path."
    ),
    "nested": (
        "A nested loop is like an odometer with two wheels. The outer loop "
        "chooses a floor. While that floor stays fixed, the inner loop visits "
        "every bay. Only after the inner loop finishes does the floor change."
    ),
    "read_code": (
        "Read nested-loop code from the outside in. Floor becomes one. Bay "
        "then begins at one. At each bay, test the conditions from top to "
        "bottom. When the pass ends, return to the inner for line for the next bay."
    ),
    "floor_one": (
        "On floor one, bay one reaches the display instruction. Bay two makes "
        "the first condition true. Continue skips everything below it for this "
        "pass, then bay becomes three. Bays three and four are displayed."
    ),
    "floor_two": (
        "When floor becomes two, the bay loop starts again at one. Bay one is "
        "displayed, and bay two is skipped. At bay three, both parts of the "
        "truck condition are true. The message is displayed, then break leaves "
        "the bay loop. Bay four is never reached."
    ),
    "controls": (
        "Continue and break do different jobs. Continue skips the rest of only "
        "the current pass, so the same loop tries its next value. Break ends "
        "the nearest loop completely. Here it ends the bay loop, not the outer floor loop."
    ),
    "trace": (
        "On paper, make one row for every pair that is actually attempted. "
        "Write the floor and bay first, evaluate the conditions, then record "
        "the action. Do not write the pair two comma four, because break means "
        "that pass never begins."
    ),
    "recap": (
        "Remember the rhythm. Fix one outer value. Run the inner values in "
        "order. Test each if from top to bottom. Continue means next inner "
        "value. Break means leave the inner loop. A trace table makes the flow visible."
    ),
}


def duration(path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def main() -> None:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    durations = {}

    for name, text in NARRATION.items():
        aiff = AUDIO_DIR / f"{name}.aiff"
        wav = AUDIO_DIR / f"{name}.wav"
        subprocess.run(
            ["say", "-v", VOICE, "-r", RATE, "-o", str(aiff), text],
            check=True,
        )
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-loglevel",
                "error",
                "-i",
                str(aiff),
                "-ar",
                "48000",
                "-ac",
                "1",
                str(wav),
            ],
            check=True,
        )
        aiff.unlink()
        durations[name] = round(duration(wav), 3)
        print(f"{name:12} {durations[name]:6.2f}s")

    (AUDIO_DIR / "durations.json").write_text(
        json.dumps(durations, indent=2) + "\n"
    )
    print(f"Total narration: {sum(durations.values()):.2f}s")


if __name__ == "__main__":
    main()
