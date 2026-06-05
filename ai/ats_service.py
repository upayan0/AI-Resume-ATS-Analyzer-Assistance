# from ai.gemini_client import ask_gemini
# from ai.prompt_templates import ATS_PROMPT


# def generate_ats_report(
#     resume_text,
#     jd_text
# ):

#     prompt = ATS_PROMPT.format(
#         resume=resume_text,
#         jd=jd_text
#     )

#     return ask_gemini(prompt)


# # from ai.llm_client import ask_llm
# # from ai.prompt_templates import ATS_PROMPT


# # def generate_ats_report(
# #     resume_text,
# #     jd_text
# # ):

# #     prompt = ATS_PROMPT.format(
# #         resume=resume_text,
# #         jd=jd_text
# #     )

# #     return ask_llm(prompt)




# # ai/ats_service.py
# import json
# from ai.gemini_client import ask_gemini
# from ai.prompt_templates import ATS_PROMPT, ATSReportSchema

# def generate_ats_report(resume_text: str, jd_text: str) -> dict:
#     """
#     Orchestrates the resume-to-JD evaluation.
#     Enforces a strict structured JSON output and returns a clean Python dictionary.
#     """
#     # 1. Format the structured system prompt template with the raw parsed text inputs
#     prompt = ATS_PROMPT.format(
#         resume=resume_text,
#         jd=jd_text
#     )
    
#     # 2. Query Gemini while enforcing the formal Pydantic validation schema
#     json_string_response = ask_gemini(prompt, response_schema=ATSReportSchema)
    
#     # 3. Safely convert the validated JSON string into an indexable Python dictionary
#     try:
#         return json.loads(json_string_response)
#     except json.JSONDecodeError:
#         # Secure structural fallback data if any parsing anomolies pop up
#         return {
#             "ats_score": 0,
#             "match_percentage": 0,
#             "resume_summary": "Failed to parse structured response from the AI engine.",
#             "skills_found": [],
#             "missing_skills": ["Structural formatting error encountered."],
#             "strengths": [],
#             "weaknesses": ["Parsing failure."],
#             "improvement_suggestions": ["Re-run the compliance diagnostics loop."],
#             "final_recommendation": "Error"
#         }

# # ==========================================
# # 🔀 MULTI-MODEL COMPARATIVE ALTERNATIVE
# # ==========================================
# # If you want to let students swap between providers to benchmark models,
# # you can keep your Groq/Llama route active with an alternative function:

# # from ai.llm_client import ask_llm

# # def generate_ats_report_via_llama(resume_text: str, jd_text: str) -> dict:
# #     prompt = ATS_PROMPT.format(resume=resume_text, jd=jd_text)
# #     json_string_response = ask_llm(prompt, response_schema=ATSReportSchema)
# #     return json.loads(json_string_response)


# ai/ats_service.py
import json
import logging
from ai.gemini_client import ask_gemini
from ai.prompt_templates import ATS_PROMPT, ATSReportSchema

# Try to import your Groq client for automatic fallback failover routing
try:
    from ai.llm_client import ask_llm
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

def generate_ats_report(resume_text: str, jd_text: str) -> dict:
    """
    Evaluates profile matching parameters. 
    Automatically switches to Groq/Llama 3.3 if the Gemini API returns a 503 overload error.
    """
    prompt = ATS_PROMPT.format(resume=resume_text, jd=jd_text)
    
    try:
        # 1. Attempt primary processing using Gemini 2.5 Flash
        json_string_response = ask_gemini(prompt, response_schema=ATSReportSchema)
        return json.loads(json_string_response)
        
    except Exception as gemini_error:
        # Check if the failure is specifically a 503 demand spike overload
        if "503" in str(gemini_error) and GROQ_AVAILABLE:
            logging.warning("GEMINI OVERLOAD DETECTED (503). AUTOMATICALLY ROUTING TO GROQ FALLBACK SUITE...")
            
            try:
                # 2. Seamlessly route to Llama-3.3-70b via Groq using the identical schema
                json_string_response = ask_llm(prompt, response_schema=ATSReportSchema)
                return json.loads(json_string_response)
            except Exception as groq_error:
                gemini_error = RuntimeError(f"Both AI Engines overloaded. Groq Error: {str(groq_error)}")
        
        # 3. Structural fallback if both models fail or Groq is not configured
        return {
            "ats_score": 0,
            "match_percentage": 0,
            "resume_summary": f"The AI services are currently overloaded. Please wait a moment and click retry. (Details: {str(gemini_error)})",
            "skills_found": [],
            "missing_skills": ["Service temporary unavailable."],
            "strengths": [],
            "weaknesses": ["API Overload spike encountered."],
            "improvement_suggestions": ["Click the calculation trigger button again in 30 seconds."],
            "final_recommendation": "System Retry Required"
        }