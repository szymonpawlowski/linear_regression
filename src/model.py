import numpy as np
import matplotlib.pyplot as plt


class LinearRegressionModel:
    def __init__(self, learning_rate = 0.001, epochs = 1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        if X.ndim == 1:
            X = X.reshape(-1, 1)

        n_samples, n_features = X.shape

        self.weights = np.random.randn(n_features, 1) * 0.01
        self.bias = 0

        plt.ion()
        fig, ax = plt.subplots()
        ax.scatter(X.flatten(), y.flatten(), color = "blue", title = "True values")
        line, = ax.plot(X, X * self.weights + self.bias, color = "red", title = "Predicted values")

        for i in range(self.epochs):
            y_predicted = np.dot(X, self.weights).flatten() + self.bias
            
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y).reshape(-1, 1))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            if i % 50 == 0:
                line.set_ydata(X * self.weights + self.bias)
                plt.pause(0.01)

        plt.ioff()
        plt.show()
            
    def predict(self, X):
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        return np.dot(X, self.weights) + self.bias
    