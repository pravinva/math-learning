# Decision loops — narrated Manim lesson

This lesson explains how to trace nested `for` loops containing `if`,
`continue` and `break`. It uses the two-floor car park exercise from the
DPEN100 programming-foundations guide.

The finished video includes:

- spoken narration;
- concise on-screen captions;
- a moving pointer showing the current `(floor, bay)` pair;
- code-line highlighting;
- separate visual explanations of `continue` and `break`;
- a complete hand-tracing table.

## Build

On macOS, install FFmpeg and create a Python 3.12 environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install manim==0.21.0
```

Generate the narration with Vertex AI Gemini TTS (Australian male, ADC
on `gcp-sandbox-field-eng`), then render at 720p without cache so every
pass keeps its voice clip:

```bash
python make_narration.py
manim -qm --disable_caching decision_loops.py DecisionLoops
```

The generated video is:

```text
media/videos/decision_loops/720p30/DecisionLoops.mp4
```

The narration wording is stored in `make_narration.py`, so it can be edited
and regenerated without changing the animation code.
