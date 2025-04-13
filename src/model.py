import numpy as np
import random


class SimpleLinearRegression:
    def __init__(self, learning_rate = 0.01, epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = random.uniform(-1, 1)
        self.bias = random.uniform(-1, 1)

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

    def predict(self, X):
        return [self.weights * x + self.bias for x in X]

    def mse(self, y_true, y_pred):
        return sum((yt - yp)**2 for yt, yp in zip(y_true, y_pred)) / len(y)


class AdvancedLinearRegression:
    def __init__(self, learning_rate = 0.01, epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y_true):
        X = np.array(X)
        y_true = np.array(y_true)
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            y_pred = np.dot(X, self.weights) + self.bias
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y_true))
            db = (1 / n_samples) * np.sum(y_pred - y_true)
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        X = np.array(X)
        return np.dot(X, self.weights) + self.bias

    def mse(self, y_true, y_pred):
        return np.mean((np.array(y_pred) - np.array(y_true))**2)


def get_model(X, learning_rate = 0.01, epochs = 1000):
    if isinstance(X[0], list) or isinstance(X[0], tuple):
        return AdvancedLinearRegression(learning_rate, epochs)
    return SimpleLinearRegression(learning_rate, epochs)
