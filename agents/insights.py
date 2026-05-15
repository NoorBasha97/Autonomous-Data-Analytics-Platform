import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
load_dotenv()

def insights_agent(state):
    """
    Insights Agent:
    - Uses LLM to generate insights from EDA + statistics
    """
    print("Running Insights Agent...")

    eda = state["eda_summary"]
    stats = state["statistics"]
    #user query
    user_query = state.get("query", "General analysis")

    #Fallback 1: No useful data
    if not eda and not stats:
        print("No data available for insights")
        state["insights"] = "No sufficient data available to generate insights."
        state["insight_status"] = "no_data"
        return state
    
    try:
        #Fallback 2: API key check
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError("Missing GROQ API key")
        # Initialize Groq LLM
        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.3
        )
        
        # Prompt
        prompt = f"""
        You are a professional data analyst.
        
        User Request:
        {user_query}

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
    except Exception as e:
        print(f"LLM Failed: {e}")

        #FALLBACK OUTPUT (VERY IMPORTANT FOR UI)
        fallback_text = f"""
        ⚠️ AI insights could not be generated.

        However, here are some basic observations:

        - Dataset contains {state.get("num_rows", "unknown")} rows
        - Number of columns: {state.get("num_columns", "unknown")}
        - Available statistical data: {"Yes" if stats else "No"}

        Please check API configuration or try again.
        """

        state["insights"] = fallback_text
        state["insight_status"] = "fallback"
        state["error"] = f"Insights error: {str(e)}"

    return state