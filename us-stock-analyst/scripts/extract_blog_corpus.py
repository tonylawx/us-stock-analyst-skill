#!/usr/bin/env python3
"""Build a compact style corpus from Tony's blog archive."""

from __future__ import annotations

import argparse
import collections
import re
from pathlib import Path


DEFAULT_BLOG = Path("blog")
SKILL_ROOT = Path(__file__).resolve().parents[1]

FINANCE_HINTS = (
    "美股",
    "纳指",
    "标普",
    "半导体",
    "科技股",
    "AI",
    "SpaceX",
    "SOXX",
    "SMH",
    "QQQ",
    "NVDA",
    "TSLA",
    "MSFT",
    "MU",
    "IGV",
)
NON_DAILY_HINTS = (
    "婚姻",
    "被动收入",
    "OPC",
    "无业",
    "投资回忆录",
    "浅谈我理解的期权",
    "黑灯工厂",
    "agent",
    "Agent",
    "漂亮的屎",
    "大陆人现在怎么买",
    "奥德赛",
    "尾部风险",
)
STOP_TICKERS = {
    "AI",
    "IPO",
    "ETF",
    "PMI",
    "CPI",
    "PCE",
    "GDP",
    "CTA",
    "RSI",
    "CEO",
    "USD",
    "EPS",
    "ADR",
    "API",
    "HTML",
}
KEY_TERMS = (
    "缩量",
    "放量",
    "买盘",
    "抛压",
    "回撤",
    "突破",
    "站稳",
    "跌破",
    "支撑",
    "压力",
    "区间",
    "观察",
    "验证",
    "仓位",
    "止损",
    "止盈",
    "流动性",
    "资本支出",
    "货币化",
    "高增长",
    "前瞻",
    "风险",
)


def read_title(path: Path, text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        parts = text.split("\n---\n", 1)
        if len(parts) == 2:
            return parts[1]
    return text


def is_daily(title: str, text: str) -> bool:
    if any(hint in title for hint in NON_DAILY_HINTS):
        return False
    if "AI 美股分析师" in title or "AI美股分析师" in title:
        return True
    if any(hint in title for hint in ("美股", "纳指", "半导体", "科技股", "美光", "SpaceX")):
        return any(hint in text[:2400] for hint in FINANCE_HINTS)
    has_date_suffix = re.search(r"20\d{6}\s*$", title) is not None
    has_market_hint = any(hint in title or hint in text[:1600] for hint in FINANCE_HINTS)
    return has_date_suffix and has_market_hint


def chinese_chars(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def section_count(text: str) -> int:
    h2 = len(re.findall(r"^##\s+", text, flags=re.M))
    if h2:
        return h2
    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    return max(0, len(paragraphs) - 1)


def tickers(text: str) -> list[str]:
    raw = re.findall(r"\b[A-Z]{2,5}\b", text)
    return [item for item in raw if item not in STOP_TICKERS]


def top_items(counter: collections.Counter[str], limit: int = 20) -> str:
    return ", ".join(f"{key}({value})" for key, value in counter.most_common(limit))


def display_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return path.name


def first_paragraph(text: str) -> str:
    body = strip_frontmatter(text)
    body = re.sub(r"^# .*\n", "", body, count=1)
    for part in re.split(r"\n\s*\n", body):
        compact = re.sub(r"\s+", " ", part).strip()
        if compact.startswith(("---", "publish_time:", "url:", "author:", "date:", "![", "##", "#")):
            continue
        if compact == "美股 · 期权 · 资讯 · 观点":
            continue
        if re.match(r"^\d+\s*[· ]", compact) and len(compact) < 80:
            continue
        if compact:
            return compact[:220]
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blog", type=Path, default=DEFAULT_BLOG)
    parser.add_argument("--out", type=Path, default=SKILL_ROOT / "references")
    args = parser.parse_args()

    archive = args.blog / "archive"
    paths = sorted(archive.glob("*.md"))
    selected: list[tuple[Path, str, str]] = []
    excluded: list[tuple[Path, str]] = []
    for path in paths:
        text = strip_frontmatter(path.read_text(encoding="utf-8"))
        title = read_title(path, text)
        if is_daily(title, text):
            selected.append((path, title, text))
        else:
            excluded.append((path, title))

    args.out.mkdir(parents=True, exist_ok=True)

    term_counts: collections.Counter[str] = collections.Counter()
    ticker_counts: collections.Counter[str] = collections.Counter()
    char_counts: list[int] = []
    section_counts: list[int] = []
    for _path, _title, text in selected:
        char_counts.append(chinese_chars(text))
        section_counts.append(section_count(text))
        ticker_counts.update(tickers(text))
        for term in KEY_TERMS:
            term_counts[term] += text.count(term)

    def avg(values: list[int]) -> int:
        return round(sum(values) / len(values)) if values else 0

    manifest_lines = [
        "# Blog Corpus Manifest",
        "",
        f"- Source archive: public blog archive",
        f"- Selected daily articles: {len(selected)}",
        f"- Excluded/non-daily articles: {len(excluded)}",
        "",
        "## Selected Daily Articles",
        "",
    ]
    for path, title, text in selected:
        manifest_lines.append(
            f"- `{display_path(path, args.blog)}` | {title} | chars={chinese_chars(text)} | sections={section_count(text)}"
        )
    manifest_lines.extend(["", "## Excluded Reference Articles", ""])
    for path, title in excluded:
        manifest_lines.append(f"- `{display_path(path, args.blog)}` | {title}")
    (args.out / "corpus-manifest.md").write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")

    baseline_lines = [
        "# Blog Style Baseline",
        "",
        "This file is generated from public archived Chinese blog posts. Use it as a baseline, then refine it from public market materials.",
        "",
        "## Corpus Stats",
        "",
        f"- Daily articles: {len(selected)}",
        f"- Average Chinese characters: {avg(char_counts)}",
        f"- Average section/paragraph count: {avg(section_counts)}",
        f"- Top tickers: {top_items(ticker_counts, 24)}",
        f"- Recurring trading terms: {top_items(term_counts, len(KEY_TERMS))}",
        "",
        "## Observed Article Shape",
        "",
        "- Start with the tape: index move, breadth, volume, tail/overnight behavior, and whether headline strength is real.",
        "- Turn news into a trade structure: what changed, which prior level is being tested, and what confirms or invalidates it.",
        "- Anchor claims in concrete levels: support, pressure, break, reclaim, gap, volume, and positioning.",
        "- Keep one core tension per article. Secondary names should support that tension, not become a ticker tour.",
        "- End with execution discipline: what to wait for, what not to chase, and where the plan is wrong.",
        "",
        "## Representative Openings",
        "",
    ]
    for path, title, text in selected[-12:]:
        baseline_lines.append(f"### {title}")
        baseline_lines.append("")
        baseline_lines.append(first_paragraph(text))
        baseline_lines.append("")
        baseline_lines.append(f"Source: `{display_path(path, args.blog)}`")
        baseline_lines.append("")
    (args.out / "blog-style-baseline.md").write_text("\n".join(baseline_lines), encoding="utf-8")

    print(f"selected={len(selected)} excluded={len(excluded)}")
    print(args.out / "corpus-manifest.md")
    print(args.out / "blog-style-baseline.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
