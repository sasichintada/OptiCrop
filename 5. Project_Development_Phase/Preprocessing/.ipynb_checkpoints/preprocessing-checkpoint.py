"""
Preprocessing Script for OptiCrop

This script handles all data preprocessing steps including:
1. Loading the dataset
2. Checking for missing values
3. Handling outliers
4. Feature scaling
5. Train-test split
6. Saving processed data
"""

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("🌾 OPTICROP - DATA PREPROCESSING")
print("="*60)

# ============================================
# 1. LOAD DATASET
# ============================================
print("\n📂 1. Loading Dataset...")

try:
    df = pd.read_csv('../Dataset/Crop_recommendation.csv')
    print(f"   ✅ Loaded {len(df)} rows and {len(df.columns)} columns")
    print(f"   📋 Columns: {list(df.columns)}")
except FileNotFoundError:
    print("   ❌ Error: Dataset not found at '../Dataset/Crop_recommendation.csv'")
    print("   ⚠️ Please make sure the dataset exists in the Dataset folder")
    exit()

# ============================================
# 2. DATA OVERVIEW
# ============================================
print("\n📊 2. Data Overview...")
print(f"   Shape: {df.shape}")
print(f"   Features: {list(df.columns)}")

# ============================================
# 3. CHECK MISSING VALUES
# ============================================
print("\n🔍 3. Checking for Missing Values...")
missing_values = df.isnull().sum()
if missing_values.sum() == 0:
    print("   ✅ No missing values found!")
else:
    print(f"   ⚠️ Found {missing_values.sum()} missing values:")
    print(missing_values[missing_values > 0])

# ============================================
# 4. DATA TYPES
# ============================================
print("\n📋 4. Data Types...")
print(df.dtypes)

# ============================================
# 5. HANDLE OUTLIERS (IQR Method)
# ============================================
print("\n📊 5. Handling Outliers...")

numeric_cols = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
outliers_count = 0

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outliers_count += len(outliers)
    
    if len(outliers) > 0:
        print(f"   {col}: {len(outliers)} outliers detected")
        # Cap outliers
        df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)

print(f"   ✅ Total outliers handled: {outliers_count}")

# ============================================
# 6. CHECK CROP DISTRIBUTION
# ============================================
print("\n🌾 6. Crop Distribution...")
crop_counts = df['label'].value_counts()
print(f"   Total unique crops: {len(crop_counts)}")
print(f"   Crop distribution:")
for crop, count in crop_counts.items():
    print(f"      - {crop}: {count} samples")

# ============================================
# 7. ENCODE TARGET VARIABLE
# ============================================
print("\n🔢 7. Encoding Target Variable...")

label_encoder = LabelEncoder()
df['label_encoded'] = label_encoder.fit_transform(df['label'])
print(f"   ✅ Encoded {len(label_encoder.classes_)} unique crops")
print(f"   📋 Crop mapping:")
for i, crop in enumerate(label_encoder.classes_):
    print(f"      - {crop}: {i}")

# ============================================
# 8. FEATURE SCALING
# ============================================
print("\n📊 8. Feature Scaling...")

# Separate features and target
X = df[numeric_cols].values
y = df['label_encoded'].values

# Initialize scaler
scaler = StandardScaler()

# Fit and transform features
X_scaled = scaler.fit_transform(X)
print(f"   ✅ Features scaled successfully!")

# ============================================
# 9. TRAIN-TEST SPLIT
# ============================================
print("\n📊 9. Train-Test Split...")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, stratify=y
)

print(f"   ✅ Training samples: {len(X_train)} (80%)")
print(f"   ✅ Testing samples: {len(X_test)} (20%)")

# ============================================
# 10. SAVE PROCESSED DATA
# ============================================
print("\n💾 10. Saving Processed Data...")

# Create processed folder if not exists
os.makedirs('processed', exist_ok=True)

# Save processed dataset
processed_df = df.copy()
processed_df['N_scaled'] = X_scaled[:, 0]
processed_df['P_scaled'] = X_scaled[:, 1]
processed_df['K_scaled'] = X_scaled[:, 2]
processed_df['temp_scaled'] = X_scaled[:, 3]
processed_df['humidity_scaled'] = X_scaled[:, 4]
processed_df['ph_scaled'] = X_scaled[:, 5]
processed_df['rainfall_scaled'] = X_scaled[:, 6]

processed_df.to_csv('processed/processed_crop_data.csv', index=False)
print("   ✅ Saved processed dataset to 'processed/processed_crop_data.csv'")

# Save scaler
with open('processed/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
print("   ✅ Saved scaler to 'processed/scaler.pkl'")

# Save label encoder
with open('processed/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)
print("   ✅ Saved label encoder to 'processed/label_encoder.pkl'")

# Save train-test split
np.save('processed/X_train.npy', X_train)
np.save('processed/X_test.npy', X_test)
np.save('processed/y_train.npy', y_train)
np.save('processed/y_test.npy', y_test)
print("   ✅ Saved train-test split to 'processed/'")

# ============================================
# 11. SUMMARY
# ============================================
print("\n" + "="*60)
print("✅ PREPROCESSING COMPLETED SUCCESSFULLY!")
print("📁 All processed files saved to 'Preprocessing/processed/'")
print("="*60)


print("\n📦 Processed data ready for model training!")
print(f"   🎯 Features: {len(numeric_cols)}")
print(f"   🌾 Crops: {len(label_encoder.classes_)}")
print(f"   📊 Training samples: {len(X_train)}")
print(f"   📊 Testing samples: {len(X_test)}")
print("="*60)
