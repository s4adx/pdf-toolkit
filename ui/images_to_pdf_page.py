import tkinter as tk
from ui.base_page import BasePage


class ImagesToPdfPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)
        
        self.selected_file = None
        self.total_pages = 0

        self.create_header(
            title="Images to PDF",
            subtitle="Combine multiple images into a single PDF in the preferred order."
        )