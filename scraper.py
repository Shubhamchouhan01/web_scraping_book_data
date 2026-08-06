"""
Task 1: Web Scraping
Author: [shubham chouhan]
Date: 2026-08-06

Purpose:
    Extract book data (title, price, rating, availability) from
    books.toscrape.com — a public site built specifically for
    practicing web scraping — and save it as a clean CSV dataset.

Libraries used:
    - requests        : downloads the raw HTML of a webpage
    - BeautifulSoup    : parses HTML so we can search for tags/classes
    - csv              : writes structured data into a .csv dataset
"""

import requests
from bs4 import BeautifulSoup
import csv
import time

# -----------------------------------------------------------------
# STEP 1: Configuration
# -----------------------------------------------------------------
BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
TOTAL_PAGES = 5          # how many pages to scrape (site has 50, we'll do 5 for a clean sample)
OUTPUT_FILE = "books_dataset.csv"

# Star ratings on the site are written as CSS classes (One, Two, Three...)
# We convert them to numbers because numbers are more useful for analysis.
RATING_MAP = {
    "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5
}


def get_page_html(url):
    """STEP 2: Download the raw HTML of a single page."""
    headers = {"User-Agent": "Mozilla/5.0"}  # pretend to be a normal browser
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # stop if the page failed to load
    return response.text


def parse_books(html):
    """STEP 3: Extract book details from the page's HTML structure."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    # Every book on the page is inside an <article class="product_pod"> tag
    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]

        price_text = item.select_one(".price_color").text.strip()
        price = price_text.replace("£", "").replace("Â", "")

        availability = item.select_one(".availability").text.strip()

        # rating is stored like: <p class="star-rating Three">
        rating_class = item.select_one(".star-rating")["class"][1]
        rating = RATING_MAP.get(rating_class, None)

        books.append({
            "title": title,
            "price_gbp": price,
            "rating_out_of_5": rating,
            "availability": availability
        })

    return books


def save_to_csv(all_books, filename):
    """STEP 4: Save the collected data into a clean CSV dataset."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "price_gbp", "rating_out_of_5", "availability"])
        writer.writeheader()
        writer.writerows(all_books)


def main():
    """STEP 5: Loop through pages, scrape each one, and save the final dataset."""
    all_books = []

    for page_num in range(1, TOTAL_PAGES + 1):
        url = BASE_URL.format(page_num)
        print(f"Scraping page {page_num}: {url}")

        html = get_page_html(url)
        books = parse_books(html)
        all_books.extend(books)

        time.sleep(1)  # be polite — don't hammer the server with requests

    save_to_csv(all_books, OUTPUT_FILE)
    print(f"\nDone. Scraped {len(all_books)} books into '{OUTPUT_FILE}'")


if __name__ == "__main__":
    main()
