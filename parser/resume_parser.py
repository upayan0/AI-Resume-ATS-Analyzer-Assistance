# from pypdf import PdfReader


# def extract_resume_text(uploaded_file):

#     reader = PdfReader(uploaded_file)

#     text = ""

#     for page in reader.pages:

#         page_text = page.extract_text()

#         if page_text:
#             text += page_text + "\n"

#     return text


# parser/resume_parser.py
import re
from pypdf import PdfReader

def extract_resume_text(uploaded_file) -> str:
    """
    Extracts, cleans, and standardizes raw text from an uploaded candidate Resume PDF.
    """
    try:
        reader = PdfReader(uploaded_file)
        raw_text = ""
        
        # Iterate page-by-page to pull out digital text streams
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                raw_text += page_text + "\n"
        
        # --- Advanced Text Sanitation Pipeline ---
        # 1. Strip non-ASCII icons, decorative rating symbols, or broken character paths
        clean_text = re.sub(r'[^\x00-\x7F]+', ' ', raw_text)
        
        # 2. Convert erratic student spacing, tab sheets, and double-returns into unified single spaces
        clean_text = re.sub(r'\s+', ' ', clean_text)
        
        # Security Guardrail: Explicitly catch empty strings if they upload a graphic or photo of a resume
        final_text = clean_text.strip()
        if not final_text:
            raise ValueError(
                "The uploaded resume document contains no indexable digital text. "
                "Ensure the PDF is a digitally generated document and not an un-scanned image."
            )
            
        return final_text

    except Exception as e:
        # Pass a structural error string up to the Streamlit UI alert module safely
        raise RuntimeError(f"Resume text extraction error: {str(e)}")