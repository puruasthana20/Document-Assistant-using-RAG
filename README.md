# 🧠 Production-Ready Retrieval-Augmented Generation (RAG) System

A Production-Ready Retrieval-Augmented Generation (RAG) application that allows users to upload any PDF document and ask natural language questions about its contents.

The system retrieves the most relevant document chunks using semantic search, improves retrieval quality through reranking, and generates context-aware answers using a local Large Language Model (LLM).

---

# 🚀 Features

* 📄 Upload any PDF document
* 💬 Chat with uploaded documents
* 🔍 Semantic search using embeddings
* 🎯 Cross-Encoder reranking for improved retrieval accuracy
* 🤖 Local LLM inference using Ollama
* 🌐 FastAPI backend
* 🎨 Streamlit chat interface
* 📚 Source chunk display
* 📝 Multiple response modes

  * Normal
  * MCQ
* ⚡ Automatic document processing after upload

---

# 🏗️ System Architecture

```
                  +----------------+
                  |  Streamlit UI  |
                  +-------+--------+
                          |
                          |
                    HTTP Requests
                          |
                          v
                  +----------------+
                  |   FastAPI API  |
                  +-------+--------+
                          |
          +---------------+----------------+
          |                                |
          |                                |
          v                                v
Document Processing                 Question Answering

PDF Loader                     Retriever
      ↓                              ↓
Chunking                     Top-K Retrieval
      ↓                              ↓
Embeddings                  Cross Encoder Reranker
      ↓                              ↓
FAISS Vector Store          Context Creation
                                     ↓
                               Ollama LLM
                                     ↓
                                Final Answer
```

---

# 📁 Project Structure

```
rag-project/

│
├── app.py                     # Streamlit UI
│
├── src/
│   ├── main.py                # FastAPI Backend
│   ├── rag_pipeline.py
│   ├── loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── reranker.py
│   ├── generator.py
│   └── vectorstore.py
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

# 🛠️ Tech Stack

## Backend

* FastAPI
* LangChain

## Frontend

* Streamlit

## Vector Database

* FAISS

## Embeddings

* BAAI/bge-small-en

## Reranker

* BAAI/bge-reranker-base

## LLM

* Ollama
* Phi-3 (recommended)

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git

cd <repository-name>
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download Ollama

https://ollama.com

Install the recommended model

```bash
ollama pull phi3
```

You may also use another supported Ollama model if your system has sufficient RAM.

---

# ▶️ Running the Project

## Step 1 — Start Ollama

Open a terminal and run

```bash
ollama serve
```

If Ollama is already running, you can skip this step.

---

## Step 2 — Start FastAPI Backend

Open a new terminal

Activate the virtual environment

```bash
.venv\Scripts\activate
```

Run

```bash
uvicorn src.main:app --reload
```

Backend will start at

```
http://127.0.0.1:8000
```

Swagger API Documentation

```
http://127.0.0.1:8000/docs
```

---

## Step 3 — Start Streamlit

Open another terminal

Activate virtual environment

```bash
.venv\Scripts\activate
```

Run

```bash
streamlit run app.py
```

Streamlit UI

```
http://localhost:8501
```

---

# 💡 Usage

1. Open the Streamlit application.
2. Upload a PDF document.
3. Wait until processing completes.
4. Ask questions related to the uploaded document.
5. View the generated answer along with retrieved source chunks.

---

# 📊 Retrieval Pipeline

```
User Question

↓

Embedding Search

↓

Top-K Retrieval

↓

Cross Encoder Reranking

↓

Context Generation

↓

LLM

↓

Answer
```

---

# 🔥 Improvements over Basic RAG

* Dynamic PDF Upload
* FastAPI REST Backend
* Streamlit Chat Interface
* Cross-Encoder Reranking
* Improved Chunk Filtering
* Source Display
* Multiple Response Modes

---

# ⚠️ Known Limitations

* One document can be queried at a time.
* Uploaded documents are not persisted after restarting the backend.
* Requires Ollama and a supported local model.
* Large models may require more system RAM.

---

# 🚀 Future Improvements

* Multi-document querying
* Persistent vector database
* Conversational memory
* Hybrid Search (BM25 + Dense Retrieval)
* Query rewriting
* RAGAS evaluation
* Cloud deployment
* Authentication
* Streaming responses

---

# 👨‍💻 Author

**Puru Asthana**

AI / ML Enthusiast

Focused on Machine Learning, NLP, LLMs and Retrieval-Augmented Generation systems.
