import numpy as np
from collections import Counter


def euclidean_distance(point1, point2):
    distance = np.sqrt(np.sum((point1 - point2) ** 2))
    return distance


class KNN:
    def __init__(self, k):
        self.X_train = None
        self.y_train = None
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return predictions

    def _predict(self, X):
        distance = [euclidean_distance(X, x_train) for x_train in self.X_train]

        #get the closest k
        k_indices = np.argsort(distance)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]

        most_common = Counter(k_nearest_labels).most_common()
        return most_common[0][0]
