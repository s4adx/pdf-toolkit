import tkinter as tk
from ui.base_page import BasePage
from utils.constants import Colors, Fonts
from ui.tools_card import ToolCard

class HomePage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)
        self._create_widgets()
        

    def _create_widgets(self):
        self._create_header()
        self._create_tool_cards()


    def _create_header(self):
        header_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )
        header_frame.pack(padx=20, pady=20, fill="x")

        header_frame.grid_columnconfigure(0, weight=1)

        title = tk.Label(
            header_frame,
            text="PDF Toolkit",
            fg=Colors.TEXT_PRIMARY,
            bg=Colors.BACKGROUND,
            font=Fonts.TITLE,
        )
        title.grid(
            row=0,
            column=0,
            sticky="ew"
        )

        sub_title = tk.Label(
            header_frame,
            text="Your All-in-One PDF Utility",
            fg=Colors.TEXT_PRIMARY,
            bg=Colors.BACKGROUND,
            font=Fonts.SUBHEADING,
        )
        sub_title.grid(
            row=1,
            column=0,
            sticky="ew"
        )

    def _create_tool_cards(self):
        cards_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )
        cards_frame.pack(padx=20, pady=20, fill="x")

        for i in range(4):
            cards_frame.grid_columnconfigure(i, weight=1)

        cards = [
            ("Merge PDF", "📄", "merge"),
            ("Split PDF", "✂️", "split"),
            ("Rotate PDF", "🔄", "rotate"),
            ("Delete Pages", "🗑️", "delete"),
            ("Protect PDF", "🔒", "protect"),
            ("Images → PDF", "🖼️", "images_to_pdf"),
            ("PDF → Images", "📷", "pdf_to_images"),
            ("Compress PDF", "🗜️", "compress"),
        ]

        for index, (text, icon, page_name) in enumerate(cards):

            row = index // 4
            column = index % 4

            card = ToolCard(
                cards_frame,
                text=text,
                icon=icon,
                command=lambda page=page_name: self.page_manager.show_page(page)
            )

            card.grid(
                row=row,
                column=column,
                padx=15,
                pady=15
            )

              



