# from rag.embeddings import generate_embedding
# from rag.faiss_store import search_documents


# def retrieve_context(
#     query_text
# ):

#     query_embedding = generate_embedding(
#         query_text
#     )

#     results = search_documents(
#         query_embedding
#     )

#     return "\n".join(results)




# rag/retrieval.py
from rag.embeddings import generate_embedding
from rag.faiss_store import search_documents

def retrieve_context(query_text: str, top_k: int = 5) -> str:
    """
    Transforms a natural language search query into an vector representation,
    isolates the top K most relevant text matches inside the FAISS index,
    and returns a single unified context string for LLM processing.
    """
    # 1. Guard check to stop processing on completely empty context requests
    if not query_text or not query_text.strip():
        return ""

    # 2. Map the plain-text search query directly into vector coordinates
    query_embedding = generate_embedding(query_text)

    # 3. Search coordinates to pull back the top K most structurally aligned data segments
    matched_metadata_records = search_documents(query_embedding, k=top_k)

    # 4. Safely extract and isolate the plain text values from the returned metadata records
    extracted_text_segments = []
    for record in matched_metadata_records:
        if isinstance(record, dict) and "text" in record:
            extracted_text_segments.append(record["text"])
        elif isinstance(record, str):
            # Safe structural fallback processing for legacy text strings
            extracted_text_segments.append(record)

    # 5. Compile the extracted text segments into a single unified context block
    return "\n\n---\n\n".join(extracted_text_segments)