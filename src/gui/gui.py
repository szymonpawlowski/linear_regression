import tkinter as tk
from options_ui import OptionsWindow
from data_ui import show_random_data_ui


class LinearRegressionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry("1500x900")
        self.menubar = tk.Menu(self.window)
        self.window.config(menu=self.menubar)

        self.data_menu = tk.Menu(self.menubar,
                                 tearoff=False)

        self.data_menu.add_command(label="Generate random data",
                                   command=show_random_data_ui(self.window))
        self.data_menu.add_command(label="Input data manually")
        self.data_menu.add_command(label="Import data from file")

        self.menubar.add_cascade(label="Data",
                                 menu=self.data_menu)

        self.menubar.add_command(label="Options",
                                 command=self.create_options_menu)

        self.menubar.add_command(label="Exit",
                                 command=self.exit_app)
        self.window.mainloop()

    def create_options_menu(self):
        OptionsWindow(self.window)

    def exit_app(self):
        self.window.quit()


LinearRegressionApp()
