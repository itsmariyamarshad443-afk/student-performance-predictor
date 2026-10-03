## 🎓 Student Performance Predictor
An end-to-end Machine Learning application that predicts a student's final grade using student academic and personal information.

The project uses a **Random Forest Regression model** and provides an interactive web interface using **Streamlit**.

---

## 🚀 Demo

### 🎥 Project Demo

https://github.com/user-attachments/assets/46a7ff30-683e-48ac-93c1-31462f41b828



## 📸 Application Preview

<img width="1920" height="1080" alt="Screenshot (1305)" src="https://github.com/user-attachments/assets/5d8ad318-5eda-4c7f-87f2-9e7fdcf40bd4" />
<img width="1920" height="1080" alt="Screenshot (1306)" src="https://github.com/user-attachments/assets/5f486ea3-2666-4f68-b506-9709ce022782" />
<img width="1920" height="1080" alt="Screenshot (1307)" src="https://github.com/user-attachments/assets/97f5fd25-4934-41f8-be10-13036ce6b93b" />





## 📌 Project Overview

The Student Performance Predictor is a Machine Learning project designed to estimate a student's final academic grade based on information available during the academic year.

The application allows users to enter student information and receive a predicted final grade through an easy-to-use Streamlit interface.

---

## 🎯 Features

* Predicts a student's final grade
* Interactive Streamlit interface
* Random Forest Regression model
* Numerical and categorical feature handling
* One-Hot Encoding
* Train/Test data splitting
* Model evaluation using MAE and R²
* Saved trained model using Joblib

---

## 🧠 Machine Learning Workflow

```text
Student Dataset
       ↓
Data Loading
       ↓
Feature Selection
       ↓
Train/Test Split
       ↓
Data Preprocessing
       ↓
Random Forest Regression
       ↓
Model Evaluation
       ↓
Saved Model
       ↓
Streamlit Application
       ↓
Predicted Final Grade
```

---

## 📊 Dataset

This project uses the **Student Performance Dataset** from the UCI Machine Learning Repository.

**Dataset:** Student Performance

**Source:** UCI Machine Learning Repository

**Dataset Link:**
https://archive.ics.uci.edu/dataset/320/student+performance

The dataset contains information about students, including academic, demographic, and social features.

The project uses the `student-mat.csv` dataset.

### Target Variable

```text
G3
```

`G3` represents the student's final grade.

### Input Features

The model uses:

* Age
* Study Time
* Past Failures
* Absences
* First Period Grade (G1)
* Second Period Grade (G2)
* Sex
* School
* Internet Access

---

## 🤖 Machine Learning Model

### Random Forest Regressor

The project uses a **Random Forest Regressor** to predict the student's final grade.

Random Forest combines multiple decision trees to produce a numerical prediction.

### Problem Type

**Supervised Learning — Regression**

The model predicts a numerical value representing the student's final grade.

---

## 📈 Model Evaluation

The model is evaluated using:

### Mean Absolute Error (MAE)

Measures the average difference between the actual and predicted grades.

### R² Score

Measures how well the model explains the variation in the final grades.

---

## 🛠️ Technology Stack

| Technology    | Purpose                 |
| ------------- | ----------------------- |
| Python        | Programming Language    |
| Pandas        | Data Processing         |
| NumPy         | Numerical Operations    |
| Scikit-learn  | Machine Learning        |
| Random Forest | Regression Model        |
| Joblib        | Model Saving            |
| Streamlit     | Web Application         |
| Git           | Version Control         |
| GitHub        | Project Hosting         |
| VS Code       | Development Environment |



## 🔮 Future Improvements

* Hyperparameter tuning
* Additional Machine Learning models
* Cross-validation
* Feature importance visualization
* Improved user interface
* Cloud deployment
* Explainable AI features

---

## ⚠️ Disclaimer

This project is created for educational and demonstration purposes. The predictions should not be used as the sole basis for decisions about a student's academic future.

---

## 👩‍💻 Author

**Maryam Arshad**

Software Engineering Student
Machine Learning | Deep Learning | Generative AI

