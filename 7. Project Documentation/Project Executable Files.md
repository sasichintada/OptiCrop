# 📦 Project Executable Files

## Project Title

🌾 **OptiCrop – Smart Agricultural Production Optimization Engine**

---

# Introduction

The OptiCrop project consists of several executable files and scripts that work together to perform data analysis, preprocessing, machine learning model training, and crop recommendation through a web application. These files are responsible for executing different stages of the project workflow.

---

# 🎯 Purpose of Executable Files

The executable files are used to:

* Load and process agricultural data.
* Perform data preprocessing.
* Train and evaluate machine learning models.
* Generate visualizations and analysis reports.
* Run the Flask web application.
* Provide crop recommendations to users.

---

# 📁 Main Executable Files

## 1. run.py

### Location

```text
OptiCrop/run.py
```

### Purpose

Acts as the main entry point of the OptiCrop application.

### Functionality

* Launches the Flask server.
* Loads required configurations.
* Starts the web application.

### Execution

```bash
python run.py
```

---

## 2. app.py

### Location

```text
OptiCrop/5.Project_Development_Phase/Application/app.py
```

### Purpose

Core Flask application file.

### Functionality

* Handles user requests.
* Receives agricultural parameters.
* Communicates with the machine learning model.
* Displays crop recommendation results.

### Execution

```bash
python 5.Project_Development_Phase/Application/app.py
```

---

## 3. model_training.py

### Location

```text
OptiCrop/5.Project_Development_Phase/Application/model_training.py
```

### Purpose

Trains machine learning models.

### Functionality

* Loads processed dataset.
* Trains Random Forest.
* Trains Logistic Regression.
* Trains KNN.
* Performs evaluation.
* Saves trained models.

### Execution

```bash
python 5.Project_Development_Phase/Application/model_training.py
```

---

## 4. preprocessing.py

### Location

```text
OptiCrop/5.Project_Development_Phase/Preprocessing/preprocessing.py
```

### Purpose

Performs data preprocessing operations.

### Functionality

* Reads dataset.
* Handles missing values.
* Detects outliers.
* Performs feature scaling.
* Encodes crop labels.
* Splits training and testing data.

### Execution

```bash
python 5.Project_Development_Phase/Preprocessing/preprocessing.py
```

---

## 5. eda.py

### Location

```text
OptiCrop/7.Project_Documentation/Data_Analysis/eda.py
```

### Purpose

Performs Exploratory Data Analysis.

### Functionality

* Generates statistical summaries.
* Creates visualizations.
* Produces correlation analysis.
* Saves plots for documentation.

### Execution

```bash
python 7.Project_Documentation/Data_Analysis/eda.py
```

---

## 6. generate_plots.py

### Location

```text
OptiCrop/generate_plots.py
```

### Purpose

Creates project visualization charts.

### Functionality

* Generates graphs.
* Produces analysis figures.
* Saves plots for reports.

### Execution

```bash
python generate_plots.py
```

---

# 📂 Supporting Files

| File                    | Location                                                | Purpose                     |
| ----------------------- | ------------------------------------------------------- | --------------------------- |
| Crop_recommendation.csv | `OptiCrop/Dataset/Crop_recommendation.csv`              | Agricultural dataset        |
| requirements.txt        | `OptiCrop/requirements.txt`                             | Python package dependencies |
| crop_model.pkl          | `OptiCrop/5.Project_Development_Phase/Model/models/`    | Trained ML model            |
| scaler.pkl              | `OptiCrop/5.Project_Development_Phase/Model/models/`    | Feature scaling object      |
| label_encoder.pkl       | `OptiCrop/5.Project_Development_Phase/Preprocessing/processed/` | Label encoding object |
| processed_crop_data.csv | `OptiCrop/5.Project_Development_Phase/Preprocessing/processed/` | Processed dataset |
| accuracy.txt            | `OptiCrop/5.Project_Development_Phase/Model/results/`   | Model performance results   |

---

# 🔄 Execution Workflow

```text
Dataset Collection
        │
        ▼
preprocessing.py
        │
        ▼
Processed Dataset
        │
        ▼
model_training.py
        │
        ▼
Trained Model
        │
        ▼
app.py
        │
        ▼
run.py
        │
        ▼
Web Application
```

---

# 🖥️ Software Requirements

### Operating System

* Windows
* Linux
* macOS

### Required Software

* Python 3.11+
* Flask
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Visual Studio Code / PyCharm

---

# 📦 Installation Commands

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python run.py
```

---

# 📊 Output Generated

The executable files generate:

✅ Crop recommendations

✅ Confidence scores

✅ Top 3 crop predictions

✅ Analysis plots

✅ Model evaluation reports

✅ Web application pages

---

# 🚀 Benefits of Modular Execution

* Easy maintenance
* Independent module testing
* Faster debugging
* Better scalability
* Reusable code structure

---

# Conclusion

The OptiCrop project uses a collection of executable scripts and application files that work together to perform agricultural data analysis, machine learning-based crop prediction, and web application deployment. These executable components form the backbone of the system and enable efficient, accurate, and scalable crop recommendation services.

---

### 🌾 OptiCrop – Smart Agricultural Production Optimization Engine

**Executable Components Powering Intelligent Agricultural Recommendations** 🚜💻📊🤖🌱
