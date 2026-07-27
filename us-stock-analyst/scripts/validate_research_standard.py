#!/usr/bin/env python3
"""Validate the public US stock analyst research-methodology contract."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

SKILL_MARKERS = (
    "references/research-standard.md",
    "Conclusion → Evidence → Mechanism → Trading implication",
    "price-attribution confidence",
    "light research gate",
)

REFERENCE_HEADINGS = (
    "## Source Hierarchy",
    "## Claim Chain",
    "## Earnings Bridge",
    "## Price Attribution Confidence",
    "## Event Scenario Tree",
    "## Light Research Gate",
)

BANNED_BINDINGS = ("LARK_DOC", "Feishu", "飞书")


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    skill_path = root / "SKILL.md"
    reference_path = root / "references" / "research-standard.md"

    if not skill_path.is_file():
        errors.append(f"missing skill file: {skill_path}")
        skill_text = ""
    else:
        skill_text = skill_path.read_text(encoding="utf-8")

    if not reference_path.is_file():
        errors.append(f"missing research standard: {reference_path}")
        reference_text = ""
    else:
        reference_text = reference_path.read_text(encoding="utf-8")

    for marker in SKILL_MARKERS:
        if marker not in skill_text:
            errors.append(f"SKILL.md missing marker: {marker}")

    for heading in REFERENCE_HEADINGS:
        if heading not in reference_text:
            errors.append(f"research-standard.md missing heading: {heading}")

    combined = f"{skill_text}\n{reference_text}"
    for binding in BANNED_BINDINGS:
        if binding in combined:
            errors.append(f"forbidden delivery binding found: {binding}")

    return errors


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "references").mkdir()
        (root / "SKILL.md").write_text(
            "\n".join(SKILL_MARKERS) + "\n",
            encoding="utf-8",
        )
        (root / "references" / "research-standard.md").write_text(
            "\n".join(REFERENCE_HEADINGS) + "\n",
            encoding="utf-8",
        )
        errors = validate(root)
        if errors:
            raise AssertionError(errors)

        (root / "references" / "research-standard.md").write_text(
            "## Source Hierarchy\nFeishu\n",
            encoding="utf-8",
        )
        errors = validate(root)
        if not any("forbidden delivery binding" in error for error in errors):
            raise AssertionError(errors)

    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("RESEARCH_STANDARD_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
