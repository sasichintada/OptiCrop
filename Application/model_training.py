import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("🤖 OPTI CROP - MODEL BUILDING")
print("="*60)

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dataset_path = os.path.join(BASE_DIR, '..', 'Dataset', 'Crop_recommendation.csv')
model_save_path = os.path.join(BASE_DIR, '..', 'Model', 'models')

# Create models directory if it doesn't exist
os.makedirs(model_save_path, exist_ok=True)

# Load data
print("\n1. Loading Dataset...")
try:
    df = pd.read_csv(dataset_path)
    print(f"   ✅ Loaded {len(df)} rows")
    print(f"   📊 Columns: {list(df.columns)}")
except FileNotFoundError:
    print(f"   ❌ Dataset not found at: {dataset_path}")
    exit()

# Prepare data
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Split data
print("\n2. Splitting Data...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"   Training: {len(X_train)} samples")
print(f"   Testing: {len(X_test)} samples")

# Scale features
print("\n3. Scaling Features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("   ✅ Features scaled")

# Train models
print("\n4. Training Models...")
models = {
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'KNN': KNeighborsClassifier(n_neighbors=5)
}

results = {}
for name, model in models.items():
    print(f"   Training {name}...")
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy
    print(f"   ✅ {name} Accuracy: {accuracy:.4f}")

# K-Means Clustering
print("\n5. K-Means Clustering...")
kmeans = KMeans(n_clusters=22, random_state=42, n_init=10)
kmeans.fit(X_train_scaled)
print("   ✅ K-Means completed")

# Save best model
print("\n6. Saving Best Model...")
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]
best_accuracy = results[best_model_name]

print(f"   🏆 Best Model: {best_model_name}")
print(f"   🎯 Accuracy: {best_accuracy:.4f}")

# Save model
model_path = os.path.join(model_save_path, 'crop_model.pkl')
scaler_path = os.path.join(model_save_path, 'scaler.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(best_model, f)

with open(scaler_path, 'wb') as f:
    pickle.dump(scaler, f)

print(f"   ✅ Model saved as '{model_path}'")
print(f"   ✅ Scaler saved as '{scaler_path}'")

# Test prediction
print("\n7. Testing Prediction...")
sample = np.array([[90, 42, 43, 20.88, 82.0, 6.5, 202.94]])
sample_scaled = scaler.transform(sample)
prediction = best_model.predict(sample_scaled)
print(f"   🌾 Recommended Crop: {prediction[0]}")

print("\n" + "="*60)
print("✅ MODEL BUILDING COMPLETED!")
print("="*60)