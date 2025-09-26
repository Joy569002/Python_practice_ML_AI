import numpy as np
from collections import  Counter


def euclidean_distance(x, y):
    return np.sqrt(np.sum(np.power(x-y,2)))


class KNN:
    #initializing values:
    def __init__(self,k=3):
        self.X = None
        self.y = None
        self.k = k
    #store X(features) and Y(output) data
    def fit(self,X,Y):
        self.X=X
        self.y=Y

    def predict(self,x):
        #saving euclidian distance as lists in distlist
        distlist=[euclidean_distance(x, X_train) for X_train in self.X]
        for i in distlist:
            print(i)

        #sorting distlist
        #argsort sort the indices
        #
        k_indices=np.argsort(distlist)[:self.k]
        for i in k_indices:
            print(i)
        k_nearest_labels=[self.y[i] for i in k_indices]
        for i in k_nearest_labels:
            print(i)
        most_common=Counter(k_nearest_labels).most_common()
        return most_common[0][0]
