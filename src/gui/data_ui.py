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
    label_n = tk.Label(frame,
                         text="Number of data points (n): ")
    label_xmin = tk.Label(frame,
                          text="Min. value of x (x min): ")
    label_xmax = tk.Label(frame,
                          text="Max. value of x (x max): ")
    label_wmin = tk.Label(frame,
                       text="Min. weight value (weight min): ")
    label_wmax = tk.Label(frame,
                          text="Max. weight value (weight max): ")

    title.pack()
    label_n.pack()
    label_xmin.pack()
    label_xmax.pack()
    label_wmin.pack()
    label_wmax.pack()
    generate_button.pack(anchor='s', pady=10)


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
