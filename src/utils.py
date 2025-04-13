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


def generate_random_data(
        dim = 1,
        n_samples = 100,
        x_range = (1, 10),
        noise = 1.0,
        w_range = (-10, 10),
        b_range = (-5, 5)
):
    if dim == 1:
        X = [random.uniform(*x_range) for _ in range(n_samples)]
        weights_true = random.uniform(*w_range)
        bias_true = random.uniform(*b_range)
        y_true = [weights_true * x + bias_true + random.uniform(-noise, noise) for x in X]
        return X, y_true
    else:
        X = np.random.uniform(*x_range, size = (n_samples, dim))
        weights_true = np.random.uniform(*w_range, size = dim)
        bias_true = np.random.uniform(*b_range)
        noise = np.random.uniform(-noise, noise, size = n_samples)
        y_true = np.dot(X, weights_true) + bias_true + noise
        return X.tolist(), y_true.tolist()