import re
import pandas as pd

INPUT_FILE = "data/extracted_text/lbscentre_colleges.txt"
OUTPUT_FILE = "data/final/kottayam_thrissur_nursing.csv"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

results = []

capture = False

for line in lines:

    line = line.strip()

    if "B.Sc. Nursing Private Self Financing Colleges – ( Kottayam District)" in line:
        capture = "Kottayam"

    elif "B.Sc. Nursing Private Self Financing Colleges–( Thrissur District)" in line:
        capture = "Thrissur"

    elif "B.Sc. Nursing Private Self Financing Colleges – ( Idukky District)" in line:
        capture = False

    elif "B.Sc. Nursing Private Self Financing Colleges – ( Palakkad District)" in line:
        capture = False

    if not capture:
        continue

    if "College of Nursing" not in line:
        continue

    results.append({
        "district": capture,
        "raw_line": line
    })

df = pd.DataFrame(results)

print(df)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nRows:", len(df))
print("\nSaved:", OUTPUT_FILE)