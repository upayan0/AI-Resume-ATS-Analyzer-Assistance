# from ai.gemini_client import ask_gemini
# from ai.prompt_templates import (
#     RESUME_REWRITE_PROMPT
# )


# def rewrite_resume(
#     resume_text
# ):

#     prompt = RESUME_REWRITE_PROMPT.format(
#         resume=resume_text
#     )

#     return ask_gemini(prompt)



# # from ai.llm_client import ask_llm
# # from ai.prompt_templates import RESUME_REWRITE_PROMPT


# # def rewrite_resume(
# #     resume_text
# # ):

# #     prompt = RESUME_REWRITE_PROMPT.format(
# #         resume=resume_text
# #     )

# #     return ask_llm(prompt)




# ai/resume_rewriter_service.py
import json
from ai.gemini_client import ask_gemini
from ai.prompt_templates import RESUME_REWRITE_PROMPT, ResumeRewriteSchema

def rewrite_resume(resume_text: str) -> dict:
    """
    Orchestrates candidate profile and project description optimization.
    Enforces a strict structured JSON schema to isolate rewritten components cleanly.
    """
    # 1. Format the optimization prompt template with the candidate's text
    prompt = RESUME_REWRITE_PROMPT.format(
        resume=resume_text
    )
    
    # 2. Query Gemini while enforcing the formal validation schema
    json_string_response = ask_gemini(prompt, response_schema=ResumeRewriteSchema)
    
    # 3. Safely parse the valid JSON string into a structured Python dictionary
    try:
        return json.loads(json_string_response)
    except json.JSONDecodeError:
        # Secure structural fallback payload if parsing anomalies pop up
        return {
            "optimized_summary": "Failed to extract a structured optimization summary from the model payload.",
            "rewritten_projects": ["Structural formatting error encountered during project refactoring."],
            "rewritten_experience_points": ["Structural formatting error encountered during experience refactoring."],
            "suggested_ats_keywords": []
        }

# ==========================================
# 🔀 MULTI-MODEL COMPARATIVE ALTERNATIVE
# ==========================================
# If you want to let students evaluate cross-model content adjustments,
# you can easily switch or keep your Groq/Llama alternative function ready here:

# from ai.llm_client import ask_llm

# def rewrite_resume_via_llama(resume_text: str) -> dict:
#     prompt = RESUME_REWRITE_PROMPT.format(resume=resume_text)
#     json_string_response = ask_llm(prompt, response_schema=ResumeRewriteSchema)
#     return json.loads(json_string_response)