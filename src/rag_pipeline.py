from src.loader import load_documents
from src.chunking import chunk_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore
from src.retriever import get_retriever
from src.generator import get_llm
from src.config import FINAL_CONTEXT_DOCS
retriever = None
llm = get_llm()

def process_document(file_path: str):
    global retriever

    documents = load_documents(file_path)
    chunks = chunk_documents(documents)
    embeddings = get_embeddings()
    vectorstore = create_vectorstore(chunks, embeddings)
    retriever = get_retriever(vectorstore)

def run_rag(query: str, mode="normal"):
    global retriever

    if retriever is None:
        return {"answer": "Please upload a document first.", "sources": []}

    docs = retriever.invoke(query)

    docs = docs[:FINAL_CONTEXT_DOCS]

    context = "\n".join([doc.page_content for doc in docs])

    if mode == "mcq":
        prompt = f"""
        Answer in MCQ style using context.

        Context:
        {context}

        Question:
        {query}
        """
    else:
        prompt = f"""
        Answer clearly using context only.

        Context:
        {context}

        Question:
        {query}
        """

    response = llm.invoke(prompt)

    return {
        "answer": response,
        "sources": [doc.page_content for doc in docs]
    }