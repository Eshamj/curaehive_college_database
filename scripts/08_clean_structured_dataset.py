import pandas as pd
import re

df = pd.read_csv(
    "data/final/structured_nursing_dataset.csv"
)

# -------------------------
# CLEAN COLLEGE NAME
# -------------------------

def clean_name(text):

    text = str(text)

    # remove leading numbers

    text = re.sub(r"^\d+\s*", "", text)

    # remove college code

    text = re.sub(r"^[A-Z]{3}\s+", "", text)

    # remove phone numbers

    text = re.sub(r"\d{10,}", "", text)

    # remove seat patterns

    text = re.sub(r"\bNU\b.*", "", text)

    text = text.strip()

    return text

df["college_name"] = df["college_name"].apply(clean_name)

# -------------------------
# COLLEGE TYPE
# -------------------------

def college_type(name):

    name = str(name).lower()

    if "govt" in name:
        return "Government"

    return "Private"

df["college_type"] = df["college_name"].apply(college_type)

# -------------------------
# SOURCE
# -------------------------

df["source_pdf"] = "lbscentre_colleges.pdf"

# -------------------------
# PLACEHOLDERS
# -------------------------

df["website"] = ""
df["address"] = ""

# -------------------------
# SAVE
# -------------------------

output = "data/final/curaehive_nursing_master.csv"

df.to_csv(
    output,
    index=False
)

print(df.head(20))
print()
print("Rows:", len(df))
print()
print("Saved:", output)