# from ai.gemini_client import ask_gemini
# from ai.prompt_templates import ROADMAP_PROMPT


# def generate_roadmap(
#     resume_text,
#     jd_text
# ):

#     prompt = ROADMAP_PROMPT.format(
#         resume=resume_text,
#         jd=jd_text
#     )

#     return ask_gemini(prompt)



# # from ai.llm_client import ask_llm
# # from ai.prompt_templates import ROADMAP_PROMPT


# # def generate_roadmap(
# #     resume_text,
# #     jd_text
# # ):

# #     prompt = ROADMAP_PROMPT.format(
# #         resume=resume_text,
# #         jd=jd_text
# #     )

# #     return ask_llm(prompt)





# ai/roadmap_service.py
import json
from ai.gemini_client import ask_gemini
from ai.prompt_templates import ROADMAP_PROMPT, UpskillingRoadmapSchema

def generate_roadmap(resume_text: str, jd_text: str) -> dict:
    """
    Orchestrates the generation of a personalized, timeline-driven upskilling roadmap.
    Enforces a strict structured JSON schema to divide recommended goals by timeline milestone phases.
    """
    # 1. Format the multi-phase roadmap prompt template with the raw parsed text inputs
    prompt = ROADMAP_PROMPT.format(
        resume=resume_text,
        jd=jd_text
    )
    
    # 2. Query Gemini while enforcing the structured UpskillingRoadmapSchema
    json_string_response = ask_gemini(prompt, response_schema=UpskillingRoadmapSchema)
    
    # 3. Safely parse the valid JSON string into an indexable Python dictionary
    try:
        return json.loads(json_string_response)
    except json.JSONDecodeError:
        # Secure structural fallback payload if parsing anomalies pop up
        return {
            "missing_skills": ["Failed to extract a structured roadmap from the model payload."],
            "recommended_certifications": [],
            "recommended_courses": [],
            "mock_projects": [],
            "plan_30_days": ["Structural formatting error encountered during timeline generation."],
            "plan_60_days": [],
            "plan_90_days": []
        }

# ==========================================
# 🔀 MULTI-MODEL COMPARATIVE ALTERNATIVE
# ==========================================
# If you want to let your students explore cross-model comparative content generation,
# you can easily switch or keep your Groq alternative function ready here:

# from ai.llm_client import ask_llm

# def generate_roadmap_via_llama(resume_text: str, jd_text: str) -> dict:
#     prompt = ROADMAP_PROMPT.format(resume=resume_text, jd=jd_text)
#     json_string_response = ask_llm(prompt, response_schema=UpskillingRoadmapSchema)
#     return json.loads(json_string_response)