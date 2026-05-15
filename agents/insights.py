import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
load_dotenv()

def insights_agent(state):
    print("Running Insights Agent...")

    # Initialize Groq LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    eda = state["eda_summary"]
    stats = state["statistics"]
    
    #user query
    user_query = state.get("query", "General analysis")

    # Prompt
    prompt = f"""
    You are a professional data analyst.

    Based on the dataset:

    1. Identify key trends
    2. Highlight correlations
    3. Detect anomalies
    4. Suggest business insights

    Data:
    EDA Summary:
    {str(eda)[:2000]}

    Statistical Analysis:
    {str(stats)[:2000]}
    """

    # Get response
    response = llm.invoke(prompt)
    # Store insights
    state["insights"] = response.content

    print("Insights Generated.")

    return state