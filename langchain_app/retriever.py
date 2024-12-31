from langchain.vectorstore import Chroma
from langchain.emdeddings.openai import OpenAIEmbeddings
def get_retriever():
    embedding_model=OpenAIEmbeddings()
    vector_store=Chroma(collection_name="training_docs",embedding_function=embedding_model)
    return vector_store.as_retriever()