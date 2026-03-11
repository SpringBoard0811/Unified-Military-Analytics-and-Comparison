# 🎯 Milestone 1 – Data Collection & Preparation


This milestone focuses on **collecting global military data and preparing it for analysis**.
The output will be a **clean, structured dataset** ready for visualization and analytics (e.g., Tableau dashboards).

---

# 🛰️ Module 1: Scraping Setup and Execution

## 🎯 Objective

Collect **country-level military statistics** from the URLs provided in the dataset links file.

---

## 📂 Data Source

All URLs are provided in:

`links_for_military_data.txt`

This file contains **country-specific pages** containing military statistics such as aircraft, tanks, defense budgets, and personnel.

---

## 📌 Tasks Performed

✔ Use `links_for_military_data.txt` as the source list of URLs
✔ Scrape **country-level military metrics** from each webpage
✔ Extract key statistics such as:

* ✈️ Total Aircraft
* 🛡️ Total Tanks
* 💰 Defense Budget
* 👥 Active Personnel
* 🚢 Naval Assets 

✔ Parse structured metric blocks from the webpage
✔ Store extracted data in a structured CSV dataset
✔ Save per-country HTML files for debugging (optional)

---

## 💾 Deliverables

| Item            | Description                  |
| --------------- | ---------------------------- |
| **Script**      | `scrape_military_metrics.py` |
| **Raw Dataset** | `military_raw_data.csv`      |

---

## 📊 Evaluation Criteria

✔ **≥ 95% URL success rate** from the provided list
✔ Military metrics successfully parsed for **140+ countries**
✔ Data stored in **consistent structured format**

---

# 🧹 Module 2: Data Cleaning and Structuring

## 🎯 Objective

Transform the **raw scraped dataset** into a **clean and standardized format** suitable for data analysis and visualization.

---

## 📌 Tasks Performed

✔ Clean textual numeric values by removing:

* commas `,`
* percentage symbols `%`
* plus signs `+`
* other special characters
✔ Convert metric values to **numeric formats**
✔ Standardize column names for consistency

Example column naming:

```
total_aircraft
total_tanks
active_personnel
defense_budget
naval_assets
```

✔ Handle **missing/null values** appropriately
✔ Ensure dataset compatibility with **Tableau visualization**

---

## 💾 Deliverables

| Item                    | Description            |
| ----------------------- | ---------------------- |
| **Clean Dataset**       | `military_cleaned.csv` |
| **Processing Notebook** | `clean_data.ipynb`     |

---

## 📊 Evaluation Criteria

✔ **< 2% missing/null values** after cleaning
✔ No structural or formatting errors in dataset
✔ Dataset ready for **Tableau visualization and analysis**

---

# 📈 Final Output of Milestone 1

By the end of this milestone we will have:

✔ 🌍 Global military metrics dataset
✔ 📊 Clean and structured data ready for analysis
✔ 🔁 Reproducible pipeline for scraping and preprocessing
✔ 📂 Dataset ready for use in **visual analytics and dashboards**

---

# 🚀 Outcome

Raw Military Data → **Clean Analytical Dataset**
Milestone 1 files
