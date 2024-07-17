import io

import requests
import pdfplumber

def fextractURL(pdf_path):
    r = requests.get(pdf_path)
    f = io.BytesIO(r.content)
    extracted_data = ""
    with pdfplumber.open(f) as pdf:
        for page in pdf.pages:
            extracted_data += page.extract_text() + "\n"  # Extract text
            tables = page.extract_tables()  # Extract tables
            for table in tables:
                for row in table:
                    extracted_data += "\t".join(str(cell) for cell in row) + "\n"
    return extracted_data









