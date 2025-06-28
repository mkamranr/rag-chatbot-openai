from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from app.retriever import load_vector_db
from app.config import OPENAI_API_KEY
import os

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def get_qa_chain():
    vectordb = load_vector_db()
    llm = ChatOpenAI(temperature=0.3)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return qa_chain

def query_bot(query: str):
    qa = get_qa_chain()
    return qa.run(query)
