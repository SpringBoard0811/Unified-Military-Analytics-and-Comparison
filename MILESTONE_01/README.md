# 🎯 Milestone 01 — Data Acquisition & Preparation

Milestone 01 focuses on collecting and preparing global military statistics for analytical use.
The goal of this stage is to transform **unstructured web-based military data into a clean and structured dataset** that can be used for further analysis and dashboard development.

This milestone establishes the **data foundation of the project** by building a reliable dataset covering **140+ countries**.

---

# 🛰 Module 01 — Data Scraping

## 🎯 Objective

Collect country-specific military statistics using the list of URLs provided in the dataset links file.

The scraping process gathers important military indicators from publicly available defense information pages.

---

## 📂 Data Source

All country URLs are stored in the following file:

```
links_for_military_data.txt
```

Each link points to a webpage containing military statistics such as defense budget, personnel strength, and equipment inventory.

The data is collected from:

🌐 GlobalFirepower.com

---

## 📌 Activities Performed

✔ Load country URLs from `links_for_military_data.txt`

✔ Send automated requests to retrieve webpage content

✔ Parse webpage structure to extract military statistics

✔ Capture key indicators including:

* ✈️ Aircraft inventory
* 🛡 Tank strength
* 👥 Active military personnel
* 🚢 Naval fleet size
* 💰 Defense budget

✔ Store extracted data in a structured dataset

---

## 💾 Outputs

| Component         | Description                     |
| ----------------- | ------------------------------- |
| Scraping Notebook | `scrape_military_metrics.ipynb` |
| Raw Dataset       | `military_raw_data.csv`         |

The raw dataset contains military statistics collected directly from the source webpages.

---

# 🧹 Module 02 — Data Cleaning & Formatting

## 🎯 Objective

Convert the raw scraped dataset into a **clean and structured dataset suitable for analysis and visualization**.

Raw data collected from web pages may contain formatting symbols, inconsistent structures, or missing values. This module standardizes the dataset.

---

## 📌 Activities Performed

✔ Remove formatting characters such as:

* commas `,`
* percentage symbols `%`
* plus signs `+`

✔ Convert values into numeric data types

✔ Standardize column names across the dataset

Example columns include:

```
country
active_personnel
aircraft_total
tanks
naval_assets
defense_budget
```

✔ Handle missing values

✔ Ensure consistent dataset structure

---

## 💾 Outputs

| Component         | Description            |
| ----------------- | ---------------------- |
| Cleaning Notebook | `Clean_data.ipynb`     |
| Clean Dataset     | `military_cleaned.csv` |

The cleaned dataset serves as the **input for further analytics and KPI generation in later milestones**.

---

# 📊 Data Quality Checks

To ensure dataset reliability:

✔ Data collected for **140+ countries**

✔ Numeric values standardized for analysis

✔ Dataset structured into a consistent tabular format

---

# 🚀 Outcome of Milestone 01

At the end of this milestone, the project produces:

✔ A global dataset containing military capability metrics
✔ Clean and standardized data ready for analysis
✔ A reproducible workflow for web scraping and data preparation

```
Raw Web Data
      ↓
Structured Raw Dataset
      ↓
Clean Analytical Dataset
```

The cleaned dataset will be used in the next milestone for **analytical KPI generation and dashboard development**.
