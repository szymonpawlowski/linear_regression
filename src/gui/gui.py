import tkinter as tk
from options_ui import OptionsWindow
from data_ui import show_random_data_ui, show_manual_data_ui, show_file_data_ui


class LinearRegressionApp:
    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("Linear Regression")
        self.parent.geometry("1500x900")

        self.content_frame = tk.Frame(self.parent)
        self.content_frame.pack(expand=True, fill='both')

        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        self.data_menu = tk.Menu(self.menubar,
                                 tearoff=False)

        self.data_menu.add_command(label="Generate random data",
                                   command=show_random_data_ui(self.content_frame))
        self.data_menu.add_command(label="Input data manually",
                                   command=show_manual_data_ui(self.content_frame))
        self.data_menu.add_command(label="Import data from file",
                                   command=show_file_data_ui(self.content_frame))

        self.menubar.add_cascade(label="Data",
                                 menu=self.data_menu)

        self.menubar.add_command(label="Options",
                                 command=self.create_options_menu)

        self.menubar.add_command(label="Exit",
                                 command=self.exit_app)
        self.parent.mainloop()

    def create_options_menu(self):
        OptionsWindow(self.parent)

    def exit_app(self):
        self.parent.quit()


LinearRegressionApp()
