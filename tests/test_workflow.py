from langgraph_workflow.training_workflow import execute_workflow
def test_workflow():
    results=execute_workflow("Python basics")
    assert "Python" in results