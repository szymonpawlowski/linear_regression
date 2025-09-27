import tkinter as tk
from options_ui import OptionsWindow
from data_ui import show_random_data_ui, show_manual_data_ui, show_file_data_ui


class LinearRegressionApp:
    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("Linear Regression")
        #width = self.parent.winfo_screenwidth()
        #height = self.parent.winfo_screenheight()
        #self.parent.geometry(f"{width}x{height}")
        self.parent.state('zoomed')

        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        self.content_frame = tk.Frame(self.parent)
        self.main_label = tk.Label(self.content_frame,
                                   text="Linear Regression App",
                                   font=("Helvetica", 20))
        self.main_label.pack()
        self.content_frame.pack(expand=True, fill='both')

        self.data_menu = tk.Menu(self.menubar,
                                 tearoff=False)

        self.data_menu.add_command(
            label="Generate random data",
            command=lambda: show_random_data_ui(self.content_frame)
        )

        self.data_menu.add_command(
            label="Input data manually",
            command=lambda: show_manual_data_ui(self.content_frame)
        )

        self.data_menu.add_command(
            label="Import data from file",
            command=lambda: show_file_data_ui(self.content_frame)
        )

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
