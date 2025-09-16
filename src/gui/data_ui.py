import tkinter as tk


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_random_data_ui(frame):
    clear_frame(frame)
    title = tk.Label(frame,
                     text="Generate Random data",
                     font=("Helvetica", 20))
    title.pack()


def show_manual_data_ui(frame):
    clear_frame(frame)
    title = tk.Label(frame,
                     text="Manual Data Input",
                     font=("Helvetica", 20))
    title.pack()


def show_file_data_ui(frame):
    clear_frame(frame)
    # seperate window for file import
