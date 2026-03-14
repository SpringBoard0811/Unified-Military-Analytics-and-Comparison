# 📊 Milestone 2 – KPI Engineering & Dashboard Design

## 📌 Project Overview

The **Unified Military Analytics and Comparison Dashboard** is designed to provide a data-driven platform for analyzing and comparing the military capabilities of countries worldwide.

In **Milestone 2**, the cleaned military dataset produced in Milestone 1 is transformed into **analytical Key Performance Indicators (KPIs)** and prepared for interactive dashboard visualization.

During this stage, several KPIs were created directly within **Power BI** using **DAX (Data Analysis Expressions)**. These calculated metrics allow dynamic analysis and support interactive filtering within the dashboard environment.

Additionally, the structure and layout of the future dashboard system were planned in this phase, forming the foundation for the visual dashboards that will be developed in the next milestone.

Overall, this milestone converts **raw statistical data into meaningful analytical metrics** that can support deeper military capability analysis.

---

# ⚙️ KPI Engineering Using DAX

In this stage, new analytical indicators were developed using **DAX formulas within Power BI**. These KPIs help evaluate military strength, operational efficiency, and defense investment patterns.

## Key KPIs Implemented

### 📊 Assets per Capita

This metric evaluates the relationship between **military equipment and available manpower**, providing insight into resource allocation efficiency.

**Formula**

```
Assets per Capita =
('clean_military_data'[total_aircraft] +
 'clean_military_data'[tanks] +
 'clean_military_data'[naval_assets])
/
'clean_military_data'[total_manpower]
```

---

### 💰 Budget-to-GDP Ratio

This KPI indicates how much of a country's **economic output is allocated toward defense spending**.

**Formula**

```
Budget-to-GDP Ratio =
'clean_military_data'[defense_budget] /
'clean_military_data'[gdp]
```

---

### 🌐 Power Index Rank Gap

This indicator measures the **ranking distance between a given country and the highest-ranked military power**.

**Formula**

```
Power Index Rank Gap =
RANKX(ALL('clean_military_data'), 'clean_military_data'[p_rank])
-
MIN('military_cleaned'[p_rank])
```

These KPIs help highlight:

- Military efficiency
- Strategic defense investment
- Relative military positioning among nations

---

# 🌍 Data Enrichment

To improve the analytical capabilities of the system, additional contextual attributes were incorporated into the dataset.

## Added Metadata Fields

- Continent
- Geographic Region
- Military Alliance Indicators (e.g., NATO membership)

These additional fields allow the dashboards to support:

- Regional military comparisons  
- Analysis of alliance structures  
- Global grouping and clustering of military capabilities  

---

# 📊 Dashboard Planning

During this milestone, the overall **dashboard architecture** was designed to support multiple analytical views of global military data.

The visualization system will consist of several modules, each providing a different perspective on military strength and defense resources.

## Planned Dashboard Modules

### ⚡ Quick Stats
Provides a **global overview of military rankings and key indicators**.

### 🌍 Nation Overview
Displays a **detailed military profile for an individual country**.

### ⚖️ Compare Powers
Allows **side-by-side comparison of defense metrics across countries**.

### 🤝 Coalition Builder
Simulates the **combined military capabilities of alliances or multiple nations**.

These modules together provide both **high-level insights and detailed analytical comparisons**.

---

# 🛠 Technologies Used

The following tools were used in this milestone:

- **Python** – Data preprocessing and dataset handling  
- **Pandas** – Data manipulation and transformation  
- **Jupyter Notebook** – Development and experimentation  
- **Power BI** – Dashboard creation and data visualization  
- **DAX (Data Analysis Expressions)** – KPI calculations and analytical measures  

---

# 📈 Milestone Outcome

At the end of **Milestone 2**, the following components were produced:

- ✔ A **military dataset enhanced with analytical KPIs**  
- ✔ Dynamic **DAX-based KPI calculations**  
- ✔ An initial **Power BI dashboard prototype**  
- ✔ A defined dashboard structure for further development  

This milestone establishes the **analytical layer of the project**, enabling advanced visualization and comparative analysis of global military capabilities.
