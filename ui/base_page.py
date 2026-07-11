import tkinter as tk
from utils.constants import Colors, Fonts

class BasePage(tk.Frame):

    def __init__(self, parent, page_manager):
        super().__init__(parent)

        self.page_manager = page_manager

        self.configure(bg=Colors.BACKGROUND)

    
    def create_header(self, title, subtitle):
        self.header_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )

        self.header_frame.pack(padx=10, pady=10, fill="x")

        self.header_frame.grid_columnconfigure(1, weight=1)


        self.back_arrow = tk.Label(
            self.header_frame,
            text="←",
            bg=Colors.BACKGROUND,
            fg="white",
            font=Fonts.BODY
        )
        self.back_arrow.grid(row=0, column=0, padx=(0, 3), pady=(10, 15), sticky="w")


        self.back = tk.Label(
            self.header_frame,
            text="Back",
            bg=Colors.BACKGROUND,
            fg="white",
            font=Fonts.BODY
        )
        self.back.grid(row=0, column=1, pady=(10, 15), sticky="w")


        title_label = tk.Label(
            self.header_frame,
            text=title,
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.TITLE
        )

        title_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))


        subtitle_title = tk.Label(
            self.header_frame,
            text=subtitle,
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )
        subtitle_title.grid(row=2, column=0, columnspan=2, sticky="w")


        divider = tk.Frame(
            self.header_frame,
            bg=Colors.BORDER,
            height=1
        )

        divider.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky="ew",
            pady=(20, 0)
        )

    
    def create_status_bar(self):
        pass