# Milestone 1 – Data Collection and Preparation
Project: Unified Military Analytics and Comparison Dashboard

## Overview
This milestone focuses on collecting and preparing global military statistics data. 
The data is scraped from publicly available military statistics pages and converted into a structured dataset for further analysis and dashboard development.

## Tasks Implemented
- Automated scraping of military statistics pages
- Extraction of country-level military metrics
- Parsing HTML content using BeautifulSoup
- Cleaning numeric values and units
- Storing data in structured CSV format

## Dataset
Raw dataset generated:

Military_raw_Data.csv

The dataset includes metrics such as:
- Total Aircraft
- Tanks
- Naval Assets
- Defense Budget
- Military Manpower
- Global Power Rank

Data has been collected for **140+ countries**.

## Files in Milestone 1
- `Milestone_1.ipynb` → Notebook containing scraping and parsing pipeline
- `Military_raw_Data.csv` → Final raw dataset

## Technologies Used
- Python
- BeautifulSoup
- Requests
- Pandas
- Jupyter Notebook

## Output
A structured dataset of global military statistics that will be used in the next milestone for:
- Data cleaning
- Feature engineering
- Dashboard visualization

