import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import os

# -----------------------------
# INDIA URL
# -----------------------------
url = "https://www.globalfirepower.com/country-military-strength-detail.php?country_id=india"

# -----------------------------
# HEADERS (Prevents 403 error)
# -----------------------------
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# -----------------------------
# FETCH PAGE
# -----------------------------
response = requests.get(url, headers=headers, timeout=15)
response.raise_for_status()

# Use html.parser (safer if lxml not installed)
soup = BeautifulSoup(response.text, "html.parser")

data = {}

# -----------------------------
# COUNTRY NAME
# -----------------------------
title = soup.find("h1")
if title:
    data["country"] = title.get_text(strip=True)
else:
    data["country"] = "India"

# -----------------------------
# POWER INDEX EXTRACTION
# -----------------------------
overview_text = soup.find("span", class_="textNormal")

if overview_text:
    text = overview_text.get_text(" ", strip=True)

    rank_match = re.search(r"ranked\s+(\d+)", text)
    score_match = re.search(r"score of\s+([\d.]+)", text)

    data["power_index_rank"] = rank_match.group(1) if rank_match else None
    data["power_index_score"] = score_match.group(1) if score_match else None
else:
    data["power_index_rank"] = None
    data["power_index_score"] = None

# -----------------------------
# METRIC EXTRACTION
# -----------------------------
metric_blocks = soup.find_all("div", class_="specsGenContainers")

for block in metric_blocks:
    label = block.find("span", class_="textLarge")
    value = block.find("span", class_="textWhite")

    if label and value:
        key = (
            label.get_text(strip=True)
            .replace(":", "")
            .lower()
            .replace(" ", "_")
        )
        data[key] = value.get_text(strip=True)

# -----------------------------
# PRINT OUTPUT
# -----------------------------
print("India Data Extracted:\n")
for k, v in data.items():
    print(f"{k}: {v}")

# -----------------------------
# SAVE CSV (Ensure folder exists)
# -----------------------------
os.makedirs("data", exist_ok=True)

df = pd.DataFrame([data])
df.to_csv("data/india_test.csv", index=False)

print("\nSaved to data/india_test.csv")
