from regression.model import SimpleLinearRegression


class Trainer:
    def __init__(self, app_instance, on_epoch_callback):
        self.app_instance = app_instance
        self.on_epoch_callback = on_epoch_callback

        self.model = SimpleLinearRegression(
            learning_rate=self.app_instance.learning_rate,
            epochs=self.app_instance.epochs
        )

    def run(self):
        try:
            self.model.fit(
                self.app_instance.X_data,
                self.app_instance.y_data,
                on_epoch=self.on_epoch_callback
            )
            return self.model.weights, self.model.bias
        except Exception as e:
            print(f"Trainer error: {e}")
            raise e
