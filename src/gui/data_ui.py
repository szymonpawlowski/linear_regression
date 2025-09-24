import tkinter as tk
from tkinter import filedialog


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


def show_file_data_ui(frame, parent):
    clear_frame(frame)

    # seperate window for file import
    class FileInputWindow:
        def __init__(self, parent):
            self.window = tk.Toplevel(parent)
            self.window.title('File Input')

            parent.update_idletasks()
            main_x = parent.winfo_x()
            main_y = parent.winfo_y()
            main_width = parent.winfo_width()
            main_height = parent.winfo_height()

            file_width = 900
            file_height = 600

            x = main_x + (main_width // 2) - (file_width // 2)
            y = main_y + (main_height // 2) - (file_height // 2)

            self.window.geometry(f"{file_width}x{file_height}+{x}+{y}")

            self.window.resizable(False, False)
            self.window.transient(parent)
            self.window.grab_set()
            self.window.wait_window()

            file_path = filedialog.askopenfilename(title="Select a file",
                                                   filetypes=[(".txt file", "*.txt"),
                                                              (".csv file", "*.csv")])
            
