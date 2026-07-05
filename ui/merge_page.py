import tkinter as tk
from ui.base_page import BasePage
from utils.constants import Colors, Fonts


class MergePage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self._create_header()
        self._create_file_section()
        self._create_buttons()
        self._create_action_section()
        self._create_status_bar()
        self._bind_events()
        

    def _create_widgets(self):
        self._create_header()
        

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
            text="Merge PDF",
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.TITLE
        )
        title.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))


        subtitle = tk.Label(
            header_frame,
            text="Combine multiple PDF files into one document.",
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
        file_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )

        file_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(20, 0)
        )

        title = tk.Label(
            file_frame,
            text="Selected PDF Files",
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(anchor="w", pady=(0, 10))


        self.file_listbox = tk.Listbox(
            file_frame,
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.BODY,
            selectbackground=Colors.PRIMARY,
            selectforeground="white",
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground=Colors.BORDER,
            height=5
        )

        self.file_listbox.pack(
            side="left",
            fill="both",
            expand=True
        )


        scrollbar = tk.Scrollbar(
            file_frame,
            orient="vertical",
            command=self.file_listbox.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.file_listbox.config(
            yscrollcommand=scrollbar.set
        )


        self.file_listbox.insert(
            tk.END,
            "No PDF files selected."
        )


    def _create_buttons(self):
        button_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )

        button_frame.pack(
            fill="x",
            padx=10,
            pady=(20, 0)
        )

        self.add_button = tk.Button(
            button_frame,
            text="Add PDFs",
            width=15,
            command=lambda: print("File added")
        )

        self.add_button.pack(
            side="left"
        )


        self.remove_button = tk.Button(
            button_frame,
            text="Remove Selected",
            width=15,
            command=lambda: print("File removed")
        )

        self.remove_button.pack(
            side="left",
            padx=(10, 0)
        )

    
    def _create_action_section(self):
        action_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=30
        )

        self.merge_button = tk.Button(
            action_frame,
            text="Merge PDFs",
            width=20,
            command=lambda: print("PDFs merged")
        )

        self.merge_button.pack()


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
            padx=10,
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


        






