---
name: us-stock-analyst
description: Write and iteratively improve Tony-style Chinese US stock daily analysis from public market materials, current market notes, and the historical blog corpus. Use when generating a 美股分析师 daily brief, comparing public source notes to a draft, updating the style skill after new public market materials, or auditing whether a draft matches the learned market-review structure.
---

# US Stock Analyst

Use this skill to make the daily article learn from historical blog writing and current public market materials. The goal is not to summarize any one source. The goal is to absorb the day's market structure, then write a sharper Chinese US stock daily brief with Tony-style discipline.

## Source Boundaries

- Use historical blog articles as the style baseline.
- Use public market materials, public source notes, or user-provided market notes as the daily factual input.
- Keep private workflow paths, unpublished notes, and operational rules out of this public skill.

Before writing or judging a draft, read `references/blog-style-baseline.md` and `references/daily-learning-log.md`. Use `references/corpus-manifest.md` only when you need exact historical article paths or representative examples.

## Daily Workflow

1. Collect current public market materials or use the public source notes the user gives.
2. If comparing against an existing draft, run:
   ```bash
   ./scripts/update_daily_learning.py '<source-notes.txt>' --draft '<draft.md>'
   ```
   If there is no draft yet, run it with only the source notes. Treat the log as evidence, not as the final judgment.
3. Identify the day's true main line before adding secondary news. Prefer the learned hierarchy: market tape, breadth/volume/tail behavior, sector pressure, key names, decision levels, and execution discipline.
4. Draft the article in Chinese using the active publishing workflow's rules: H1 title with `YYYYMMDD`, H2 sections starting at `0`, ticker symbols bolded, no source-tracing words, and no hand-added footer.
5. Run the normal downstream workflow for humanizer, rendering, publication handoff, X copy, report, and validation when those tools are available.
6. After each day, update `references/daily-learning-log.md`. Update `references/style-guide.md` only when the same miss repeats or a new durable pattern appears.

## Writing Standard

Start with the tape, not the headline. The first section should answer: did the index move actually have breadth, volume, closing strength, and overnight confirmation?

Turn news into a trading structure. A catalyst matters only after it changes a level, trend, rotation, valuation story, or risk trigger.

Keep one core tension. Examples: semis up but software weak, index green but breadth poor, AI capex story intact but storage price action breaking, defensive rotation real or temporary. Secondary tickers must serve the tension.

Use levels as decision points. Write `站稳`, `跌破`, `守住`, `回到`, `上看`, `下看`, `观察`, and `验证` around concrete prices or zones. Do not dump prices without a plan.

Preserve trading personality. Good daily articles include caution, impatience control, and conditional action: do not chase the middle, wait for confirmation, cut if the key line breaks, hold if the thesis is intact.

Use analogies only when they clarify the market mechanic. Do not force jokes, slogans, or dramatic metaphors. The house style can be vivid, but the trade map must stay in charge.

## Common Failure Modes

- Writing a clean market note while missing the day's true market line.
- Adding a standalone TSLA or macro section just because the news is interesting.
- Covering too many tickers with shallow comments instead of drilling into the few names that move the thesis.
- Reporting a level without saying what happens above or below it.
- Losing the prior-day memory: whether today's move validates, delays, or invalidates yesterday's setup.
- Over-sanitizing the voice until the article sounds like generic AI research.

## Resources

- `references/blog-style-baseline.md`: generated style baseline from historical daily articles.
- `references/corpus-manifest.md`: generated list of selected and excluded blog articles.
- `references/style-guide.md`: human-maintained durable rules.
- `references/daily-learning-log.md`: append-only daily public-source comparison notes.
- `scripts/extract_blog_corpus.py`: refresh the historical corpus files from a blog archive.
- `scripts/update_daily_learning.py`: append a daily public-source/draft comparison entry.
