# from google import genai
# from config import GEMINI_API_KEY

# client = genai.Client(
#     api_key=GEMINI_API_KEY
# )

# def ask_gemini(prompt: str) -> str:

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt
#     )

#     return response.text

# ai/gemini_client.py
from google import genai
from google.genai import types
from config import GEMINI_API_KEY

# Initialize the official recommended SDK client structure
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: str, response_schema=None) -> str:
    """
    Sends a text prompt to the Gemini 2.5 Flash model.
    Optionally accepts a Pydantic BaseModel class schema to force structured JSON responses.
    """
    try:
        # Build configuration properties dynamically
        config_params = {}
        if response_schema:
            config_params["response_mime_type"] = "application/json"
            config_params["response_schema"] = response_schema
            config_params["temperature"] = 0.15  # Low temperature for deterministic/objective evaluation
            
        config = types.GenerateContentConfig(**config_params) if config_params else None

        # Execute generation telemetry across the API boundary
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=config
        )
        
        if not response.text:
            raise ValueError("The Gemini API returned an empty or unreadable text payload.")
            
        return response.text

    except Exception as e:
        # Catch and surface quota blocks, network jitter, or configuration errors safely
        raise RuntimeError(f"Gemini Service Communication Failure: {str(e)}")