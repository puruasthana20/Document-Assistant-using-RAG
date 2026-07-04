from sentence_transformers import CrossEncoder

# Load model once (IMPORTANT)
reranker_model = CrossEncoder("BAAI/bge-reranker-base")

def rerank(query, docs, top_k=3):
    pairs = [(query, doc.page_content) for doc in docs]

    scores = reranker_model.predict(pairs)

    # Combine docs + scores
    scored_docs = list(zip(docs, scores))

    # Sort by score (descending)
    ranked_docs = sorted(scored_docs, key=lambda x: x[1], reverse=True)

    # Return top_k docs only
    return [doc for doc, score in ranked_docs[:top_k]]
