import numpy as np
from machine_learning.Algorithm_implemention.regression.linear_regression.multiple_linear_regression.mult import MultipleLinearRegression

class PolynomialRegression:
    def __init__(self, degree=2, lr=0.01, iterations=1000):
        self.degree     = degree
        self.lr         = lr
        self.iterations = iterations
        self.model      = None

    def _poly_features(self, X):
        X = np.array(X, dtype=float)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        # build [x, x^2, ..., x^d]
        features = [X ** d for d in range(1, self.degree + 1)]
        return np.hstack(features)

    def fit(self, X, y):
        X_poly = self._poly_features(X)
        self.model = MultipleLinearRegression(X_poly, y)
        self.model.gradient_descent(lr=self.lr, iterations=self.iterations)

    def predict(self, X):
        X_poly = self._poly_features(X)
        return self.model.predict(X_poly)