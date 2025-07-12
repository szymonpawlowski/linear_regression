import tkinter as tk


class LinearRegressionApp:
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("Linear Regression")
        self.window.geometry("800x800")
        self.window.mainloop()


app = LinearRegressionApp()
