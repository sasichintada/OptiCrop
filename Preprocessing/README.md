\# 🔧 OptiCrop – Data Preprocessing



This folder contains all preprocessing operations performed before training machine learning models for crop recommendation. These steps ensure that the data is clean, consistent, and optimized for predictive modeling.



\---



\## 📁 Folder Structure



```text

Preprocessing/

├── preprocessing.py

├── processed/

│   ├── processed\_crop\_data.csv

│   ├── scaler.pkl

│   ├── label\_encoder.pkl

│   ├── X\_train.npy

│   ├── X\_test.npy

│   ├── y\_train.npy

│   └── y\_test.npy

└── README.md

```



\---



\## 🎯 Objectives



\* Clean and prepare the dataset.

\* Handle outliers.

\* Standardize feature values.

\* Encode categorical labels.

\* Create train-test splits.

\* Save reusable preprocessing artifacts.



\---



\## 📊 Dataset Overview



| Metric         | Value    |

| -------------- | -------- |

| Total Samples  | 2,200    |

| Features       | 7        |

| Target Classes | 22       |

| Missing Values | 0        |

| Dataset Type   | Balanced |



\---



\## 🔍 Preprocessing Pipeline



\### 1. Data Loading



The crop recommendation dataset is loaded using Pandas.



```python

df = pd.read\_csv('../Dataset/Crop\_recommendation.csv')

```



\---



\### 2. Missing Value Analysis



All columns are checked for null values.



```python

df.isnull().sum()

```



Result:



✅ No missing values detected.



\---



\### 3. Outlier Detection and Handling



Outliers are identified using the Interquartile Range (IQR) technique.



```python

Q1 = df\[col].quantile(0.25)

Q3 = df\[col].quantile(0.75)

IQR = Q3 - Q1

```



Benefits:



\* Reduces noise

\* Improves model stability

\* Prevents bias from extreme values



\---



\### 4. Feature Scaling



Standardization is performed using StandardScaler.



```python

from sklearn.preprocessing import StandardScaler

```



Advantages:



\* Mean centered at 0

\* Standard deviation of 1

\* Faster model convergence



\---



\### 5. Label Encoding



Crop names are converted into numerical labels.



```python

from sklearn.preprocessing import LabelEncoder

```



This enables machine learning algorithms to process categorical targets efficiently.



\---



\### 6. Train-Test Split



Dataset division:



```python

train\_test\_split(

&#x20;   X,

&#x20;   y,

&#x20;   test\_size=0.20,

&#x20;   random\_state=42,

&#x20;   stratify=y

)

```



| Dataset      | Samples | Percentage |

| ------------ | ------- | ---------- |

| Training Set | 1,760   | 80%        |

| Testing Set  | 440     | 20%        |



\---



\## 📁 Generated Files



| File                    | Purpose                 |

| ----------------------- | ----------------------- |

| processed\_crop\_data.csv | Final processed dataset |

| scaler.pkl              | Saved StandardScaler    |

| label\_encoder.pkl       | Saved LabelEncoder      |

| X\_train.npy             | Training features       |

| X\_test.npy              | Testing features        |

| y\_train.npy             | Training labels         |

| y\_test.npy              | Testing labels          |



\---



\## 📈 Benefits of Preprocessing



\### Feature Scaling



\* Improves algorithm performance

\* Eliminates scale bias



\### Label Encoding



\* Converts categorical values into machine-readable format



\### Data Splitting



\* Enables unbiased model evaluation



\### Outlier Handling



\* Improves robustness and prediction accuracy



\---



\## 🛠 Technologies Used



\* Python

\* Pandas

\* NumPy

\* Scikit-learn



\---



\## 🚀 Running the Preprocessing Pipeline



```bash

cd Preprocessing

python preprocessing.py

```



All processed datasets and preprocessing objects will be stored inside the `processed/` directory.



\---



\## 📊 Output Summary



| Metric           | Value |

| ---------------- | ----- |

| Total Samples    | 2,200 |

| Training Samples | 1,760 |

| Testing Samples  | 440   |

| Features         | 7     |

| Crop Classes     | 22    |



\---



\## 📌 Conclusion



The preprocessing pipeline transforms raw agricultural data into a machine-learning-ready format by handling data quality issues, scaling features, encoding labels, and creating reproducible datasets for training and evaluation.



\---



\### 🌾 Part of OptiCrop – Smart Agricultural Production Optimization Engine



