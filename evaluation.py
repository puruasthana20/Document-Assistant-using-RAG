from ragas import evaluate
from datasets import Dataset

def evaluate_rag(questions, answers, contexts, ground_truths):
    data = {
        "question": questions,
        "answer": answers,
        "contexts": contexts,
        "ground_truth": ground_truths
    }

    dataset = Dataset.from_dict(data)
    result = evaluate(dataset)

    return result