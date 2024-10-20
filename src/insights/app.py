import pandas as pd
import streamlit as st
from lab_report_LLM_extractor.extraction import extract_lab_results
from utility.pdf_to_text import pdf_to_string
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    st.title("PDF to Text Converter")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        text = pdf_to_string(uploaded_file)
        extracted_data = extract_lab_results(text)
        Auftragsdatum = extracted_data.parsed.Auftragsdatum
        Befunddatum = extracted_data.parsed.Befunddatum
        Auftragsnummer = extracted_data.parsed.Auftragsnummer
        date_of_birth = extracted_data.parsed.dateofbirth
        gender = extracted_data.parsed.gender
        extracted_lab_report = extracted_data.parsed.entities
        df_data = []
        for entity in extracted_lab_report:
            df_data.append(
                {
                    "entity_type": entity.entity_type,
                    "value": entity.value,
                    "unit": entity.unit,
                    "upper_limit": entity.range.upper_limit,
                    "lower_limit": entity.range.lower_limit,
                }
            )

        df = pd.DataFrame(df_data)
        st.text_area("Auftragsdatum", Auftragsdatum)
        st.text_area("Befunddatum", Befunddatum)
        st.text_area("Auftragsnummer", Auftragsnummer)
        st.text_area("date of birth", date_of_birth)
        st.text_area("Gender", gender)
        st.dataframe(df)


if __name__ == "__main__":
    main()
