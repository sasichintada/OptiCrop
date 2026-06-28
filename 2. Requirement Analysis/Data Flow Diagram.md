# 🔄 Data Flow Diagram (DFD)

## Project Title

🌾 **OptiCrop – Smart Agricultural Production Optimization Engine**

---

# Introduction

A Data Flow Diagram (DFD) represents how data moves through the OptiCrop system. It illustrates the interaction between users, the web application, machine learning model, dataset, and prediction results.

The DFD helps visualize the flow of agricultural data from user input to crop recommendation output.

---

# 🎯 Purpose of DFD

* Understand system functionality
* Visualize data movement
* Identify system components
* Define inputs and outputs
* Support system design and implementation

---

# 📋 Main Components

## 👨‍🌾 External Entity

### Farmer / User

Provides agricultural and environmental parameters to the system and receives crop recommendations.

---

## ⚙️ Process

### Crop Recommendation Engine

Processes user inputs using Machine Learning algorithms and generates suitable crop recommendations.

---

## 🗄️ Data Store

### Agricultural Dataset

Stores historical crop and environmental data used for training and prediction.

---

## 📊 Output

### Recommendation Results

Displays:

* Recommended Crop
* Confidence Score
* Top Crop Matches
* Prediction Insights

---

# 📥 Input Parameters

The user provides:

🌱 Nitrogen (N)

🌱 Phosphorous (P)

🌱 Potassium (K)

🌡 Temperature

💧 Humidity

⚗ Soil pH

☔ Rainfall

---

# 📤 Output Information

The system provides:

✅ Best Crop Recommendation

✅ Prediction Confidence

✅ Top 3 Crop Matches

✅ Agricultural Insights

---

# Level 0 DFD (Context Diagram)

```text
+------------------+
|     Farmer       |
+------------------+
         |
         | Soil & Environmental Data
         v
+----------------------------------+
|            OptiCrop              |
| Crop Recommendation System       |
+----------------------------------+
         |
         | Recommended Crop
         | Confidence Score
         v
+------------------+
|     Farmer       |
+------------------+
```

---

# Level 1 DFD

```text
+------------------+
|     Farmer       |
+------------------+
         |
         | Input Parameters
         v

+--------------------------+
|  Input Validation Module |
+--------------------------+
         |
         v

+--------------------------+
| Data Preprocessing Layer |
+--------------------------+
         |
         v

+--------------------------+
| Machine Learning Model   |
| (Random Forest / KNN /   |
| Logistic Regression)     |
+--------------------------+
         |
         ^
         |
+--------------------------+
| Agricultural Dataset     |
+--------------------------+

         |
         v

+--------------------------+
| Prediction Engine        |
+--------------------------+
         |
         v

+--------------------------+
| Recommendation Results   |
+--------------------------+
         |
         v

+------------------+
|     Farmer       |
+------------------+
```

---

# Data Flow Description

| Step | Data Flow                            |
| ---- | ------------------------------------ |
| 1    | Farmer enters soil and climate data  |
| 2    | Input Validation checks values       |
| 3    | Data Preprocessing prepares features |
| 4    | ML Model analyzes conditions         |
| 5    | Dataset supports prediction process  |
| 6    | Prediction Engine generates results  |
| 7    | Recommended crop is displayed        |

---

# DFD Workflow

```text
User Input
     │
     ▼
Input Validation
     │
     ▼
Data Preprocessing
     │
     ▼
Machine Learning Model
     │
     ▼
Crop Prediction
     │
     ▼
Result Generation
     │
     ▼
Recommendation Output
```

---

# Benefits of the DFD

📊 Clear understanding of system flow

⚡ Simplifies application design

🔍 Identifies data movement

🌾 Improves agricultural decision support

🤖 Supports machine learning integration

---

# Conclusion

The Data Flow Diagram demonstrates how agricultural data moves through the OptiCrop system. From user input to machine learning prediction and recommendation output, the DFD provides a clear representation of the system's functionality and workflow.

---

### 🌾 OptiCrop – Smart Agricultural Production Optimization Engine
