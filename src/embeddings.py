import os
from typing import List

from google import genai
from langchain_core.embeddings import Embeddings
from src.config import GEMINI_API_KEY, GEMINI_EMBEDDING_MODEL


class GeminiEmbeddings(Embeddings):
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_EMBEDDING_MODEL

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = []

        for text in texts:
            response = self.client.models.embed_content(
                model=self.model,
                contents=text
            )
            embeddings.append(response.embeddings[0].values)

        return embeddings

    def embed_query(self, text: str) -> List[float]:
        response = self.client.models.embed_content(
            model=self.model,
            contents=text
        )

        return response.embeddings[0].values


def get_embeddings():
    return GeminiEmbeddings()