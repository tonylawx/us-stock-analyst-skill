# US Stock Analyst Skill

Codex skill for writing and iteratively improving Tony-style Chinese US stock daily analysis from public market materials and historical blog articles.

The skill lives in `us-stock-analyst/`.

## Daily Update

```bash
cd us-stock-analyst
./scripts/extract_blog_corpus.py --blog '<blog-archive-root>'
./scripts/update_daily_learning.py '<source-notes.txt>' --draft '<draft.md>'
```

## License

MIT
