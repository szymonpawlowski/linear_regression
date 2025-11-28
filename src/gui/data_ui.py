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
            X.append(float(parts[0]))
            y.append(float(parts[1]))
    return X, y


def show_random_data_ui(frame, app_instance):

    title = tk.Label(frame, text="Generate Random Data", font=('calibre', 20, 'bold'))
    title.grid(row=0, column=0, columnspan=3, pady=10)

    entries = {}
    labels_info = [
        ("epochs", "Number of epochs: ", "1000"),
        ("lr", "Learning rate: ", "0.01"),
        ("n", "Number of points (n): ", "50"),
        ("x_min", "X min: ", "0"),
        ("x_max", "X max: ", "10"),
        ("w_min", "Weight min (slope): ", "1"),
        ("w_max", "Weight max (slope): ", "5"),
        ("b_min", "Bias min (intercept): ", "0"),
        ("b_max", "Bias max (intercept): ", "10"),
    ]

    for i, (key, text, default) in enumerate(labels_info):
        tk.Label(frame, text=text).grid(row=i+1, column=0, sticky='e', padx=5, pady=2)
        entry = tk.Entry(frame)
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

            messagebox.showinfo("Success", f"Generated {n} points.\nTarget slope: {true_w:.2f}\nTarget bias: {true_b:.2f}")

            # Tu można by wywołać funkcję rysującą wstępny wykres, gdy już ją napiszemy
            # np. app_instance.refresh_plot()

        except ValueError as e:
            messagebox.showerror("Error", "Invalid input. Please enter numbers.")

    tk.Button(frame, text="Generate Data", command=submit_random, bg="#dddddd", height=2, width=20).grid(row=10, column=0, columnspan=2, pady=20)


def show_manual_data_ui(frame, app_instance):
    title = tk.Label(frame, text="Manual Data Input", font=('calibre', 20, 'bold'))
    title.pack(pady=10)

    info = tk.Label(frame, text="Enter data points (x, y) - one pair per line.\nExample:\n1.0, 2.5\n2.0, 4.1")
    info.pack()

    text_area = tk.Text(frame, height=10, width=40)
    text_area.pack(pady=10)

    def submit_manual():
        raw_text = text_area.get("1.0", tk.END)
        try:
            X, y = parse_manual_data(raw_text)
            if len(X) < 2:
                raise ValueError("Need at least 2 points.")

            app_instance.X_data = X
            app_instance.y_data = y

            messagebox.showinfo("Success", f"Loaded {len(X)} points manually.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not parse data.\n{e}")

    tk.Button(frame, text="Load Data", command=submit_manual).pack(pady=10)


def show_file_data_ui(frame, app_instance):
    title = tk.Label(frame, text="Import Data from File", font=('calibre', 20, 'bold'))
    title.pack(pady=10)

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
            with open(path, 'r') as f:
                content = f.read()
                X, y = parse_manual_data(content)

                app_instance.X_data = X
                app_instance.y_data = y
                messagebox.showinfo("Success", f"Loaded {len(X)} points from file.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file.\n{e}")

    tk.Label(frame, text="Supported format: x,y (one pair per line)").pack()

    file_label = tk.Label(frame, textvariable=file_path_var, fg="blue")
    file_label.pack(pady=5)

    browse_btn = tk.Button(frame, text="Browse...", command=select_file)
    browse_btn.pack(pady=5)

    load_btn = tk.Button(frame, text="Load Data & Set to Model", command=load_file_content, bg="#dddddd")
    load_btn.pack(pady=20)