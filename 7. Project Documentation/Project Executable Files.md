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
OptiCrop/5. Project_Development_Phase/Application/app.py
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
python 5. Project_Development_Phase/Application/app.py
```

---

## 3. app.ipynb (Jupyter Notebook)

### Location

```text
OptiCrop/5. Project_Development_Phase/Application/app.ipynb
```

### Purpose

Jupyter Notebook version of the Flask application.

### Functionality

* Interactive Flask app development.
* Step-by-step code execution.
* Visual debugging and testing.

### Execution

```bash
jupyter notebook 5. Project_Development_Phase/Application/app.ipynb
```

---

## 4. model_training.ipynb (Jupyter Notebook)

### Location

```text
OptiCrop/5. Project_Development_Phase/Application/model_training.ipynb
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
jupyter notebook 5. Project_Development_Phase/Application/model_training.ipynb
```

---

## 5. preprocessing.ipynb (Jupyter Notebook)

### Location

```text
OptiCrop/5. Project_Development_Phase/Preprocessing/preprocessing.ipynb
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
jupyter notebook 5. Project_Development_Phase/Preprocessing/preprocessing.ipynb
```

---

## 6. eda.ipynb (Jupyter Notebook)

### Location

```text
OptiCrop/7. Project Documentation/Data_Analysis/eda.ipynb
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
jupyter notebook 7. Project Documentation/Data_Analysis/eda.ipynb
```

---

## 7. evaluate.ipynb (Jupyter Notebook)

### Location

```text
OptiCrop/5. Project_Development_Phase/Model/evaluate.ipynb
```

### Purpose

Evaluates model performance.

### Functionality

* Calculates accuracy metrics.
* Generates classification report.
* Creates confusion matrix.
* Performs cross-validation.
* Saves evaluation results.

### Execution

```bash
jupyter notebook 5. Project_Development_Phase/Model/evaluate.ipynb
```

---

# 📂 Supporting Files

| File                    | Location                                                         | Purpose                     |
| ----------------------- | ---------------------------------------------------------------- | --------------------------- |
| Crop_recommendation.csv | `OptiCrop/Dataset/Crop_recommendation.csv`                       | Agricultural dataset        |
| requirements.txt        | `OptiCrop/requirements.txt`                                      | Python package dependencies |
| crop_model.pkl          | `OptiCrop/5. Project_Development_Phase/Model/models/`            | Trained ML model            |
| scaler.pkl              | `OptiCrop/5. Project_Development_Phase/Model/models/`            | Feature scaling object      |
| label_encoder.pkl       | `OptiCrop/5. Project_Development_Phase/Preprocessing/processed/` | Label encoding object       |
| processed_crop_data.csv | `OptiCrop/5. Project_Development_Phase/Preprocessing/processed/` | Processed dataset           |
| accuracy.txt            | `OptiCrop/5. Project_Development_Phase/Model/results/`           | Model performance results   |
| Procfile                | `OptiCrop/Procfile`                                              | Render deployment file      |

---

# 🔄 Execution Workflow

```text
Dataset Collection
        │
        ▼
preprocessing.ipynb
        │
        ▼
Processed Dataset
        │
        ▼
model_training.ipynb
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
* Jupyter Notebook
* Visual Studio Code / PyCharm

---

# 📦 Installation Commands

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Jupyter (if not installed)

```bash
pip install jupyter
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

✅ Jupyter Notebooks with interactive outputs

---

# 🚀 Benefits of Modular Execution

* Easy maintenance
* Independent module testing
* Faster debugging
* Better scalability
* Reusable code structure
* Interactive analysis with Jupyter Notebooks

---

# Conclusion

The OptiCrop project uses a collection of executable scripts and application files that work together to perform agricultural data analysis, machine learning-based crop prediction, and web application deployment. These executable components form the backbone of the system and enable efficient, accurate, and scalable crop recommendation services.

---

### 🌾 OptiCrop – Smart Agricultural Production Optimization Engine

**Executable Components Powering Intelligent Agricultural Recommendations** 🚜💻📊🤖🌱
