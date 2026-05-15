from langgraph.graph import StateGraph , END
from agents.ingestion import data_ingestion_agent
from agents.eda import eda_agent
from agents.stats import statistical_agent
from agents.visualization import visualization_agent
from agents.insights import insights_agent
from agents.supervisor import supervisor_node, supervisor_router


def create_workflow():

    workflow = StateGraph(dict)

    # Nodes
    workflow.add_node("supervisor", supervisor_node)
    workflow.add_node("ingestion", data_ingestion_agent)
    workflow.add_node("eda", eda_agent)
    workflow.add_node("stats", statistical_agent)
    workflow.add_node("visualization", visualization_agent)
    workflow.add_node("insights", insights_agent)

    # Entry point
    workflow.set_entry_point("supervisor")

    # Conditional routing
    workflow.add_conditional_edges(
        "supervisor",
        supervisor_router,
        {
            "ingestion": "ingestion",
            "eda": "eda",
            "stats": "stats",
            "visualization": "visualization",
            "insights": "insights",
            "end": END
        }
    )

    # Loop back to supervisor
    workflow.add_edge("ingestion", "supervisor")
    workflow.add_edge("eda", "supervisor")
    workflow.add_edge("stats", "supervisor")
    workflow.add_edge("visualization", "supervisor")
    workflow.add_edge("insights", "supervisor")

    return workflow.compile()