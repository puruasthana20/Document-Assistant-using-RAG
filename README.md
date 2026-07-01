# 🧠 Production-Ready RAG Chat Assistant

A **Production-Ready Retrieval-Augmented Generation (RAG)** application that enables users to upload PDF documents and ask natural language questions about their contents.

The system processes uploaded PDFs, generates semantic embeddings using **Google Gemini Embedding API**, stores document vectors in **FAISS**, retrieves the most relevant document chunks, and generates accurate context-aware responses using **Gemini 2.5 Flash**.

The application follows a production-style architecture with a **FastAPI backend**, **Streamlit frontend**, and cloud deployment on **Render**.

---

# 🚀 Live Demo

### 🌐 Application

https://document-assistant-using-rag-3.onrender.com

### ⚙️ Backend API

https://document-assistant-using-rag-2.onrender.com

### 📖 API Documentation (Swagger)

https://document-assistant-using-rag-2.onrender.com/docs

---

# ✨ Features

- 📄 Upload any PDF document
- 💬 Chat with uploaded documents
- 🔍 Semantic search using Gemini Embeddings
- 🧠 Context-aware responses using Gemini 2.5 Flash
- ⚡ Automatic PDF processing after upload
- 📚 FAISS Vector Database
- 🎨 Interactive Streamlit Chat UI
- 🌐 FastAPI REST Backend
- 📄 Source chunk display
- 📝 Multiple response modes
  - Normal Mode
  - MCQ Mode
- ☁️ Cloud Deployment using Render
- 🚀 Lightweight architecture without Torch or Transformers

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
              Streamlit Frontend
                      │
               HTTP Requests
                      │
                      ▼
              FastAPI Backend
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 Document Processing         Question Answering

      PDF Upload                User Query
          │                         │
          ▼                         ▼
   PyPDFLoader              Gemini Embedding API
          │                         │
          ▼                         ▼
 Recursive Character        FAISS Similarity Search
 Text Splitter                     │
          │                         ▼
          ▼                  Top-K Retrieval
 Gemini Embedding API              │
          │                         ▼
          ▼                  Context Generation
     FAISS Index                   │
                                   ▼
                         Gemini 2.5 Flash LLM
                                   │
                                   ▼
                            Final Response
```

---

# 📁 Project Structure

```text
rag-project/
│
├── app.py                     # Streamlit Frontend
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── data/
│
└── src/
    ├── config.py
    ├── main.py
    ├── rag_pipeline.py
    ├── loader.py
    ├── chunking.py
    ├── embeddings.py
    ├── vectorstore.py
    ├── retriever.py
    └── generator.py
```

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## Backend

- FastAPI

## LLM

- Google Gemini 2.5 Flash

## Embedding Model

- Gemini Embedding API (`gemini-embedding-001`)

## Vector Database

- FAISS

## Frameworks

- LangChain
- Google GenAI SDK

## Deployment

- Render

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git

cd <repository-name>
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

(Optional for local development)

```env
BACKEND_URL=http://127.0.0.1:8000
```

---

# ▶️ Running the Project

## Start FastAPI Backend

```bash
uvicorn src.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Start Streamlit Frontend

```bash
streamlit run app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 💡 Usage

1. Open the Streamlit application.
2. Upload any PDF document.
3. Wait for the document to be processed.
4. Ask questions related to the uploaded PDF.
5. Receive context-aware answers generated using Gemini.
6. Expand **Sources** to view the retrieved document chunks.

---

# 🔄 Retrieval Pipeline

```text
User Question
      │
      ▼
Gemini Embedding API
      │
      ▼
FAISS Similarity Search
      │
      ▼
Top-K Retrieval
      │
      ▼
Context Generation
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Final Answer
```

---

# 🚀 Deployment Architecture

```text
                   Internet
                      │
        ┌─────────────┴─────────────┐
        │                           │
        ▼                           ▼
 Streamlit Frontend          FastAPI Backend
 (Render Web Service)      (Render Web Service)
        │                           │
        └──────────HTTP─────────────┘
```

---

# 📈 Performance Optimizations

- Removed Torch dependency
- Removed Transformers dependency
- Removed Sentence-Transformers
- Replaced local embeddings with Gemini Embedding API
- Lightweight deployment for Render Free Tier
- Modular project architecture
- Configurable parameters using `config.py`

---

# 🔥 Key Features

- Production-ready architecture
- Dynamic PDF upload
- Semantic document retrieval
- Context-aware question answering
- Cloud deployment
- FastAPI REST API
- Interactive Streamlit interface
- Gemini Embeddings
- Gemini 2.5 Flash
- FAISS Vector Search
- Multiple response modes
- Source chunk visualization

---

# ⚠️ Known Limitations

- Supports one uploaded document at a time.
- Uploaded documents are stored temporarily and are not persistent across backend restarts.
- Requires a valid Gemini API Key.
- Render free-tier services may sleep after inactivity, causing a short delay for the first request.

---

# 🚀 Future Improvements

- Multi-document retrieval
- Persistent FAISS storage
- Conversation memory
- Hybrid Search (BM25 + Dense Retrieval)
- Streaming responses
- Authentication & User Accounts
- Document management dashboard
- Docker support
- Kubernetes deployment
- RAG evaluation using RAGAS
- OCR support for scanned PDFs
- Citation-aware responses

---

# 📸 Screenshots

> Add screenshots of:
>
> - Home Page
> - PDF Upload
> - Chat Interface
> - Source Chunk Viewer
> - MCQ Mode

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you find any issues, feel free to open an issue or submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Puru Asthana**

AI & Machine Learning Enthusiast

- Machine Learning
- Natural Language Processing (NLP)
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Generative AI

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!