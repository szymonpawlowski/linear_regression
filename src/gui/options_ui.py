import tkinter as tk
from tkinter import messagebox


class OptionsWindow:
    def __init__(self, parent, app_instance):
        self.app_instance = app_instance

        self.window = tk.Toplevel(parent)
        self.window.title('Model and Visualization Options')

        self.lr_var = tk.DoubleVar(value=self.app_instance.learning_rate)
        self.epochs_var = tk.IntVar(value=self.app_instance.epochs)
        self.frequency_var = tk.IntVar(value=20)
        self.save_plot_var = tk.BooleanVar(value=False)
        self.mse_threshold_var = tk.DoubleVar(value=0.0001)

        parent.update_idletasks()
        main_x = parent.winfo_x()
        main_y = parent.winfo_y()
        main_width = parent.winfo_width()
        main_height = parent.winfo_height()

        options_width = 450
        options_height = 400

        x = main_x + (main_width // 2) - (options_width // 2)
        y = main_y + (main_height // 2) - (options_height // 2)

        self.window.geometry(f"{options_width}x{options_height}+{x}+{y}")
        self.window.resizable(False, False)

        main_frame = tk.Frame(self.window, padx=15, pady=15)
        main_frame.pack(expand=True, fill='both')
        main_frame.columnconfigure(1, weight=1)

        tk.Label(main_frame, text="⚙️ Training settings", font=('calibre', 14, 'bold')).grid(row=0, columnspan=2, pady=10, sticky='w')

        tk.Label(main_frame, text="Learning Rate (α):").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        tk.Entry(main_frame, textvariable=self.lr_var).grid(row=1, column=1, sticky='we', padx=5, pady=5)

        tk.Label(main_frame, text="Number of epochs (max):").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        tk.Entry(main_frame, textvariable=self.epochs_var).grid(row=2, column=1, sticky='we', padx=5, pady=5)

        tk.Label(main_frame, text="Stop when MSE < :").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        tk.Entry(main_frame, textvariable=self.mse_threshold_var).grid(row=3, column=1, sticky='we', padx=5, pady=5)

        tk.Frame(main_frame, height=1, bg="gray").grid(row=4, columnspan=2, sticky="ew", pady=10)

        tk.Label(main_frame, text="📈 Visualization Settings", font=('calibre', 14, 'bold')).grid(row=5, columnspan=2, pady=10, sticky='w')

        tk.Label(main_frame, text="Draw every (N-epochs)").grid(row=6, column=0, sticky='w', padx=5, pady=5)
        tk.Entry(main_frame, textvariable=self.frequency_var).grid(row=6, column=1, sticky='we', padx=5, pady=5)

        tk.Checkbutton(main_frame, text="Automatically save plot after training", variable=self.save_plot_var).grid(row=7, columnspan=2, sticky='w', padx=5, pady=5)

        tk.Button(main_frame, text="Save & Close", command=self.save_options, bg="#4CAF50", fg="white", height=2).grid(row=8, columnspan=2, pady=20, sticky='we')

        self.window.transient(parent)
        self.window.grab_set()
        self.window.wait_window()

    def save_options(self):
        try:
            self.app_instance.learning_rate = self.lr_var.get()
            self.app_instance.epochs = self.epochs_var.get()

            self.app_instance.plot_frequency = self.frequency_var.get()
            self.app_instance.save_plot_auto = self.save_plot_var.get()
            self.app_instance.mse_stop_threshold = self.mse_threshold_var.get()

            messagebox.showinfo("Saved", "Options were updated.")
            self.window.destroy()

        except Exception as e:
            messagebox.showerror("Error", f"Invalid input data. \nDetails: {e}")
