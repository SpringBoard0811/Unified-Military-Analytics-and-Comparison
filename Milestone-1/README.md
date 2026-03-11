# 🎯 Milestone 1 – Data Acquisition & Preparation

This milestone focuses on **gathering global military data and preparing it for further analysis**.

The primary outcome of this stage is a **well-structured and clean dataset** that can later be used for analytics and dashboard creation.

---

# 🛰 Module 1: Data Scraping

## 🎯 Objective

Collect **country-specific military statistics** using the list of URLs provided in the dataset links file.

---

## 📂 Data Source

All the required URLs are listed in:

```
links_for_military_data.txt
```

Each link points to a webpage containing **military statistics for a specific country**, including information such as defense budget, equipment counts, and manpower.

---

## 📌 Activities Performed

- ✔ Use `links_for_military_data.txt` to obtain all country URLs  
- ✔ Extract military statistics from each webpage  
- ✔ Retrieve important indicators such as:

  - ✈️ Aircraft inventory  
  - 🛡 Tank strength  
  - 💰 Defense budget  
  - 👥 Active military personnel  
  - 🚢 Naval fleet size  

- ✔ Parse the webpage structure to capture relevant metrics  
- ✔ Save extracted information in a **structured CSV dataset**  
- ✔ Optionally store **HTML pages for debugging and verification**

---

## 💾 Outputs

| Component | Description |
|-----------|-------------|
| **Scraping Script** | `scrape_military_metrics.py` |
| **Raw Dataset** | `military_raw_data.csv` |

---

## 📊 Validation Criteria

- ✔ At least **95% successful data extraction** from the provided URLs  
- ✔ Military metrics captured for **more than 140 countries**  
- ✔ Dataset stored in a **consistent and organized structure**

---

# 🧹 Module 2: Data Cleaning & Formatting

## 🎯 Objective

Convert the **raw scraped dataset** into a **clean and analysis-ready dataset**.

This step ensures the data is consistent and suitable for analytics tools and dashboards.

---

## 📌 Activities Performed

- ✔ Remove unwanted characters from numeric values such as:

  - commas `,`  
  - percentage signs `%`  
  - plus symbols `+`  
  - other formatting characters  

- ✔ Convert values into proper **numeric data types**
- ✔ Standardize dataset column names

### Example Column Names

```
total_aircraft
total_tanks
active_personnel
defense_budget
naval_assets
```

- ✔ Manage **missing or incomplete values**
- ✔ Ensure compatibility with **visualization platforms such as Tableau**

---

## 💾 Outputs

| Component | Description |
|-----------|-------------|
| **Processed Dataset** | `military_cleaned.csv` |
| **Data Processing Notebook** | `clean_data.ipynb` |

---

## 📊 Quality Checks

- ✔ **Less than 2% missing values** after processing  
- ✔ No inconsistencies in dataset formatting  
- ✔ Dataset ready for **analysis and visualization**

---

# 📈 Final Result of Milestone 1

At the end of this milestone, the project produces:

- ✔ 🌍 A global dataset containing military metrics  
- ✔ 📊 Clean and standardized data ready for analytics  
- ✔ 🔁 A reproducible workflow for scraping and preprocessing  
- ✔ 📂 A dataset prepared for use in dashboards and comparative analysis

---

# 🚀 Outcome

```
Raw Military Data → Structured Analytical Dataset
```

This dataset will act as the **base for the next milestone**, where advanced analytics and dashboards will be developed to explore global military capabilities.
