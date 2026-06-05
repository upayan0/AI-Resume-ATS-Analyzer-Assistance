# from pypdf import PdfReader


# def extract_jd_text(uploaded_file):

#     reader = PdfReader(uploaded_file)

#     text = ""

#     for page in reader.pages:

#         page_text = page.extract_text()

#         if page_text:
#             text += page_text + "\n"

#     return text

# parser/jd_parser.py
import re
from pypdf import PdfReader

def extract_jd_text(uploaded_file) -> str:
    """
    Extracts, cleans, and standardizes raw text from an uploaded Job Description PDF.
    """
    try:
        reader = PdfReader(uploaded_file)
        raw_text = ""
        
        # Extract plain text page-by-page
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                raw_text += page_text + "\n"
        
        # --- Advanced Text Sanitation Pipeline ---
        # 1. Strip non-ASCII glyphs, corrupted ligatures, or decorative symbols
        clean_text = re.sub(r'[^\x00-\x7F]+', ' ', raw_text)
        
        # 2. Collapse excessive whitespace, tabs, and duplicate line breaks into clean spaces
        clean_text = re.sub(r'\s+', ' ', clean_text)
        
        # Final safety check: Guard against empty strings (e.g., scanned/image-only PDFs)
        final_text = clean_text.strip()
        if not final_text:
            raise ValueError(
                "The uploaded document contains no extractable digital text. "
                "It may be empty or an un-scanned image file."
            )
            
        return final_text

    except Exception as e:
        # Pass a structural error string back up to the Streamlit UI layer safely
        raise RuntimeError(f"Document parsing failure: {str(e)}")