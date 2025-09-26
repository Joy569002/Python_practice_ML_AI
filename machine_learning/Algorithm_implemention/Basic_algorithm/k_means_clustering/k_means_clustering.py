import random
import numpy as np

class KMeansCluster:
    def __init__(self, k=2, max_iter=1000):
        self.k = k
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, X):
        random_index = random.sample(range(0, X.shape[0]), self.k)
        self.centroids = X[random_index]

        for i in range(self.max_iter):
            cluster_group = self.assign_cluster(X)
            old_centroids = self.centroids.copy()
            self.centroids = self.move_centroids(X, cluster_group)

            if np.allclose(old_centroids, self.centroids):
                break

        return cluster_group

    def assign_cluster(self, X):
        cluster_group = []
        for row in X:
            distances = [np.linalg.norm(row - centroid) for centroid in self.centroids]
            cluster_group.append(np.argmin(distances))
        return np.array(cluster_group)

    def move_centroids(self, X, cluster_group):
        new_centroids = []
        cluster_types = np.unique(cluster_group)
        for cluster_id in cluster_types:
            new_centroids.append(X[cluster_group == cluster_id].mean(axis=0))
        return np.array(new_centroids)