# US Stock Analyst Skill

Codex skill for writing and iteratively improving Tony-style Chinese US stock daily analysis from public market materials and historical blog articles. It supports both fresh creator-material days and news-sourced original days when no fresh update exists.

The skill lives in `us-stock-analyst/`.

## Daily Update

```bash
cd us-stock-analyst
./scripts/extract_blog_corpus.py --blog '<blog-archive-root>'
./scripts/update_daily_learning.py '<source-notes.txt>' --draft '<draft.md>'
```

Source-mode rule:

- Use fresh creator material or a user-provided transcript when available.
- If the creator explicitly announces no update, or no fresh material exists, switch immediately to public-news mode and do not invent transcript evidence.

## License

MIT
