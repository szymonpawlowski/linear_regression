import matplotlib.pyplot as plt
import numpy as np
import random


def mean_squared_error(y_true, y_pred):
    y_true = np.array(y_true).flatten()
    y_pred = np.array(y_pred).flatten()

    if y_true.shape != y_pred.shape:
        raise ValueError('⚠️ Error: Y values and predicted Y values must have the same shape!')

    return np.mean((y_true - y_pred) ** 2)


def validate_input(X, y_true):
    if len(X) != len(y_true):
        raise ValueError("⚠️ Error: Number of X and Y samples must match!")


def load_data_file(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        if len(lines) < 2:
            raise ValueError("⚠️ Error: The file must contain at least 2 lines (X and Y values)!")

        X = [float(x) for x in lines[0].replace(",", " ").split()]
        y_true = [float(y) for y in lines[1].replace(",", " ").split()]

        if len(X) != len(y_true):
            raise ValueError("⚠️ Error: Number of X and Y values must be the same!")

        return X, y_true
    except FileNotFoundError:
        print("⚠️ Error: File not found.")
        return None, None

    except Exception as e:
        print(f"⚠️ Error: {e}")
        return None, None


def generate_random_data(data):
    X = [random.uniform(data[3], data[4]) for _ in range(data[2])]
    weight = random.uniform(data[5], data[6])
    bias = random.uniform(data[7], data[8])
    y_true = [weight * x + bias + random.uniform(-0.1, 0.1) for x in X]
    return X, y_true


def plot_regression(X, y_true, epoch, y_pred):
    plt.clf()
    plt.title(f"Epoch {epoch}")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.scatter(X, y_true, color='blue', label='True values')

    if isinstance(X[0], (list, tuple, np.ndarray)):
        X_plot = np.array(X)[:, 0]
    else:
        X_plot = X

    plt.plot(X_plot, y_pred, color='red', label='Predicted values')

    epoch_mse = mean_squared_error(y_true, y_pred)

    plt.text(0.05, 0.9, f"MSE = {epoch_mse:.4f}", transform=plt.gca().transAxes,
             verticalalignment='top', fontsize=10)
    plt.legend()
    plt.pause(0.1)
