import numpy as np
import random

class SimpleLinearRegression:
    def __init__(self, learning_rate = 0.01, epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = random.uniform(-1, 1)
        self.bias = random.uniform(-1, 1)
        
    def predict(self, X):
        return [self.weights * x + self.bias for x in X]
    
    def fit(self, X, y_true, on_epoch = None):
        n = len(X)
        for epoch in range(self.epochs):
            y_pred = self.predict(X)
            dw = (-2 / n) * sum((y_true[i] - y_pred[i]) * X[i] for i in range(n))
            db = (-2 / n) * sum((y_true[i] - y_pred[i]) for i in range(n))
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db
            if on_epoch:
                on_epoch(epoch, self.predict(X))

    def mse(self, y_true, y_pred):
        return sum((yt - yp)**2 for yt, yp in zip(y_true, y_pred)) / len(y)
