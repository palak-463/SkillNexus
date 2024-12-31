from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from retriever import get_retriever
def build_qa_chain():
    retriever=get_retriever()
    qa_chain=RetrievalQA(llm=ChatOpenAI(), retriever=retriever)
    return qa_chain