---
name: us-stock-analyst
description: Use when writing, revising, or auditing Chinese US stock daily briefs from current market materials, transcripts, earnings, price action, or historical public market-writing patterns.
---

# US Stock Analyst

Use this skill to turn the day's market structure into a sharper Chinese US stock brief. Make every material conclusion earn its place through evidence, mechanism, and an executable trade map.

## Required References

Before writing or judging a draft, read:

- `references/blog-style-baseline.md` for the learned public writing baseline.
- `references/style-guide.md` for durable writing rules.
- `references/research-standard.md` for evidence, accounting, attribution, and scenario discipline.

Use `references/corpus-manifest.md` only when exact historical article paths or representative examples are needed.

## Source Boundaries

- Use historical public articles as the style baseline, not as current market evidence.
- Use current public market materials, public source notes, or user-provided notes as factual input.
- Keep private workflow paths, unpublished notes, credentials, personal portfolios, account details, and operational rules out of this public skill.
- Do not turn a news headline, source opinion, or market coincidence into a verified fact.

## Daily Workflow

1. Decide the source mode before writing:
   - If fresh source material or a user-provided transcript exists, use it as the primary factual hierarchy.
   - If no fresh source material exists for the target market date, switch immediately to a news-sourced original article. Do not invent transcript evidence.
2. Lock the research frame: target market date, information cutoff, relevant benchmark, and—when financial statements matter—period, currency, units, and accounting basis.
3. Build a compact source bundle. Separate market tape, macro variables, earnings facts, sector structure, and decision levels. Distinguish primary facts, company statements, estimates, reporting, and interpretation.
4. Identify the day's true main line before adding secondary news. Prefer the hierarchy: tape, breadth/volume/tail behavior, sector pressure, key names, decision levels, and execution discipline.
5. Build material claims in this order: **Conclusion → Evidence → Mechanism → Trading implication**. State price-attribution confidence as high, medium, or low when explaining why an asset moved.
6. Draft in Chinese using the active publishing workflow's rules when provided. Keep ticker formatting, heading structure, metadata, and downstream publication conventions separate from the analytical core.
7. Run the light research gate in `references/research-standard.md`. Fix unsupported causality, mixed accounting bases, missing units, weak scenario logic, and ticker-tour padding before publishing.
8. When downstream publication, rendering, social-copy, or validation tools exist, use them only after the analytical draft passes the research gate.

## Writing Standard

Start with the tape, not the headline. The first section should answer whether the index move had breadth, volume, closing strength, and overnight confirmation. When breadth diverges from index direction, lead with breadth.

Volume and VIX divergences are stronger opening hooks than headline index gains. If the market rose on declining volume or VIX rose alongside gains, lead with the divergence.

Keep one core tension. Secondary tickers must explain that tension rather than become a ticker tour.

Turn news into a trading structure. A catalyst matters only after it changes a level, trend, rotation, valuation story, cash-flow path, or risk trigger.

Use levels as decisions. Write `站稳`, `跌破`, `守住`, `回到`, `上看`, `下看`, `观察`, and `验证` around concrete prices or zones. State what changes above or below the level.

Size the story to the financial reality. Quantify the gap when an action has headline impact but trivial financial magnitude. Do not promote a small event into the main line.

Separate operating growth from cash conversion. Revenue, cloud growth, deliveries, or bookings do not settle the thesis when margins, CapEx, depreciation, financing needs, or free cash flow deteriorate.

Treat the post-earnings reaction as valuation evidence. Compare guidance, consensus, capital intensity, cash conversion, balance-sheet burden, and starting valuation before calling a selloff irrational.

Recognize regime changes in rotation. If semiconductors, software, and megacap technology stop offsetting one another and fall together, re-rank macro variables such as oil and Treasury yields as possible dominant discount-rate drivers.

Use event-driven decision trees for major earnings or macro switches. Define bullish, neutral, and bearish outcomes, then map the affected sectors, confirmation levels, invalidation points, and observation horizon.

Preserve a disciplined trader voice. Use caution, impatience control, and conditional action. Do not chase the middle; wait for confirmation; change the view when the key line or thesis breaks.

Use analogies only when they clarify market mechanics. The trade map stays in charge.

## Privacy and Portability Rules

This public skill must remain user-agnostic and portable.

Do not include:
- a person's name, handle, employer, location, medical history, immigration history, or personal biography
- brokerage names or account-specific workflow unless universally required by the skill
- personal portfolio size, holdings, cost basis, realized/unrealized P&L, debt, repayment goals, or risk budget
- private source names, unpublished creators, private transcripts, local filesystem paths, private repositories, credentials, tokens, IDs, or messaging workflows
- first-person historical trade records that can identify the original author

When a useful rule was learned from a private or personal case, keep only the generalized analytical rule. Remove the identifying example.

## Common Failure Modes

- Writing a clean market note while missing the day's true market line.
- Using a coincident headline as a single-cause explanation for price action.
- Treating an earnings beat as automatically bullish.
- Mixing GAAP/non-GAAP, currencies, units, or reporting periods without labels.
- Reporting a level without saying what happens above or below it.
- Adding a standalone ticker or macro section only because the news is interesting.
- Covering too many names with shallow comments instead of drilling into thesis drivers.
- Losing prior-day context: whether today's move validates, delays, or invalidates the previous setup.
- Over-sanitizing the voice until the article sounds like generic AI research.
- Writing a news-sourced article as though it came from a transcript.
- Leaking personal, account-specific, or private-source context into a public reusable skill.

## Resources

- `references/blog-style-baseline.md`: public style baseline from selected historical market articles.
- `references/corpus-manifest.md`: generated list of selected and excluded public articles.
- `references/style-guide.md`: durable writing rules.
- `references/research-standard.md`: evidence, earnings, attribution, scenario, and quality-gate rules.
- `scripts/extract_blog_corpus.py`: refresh the historical corpus from a public blog archive.
- `scripts/validate_research_standard.py`: validate the research-methodology contract.
