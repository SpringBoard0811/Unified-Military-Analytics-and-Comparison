# 📊 Milestone 2 – KPI Engineering & Dashboard Planning

**Project:** Global Military Analytics & Comparison Dashboard

---

## 📌 Overview

Milestone 2 focuses on transforming the cleaned military dataset into analytical features (KPIs) and preparing it for visualization. This stage includes feature selection, KPI engineering, data enrichment, and planning the structure and interaction flow of the final dashboard.

---

## ⚙️ KPI Engineering

The following KPIs were created from the dataset:

* **Rank Gap (`rank_gap`)** – Difference between a country’s power index rank and the top-ranked country
* **Assets per Capita (`assets_per_capita`)** – Ratio of total military assets to active personnel
* **Budget to GDP Ratio (`budget_to_gdp_ratio`)** – Defense budget as a proportion of GDP

These KPIs help analyze:

* Relative military positioning
* Resource efficiency
* Economic investment in defense

---

## 🧩 Feature Selection

The dataset was reduced to the most relevant metrics:

* Country
* Power Index Rank
* Total Active Personnel
* Tanks
* Total Aircraft
* Fighter Aircraft
* Naval Assets
* Defense Budget
* GDP

---

## 🔍 Data Enrichment

To improve data usability and analytical context:

* Standardized column naming conventions
* Cleaned and formatted numeric values
* Ensured consistency across all records
* Integrated KPI columns into the dataset
* Added metadata fields for deeper analysis:

  * **Region**
  * **Continent**
  * **Alliance** (e.g., NATO or other groupings)

---

## 📊 Data Preparation

The dataset was structured for visualization:

* Combined selected metrics with KPIs
* Organized into a clean, tabular format
* Prepared for direct use in Power BI

Final outputs:

```
military_kpi.csv
military_final.csv
```

---

## 📈 Dashboard Planning

### Planned Dashboard Modules:

* **Quick Stats**

  * Global overview of key KPIs
  * Summary cards for major indicators

* **Nation Overview**

  * Detailed profile of a selected country
  * Breakdown of manpower, air, land, and naval strength
  * Display of KPIs specific to the selected nation

* **Compare Powers**

  * Side-by-side comparison of multiple countries
  * Visual comparison using charts and KPIs

* **Coalition Builder**

  * Simulated combined strength of selected countries
  * Aggregated metrics for alliances or groups
  * Comparison of coalition strength vs individual nations

---

### 📊 Visualizations:

* Bar Charts → Country comparisons
* KPI Cards → Highlight key metrics
* Tables → Detailed country-level data

---

### 🔄 Interaction Flow:

* Country selection filters
* Multi-country comparison selection
* Dynamic KPI updates based on selection
* Drill-down into individual country profiles
* Coalition-based aggregation for group analysis

---

### 🧪 Prototyping:

* Created wireframes (paper/Figma)
* Designed layout and navigation flow
* Defined transitions between dashboard views
* Tested interaction logic using sample data

---

## 📂 Files in Milestone 2

```
Military_Analysis_Milestone2.ipynb
military_kpi.csv
military_final.csv
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* Google Colab / Jupyter Notebook
* Power BI

---

## 📌 Output

* KPI-enriched dataset
* Structured data ready for visualization
* Defined multi-dashboard architecture
* Prototype for interactive military analytics dashboard

---
