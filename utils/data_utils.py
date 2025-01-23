import pandas as pd

def load_data(file_path="data/DoorDash_Mock_Data.csv"):
    """Load the dataset from a file."""
    return pd.read_csv(file_path)

def validate_and_clean_data(df):
    """Validate and clean the uploaded dataset."""
    # Required columns
    required_columns = ["order_date", "base_pay", "tips", "peak_pay", "adjustments"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Ensure order_date is a datetime
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    if df['order_date'].isnull().any():
        raise ValueError("Invalid dates detected in `order_date` column.")
    
    # Fill missing numeric values
    numeric_columns = ["base_pay", "tips", "peak_pay", "adjustments"]
    df[numeric_columns] = df[numeric_columns].fillna(0)
    
    # Add total earnings column
    df['total_earnings'] = df['base_pay'] + df['tips'] + df['peak_pay'] + df['adjustments']
    return df
