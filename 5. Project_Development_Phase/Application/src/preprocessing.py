# src/preprocessing.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import matplotlib.pyplot as plt  # ADD THIS LINE
import seaborn as sns             # ADD THIS LINE
import pickle
import os
import warnings
warnings.filterwarnings('ignore')

def preprocess_data(df):
    """Preprocess agricultural dataset"""
    
    print("\n🔧 Data Preprocessing")
    print("="*60)
    
    # Create directories
    os.makedirs('models', exist_ok=True)
    
    # 1. Check dataset
    print(f"Dataset Shape: {df.shape}")
    print(f"Features: {df.columns.tolist()}")
    
    # 2. Check null values
    print(f"\nNull Values:\n{df.isnull().sum()}")
    
    # 3. Check for outliers using boxplots
    print("\n📊 Outlier Detection with Boxplots")
    plt.figure(figsize=(14, 8))
    df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].boxplot()
    plt.title('Boxplot for Outlier Detection')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outlier_boxplots.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # 4. Handle outliers using IQR
    print("\n🔍 Handling Outliers using IQR Method")
    print(f"Upper Bound = Q3 + 1.5 × IQR")
    print(f"Lower Bound = Q1 - 1.5 × IQR")
    
    df_cleaned = df.copy()
    for col in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']:
        Q1 = df_cleaned[col].quantile(0.25)
        Q3 = df_cleaned[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df_cleaned[(df_cleaned[col] < lower_bound) | (df_cleaned[col] > upper_bound)]
        print(f"  {col}: {len(outliers)} outliers detected")
        
        # Cap outliers
        df_cleaned[col] = df_cleaned[col].clip(lower=lower_bound, upper=upper_bound)
    
    # 5. Log transformation for Potassium (as mentioned)
    print("\n📈 Applying Log Transformation to Potassium")
    df_cleaned['K_log'] = np.log1p(df_cleaned['K'])
    
    # 6. Extract seasonal crops
    print("\n🌱 Extracting Seasonal Crops")
    seasonal_crops = {
        'Summer': df[(df['temperature'] > 25) & (df['rainfall'] < 150)]['label'].unique(),
        'Winter': df[(df['temperature'] < 20) & (df['humidity'] > 50)]['label'].unique(),
        'Rainy': df[(df['rainfall'] > 200) & (df['humidity'] > 70)]['label'].unique()
    }
    
    for season, crops in seasonal_crops.items():
        print(f"  {season}: {list(crops)[:5]}...")  # Show first 5 crops
    
    # 7. Create features and target
    X = df_cleaned[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df_cleaned['label']
    
    # 8. Encode target
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # 9. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    print(f"\n📊 Data Split:")
    print(f"  X_train: {X_train.shape}")
    print(f"  X_test: {X_test.shape}")
    print(f"  y_train: {y_train.shape}")
    print(f"  y_test: {y_test.shape}")
    
    # 10. Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 11. Save preprocessors
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    with open('models/label_encoder.pkl', 'wb') as f:
        pickle.dump(le, f)
    
    print("\n✅ Preprocessors saved to models/")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, le, scaler

if __name__ == "__main__":
    # Load data
    from data_loader import load_agricultural_data
    df = load_agricultural_data()
    
    # Preprocess
    X_train, X_test, y_train, y_test, le, scaler = preprocess_data(df)
