from agents.ingestion import data_ingestion_agent
#This is central global state shared among all the agents
def initialize_state():
    return{
        "dataframe":None,
        "eda_summary":"",
        "statistics":{},
        "plots":[],
        "insights":""
    }
    
if __name__ == "__main__":
    file_path = "sample_data.csv"  #dataset
    
    state = initialize_state()
    
    state = data_ingestion_agent(state, file_path)
    
    #kept for debugging purpose
    print("\nColumn types:")
    print(state["column_types"])
    
    print("\nPreview data:")
    print(state["dataframe"].head())