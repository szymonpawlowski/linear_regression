import tkinter as tk
from tkinter import filedialog, messagebox
import random


def generate_synthetic_data(n, x_min, x_max, w_min, w_max, b_min, b_max):
    true_w = random.uniform(w_min, w_max)
    true_b = random.uniform(b_min, b_max)

    X = []
    y = []

    for _ in range(n):
        x_val = random.uniform(x_min, x_max)
        noise = random.uniform(-1, 1) * 0.1 * (abs(true_w * x_val) + 1)
        y_val = true_w * x_val + true_b + noise

        X.append(x_val)
        y.append(y_val)

    return X, y, true_w, true_b


def parse_manual_data(text_data):
    X = []
    y = []
    lines = text_data.strip().split('\n')
    for line in lines:
        if not line.strip(): continue
        clean_line = line.replace(';', ',')
        parts = clean_line.split(',')
        if len(parts) == 2:
            try:
                x_val = float(parts[0])
                y_val = float(parts[1])
                X.append(x_val)
                y.append(y_val)
            except ValueError:
                continue
    return X, y


def show_random_data_ui(frame, app_instance):

    tk.Label(frame, text="Generate Random Data", font=('calibre', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    entries = {}
    labels_info = [
        ("epochs", "Epochs:", "1000"),
        ("lr", "Learning Rate:", "0.01"),
        ("n", "Count (n):", "50"),
        ("x_min", "X min:", "0"),
        ("x_max", "X max:", "10"),
        ("w_min", "Slope min:", "1"),
        ("w_max", "Slope max:", "5"),
        ("b_min", "Bias min:", "0"),
        ("b_max", "Bias max:", "10"),
    ]

    for i, (key, text, default) in enumerate(labels_info):
        tk.Label(frame, text=text).grid(row=i+1, column=0, sticky='e', padx=5, pady=2)
        entry = tk.Entry(frame, width=15)
        entry.insert(0, default)
        entry.grid(row=i+1, column=1, sticky='w', padx=5, pady=2)
        entries[key] = entry

    def submit_random():
        try:
            n = int(entries['n'].get())
            epochs = int(entries['epochs'].get())
            lr = float(entries['lr'].get())

            X, y, true_w, true_b = generate_synthetic_data(
                n,
                float(entries['x_min'].get()), float(entries['x_max'].get()),
                float(entries['w_min'].get()), float(entries['w_max'].get()),
                float(entries['b_min'].get()), float(entries['b_max'].get())
            )

            app_instance.X_data = X
            app_instance.y_data = y
            app_instance.epochs = epochs
            app_instance.learning_rate = lr

            messagebox.showinfo("Success", f"Generated {n} points.\nTarget slope: {true_w:.2f}")

            app_instance.show_training_panel()

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers.")

    tk.Button(frame, text="Generate & Load", command=submit_random, bg="#dddddd", height=2).grid(row=10, column=0, columnspan=2, pady=20, sticky="ew")


def show_manual_data_ui(frame, app_instance):
    tk.Label(frame, text="Manual Data Input", font=('calibre', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="Epochs:").grid(row=1, column=0, sticky='e')
    epochs_entry = tk.Entry(frame, width=10)
    epochs_entry.insert(0, "1000")
    epochs_entry.grid(row=1, column=1, sticky='w')

    tk.Label(frame, text="Learn Rate:").grid(row=2, column=0, sticky='e')
    lr_entry = tk.Entry(frame, width=10)
    lr_entry.insert(0, "0.01")
    lr_entry.grid(row=2, column=1, sticky='w')

    tk.Label(frame, text="Data points (x, y) - one per line:").grid(row=3, column=0, columnspan=2, pady=(10, 0))

    text_area = tk.Text(frame, height=10, width=30)
    text_area.grid(row=4, column=0, columnspan=2, pady=5, padx=5)
    text_area.insert("1.0", "1.0, 2.0\n2.0, 4.0\n3.0, 6.0")

    def submit_manual():
        raw_text = text_area.get("1.0", tk.END)
        try:
            X, y = parse_manual_data(raw_text)
            if len(X) < 2:
                raise ValueError("Need at least 2 points.")

            app_instance.epochs = int(epochs_entry.get())
            app_instance.learning_rate = float(lr_entry.get())
            app_instance.X_data = X
            app_instance.y_data = y

            messagebox.showinfo("Success", f"Loaded {len(X)} points manually.")

            app_instance.show_training_panel()

        except ValueError:
            messagebox.showerror("Error", "Check your inputs (epochs/lr must be numbers).")
        except Exception as e:
            messagebox.showerror("Error", f"Could not parse data.\n{e}")

    tk.Button(frame, text="Load Data", command=submit_manual, bg="#dddddd", height=2).grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")


def show_file_data_ui(frame, app_instance):
    tk.Label(frame, text="Import Data from File", font=('calibre', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="Epochs:").grid(row=1, column=0, sticky='e')
    epochs_entry = tk.Entry(frame, width=10)
    epochs_entry.insert(0, "1000")
    epochs_entry.grid(row=1, column=1, sticky='w')

    tk.Label(frame, text="Learn Rate:").grid(row=2, column=0, sticky='e')
    lr_entry = tk.Entry(frame, width=10)
    lr_entry.insert(0, "0.01")
    lr_entry.grid(row=2, column=1, sticky='w')

    file_path_var = tk.StringVar(value="No file selected")

    def select_file():
        file = filedialog.askopenfile(mode='r', filetypes=[("Text/CSV", "*.txt *.csv")])
        if file:
            file_path_var.set(file.name)
            file.close()

    def load_file_content():
        path = file_path_var.get()
        if path == "No file selected":
            messagebox.showwarning("Warning", "Please select a file first.")
            return

        try:
            epochs = int(epochs_entry.get())
            lr = float(lr_entry.get())

            with open(path, 'r') as f:
                content = f.read()
                X, y = parse_manual_data(content)

                if len(X) < 2:
                    raise ValueError("File must contain at least 2 data points.")

                app_instance.X_data = X
                app_instance.y_data = y
                app_instance.epochs = epochs
                app_instance.learning_rate = lr

                messagebox.showinfo("Success", f"Loaded {len(X)} points from file.")

                app_instance.show_training_panel()

        except ValueError:
            messagebox.showerror("Error", "Check your inputs (epochs/lr).")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file.\n{e}")

    tk.Label(frame, text="Supported format: x,y (one pair per line)").grid(row=3, column=0, columnspan=2, pady=5)

    tk.Button(frame, text="Browse...", command=select_file).grid(row=4, column=0, columnspan=2, pady=5)
    tk.Label(frame, textvariable=file_path_var, fg="blue", wraplength=300).grid(row=5, column=0, columnspan=2)

    tk.Button(frame, text="Load Data & Set to Model", command=load_file_content, bg="#dddddd", height=2).grid(row=6, column=0, columnspan=2, pady=20, sticky="ew")