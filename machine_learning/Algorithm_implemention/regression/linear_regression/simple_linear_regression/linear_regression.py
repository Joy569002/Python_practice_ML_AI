import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class LinearRegression:

    def __init__(self,learning_rate=0.01,iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = iterations
        self.weights=None
        self.bias=None

    def fit(self,x,y):
        n_samples = x.shape[0]
        n_features = x.shape[1]
        self.weights=np.zeros(n_features)
        self.bias=np.zeros(1)
        for _ in range(self.num_iterations):
            y_predict=np.dot(x,self.weights)+self.bias
            dw=(1/n_samples)*np.dot(x.T,y_predict-y)
            db=(1/n_samples)*np.sum(y_predict-y)
            self.weights=self.weights-self.learning_rate*dw
            self.bias=self.bias-self.learning_rate*db

    def predict(self,x):
        y_predict=np.dot(x,self.weights)+self.bias
        return y_predict