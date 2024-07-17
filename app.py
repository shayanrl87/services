import streamlit as st

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




st.write("Extarct full text from PDF url")

pdfURL = st.text_input(label="origin URL", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
button = st.button(label='Extract', key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False)
extractedText = st.empty()

if button:
    try:
        text = fextractURL(pdfURL)
        extractedText.text(text)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")