# ai_engine/utils/embeddings.py
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """
    Returns the embedding model used across the entire project.
    Production Tip: If we change to OpenAI embeddings later, 
    we only change this ONE file!
    """
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")