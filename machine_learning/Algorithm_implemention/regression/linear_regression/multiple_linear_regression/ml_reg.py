# run_visualization.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# import your class
from mult import MultipleLinearRegression

def main():
    # 1) Load & preprocess
    df = pd.read_csv("50_Startups.csv")
    df_enc = pd.get_dummies(df, columns=["State"], drop_first=True)
    X = df_enc.drop("Profit", axis=1).values
    y = df_enc["Profit"].values

    # 2) Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # 3) Fit model
    model = MultipleLinearRegression(X_train, y_train)
    theta = model.gradient_descent(lr=0.01, iterations=1000)

    # 4) Predict
    y_train_pred = model.predict(X_train)
    y_test_pred  = model.predict(X_test)

    # 5A) If single feature, plot X vs y with the regression line
    if X_train.shape[1] == 1:
        plt.figure(figsize=(12,5))

        # train
        plt.subplot(1,2,1)
        plt.scatter(X_train[:,0], y_train, label="Train actual", alpha=0.6)
        # sort for a clean line
        idx = X_train[:,0].argsort()
        plt.plot(X_train[idx,0], y_train_pred[idx], color="red", label="Train fit")
        plt.title("Train: X vs y")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)

        # test
        plt.subplot(1,2,2)
        plt.scatter(X_test[:,0], y_test, label="Test actual", alpha=0.6)
        idx = X_test[:,0].argsort()
        plt.plot(X_test[idx,0], y_test_pred[idx], color="green", label="Test fit")
        plt.title("Test: X vs y")
        plt.xlabel("X")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    # 5B) If multiple features, plot y_true vs y_pred
    else:
        plt.figure(figsize=(12,5))

        # train
        plt.subplot(1,2,1)
        plt.scatter(y_train, y_train_pred, alpha=0.6)
        mn, mx = y_train.min(), y_train.max()
        plt.plot([mn,mx], [mn,mx], 'r--')
        plt.title("Train: True vs Predicted")
        plt.xlabel("y_true")
        plt.ylabel("y_pred")
        plt.grid(True)

        # test
        plt.subplot(1,2,2)
        plt.scatter(y_test, y_test_pred, alpha=0.6)
        mn, mx = y_test.min(), y_test.max()
        plt.plot([mn,mx], [mn,mx], 'r--')
        plt.title("Test: True vs Predicted")
        plt.xlabel("y_true")
        plt.ylabel("y_pred")
        plt.grid(True)

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()