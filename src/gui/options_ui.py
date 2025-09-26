import tkinter as tk


class OptionsWindow:
    def __init__(self, parent):
        self.window = tk.Toplevel(parent)
        self.window.title('Options')

        #centering
        parent.update_idletasks()
        main_x = parent.winfo_x()
        main_y = parent.winfo_y()
        main_width = parent.winfo_width()
        main_height = parent.winfo_height()

        options_width = 900
        options_height = 600

        x = main_x + (main_width // 2) - (options_width // 2)
        y = main_y + (main_height // 2) - (options_height // 2)

        self.window.geometry(f"{options_width}x{options_height}+{x}+{y}")

        self.window.resizable(False, False)
        self.window.transient(parent)
        self.window.grab_set()
        self.window.wait_window()
