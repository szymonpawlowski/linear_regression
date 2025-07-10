from src.data.input_handler import get_data, get_learning_parameters
from src.model.regression import get_model
from src.model.utils import mean_squared_error, plot_regression
import matplotlib.pyplot as plt
plt.ion()


def main():
    X, y_true = get_data()

    learning_rate, epochs = get_learning_parameters()

    model = get_model(X, learning_rate=learning_rate, epochs=epochs)

    def on_epoch(epoch, model):
        y_pred = model.predict(X)
        plot_regression(X, y_true, epoch, y_pred)

    model.fit(X, y_true, on_epoch=on_epoch)

    y_pred = model.predict(X)
    mse = mean_squared_error(y_true, y_pred)

    print(8*"="+" Training complete "+"="*8)
    print(f"Mean Squared Error = {mse}")


if __name__ == '__main__':
    main()
