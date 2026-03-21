# 📊 Milestone 2 – KPI Engineering & Dashboard Planning

**Project:** Global Military Analytics & Comparison Dashboard

---

## 📌 Overview

Milestone 2 focuses on transforming the cleaned military dataset into analytical features (KPIs) and preparing it for visualization. This stage includes feature selection, KPI engineering, data enrichment, and planning the structure and interaction flow of the final dashboard.

---

## ⚙️ KPI Engineering

The following KPIs were created from the dataset to enable deeper analysis:

* **Rank Gap (`rank_gap`)** – Difference between a country’s power index rank and the top-ranked country
* **Assets per Capita (`assets_per_capita`)** – Ratio of total military assets to active personnel
* **Budget to GDP Ratio (`budget_to_gdp_ratio`)** – Defense budget as a proportion of GDP

These KPIs help evaluate:

* Relative military standing
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

This ensures clarity and improves performance for analysis and visualization.

---

## 🔍 Data Enrichment

To improve usability:

* Standardized column names
* Cleaned and formatted numerical values
* Ensured consistent data types
* Integrated KPI columns into the dataset

---

## 📊 Data Preparation

The dataset was structured for visualization:

* Combined base metrics with KPIs
* Organized in a clean tabular format
* Prepared for direct use in visualization tools

Final outputs:

```
military_kpi.csv
military_final.csv
```

---

## 📈 Dashboard Planning

### Planned Dashboard Modules:

* **Quick Stats**

  * Overview of global military KPIs
  * Summary cards for key indicators

* **Country Overview**

  * Detailed military profile of each country
  * Breakdown of manpower, equipment, and budget

* **Comparison Dashboard**

  * Side-by-side country comparison
  * Visual comparison using charts

---

### 📊 Visualizations:

* Bar Charts → Country comparisons
* KPI Cards → Highlight key values
* Tables → Detailed data view

---

### 🔄 Interaction Flow:

* Country-based filtering
* KPI-based comparisons
* Drill-down into specific country data

---

### 🧪 Prototyping:

* Created basic wireframes (paper/Figma)
* Planned layout and navigation flow
* Designed interaction between dashboard sections

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
* Structured data ready for dashboard visualization
* Defined dashboard layout and interaction plan

---

## 👩‍💻 Author

Kavya Vudarla
