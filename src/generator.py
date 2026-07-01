import os
from google import genai
from dotenv import load_dotenv
from src.config import GEMINI_CHAT_MODEL
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiLLM:
    def invoke(self, prompt):
        response = client.models.generate_content(
            model=GEMINI_CHAT_MODEL,
            contents=prompt
        )
        return response.text

def get_llm():
    return GeminiLLM()