# 🌍 Global Military Power Dashboard
### Milestone 2 – Power BI Overview Dashboard

---

## 📌 Project Overview

This dashboard is the **second milestone** of the Global Military Power Analysis project. It delivers an interactive Power BI report providing a high-level overview of military capabilities across **145 countries**, enabling users to explore and compare military resources through rich visual analytics.

---

## 🎯 Objective

Build an interactive Power BI dashboard that enables stakeholders to:

- Quickly assess global military statistics at a glance
- Identify and compare the world's top military powers
- Analyze defense budget distribution across major nations
- Explore military asset composition (aircraft, tanks, naval fleet)
- Filter and drill down by individual country

---

## 📂 Data Source

| Field | Details |
|---|---|
| File | `military_cleaned.csv` |
| Source | Milestone 1 – Cleaned Dataset |
| Countries Covered | 145 |
| Key Metrics | Total Aircraft, Total Tanks, Naval Fleet, Active Personnel, Defense Budget |

---

## 📊 Dashboard Visualizations

### 🔢 Quick Stats Panel
KPI summary cards displayed on the left panel:

| Metric | Value |
|---|---|
| Total Countries Analyzed | 145 |
| Top Military Country | United States |
| Global Defense Budget | ~3 Trillion USD |
| Global Military Manpower | ~24 Million |

---

### 🏆 Power Index Rank by Country
Horizontal bar chart ranking countries by Power Index score *(lower = stronger)*:

| Country | Power Index |
|---|---|
| United States | 0.07 |
| Russia | 0.08 |
| China | 0.09 |
| India | 0.13 |
| South Korea | 0.16 |
| France | 0.18 |

---

### 💰 Defense Budget Comparison
Column chart comparing defense budgets of major powers (in USD Trillions):

| Country | Budget |
|---|---|
| United States | 0.83T |
| China | 0.30T |
| Russia | 0.21T |
| India | 0.11T |
| France | 0.07T |
| South Korea | 0.04T |

---

### 🛡️ Military Assets Comparison
Stacked bar chart comparing hardware across top countries:

- **Sum of Total Military Aircraft**
- **Sum of Tanks**
- **Sum of Submarines**

Countries: United States, Russia, China, India, South Korea, France

---

### 🍩 Asset Distribution – Donut Charts

**Naval Fleet Distribution**

| Country | Share |
|---|---|
| China | 30% |
| Russia | 27% |
| United States | 17% |
| India | 12% |
| South Korea | 8% |
| France | 6% |

**Aircraft Carriers Distribution**

| Country | Share |
|---|---|
| United States | 61% |
| China | 17% |
| India | 11% |
| Russia | 6% |
| France | 6% |

---

## 🎛️ Interactive Features

- **Country Filter Dropdown** – Select any of the 145 countries to filter all visuals
- **Dynamic Visual Updates** – All charts update in real time based on filter selection
- **Cross-Filtering** – Clicking any chart element filters all other visuals on the page

---

## 🛠️ Tools & Technologies

| Tool / Technology | Usage |
|---|---|
| Power BI Desktop | Dashboard development |
| CSV (`military_cleaned.csv`) | Data source |
| Bar / Column / Donut Charts | Visualizations |
| Power BI Slicers | Interactive filtering |
| Data Modeling | Calculated measures & relationships |

---

## 📁 File Structure

```
Milestone-2/
├── military_dashboard_overview.pbix   # Power BI dashboard file
├── military_cleaned.csv               # Dataset (from Milestone 1)
├── images/
│   └── dashboard_overview.png         # Dashboard screenshot
└── README.md                          # This file
```

---

## 💡 Key Insights

1. The **United States** holds the largest defense budget globally at **~0.83 Trillion USD**, nearly 3× that of China.
2. **China leads in Naval Fleet** size with a 30% global share, reflecting rapid naval expansion.
3. The **United States dominates aircraft carrier ownership** with 61% of the global total.
4. Military assets are **heavily concentrated among 5–6 nations**, accounting for the vast majority of global hardware.
5. **India consistently ranks in the top 4** across all key military metrics.
6. **Russia** maintains large armored forces and a significant submarine fleet despite a comparatively lower defense budget.

---

## 🚀 How to Use

1. Open **Power BI Desktop** and load `military_dashboard_overview.pbix`
2. Ensure `military_cleaned.csv` is in the expected data source path (update connection if prompted)
3. Click **Home > Refresh** to reload the data if required
4. Use the **Country Filter dropdown** to explore data for specific countries
5. Click any visual element to trigger **cross-filtering** across all charts

---

## 📈 Roadmap – Upcoming Dashboards

| # | Dashboard | Status |
|---|---|---|
| 1 | Nation Military Overview | ✅ Current (Milestone 2) |
| 2 | Military Power Comparison | 🔜 Upcoming |
| 3 | Military Coalition Analysis | 🔜 Upcoming |
| 4 | Strategic Military Insights | 🔜 Upcoming |

---

## ✅ Evaluation Criteria

- [x] Dashboard built using Power BI Desktop
- [x] Clear visualization of all key military metrics
- [x] Functional interactive filtering and cross-filtering
- [x] Clean and intuitive dashboard design
- [x] Dataset correctly sourced from Milestone 1 output

---

*Global Military Power Analysis Project – Milestone 2*
