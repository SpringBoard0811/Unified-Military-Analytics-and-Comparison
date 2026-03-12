# 🎯 Milestone 1 – Data Collection & Preparation

This milestone focuses on **collecting global military data and preparing it for analysis**.
The output is a **clean and structured dataset** ready for visualization and analytics dashboards.

---

## 🛰️ Data Collection

Military statistics are collected from the URLs listed in:

`links_for_military_data.txt`

Each page contains country-level metrics such as aircraft, tanks, defense budgets, and personnel.

### Tasks

✔ Scrape military data for **140+ countries**
✔ Extract key metrics such as:

* ✈️ Total Aircraft
* 🛡️ Tanks
* 💰 Defense Budget
* 👥 Active Personnel
* 🚢 Naval Assets

✔ Parse structured data from each webpage
✔ Store the results in a **CSV dataset**
✔ Optionally save HTML files for debugging

### Deliverables

| Item        | Description                  |
| ----------- | ---------------------------- |
| Script      | `scrape_military_metrics.py` |
| Raw Dataset | `military_raw_data.csv`      |

---

## 🧹 Data Cleaning & Structuring

The scraped dataset is cleaned and standardized to make it suitable for analytics.

### Tasks

✔ Remove symbols such as `, % +` and other special characters
✔ Convert values to numeric formats
✔ Standardize column names (e.g., `total_aircraft`, `active_personnel`)
✔ Handle missing or null values
✔ Prepare dataset for dashboard tools

### Deliverables

| Item          | Description            |
| ------------- | ---------------------- |
| Clean Dataset | `military_cleaned.csv` |
| Notebook      | `clean_data.ipynb`     |

---

## 📊 Evaluation Criteria

✔ ≥ **95% URL scraping success rate**
✔ Data collected for **140+ countries**
✔ **< 2% missing values** after cleaning
✔ Dataset ready for visualization

---

## 🚀 Outcome

Raw Military Data → **Clean Analytical Dataset**

This dataset becomes the **foundation for the next milestone**, where KPIs will be engineered and dashboards will be developed.
