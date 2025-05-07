import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from app.data_ingestion import load_data

def compare_models():
    data = load_data()
    X = data[["year", "gdp", "population"]]
    y = data["sales"]

    # Train models
    rf = RandomForestRegressor(n_estimators=100, random_state=42)
    lr = LinearRegression()
    baseline_pred = [y.mean()] * len(y)  # Baseline: mean sales

    rf.fit(X, y)
    lr.fit(X, y)

    # Predictions
    rf_pred = rf.predict(X)
    lr_pred = lr.predict(X)

    # Metrics
    rf_mse = mean_squared_error(y, rf_pred)
    lr_mse = mean_squared_error(y, lr_pred)
    baseline_mse = mean_squared_error(y, baseline_pred)

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.bar(["Random Forest", "Linear Regression", "Baseline"], [rf_mse, lr_mse, baseline_mse])
    plt.title("Model Comparison: Mean Squared Error")
    plt.ylabel("MSE")
    plt.savefig("model_comparison.png")
    plt.close()

if __name__ == "__main__":
    compare_models()