import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
import pandas as pd
from config import TARGET_DISTRICTS

INPUT = "data/processed/clean_colleges.csv"
OUTPUT = "data/processed/kt_tcr_colleges.csv"


df = pd.read_csv(INPUT)

filtered = []

for _, row in df.iterrows():

    name = str(row["college_name"]).lower()

    if any(term in name for term in TARGET_DISTRICTS):

        filtered.append(row)

result = pd.DataFrame(filtered)

result = result.drop_duplicates(
    subset=["college_name"]
)

result.to_csv(
    OUTPUT,
    index=False
)

print("="*50)
print("KOTTAYAM + THRISSUR FILTER")
print("="*50)

print(result.head(30))

print()
print("Rows:", len(result))
print("Saved:", OUTPUT)