import tkinter as tk
from ui.base_page import BasePage


class RotatePage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)
        self._create_widgets()

        self.create_header(
            title="Rotate PDF",
            subtitle="Rotate all pages, a single page, or a selected page range."
        )

        

        self.create_status_bar()
        self.update_default_status()

    def _create_widgets(self):
        pass