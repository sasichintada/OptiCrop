import pandas as pd
import numpy as np

print("="*70)
print("📊 OPTICROP - DATASET VIEWER")
print("="*70)

# Load dataset
df = pd.read_csv('Dataset/Crop_recommendation.csv')

print("\n📁 Dataset Information:")
print("-"*50)
print(f"   File: Crop_recommendation.csv")
print(f"   Total Rows: {len(df)}")
print(f"   Total Columns: {len(df.columns)}")
print(f"   Features: {list(df.columns)}")

print("\n📊 Feature Statistics:")
print("-"*50)
print(df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']].describe())

print("\n🌾 All Crops in Dataset:")
print("-"*50)
crops = df['label'].unique()
for i, crop in enumerate(crops, 1):
    count = len(df[df['label'] == crop])
    print(f"   {i:2}. {crop:15} - {count} samples")

print("\n📊 Sample Data for Each Crop:")
print("-"*70)
print(f"{'Crop':15} | {'N':6} | {'P':6} | {'K':6} | {'Temp':8} | {'Humidity':8} | {'pH':6} | {'Rainfall':8}")
print("-"*70)

for crop in crops:
    sample = df[df['label'] == crop].iloc[0]
    print(f"{crop:15} | {sample.N:6.0f} | {sample.P:6.0f} | {sample.K:6.0f} | {sample.temperature:8.2f} | {sample.humidity:8.2f} | {sample.ph:6.2f} | {sample.rainfall:8.2f}")

print("\n" + "="*70)
print("✅ Dataset loaded successfully!")
print("="*70)