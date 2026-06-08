import os
import re
import pandas as pd

TEXT_FOLDER = "data/extracted_text"
OUTPUT_FILE = "data/processed/college_records.csv"

records = []

txt_files = os.listdir(TEXT_FOLDER)

for file in txt_files:

    if not file.endswith(".txt"):
        continue

    print(f"Processing {file}")

    path = os.path.join(TEXT_FOLDER, file)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) < 5:
            continue

        # Remove extra spaces
        clean_line = re.sub(r"\s+", " ", line)

        records.append({
            "source_file": file,
            "text": clean_line
        })

df = pd.DataFrame(records)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print()
print("=" * 50)
print("COLLEGE RECORD DATASET CREATED")
print("=" * 50)
print(df.head(20))
print()
print(f"Rows: {len(df)}")
print(f"Saved to: {OUTPUT_FILE}")