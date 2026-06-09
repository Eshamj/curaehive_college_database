import pandas as pd

INPUT_FILE = "data/final/curaehive_nursing_master.csv"
OUTPUT_FILE = "data/final/curaehive_nursing_master_merged.csv"

df = pd.read_csv(INPUT_FILE)

merged_rows = []
skip_next = False

for i in range(len(df)):

    if skip_next:
        skip_next = False
        continue

    current = df.iloc[i].copy()

    # Check next row exists
    if i < len(df) - 1:

        next_row = df.iloc[i + 1]

        current_name = str(current["college_name"]).lower()
        next_name = str(next_row["college_name"]).lower()

        # Detect NRI row
        if (
            "nri" in next_name
            and current_name.split(",")[0] in next_name
        ):

            current["management_seat"] = next_row["merit_seat"]

            skip_next = True

    merged_rows.append(current)

final_df = pd.DataFrame(merged_rows)

final_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("=" * 50)
print("NRI MERGE COMPLETED")
print("=" * 50)

print(final_df.head(20))

print("\nRows:", len(final_df))
print("\nSaved:", OUTPUT_FILE)