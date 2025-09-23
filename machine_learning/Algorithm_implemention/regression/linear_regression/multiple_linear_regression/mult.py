import numpy as np

class MultipleLinearRegression:
    def __init__(self, X, y):
        # Ensure X is 2D NumPy array
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float)
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        # Save sample count and feature count
        self.m, self.n = X.shape

        # Feature scaling
        self.X_mean = X.mean(axis=0)
        self.X_std  = X.std(axis=0)
        self.X_std[self.X_std == 0] = 1  # prevent divide-by-zero
        X_scaled = (X - self.X_mean) / self.X_std

        # Augment with bias column
        ones = np.ones((self.m, 1))
        self.X_aug = np.hstack((ones, X_scaled))

        # Targets and parameters
        self.y     = y
        self.theta = np.random.randn(self.n + 1) * 0.01

    def compute_cost(self):
        h = self.X_aug @ self.theta
        return (1 / (2 * self.m)) * np.sum((h - self.y) ** 2)

    def gradient_descent(self, lr=0.01, iterations=1000):
        self.cost_history = []
        for i in range(iterations):
            h        = self.X_aug @ self.theta
            gradient = (1 / self.m) * (self.X_aug.T @ (h - self.y))
            self.theta -= lr * gradient
            cost = self.compute_cost()
            self.cost_history.append(cost)
            if i % 100 == 0:
                print(f"Iter {i:4d} | Cost = {cost:.4f}")
        return self.theta

    def predict(self, X_test):
        X_test = np.array(X_test, dtype=float)
        if X_test.ndim == 1:
            X_test = X_test.reshape(-1, 1)
        X_scaled = (X_test - self.X_mean) / self.X_std
        ones     = np.ones((X_scaled.shape[0], 1))
        X_aug    = np.hstack((ones, X_scaled))
        return X_aug @ self.theta

    def normal_equation(self):
        return np.linalg.pinv(self.X_aug.T @ self.X_aug) @ self.X_aug.T @ self.y