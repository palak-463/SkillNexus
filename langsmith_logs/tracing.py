from langsmith import Tracer
from langchain_app.chains import build_qa_chain
def trace_workflow(query):
    tracer=Tracer()
    qa_chain=build_qa_chain()
    with tracer.trace("Training Plan Workflow"):
        response=qa_chain.run(query)
        print(response)
if __name__=="__main__":
    trace_workflow("Create a Python training plan for beginners.")