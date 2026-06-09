import pandas as pd

all_data = []

# Nursing
nursing = pd.read_csv(
    "data/final/kottayam_thrissur_nursing.csv"
)

for _, row in nursing.iterrows():
    all_data.append({
        "college_name": row["raw_line"],
        "district": row["district"],
        "course": "BSc Nursing",
        "source_pdf": "lbscentre_colleges.pdf"
    })

master = pd.DataFrame(all_data)

master.to_csv(
    "data/final/curaehive_master.csv",
    index=False
)

print(master.head(20))
print("\nRows:", len(master))
print("\nSaved: data/final/curaehive_master.csv")