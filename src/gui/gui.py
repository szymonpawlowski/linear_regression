import tkinter as tk


class LinearRegressionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry("800x600")
        self.create_start_menu()
        self.window.mainloop()

    def return_start_menu(self):
        self.data_selection_frame.destroy()
        self.return_start_menu_button.destroy()
        self.create_start_menu()

    def create_data_selection_menu(self):
        self.data_selection_frame = tk.Frame(self.window)
        self.data_selection_frame.columnconfigure(0, weight=1)
        self.data_selection_frame.columnconfigure(1, weight=1)
        self.data_selection_frame.columnconfigure(2, weight=1)

        self.random_data_button = tk.Button(self.data_selection_frame, text="RANDOM DATA")
        self.random_data_button.grid(row=0, column=0, sticky="we", padx=5)
        self.user_data_button = tk.Button(self.data_selection_frame, text="USER DATA")
        self.user_data_button.grid(row=0, column=1, sticky="we")
        self.file_data_button = tk.Button(self.data_selection_frame, text="FILE DATA")
        self.file_data_button.grid(row=0, column=2, sticky="we", padx=5)
        self.return_start_menu_button = tk.Button(self.data_selection_frame, text="RETURN", command=self.return_start_menu)
        self.return_start_menu_button.grid(row=1, column=1, pady=5)

        self.data_selection_frame.pack(fill="x")

    def start_app(self):
        # clearing window and creating mode selection
        for widget in self.start_menu_widgets:
            widget.grid_forget()
        self.create_data_selection_menu()

    def exit_app(self):
        self.window.quit()

    def create_start_menu(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.columnconfigure(0, weight=1)
        self.welcome_label = tk.Label(self.main_frame, text="LINEAR REGRESSION", font=("Consolas", 20, "bold"), justify="center")
        self.welcome_label.grid(row=0, column=0)
        self.start_button = tk.Button(self.main_frame, text="START", command=self.start_app)
        self.start_button.grid(row=1, column=0, padx=200, pady=10, sticky="we")
        self.exit_button = tk.Button(self.main_frame, text="EXIT", command=self.exit_app)
        self.exit_button.grid(row=2, column=0, padx=200, sticky="we")
        self.start_menu_widgets = [self.welcome_label, self.start_button, self.exit_button]
        self.main_frame.pack(fill="x")


app = LinearRegressionApp()
