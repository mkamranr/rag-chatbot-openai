from fastapi import FastAPI, UploadFile, File
from app.retriever import ingest_document
from app.rag_pipeline import query_bot

app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    with open(f"temp_{file.filename}", "wb") as f:
        f.write(await file.read())
    ingest_document(f"temp_{file.filename}")
    return {"status": "Document ingested."}

@app.get("/query")
def ask(query: str):
    answer = query_bot(query)
    return {"answer": answer}
