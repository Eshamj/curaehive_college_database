import pandas as pd

df = pd.read_csv("data/final/curaehive_nursing_master_merged.csv")

print("=" * 50)
print("DATASET VALIDATION")
print("=" * 50)

print("\nTotal Rows:")
print(len(df))

print("\nMissing District:")
print(df["district"].isna().sum())

print("\nMissing Merit Seats:")
print(df["merit_seat"].isna().sum())

print("\nMissing Management Seats:")
print(df["management_seat"].isna().sum())

print("\nMissing College Code:")
print(df["college_code"].isna().sum())

print("\nDuplicate Colleges:")
print(df["college_name"].duplicated().sum())

print("\nRows Missing District:")
print(
    df[df["district"].isna()][
        ["college_name", "college_code"]
    ].head(50)
)

print("\nRows Missing Seats:")
print(
    df[df["merit_seat"].isna()][
        ["college_name", "district"]
    ].head(50)
)