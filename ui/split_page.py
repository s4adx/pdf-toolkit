import tkinter as tk
from ui.base_page import BasePage
from utils.constants import Colors, Fonts 


class SplitPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.create_header(
            title="Split PDF",
            subtitle="Split a PDF by page, extract a page range, or split every page."
        )

        self._create_file_section()
        self._create_split_mode_section()
        # self._create_settings_section()
        self._create_action_section()
        
        self.create_status_bar()
        self.update_default_status()

        self.selected_file = None
        self.status_timer = None
        

    def _create_file_section(self):

        card = tk.Frame(
            self,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            padx=10,
            pady=(15, 8)
        )


        title = tk.Label(
            card,
            text="Selected PDF",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )
        title.pack(anchor="w", padx=15, pady=(12, 8))


        row = tk.Frame(
            card,
            bg=Colors.CARD
        )
        row.pack(fill="x", padx=15, pady=(0, 12))


        self.pdf_name = tk.Label(
            row,
            text="No PDF Selected",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )
        self.pdf_name.pack(side="left")


        self.browse_button = tk.Button(
            row,
            text="Browse",
            width=12
        )
        self.browse_button.pack(side="right")


    def _create_split_mode_section(self):

        card = tk.Frame(
            self,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        title = tk.Label(
            card,
            text="Split Mode",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(anchor="w", padx=15, pady=(12,8))

        self.split_mode = tk.StringVar(value="split")

        options = [
            ("Split at Page", "split"),
            ("Extract Page Range", "extract"),
            ("Split Every Page", "every")
        ]


        for text, value in options:

            tk.Radiobutton(
                card,
                text=text,
                variable=self.split_mode,
                value=value,
                bg=Colors.CARD,
                fg=Colors.TEXT_PRIMARY,
                activebackground=Colors.CARD,
                selectcolor=Colors.CARD
            ).pack(anchor="w", padx=20, pady=2)


        tk.Frame(card, height=8, bg=Colors.CARD).pack()


    def _create_settings_section(self):

        card = tk.Frame(
            self,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            padx=10,
            pady=(0,20)
        )


        self.setting_title = tk.Label(
            card,
            text="Split After Page",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        self.setting_title.pack(
            anchor="w",
            padx=15,
            pady=(12,8)
        )


        self.page_entry = tk.Entry(
            card,
            width=15,
            justify="center",
            font=Fonts.BODY
        )

        self.page_entry.pack(
            anchor="w",
            padx=15,
            pady=(0,15)
        )
        
    
    def _create_action_section(self):
        action_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=20
        )

        self.split_button = tk.Button(
            action_frame,
            text="Split PDF",
            width=20,
            # command=
        )
        self.split_button.config(state="disabled")
        self.split_button.pack()

    def update_default_status(self):
        pass
