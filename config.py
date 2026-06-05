# from dotenv import load_dotenv
# import os

# load_dotenv()

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# # from dotenv import load_dotenv
# # import os

# # load_dotenv()

# # GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# config.py
import os
from dotenv import load_dotenv

# 1. Load environmental variables from your local encrypted .env file
load_dotenv()

# =====================================================================
# 🔑 CENTRALIZED SECRET API KEY MANAGEMENT
# =====================================================================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Enterprise Guardrail ---
# Ensures the application halts immediately on initialization if the core 
# token string is missing or empty, avoiding ambiguous runtime errors deep 
# inside your backend AI service modules.
if not GEMINI_API_KEY:
    raise ValueError(
        "CRITICAL APPLICATION SETUP ERROR: 'GEMINI_API_KEY' is missing or unreadable in your .env file. "
        "Please confirm your token configuration before restarting the engine."
    )


# =====================================================================
# 📁 RELATIONAL DATABASE & LOCAL STORAGE PATHS
# =====================================================================
# Defines static paths for storing student screening logs and metrics
DB_PATH = "database/ats_records.db"


# =====================================================================
# 🧬 SEMANTIC RAG VECTOR CONFIGURATIONS (FAISS)
# =====================================================================
# Establishes specific coordinate storage paths on your disk, 
# ensuring indexed student resumes persist across hot-reloads and application restarts.
FAISS_INDEX_DIR = "rag/faiss_index.bin"
METADATA_PATH = "rag/faiss_metadata.pkl"


# =====================================================================
# 🖨️ EXPORT SUB-SYSTEM DIRECTORY PATHS
# =====================================================================
# Central location for generating downloadable ReportLab candidate audit PDFs
PDF_OUTPUT_DIR = "outputs"