import numpy as np


def mean_squared_error(y_true, y_pred):
    y_true = np.asarray(y_true).flatten()
    y_pred = np.asarray(y_pred).flatten()

    if y_true.shape != y_pred.shape:
        raise ValueError('⚠️ Error: Y values and predicted Y values must have the same shape!')

    return np.mean((y_true - y_pred) ** 2)
