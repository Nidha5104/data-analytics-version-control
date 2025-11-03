# data_cleaning.py

import pandas as pd

def clean(df):
    # Drop rows with all NaN values
    df = df.dropna(how="all")
    # Convert numeric columns safely
    if "value" in df.columns:
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
    return df

if __name__ == "__main__":
    print("Running data cleaning demo.")
