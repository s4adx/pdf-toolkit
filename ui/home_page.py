import tkinter as tk
from ui.base_page import BasePage
from utils.constants import Colors, Fonts

class HomePage(BasePage):

    def __init__(self, parent):
        super().__init__(parent)
        self._create_widgets()
        

    def _create_widgets(self):
        title = tk.Label(
            self,
            text="PDF Toolkit",
            fg=Colors.TEXT_PRIMARY,
            bg=Colors.BACKGROUND,
            font=Fonts.TITLE
        )
        title.pack()

