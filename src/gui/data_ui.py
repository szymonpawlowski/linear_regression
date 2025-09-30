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
                     font=('calibre', 20, 'bold'))

    generate_button = tk.Button(frame,
                                text="Generate Data")

    n = tk.IntVar()
    n_label = tk.Label(frame,
                       text="Number of data points (n): ",
                       font=('calibre', 10, 'bold'))
    n_entry = tk.Entry(frame,
                       textvariable=n)

    x_min = tk.IntVar()
    x_max = tk.IntVar()
    x_label = tk.Label(frame,
                       text="Range of x values: ",
                       font=('calibre', 10, 'bold'))
    xmin_entry = tk.Entry(frame,
                          textvariable=x_min)
    xmax_entry = tk.Entry(frame,
                          textvariable=x_max)

    w_min = tk.IntVar()
    w_max = tk.IntVar()
    weight_label = tk.Label(frame,
                            text="Range of weight values: ",
                            font=('calibre', 10, 'bold'))
    weight_min_entry = tk.Entry(frame,
                                textvariable=w_min)
    weight_max_entry = tk.Entry(frame,
                                textvariable=w_max)

    b_min = tk.IntVar()
    b_max = tk.IntVar()
    bias_label = tk.Label(frame,
                          text="Range of bias values: ",
                          font=('calibre', 10, 'bold'))
    bias_min_entry = tk.Entry(frame,
                              textvariable=b_min)
    bias_max_entry = tk.Entry(frame,
                              textvariable=b_max)

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
                     font=('calibre', 20, 'bold'))
    title.pack()


def show_file_data_ui(frame):
    clear_frame(frame)

    title = tk.Label(frame,
                     text="Input Data File",
                     font=('calibre', 20, 'bold'))

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
