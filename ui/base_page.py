import tkinter as tk
from utils.constants import Colors

class BasePage(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.configure(bg=Colors.BACKGROUND)