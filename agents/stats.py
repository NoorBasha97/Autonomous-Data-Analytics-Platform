import pandas as pd

def statistical_agent(state):
    print("Running the statistical agent...")
    
    df = state["dataframe"]
    #selecting only the numeric columns
    numeric_df = df.select_dtypes(include=["number"])
    
    #statistical summary
    stats_summary = {}
    
    for col in numeric_df.columns:
        stats_summary[col] = {
            "mean": numeric_df[col].mean(),
            "median": numeric_df[col].median(),
            "std": numeric_df[col].std(),
            "min": numeric_df[col].min(),
            "max": numeric_df[col].max()
        }
    
    #correlation matrix
    correlation_matrix = numeric_df.corr().to_dict()
    
    #store these in the shared state
    state["statistics"] = {
        "basic_stats": stats_summary,
        "correlation": correlation_matrix
    }
    
    print("Statistical analysis is successfully completed.")
    return state