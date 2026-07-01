
# 📊 OptiCrop – Model Results

This folder contains the evaluation outputs, visualizations, and performance metrics generated during the Machine Learning model evaluation phase of the OptiCrop project.

---

## 📁 Folder Structure

```text
Model/results/
├── accuracy.txt
├── confusion_matrix.png
├── elbow_graph.png
└── README.md
```

---

## 📄 Files Description

| File                   | Description                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| `accuracy.txt`         | Contains model evaluation metrics such as accuracy, precision, recall, F1-score, and classification reports |
| `confusion_matrix.png` | Visualization of actual vs predicted crop classes                                                           |
| `elbow_graph.png`      | K-Means clustering elbow method visualization                                                               |
| `README.md`            | Documentation for the results folder                                                                        |

---

## 📈 Model Performance Summary

The Random Forest classifier achieved the highest performance among all evaluated algorithms and was selected as the final prediction model.

| Metric     | Value         |
| ---------- | ------------- |
| Best Model | Random Forest |
| Accuracy   | 99.86%        |
| Precision  | 99.85%        |
| Recall     | 99.85%        |
| F1-Score   | 99.85%        |

---

## 🌾 Evaluated Algorithms

| Algorithm                 | Accuracy |
| ------------------------- | -------- |
| Random Forest             | 99.86% ✅ |
| Logistic Regression       | 96.36%   |
| K-Nearest Neighbors (KNN) | 95.68%   |

---

## 📊 Confusion Matrix Analysis

The confusion matrix provides a detailed comparison between actual crop labels and model predictions.

### Purpose

* Evaluate classification performance.
* Identify correctly classified crops.
* Detect possible misclassifications.
* Assess model reliability.

### Interpretation

* Diagonal values represent correct predictions.
* Off-diagonal values represent classification errors.
* Higher concentration along the diagonal indicates better model performance.

---

## 📉 Elbow Method Analysis

The elbow graph is generated using K-Means clustering to determine the optimal number of clusters within the dataset.

### Purpose

* Analyze crop groupings.
* Understand dataset structure.
* Support exploratory data analysis.

### Interpretation

* The elbow point indicates the most suitable number of clusters.
* Helps visualize natural groupings within agricultural data.

---

## 🔍 Key Observations

### Model Strengths

* High prediction accuracy.
* Strong generalization capability.
* Robust handling of multiple agricultural features.
* Effective classification across all crop categories.

### Important Prediction Factors

The model considers:

* Nitrogen (N)
* Phosphorous (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

These features collectively influence crop suitability predictions.

---

## 🚀 Regenerating Results

Run the model evaluation script to generate updated results:

```bash
cd Model
python evaluate.py
```

Generated outputs will be stored in the `results/` directory.

---

## 📊 Why Random Forest?

Random Forest was selected because it offers:

* High prediction accuracy
* Reduced overfitting through ensemble learning
* Strong performance on structured agricultural datasets
* Reliable feature importance estimation

---

## 🎯 Outcome

The evaluation results demonstrate that OptiCrop can accurately analyze agricultural parameters and provide reliable crop recommendations, making it a strong decision-support tool for smart farming applications.

---

### 🌾 OptiCrop – Smart Agricultural Production Optimization Engine

Using Machine Learning to enable intelligent, data-driven agricultural decision-making.
