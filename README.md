# Task 1 – Web Scraping (SAM AI Technologies)

## What this project does
Scrapes book data (title, price, rating, availability) from `books.toscrape.com`
— a website built specifically for practicing web scraping legally and safely —
and saves it as a clean CSV dataset.

This satisfies every requirement on the task slide:
- Uses a Python library (BeautifulSoup) to extract data ✅
- Identifies and collects a relevant dataset from public web pages ✅
- Handles HTML structure and pagination (multiple pages) ✅
- Produces a custom dataset (CSV) ready for analysis ✅

---

## How to run it yourself (takes 2 minutes)

### Step 1 — Install Python
If you don't have Python installed, download it from https://python.org
(Check "Add Python to PATH" during install on Windows.)

### Step 2 — Open a terminal in this folder
- Windows: Shift + Right-click inside the folder → "Open PowerShell here"
- Mac/Linux: `cd path/to/task1_webscraping`

### Step 3 — Install the required libraries
```
pip install -r requirements.txt
```

### Step 4 — Run the scraper
```
python scraper.py
```

You'll see output like:
```
Scraping page 1: http://books.toscrape.com/catalogue/page-1.html
Scraping page 2: http://books.toscrape.com/catalogue/page-2.html
...
Done. Scraped 100 books into 'books_dataset.csv'
```

### Step 5 — Check your result
Open `books_dataset.csv` in Excel or Google Sheets. You'll see columns:
`title | price_gbp | rating_out_of_5 | availability`

---

## How the code works (for your submission notes / viva)

| Step in code | What it does |
|---|---|
| `get_page_html()` | Sends an HTTP request and downloads the page's raw HTML |
| `parse_books()` | Uses BeautifulSoup to find each book's tags and pull out title, price, rating, stock status |
| `save_to_csv()` | Writes the collected list of dictionaries into a structured CSV file |
| `main()` | Loops through 5 pages (pagination), scrapes each, waits 1 second between requests (politeness/rate-limiting), then saves everything |

## Customizing for a different dataset
To scrape a different site instead of books, change:
1. `BASE_URL` to the target site's page pattern
2. The CSS selectors inside `parse_books()` (find these using your browser's
   "Inspect Element" tool — right-click any item on the page → Inspect)

## Ethics note (mention this in your submission — it shows professionalism)
- Only scrape publicly available data.
- Always check a site's `robots.txt` (e.g. `site.com/robots.txt`) before scraping.
- Don't scrape data behind logins or paywalls.
- Add delays between requests so you don't overload the server.

