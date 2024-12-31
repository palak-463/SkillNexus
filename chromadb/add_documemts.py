from chroma_setup import initialize_chroma
from langchain.embeddings.openai import OpenAIEmbeddings
def add_documents_to_chroma():
    client, collection=initialize_chroma()
    embedding_model=OpenAIEmbeddings()
    documents=[
        {"id":"1","text":"Basics of Python programming for beginners."},
        {"id":"2"."text":"Introduction to data visualization with Matplotlib."}
    ]
    for doc in documents:
        embedding=embedding_model.embed_query(doc["text"])
        collection.add(ids=[doc["id"]], documents=[doc["text"]], embeddings=[embedding])
if __name__=="__main__":
    add_documents_to_chroma()