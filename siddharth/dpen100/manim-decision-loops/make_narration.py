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
        raw = AUDIO_DIR / f"{name}-raw.wav"
        wav = AUDIO_DIR / f"{name}.wav"
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


if __name__ == "__main__":
    main()
