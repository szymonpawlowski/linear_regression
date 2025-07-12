import tkinter as tk


class LinearRegressionApp:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry("800x600")
        self.welcome_label = tk.Label(self.window, text = "LINEAR REGRESSION", font = ("Consolas", 20), justify = "center")
        self.welcome_label.pack(anchor = "n")   # label alignment to center - north anchor
        self.window.mainloop()


app = LinearRegressionApp()
