# US Stock Analyst Skill

Codex skill that learns a published daily US-stock voice from the article corpus, then writes that day's note in the learned voice when no fresh episode or transcript exists. A fresh episode still leads. The missing episode is not the subject.

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
