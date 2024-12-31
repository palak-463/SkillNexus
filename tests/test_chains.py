from langchain_app.chains import build_qa_chain
def test_qa_chain():
    qa_chain-build_qa_chain()
    response=qa_chain.run("Explain Python loops.")
    assert "loop" in response