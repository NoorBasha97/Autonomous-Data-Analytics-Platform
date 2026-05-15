from tools.plot_tools import plot_histogram, plot_bar, plot_correlation_heatmap

def visualization_agent(state):
    print("Running visualization agent...")
    
    df = state["dataframe"]
    column_types = state["column_types"]
    
    plots = []
    
    #based on the column type ploting
    for col, col_type in column_types.items():
        if col_type == "numeric":
            plot = plot_histogram(df, col)
            plots.append((col, "histogram", plot))
            
        elif col_type == "categorical":
            plot = plot_bar(df, col)
            plots.append((col, "barplot", plot))
            
    #correlation heatmap
    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        heatmap = plot_correlation_heatmap(numeric_df)
        plots.append(("correlation", "heatmap", heatmap))
    
    print("Visualizations completed successfully.")
    #update the state
    state["plots"] = plots
    return state