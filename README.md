# 🌍 Unified Military Analytics & Comparison Dashboard

## 📊 Project Overview

The **Unified Military Analytics and Comparison Dashboard** is a data analytics project designed to analyze and compare the military strength of different countries using various military metrics. The project integrates multiple datasets and visualizes them through an interactive **Power BI dashboard** to provide meaningful insights into global military capabilities.

This project focuses on data cleaning, integration, analysis, and visualization of military-related statistics such as **Active Personnel, Combat Aircraft, Submarines, and Defense Budget**.

---

## 🎯 Objectives

* To collect and integrate military data from multiple sources.
* To clean and preprocess raw datasets for analysis.
* To compare military strength across different countries.
* To visualize military metrics through an interactive dashboard.
* To enable easy comparison of global defense capabilities.

---

## 📁 Dataset Description

### 1️⃣ Military Raw Data

The **Military_raw_data.xlsx** file contains the base dataset with military statistics for multiple countries.
It includes attributes such as:

* Country Name
* Active Personnel
* Combat Aircraft
* Submarines
* Defense Budget
* Additional military capability indicators

### 2️⃣ Military Collected Data

The **military_raw_collected.xlsx** file acts as a reference dataset used to:

* Add missing countries after Greece
* Fill missing column values
* Validate existing data
* Improve dataset completeness

Both datasets were merged and cleaned to produce a **complete dataset for analysis**.

---

## 🧹 Data Processing Steps

The following steps were performed to prepare the dataset:

1. **Data Collection**

   * Military statistics collected from multiple sources.

2. **Data Cleaning**

   * Removed duplicate countries
   * Handled missing values
   * Standardized country names

3. **Data Integration**

   * Combined `Military_raw_data` and `military_raw_collected` datasets.

4. **Data Completion**

   * Added countries alphabetically after **Greece**.
   * Filled missing column values.

5. **Final Dataset Preparation**

   * Ensured no null values
   * Maintained consistent data structure

---

## 📊 Dashboard Features (Power BI)

The Power BI dashboard provides interactive visualizations including:

### 🔹 KPI Cards

* Total Countries
* Total Active Personnel
* Total Combat Aircraft
* Total Submarines
* Total Defense Budget

### 🔹 Visualizations

* Top Countries by Active Personnel
* Defense Budget Comparison
* Aircraft vs Submarines Scatter Analysis
* Country-wise Military Strength Comparison

### 🔹 Interactive Filters

* Country selection
* Personnel range filtering
* Defense budget comparison

---

## 🛠️ Tools & Technologies Used

| Tool                         | Purpose                                 |
| ---------------------------- | --------------------------------------- |
| **Power BI**                 | Data Visualization & Dashboard          |
| **Excel**                    | Data Storage & Cleaning                 |
| **Python / Data Processing** | Data preprocessing                      |
| **GitHub**                   | Version Control & Project Documentation |

---

## 📂 Project Structure

```
Unified-Military-Analytics-Dashboard
│
├── datasets
│   ├── Military_raw_data.xlsx
│   └── military_raw_collected.xlsx
│
├── dashboard
│   └── Military_Analytics_Dashboard.pbix
│
├── documentation
│   └── project_report.pdf
│
└── README.md
```

---

## 📈 Key Insights

* Countries with the largest military personnel can be easily identified.
* Defense budgets vary significantly across nations.
* Some countries have stronger air capabilities while others focus on naval strength.
* The dashboard allows dynamic comparison between different military metrics.

---

## 🚀 Future Improvements

* Add real-time defense data updates.
* Include geographical visualization (map-based analysis).
* Expand dataset with additional military indicators.
* Integrate machine learning models for predictive analysis.

---

## 👩‍💻 Author

**Kondaveeti Prathyusha**

---

## 📜 License

This project is for **academic and educational purposes**.
