import tkinter as tk


class LinearRegressionApp:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry("800x600")
        self.create_start_screen()
        self.window.mainloop()

    def start_app(self):
        
    def exit_app(self):
        self.window.quit()

    def create_start_screen(self):
        self.welcome_label = tk.Label(self.window, text = "LINEAR REGRESSION", font = ("Consolas", 20, "bold"), justify = "center")
        self.welcome_label.pack(anchor = "n")   # label alignment to center - north anchor
        self.start_button = tk.Button(self.window, text = "START")
        self.start_button.pack(pady = 10, anchor = "n", command = self.start_app)
        self.exit_button = tk.Button(self.window, text = "EXIT", command = self.exit_app)
        self.exit_button.pack(anchor = "n")


app = LinearRegressionApp()
