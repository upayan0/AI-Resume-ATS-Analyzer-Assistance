# from groq import Groq
# from config import GROQ_API_KEY

# client = Groq(
#     api_key=GROQ_API_KEY
# )

# def ask_llm(prompt):

#     try:

#         completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": prompt
#                 }
#             ],
#             temperature=0.3,
#             max_tokens=4096
#         )

#         return completion.choices[0].message.content

#     except Exception as e:

#         return f"Error: {str(e)}"




# # ai/llm_client.py
# import json
# from groq import Groq
# from config import os

# # Initialize the Groq client routing layer safely if keys exist
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

# def ask_llm(prompt: str, response_schema=None) -> str:
#     """
#     Sends a text prompt to the Llama 3.3 model via Groq.
#     Optionally accepts a Pydantic schema class to enforce strict structured JSON output.
#     """
#     if not client:
#         raise ValueError(
#             "Groq Client is uninitialized. Ensure 'GROQ_API_KEY' is active in your .env file."
#         )

#     try:
#         # 🛠️ Configuration parameters setup
#         params = {
#             "model": "llama-3.3-70b-versatile",
#             "messages": [{"role": "user", "content": prompt}],
#             "temperature": 0.15,  # Low temperature for objective screening
#             "max_tokens": 4096
#         }

#         # Inject Pydantic tool constraints if a JSON schema is requested
#         if response_schema:
#             params["response_format"] = {
#                 "type": "json_object",
#                 "schema": response_schema.model_json_schema()
#             }

#         # Execute generation stream across the Groq API boundary
#         completion = client.chat.completions.create(**params)
        
#         output_text = completion.choices[0].message.content
#         if not output_text:
#             raise ValueError("The inference gateway returned an empty message payload.")
            
#         return output_text

#     except Exception as e:
#         # Prevent runtime breaking by surface-routing clean error messages up to Streamlit
#         raise RuntimeError(f"Groq Cloud Inference Service Exception: {str(e)}")