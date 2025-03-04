import numpy as np
import matplotlib.pyplot as plt

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

def plot_predictions(X, y_true, y_pred):
    plt.scatter(X, y_true, color = "blue", label = "True values")
    plt.plot(X, y_pred, color = "red", label = "Prediction model")
    plt.legend()
    plt.show()
