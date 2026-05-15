from tools.data_tools import load_data,handle_missing_values,detect_column_types

def data_ingestion_agent(state):
    """
    Data Ingestion Agent:
    - Loads data
    - Cleans missing values
    - Detects column types
    """
    print("Data ingestion agent is running....") #kept this for debugging purpose
    
    file_path = state["file_path"]
    #1.load data
    df = load_data(file_path)
    
    #2.handle missing values
    df = handle_missing_values(df)
    
    #3.detect the column types
    column_types = detect_column_types(df)
    
    #now update the shared state
    state["dataframe"] = df
    state["column_types"] = column_types
    
    print("Data ingestion is successfully completed")
    
    return state