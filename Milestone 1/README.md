# Milestone 1 – Data Collection & Preparation

## Unified Military Analytics and Comparison Dashboard

---

## 📌 Project Overview

The **Unified Military Analytics and Comparison Dashboard** aims to develop an analytical platform for exploring and comparing global military capabilities across countries.

The platform integrates structured military datasets and interactive dashboards to provide insights into defense strength, resource distribution, and global military rankings.

**Milestone 1** focuses on the **data acquisition and preparation stage**, where military statistics are collected from publicly available sources, processed, and converted into structured datasets ready for analysis and visualization.

---

## 🔄 Data Pipeline

```
Web Scraping → Raw Dataset → Feature Selection → Data Cleaning → Final Dataset
```

---

## 🧩 Modules in Milestone 1

### ⚙️ Module 1 – Scraping Setup and Execution

This module implements the automated web scraping pipeline used to collect global military statistics.

The scraping process uses **Global Firepower** as the centralized data source. Multiple URLs corresponding to different military metrics (aircraft, tanks, naval assets, budgets, manpower, etc.) are accessed and processed.

The system retrieves country-level data, parses relevant sections from each webpage, and stores the extracted information in a structured format.

#### 🔹 Key Tasks

* Automated scraping of military statistics webpages
* Retrieval of URLs from source list
* Extraction of country-level military metrics
* HTML parsing using BeautifulSoup
* Optional saving of raw HTML for debugging
* Structuring extracted data into CSV format

#### 📦 Deliverable

* `Military_raw_data.csv`

#### 📊 Evaluation Criteria

* ≥95% successful URL retrieval
* Accurate parsing of metric blocks
* Data extracted for 140+ countries

---

### 🧹 Module 2 – Data Cleaning and Structuring

This module transforms the raw dataset into a clean and analysis-ready format.

Web-scraped data often contains inconsistencies such as symbols, formatting issues, and missing values. This stage ensures the dataset is standardized and reliable.

#### 🔹 Key Tasks

* Removing formatting symbols (`,`, `%`, `+`, etc.)
* Converting values to numeric format
* Standardizing column names
* Handling missing/null values
* Preparing structured dataset for analytics

#### 📦 Deliverable

* `Final_Military_Data.csv`

#### 📊 Evaluation Criteria

* <2% missing/null values
* Consistent numeric formatting
* No structural/schema errors

---

## 📊 Key Military Metrics Collected

The dataset includes:

* ✈ Total Aircraft
* 🪖 Active Military Personnel
* 🪖 Reserve Personnel
* 🚢 Naval Assets
* 🛡 Defense Budget
* 🚜 Tank Strength
* 🌐 Global Military Power Ranking

---

## 📁 Folder Structure

```
Milestone_1/
│
├── Milestone_1.ipynb              # Scraping and preprocessing notebook
├── Military_raw_data.csv          # Raw dataset
├── Final_Military_Data.csv        # Cleaned dataset
└── README.md                      # Documentation
```

---

## 🛠 Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* Jupyter Notebook

---

## 📈 Milestone Outcome

At the end of Milestone 1, two datasets are produced:

* **Raw Dataset:** `Military_raw_data.csv`
* **Final Dataset:** `Final_Military_Data.csv`

The cleaned dataset serves as the foundation for further analysis and dashboard development.

---

## 🚀 Next Steps (Milestone 2)

* Feature engineering and derived metrics
* KPI development
* Comparative country analysis
* Interactive dashboard creation (Power BI)

---

## 📌 Summary

Milestone 1 establishes the **core data foundation** required to build an intelligent military analytics dashboard capable of delivering meaningful global defense insights.
