# 📱 Amazon Mobile Scraper 🔍

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green?style=flat-square&logo=selenium)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-HTML%20Parsing-yellow?style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-black?style=flat-square&logo=pandas)
![Amazon](https://img.shields.io/badge/Amazon-IN-red?style=flat-square&logo=amazon)

---

A simple and efficient **web scraping project** using `Selenium` and `BeautifulSoup` to extract mobile phone data under ₹20,000 from **Amazon India** 🇮🇳 and export it to a clean `.csv` file for further analysis.

---

## 🚀 Features

- ✅ Scrapes mobile phone listings from Amazon India
- ✅ Stores product HTML files locally
- ✅ Extracts product **title**, **price**, and **link**
- ✅ Outputs data to a structured `data.csv` file

---

## 🗂️ Project Structure

```
amazon_mobile_scraper/
├── main.py # Display scraped product info
├── project.py # Fetch and save product HTML files
├── collection.py # Parse HTML and export to CSV
├── data/ # Folder storing HTML pages
└── data.csv # Final extracted output
```

---

## ⚙️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/amazon-mobile-scraper.git
cd amazon-mobile-scraper
```

### 2. Install Dependencies

```bash
pip install selenium beautifulsoup4 pandas
```

### 3. Make Sure You Have
✅ Google Chrome

✅ ChromeDriver (must match your Chrome version)

✅ A folder named data/ inside your project root

### 4. Run the Scripts
🔸 Step 1: Fetch and Save HTML Pages
```bash
python project.py
```
🔸 Step 2: Parse HTML Files and Save to CSV
```bash
python collection.py
```

### 5. 🎉 Check your output
Open data.csv to view the extracted data.

---

## 🧪 Sample Output
```bash
Title: Samsung Galaxy M35 5G
Price: ₹18,499
Link : https://www.amazon.in/...
```

---

## 🧰 Tech Stack

