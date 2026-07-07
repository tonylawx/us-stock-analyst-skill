#!/usr/bin/env python3
"""Append a daily public-source-vs-draft learning entry for the style skill."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOG = SKILL_ROOT / "references" / "daily-learning-log.md"

FOCUS_TERMS = (
    "缩量",
    "放量",
    "买盘",
    "抛压",
    "低点",
    "高点",
    "跳空",
    "站稳",
    "跌破",
    "突破",
    "支撑",
    "压力",
    "仓位",
    "减仓",
    "止损",
    "流动性",
    "资本支出",
    "货币化",
    "财报",
    "前瞻",
    "趋势",
    "验证",
)
COMMON_NAMES = (
    "三星",
    "美光",
    "英伟达",
    "微软",
    "台积电",
    "博通",
    "阿斯麦",
    "特斯拉",
    "半导体",
    "存储",
    "软件",
    "光模块",
    "费城半导体",
    "纳指",
    "标普",
)


def clean_source_text(text: str) -> str:
    return re.sub(r"\[\d\d:\d\d:\d\d,\d{3}\]\s*", "", text)


def title_from_path(path: Path) -> str:
    name = path.stem
    return re.sub(r"^[A-Za-z0-9_-]+-", "", name)


def count_terms(text: str, terms: tuple[str, ...]) -> list[tuple[str, int]]:
    hits = [(term, text.count(term)) for term in terms]
    return [(term, count) for term, count in hits if count]


def extract_numbers(text: str, limit: int = 32) -> list[str]:
    seen: list[str] = []
    for match in re.findall(r"\d+(?:\.\d+)?%?|\d+\s*到\s*\d+", text):
        if match not in seen:
            seen.append(match)
        if len(seen) >= limit:
            break
    return seen


def extract_section_titles(draft_text: str) -> list[str]:
    return re.findall(r"^##\s+(.+)$", draft_text, flags=re.M)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_notes", type=Path)
    parser.add_argument("--draft", type=Path)
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    parser.add_argument("--date", default=dt.date.today().isoformat())
    args = parser.parse_args()

    source_text = clean_source_text(args.source_notes.read_text(encoding="utf-8"))
    draft_text = args.draft.read_text(encoding="utf-8") if args.draft else ""
    source_title = title_from_path(args.source_notes)
    focus = count_terms(source_text, FOCUS_TERMS)
    names = count_terms(source_text, COMMON_NAMES)
    numbers = extract_numbers(source_text)
    draft_sections = extract_section_titles(draft_text)

    covered = []
    missing = []
    if draft_text:
        for term, _count in names[:16] + focus[:16]:
            (covered if term in draft_text else missing).append(term)

    entry = [
        f"## {args.date} Daily Learning",
        "",
        f"- Public source notes: `{args.source_notes}`",
    ]
    if args.draft:
        entry.append(f"- Compared draft: `{args.draft}`")
    entry.extend(
        [
            f"- Source-note title: {source_title}",
            f"- Top source names: {', '.join(f'{term}({count})' for term, count in names[:18]) or 'n/a'}",
            f"- Trading focus terms: {', '.join(f'{term}({count})' for term, count in focus[:18]) or 'n/a'}",
            f"- First numeric anchors: {', '.join(numbers) or 'n/a'}",
        ]
    )
    if draft_sections:
        entry.append(f"- Draft sections: {' | '.join(draft_sections)}")
    if draft_text:
        entry.append(f"- Covered terms: {', '.join(covered) or 'n/a'}")
        entry.append(f"- Missing terms to consider: {', '.join(missing) or 'n/a'}")
    entry.extend(
        [
            "",
            "### Update Notes",
            "",
            "- Preserve the source day's true main line before adding outside news.",
            "- Convert repeated public-source levels into explicit article decision points.",
            "- If a draft misses a source term above, decide whether it was noise or a real omission before updating the style guide.",
            "",
        ]
    )

    args.log.parent.mkdir(parents=True, exist_ok=True)
    previous = args.log.read_text(encoding="utf-8") if args.log.exists() else "# Daily Learning Log\n\n"
    args.log.write_text(previous.rstrip() + "\n\n" + "\n".join(entry), encoding="utf-8")
    print(args.log)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
