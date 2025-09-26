from statistics import linear_regression

import  numpy as np
class LinearRegression:
    def __init__(self,lr=0.01,iterations=1000):
        self.weights=None
        self.bias=None
        self.lr=lr
        self.iteration=iterations
    def fit(self,X,y):
        n_samples,n_features=X.shape
        self.weights=np.zeros(n_features)
        self.bias=0
        for i in range(self.iteration):
            #y=mx+c
            #
            y_pred=np.dot(X,self.weights)+self.bias
            dw=(1/n_samples)*np.dot(X.T,y_pred-y)
            db=(1/n_samples)*np.sum(y_pred-y)
            self.weights=self.weights-self.lr*dw
            self.bias=self.bias-self.lr*db