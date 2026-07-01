from src.config import TOP_K
def get_retriever(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="similarity",   # explicit
        search_kwargs={"k": 7}
    )
    return retriever