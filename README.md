# 📱 Amazon Mobile Scraper 🔍

A simple **web scraper** built using **Selenium** and **BeautifulSoup** to extract data of **mobile phones under ₹20,000** from Amazon India 🇮🇳.

---

## 🚀 Project Overview

This project performs 3 main tasks:

1. **Scrape** mobile listings from Amazon using Selenium.
2. **Save HTML pages** locally for each product.
3. **Extract data** (title, price, and link) using BeautifulSoup.
4. **Export** the data to a CSV file. ✅

---

## 📂 Files Included

- `main.py` — Displays scraped product text from Amazon.
- `project.py` — Saves each product’s HTML to the `data/` folder.
- `collection.py` — Parses saved HTML files and writes data to `data.csv`.

---

## ⚙️ How to Use

1. **Install required packages**:
   ```bash
   pip install selenium beautifulsoup4 pandas
   ```
2. **Run scraper to fetch and store product HTML**:
   ```bash
   python project.py
   ```
3. **Collect product data from saved HTML**:
   ```bash
   python collection.py
   ```
4. **🎉 Your final output will be in data.csv.**

---

## 📌 Notes
Make sure you have Google Chrome and ChromeDriver installed.

Create a data/ folder before running project.py.

You can change the query to scrape other product types.

---

## 📊 Output Sample
```makefile
Title: Samsung Galaxy M35 5G
Price: 18,499
Link: https://www.amazon.in/...
```

---

## 🛠️ Tech Used
Python 🐍

Selenium

BeautifulSoup

Pandas

---

## 📁 Author
Made with 💻 by Adithya Salian
