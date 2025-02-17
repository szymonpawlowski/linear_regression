import numpy as np
import matplotlib.pyplot as plt
from src import LinearRegressionModel, mean_squared_error, plot_predictions

# RANDOM DATA GENERATION
np.random.seed(50)
X = 2 * np.random.rand(100, 1)
y = 3 * X + 5 + np.random.randn(100, 1)
y = y.ravel()

# MODEL
model = LinearRegressionModel(learning_rate=0.01, iterations=1000)
model.fit(X, y)

# PREDICTIONS
y_pred = model.predict(X)

# MSE ERROR
mse = mean_squared_error(y, y_pred)
print(f"Błąd MSE: {mse:.4f}")

# PLOT
plot_predictions(X, y, y_pred)
