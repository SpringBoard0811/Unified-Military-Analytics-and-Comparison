# 📊 Milestone 2 – KPI Engineering and Dashboard Planning

## 📌 Project
**Unified Military Analytics and Comparison Dashboard**

Milestone 2 focuses on transforming the cleaned military dataset into an **analytics-ready dataset** by creating **Key Performance Indicators (KPIs)** and preparing the data for dashboard visualization tools such as **Tableau, Power BI, or Python dashboards**.

This stage also includes **dashboard planning and prototype design** for the final analytics platform.

---

# 🎯 Objectives

- Engineer analytical **KPI features**
- Enrich dataset with **metadata**
- Prepare dataset for **data visualization**
- Design **dashboard layouts and interactions**
- Build an **initial dashboard prototype**

---

# 🧠 KPI Feature Engineering

Additional analytical metrics were created to enhance military comparison and strategic analysis.

## 📊 KPI Table

| KPI Name | Formula | Description |
|--------|--------|-------------|
| **Power Index Rank Gap** | Rank Difference | Measures the ranking gap between countries |
| **Assets per Capita** | Total Assets / Population | Indicates military resources available per citizen |
| **Budget-to-GDP Ratio** | Defense Budget / GDP | Shows the percentage of economic output spent on defense |

These KPIs provide deeper insights into **military capability, resource efficiency, and defense spending priorities**.

---

# 🌍 Metadata Enrichment

Additional metadata attributes were added to support regional and strategic analysis.

| Field | Description |
|------|-------------|
| Region | Geographic grouping of countries |
| Continent | Continental classification |
| Alliance Flags | Military alliances such as NATO |

This enrichment allows filtering and grouping of countries for **comparative analytics**.

---

# 🗂 Dataset Schema

The final dataset contains structured military indicators and engineered features.

| Column Name | Description |
|-------------|-------------|
| Country | Name of the country |
| Power Index | Global military power score |
| Rank | Global ranking based on military strength |
| Defense Budget | Military expenditure |
| Total Aircraft | Number of aircraft |
| Tanks | Number of battle tanks |
| Naval Fleet | Total naval assets |
| Active Personnel | Military personnel count |
| Population | Total population |
| GDP | Economic output of the country |
| Assets per Capita | Engineered KPI |
| Budget-to-GDP Ratio | Engineered KPI |

Dataset format: **Excel / CSV**

---

# 📑 Data Preparation

To ensure compatibility with visualization tools, the dataset was formatted in two structures:

**Wide Format**
- Used for structured dashboard metrics.

**Long Format**
- Used for flexible visualization and filtering in analytics tools.

This preparation ensures seamless integration with **Tableau and Power BI dashboards**.

---

# 🏗 Project Architecture

The overall data processing workflow for Milestone 2 is illustrated below:

```
Raw Military Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
(KPI Generation)
        │
        ▼
Metadata Enrichment
        │
        ▼
Structured Dataset
        │
        ▼
Dashboard Planning
        │
        ▼
Prototype Dashboard
```

---

# 🖼 Dashboard Wireframe Planning

Dashboard wireframes were designed to define layout, navigation, and interactions.

### Dashboard Modules

**1️⃣ Quick Stats**
- Global military rankings
- Top countries by assets and budget

**2️⃣ Nation Overview**
- Detailed military statistics for a selected country

**3️⃣ Compare Powers**
- Side-by-side comparison between countries

**4️⃣ Coalition Builder**
- Simulation of combined military strength for alliances

These wireframes guide the development of the final interactive dashboard.

---

# 📦 Milestone Deliverables

- KPI engineered dataset  
- Metadata enriched dataset  
- Python script for KPI generation  
- Dashboard wireframes and layout plan  
- Prototype dashboard  

---

# 🎯 Final Outcomes

At the completion of Milestone 2, the following outcomes were achieved:

- Development of **analytical KPIs for military comparison**
- Creation of a **structured and enriched dataset**
- Preparation of data for **visual analytics platforms**
- Design of **dashboard architecture and user interactions**
- Development of an **initial dashboard prototype**

These outcomes establish a **strong analytical foundation for the final Military Analytics Dashboard**.
