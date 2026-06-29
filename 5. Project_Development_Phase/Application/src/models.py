# src/models.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import pickle
import warnings
warnings.filterwarnings('ignore')

def build_models(X_train, X_test, y_train, y_test, label_encoder):
    """Build and evaluate models"""
    
    print("\n🤖 Model Building")
    print("="*60)
    
    # 1. K-Means Clustering
    print("\n📌 K-Means Clustering")
    print("Using Elbow Method to find optimal clusters")
    
    wcss = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_train)
        wcss.append(kmeans.inertia_)
    
    # Plot Elbow Graph
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), wcss, 'bo-', linewidth=2)
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
    plt.title('Elbow Method for Optimal k')
    plt.axvline(x=5, color='red', linestyle='--', label='Optimal k=5')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('elbow_graph.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Train K-Means with optimal k
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_train)
    print(f"✅ K-Means clustering completed with 5 clusters")
    
    # 2. Logistic Regression
    print("\n📌 Logistic Regression")
    lr = LogisticRegression(max_iter=1000, random_state=42, multi_class='multinomial')
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    accuracy_lr = accuracy_score(y_test, y_pred_lr)
    print(f"   Accuracy: {accuracy_lr:.4f}")
    
    # 3. Decision Tree
    print("\n📌 Decision Tree")
    dt = DecisionTreeClassifier(random_state=42, max_depth=10)
    dt.fit(X_train, y_train)
    y_pred_dt = dt.predict(X_test)
    accuracy_dt = accuracy_score(y_test, y_pred_dt)
    print(f"   Accuracy: {accuracy_dt:.4f}")
    
    # 4. Random Forest
    print("\n📌 Random Forest")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    print(f"   Accuracy: {accuracy_rf:.4f}")
    
    # 5. KNN
    print("\n📌 K-Nearest Neighbors")
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    accuracy_knn = accuracy_score(y_test, y_pred_knn)
    print(f"   Accuracy: {accuracy_knn:.4f}")
    
    # Model Comparison
    print("\n📊 Model Performance Comparison")
    print("="*60)
    print(f"Logistic Regression: {accuracy_lr:.4f}")
    print(f"Decision Tree: {accuracy_dt:.4f}")
    print(f"Random Forest: {accuracy_rf:.4f}")
    print(f"KNN: {accuracy_knn:.4f}")
    
    # Select best model
    best_model = rf
    best_accuracy = accuracy_rf
    best_name = "Random Forest"
    best_predictions = y_pred_rf
    
    # Confusion Matrix for best model
    print(f"\n🏆 Best Model: {best_name} (Accuracy: {best_accuracy:.4f})")
    print("\n📋 Classification Report:")
    print(classification_report(y_test, best_predictions, 
                               target_names=label_encoder.classes_))
    
    # Confusion Matrix Visualization
    cm = confusion_matrix(y_test, best_predictions)
    plt.figure(figsize=(12, 10))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=label_encoder.classes_,
                yticklabels=label_encoder.classes_)
    plt.title(f'Confusion Matrix - {best_name}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Save best model
    print("\n💾 Saving Best Model")
    with open('models/model.pkl', 'wb') as f:
        pickle.dump(best_model, f)
    print("✅ Model saved as model.pkl")
    
    return best_model, best_accuracy, best_predictions

if __name__ == "__main__":
    # Load preprocessed data
    df = pd.read_csv('data/Crop_recommendation.csv')
    from preprocessing import preprocess_data
    X_train, X_test, y_train, y_test, le, scaler = preprocess_data(df)
    
    # Build models
    model, accuracy, predictions = build_models(X_train, X_test, y_train, y_test, le)
