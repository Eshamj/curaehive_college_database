import pandas as pd

df = pd.read_csv("data/final/curaehive_master.csv")

df["college_name"] = (
    df["college_name"]
    .astype(str)
    .str.replace(r"^\d+\s*", "", regex=True)
    .str.strip()
)

df.drop_duplicates(
    subset=["college_name", "course"],
    inplace=True
)

df.to_csv(
    "data/final/curaehive_master_clean.csv",
    index=False
)

print(df.head(20))
print("\nRows:", len(df))