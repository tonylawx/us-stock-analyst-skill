#!/usr/bin/env python3
"""Validate the public US stock analyst research-methodology contract and brief drafts."""

from __future__ import annotations

import argparse
import re
import sys
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

FORBIDDEN_WORDS = [
    "主播", "视频", "节目", "录音", "转录", "字幕", "原文",
    "上述内容", "这期", "本期节目", "文中提到", "作者提到",
    "他说", "她说", "震撼发布", "彻底颠覆", "史诗级", "吊打",
    "暴富", "无脑做多", "无脑做空", "内幕消息",
    "长桥", "富途", "老虎证券", "雪盈证券",
    "上期把", "上期设", "上期写", "上期提到", "上期文章", "上期日历",
    "上期的说法", "应更正为", "应予收回", "应收回", "正如上期",
]

RETAIL_BROKER_KEYWORDS = ["长桥", "富途", "老虎证券", "雪盈证券"]

ASSUMED_CONTEXT_PATTERNS = [
    r"上期(?!度)",
    r"上期把",
    r"上期设",
    r"上期写",
    r"上期提到",
    r"上期文章",
    r"上期日历",
    r"上期的?[说判研预测推]",
    r"应更正为",
    r"应收回",
    r"应予收回",
    r"正如上期",
]


def validate(root: Path) -> list[str]:
    """Validate repository contract markers and reference headings."""
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


def validate_draft(text: str) -> list[str]:
    """Validate a daily market brief draft against industrial richness and format standards."""
    errors: list[str] = []
    lines = text.strip().splitlines()

    # 1. H1 Title check
    h1_lines = [line for line in lines if line.startswith("# ")]
    if not h1_lines:
        errors.append("Missing H1 title (# Title).")
    else:
        title = h1_lines[0].strip()
        if ":" in title or "：" in title:
            errors.append(f"H1 title must not contain colons (':' or '：') (got: {title})")
        if not re.search(r"\b20\d{6}\b", title):
            errors.append(f"H1 title must end with target date in YYYYMMDD format (got: {title})")

    # 2. Subheadings check
    h2_lines = [line for line in lines if line.startswith("## ")]
    if not h2_lines:
        errors.append("Draft must contain at least one H2 section (## Section).")
    for line in h2_lines:
        if ":" in line or "：" in line:
            errors.append(f"Subheading must not contain colons: {line.strip()}")

    # 3. Forbidden words check
    for word in FORBIDDEN_WORDS:
        count = text.count(word)
        if count > 0:
            errors.append(f"Found forbidden or unprofessional word '{word}' ({count} times).")

    # 4. Retail broker keywords
    for broker in RETAIL_BROKER_KEYWORDS:
        if broker in text:
            errors.append(f"Found retail broker reference '{broker}'. Use institutional market sources.")

    # 5. Assumed prior context check
    for pat in ASSUMED_CONTEXT_PATTERNS:
        matches = re.findall(pat, text)
        if matches:
            errors.append(f"Found assumed prior-issue context matching pattern '{pat}' ({len(matches)} times).")

    # 6. First-person limit
    first_person_count = text.count("我") + text.count("我们")
    if first_person_count > 12:
        errors.append(f"First-person pronoun count exceeds limit: {first_person_count} > 12.")

    # 7. Length & Richness check
    char_count = len(re.sub(r"\s+", "", text))
    if char_count < 2200:
        errors.append(f"Draft is too terse for an industrial-grade brief: {char_count} chars (minimum 2200 required, 2800~3800 recommended).")

    # 8. Section paragraph richness
    sections = re.split(r"(?m)^##\s+", text)
    if len(sections) > 1:
        for idx, sec in enumerate(sections[1:], start=0):
            sec_lines = sec.strip().splitlines()
            sec_title = sec_lines[0] if sec_lines else f"Section {idx}"
            clean_sec = re.sub(r"```chart[\s\S]*?```", "", sec)
            paragraphs = [p.strip() for p in re.split(r"\n\s*\n", clean_sec)[1:] if len(p.strip()) > 50]
            if len(paragraphs) < 2:
                errors.append(f"Section '## {sec_title}' lacks depth: found {len(paragraphs)} substantial paragraphs (minimum 2 required).")

    # 9. Quantitative evidence density
    metrics_found = re.findall(r"\d+(?:\.\d+)?%|\$\d+(?:\.\d+)?|\b\d+(?:\.\d+)?(?:点|基点|bps|亿|万|美元|元|MW|GW)\b", text)
    if len(metrics_found) < 6:
        errors.append(f"Insufficient quantitative market data density: found only {len(metrics_found)} specific metric occurrences (minimum 6 required).")

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

        # Test draft validation
        sample_valid = """# 示例美股大盘异动与支撑对账 20261026

## 0 大盘盘面复盘与指数检验

标普500指数全周微跌0.56%收报5780点，周五冲高回落显露资金追涨乏力。盘面上科技权重股遭遇持续调仓压力，整体成交量能放大但价格未有突破。大盘ETF SPY 下跌0.5%，纳指100 ETF QQQ 下跌1.8%，多头在5750点整数关口展开防守。

深入资金面结构，纳指100与半导体板块出现显著抛压，多头在关键点位5750点展开防御，成交宽度呈现收窄态势。十年期美债收益率上升5个基点至4.95%，资金借贷成本边际上行抑制风险偏好。

## 1 核心龙头微观账本穿透

AMD公布最新财报营收录得68亿美元，净利润符合预期，但自由现金流转换率仅为52%，单季度股权激励支出高达3.8亿美元，显著摊薄利润质量。

产业链博弈表明上游晶圆制造巨头维持55%高毛利，下游云厂商施加采购议价压力，使得中游硬件供应商利润空间受到挤压。单卡售价与液冷CDU改造成本增加，服务器投资回收周期明显拉长。
""" + ("\n客观跟踪价格点位与微观财务指标，以分水岭确认多空边界，支撑位在5720点，高位阻力在5800点，折现率变动25基点。" * 35)

        draft_errs = validate_draft(sample_valid)
        if draft_errs:
            raise AssertionError(draft_errs)

    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--draft", type=Path, help="Path to markdown draft file to validate")
    args = parser.parse_args()

    if args.self_test:
        return self_test()

    if args.draft:
        if not args.draft.is_file():
            print(f"Draft file not found: {args.draft}")
            return 1
        content = args.draft.read_text(encoding="utf-8")
        errors = validate_draft(content)
        if errors:
            print("DRAFT_VALIDATION_FAILED:")
            for err in errors:
                print(f"  - {err}")
            return 1
        print("DRAFT_VALIDATION_OK")
        return 0

    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"VALIDATION_ERROR: {error}", file=sys.stderr)
        return 1

    print("RESEARCH_STANDARD_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
