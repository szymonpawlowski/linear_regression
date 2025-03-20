import numpy as np
from src import LinearRegressionModel, mean_squared_error

# RANDOM DATA GENERATION
N = int(input("Set number of points (N): "))
np.random.seed(50)
X = 2 * np.random.rand(N, 1).reshape(-1, 1)
y = 3 * X + 5 + np.random.randn(N, 1).ravel()

# MODEL
learning_rate = float(input("Set learning rate (default = 0.001): "))
epochs = int(input("Set number of epochs (default = 1000): "))
model = LinearRegressionModel(learning_rate = 0.001, epochs = 1000)
model.fit(X, y)

# PREDICTIONS
y_pred = model.predict(X)

# MSE ERROR
mse = mean_squared_error(y, y_pred)
print(f"MSE error: {mse:.6f}")
