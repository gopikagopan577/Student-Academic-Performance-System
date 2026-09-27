import pandas as pd
import mlflow
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

from utils import calculate_rmse, log_parameters, log_metrics, log_model, save_model

mlflow.set_experiment("Student Performance Prediction")

df = pd.read_csv("Data/Processed_data.csv")


X = df.drop(columns=["final_grade"])
y = df["final_grade"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)


# Creating the models
models = {
     "Decision Tree": DecisionTreeRegressor( max_depth=5, random_state=42),

    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),

    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
}

## store results
results = {}

# Train and evaluate each model
for name, model in models.items():

    with mlflow.start_run(run_name=name):

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)

        rmse = calculate_rmse(y_test, predictions)

        results[name] = rmse

        log_parameters(model.get_params())

        log_metrics({"RMSE": rmse})

        log_model(model, name)

        print("Model:", name)
        print("RMSE:", rmse)

## To show best model

best_model_name = min(results, key=results.get)
best_model = models[best_model_name]

print("Best Model:", best_model_name)
print("Best RMSE:", round(results[best_model_name], 2))

save_model(best_model, 'models/model.pkl')

# Model Evaluation Plots
best_predictions = best_model.predict(X_test)

# Actual vs Predicted Plot
plt.scatter(y_test, best_predictions)
plt.xlabel("Actual Final Grade")
plt.ylabel("Predicted Final Grade")
plt.title("Actual vs Predicted Final Grade")
plt.show()

# Residual Plot
residuals = y_test - best_predictions
plt.scatter(best_predictions, residuals)
plt.xlabel("Predicted Final Grade")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.axhline(y=0)
plt.show()