
from groq import Groq
from django.conf import settings


class GroqService:
    def __init__(self):
        api_key = getattr(settings, 'GROQ_API_KEY', None)
        if not api_key:
            raise ValueError("GROQ_API_KEY is missing!")
            
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile" 

    

    def generate_response(self, query, context):
        """Generates answer using Context + Query"""
        system_prompt = f"""You are a helpful Financial AI Assistant. 
        Use the following extracted document context to answer the user's question. 
        If you don't know the answer based on the context, say so.
        
        CONTEXT:
        {context}
        """

        try:
            print(">>> Sending prompt to Groq API...")
            response = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                model=self.model,
                temperature=0.2,
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"!!! GROQ API ERROR: {e}")
            return f"Error from Groq API: {str(e)}"