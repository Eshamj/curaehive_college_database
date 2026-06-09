import pandas as pd
import re

INPUT_FILE = "data/extracted_text/lbscentre_colleges.txt"

records = []

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

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

for line in lines:

    if "College of Nursing" not in line:
        continue

    district = ""

    for d in districts:
        if d.lower() in line.lower():
            district = d
            break

    code_match = re.search(r"\b[A-Z]{3}\b", line)

    college_code = ""

    if code_match:
        college_code = code_match.group()

    merit_match = re.search(r"\b(\d{1,3})\s+(NA|\d{1,3})\b", line)

    merit = ""
    management = ""

    if merit_match:
        merit = merit_match.group(1)
        management = merit_match.group(2)

    records.append({
        "college_code": college_code,
        "college_name": line,
        "district": district,
        "merit_seat": merit,
        "management_seat": management
    })

df = pd.DataFrame(records)

df.to_csv(
    "data/final/structured_nursing_dataset.csv",
    index=False
)

print(df.head(20))
print()
print("Rows:", len(df))
print()
print("Saved: data/final/structured_nursing_dataset.csv")