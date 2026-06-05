# from ai.gemini_client import ask_gemini
# from ai.prompt_templates import INTERVIEW_PROMPT


# def generate_interview_questions(
#     resume_text,
#     jd_text
# ):

#     prompt = INTERVIEW_PROMPT.format(
#         resume=resume_text,
#         jd=jd_text
#     )

#     return ask_gemini(prompt)



# # from ai.llm_client import ask_llm
# # from ai.prompt_templates import INTERVIEW_PROMPT


# # def generate_interview_questions(
# #     resume_text,
# #     jd_text
# # ):

# #     prompt = INTERVIEW_PROMPT.format(
# #         resume=resume_text,
# #         jd=jd_text
# #     )

# #     return ask_llm(prompt)




# ai/interview_service.py
import json
from ai.gemini_client import ask_gemini
from ai.prompt_templates import INTERVIEW_PROMPT, InterviewPrepSchema

def generate_interview_questions(resume_text: str, jd_text: str) -> dict:
    """
    Orchestrates candidate-specific mock interview question extraction.
    Enforces a strict structured JSON schema to separate questions by category.
    """
    # 1. Format the multi-category interview prompt with the raw parsed text inputs
    prompt = INTERVIEW_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )
    
    # 2. Query Gemini while enforcing the structured InterviewPrepSchema
    json_string_response = ask_gemini(prompt, response_schema=InterviewPrepSchema)
    
    # 3. Safely parse the structural JSON string into an indexable Python dictionary
    try:
        return json.loads(json_string_response)
    except json.JSONDecodeError:
        # Secure structural fallback payload if parsing anomalies pop up
        return {
            "technical_questions": ["Failed to extract technical questions from the model payload."],
            "project_questions": ["Failed to extract project-specific architectural questions."],
            "hr_questions": ["Failed to extract HR screening questions."],
            "behavioral_questions": ["Failed to extract situational behavioral questions."]
        }

# ==========================================
# 🔀 MULTI-MODEL COMPARATIVE ALTERNATIVE
# ==========================================
# If you want to run cross-model comparative benchmarks with your students,
# you can seamlessly switch or keep your Groq alternative function ready here:

# from ai.llm_client import ask_llm

# def generate_interview_questions_via_llama(resume_text: str, jd_text: str) -> dict:
#     prompt = INTERVIEW_PROMPT.format(resume=resume_text, jd=jd_text)
#     json_string_response = ask_llm(prompt, response_schema=InterviewPrepSchema)
#     return json.loads(json_string_response)