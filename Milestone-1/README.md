# 🎯 Milestone 1 – Data Collection & Preparation

This milestone focuses on gathering global military capability data and preparing it for analytical use.  
The objective is to build a **clean, well-structured dataset** that can later support visualization dashboards and advanced analytics.

The output of this stage is a **processed dataset containing military indicators for 140+ countries**, ready for further analysis in upcoming milestones.

---

# 🛰️ Data Collection

Military capability statistics are collected from the URLs listed in the following file:
`links_for_military_data.txt`

Each webpage contains country-level defense metrics such as military manpower, equipment inventory, and economic indicators related to defense capability.

### Key Tasks

✔ Scrape military data for **140+ countries**  
✔ Extract major defense indicators including:

- ✈️ Total Aircraft  
- 🛡️ Tanks  
- 💰 Defense Budget  
- 👥 Active Military Personnel  
- 🚢 Naval Assets  

✔ Parse structured information from each webpage  
✔ Store the extracted data into a **CSV dataset**  
✔ Optionally store HTML pages locally for **debugging and verification**

---

# 📦 Deliverables

| Item | Description |
|-----|-------------|
| Script | `scrape_military_metrics.py` |
| Raw Dataset | `military_raw_data.csv` |

---

# 🧹 Data Cleaning & Structuring

The raw scraped dataset undergoes several preprocessing steps to ensure it is suitable for analytics and visualization.

### Data Preparation Tasks

✔ Remove symbols such as **commas, percentage signs, plus symbols, and other special characters**  
✔ Convert extracted values into **numeric formats**  
✔ Standardize column names (e.g., `total_aircraft`, `active_personnel`)  
✔ Handle missing or null values  
✔ Format the dataset for compatibility with **data visualization tools**

---

# 📦 Deliverables

| Item | Description |
|-----|-------------|
| Clean Dataset | `military_cleaned.csv` |
| Notebook | `clean_data.ipynb` |

---

# 📊 Evaluation Criteria

The milestone will be considered successful if the following conditions are met:

✔ **≥ 95% URL scraping success rate**  
✔ Data successfully collected for **140+ countries**  
✔ **Less than 2% missing values** after the cleaning process  
✔ Dataset prepared and validated for **analytics and dashboard development**

---

# 🚀 Outcome
Raw Military Data
↓
Cleaned & Structured Dataset

The resulting dataset forms the **foundation for the next milestone**, where additional **analytical KPIs will be engineered and integrated into interactive dashboards.**
