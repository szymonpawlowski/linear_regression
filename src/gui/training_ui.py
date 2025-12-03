import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import time

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from regression.utils import mean_squared_error
from regression.trainer import Trainer


class TrainingWindow(tk.Toplevel):
    def __init__(self, parent, app_instance):
        super.__init__(parent)
        self.title("Training and Visualization")
        self.app_instance = app_instance
        self.is_training = False

        if not self.app_instance.X_data or not self.app_instance.y_data:
            messagebox.showerror("Error", "No data. Load data first.")
            self.destroy()
            return

        self.geometry("800x600")

        self.epoch_var = tk.StringVar(value="Epoch: 0")
        self.mse_var = tk.StringVar(value="MSE = -")
        self.weight_var = tk.StringVar(value="Weight (w) = 0.0")
        self.bias_var = tk.StringVar(value="Bias (b) = 0.0")

        self.createWidgets()
        self.plotInitialData()

    def createWidgets(self):
        main_paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        main_paned_window.pack(fill=tk.BOTH, expand=True)

        self.plotFrame = tk.Frame(main_paned_window, bd=2, relief=tk.SUNKEN)
        main_paned_window.add(self.plotFrame, width=550)

        self.control_frame = tk.Frame(main_paned_window, width=250, padx=10, pady=10)
        main_paned_window.add(self.control_frame)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.draw()

        # Opcjonalny pasek narzędzi Matplotlib
        toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)
        toolbar.update()

        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        # --- Kontrolki (Prawy Panel) ---
        tk.Label(self.control_frame, text="Wyniki Treningu", font=('calibre', 14, 'bold')).pack(pady=10)

        tk.Label(self.control_frame, textvariable=self.epoch_var).pack(anchor='w')
        tk.Label(self.control_frame, textvariable=self.mse_var).pack(anchor='w')
        tk.Label(self.control_frame, textvariable=self.weight_var).pack(anchor='w')
        tk.Label(self.control_frame, textvariable=self.bias_var).pack(anchor='w')

        self.start_button = tk.Button(self.control_frame, text="Start Treningu", command=self.start_training, bg="#4CAF50", fg="white", height=2)
        self.start_button.pack(pady=20, fill='x')

    def plot_initial_data(self):
        self.ax.clear()
        self.ax.scatter(self.app_instance.X_data, self.app_instance.y_data, s=20, color='blue', label='Dane wejściowe')
        self.ax.set_title("Regresja Liniowa")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

    def update_plot_callback(self, epoch, w, b, y_pred):
        current_mse = mean_squared_error(self.app_instance.y_data, y_pred)

        self.epoch_var.set(f"Epoch: {epoch}/{self.app_instance.epochs}")
        self.mse_var.set(f"MSE: {current_mse:.4f}")
        self.weight_var.set(f"Weight (w): {w:.4f}")
        self.bias_var.set(f"Bias (b): {b:.4f}")

        if current_mse < self.app_instance.mse_stop_threshold:
            self.stop_training("Early Stopping: Osiągnięto minimalny błąd.")
            return

        if epoch % self.app_instance.plot_frequency == 0 or epoch == self.app_instance.epochs:
            self.after(1, lambda: self._draw_regression_line(y_pred))

    def _draw_regression_line(self, y_pred):
        try:
            if hasattr(self, 'regression_line'):
                self.regression_line.pop(0).remove()

            self.regression_line = self.ax.plot(self.app_instance.X_data, y_pred, color='red', label='Regression line')
            self.ax.legend()
            self.canvas.draw()
        except:
            pass

    def start_training(self):
        if self.is_training:
            self.stop_training("Manual stop.")
            return

        self.is_training = True
        self.start_button.config(text="STOP Training", bg="#FF0000")

        self.plot_initial_data()
        self.epoch_var.set("Epoch: START")

        self.training_thread = threading.Thread(target=self.run_trainer, daemon=True)
        self.training_thread.start()

    def stop_training(self, message="Training finished."):
        self.is_training = False
        self.start_button.config(text="Resume training", bg="#FFA500")
        messagebox.showinfo("Training status", message)

        if self.app_instance.save_plot_auto:
            self.save_plot()

    def run_trainer(self):
        from . import model # TODO: add model import

        regressor = model.SimpleLinearRegression(
            learning_rate=self.app_instance.learning_rate,
            epochs=self.app_instance.epochs
        )

        def callback(epoch, y_pred):
            if not self.is_training:
                raise InterruptedError

            self.after(1, lambda: self.update_plot_callback(epoch, regressor.weights, regressor.bias, y_pred))

        try:
            regressor.fit(self.app_instance.X_data, self.app_instance.y_data, on_epoch=callback)

            self.after(1, lambda: self.stop_training(f"Training ended after {self.app_instance.epochs} epochs."))

        except InterruptedError:
            self.after(1, lambda: self.stop_training("Training stopped by user."))
        except Exception as e:
            self.after(1, lambda: self.stop_training(f"Error occured during training: {e}"))

    def save_plot(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if filepath:
            self.fig.savefig(filepath)
            messagebox.showinfo("Saved", f"Plot saved to: {filepath}")
