from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Load PDF
loader = PyPDFLoader("cinderella.pdf")  # change filename if needed
documents = loader.load()

# 2. Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)

# 3. Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 4. Vector Store
vectorstore = FAISS.from_documents(chunks, embeddings)

# 5. Query loop
while True:
    query = input("\nAsk something: ")

    # Retrieve
    docs = vectorstore.similarity_search(query, k=5)

    # 🔥 Filter junk (basic)
    filtered_docs = []
    for doc in docs:
        text = doc.page_content.lower()

        if any(word in text for word in [
            "references", "table", "figure", 
            "et al", "arxiv", "google brain", "university"
        ]):
            continue

        if len(text.strip()) < 100:
            continue

        filtered_docs.append(doc)

    docs = filtered_docs

    # ✅ Print retrieved chunks (ONLY LOOP HERE)
    print("\n--- Retrieved Chunks ---")
    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}:\n{doc.page_content[:300]}")

    # ✅ Combine chunks (OUTSIDE LOOP)
    final_text = "\n\n".join([doc.page_content for doc in docs])

    # ✅ Print answer ONCE
    print("\n--- Answer ---")
    print(final_text[:700])