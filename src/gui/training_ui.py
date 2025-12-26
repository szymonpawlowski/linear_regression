import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from regression.utils import mean_squared_error
from regression.trainer import Trainer


class TrainingPanel(tk.Frame):
    def __init__(self, parent, app_instance):
        super().__init__(parent)
        self.app_instance = app_instance
        self.is_training = False

        self.epoch_var = tk.StringVar(value="Epoch: 0")
        self.mse_var = tk.StringVar(value="MSE = -")
        self.weight_var = tk.StringVar(value="Weight (w) = 0.0")
        self.bias_var = tk.StringVar(value="Bias (b) = 0.0")

        self.create_widgets()
        self.plot_initial_data()

    def create_widgets(self):
        self.main_paned = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill=tk.BOTH, expand=True)

        # left side - plot
        self.plot_frame = tk.Frame(self.main_paned, bd=1, relief=tk.SUNKEN)
        self.main_paned.add(self.plot_frame, stretch='always')

        # right side - stats
        self.control_panel = tk.Frame(self.main_paned, width=300, padx=10, pady=10)
        self.main_paned.add(self.control_panel, sticky=tk.NSEW)

        # matplotlib config
        self.fig = Figure(figsize=(5, 4), dpi=100, tight_layout=True)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.plot_frame)
        self.toolbar.update()

        tk.Label(self.control_panel, text="").pack(pady=20)

        results_group = tk.LabelFrame(self.control_panel, text=" Live Stats ", padx=10, pady=10)
        results_group.pack(fill='x', pady=10)
        font_style = ('Consolas', 16, 'bold')

        tk.Label(results_group, textvariable=self.epoch_var, font=font_style).pack(anchor='w')
        tk.Label(results_group, textvariable=self.weight_var, font=font_style).pack(anchor='w')
        tk.Label(results_group, textvariable=self.bias_var, font=font_style).pack(anchor='w', pady=(0, 10))

        tk.Frame(results_group, height=1, bg="#bdc3c7").pack(fill='x', pady=5)

        tk.Label(results_group, textvariable=self.mse_var, font=font_style).pack(anchor='w')

        self.start_button = tk.Button(
            self.control_panel,
            text="Start Training",
            command=self.toggle_training,
            bg="#4CAF50",
            fg="white",
            font=('Arial', 10, 'bold'),
            height=2,
            cursor='hand2'
        )
        self.start_button.pack(fill='x', side=tk.BOTTOM, pady=20)

    def plot_initial_data(self):
        self.ax.clear()
        if self.app_instance.X_data and self.app_instance.y_data:
            self.ax.scatter(self.app_instance.X_data, self.app_instance.y_data, s=20, color='blue', label='Input Data')

        self.ax.set_title("Linear Regression Visualization")
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_facecolor('#f8f9fa')
        self.ax.grid(True, linestyle='--', alpha=0.6)
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.legend()
        self.canvas.draw()

    def update_plot_callback(self, epoch, w, b, y_pred):
        mse = mean_squared_error(self.app_instance.y_data, y_pred)

        self.epoch_var.set(f"Epoch: {epoch}/{self.app_instance.epochs}")
        self.mse_var.set(f"MSE: {mse:.4f}")
        self.weight_var.set(f"Weight (w): {w:.4f}")
        self.bias_var.set(f"Bias (b): {b:.4f}")

        # early stop logic
        if mse < self.app_instance.mse_stop_threshold:
            self.is_training = False
            return

        # refresh
        if epoch % self.app_instance.plot_frequency == 0 or epoch == self.app_instance.epochs:
            self.after(0, lambda: self._draw_regression_line(y_pred))

    def _draw_regression_line(self, y_pred):
        try:
            if hasattr(self, 'regression_line'):
                self.regression_line.pop(0).remove()

            self.regression_line = self.ax.plot(self.app_instance.X_data, y_pred, color='red', linewidth=2, label='Regression')
            self.canvas.draw_idle()
        except Exception:
            pass

    def toggle_training(self):
        if self.is_training:
            self.is_training = False
            return

        self.is_training = True
        self.start_button.config(text="STOP Training", bg="#f44336")

        # plot reset
        self.plot_initial_data()

        # start
        self.thread = threading.Thread(target=self.run_trainer, daemon=True)
        self.thread.start()

    def run_trainer(self):
        def internal_callback(epoch, y_pred):
            if not self.is_training:
                raise InterruptedError
            self.after(0, lambda: self.update_plot_callback(epoch, trainer_obj.model.weights, trainer_obj.model.bias, y_pred))

        try:
            trainer_obj = Trainer(self.app_instance, internal_callback)
            trainer_obj.run()

            self.after(0, lambda: self.finish_training("Training completed successfully."))

        except InterruptedError:
            self.after(0, lambda: self.finish_training("Training stopped by user."))
        except Exception as e:
            self.after(0, lambda: self.finish_training(f"Error: {str(e)}"))

    def finish_training(self, message):
        self.is_training = False
        self.start_button.config(text="Start Training", bg="#4CAF50")
        messagebox.showinfo("Trainer", message)

        if self.app_instance.save_plot_auto:
            self.save_plot()

    def save_plot(self):
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.fig.savefig(path)
