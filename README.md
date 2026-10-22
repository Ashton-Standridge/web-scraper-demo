# Paginated Web Scraper → Clean CSV and Excel

[![tests](https://github.com/Ashton-Standridge/web-scraper-demo/actions/workflows/tests.yml/badge.svg)](https://github.com/Ashton-Standridge/web-scraper-demo/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.12-blue.svg)

> **Sample / demo project.** Not client work. It targets [books.toscrape.com](https://books.toscrape.com), a sandbox site built for scraping practice.

Scrapes all 1,000 books across 50 pages, then exports a clean, deduplicated, sorted CSV and a filterable Excel file.

![Sample output: books spreadsheet](screenshot.svg)

## The problem
A lot of jobs come down to "get the data off these pages into a spreadsheet." The hard parts are following pagination, not falling over when a request fails, and not ending up with duplicates.

## Sample output
```text
$ python scraper.py
...
page 50: 20 items
Pages: 50 | scraped: 1000 | after dedupe: 1000 -> output/books.csv / .xlsx
```
```csv
title,price_gbp,rating,in_stock,url
An Abundance of Katherines,10.0,5,True,https://books.toscrape.com/catalogue/an-abundance-of-katherines_362/index.html
Greek Mythic History,10.23,5,True,https://books.toscrape.com/catalogue/greek-mythic-history_698/index.html
```
Full file: [`output/books.csv`](output/books.csv) (1,000 rows)

## Features
- Follows the "next" link through every page, or stop early with `--pages`.
- Retries with backoff on 429/5xx responses and connection errors, with a polite delay between pages.
- Parses title, price, star rating (as a number), stock status and the full product URL.
- Dedupes by URL and sorts by rating, then price.
- Exports CSV plus Excel with a styled header, frozen top row and filters.
- Tests run offline against a fake session, so they never hit the site.

## Quickstart
```bash
git clone https://github.com/Ashton-Standridge/web-scraper-demo.git
cd web-scraper-demo
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python scraper.py                              # all pages -> output/books.csv and output/books.xlsx
python scraper.py --pages 3 --out output/sample
```

## Project layout
```text
scraper.py          fetch (with retries) -> parse -> dedupe/sort -> CSV + Excel
test_scraper.py     offline pytest suite (fake session, no network)
output/books.csv    real output from a full run
output/run.txt      log of that run
requirements.txt    requests, beautifulsoup4, openpyxl, pytest
```

## Tests
```bash
python -m pytest -q
```
Runs on every push in [GitHub Actions](https://github.com/Ashton-Standridge/web-scraper-demo/actions/workflows/tests.yml).

## How this maps to client work
| If you need… | This demo shows… |
|---|---|
| Product, directory or listing data in a spreadsheet | Multi-page collection into CSV/Excel |
| A scraper that doesn't break on one bad request | Retries with backoff and polite delays |
| Clean data, not raw dumps | Typed fields, dedupe and sorting |
| Something you can rerun next month | A documented CLI with tests |

Only scrape sites you are allowed to scrape: check the terms of service and robots.txt first.

## Need this for your data?
Need data collected from a site into a spreadsheet? [Message me on Upwork](https://www.upwork.com/freelancers/~01d2f0883f3e7f03a4). More samples: [https://ashton-standridge.github.io/](https://ashton-standridge.github.io/)

## License
[MIT](LICENSE) © 2026 Ashton Standridge (Venture Studio Arts)
