# 🎯 Milestone 1 – Data Collection & Preparation

This milestone focuses on collecting global military data and preparing it for analysis. The final output will be a clean, structured dataset ready for visualization and analytics (e.g., Tableau dashboards).

# 🛰️ Module 1: Scraping Setup and Execution
# 🎯 Objective

Collect country-level military statistics from the URLs provided in the dataset links file.

# 📂 Data Source

The URLs used for data collection are listed in the file:

links_for_military_data.txt

Each link corresponds to a country-specific webpage containing military statistics such as:

✈️ Total Aircraft

🛡️ Total Tanks

💰 Defense Budget

👥 Active Personnel

🚢 Naval Assets

# 📌 Tasks Performed

Use links_for_military_data.txt as the source list of URLs

Scrape country-level military metrics from each webpage

Extract key statistics including:

✈️ Total Aircraft

🛡️ Total Tanks

💰 Defense Budget

👥 Active Personnel

🚢 Naval Assets

Parse structured metric blocks from the webpage

Store extracted data in a structured CSV dataset

Save per-country HTML files for debugging (optional)

# 💾 Deliverables
Item	Description
Raw Dataset	military_raw_data.csv

# 📊 Evaluation Criteria

✔ ≥ 95% URL success rate from the provided list

✔ Military metrics successfully parsed for 140+ countries

✔ Data stored in a consistent structured format

# 🧹 Module 2: Data Cleaning and Structuring
# 🎯 Objective

Transform the raw scraped dataset into a clean and standardized format suitable for data analysis and visualization.

# 📌 Tasks Performed

Clean textual numeric values by removing:

commas ,

percentage symbols %

plus signs +

other special characters

Convert metric values to numeric formats

Standardize column names for consistency

Example column naming:

total_aircraft
total_tanks
active_personnel
defense_budget
naval_assets

Handle missing / null values appropriately

Ensure dataset compatibility with Tableau visualization

# 💾 Deliverables
Item	Description
Clean Dataset	military_cleaned.csv
Notebook	web_scraping_one_country.ipynb
Automation Notebook	automate_scraping_urls.ipynb

# 📊 Evaluation Criteria

✔ < 2% missing/null values after cleaning

✔ No structural or formatting errors in dataset

✔ Dataset ready for Tableau visualization and analysis

# 📈 Final Output of Milestone 1

By the end of this milestone we will have:

✔ 🌍 Global military metrics dataset

✔ 📊 Clean and structured data ready for analysis

✔ 🔁 Reproducible pipeline for scraping and preprocessing

✔ 📂 Dataset ready for use in visual analytics and dashboards

# 🚀 Outcome
Raw Military Data → Clean Analytical Dataset

This dataset will serve as the foundation for the next milestone, where the data will be used for comparative analytics, visual dashboards, and military capability insights.
