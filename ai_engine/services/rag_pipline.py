
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ai_engine.utils.vector_store import save_chunks_to_vector_store, search_vector_store
from ai_engine.services.rag_client import GroqService

class FinancialRAGEngine:
    def __init__(self):
        # Initialize sub-services inside the engine
        self.groq = GroqService()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    def ingest_document(self, file_path):
        """Extracts text from PDF and saves to FAISS."""
        print(f">>> Reading PDF: {file_path}")
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted
                
        if not text.strip():
            raise ValueError("Could not extract any text. Is this a scanned image instead of a text PDF?")

        chunks = self.text_splitter.split_text(text)
        print(f">>> Split into {len(chunks)} chunks. Saving to FAISS...")
        
        save_chunks_to_vector_store(chunks)
        return True

    def ask_question(self, query):
        """Searches FAISS and queries Groq."""
        print(f">>> Searching FAISS for: '{query}'")
        
        docs = search_vector_store(query)
        
        if not docs:
            print("!!! FAISS returned no documents.")
            return "System Error: I couldn't find relevant information. Ensure a document is uploaded and indexed."

        context = "\n\n".join([doc.page_content for doc in docs])
        print(f">>> FAISS found {len(docs)} chunks of context.")
        
        # Pass the retrieved context to our Groq Class
        answer = self.groq.generate_response(query, context)
        return answer