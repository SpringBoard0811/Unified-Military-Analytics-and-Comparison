# Milestone 3 – Full Dashboard Development
Project: Unified Military Analytics and Comparison Dashboard

## Overview
Milestone 3 focuses on the complete development of the interactive PowerBi dashboards for the Global Military Analytics platform. Using the KPI-enriched dataset generated in Milestone 2, this stage implements four fully functional dashboards that allow users to explore, compare, and analyze global military capabilities.

The dashboards provide both high-level summaries and detailed country-level insights, enabling users to understand military power distribution, resource allocation, and potential coalition strengths across nations.

---

# Dashboard Modules

## 1. Quick Stats Dashboard

The **Quick Stats** dashboard provides a global overview of military strength indicators across countries.

### Features
- Displays **Top 10 countries by Power Index**
- Dynamic **KPI cards** showing key indicators
- Interactive filters allowing users to explore military power distribution by:
  - Region
  - Continent
  - Alliance membership (e.g., NATO)

### Visual Components
- Top 10 Power Index ranking chart
- KPI indicator cards
- Global comparison charts

### Purpose
This dashboard allows users to quickly identify the strongest military powers and analyze patterns across regions and alliances.

---

## 2. Nation Overview Dashboard

The **Nation Overview** dashboard provides a detailed profile of an individual country's military capabilities.

### Features
- Country selector for viewing detailed national military statistics
- Visualization of key metrics including:
  - Military manpower
  - Aircraft strength
  - Tank strength
  - Naval assets
  - Defense budget
  - Engineered KPIs

### Visual Components
- Bar charts for category comparison
- Radar charts to visualize overall military capability
- Tooltips displaying:
  - Global rank
  - Comparative values with other countries

### Purpose
This dashboard enables in-depth analysis of each country’s military resources and strengths relative to other nations.

---

## 3. Compare Powers Dashboard

The **Compare Powers** dashboard allows users to compare military capabilities between two countries.

### Features
- Side-by-side comparison of two selected countries
- Metrics compared include:
  - Manpower
  - Aircraft
  - Tanks
  - Naval assets
  - Defense budget
  - Key performance indicators (KPIs)

### Interaction
Country selection is implemented using **PowerBi parameters**, allowing users to dynamically change comparison targets.

### Purpose
This dashboard provides an analytical comparison of military strengths between nations, helping identify strategic advantages and resource differences.

---

## 4. Coalition Builder Dashboard

The **Coalition Builder** dashboard simulates the combined military strength of multiple countries.

### Features
- Multi-country selection using filters
- Aggregation of selected countries’ military metrics
- Comparison of coalition strength against:
  - Another coalition
  - A reference country

### Metrics Aggregated
- Total manpower
- Total aircraft
- Total tanks
- Naval assets
- Defense budget
- Combined KPIs

### Purpose
This dashboard enables analysis of potential alliances and the combined military strength of coalitions.

---

# Dashboard Integration

All dashboards are integrated into a single interactive PowerBi application.

### Navigation Features
- Navigation buttons between dashboards
- Shared filters across multiple dashboards
- Interactive parameter controls

### Navigation Flow
Quick Stats → Nation Overview → Compare Powers → Coalition Builder

This allows seamless movement between global analysis and detailed comparisons.

---

# Deliverables

The following outputs were generated as part of Milestone 3:

- **Sample dashboard application**
- Fully implemented dashboards:
  - Quick Stats
  - Nation Overview
  - Compare Powers
  - Coalition Builder

Final PowerBi workbook:

`global_military_firepower_2025.twbx`

This workbook contains all dashboards, datasets, filters, and interactions.

---

# Technologies Used

- PowerBi
- Python (for KPI dataset preparation)
- Pandas
- Excel dataset integration

---

# Evaluation Criteria

Milestone 3 satisfies the following evaluation requirements:

- Country and region filters function correctly
- Nation Overview dashboard visualizes all major military metrics
- Compare Powers dashboard supports dynamic country comparison
- Coalition Builder successfully aggregates multi-country metrics
- Smooth navigation between dashboards
- All dashboards integrated within a single PowerBi workbook

---

# Outcome

This milestone delivers a fully interactive military analytics dashboard system that enables users to:

- Explore global military power rankings
- Analyze individual country capabilities
- Compare military strengths between nations
- Simulate coalition military power

These dashboards form the core visualization component of the **Unified Military Analytics and Comparison Dashboard** platform.
