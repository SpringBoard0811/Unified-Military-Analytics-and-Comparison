# 🛰️ Milestone 1

## Data Collection & Preparation

<div align="center">

### 🌍 Unified Military Analytics & Comparison Dashboard

### Building the Foundation Dataset for Global Military Analytics

👩‍💻 **Author:** Shanmukhi

</div>

---

# 🎯 Milestone Objective

Milestone 1 focuses on **collecting and preparing global military data** required for the analytics pipeline.

The goal of this milestone is to transform **unstructured military statistics into a clean and structured dataset** ready for further analysis and visualization.

This stage establishes the **data foundation for the entire project**.

---

# 📂 Data Source

All military statistics are collected from country-level pages listed in the file:

```
links_for_military_data.txt
```

Each link corresponds to a specific **military capability metric page**.

### Examples of metrics extracted

✈️ Total Aircraft
🛡️ Total Tanks
🚢 Naval Fleet Size
👥 Active Military Personnel
👥 Reserve Personnel
💰 Defense Budget
🌍 Population

---

# 🛰️ Module 1 — Web Scraping

### Objective

Automatically collect military statistics for **140+ countries**.

### Tasks Performed

✔ Read dataset links from `links_for_military_data.txt`
✔ Access each webpage using HTTP requests
✔ Parse structured HTML tables containing country metrics
✔ Extract country-level military statistics
✔ Store extracted data into a structured dataset

---

### Output Dataset

```
military_raw_data.csv
```

This dataset contains **raw scraped military statistics** before any preprocessing.

---

# 🧹 Module 2 — Data Cleaning & Structuring

### Objective

Convert the raw dataset into a **clean and standardized format** suitable for data analysis and visualization.

---

### Cleaning Operations

| Operation                      | Example                         |
| ------------------------------ | ------------------------------- |
| Remove commas                  | 1,500,000 → 1500000             |
| Remove currency symbols        | $800,000,000 → 800000000        |
| Remove extra symbols           | +500 → 500                      |
| Convert text to numeric values | "1500000" → 1500000             |
| Standardize column names       | Total Aircraft → total_aircraft |

---

# 📊 Final Dataset

After preprocessing, the cleaned dataset generated is:

```
military_cleaned.csv
```

This dataset is **fully structured and ready for analytics and dashboard visualization**.

---

# 📁 Milestone 1 Structure

```
milestone-1
│
├── links_for_military_data.txt
├── scrape_military_metrics.py
├── military_raw_data.csv
├── clean_data.ipynb
└── military_cleaned.csv
```

---

# 📊 Milestone Evaluation Checklist

| Requirement                           | Status |
| ------------------------------------- | ------ |
| Successful scraping of 140+ countries | ✔      |
| Raw dataset generation                | ✔      |
| Clean structured dataset              | ✔      |
| Numeric formatting consistency        | ✔      |
| Dataset ready for visualization       | ✔      |

---

# 🚀 Milestone Outcome

```
Raw Military Data
        ↓
Clean Structured Dataset
        ↓
Ready for Analytics & Dashboard Development
```

Milestone 1 successfully prepares the **core dataset** that will be used in the next stages of the project:

📈 KPI Engineering
📊 Military Analytics
🌍 Interactive Dashboard Development

---

<div align="center">

### 👩‍💻 Created by **Shanmukhisudha**

</div>
