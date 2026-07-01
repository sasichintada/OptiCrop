
# 🔧 OptiCrop – Data Preprocessing

This folder contains all preprocessing operations performed before training machine learning models for crop recommendation. These steps ensure that the data is clean, consistent, and optimized for predictive modeling.

---

## 📁 Folder Structure

```text
Preprocessing/
├── preprocessing.py
├── processed/
│   ├── processed_crop_data.csv
│   ├── scaler.pkl
│   ├── label_encoder.pkl
│   ├── X_train.npy
│   ├── X_test.npy
│   ├── y_train.npy
│   └── y_test.npy
└── README.md
```

---

## 🎯 Objectives

* Clean and prepare the dataset.
* Handle outliers.
* Standardize feature values.
* Encode categorical labels.
* Create train-test splits.
* Save reusable preprocessing artifacts.

---

## 📊 Dataset Overview

| Metric         | Value    |
| -------------- | -------- |
| Total Samples  | 2,200    |
| Features       | 7        |
| Target Classes | 22       |
| Missing Values | 0        |
| Dataset Type   | Balanced |

---

## 🔍 Preprocessing Pipeline

### 1. Data Loading

The crop recommendation dataset is loaded using Pandas.

```python
df = pd.read_csv('../Dataset/Crop_recommendation.csv')
```

---

### 2. Missing Value Analysis

All columns are checked for null values.

```python
df.isnull().sum()
```

Result:

✅ No missing values detected.

---

### 3. Outlier Detection and Handling

Outliers are identified using the Interquartile Range (IQR) technique.

```python
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1
```

Benefits:

* Reduces noise
* Improves model stability
* Prevents bias from extreme values

---

### 4. Feature Scaling

Standardization is performed using StandardScaler.

```python
from sklearn.preprocessing import StandardScaler
```

Advantages:

* Mean centered at 0
* Standard deviation of 1
* Faster model convergence

---

### 5. Label Encoding

Crop names are converted into numerical labels.

```python
from sklearn.preprocessing import LabelEncoder
```

This enables machine learning algorithms to process categorical targets efficiently.

---

### 6. Train-Test Split

Dataset division:

```python
train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
```

| Dataset      | Samples | Percentage |
| ------------ | ------- | ---------- |
| Training Set | 1,760   | 80%        |
| Testing Set  | 440     | 20%        |

---

## 📁 Generated Files

| File                    | Purpose                 |
| ----------------------- | ----------------------- |
| processed_crop_data.csv | Final processed dataset |
| scaler.pkl              | Saved StandardScaler    |
| label_encoder.pkl       | Saved LabelEncoder      |
| X_train.npy             | Training features       |
| X_test.npy              | Testing features        |
| y_train.npy             | Training labels         |
| y_test.npy              | Testing labels          |

---

## 📈 Benefits of Preprocessing

### Feature Scaling

* Improves algorithm performance
* Eliminates scale bias

### Label Encoding

* Converts categorical values into machine-readable format

### Data Splitting

* Enables unbiased model evaluation

### Outlier Handling

* Improves robustness and prediction accuracy

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

---

## 🚀 Running the Preprocessing Pipeline

```bash
cd Preprocessing
python preprocessing.py
```

All processed datasets and preprocessing objects will be stored inside the `processed/` directory.

---

## 📊 Output Summary

| Metric           | Value |
| ---------------- | ----- |
| Total Samples    | 2,200 |
| Training Samples | 1,760 |
| Testing Samples  | 440   |
| Features         | 7     |
| Crop Classes     | 22    |

---

## 📌 Conclusion

The preprocessing pipeline transforms raw agricultural data into a machine-learning-ready format by handling data quality issues, scaling features, encoding labels, and creating reproducible datasets for training and evaluation.

---

### 🌾 Part of OptiCrop – Smart Agricultural Production Optimization Engine
