import random


def get_random_data(n, xmin, xmax, wmin, wmax, bmin, bmax):
    data = []
    for _ in range(n):
        X = random.uniform(xmin, xmax)
        weight = random.uniform(wmin, wmax)
        bias = random.uniform(bmin, bmax)
        y_pred = weight * X + bias
        data.append((X, y_pred))
    return data
