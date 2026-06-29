"""
OptiCrop - Model Evaluation Script
Evaluates model performance with detailed metrics
"""

import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("📊 OPTICROP - MODEL EVALUATION")
print("="*70)

# ============================================
# LOAD MODEL AND DATASET
# ============================================

print("\n📂 Loading model and dataset...")

with open('models/crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

df = pd.read_csv('../Dataset/Crop_recommendation.csv')
print(f"✅ Model loaded successfully!")
print(f"✅ Dataset loaded: {len(df)} rows")

# ============================================
# PREPARE DATA
# ============================================

print("\n📊 Preparing data...")

X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ============================================
# CALCULATE METRICS
# ============================================

print("\n🤖 Calculating metrics...")
y_pred = model.predict(X_scaled)

accuracy = accuracy_score(y, y_pred) * 100
precision = precision_score(y, y_pred, average='weighted') * 100
recall = recall_score(y, y_pred, average='weighted') * 100
f1 = f1_score(y, y_pred, average='weighted') * 100

print(f"\n📈 ACCURACY METRICS:")
print(f"   ✅ Accuracy:  {accuracy:.2f}%")
print(f"   ✅ Precision: {precision:.2f}%")
print(f"   ✅ Recall:    {recall:.2f}%")
print(f"   ✅ F1-Score:  {f1:.2f}%")

# ============================================
# CLASSIFICATION REPORT
# ============================================

print("\n📋 Classification Report:")
print("-"*60)
print(classification_report(y, y_pred))

# ============================================
# CONFUSION MATRIX
# ============================================

cm = confusion_matrix(y, y_pred)
print(f"\n📊 Confusion Matrix Shape: {cm.shape}")

# ============================================
# CROSS-VALIDATION
# ============================================

print("\n🔄 Cross-Validation (5-Fold):")
cv_scores = cross_val_score(model, X_scaled, y, cv=5)
print(f"   Scores: {cv_scores}")
print(f"   Mean: {cv_scores.mean()*100:.2f}%")
print(f"   Std: {cv_scores.std()*100:.2f}%")

# ============================================
# FEATURE IMPORTANCE
# ============================================

if hasattr(model, 'feature_importances_'):
    print("\n📊 Feature Importance:")
    features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    importance = model.feature_importances_
    for name, imp in zip(features, importance):
        print(f"   {name:12}: {imp*100:.2f}%")

# ============================================
# SAVE RESULTS - FIXED ENCODING
# ============================================

print("\n💾 Saving results...")

try:
    with open('results/accuracy.txt', 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("OPTICROP - MODEL ACCURACY RESULTS\n")
        f.write("="*70 + "\n\n")
        f.write(f"Overall Accuracy   : {accuracy:.2f}%\n")
        f.write(f"Precision          : {precision:.2f}%\n")
        f.write(f"Recall             : {recall:.2f}%\n")
        f.write(f"F1-Score           : {f1:.2f}%\n\n")
        f.write("="*70 + "\n")
        f.write("CROSS-VALIDATION\n")
        f.write("="*70 + "\n")
        f.write(f"Mean CV Score    : {cv_scores.mean()*100:.2f}%\n")
        f.write(f"Std CV Score     : {cv_scores.std()*100:.2f}%\n\n")
        f.write("="*70 + "\n")
        f.write("FEATURE IMPORTANCE\n")
        f.write("="*70 + "\n")
        if hasattr(model, 'feature_importances_'):
            features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
            importance = model.feature_importances_
            for name, imp in zip(features, importance):
                f.write(f"{name}: {imp*100:.2f}%\n")
    print("✅ Saved results to 'results/accuracy.txt'")
except Exception as e:
    print(f"⚠️ Could not save to file: {e}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "="*70)
print("✅ EVALUATION COMPLETE!")
print("="*70)

print(f"""
📊 SUMMARY:
   - Dataset: {len(df)} samples
   - Best Model: Random Forest
   - Accuracy: {accuracy:.2f}%
   - Precision: {precision:.2f}%
   - Recall: {recall:.2f}%
   - F1-Score: {f1:.2f}%
   - Cross-Validation: {cv_scores.mean()*100:.2f}% (+/- {cv_scores.std()*100:.2f}%)
""")