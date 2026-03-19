# 🎯 Milestone 02 — KPI Engineering & Feature Development

Milestone 02 focuses on transforming the cleaned military dataset into an **analytical dataset enriched with derived indicators and Key Performance Indicators (KPIs)**.

While the dataset collected in Milestone 01 contains raw military statistics, this stage introduces **analytical metrics that help interpret military strength, efficiency, and strategic capacity across countries**.

These KPIs make the dataset suitable for **comparative analysis and dashboard visualization**.

---

# 📂 Input Dataset

The dataset used in this milestone is the cleaned output from **Milestone 01**.

| Dataset                | Description                                                                 |
| ---------------------- | --------------------------------------------------------------------------- |
| `military_cleaned.csv` | Cleaned dataset containing standardized military metrics for 140+ countries |

This dataset includes indicators such as:

* Military manpower
* Aircraft inventory
* Naval assets
* Defense budgets
* Economic indicators
* Resource production statistics

---

# 📊 Objective

The primary objectives of this milestone are:

✔ Create analytical **Key Performance Indicators (KPIs)**
✔ Transform raw military metrics into **interpretable indicators**
✔ Enable **country comparison and strategic analysis**
✔ Prepare the dataset for **interactive dashboards**

---

# 🧠 KPI Engineering

Derived KPIs provide deeper insights than raw metrics by relating multiple variables together.

The project introduces analytical indicators such as:

---

## ⚔️ Power Index Rank Gap

Measures how far a country is from the **top global military rank**.

Formula:

```
power_index_rank_gap = power_index_rank - 1
```

Purpose:

* Highlights the distance from the strongest military power.
* Helps visualize global ranking differences in dashboards.

---

## 🪖 Assets per Capita

Measures military equipment relative to population size.

Example concept:

```
assets_per_capita = total_assets / total_population
```

Purpose:

* Indicates **military equipment density**
* Allows fair comparison between large and small countries

---

## 💰 Defense Budget Strength

Analyzes the financial capacity supporting military forces.

Example indicator:

```
defense_budget_per_person = defense_budget / total_population
```

Purpose:

* Shows **defense spending intensity**
* Helps identify economically strong military systems

---

# ⚙️ Data Processing Steps

The KPI generation pipeline performs the following steps:

✔ Load the cleaned dataset
✔ Select relevant analytical columns
✔ Generate derived KPIs
✔ Ensure numeric formatting for analysis
✔ Store the enriched dataset for visualization

---

# 💾 Outputs

| Component          | Description                |
| ------------------ | -------------------------- |
| KPI Notebook       | `generate_kpis.ipynb`      |
| Analytical Dataset | `military_kpi_dataset.csv` |

The output dataset contains both **original metrics and derived analytical indicators**.

---

# 📊 Analytical Capabilities Enabled

After KPI engineering, the dataset supports:

✔ Country-level military capability comparison
✔ Strategic ranking analysis
✔ Resource and equipment efficiency analysis
✔ Defense spending analysis

These insights will be explored through interactive dashboards in the next milestone.

---

# 📈 Data Transformation Pipeline

```
Raw Military Data
        ↓
Clean Dataset (Milestone 01)
        ↓
KPI Engineering
        ↓
Analytical Dataset
```

---

# 🚀 Outcome of Milestone 02

At the end of this milestone, the project produces:

✔ A **feature-enriched military dataset**
✔ Derived KPIs for deeper military analysis
✔ Structured data ready for **dashboard development**

This analytical dataset will be used in the next stage to build **interactive dashboards for exploring global military power**.

