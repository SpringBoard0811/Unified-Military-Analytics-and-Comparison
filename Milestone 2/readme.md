# Milestone 2 – KPI Engineering & Dashboard Preparation

## 📌 Overview

This milestone focuses on transforming the cleaned military dataset into an **analytics-ready dataset** by creating meaningful **Key Performance Indicators (KPIs)** and preparing the data structure for **interactive Power BI dashboards**.

The goal is to convert raw military statistics into **insightful metrics and visualization-ready data** that can support global military power analysis.

---

# 📊 KPI Feature Engineering

## Objective

Create derived metrics that provide deeper analytical insights into global military strength, resource distribution, and economic capacity.

## Tasks

### 1️⃣ Compute Key Indicators

The following KPIs were engineered from the cleaned dataset:

* 🥇 **Power Index Rank Gap**
  Difference between a country's current military rank and the top-ranked nation.

* 👥 **Assets per Capita**
  Measures military resources relative to population.

  Formula:

  ```
  Assets per Capita = Total Military Assets / Population
  ```

* 💰 **Budget-to-GDP Ratio**
  Indicates how much of a country's economy is allocated to military spending.

  Formula:

  ```
  Budget-to-GDP Ratio = Military Budget / GDP
  ```

---

### 2️⃣ Metadata Enrichment

To enable regional and geopolitical analysis, additional attributes were added:

* 🌍 **Region**
  Geopolitical region classification.

* 🌎 **Continent**
  Continental grouping for global comparisons.

* 🤝 **Alliance Indicators**
  Binary or categorical indicators identifying membership in alliances such as:

  * NATO
  * Other regional alliances (if applicable)

---

### 3️⃣ Data Preparation for Visualization

The dataset was structured to ensure compatibility with **Power BI dashboards**, including:

* Clean column naming conventions
* Standardized numeric formats
* Removal of redundant fields
* Creation of aggregated metrics for visualization

---

# 📦 Deliverables

| Item    | Description                              |
| ------- | ---------------------------------------- |
| Dataset | `military_raw_collected (1).csv`         |
| Script  | KPI Engineering & Feature Creation.ipynb |

---

# 📊 Dashboard Planning

## Objective

Design the structure and interaction flow for the Power BI dashboard system to support interactive exploration of military power metrics.

---

## Dashboard Views

### ⚡ Quick Stats

Provides a **global military overview** including:

* Top military powers
* Total global military budget
* Global asset distribution
* Key KPI highlights

---

### 🌍 Nation Overview

A **detailed country-level analysis** showing:

* Military rank
* Budget
* Assets
* Population-adjusted metrics
* Regional comparison

---

### ⚔️ Compare Powers

Allows **side-by-side comparison** of multiple countries based on:

* Military budget
* Personnel
* Assets
* Power index
* KPIs

---

### 🤝 Coalition Builder

Simulates **combined military strength** of selected countries.

Features include:

* Total combined budget
* Combined personnel
* Aggregated military assets
* Strategic alliance analysis

---

## Dashboard Interactions

The dashboard supports the following interactions:

* Country filters
* Region and continent filters
* Drill-down from global to country level
* Dynamic KPI recalculation
* Multi-country selection for comparison

---

# 📦 Dashboard Deliverables

| Item                 | Description                              |
| -------------------- | ---------------------------------------- |
| Dashboard Storyboard | Layout sketches and interaction planning |
| Prototype Dashboard  | Initial working Power BI dashboard       |

---

# 📊 Evaluation Criteria

The milestone is considered successful when:

* ✔ KPIs are correctly calculated
* ✔ Dataset includes complete metadata enrichment
* ✔ Dashboard interactions are clearly defined
* ✔ KPIs are properly integrated into visualizations

---

# 🚀 Outcome

```
Clean Dataset
      ↓
Engineered KPIs
      ↓
Dashboard Prototype
```

This milestone prepares the project for **full-scale dashboard development and advanced interactive analytics** in the next stage.

---
