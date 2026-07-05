import tkinter as tk
from utils.constants import Colors

class BasePage(tk.Frame):

    def __init__(self, parent, page_manager):
        super().__init__(parent)

        self.page_manager = page_manager

        self.configure(bg=Colors.BACKGROUND)