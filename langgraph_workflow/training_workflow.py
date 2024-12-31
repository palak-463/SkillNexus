from langgraph import Graph, Node
from langchain_app.retriever import get_retriever
from langchain_app.chains import build_qa_chain
def execute_workflow(query):
    retriever_node=Node(name="Retrieve from Chroma", function=get_retriever().get_relevant_documents)
    response_node=Node(name="Generate Traning Plan", fucntion=build_qa_chain().run)
    workflow=Graph()
    workflow.add_node(retriver_node)
    workflow.add_node(response_node)
    workflow.add_edge(retriever_node, response_node, condition="results_found")
    results=workflow.run(query)
    print(results)
if __name__=="__main__":
    execute_workflow("Python training plan for beginners.")
    