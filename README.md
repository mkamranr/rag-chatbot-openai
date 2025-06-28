# RAG Chatbot: Retrieval-Augmented Generation with OpenAI + HuggingFace + FAISS

This project demonstrates a chatbot using **RAG** (Retrieval-Augmented Generation), powered by OpenAI's GPT models and HuggingFace embeddings with FAISS vector store.

## 🧠 Features
- Upload PDF documents
- Automatically chunk, embed, and index with FAISS
- Ask natural language questions and get contextual answers
- Built with FastAPI for easy integration

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/mkamranr/rag-chatbot-openai.git
cd rag-chatbot-openai
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI key
Edit `app/config.py` and replace:
```python
OPENAI_API_KEY = "your-openai-api-key"
```

### 4. Run the app
```bash
uvicorn app.main:app --reload
```

### 5. Upload PDF and Ask
- POST `/upload` with a PDF
- GET `/query?query=Your question here`

## 🛠️ Tech Stack
- **FastAPI** – Web server
- **LangChain** – Chaining + Vector DB utils
- **FAISS** – Vector storage
- **OpenAI GPT** – LLM backend
- **HuggingFace** – Embeddings (MiniLM)

## 📁 Sample PDF
You can test with `data/sample.pdf` or upload your own.

## 📌 Future Improvements
- Support multi-file ingestion
- Streamlit / React front-end
- Use open-source LLMs (e.g. Mistral) via vLLM or LM Studio
