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

    n_label = tk.Label(frame,
                       text="Number of data points (n): ",
                       font=('calibre', 10, 'bold'))
    n_entry = tk.Entry(frame)

    epochs_label = tk.Label(frame,
                            text="Number of epochs: ",
                            font=('calibre', 10, 'bold'))
    epochs_entry = tk.Entry(frame)

    lr_label = tk.Label(frame,
                        text="Learning rate: ",
                        font=('calibre', 10, 'bold'))
    lr_entry = tk.Entry(frame)

    x_label = tk.Label(frame,
                       text="Range of x values: ",
                       font=('calibre', 10, 'bold'))
    xmin_entry = tk.Entry(frame)
    xmax_entry = tk.Entry(frame)

    weight_label = tk.Label(frame,
                            text="Range of weight values: ",
                            font=('calibre', 10, 'bold'))
    weight_min_entry = tk.Entry(frame)
    weight_max_entry = tk.Entry(frame)

    bias_label = tk.Label(frame,
                          text="Range of bias values: ",
                          font=('calibre', 10, 'bold'))
    bias_min_entry = tk.Entry(frame)
    bias_max_entry = tk.Entry(frame)

    def submit_random():
        n = int(n_entry.get())
        epochs = int(epochs_entry.get())
        lr = float(lr_entry.get())
        x_min = float(xmin_entry.get())
        x_max = float(xmax_entry.get())
        w_min = float(weight_min_entry.get())
        w_max = float(weight_max_entry.get())
        b_min = float(bias_min_entry.get())
        b_max = float(bias_max_entry.get())

        #print(f"{n}, {epochs}, {lr}, {x_min}, {x_max}, {w_min}, {w_max}, {b_min}, {b_max}")

    generate_button = tk.Button(frame,
                                text="Generate Data",
                                command=submit_random)

    title.grid(row=0, column=0, columnspan=8, sticky='we')

    n_label.grid(row=1, column=0)
    n_entry.grid(row=1, column=1, columnspan=2, sticky='we')

    epochs_label.grid(row=2, column=0)
    epochs_entry.grid(row=2, column=1, columnspan=2, sticky='we')

    lr_label.grid(row=3, column=0)
    lr_entry.grid(row=3, column=1, columnspan=2, sticky='we')

    x_label.grid(row=4, column=0)
    xmin_entry.grid(row=4, column=1)
    xmax_entry.grid(row=4, column=2)

    weight_label.grid(row=5, column=0)
    weight_min_entry.grid(row=5, column=1)
    weight_max_entry.grid(row=5, column=2)

    bias_label.grid(row=6, column=0)
    bias_min_entry.grid(row=6, column=1)
    bias_max_entry.grid(row=6, column=2)

    generate_button.grid(row=7, column=1)




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
