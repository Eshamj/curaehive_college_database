import os
import pdfplumber
import pytesseract
import sys


sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from pdf2image import convert_from_path

from config import (
    RAW_FOLDER,
    TEXT_FOLDER,
    PROCESSED_FOLDER,
    POPPLER_PATH
)

# ------------------------------------
# GET PDF FILES
# ------------------------------------

def get_pdf_files():

    pdfs = []

    for file in os.listdir(RAW_FOLDER):

        if file.lower().endswith(".pdf"):
            pdfs.append(file)

    return pdfs


# ------------------------------------
# NORMAL PDF EXTRACTION
# ------------------------------------

def extract_using_pdfplumber(pdf_path):

    extracted_text = ""

    try:

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    extracted_text += text + "\n"

    except Exception as e:

        print("PDF Error:", e)

    return extracted_text


# ------------------------------------
# OCR EXTRACTION
# ------------------------------------

def extract_using_ocr(pdf_path):

    extracted_text = ""

    try:

        images = convert_from_path(
    pdf_path,
    poppler_path=POPPLER_PATH,
    fmt="png"
)

        for image in images:

            text = pytesseract.image_to_string(image)

            extracted_text += text + "\n"

    except Exception as e:

        print("OCR Error:", e)

    return extracted_text


# ------------------------------------
# DECIDE EXTRACTION METHOD
# ------------------------------------

def extract_text(pdf_path):

    text = extract_using_pdfplumber(pdf_path)

    if len(text.strip()) < 100:

        print("   Using OCR...")

        text = extract_using_ocr(pdf_path)

    return text


# ------------------------------------
# SAVE TXT FILE
# ------------------------------------

def save_text(filename, text):

    txt_name = filename.replace(".pdf", ".txt")

    output_path = os.path.join(
        TEXT_FOLDER,
        txt_name
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)

    return output_path


# ------------------------------------
# MAIN
# ------------------------------------

def main():

    print("=" * 60)
    print("CURAEHIVE PDF EXTRACTION")
    print("=" * 60)

    pdf_files = get_pdf_files()

    report = []

    for pdf in pdf_files:

        print("\nProcessing:", pdf)

        pdf_path = os.path.join(
            RAW_FOLDER,
            pdf
        )

        text = extract_text(pdf_path)

        output_file = save_text(
            pdf,
            text
        )

        characters = len(text)

        report.append({
            "PDF File": pdf,
            "Characters": characters,
            "Status":
                "Success"
                if characters > 0
                else "Failed"
        })

        print("   Characters:", characters)
        print("   Saved:", output_file)

    print("\n")
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for item in report:

        print(
            item["PDF File"],
            "->",
            item["Status"],
            "(",
            item["Characters"],
            "chars )"
        )


if __name__ == "__main__":
    main()