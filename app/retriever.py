from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from app.config import *
import os

def ingest_document(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=OVERLAP)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectordb = FAISS.from_documents(chunks, embedding=embeddings)
    vectordb.save_local(VECTOR_STORE_PATH)
    return vectordb

def load_vector_db():
    if not os.path.exists(VECTOR_STORE_PATH):
        raise ValueError("Vector store not found. Run ingestion first.")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectordb = FAISS.load_local(VECTOR_STORE_PATH, embeddings)
    return vectordb
