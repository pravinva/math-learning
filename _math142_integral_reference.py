from pathlib import Path
import re


ROOT = Path(__file__).parent
LESSONS = ROOT / "siddharth" / "math142"
CANONICAL = LESSONS / "MATH142_Week1_Integration_Techniques.html"

CSS_START = "/* INTEGRAL_REFERENCE_CSS_START */"
CSS_END = "/* INTEGRAL_REFERENCE_CSS_END */"
BLOCK_START = "<!-- INTEGRAL_REFERENCE_START -->"
BLOCK_END = "<!-- INTEGRAL_REFERENCE_END -->"

TARGETS = [
    "MATH142_Week2_PartialFractions_ImproperIntegrals.html",
    "MATH142_Week4_PolarCoordinates.html",
    "MATH142_Week4A_Parametric_Curves.html",
    "MATH142_Week5_Areas_Volumes.html",
    "MATH142_Week6_ArcLength.html",
    "MATH142_Week7_SeparableDE_IntegratingFactor.html",
    "MATH142_Week8_LinearDE_Applications.html",
    "MATH142_Week8A_Exact_Homogeneous_Bernoulli.html",
    "MATH142_Week11_Sequences_Series_ConvergenceTests.html",
]


def marked_fragment(text: str, start: str, end: str) -> str:
    first = text.index(start)
    last = text.index(end, first) + len(end)
    return text[first:last]


def replace_or_insert(
    text: str,
    fragment: str,
    start: str,
    end: str,
    insertion_token: str,
    place_after: bool,
) -> str:
    if start in text:
        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
        text, replacements = pattern.subn(lambda _: fragment, text, count=1)
        if replacements != 1:
            raise RuntimeError(f"Could not replace block beginning {start}")
        return text

    if insertion_token not in text:
        raise RuntimeError(f"Could not find insertion token {insertion_token}")
    if place_after:
        return text.replace(insertion_token, insertion_token + "\n\n" + fragment, 1)
    return text.replace(insertion_token, fragment + "\n" + insertion_token, 1)


def inject(path: Path, css: str, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_or_insert(
        text, css, CSS_START, CSS_END, "</style>", place_after=False
    )
    text = replace_or_insert(
        text, block, BLOCK_START, BLOCK_END, "</header>", place_after=True
    )

    if 'href="#integral-table"' not in text:
        pattern = re.compile(
            r'(<div class="toc-title">Contents</div>\s*<ol>)', re.I
        )
        text, replacements = pattern.subn(
            r'\1\n<li><a href="#integral-table">Table of integrals</a></li>',
            text,
            count=1,
        )
        if replacements != 1:
            raise RuntimeError(f"Could not add contents link in {path.name}")

    path.write_text(text, encoding="utf-8")
    print(f"Updated {path.name}")


def main() -> None:
    canonical_text = CANONICAL.read_text(encoding="utf-8")
    css = marked_fragment(canonical_text, CSS_START, CSS_END)
    block = marked_fragment(canonical_text, BLOCK_START, BLOCK_END)
    for filename in TARGETS:
        inject(LESSONS / filename, css, block)


if __name__ == "__main__":
    main()
