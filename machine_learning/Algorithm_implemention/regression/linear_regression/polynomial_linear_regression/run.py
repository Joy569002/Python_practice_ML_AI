import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression

def main():
    # 1. Load data
    df = pd.read_csv("50_Startups.csv")
    # we only need R&D Spend vs Profit for example
    X = df[["R&D Spend"]].values
    y = df["Profit"].values

    # 2. Train polynomial regressor (degree=2)
    poly = PolynomialRegression(degree=2, lr=0.01, iterations=2000)
    poly.fit(X, y)
    preds = poly.predict(X)

    # 3. Plot fit
    sorted_idx = X[:,0].argsort()
    plt.scatter(X, y, color="blue", label="Data")
    plt.plot(X[sorted_idx], preds[sorted_idx], color="red", label="Poly Fit")
    plt.xlabel("R&D Spend")
    plt.ylabel("Profit")
    plt.title("Polynomial Regression (degree=2)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()