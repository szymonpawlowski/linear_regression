import tkinter as tk

from gui.data_ui import show_random_data_ui, show_manual_data_ui, show_file_data_ui
from gui.options_ui import OptionsWindow
from gui.training_ui import TrainingPanel


class LinearRegressionApp:
    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("Linear Regression App")

        try:
            self.parent.state('zoomed')
        except:
            pass

        self.X_data = None
        self.y_data = None
        self.learning_rate = 0.01
        self.epochs = 1000
        self.plot_frequency = 20
        self.mse_stop_threshold = 0.0001
        self.save_plot_auto = False

        # --- WINDOW LOADOUT ---
        # main menu
        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        # main container
        self.main_container = tk.Frame(self.parent)
        self.main_container.pack(expand=True, fill='both', padx=5, pady=5)

        # left container - entries
        self.left_frame = tk.Frame(self.main_container, width=350, bd=1, relief=tk.RIDGE)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        self.left_frame.pack_propagate(False)

        # right container - results
        self.right_frame = tk.Frame(self.main_container, bd=1, relief=tk.RIDGE)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # --- WELCOME SCREEN ---
        self.show_welcome_screen()
        self.show_right_placeholder()

        # --- MENU CONFIG ---
        self.data_menu = tk.Menu(self.menubar, tearoff=False)
        self.data_menu.add_command(
            label="Generate random data",
            command=lambda: self.switch_data_view(show_random_data_ui)
        )
        self.data_menu.add_command(
            label="Input data manually",
            command=lambda: self.switch_data_view(show_manual_data_ui)
        )
        self.data_menu.add_command(
            label="Import data from file",
            command=lambda: self.switch_data_view(show_file_data_ui)
        )
        self.menubar.add_cascade(label="Data", menu=self.data_menu)
        self.menubar.add_command(label="Options", command=self.open_options)
        self.menubar.add_command(label="Exit", command=self.parent.quit)

        self.parent.mainloop()

    # --- VIEW METHODS ---
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_frame(self.left_frame)
        tk.Label(self.left_frame, text="Choose data source\nfrom the menu above.", font=('Arial', 16, 'bold'), justify=tk.CENTER).pack(pady=20)

    def show_right_placeholder(self):
        self.clear_frame(self.right_frame)
        tk.Label(self.right_frame, text="Plot & results will show up here.",
                 font=('Arial', 14, 'italic'), fg="gray").pack(expand=True)

    def switch_data_view(self, view_function):

        self.clear_frame(self.left_frame)
        view_function(self.left_frame, self)

    def show_training_panel(self):
        self.clear_frame(self.right_frame)

        training_view = TrainingPanel(self.right_frame, self)
        training_view.pack(expand=True, fill='both')

    def open_options(self):
        OptionsWindow(self.parent, self)
