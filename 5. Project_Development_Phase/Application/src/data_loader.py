# src/data_loader.py

import pandas as pd
import numpy as np

def load_agricultural_data():
    """Load agricultural dataset from CSV file"""
    print("📊 Loading Agricultural Dataset...")
    
    # Load dataset using pandas read_csv
    df = pd.read_csv('data/Crop_recommendation.csv')
    
    print(f"✅ Data loaded successfully!")
    print(f"   Shape: {df.shape}")
    print(f"   Features: {', '.join(df.columns)}")
    print(f"   Target: {df.columns[-1]}")
    
    return df

if __name__ == "__main__":
    df = load_agricultural_data()
    print(df.head())
