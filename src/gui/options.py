import tkinter as tk


class OptionsWindow:
    def __init__(self, main_window):
        self.window = tk.Toplevel(main_window)
        self.window.title('Options')

        #centering the options window
        main_window.update_idletasks()
        main_x = main_window.winfo_x()
        main_y = main_window.winfo_y()
        main_width = main_window.winfo_width()
        main_height = main_window.winfo_height()

        options_width = 900
        options_height = 600

        x = main_x + (main_width // 2) - (options_width // 2)
        y = main_y + (main_height // 2) - (options_height // 2)

        self.window.geometry(f"{options_width}x{options_height}+{x}+{y}")

        self.wip = tk.Label(self.window, text="Options WIP")
        self.wip.place(relx=0.5, rely=0.5, anchor="center")

        self.window.resizable(False, False)
        self.window.transient(main_window)
        self.window.grab_set()
        self.window.wait_window()
