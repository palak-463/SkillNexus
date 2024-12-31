from langchain_app.retriever import get_retriever
def test_retriever():
    retriever=get_retriever()
    results=retriever.get_relevant_documents("Python basics")
    assert len(results)>0