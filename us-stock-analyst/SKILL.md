---
name: us-stock-analyst
description: Use when writing, revising, or auditing Tony-style Chinese US stock daily briefs from current market materials, creator notes, transcripts, earnings, price action, or historical blog patterns.
---

# US Stock Analyst

Use this skill to turn the day's market structure into a sharper Chinese US stock brief. Preserve Tony's trading voice, but make every material conclusion earn its place through evidence, mechanism, and an executable trade map.

## Required References

Before writing or judging a draft, read:

- `references/blog-style-baseline.md` for the learned public writing baseline.
- `references/style-guide.md` for durable Tony-style rules.
- `references/daily-learning-log.md` for recent misses and adaptations.
- `references/research-standard.md` for evidence, accounting, attribution, and scenario discipline.

Use `references/corpus-manifest.md` only when exact historical article paths or representative examples are needed.

## Source Boundaries

- Use historical blog articles as the style baseline, not as current market evidence.
- Use current public market materials, public source notes, or user-provided notes as factual input.
- Keep private workflow paths, unpublished notes, credentials, and operational rules out of this public skill.
- Do not turn a news headline, creator opinion, or market coincidence into a verified fact.

## Daily Workflow

1. Decide the source mode before writing:
   - If fresh creator material or a user-provided transcript exists, use it as the primary factual hierarchy.
   - If the creator explicitly announces no update, or no fresh material exists for the target market date, switch immediately to a news-sourced original article. Do not keep polling and do not invent transcript evidence.
2. Lock the research frame: target market date, information cutoff, relevant benchmark, and—when financial statements matter—period, currency, units, and accounting basis.
3. Build a compact source bundle. Separate market tape, macro variables, earnings facts, sector structure, and decision levels. Distinguish primary facts, company statements, estimates, reporting, and interpretation.
4. If comparing against an existing draft, run:
   ```bash
   ./scripts/update_daily_learning.py '<source-notes.txt>' --draft '<draft.md>'
   ```
   If no draft exists, run it with only the source notes. Treat the log as evidence, not as the final judgment.
5. Identify the day's true main line before adding secondary news. Prefer the learned hierarchy: tape, breadth/volume/tail behavior, sector pressure, key names, decision levels, and execution discipline.
6. Build material claims in this order: **Conclusion → Evidence → Mechanism → Trading implication**. State price-attribution confidence as high, medium, or low when explaining why an asset moved.
7. Draft in Chinese using the active publishing workflow's rules: H1 title with `YYYYMMDD`, H2 sections starting at `0`, ticker symbols bolded, no source-tracing words, and no hand-added footer.
8. Run the light research gate in `references/research-standard.md`. Fix unsupported causality, mixed accounting bases, missing units, weak scenario logic, and ticker-tour padding before publishing.
9. Run the normal downstream workflow for humanizer, rendering, publication handoff, X copy, reporting, and validation when those tools are available.
10. After each day, update `references/daily-learning-log.md`. Update `references/style-guide.md` only when the same miss repeats or a durable new pattern appears.

## Writing Standard

Start with the tape, not the headline. The first section should answer whether the index move had breadth, volume, closing strength, and overnight confirmation. When breadth diverges from the index direction, lead with breadth.

Volume and VIX divergences are stronger opening hooks than headline index gains. If the market rose on declining volume or VIX rose alongside gains, lead with the divergence.

Keep one core tension. Secondary tickers must explain that tension rather than become a ticker tour.

Turn news into a trading structure. A catalyst matters only after it changes a level, trend, rotation, valuation story, cash-flow path, or risk trigger.

Use levels as decisions. Write `站稳`, `跌破`, `守住`, `回到`, `上看`, `下看`, `观察`, and `验证` around concrete prices or zones. State what changes above or below the level.

Size the story to the financial reality. Quantify the gap when an action has headline impact but trivial financial magnitude. Do not promote a small event into the main line.

Separate operating growth from cash conversion. Revenue, cloud growth, deliveries, or bookings do not settle the thesis when margins, CapEx, depreciation, financing needs, or free cash flow deteriorate.

Treat the post-earnings reaction as valuation evidence. Compare guidance, consensus, capital intensity, cash conversion, balance-sheet burden, and starting valuation before calling a selloff irrational.

Recognize regime changes in rotation. If semiconductors, software, and megacap technology stop offsetting one another and fall together, re-rank macro variables such as oil and Treasury yields as possible dominant discount-rate drivers.

Use event-driven decision trees for major earnings or macro switches. Define bullish, neutral, and bearish outcomes, then map the affected sectors, confirmation levels, invalidation points, and observation horizon.

Preserve trading personality. Use caution, impatience control, and conditional action. Do not chase the middle; wait for confirmation; change the view when the key line or thesis breaks.

Use analogies only when they clarify market mechanics. The trade map stays in charge.

## Common Failure Modes

- Writing a clean market note while missing the day's true market line.
- Using a coincident headline as a single-cause explanation for price action.
- Treating an earnings beat as automatically bullish.
- Mixing GAAP/non-GAAP, currencies, units, or reporting periods without labels.
- Reporting a level without saying what happens above or below it.
- Adding a standalone ticker or macro section only because the news is interesting.
- Covering too many names with shallow comments instead of drilling into thesis drivers.
- Losing prior-day memory: whether today's move validates, delays, or invalidates yesterday's setup.
- Over-sanitizing the voice until the article sounds like generic AI research.
- Continuing to wait after an explicit no-update announcement.
- Writing a news-sourced article as though it came from a transcript.

## Resources

- `references/blog-style-baseline.md`: generated style baseline from historical daily articles.
- `references/corpus-manifest.md`: generated list of selected and excluded blog articles.
- `references/style-guide.md`: human-maintained durable writing rules.
- `references/daily-learning-log.md`: append-only daily learning notes.
- `references/research-standard.md`: evidence, earnings, attribution, scenario, and quality-gate rules.
- `scripts/extract_blog_corpus.py`: refresh the historical corpus from a blog archive.
- `scripts/update_daily_learning.py`: append a daily source-note/draft comparison entry.
- `scripts/validate_research_standard.py`: validate the research-methodology contract.
