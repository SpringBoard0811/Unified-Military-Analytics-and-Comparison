# 📊 Milestone 2 – KPI Development & Dashboard Preparation
## Unified Military Analytics and Comparison Dashboard

---

## 📌 Project Overview

The **Unified Military Analytics and Comparison Dashboard** project is designed to create an analytical system for examining and comparing the military capabilities of countries across the world.

**Milestone 2** concentrates on converting the cleaned military dataset into **analytical Key Performance Indicators (KPIs)** and preparing the information for visualization through **Power BI dashboards**.

During this phase, KPI measures were developed directly in **Power BI using DAX (Data Analysis Expressions)**. This allows the dashboard to support dynamic filtering, interactive exploration, and deeper analytical insights. Additionally, the **basic layout and planning of the dashboard** were designed during this stage, which will be further enhanced in the next phases of development.

This milestone transforms raw military statistics into **meaningful and actionable analytical indicators**.

---

# ⚙️ KPI Creation using DAX

In this stage, several analytical metrics were implemented within **Power BI** using **DAX formulas**. These indicators help in performing detailed comparisons related to military capability, defense spending efficiency, and resource allocation.

### Key KPIs Implemented

#### 📊 Assets per Capita

This metric evaluates the relationship between the total military equipment available and the manpower capacity of a country.

**Formula**

Assets per Capita =
('clean_military_data'[total_aircraft] +
 'clean_military_data'[tanks] +
 'clean_military_data'[naval_assets])
 /
 'clean_military_data'[total_manpower]

---

### 💰 Budget-to-GDP Ratio

This KPI indicates the percentage of a country's economic output that is allocated to defense expenditure.

**Formula**

Budget-to-GDP Ratio =
'clean_military_data'[defense_budget] / 'clean_military_data'[gdp]

---

### 🌐 Power Index Rank Gap

This metric determines the difference between a country’s military ranking and the highest-ranked nation in the dataset.

**Formula**

Power Index Rank Gap =
RANKX(
    ALL('clean_military_data'),
    'clean_military_data'[p_rank]
)

MIN('military_cleaned'[p_rank])

These KPIs help the dashboard emphasize **defense efficiency, strategic investment levels, and relative military strength among countries.**

---

# 🌍 Data Enrichment

To support more comprehensive analysis, additional contextual information was added to the dataset.

### Added Metadata Fields

- **Continent**
- **Geographical Region**
- **Military Alliance Indicators** (for example, NATO membership)

Including these attributes enables the dashboard to perform:

- Regional comparisons
- Analysis of military alliances
- Grouped global military insights

---

# 📊 Dashboard Planning

The dashboard framework was planned to present multiple analytical perspectives related to global military power.

The following dashboard components were conceptualized to guide the final visualization design.

## Planned Dashboard Modules  
### Data/Sample_1.png

### ⚡ Quick Stats
Provides a high-level summary of global military KPIs and combined statistics.

### 🌍 Nation Overview
Displays detailed military information for individual countries.

### ⚖️ Compare Powers
Allows comparison of military capabilities across multiple countries.

### 🤝 Coalition Builder
Supports simulation and evaluation of combined military alliances.

These sections provide both **strategic overview insights and detailed country-level comparisons.**

---

# 🛠 Technologies Used

The following technologies were utilized in this milestone:

- **Python** – Data preparation and processing
- **Pandas** – Data manipulation and transformation
- **Jupyter Notebook** – Development and documentation
- **Power BI** – Interactive data visualization
- **DAX (Data Analysis Expressions)** – Creation of KPI measures

---

# 📈 Milestone Outcome

By the completion of **Milestone 2**, the project provides:

- A **military dataset enriched with analytical KPIs**
- **Dynamic KPI measures** created through DAX
- A **prototype Power BI dashboard structure**
- Clearly defined dashboard modules for advanced military analysis

This milestone lays the **foundation for building a complete global military comparison and analytics platform.**
