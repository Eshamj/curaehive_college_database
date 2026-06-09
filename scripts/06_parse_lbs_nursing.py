import pandas as pd
import re

INPUT_FILE = "data/extracted_text/lbscentre_colleges.txt"

records = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:

    line = line.strip()

    if "College of Nursing" not in line:
        continue

    district = ""

    districts = [
        "Kottayam",
        "Thrissur",
        "Ernakulam",
        "Kannur",
        "Kollam",
        "Pathanamthitta",
        "Alappuzha",
        "Idukki",
        "Palakkad",
        "Kozhikode",
        "Malappuram",
        "Kasargod",
        "Kasaragod",
        "Wayanad",
        "Thiruvananthapuram"
    ]

    for d in districts:
        if d.lower() in line.lower():
            district = d

    records.append({
        "college_name": line,
        "district": district
    })

df = pd.DataFrame(records)

df = df.drop_duplicates()

df.to_csv(
    "data/final/nursing_colleges_clean.csv",
    index=False
)

print(df.head(20))
print()
print("Rows:", len(df))