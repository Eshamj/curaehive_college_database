import pandas as pd
import re

INPUT = "data/processed/master_colleges.csv"
OUTPUT = "data/processed/clean_colleges.csv"

df = pd.read_csv(INPUT)

REMOVE_PATTERNS = [
    "sl college",
    "college name",
    "course name",
    "intake",
    "diploma",
    "md ",
    "ms ",
    "bams",
    "bsc",
    "mbbs",
    "vidhi",
    "vigyana",
    "samanya",
    "shalya",
    "kriyasarir",
]

clean_rows = []

for _, row in df.iterrows():

    name = str(row["college_name"]).strip()

    lower = name.lower()

    skip = False

    for pattern in REMOVE_PATTERNS:
        if pattern in lower:
            skip = True
            break

    if skip:
        continue

    # remove extra spaces
    name = re.sub(r"\s+", " ", name)

    clean_rows.append({
        "college_name": name,
        "source": row["source"]
    })

clean = pd.DataFrame(clean_rows)

clean = clean.drop_duplicates(
    subset=["college_name"]
)

clean.to_csv(
    OUTPUT,
    index=False
)

print("=" * 50)
print("CLEAN DATASET")
print("=" * 50)

print(clean.head(50))

print()
print("Total:", len(clean))
print("Saved:", OUTPUT)