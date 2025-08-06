import tkinter as tk
from options import OptionsWindow


class LinearRegressionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry("1500x900")
        self.menubar = tk.Menu(self.window)
        self.window.config(menu=self.menubar)
        self.create_data_menubar()
        self.menubar.add_command(label="Options",
                                 command=self.create_options_menu)
        self.menubar.add_command(label="Exit",
                                 command=self.exit_app)
        self.window.mainloop()

    def create_options_menu(self):
        OptionsWindow(self.window)

    def exit_app(self):
        self.window.quit()

    def create_data_menubar(self):
        self.data_menu = tk.Menu(self.menubar)
        self.data_menu.add_command(label="Generate random data")
        self.data_menu.add_command(label="Input data manually")
        self.data_menu.add_command(label="Import data from file")
        self.menubar.add_cascade(label="Data",
                                 menu=self.data_menu,
                                 underline=0)


app = LinearRegressionApp()
