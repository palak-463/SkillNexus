from langsmith_logs.tracing import trace_workflow
from langgraph_workflow.training_workflow import execute_workflow
def main():
    print("Running with LangSmith Observability...")
    trace_workflow("Create a Python training plan.")
    print("Running with LangGraph Workflow...")
    execute_workflow("Python training plan for beginners.")
if __name__=="__main__":
    main()