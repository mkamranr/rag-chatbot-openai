import streamlit as st
import requests

st.title("🧠 RAG Chatbot")

# Upload PDF
st.header("📄 Upload a Document")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner("Uploading and ingesting..."):
        response = requests.post("http://localhost:8000/upload", files={"file": uploaded_file.getvalue()})
        if response.status_code == 200:
            st.success("Document uploaded and ingested.")
        else:
            st.error("Failed to upload the document.")

# Query input
st.header("💬 Ask a Question")
query = st.text_input("Enter your question")

if query:
    with st.spinner("Thinking..."):
        response = requests.get("http://localhost:8000/query", params={"query": query})
        if response.status_code == 200:
            answer = response.json().get("answer")
            st.success(answer)
        else:
            st.error("Failed to get a response.")
