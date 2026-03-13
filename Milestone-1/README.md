# 🌍 Milestone 1 – Data Collection & Preparation
## Unified Military Analytics and Comparison Dashboard

---

## 📌 Project Overview

The **Unified Military Analytics and Comparison Dashboard** aims to develop an analytical platform for exploring and comparing global military capabilities across countries.

The platform integrates structured military datasets and interactive dashboards to provide insights into **defense strength, resource distribution, and global military rankings**.

**Milestone 1** focuses on the **data acquisition and preparation stage**, where military statistics are collected from publicly available sources, processed, and converted into structured datasets ready for analysis and visualization.

This milestone is divided into two core modules:

- **Module 1 – Scraping Setup and Execution**
- **Module 2 – Data Cleaning and Structuring**
- **Pipeline:**
**Web Scraping → Raw Dataset → Feature Selection → Data Cleaning → Final Dataset**

Together, these modules establish the **data foundation required for analytics and dashboard development in later milestones.**

---

# ⚙️ Module 1 – Scraping Setup and Execution

This module implements the **automated web scraping pipeline** used to collect global military statistics.

The scraping process uses the file **`https://www.globalfirepower.com/`** as the centralized source of all required URLs. These URLs correspond to different military metrics such as aircraft strength, tank inventory, naval assets, defense budgets, and manpower statistics.

The scraping system retrieves country-level military data, parses the relevant metric blocks from each webpage, and stores the extracted information in structured format.

For debugging and traceability purposes, the raw HTML pages may also be saved locally.

### Key Tasks Implemented

- Automated scraping of military statistics webpages
- Retrieval of URLs from **`https://www.globalfirepower.com/`**
- Extraction of **country-level military metrics**
- Parsing HTML content using **BeautifulSoup**
- Saving raw HTML pages for debugging (optional)
- Structuring extracted data into CSV format

### Deliverables

- **Raw Dataset:** `Military_Raw_Data.csv`

### Evaluation Criteria

- At least **95% successful URL retrieval** from the provided URL list
- Correct parsing of **military metric blocks**
- Successful extraction of statistics for **140+ countries**

This module produces the **raw dataset that serves as the input for the data preprocessing stage.**

---

# 🧹 Module 2 – Data Cleaning and Structuring

The second module focuses on transforming the raw dataset into a **clean, structured, and analysis-ready format**.

Since web-scraped data often contains formatting inconsistencies such as commas, percentage signs, plus symbols, or textual annotations, a systematic data cleaning process is implemented.

The dataset is processed to remove unwanted characters, convert textual values into numeric format, and standardize column names to maintain consistency across the dataset.

Missing values are also handled to ensure the dataset remains reliable for analytical and visualization purposes.

### Key Tasks Implemented

- Removing formatting symbols (`,`, `%`, `+`, etc.)
- Converting metrics into **numeric values**
- Standardizing column naming conventions
- Handling missing or null values
- Preparing a structured dataset for analytics tools

### Deliverables

- **Clean Dataset:** `Final_Military_Data.csv`

### Evaluation Criteria

- **Less than 2% missing or null values** after cleaning
- Consistent numeric formatting across dataset columns
- No structural or schema errors in the final dataset

This module ensures that the dataset becomes **fully prepared for analytics, feature engineering, and dashboard visualization.**

---

# 📊 Key Military Metrics Collected

The dataset contains multiple military capability indicators, including:

- ✈ **Total Aircraft**
- 🪖 **Active Military Personnel**
- 🪖 **Reserve Personnel**
- 🚢 **Naval Assets**
- 🛡 **Defense Budget**
- 🚜 **Tank Strength**
- 🌐 **Global Military Power Ranking**

These metrics enable **comparative analysis of national defense capabilities across countries.**

---

# 📁 Files Included in Milestone 1

| File | Description |
|-----|-------------|
| `Milestone_1.ipynb` | Python script used to scrape military statistics from provided URLs |
| `Military_raw_Data.csv` | Raw dataset generated after web scraping |
| `Final_Military_Data.csv` | Final cleaned dataset ready for analysis |

---

# 🛠 Technologies Used

The following tools and technologies were used to implement this milestone:

- **Python** – Core programming language
- **Requests** – For HTTP requests and webpage retrieval
- **BeautifulSoup** – For parsing HTML content
- **Pandas** – For data cleaning and dataset structuring
- **Jupyter Notebook** – For development and documentation

---

# 📈 Milestone Outcome

At the end of **Milestone 1**, two datasets are generated:

1. **Raw Dataset** – `Military_raw_data.csv`
2. **Final Dataset** – `Final_Military_Data.csv`

The cleaned dataset serves as the **primary input for further analytics and dashboard development.**

---

# 🚀 Next Steps (Milestone 2)

The next milestone will focus on **analytical enhancement and dashboard development**, including:

- Feature engineering and derived military indicators
- Creation of analytical KPIs
- Comparative analysis across countries
- Development of interactive **Power BI dashboards**

---

📌 *Milestone 1 establishes the foundational data layer required for building an intelligent military analytics dashboard capable of providing meaningful global defense insights.*
