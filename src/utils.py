import joblib
import mlflow
from sklearn.metrics import mean_squared_error


# Calculating RMSE
def calculate_rmse(actual, predicted):
    rmse = mean_squared_error(actual, predicted) ** 0.5
    return rmse


# Saving the trained model
def save_model(model, file_path):
    joblib.dump(model, file_path)


# Load a saved model
def load_model(file_path):
    return joblib.load(file_path)


# Log parameters in MLflow
def log_parameters(parameters):
    for name, value in parameters.items():
        mlflow.log_param(name, value)


# Log metrics in MLflow
def log_metrics(metrics):
    for name, value in metrics.items():
        mlflow.log_metric(name, value)


# Log model in MLflow
def log_model(model, model_name):
    mlflow.sklearn.log_model(model, name = model_name)