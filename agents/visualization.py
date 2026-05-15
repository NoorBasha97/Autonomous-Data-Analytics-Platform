from tools.plot_tools import plot_histogram, plot_bar, plot_correlation_heatmap

def visualization_agent(state):
    """
    Visualization Agent:
    - Generates plots automatically based on data types
    """
    print("Running visualization agent...") # kept for debugging purpose
    
    df = state["dataframe"]
    column_types = state["column_types"]
    
     #  Fallback 1: No dataframe
    if df is None:
        raise ValueError("No dataframe available for visualization")

    #  Fallback 2: Empty dataframe
    if df.empty:
        raise ValueError("Empty dataframe")
    
    plots = []
    
    try:
        #based on the column type ploting
        for col, col_type in column_types.items():
            try:
                #  Skip high-cardinality categorical columns --fall back
                if col_type == "categorical" and df[col].nunique() > 20:
                    continue
                
                if col_type == "numeric":
                    plot = plot_histogram(df, col)
                    plots.append((col, "histogram", plot))
                    
                elif col_type == "categorical":
                    plot = plot_bar(df, col)
                    plots.append((col, "barplot", plot))
            except Exception as e:
                print(f"Skipping plot for {col}: {e}")
                continue  # skip only that column
        
        try:  
            #correlation heatmap
            numeric_df = df.select_dtypes(include=["number"])
            if not numeric_df.empty and numeric_df.shape[1] > 1:
                heatmap = plot_correlation_heatmap(numeric_df)
                plots.append(("correlation", "heatmap", heatmap))
        except Exception as e:
            print(f"Heatmap failed: {e}")
            
        #Fallback 3: No plots generated
        if not plots:
            print("No plots generated")
            state["plots"] = []
            state["plot_status"] = "No valid plots available"
        else:
            #if success then update the state
            state["plots"] = plots
            state["plot_status"] = "success"
            
        print("Visualizations completed successfully.")
    
    except Exception as e:
        print(f"Visualization Failed: {e}")

        #IMPORTANT: Don't break UI
        state["plots"] = []
        state["plot_status"] = "Visualization failed"
        state["error"] = f"Visualization error: {str(e)}"
    
    return state