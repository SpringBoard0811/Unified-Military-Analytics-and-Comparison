# Milestone 1 – Data Collection & Preparation

## Unified Military Analytics and Comparison Dashboard

---

## 📌 Project Overview

The **Unified Military Analytics and Comparison Dashboard** aims to analyze and compare global military capabilities across countries using structured datasets.

**Milestone 1** focuses on building the data foundation by collecting, organizing, and cleaning military data from publicly available sources.

---

## 🔄 Data Pipeline

```
Web Scraping → Raw Dataset → Data Cleaning → Final Dataset
```

---

## 🧩 Modules in Milestone 1

### ⚙️ Module 1 – Data Collection (Web Scraping)

This module is responsible for extracting military data from multiple web sources.

* URLs are sourced from `links for military data.txt`
* Country-wise military data is scraped
* Multiple metrics are combined into a single dataset

#### 🔹 Output

* `military_raw_data.csv`

---

### 🧹 Module 2 – Data Cleaning & Structuring

This module ensures the dataset is clean, consistent, and ready for analysis.

#### 🔹 Key Tasks

* Removed formatting symbols (`,`, `%`, `+`, etc.)
* Converted values into numeric format
* Standardized column names
* Handled missing/null values

#### 🔹 Outputs

* `military_selected.csv` (filtered dataset)
* `military_selected_clean.csv` (final cleaned dataset)

---

## 📊 Key Metrics Included

* ✈ Aircraft Strength
* 🪖 Active & Reserve Personnel
* 🚢 Naval Assets
* 🛡 Defense Budget
* 🚜 Tanks & Armored Vehicles

---

## 📁 Folder Structure

```
Milestone_1/
│
├── Military_Analysysis_Milestone1.ipynb   # Main notebook (scraping + cleaning)
├── links for military data.txt           # Source URLs
├── military_raw_data.csv                 # Raw dataset
├── military_selected.csv                 # Filtered dataset
├── military_selected_clean.csv           # Final cleaned dataset
└── README.md                             # Documentation
```

---

## 🛠 Technologies Used

* Python
* Pandas
* BeautifulSoup
* Requests
* Jupyter Notebook

---

## 📈 Milestone Outcome

At the end of Milestone 1, the project produces:

* **Raw Dataset:** `military_raw_data.csv`
* **Processed Dataset:** `military_selected.csv`
* **Final Clean Dataset:** `military_selected_clean.csv`

This dataset is fully prepared for further analytical processing.

---

## 🚀 Next Steps (Milestone 2)

* KPI Engineering
* Feature Selection Optimization
* Metadata Enrichment
* Advanced Data Analysis
* Dashboard Development

---

## 📌 Summary

Milestone 1 establishes a robust data pipeline that transforms raw scraped data into a clean and structured dataset, forming the foundation for future analytics and dashboard development.
