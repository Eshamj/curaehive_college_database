import pandas as pd

master = pd.read_csv("data/final/curaehive_master.csv")

new_rows = [
    {
        "college_name": "Amala Institute of Medical Sciences",
        "district": "Thrissur",
        "course": "MBBS",
        "source_pdf": "mbbs.pdf"
    },
    {
        "college_name": "Pushpagiri Institute of Medical Sciences & Research Centre",
        "district": "Kottayam",
        "course": "MBBS",
        "source_pdf": "mbbs.pdf"
    },
    {
        "college_name": "Amala College of Allied Health Sciences",
        "district": "Thrissur",
        "course": "BSc MLT",
        "source_pdf": "bsc mlt.pdf"
    },
    {
        "college_name": "School of Medical Education, Gandhi Nagar",
        "district": "Kottayam",
        "course": "BSc MLT",
        "source_pdf": "bsc mlt.pdf"
    }
]

master = pd.concat([master, pd.DataFrame(new_rows)], ignore_index=True)

master.to_csv(
    "data/final/curaehive_master.csv",
    index=False
)

print("Rows:", len(master))
print(master.tail(10))