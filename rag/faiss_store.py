# import faiss
# import numpy as np

# DIMENSION = 384

# index = faiss.IndexFlatL2(
#     DIMENSION
# )

# document_store = {}


# def add_document(
#     doc_id,
#     text,
#     embedding
# ):

#     embedding = np.array(
#         [embedding]
#     ).astype("float32")

#     index.add(embedding)

#     document_store[
#         index.ntotal - 1
#     ] = text


# def search_documents(
#     query_embedding,
#     k=5
# ):

#     query_embedding = np.array(
#         [query_embedding]
#     ).astype("float32")

#     distances, indices = index.search(
#         query_embedding,
#         k
#     )

#     results = []

#     for idx in indices[0]:

#         if idx in document_store:
#             results.append(
#                 document_store[idx]
#             )

#     return results





# rag/faiss_store.py
import faiss
import numpy as np
import pickle
import os
from config import FAISS_INDEX_DIR, METADATA_PATH

DIMENSION = 384

def init_or_load_vector_store():
    """
    Safely reads pre-saved vector weights and document structures from disk.
    If no index exists, it initializes a clean flat L2 distance matrix.
    """
    if os.path.exists(FAISS_INDEX_DIR) and os.path.exists(METADATA_PATH):
        try:
            index = faiss.read_index(FAISS_INDEX_DIR)
            with open(METADATA_PATH, "rb") as f:
                document_store = pickle.load(f)
            return index, document_store
        except Exception:
            # Fallback to fresh instantiation if data gets corrupted
            pass
            
    # Instantiate clean in-memory flat vector calculation layout
    index = faiss.IndexFlatL2(DIMENSION)
    document_store = {}
    return index, document_store


def save_vector_store(index, document_store):
    """Serializes the FAISS index layout and metadata dictionary to disk."""
    # Ensure parent directories exist
    os.makedirs(os.path.dirname(FAISS_INDEX_DIR), exist_ok=True)
    
    faiss.write_index(index, FAISS_INDEX_DIR)
    with open(METADATA_PATH, "wb") as f:
        pickle.dump(document_store, f)


def add_document(doc_id: str, text: str, embedding: list):
    """
    Appends a new text block to the local vector index.
    Saves the updated collection persistently to disk.
    """
    # 1. Load current persistent index state
    index, document_store = init_or_load_vector_store()
    
    # 2. Re-shape the float list into a strict 2D float32 NumPy matrix
    vector_matrix = np.array([embedding]).astype("float32")
    
    # 3. Add to the spatial database index
    index.add(vector_matrix)
    
    # 4. Map the internal FAISS index allocation pointer back to document metadata
    assigned_slot = index.ntotal - 1
    document_store[assigned_slot] = {
        "doc_id": doc_id,
        "text": text
    }
    
    # 5. Flush changes to disk
    save_vector_store(index, document_store)


def search_documents(query_embedding: list, k: int = 5) -> list:
    """
    Queries the vector coordinates map to isolate the top K most 
    semantically accurate text blocks.
    """
    index, document_store = init_or_load_vector_store()
    
    # Return empty results safely if no candidate metrics have been indexed yet
    if index.ntotal == 0:
        return []
        
    # Standardize query vector format for FAISS matching calculations
    query_matrix = np.array([query_embedding]).astype("float32")
    
    # Execute distance matrix search
    distances, indices = index.search(query_matrix, min(k, index.ntotal))
    
    results = []
    for idx in indices[0]:
        if idx in document_store:
            # Extract and return the parsed context dictionaries
            results.append(document_store[idx])
            
    return results