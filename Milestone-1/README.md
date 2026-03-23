# 🛰️ Module 1: Data Scraping & Collection

## 🎯 Objective

This module focuses on collecting **global military data** from multiple country-specific web pages and converting it into a structured dataset.

---

## 🌍 Data Source

* Input file: `links_for_military_data.txt`
* Contains URLs for each country's military statistics page

---

## ⚙️ Process Workflow

```
URL List → Web Scraping → Data Extraction → Raw Dataset
```

---

## 📌 Key Metrics Extracted

| Category       | Metrics                          |
| -------------- | -------------------------------- |
| 🪖 Manpower    | Total Manpower, Active Personnel |
| ✈️ Air Power   | Total Aircraft, Fighter Aircraft |
| 🚢 Naval Power | Naval Assets                     |
| 🛡️ Land Power | Tanks                            |
| 💰 Economy     | Defense Budget                   |

---

## 🛠️ Technologies Used

* Python 🐍
* BeautifulSoup 🌐
* Requests 📡
* Pandas 📊

---

## 🔍 Scraping Strategy

✔ Read all URLs from file
✔ Send HTTP requests with headers
✔ Parse HTML content
✔ Extract metric blocks
✔ Store data in structured format
✔ Handle failures gracefully

---

## 📂 Output Files

| File                         | Description         |
| ---------------------------- | ------------------- |
| `military_raw_data.csv`      | Raw scraped dataset |
| `scrape_military_metrics.py` | Scraping script     |

---

## 📊 Sample Output

| Country | Rank | Aircraft | Tanks | Budget |
| ------- | ---- | -------- | ----- | ------ |
| India   | 4    | 2229     | 4614  | 75B    |

---

## ✅ Evaluation Criteria

* ✔ ≥ 95% successful scraping
* ✔ 140+ countries covered
* ✔ Structured dataset generated

---

## 🚀 Outcome

✔ Automated data collection pipeline
✔ Global military dataset created
✔ Ready for cleaning & processing

---

## 👩‍💻 Author

**Shanmukhi Sudha**
