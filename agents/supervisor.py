def supervisor_node(state):
    print("Supervisor running...")
    return state

def supervisor_router(state):
    """
    Decides which agent to run next
    """
    print("Supervisor deciding next step...")

    #routing logic
    if state.get("dataframe") is None:
        return "ingestion"

    if not state.get("eda_summary"):
        return "eda"

    if not state.get("statistics"):
        return "stats"

    if not state.get("plots"):
        return "visualization"

    if not state.get("insights"):
        return "insights"

    return "end"