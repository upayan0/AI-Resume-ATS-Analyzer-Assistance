# from ai.gemini_client import ask_gemini
# from ai.prompt_templates import COVER_LETTER_PROMPT


# def generate_cover_letter(
#     resume_text,
#     jd_text
# ):

#     prompt = COVER_LETTER_PROMPT.format(
#         resume=resume_text,
#         jd=jd_text
#     )

#     return ask_gemini(prompt)


# # from ai.llm_client import ask_llm
# # from ai.prompt_templates import COVER_LETTER_PROMPT


# # def generate_cover_letter(
# #     resume_text,
# #     jd_text
# # ):

# #     prompt = COVER_LETTER_PROMPT.format(
# #         resume=resume_text,
# #         jd=jd_text
# #     )

# #     return ask_llm(prompt)

# ai/cover_letter_service.py
from ai.gemini_client import ask_gemini
from ai.prompt_templates import COVER_LETTER_PROMPT

def generate_cover_letter(resume_text: str, jd_text: str) -> str:
    """
    Generates a personalized, professional corporate cover letter.
    Returns a standard formatted string block ready for display or text-file export.
    """
    # 1. Format the cover letter prose prompt template with the raw parsed text elements
    prompt = COVER_LETTER_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )
    
    try:
        # 2. Request a standard text completion response from the Gemini client layer
        cover_letter_prose = ask_gemini(prompt)
        return cover_letter_prose.strip()
        
    except Exception as e:
        # Catch and surface clean error guidance to the user on the Streamlit screen
        return (
            f"ERROR: Unable to generate your tailored cover letter at this moment.\n"
            f"Details: {str(e)}\n\n"
            f"Please verify your API key configurations or input constraints and try again."
        )

# ==========================================
# 🔀 MULTI-MODEL COMPARATIVE ALTERNATIVE
# ==========================================
# If you want to let students explore cross-model comparative performance, 
# you can easily switch or keep your Groq alternative function ready here:

# from ai.llm_client import ask_llm

# def generate_cover_letter_via_llama(resume_text: str, jd_text: str) -> str:
#     prompt = COVER_LETTER_PROMPT.format(resume=resume_text, jd=jd_text)
#     try:
#         return ask_llm(prompt).strip()
#     except Exception as e:
#         return f"Groq Llama Cover Letter Generation Error: {str(e)}"