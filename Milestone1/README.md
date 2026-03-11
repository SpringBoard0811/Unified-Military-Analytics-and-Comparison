# Milestone 1 – Data Collection & Data Cleaning

## Overview

The objective of this milestone is to collect global military power data and prepare a clean dataset for further analysis and dashboard development.
Raw data is collected, examined, and cleaned so that it can be used for analytical tasks in the next milestones.

## Data Source

The dataset was collected from the website:

https://www.globalfirepower.com

This website provides country-level military statistics including manpower, military equipment, defense budget, and economic indicators.

## Tasks Completed

### 1. Data Collection

Military data was collected for multiple countries using the provided source.
The following fields were gathered:

* Country
* Power Index Rank
* Total Manpower
* Active Personnel
* Reserve Personnel
* Total Aircraft
* Fighter Aircraft
* Naval Assets
* Tanks
* Defense Budget
* GDP

### 2. Raw Dataset Creation

The collected data was stored in its original form without modification.
The dataset contained:

* Numeric values with commas
* Symbols such as %
* Missing values in some fields

The raw dataset was exported as:

**military_raw_data.csv**

### 3. Data Cleaning & Standardization

The raw dataset was cleaned and prepared for analysis.

Cleaning steps included:

* Removing commas and special characters
* Converting values to numeric data types
* Handling missing values
* Standardizing column names
* Ensuring consistent data formatting

The cleaned dataset was exported as:

**military_cleaned_data.csv**

## Files Included

This milestone folder contains the following files:

* `Milestone 1 – Data Collection & Data Cleaning.ipynb`
  Jupyter Notebook containing the data collection and cleaning implementation.

* `military_raw_data.csv`
  Raw dataset collected from the source.

* `military_cleaned_data.csv`
  Cleaned dataset ready for analysis.

## Outcome

At the end of Milestone 1:

* Military data was successfully collected from the source website.
* The dataset was cleaned and standardized.
* The cleaned dataset is ready for further analysis and KPI engineering in the next milestone.

