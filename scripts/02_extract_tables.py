import os
import pandas as pd

TEXT_FOLDER = "data/extracted_text"
OUTPUT_FILE = "data/processed/master_raw_text.csv"

rows = []

for file in os.listdir(TEXT_FOLDER):

    if file.endswith(".txt"):

        path = os.path.join(TEXT_FOLDER, file)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        rows.append({
            "source_file": file,
            "text": text
        })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT_FILE, index=False)

print("="*50)
print("MASTER DATASET CREATED")
print("="*50)
print(df.head())
print()
print("Rows:", len(df))
print("Saved to:", OUTPUT_FILE)