import tkinter as tk


class LinearRegressionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry("1600x1000")
        self.menubar = tk.Menu(self.window)
        self.window.config(menu=self.menubar)
        self.create_data_menubar()
        self.create_options_menubar()
        self.create_exit_menubar()
        self.window.mainloop()


    def exit_app(self):
        self.window.quit()

    def create_start_menu(self):
        self.main_sidebar =  tk.Frame(self.window)
        self.main_sidebar.columnconfigure(0, weight=1)

        self.title_label = tk.Label(self.main_sidebar,
                                    text="LINEAR\n REGRESSION ",
                                    font=("Consolas", 20, "bold"),
                                    justify="center",
                                    relief="raised",
                                    bd=5)
        self.title_label.grid(row=0, column=0, sticky="we")

        self.start_button = tk.Button(self.main_sidebar,
                                      text="START",
                                      height=2,
                                      font=("Consolas", 15),
                                      relief="raised",
                                      bd=5,
                                      command=self.start_app)
        self.start_button.grid(row=1, column=0, sticky="we")

        self.exit_button = tk.Button(self.main_sidebar,
                                     text="EXIT",
                                     height=2,
                                     font=("Consolas", 15),
                                     relief="raised",
                                     bd=5,
                                     command=self.exit_app)
        self.exit_button.grid(row=2, column=0, sticky="we")

        self.empty_label = tk.Label(self.main_sidebar,
                                    relief="raised",
                                    bd=5,
                                    height=10000)
        self.empty_label.grid(row=3, column=0, sticky="we")

        self.start_menu_widgets = [self.title_label, self.start_button, self.exit_button, self.empty_label]
        self.main_sidebar.place(x=0, y=0, anchor="nw")

    def create_data_menubar(self):
        self.data_menu = tk.Menu(self.menubar)
        self.data_menu.add_command(label="Generate random data")
        self.data_menu.add_command(label="Input data manually")
        self.data_menu.add_command(label="Import data from file")
        self.menubar.add_cascade(label="Data",
                                 menu=self.data_menu,
                                 underline=0)

    def create_options_menubar(self):
        self.options_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Options",
                                 menu=self.options_menu,
                                 underline=0)

    def create_exit_menubar(self):
        self.exit_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Exit",
                                 command=self.exit_app)


app = LinearRegressionApp()
