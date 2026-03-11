import pandas as pd

# Load dataset
# Example dataset columns:
# Country, Military_Power_Index, Defense_Budget_Billion, Active_Personnel,
# Aircraft, Tanks, Naval_Ships

data = pd.read_csv("military_data.csv")

# -----------------------------
# KPI CALCULATIONS
# -----------------------------

# 1 Total Countries Analyzed
total_countries = data["Country"].nunique()

# 2 Total Active Military Personnel
total_personnel = data["Active_Personnel"].sum()

# 3 Total Aircraft
total_aircraft = data["Aircraft"].sum()

# 4 Total Tanks
total_tanks = data["Tanks"].sum()

# 5 Total Naval Ships
total_naval = data["Naval_Ships"].sum()

# 6 Total Defense Budget
total_budget = data["Defense_Budget_Billion"].sum()

# 7 Strongest Military (Lowest Power Index)
strongest_country = data.loc[data["Military_Power_Index"].idxmin(), "Country"]

# 8 Top 10 Military Powers
top10 = data.sort_values(by="Military_Power_Index").head(10)

# -----------------------------
# PRINT KPIs
# -----------------------------

print("------ Military Dashboard KPIs ------")

print(f"Total Countries Analyzed: {total_countries}")
print(f"Total Active Personnel: {total_personnel:,}")
print(f"Total Aircraft: {total_aircraft:,}")
print(f"Total Tanks: {total_tanks:,}")
print(f"Total Naval Ships: {total_naval:,}")
print(f"Total Defense Budget (Billion USD): {total_budget}")
print(f"Strongest Military: {strongest_country}")

print("\nTop 10 Military Powers:")
print(top10[["Country", "Military_Power_Index"]])

# -----------------------------
# EXPORT KPI SUMMARY
# -----------------------------

kpi_summary = {
    "Total Countries": total_countries,
    "Total Personnel": total_personnel,
    "Total Aircraft": total_aircraft,
    "Total Tanks": total_tanks,
    "Total Naval Ships": total_naval,
    "Total Budget (Billion USD)": total_budget,
    "Strongest Country": strongest_country
}

kpi_df = pd.DataFrame(list(kpi_summary.items()), columns=["KPI", "Value"])
kpi_df.to_csv("military_kpis.csv", index=False)

print("\nKPI summary saved to military_kpis.csv")