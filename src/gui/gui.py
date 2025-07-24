import tkinter as tk
import config


class LinearRegressionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry(str(config.WINDOW_WIDTH)+"x"+str(config.WINDOW_HEIGHT))
        self.create_start_menu()
        self.window.mainloop()
        
    def return_start_menu(self):
        self.data_selection_frame.destroy()
        self.return_button.destroy()
        self.create_start_menu()

    def create_data_selection_menu(self):
        self.data_selection_frame = tk.Frame(self.window)
        self.data_selection_frame.pack()
        self.random_data_button = tk.Button(self.data_selection_frame, text = "RANDOM DATA")
        self.random_data_button.pack(padx = 3, side = tk.LEFT)
        self.user_data_button = tk.Button(self.data_selection_frame, text = "USER DATA")
        self.user_data_button.pack(padx = 3, side = tk.LEFT)
        self.file_data_button = tk.Button(self.data_selection_frame, text = "FILE DATA")
        self.file_data_button.pack(padx = 3, side = tk.LEFT)
        self.return_button = tk.Button(self.data_selection_frame, text = "RETURN", command = self.return_start_menu)
        self.return_button.pack(pady = 5)

    def start_app(self):
        # clearing window and creating mode selection
        for widget in self.start_menu_widgets:
            widget.pack_forget()
        self.create_data_selection_menu()

    def exit_app(self):
        self.window.quit()

    def create_start_menu(self):
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack()
        self.welcome_label = tk.Label(self.main_frame, text = "LINEAR REGRESSION", font = ("Consolas", 20, "bold"), justify = "center")
        self.welcome_label.pack(anchor = "n")   # label alignment to center - north anchor
        self.start_button = tk.Button(self.main_frame, text = "START", command = self.start_app)
        self.start_button.pack(pady = 10, anchor = "n")
        self.exit_button = tk.Button(self.main_frame, text = "EXIT", command = self.exit_app)
        self.exit_button.pack(anchor = "n")
        self.start_menu_widgets = [self.welcome_label, self.start_button, self.exit_button]


app = LinearRegressionApp()
