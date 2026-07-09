import tkinter as tk
from ui.base_page import BasePage
from utils.constants import Colors, Fonts 


class SplitPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self._create_header()
        self._create_file_section()
        self._create_split_mode_section()
        # self._create_settings_section()
        self._create_action_section()
        self._create_status_bar()
        self._bind_events()
        
        self.selected_file = None
        self.status_timer = None
        

    def _create_header(self):
        header_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )

        header_frame.pack(padx=10, pady=10, fill="x")

        header_frame.grid_columnconfigure(1, weight=1)


        self.back_arrow = tk.Label(
            header_frame,
            text="←",
            bg=Colors.BACKGROUND,
            fg="white",
            font=Fonts.BODY
        )
        self.back_arrow.grid(row=0, column=0, padx=(0, 3), pady=(10, 15), sticky="w")


        self.back = tk.Label(
            header_frame,
            text="Back",
            bg=Colors.BACKGROUND,
            fg="white",
            font=Fonts.BODY
        )
        self.back.grid(row=0, column=1, pady=(10, 15), sticky="w")


        title = tk.Label(
            header_frame,
            text="Split PDF",
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.TITLE
        )
        title.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))


        subtitle = tk.Label(
            header_frame,
            text="Split a PDF by page, extract a page range, or split every page.",
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )
        subtitle.grid(row=2, column=0, columnspan=2, sticky="w")


        divider = tk.Frame(
            header_frame,
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


    def _create_status_bar(self):
        self.status_label = tk.Label(
            self,
            text="Ready",
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        self.status_label.pack(
            anchor="e",
            padx=5,
            pady=(0, 10)
    )


    def _bind_events(self):
        widgets = [
            self.back_arrow,
            self.back
        ]

        for widget in widgets:
            widget.bind("<Button-1>", self._on_click)
            widget.bind("<Enter>", self._on_enter)
            widget.bind("<Leave>", self._on_leave)
            


    def _on_click(self, event):
        self.page_manager.show_page("home")


    def _on_enter(self, event):
        self.back_arrow.config(fg=Colors.PRIMARY, cursor="hand2")
        self.back.config(fg=Colors.PRIMARY, cursor="hand2")
    

    def _on_leave(self, event):
        self.back_arrow.config(fg=Colors.TEXT_PRIMARY)
        self.back.config(fg=Colors.TEXT_PRIMARY)

