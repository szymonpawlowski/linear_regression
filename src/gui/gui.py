import tkinter as tk

from options_ui import OptionsWindow
from data_ui import show_random_data_ui, show_manual_data_ui, show_file_data_ui


class LinearRegressionApp:
    def __init__(self):
        self.parent = tk.Tk()
        self.parent.title("Linear Regression Project")
        try:
            self.parent.state('zoomed')
        except:
            pass

        self.X_data = None
        self.y_data = None
        self.learning_rate = 0.01
        self.epochs = 1000

        self.menubar = tk.Menu(self.parent)
        self.parent.config(menu=self.menubar)

        self.content_frame = tk.Frame(self.parent)
        self.content_frame.pack(expand=True, fill='both', padx=20, pady=20)

        self.show_welcome_screen()

        self.data_menu = tk.Menu(self.menubar, tearoff=False)

        self.data_menu.add_command(
            label="Generate random data",
            command=lambda: self.switch_view(show_random_data_ui)
        )

        self.data_menu.add_command(
            label="Input data manually",
            command=lambda: self.switch_view(show_manual_data_ui)
        )

        self.data_menu.add_command(
            label="Import data from file",
            command=lambda: self.switch_view(show_file_data_ui)
        )

        self.menubar.add_cascade(label="Data", menu=self.data_menu)

        self.menubar.add_command(label="Options", command=self.create_options_menu)
        self.menubar.add_command(label="Exit", command=self.exit_app)

        self.parent.mainloop()

    def show_welcome_screen(self):
        self.clear_content()
        self.main_label = tk.Label(self.content_frame,
                                   text="Linear Regression App",
                                   font=('calibre', 30, 'bold'))
        self.main_label.pack(pady=50)

        info_label = tk.Label(self.content_frame,
                              text="Wybierz źródło danych z menu 'Data' aby rozpocząć.",
                              font=('calibre', 12))
        info_label.pack()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def switch_view(self, view_function):
        self.clear_content()
        view_function(self.content_frame, self)

    def create_options_menu(self):
        OptionsWindow(self.parent, self)

    def exit_app(self):
        self.parent.quit()


if __name__ == "__main__":
    LinearRegressionApp()