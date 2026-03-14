# 📊 Milestone 2 – KPI Engineering & Dashboard Design

---

# 📌 Project Overview

The **Unified Military Analytics and Comparison Dashboard** is designed to provide a data-driven environment for analyzing and comparing military capabilities of countries around the world.

In **Milestone 2**, the cleaned dataset produced in Milestone 1 is enhanced with **analytical Key Performance Indicators (KPIs)** and structured for interactive dashboard development.

During this stage:

- Key analytical metrics were created using **Power BI and DAX (Data Analysis Expressions)**  
- Additional metadata fields were incorporated to enable **regional and alliance-level analysis**  
- The **initial dashboard architecture** was planned and prototyped  

This milestone transforms raw military statistics into **actionable analytical insights** suitable for visualization and strategic comparison.

---

# 🧮 Module 3 – KPI Feature Engineering

## 🎯 Objective

Generate meaningful **analytical indicators** that allow deeper comparison of military capabilities, resource efficiency, and defense investment.

---

## 📌 Tasks Performed

- Compute the following KPIs:

### 🌐 Power Index Rank Gap
Measures the ranking difference between a country and the **top-ranked military power**.

### 📊 Assets per Capita
Represents the ratio of military equipment to available manpower.

### 💰 Budget-to-GDP Ratio
Shows the proportion of a country’s **economic output spent on defense**.

---

# 🧮 KPI Calculations

---

## 1️⃣ Assets per Capita

This metric aggregates major military assets and relates them to the available military manpower.

It helps measure **how efficiently a country’s equipment resources are distributed relative to its personnel strength**.

To avoid division-by-zero errors, the calculation uses **`np.where()`**.

### Implementation

```
Combine major military assets
df["total_assets"] = (
    df["total_military_aircraft"] +
    df["tanks"] +
    df["total_naval_fleet"]
)

Calculate assets per capita while preventing division by zero
df["assets_per_capita"] = np.where(
    df["total_military_manpower"] > 0,
    df["total_assets"] / df["total_military_manpower"],
    0
)
```

---

## 2️⃣ Budget-to-GDP Ratio

This KPI evaluates **defense spending relative to the country's economic strength**.

A higher ratio indicates that a **larger portion of national economic resources is allocated to defense**.

### Implementation

```
df["budget_to_gdp_ratio"] = np.where(
    df["purchasing_power_parity_usd"] > 0,
    df["defense_budget_usd"] / df["purchasing_power_parity_usd"],
    0
)
```

---

## 3️⃣ Power Index Rank Gap

This metric shows how far a country’s military ranking is from the **top-ranked military power**.

The strongest country will have a **rank gap of 0**, while other countries will have increasing values depending on their rank position.

### Implementation

```python
top_rank = df["power_index_rank"].min()

df["power_index_rank_gap"] = df["power_index_rank"] - top_rank
```

---

### 📊 Purpose of These KPIs

These indicators enable deeper military analytics by helping to analyze:

- Military **resource efficiency**
- National **defense investment intensity**
- Relative **military ranking differences**

They serve as the foundation for **interactive dashboards and comparative analysis** in later stages of the project.

## 🌍 Data Enrichment

To support advanced analysis, the dataset was extended with additional contextual attributes.

### Added Metadata Fields

- Continent
- Geographic Region
- Military Alliance Indicators (e.g., NATO membership)

These attributes allow the dashboard to support:

- Regional military comparisons
- Alliance-based analysis
- Global grouping of defense capabilities

---

## 📊 Data Formatting

The dataset was prepared in both:

- **Wide format** for standard dashboard visuals  
- **Long format** for flexible Tableau analysis  

This ensures compatibility with **Tableau and other visualization tools**.

---

## 💾 Deliverables

| Item | Description |
|-----|-------------|
| Dataset | `military_final.xlsx` |
| KPI Generation Script | `generate_kpis.py` |

---

## 📊 Evaluation Criteria

- ✔ All KPI metrics are correctly calculated  
- ✔ Dataset structure is consistent and clean  
- ✔ Data loads into **Tableau without additional transformation**

---

# 🧭 Module 4 – Dashboard Planning & Prototyping

## 🎯 Objective

Design the **initial dashboard structure** and create a prototype visualization environment that will be expanded in Milestone 3.

---

## 📌 Tasks Performed

- Create layout sketches or wireframes for the following dashboards:

### ⚡ Quick Stats
Global overview of major military indicators and rankings.

### 🌍 Nation Overview
Detailed military profile of an individual country.

### ⚖️ Compare Powers
Side-by-side comparison of defense metrics across nations.

### 🤝 Coalition Builder
Simulation of combined military capabilities of multiple countries.

---

### Dashboard Interaction Planning

Define the logic for:

- Filters
- Navigation buttons
- Cross-dashboard interactions
- Parameter-based comparisons

---

## 💾 Deliverables

| Item | Description |
|-----|-------------|
| Dashboard Storyboard | Layout sketches and wireframes |
| Prototype Dashboard | Initial working dashboard application |

---

## 📊 Evaluation Criteria

- ✔ Dashboard interactions and KPIs are mapped correctly  
- ✔ Navigation and filtering logic are defined  
- ✔ At least **one dashboard module (Quick Stats or Nation Overview)** is functional  

---

# 🛠 Technologies Used

The following technologies were utilized in this milestone:

- **Python** – Data preprocessing and automation  
- **Pandas** – Dataset manipulation and transformation  
- **Jupyter Notebook** – Development and experimentation  
- **Power BI** – Dashboard visualization  
- **DAX (Data Analysis Expressions)** – KPI calculations  

---

# 📈 Milestone Outcome

At the completion of Milestone 2, the project produces:

- ✔ A **KPI-enriched military dataset**
- ✔ Dynamic **DAX-based analytical metrics**
- ✔ A structured dataset ready for **Tableau dashboards**
- ✔ A prototype dashboard and defined visualization architecture

This milestone establishes the **analytical layer of the platform**, enabling advanced comparative analysis of global military capabilities.
