import pandas as pd

def eda_agent(state):
    """
    EDA Agent:
    - Generates dataset summary
    - Missing values analysis
    - Basic statistics
    """
    #kept this for debugging purpose
    print("Running EDA agent........")
    
    df = state["dataframe"]
    #basic info
    num_rows, num_cols = df.shape
    columns = list(df.columns)
    dtypes = df.dtypes.astype(str).to_dict()
    
    # Missing values
    missing_values = df.isnull().sum().to_dict()
    
    # Descriptive statistics
    describe = df.describe(include="all").fillna("").to_dict()
    
    #structured output
    eda_summary = {
        "shape": {
            "rows": num_rows,
            "columns": num_cols
        },
        "columns": columns,
        "data_types": dtypes,
        "missing_values": missing_values,
        "describe": describe
    }
    # Human-readable summary
    summary_text = f"""
    Dataset has {num_rows} rows and {num_cols} columns.

    Columns:
    {columns}

    Missing Values:
    {missing_values}
    """

    # Update state
    state["eda_summary"] = eda_summary
    state["eda_text"] = summary_text

    print("Execution of EDA agent is completed successfully.....")

    return state