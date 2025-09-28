import tkinter as tk
from tkinter import filedialog


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def browse_files():
    filepath = filedialog.askopenfile(title="Select file",
                                      filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
    return filepath


def show_random_data_ui(frame):
    clear_frame(frame)

    title = tk.Label(frame,
                     text="Generate Random Data",
                     font=("Helvetica", 20))

    generate_button = tk.Button(frame,
                                text="Generate Data")
    n_label = tk.Label(frame,
                         text="Number of data points (n): ")
    n_entry = tk.Entry(frame)

    x_label = tk.Label(frame,
                       text="Range of x values: ")
    xmin_entry = tk.Entry(frame)
    xmax_entry = tk.Entry(frame)

    weight_label = tk.Label(frame,
                            text="Range of weight values: ")
    weight_min_entry = tk.Entry(frame)
    weight_max_entry = tk.Entry(frame)

    bias_label = tk.Label(frame,
                          text="Range of bias values: ")
    bias_min_entry = tk.Entry(frame)
    bias_max_entry = tk.Entry(frame)

    title.grid(row=0, column=0, columnspan=8, sticky='we')

    n_label.grid(row=1, column=0)
    n_entry.grid(row=1, column=1, columnspan=2, sticky='we')

    x_label.grid(row=2, column=0)
    xmin_entry.grid(row=2, column=1)
    xmax_entry.grid(row=2, column=2)

    weight_label.grid(row=3, column=0)
    weight_min_entry.grid(row=3, column=1)
    weight_max_entry.grid(row=3, column=2)

    bias_label.grid(row=4, column=0)
    bias_min_entry.grid(row=4, column=1)
    bias_max_entry.grid(row=4, column=2)

    generate_button.grid(row=5, column=1)


def show_manual_data_ui(frame):
    clear_frame(frame)

    title = tk.Label(frame,
                     text="Manual Data Input",
                     font=("Helvetica", 20))
    title.pack()


def show_file_data_ui(frame):
    clear_frame(frame)

    title = tk.Label(frame,
                     text="Input Data File",
                     font=("Helvetica", 20))

    select_file_label = tk.Label(frame, text="Selected file: ")
    browse_file_button = tk.Button(frame, text="Browse...",
                                   command=lambda: browse_files())
    epoch_label = tk.Label(frame, text="Epochs: ")
    lr_label = tk.Label(frame, text="Learning rate: ")

    title.pack()
    select_file_label.pack(anchor='w', padx=10)
    browse_file_button.pack()
    epoch_label.pack(anchor='w', padx=10)
    lr_label.pack(anchor='w', padx=10)

    filename = "None"
    select_file_label.config(text=f"Selected file: {filename}")
