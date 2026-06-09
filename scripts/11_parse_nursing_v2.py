import re
import pandas as pd

INPUT_FILE = "data/extracted_text/lbscentre_colleges.txt"
OUTPUT_FILE = "data/final/nursing_v2.csv"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

districts = [
    "Thiruvananthapuram",
    "Kollam",
    "Pathanamthitta",
    "Alappuzha",
    "Kottayam",
    "Idukki",
    "Ernakulam",
    "Thrissur",
    "Palakkad",
    "Malappuram",
    "Kozhikode",
    "Wayanad",
    "Kannur",
    "Kasargod",
    "Kasaragod"
]

rows = []

lines = text.split("\n")

for line in lines:

    line = line.strip()

    if len(line) < 20:
        continue

    if "College of Nursing" not in line:
        continue

    merit_match = re.search(r"\s(\d+)\s+(\d+)\s*$", line)

    merit = None
    management = None

    if merit_match:
        merit = merit_match.group(1)
        management = merit_match.group(2)

    code_match = re.search(r"\b([A-Z]{3})\b", line)

    code = ""

    if code_match:
        code = code_match.group(1)

    district = ""

    for d in districts:
        if d.lower() in line.lower():
            district = d
            break

    college_name = line

    if code:
        college_name = college_name.replace(code, "")

    college_name = re.sub(r"^\d+", "", college_name).strip()

    college_type = "Private"

    if "Govt" in line or "Government" in line:
        college_type = "Government"

    rows.append({
        "college_code": code,
        "college_name": college_name,
        "district": district,
        "merit_seat": merit,
        "management_seat": management,
        "college_type": college_type
    })

df = pd.DataFrame(rows)

df = df.drop_duplicates(
    subset=["college_name"]
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("NURSING V2 DATASET")
print("=" * 50)

print(df.head(30))

print("\nRows:", len(df))
print("\nSaved:", OUTPUT_FILE)