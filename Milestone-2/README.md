# 📊 Milestone 2 – KPI Engineering & Dashboard Planning
## Unified Military Analytics and Comparison Dashboard

---

## 📌 Project Overview

The **Unified Military Analytics and Comparison Dashboard** aims to provide an analytical platform for evaluating and comparing global military capabilities.

**Milestone 2** focuses on transforming the cleaned military dataset into **analytical Key Performance Indicators (KPIs)** and preparing the data for interactive visualization within **Power BI dashboards**.

In this stage, KPI metrics were generated directly within **Power BI using DAX (Data Analysis Expressions)** to enable dynamic analysis and interactive filtering. This milestone also includes the **initial design and planning of the dashboard structure**, which will be expanded in later development phases.

This milestone ensures that the dataset evolves from raw numerical statistics into **actionable analytical insights**.

---

# ⚙️ KPI Engineering using DAX

In this module, new analytical metrics were created directly within **Power BI** using **DAX formulas**. These KPIs enable deeper comparative analysis of military strength, resource efficiency, and national defense investment.

### Key KPIs Implemented

#### 📊 Assets per Capita

Measures the relationship between military equipment and available manpower.

**Formula**

Assets per Capita =
('clean_military_data'[total_aircraft] +
 'clean_military_data'[tanks] +
 'clean_military_data'[naval_assets])
 /
 'clean_military_data'[total_manpower]

---

### 💰 Budget-to-GDP Ratio

Represents the proportion of a country’s economic output allocated to defense spending.

**Formula**

Budget-to-GDP Ratio =
'clean_military_data'[defense_budget] / 'clean_military_data'[gdp]

---

### 🌐 Power Index Rank Gap

Measures the difference between a country's military power ranking and the top-ranked nation.

**Formula**

Power Index Rank Gap =
RANKX(
    ALL('clean_military_data'),
    'clean_military_data'[p_rank]
)

MIN('military_cleaned'[p_rank])

These KPIs allow the dashboard to highlight **military efficiency, strategic investment, and relative defense strength among countries.**

---

# 🌍 Data Enrichment

To enable more advanced comparative analytics, additional metadata fields were incorporated into the dataset.

### Added Metadata Fields

- **Continent**
- **Geographic Region**
- **Military Alliance Indicators** (e.g., NATO membership)

These attributes allow the dashboard to support:

- Regional analysis
- Alliance comparisons
- Global military grouping insights

---

# 📊 Dashboard Planning

The dashboard architecture was designed to provide multiple analytical perspectives on global military capabilities.

The following dashboard modules were conceptualized to guide the final visualization system.

## Planned Dashboard Modules

### Data/Sample_1.png

### ⚡ Quick Stats
Global overview of military KPIs and aggregated statistics.

### 🌍 Nation Overview
Detailed military profile for individual countries.

### ⚖️ Compare Powers
Multi-country comparison of defense metrics.

### 🤝 Coalition Builder
Simulation and analysis of combined military alliances.

These modules provide both **high-level strategic insights** and **detailed country-level analysis.**

---

# 🛠 Technologies Used

The following tools and technologies were used during this milestone:

- **Python** – Data processing and preparation
- **Pandas** – Dataset manipulation and transformation
- **Jupyter Notebook** – Development and documentation
- **Power BI** – Interactive dashboard creation
- **DAX (Data Analysis Expressions)** – KPI calculations and analytical measures

---

# 📈 Milestone Outcome

At the end of **Milestone 2**, the project delivers:

- A **KPI-enriched military dataset**
- **Dynamic KPI calculations** implemented using DAX
- A **structured Power BI dashboard prototype**
- Defined dashboard modules for advanced military analytics

This milestone establishes the **analytical layer required for building a comprehensive global military comparison platform.**
