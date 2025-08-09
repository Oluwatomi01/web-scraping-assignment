import requests
from bs4 import BeautifulSoup
import csv
import time

# Target URL
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# Prepare CSV
with open("books.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Stock Availability"])

    # Loop through first 3 pages (as example)
    for page in range(1, 4):
        print(f"Scraping page {page}...")
        url = BASE_URL.format(page)
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            stock = book.find("p", class_="instock availability").text.strip()

            writer.writerow([title, price, stock])

        time.sleep(1)  # polite delay

print("Scraping complete. Data saved to books.csv")
