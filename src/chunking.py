from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHUNK_SIZE, CHUNK_OVERLAP
def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    
    chunks = splitter.split_documents(documents)

    clean_chunks = []
    bad_phrases = [
        "discussion questions",
        "directions",
        "part a",
        "part b",
        "brainstorm",
        "multiple choice",
        "which of the following"
    ]

    for chunk in chunks:
        text = chunk.page_content.lower()
        
        if any(phrase in text for phrase in bad_phrases):
            continue
        
        clean_chunks.append(chunk)

    return clean_chunks