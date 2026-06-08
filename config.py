import os
import pytesseract

# -----------------------------------
# OCR SETTINGS
# -----------------------------------

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

POPPLER_PATH = r"C:\poppler\poppler-26.02.0\Library\bin"

# -----------------------------------
# FOLDERS
# -----------------------------------

RAW_FOLDER = "data/raw"

TEXT_FOLDER = "data/extracted_text"

PROCESSED_FOLDER = "data/processed"

ENRICHED_FOLDER = "data/enriched"

FINAL_FOLDER = "data/final"

# -----------------------------------
# CREATE FOLDERS
# -----------------------------------

folders = [
    TEXT_FOLDER,
    PROCESSED_FOLDER,
    ENRICHED_FOLDER,
    FINAL_FOLDER
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)