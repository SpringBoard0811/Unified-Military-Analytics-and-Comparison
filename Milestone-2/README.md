# 🧹 Module 2: Data Cleaning & Standardization

## 🎯 Objective

Transform raw scraped data into a **clean, structured, and analysis-ready dataset** suitable for dashboards and analytics.

---

## ⚙️ Process Workflow

```
Raw Data → Cleaning → Standardization → Clean Dataset
```

---

## 📌 Data Issues Identified

| Issue Type           | Example          |
| -------------------- | ---------------- |
| Missing Values       | NULL entries     |
| Special Characters   | $, commas, +     |
| Inconsistent Formats | Mixed data types |
| Noisy Data           | Incorrect values |

---

## 🛠️ Cleaning Steps

### 1️⃣ Load Raw Dataset

* Import CSV using Pandas

### 2️⃣ Handle Missing Values

* Fill using median values
* Remove invalid rows

### 3️⃣ Clean Numeric Data

* Remove commas, $, symbols
* Convert to numeric types

### 4️⃣ Standardize Column Names

* Convert to lowercase
* Replace spaces with `_`

Example:

```
Total Aircraft → total_aircraft
```

### 5️⃣ Data Validation

* Remove duplicates
* Check logical conditions
* Ensure consistency

---

## 📂 Output Files

| File                   | Description            |
| ---------------------- | ---------------------- |
| `military_cleaned.csv` | Cleaned dataset        |
| `clean_data.ipynb`     | Data cleaning notebook |

---

## 📊 Clean Dataset Features

* ✔ No missing values
* ✔ Numeric format standardized
* ✔ Ready for visualization
* ✔ Compatible with Tableau

---

## 📈 Example Columns

| Column           |
| ---------------- |
| country          |
| power_index_rank |
| total_aircraft   |
| tanks            |
| defense_budget   |
| naval_assets     |

---

## ✅ Evaluation Criteria

* ✔ < 2% missing values
* ✔ Fully numeric dataset
* ✔ Structured and consistent

---

## 🚀 Outcome

✔ Clean analytical dataset
✔ Improved data quality
✔ Ready for KPI engineering & dashboards

---

## 👩‍💻 Author

**Shanmukhi Sudha**
Milestone 2 files
