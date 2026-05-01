questions = [
    "What is RAG?",
    "What are embeddings in machine learning?",
    "Why are embeddings important in RAG systems?",
    "What is cosine similarity?",
    "What is chunking in document processing?",
    "Why is chunking important in RAG?",
    "What is FAISS used for?",
    "What is semantic search?",
    "Difference between keyword search and semantic search?",
    "What is a vector database?",
    "What is the role of retriever in RAG?",
    "What is the role of generator in RAG?",
    "What is prompt engineering?",
    "What is hallucination in LLMs?",
    "How can hallucination be reduced in RAG systems?"
]


ground_truths = [
    "RAG stands for Retrieval Augmented Generation, a technique that combines document retrieval with text generation.",
    
    "Embeddings are vector representations of text that capture semantic meaning.",
    
    "Embeddings help convert text into vectors so similarity between queries and documents can be computed.",
    
    "Cosine similarity measures the similarity between two vectors based on the cosine of the angle between them.",
    
    "Chunking is the process of splitting large documents into smaller pieces.",
    
    "Chunking ensures relevant parts of documents are retrieved instead of entire large documents.",
    
    "FAISS is a library used for efficient similarity search and vector retrieval.",
    
    "Semantic search finds results based on meaning rather than exact keyword matching.",
    
    "Keyword search matches exact words, while semantic search understands the meaning of the query.",
    
    "A vector database stores embeddings and allows similarity-based retrieval.",
    
    "The retriever fetches relevant documents based on the query.",
    
    "The generator creates the final answer using retrieved context.",
    
    "Prompt engineering is designing effective prompts to guide LLM output.",
    
    "Hallucination is when an LLM generates incorrect or fabricated information.",
    
    "Hallucination can be reduced by grounding responses in retrieved documents and using strict prompts."
]