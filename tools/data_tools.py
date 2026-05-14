import os
import pandas as pd

def load_data(file_path):
    """
    Load CSV or Excel file into pandas DataFrame
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("File doesnot exists!")
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
        if df.empty:
            raise ValueError("Dataset is empty")
        return df
    
    except Exception as e:
        raise Exception(f"Error in loading the file : {e}")
    
def handle_missing_values(df):
    """
    Simple missing value handling:
    - Numeric → fill with mean
    - Categorical → fill with mode
    """
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
            
    return df

def detect_column_types(df):
    """
    Detect column types
    """
    column_tyeps = {}
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            column_tyeps[col] = "numeric"
        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            column_tyeps[col] = "datetime"
        else:
            column_tyeps[col] = "categorical"
            
    return column_tyeps