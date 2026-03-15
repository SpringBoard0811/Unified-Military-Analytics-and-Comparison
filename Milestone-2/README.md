# Milestone 2 – KPI Engineering & Dashboard Planning
Project: Unified Military Analytics and Comparison Dashboard

## Overview
Milestone 2 focuses on transforming the raw military dataset into analytical features (KPIs) and preparing the data for visualization in Tableau. This stage also includes designing the dashboard structure and prototyping the interaction flow for the final analytics platform.

## KPI Engineering
New analytical metrics were created from the raw military dataset:

- **Power Index Rank Gap** – Difference between a country's military rank and the top-ranked country.
- **Assets per Capita** – Total military assets relative to total manpower.
- **Budget-to-GDP Ratio** – Defense budget as a proportion of national GDP.

These KPIs enable comparative analysis of military strength, resource efficiency, and economic investment in defense.

## Data Enrichment
To support regional and alliance-based analysis, the dataset was enriched with metadata including:

- Continent  
- Geographic region  
- Military alliance flags (e.g., NATO membership)

## Data Preparation
The dataset was formatted for Tableau visualization in two formats:

- **Wide Format** – Each metric stored as a column for quick KPI comparison.  
- **Long Format** – Restructured for flexible dashboard visualizations and filtering.

Final dataset exported as:

`military_final.xlsx`

## Dashboard Planning
Initial dashboard layouts were designed to guide the final visualization system. The following dashboard modules were planned:

- **Quick Stats** – Global military overview and KPIs  
- **Nation Overview** – Detailed military profile for each country  
- **Compare Powers** – Multi-country comparison dashboard  
- **Coalition Builder** – Alliance and coalition strength simulation  

A prototype dashboard was created using sample data to validate interactions and navigation flow.

## Files in Milestone 2
- `Milestone_2.ipynb` – Notebook for KPI computation and dataset preparation  
- `generate_kpis.py` – Script to generate KPI features  
- `military_final.xlsx` – Final dataset prepared for Tableau  
- `dashboard_storyboard.pdf` – Layout sketches and dashboard design  

## Technologies Used
- Python  
- Pandas  
- Jupyter Notebook  
- Tableau  

## Output
A KPI-enriched military dataset and an initial dashboard prototype ready for visualization and interactive analytics.
