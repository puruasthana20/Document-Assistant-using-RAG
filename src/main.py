from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from src.rag_pipeline import process_document, run_rag
import os

app = FastAPI()

# Create upload directory automatically
UPLOAD_DIR = "data"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class QueryRequest(BaseModel):
    question: str
    mode: str = "normal"


@app.get("/")
def home():
    return {"message": "RAG API running"}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(content)

    process_document(file_path)

    return {
        "message": f"{file.filename} uploaded and processed successfully"
    }


@app.post("/query")
def query_rag(request: QueryRequest):
    return run_rag(request.question, request.mode)