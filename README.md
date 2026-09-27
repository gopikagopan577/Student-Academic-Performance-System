# Student Academic Performance Prediction System

## Overview

The Student Academic Performance Prediction System is a machine
learning application that predicts a student's final academic grade
using academic and behavioral factors.

This project uses a **regression** model to predict the **final_grade** (target variable).

The predicted grade is also used to determine the result:

- Predicted grade >= 40 → PASS
- Predicted grade < 40 → FAIL

The project includes MLflow for experiment tracking, FastAPI for the
backend, Streamlit for the frontend, and Docker for deployment.

---

## 1. Problem Statement

The objective of this project is to predict a student's final academic
grade based on:

- Age
- Study hours
- Assignment completion rate
- Attendance percentage
- Motivation level
- Stress level
- Sleep hours

Predicting the final grade can help estimate student academic
performance and identify students who may need additional academic
support.

Since **final_grade** is a continuous numerical value, the project uses
**regression**.

**PASS/FAIL** is derived from the predicted grade and does not use a
separate classification model.

---

## 2. Dataset

The project uses a synthetic student performance dataset .

### Dataset Details

- Records: 5,000
- Total columns: 8
- Input features: 7
- Target variable: **final_grade**

### Features

| Feature | Description |
|---|---|
| ***age*** | Student age |
| ***study_hours*** | Hours spent studying |
| ***assignment_completion_rate*** | Assignment completion percentage |
| ***attendance_percentage*** | Attendance percentage |
| ***motivation_level*** | Motivation level |
| ***stress_level*** | Stress level |
| ***sleep_hours*** | Average sleep hours |
| ***final_grade*** | Final academic grade |

### Dataset Files


Data/
├── Raw_data.csv
└── Processed_data.csv
---

## 3. Project Features

- Final academic grade prediction
- Regression-based machine learning
- Comparison of multiple regression models
- RMSE-based model evaluation
- MLflow experiment tracking
- FastAPI prediction API
- Streamlit user interface
- PASS/FAIL result from predicted grade
- Docker containerization
- Docker Compose deployment

---

## 4. MLflow

MLflow is used to track and compare the machine learning experiments.

The following are logged:

- Model parameters
- RMSE metrics
- Experiment runs
- Trained models

| **Model**             |  **RMSE** |
| ----------------- | ----: |
| Decision Tree     | 10.18 |
| Random Forest     |  9.65 |
| Gradient Boosting |  9.35 |

The Gradient Boosting Regressor was selected as the final model based
on the lowest RMSE among the tested models.

***The trained model is saved as:***

- models/model.pkl

### Run MLflow

- mlflow server --backend-store-uri "sqlite:///mlflow.db" --host 127.0.0.1 --port 5003 --workers 1

**Open:**

`http://127.0.0.1:5003`

---
## 5. FastAPI

FastAPI is used as the backend for the prediction system.

### Endpoints

**GET /**

Checks whether the API is running.

**POST /predict**

Accepts student details and returns the predicted final grade and
PASS/FAIL result.

- *Request Example*
{
  "student_id": "ST001",
  "student_name": "Student 1",
  "age": 18,
  "study_hours": 5.5,
  "assignment_completion_rate": 85.5,
  "attendance_percentage": 90.0,
  "motivation_level": 8,
  "stress_level": 4,
  "sleep_hours": 7.5
}

- *Response Example*
{
  "student_id": "ST001",
  "student_name": "Student 1",
  "predicted_final_grade": 76.42,
  "result": "PASS"
}

---

### Run FastAPI

- python -m uvicorn backend.main:app --reload

**API:**

`http://127.0.0.1:8000`

**Swagger documentation:**

`http://127.0.0.1:8000/docs`

---

## 6. Streamlit

Streamlit is used to create the frontend of the application.

The user enters the student details and clicks:

**Predict Final Grade**

The Streamlit application sends the data to the FastAPI /predict
endpoint.

The predicted grade and PASS/FAIL result are then displayed.

### Run Streamlit

- streamlit run frontend/app.py

**Open:**

`http://localhost:8501`

---

## 7. Docker

Docker is used to containerize the application.

The project contains two services:

- FastAPI backend
- Streamlit frontend

### Docker Files

- Dockerfile.backend
- Dockerfile.frontend
- docker-compose.yml

### Build and Run

- docker compose up --build

### Stop

- docker compose down

### Ports

- FastAPI   → 8000
- Streamlit → 8501

When running with Docker, the frontend communicates with the backend
using:

`http://backend:8000`

---
## Project Structure

Student Performance System/
│
├── Data/
│   ├── Raw_data.csv
│   └── Processed_data.csv
│
├── notebook/
│   └── 01_eda.ipynb
│
├── src/
│   ├── train.py
│   ├── preprocess.py
│   ├── utils.py
│   └── requirements.txt
│
├── models/
│   └── model.pkl
│
├── mlruns/
│
├── backend/
│   ├── main.py
│   ├── schemas.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
├── README.md
└── .gitignore

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- MLflow
- Joblib
- FastAPI
- Uvicorn
- Streamlit
- Docker
- Docker Compose

---

## How to Run

### 1. Create Virtual Environment

 python -m venv venv

### 2. Activate Virtual Environment

 venv\Scripts\activate

### 3. Install Dependencies

- pip install -r src/requirements.txt

- pip install -r backend/requirements.txt

- pip install -r frontend/requirements.txt

### 4. Train the Model

 python src/train.py

### 5. Run MLflow

mlflow server --backend-store-uri "sqlite:///mlflow.db" --host 127.0.0.1 --port 5003 --workers 1

### 6. Run FastAPI

python -m uvicorn backend.main:app --reload

### 7. Run Streamlit

**Open another terminal:**

streamlit run frontend/app.py

### 8. Run with Docker

docker compose up --build
