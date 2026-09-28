# MATH142 Manim integration examples

Three short scenes introduce:

1. recognising a logarithmic derivative fingerprint;
2. substitution as a change of variable and scale;
3. integration by parts as the rearranged product rule.

The published videos and browser gallery are in `index.html`. The editable
Manim source is `integration_intuition.py`.

## Render locally

Use Python 3.12 or 3.13 and Manim Community Edition:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
manim -qm integration_intuition.py \
  DerivativeFingerprints \
  SubstitutionAsRescaling \
  IntegrationByPartsFromProductRule
```

Manim also requires FFmpeg and a LaTeX installation. On macOS they can be
installed with Homebrew:

```bash
brew install ffmpeg texlive dvisvgm
```

If Homebrew installs `texlive` and `dvisvgm` under separate prefixes, export
the TeX paths before rendering:

```bash
export TEXMFROOT="$(brew --prefix texlive)/share"
export TEXMFDIST="$TEXMFROOT/texmf-dist"
export TEXMFCNF="$TEXMFDIST/web2c:"
```

The mathematics in every scene is checked at the end by differentiating the
displayed antiderivative.
