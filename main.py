from pprint import pprint
from agents.ingestion import data_ingestion_agent
from agents.eda import eda_agent
from agents.stats import statistical_agent
#This is central global state shared among all the agents
def initialize_state():
    return{
        "dataframe":None,
        "column_types": {},
        "num_rows": 0,
        "num_columns": 0,
        "eda_summary":"",
        "eda_text": "",
        "statistics":{},
        "plots":[],
        "insights":""
    }
    
if __name__ == "__main__":
    file_path = "sample_data.csv"  #dataset
    
    state = initialize_state()
    
    #1.Run the data ingestion agent
    state = data_ingestion_agent(state, file_path)
    
    #printing the output of data ingestion agent
    # print("\nColumn types:")
    # print(state["column_types"])
    # print("\nPreview data:")
    # print(state["dataframe"].head())

    #2. run the EDA agent
    state = eda_agent(state)
    
    #printing the output of EDA agent
    # print("\nEDA_Summary:")
    # pprint(state["eda_summary"])
    
    # print("\n EDA_text_in_HumanReadableForm:")
    # print(state["eda_text"])
    
    #3.Run the Stats Agent
    state = statistical_agent(state)
    
    print("\n Statistics:")
    pprint(state["statistics"])