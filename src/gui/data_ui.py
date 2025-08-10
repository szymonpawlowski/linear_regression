import tkinter as tk


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def show_random_data_ui(parent):
    clear_frame(parent)


def show_manual_data_ui(parent):
    clear_frame(parent)


def show_file_data_ui(parent):
    clear_frame(parent)
