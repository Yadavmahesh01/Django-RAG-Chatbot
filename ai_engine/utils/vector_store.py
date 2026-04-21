# ai_engine/utils/vector_store.py
import os
from langchain_community.vectorstores import FAISS
from .embeddings import get_embedding_model

FAISS_INDEX_PATH = "faiss_index"

def save_chunks_to_vector_store(chunks):
    """Saves text chunks into the FAISS index."""
    embeddings = get_embedding_model()
    
    if os.path.exists(FAISS_INDEX_PATH):
        vector_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
        vector_store.add_texts(chunks)
    else:
        vector_store = FAISS.from_texts(chunks, embeddings)
        
    vector_store.save_local(FAISS_INDEX_PATH)

def search_vector_store(query, top_k=4):
    """Searches FAISS and returns the most relevant chunks."""
    if not os.path.exists(FAISS_INDEX_PATH):
        return None
        
    embeddings = get_embedding_model()
    vector_store = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    
    # Returns the actual chunks of text
    return vector_store.similarity_search(query, k=top_k)