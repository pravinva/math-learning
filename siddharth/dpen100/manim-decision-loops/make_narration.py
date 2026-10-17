"""Generate the narration clips used by the decision-loops Manim scene.

Uses Google Cloud Vertex AI Gemini 3.8 Flash TTS via Application Default
Credentials (ADC) on project ``gcp-sandbox-field-eng``.
Voice is Charon, with natural Australian English university-lecturer style.
Clips are normalized and converted to 48 kHz mono WAV for Manim.
"""

from __future__ import annotations

import base64
import json
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AUDIO_DIR = ROOT / "audio"
PROJECT = os.environ.get("GOOGLE_CLOUD_PROJECT") or "gcp-sandbox-field-eng"
VOICE = "Charon"  # Clear, informative male voice
STYLE = (
    "Australian male university lecturer; calm, clear, slightly warm; "
    "natural Australian English; unhurried educational narration"
)

NARRATION = {
    "intro": (
        "A loop looks like a wall of code, but the computer only ever follows "
        "one instruction at a time. Keep your eye on the current values, and "
        "trace each pass in order."
    ),
    "single_intro": (
        "First, one loop. Bay will be one, then two, then three, then four. "
        "The if question is asked again on every pass."
    ),
    "single_bay1": (
        "Pass one. Bay is one. The if is false, so continue does not run. "
        "Display one."
    ),
    "single_bay2": (
        "Pass two. Bay is two. The if is true. Continue skips display, and "
        "jumps to the next bay. This pass is skipped, not ended."
    ),
    "single_bay3": (
        "Pass three. Bay is three. The if is false. Display three."
    ),
    "single_bay4": (
        "Pass four. Bay is four. Display four. Now the loop has no values left, "
        "so it ends."
    ),
    "nested_intro": (
        "Now nest the loops. Think of an odometer. Floor is the outer wheel. "
        "Bay is the inner wheel. Floor stays fixed while bay runs all the way around."
    ),
    "nested_floor1": (
        "Floor is one. Hold that outer value. The inner loop now visits bay one, "
        "bay two, bay three, and bay four. Only then may the floor change."
    ),
    "nested_floor2": (
        "The inner loop has finished, so floor becomes two. Bay starts again at "
        "one, then two, three, and four. The outer loop does not skip ahead."
    ),
    "read_code": (
        "Read this code from the outside in. Choose a floor. Then choose a bay. "
        "Test if bay is two. Then test the truck condition. Then display the pair. "
        "When the pass ends, return to the inner for line for the next bay."
    ),
    "f1_bay1": (
        "Floor one, bay one. Bay is not two, and there is no truck. "
        "Display one, one."
    ),
    "f1_bay2": (
        "Floor one, bay two. The first if is true. Continue skips display, "
        "and the inner loop tries the next bay. Floor is still one."
    ),
    "f1_bay3": (
        "Floor one, bay three. Both ifs are false. Display one, three."
    ),
    "f1_bay4": (
        "Floor one, bay four. Display one, four. The inner loop is finished, "
        "so we go back to the outer for, and floor may change."
    ),
    "f2_bay1": (
        "Floor becomes two. The bay loop starts again at one. "
        "Display two, one."
    ),
    "f2_bay2": (
        "Floor two, bay two. Continue again. Skip display. Next bay."
    ),
    "f2_bay3": (
        "Floor two, bay three. The truck condition is true. Print the message. "
        "Break ends the bay loop only. Display of two, three never runs."
    ),
    "f2_never": (
        "Bay four on floor two never starts. Control returns to the floor loop. "
        "There is no floor three, so the program stops."
    ),
    "controls": (
        "Continue skips the rest of only this pass, then the same loop tries "
        "its next value. Break ends the nearest loop completely. Here that is "
        "the bay loop, not the floor loop."
    ),
    "trace_intro": (
        "Now copy the run onto paper as a table. One row for every pass that "
        "actually begins. Write floor, then bay, then the condition result, "
        "then the action. Do not invent rows for pairs the loop never starts."
    ),
    "trace_11": (
        "First row. Floor one, bay one. Neither if is true, so the action is "
        "display one, one."
    ),
    "trace_12": (
        "Second row. Floor one, bay two. The bay-equals-two condition is true. "
        "The action is continue. The pair is still written, because this pass did begin."
    ),
    "trace_13": (
        "Third row. Floor one, bay three. Neither condition is true. Display one, three."
    ),
    "trace_14": (
        "Fourth row. Floor one, bay four. Display one, four. That finishes every "
        "inner value for floor one."
    ),
    "trace_21": (
        "Fifth row. Floor becomes two, and the inner loop starts again. "
        "Floor two, bay one. Display two, one."
    ),
    "trace_22": (
        "Sixth row. Floor two, bay two. Continue again. Write the row. "
        "Then move to the next bay."
    ),
    "trace_23": (
        "Seventh row. Floor two, bay three. The truck condition is true. "
        "Write the message, then break. Break is the action on this row."
    ),
    "trace_missing": (
        "Look at what is missing. There is no row for two comma four. "
        "Break already left the bay loop, so that pass never begins, and a "
        "honest table does not invent it."
    ),
    "recap": (
        "The rhythm is slow and strict. Fix one outer value. Run inner values "
        "in order. Test each if. Continue means next inner value. Break means "
        "leave the inner loop."
    ),
}


def get_access_token() -> str:
    token = os.environ.get("GOOGLE_OAUTH_ACCESS_TOKEN")
    if token:
        return token.strip()
    cmd = ["gcloud", "auth", "application-default", "print-access-token"]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return result.stdout.strip()


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


def generate_speech_vertex(token: str, text: str) -> tuple[bytes, str]:
    url = (
        f"https://aiplatform.googleapis.com/v1beta1/projects/{PROJECT}/"
        f"locations/global/publishers/google/models/gemini-3.8-flash-tts:generateContent"
    )
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": text,
                        "speech_metadata": {"style": STYLE},
                    }
                ],
            }
        ],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {"voice": VOICE},
            },
        },
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Goog-User-Project": PROJECT,
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        body = json.loads(response.read().decode())
    parts = body["candidates"][0]["content"]["parts"]
    audio_part = next(p for p in parts if p.get("inlineData") or p.get("inline_data"))
    inline = audio_part.get("inlineData") or audio_part.get("inline_data")
    return base64.b64decode(inline["data"]), inline.get("mimeType") or inline.get("mime_type") or ""


def write_wav(raw: Path, data: bytes, mime: str) -> None:
    if data[:4] == b"RIFF":
        raw.write_bytes(data)
        return
    rate = 24000
    if "rate=" in mime:
        try:
            rate = int(mime.split("rate=", 1)[1].split(";")[0])
        except ValueError:
            pass
    pcm = AUDIO_DIR / f"{raw.stem}.pcm"
    pcm.write_bytes(data)
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-f",
            "s16le",
            "-ar",
            str(rate),
            "-ac",
            "1",
            "-i",
            str(pcm),
            str(raw),
        ],
        check=True,
    )
    pcm.unlink(missing_ok=True)


def to_manim_wav(src: Path, dest: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-loglevel",
            "error",
            "-i",
            str(src),
            "-ar",
            "48000",
            "-ac",
            "1",
            "-af",
            "loudnorm=I=-16:TP=-1.5:LRA=11",
            str(dest),
        ],
        check=True,
    )


def main() -> None:
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    token = get_access_token()
    durations = {}

    print(f"Using Vertex AI Gemini 3.8 Flash TTS via ADC (project: {PROJECT}, voice: {VOICE})")
    for name, text in NARRATION.items():
        wav = AUDIO_DIR / f"{name}.wav"
        if wav.is_file():
            durations[name] = round(duration(wav), 3)
            print(f"  {name:12} {durations[name]:6.2f}s  (kept)")
            continue
        raw = AUDIO_DIR / f"{name}-raw.wav"
        data, mime = generate_speech_vertex(token, text)
        write_wav(raw, data, mime)
        to_manim_wav(raw, wav)
        raw.unlink(missing_ok=True)
        durations[name] = round(duration(wav), 3)
        print(f"  {name:12} {durations[name]:6.2f}s")
        time.sleep(0.5)

    (AUDIO_DIR / "durations.json").write_text(
        json.dumps(durations, indent=2) + "\n"
    )
    print(f"Total narration: {sum(durations.values()):.2f}s")


def mix_into_video(video: Path, cues_path: Path, output: Path) -> None:
    cues = json.loads(cues_path.read_text())
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(video)]
    filters = []
    labels = []
    for index, cue in enumerate(cues):
        wav = AUDIO_DIR / f"{cue['key']}.wav"
        cmd += ["-i", str(wav)]
        delay_ms = max(int(round(float(cue["t"]) * 1000)), 0)
        label = f"a{index}"
        filters.append(
            f"[{index + 1}:a]adelay={delay_ms}|{delay_ms},"
            f"aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[{label}]"
        )
        labels.append(f"[{label}]")
    mix = (
        "".join(labels)
        + f"amix=inputs={len(cues)}:duration=longest:dropout_transition=0:normalize=0,"
        + "loudnorm=I=-14:TP=-1.5:LRA=11,"
        + "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo[aout]"
    )
    cmd += [
        "-filter_complex",
        ";".join(filters + [mix]),
        "-map",
        "0:v:0",
        "-map",
        "[aout]",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
        str(output),
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
