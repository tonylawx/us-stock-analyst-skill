# US Stock Analyst Skill

Codex skill for writing and iteratively improving evidence-led Chinese US stock daily analysis. It supports both fresh-source days and news-sourced original days when no fresh update exists.

The skill lives in `us-stock-analyst/`.

## Research Discipline

The durable research rules live in `references/research-standard.md`. They cover:

- source hierarchy and fact/estimate/interpretation separation
- `Conclusion → Evidence → Mechanism → Trading implication`
- earnings and cash-conversion checks
- price-attribution confidence
- bullish/neutral/bearish event scenarios
- a light pre-publish research gate

## Privacy

This repository is intended to remain reusable and user-agnostic. Do not add personal biography, account-specific portfolio details, private source names, local filesystem paths, credentials, private workflow identifiers, or other identifying context. When a useful rule comes from a private case, keep only the generalized analytical rule.

## Validation

```bash
python3 us-stock-analyst/scripts/validate_research_standard.py --self-test
python3 us-stock-analyst/scripts/validate_research_standard.py
```

## License

MIT
