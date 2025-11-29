import tkinter as tk
from tkinter import messagebox
import threading
import time

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from regression.utils import mean_squared_error
from regression.trainer import Trainer


class TrainingWindow(tk.Toplevel):
    def __init__(self, parent, app_instance):
        super.__init__(parent)
        self.title