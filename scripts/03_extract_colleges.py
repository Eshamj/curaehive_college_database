import pandas as pd
import re

INPUT = "data/processed/college_records.csv"
OUTPUT = "data/processed/master_colleges.csv"

df = pd.read_csv(INPUT)

records = []

for _, row in df.iterrows():

    text = str(row["text"])

    # Skip very short lines
    if len(text) < 5:
        continue

    # Look for lines that probably contain colleges
    keywords = [
        "college",
        "institute",
        "academy",
        "school of nursing",
        "medical college",
        "hospital"
    ]

    if any(word in text.lower() for word in keywords):

        intake = ""

        nums = re.findall(r"\d+", text)

        if nums:
            intake = nums[-1]

        records.append({
            "college_name": text,
            "possible_intake": intake,
            "source": row["source_file"]
        })

master = pd.DataFrame(records)

master = master.drop_duplicates(
    subset=["college_name"]
)

master.to_csv(
    OUTPUT,
    index=False
)

print("=" * 50)
print("MASTER COLLEGE DATASET")
print("=" * 50)

print(master.head(30))

print()
print("Total Colleges:", len(master))
print("Saved:", OUTPUT)