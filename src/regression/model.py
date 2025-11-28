import numpy as np


class SimpleLinearRegression:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = 0.0
        self.bias = 0.0

    def fit(self, X, y_true, on_epoch=None):
        X_list = list(X)
        y_true_list = list(y_true)
        n = len(X_list)

        if n == 0:
            return

        for epoch in range(1, self.epochs + 1):
            y_pred = self.predict(X_list)

            error_diff = [(y_true_list[i] - y_pred[i]) for i in range(n)]

            dw = (-2 / n) * sum(error_diff[i] * X_list[i] for i in range(n))
            db = (-2 / n) * sum(error_diff)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            if on_epoch:
                on_epoch(epoch, self.predict(X_list))

    def predict(self, X):
        return [self.weights * x + self.bias for x in X]