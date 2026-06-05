# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )


# def generate_embedding(text):

#     embedding = model.encode(text)

#     return embedding



# rag/embeddings.py
from sentence_transformers import SentenceTransformer

# Loads an open-source, lightweight text embedding model generating 384 dimensions
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text: str) -> list:
    """
    Transforms plain text into a normalized 384-dimensional vector coordinate array.
    Converts the output into a Python list to ensure strict FAISS compatibility.
    """
    try:
        # Guard against processing empty or null strings
        if not text or not text.strip():
            return [0.0] * 384
            
        # Generate the dense spatial embedding array
        embedding_array = model.encode(text)
        
        # Convert to standard Python list format to align with FAISS specifications
        return embedding_array.tolist()
        
    except Exception as e:
        raise RuntimeError(f"Embedding Generation Subsystem Exception: {str(e)}")