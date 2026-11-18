# Stock & ETF Share-Price Chart Policy

## Mandatory chart choice

When a research note materially discusses the **USD share price** of a named stock or ETF—its current or closing price, stop, support, resistance, target, entry, exit, or buy/sell range—show a dated **candlestick/K-line** chart for that exact ticker. If several stocks have price setups, include one K-line per instrument. Do not silently substitute a bar chart of hypothetical price levels.

Use **bars** for index percentage changes, breadth, revenue, earnings, CapEx, financial comparisons, or other non-share-price quantities. Plain index point ranges (SPX, NDX) need not be plotted as a single-stock K-line; an ETF with a dollar share-price setup (SPY, QQQ) does.

## Data integrity

- K-lines represent actual OHLC observations, not invented candles or interpolated price paths.
- Prefer reliable and clearly dated exchange/market data, and preserve the correct trading session, interval and information cutoff.
- Mark support/resistance or scenario prices as **overlays**, not observed historical OHLC.
- Never use candles from *after* the article's information cutoff for a historical market note.
- If OHLC is inaccessible or lacks trustworthy timestamps, stop the chart step, explain the source failure and seek verified candles. Do not downgrade to bars simply to make publication pass.
- The corresponding English written article keeps the same underlying candles, levels and ticker; English listening versions may omit graphics.

## Generic fenced chart example

When the downstream renderer supports chart-JSON fences, use this generic shape. This illustrates *structure only*; replace the ticker and levels with documented figures, and let a trusted data adapter provide OHLC.

    ``chart
    {"id":"example-daily-price","kind":"kline","title":"Example price levels","ticker":"EXAMPLE","interval":"1d","range":"3mo","levels":[{"label":"Support","price":100}]}
    ``

A chart-data adapter may expect the keys date/o/h/l/c for independently verified candles. Do not add synthetic candles to satisfy rendering.
