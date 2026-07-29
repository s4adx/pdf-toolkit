import tkinter as tk
from pathlib import Path

from ui.base_page import BasePage
from utils.constants import Colors, Fonts
from utils.file_dialog import select_pdf_file
from utils.helpers import count_pdf_pages


class ProtectPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.selected_file = None
        self.total_pages = 0

        self.create_header(
            title="Protect PDF",
            subtitle="Add password protection to prevent unauthorized access to a PDF."
        )

        self._create_content_layout()
        self._create_file_section()
        self._create_password_section()
        self._create_action_section()

        self.create_status_bar()
        self.update_default_status()


    def _create_content_layout(self):
        self.content_frame = tk.Frame(
            self,
            bg=Colors.BACKGROUND
        )

        self.content_frame.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=(6, 0)
        )


    def _create_file_section(self):
        card = tk.Frame(
            self.content_frame,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.pack(fill="x")

        title = tk.Label(
            card,
            text="Selected PDF",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(11, 3)
        )

        description = tk.Label(
            card,
            text="Choose the PDF that should be protected.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        description.pack(
            anchor="w",
            padx=15
        )

        row = tk.Frame(
            card,
            bg=Colors.CARD
        )

        row.pack(
            fill="x",
            padx=15,
            pady=(10, 10)
        )

        self.pdf_name = tk.Label(
            row,
            text="No PDF selected",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY,
            anchor="w"
        )

        self.pdf_name.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.browse_button = tk.Button(
            row,
            text="Browse",
            width=10,
            command=self._select_pdf,
            cursor="hand2"
        )

        self.browse_button.pack(side="right")


    def _create_password_section(self):
        card = tk.Frame(
            self.content_frame,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(10, 0)
        )

        title = tk.Label(
            card,
            text="Password Protection",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(11, 3)
        )

        description = tk.Label(
            card,
            text="Enter and confirm the password required to open the PDF.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        description.pack(
            anchor="w",
            padx=15
        )

        form_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        form_frame.pack(
            fill="x",
            padx=15,
            pady=(12, 6)
        )

        form_frame.grid_columnconfigure(
            1,
            weight=1
        )

        password_label = tk.Label(
            form_frame,
            text="Password",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )

        password_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 15),
            pady=(0, 8)
        )

        self.password_entry = tk.Entry(
            form_frame,
            show="•",
            font=Fonts.BODY,
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_PRIMARY,
            insertbackground=Colors.TEXT_PRIMARY,
            relief="flat",
            bd=0,
            highlightbackground=Colors.BORDER,
            highlightcolor=Colors.PRIMARY,
            highlightthickness=1
        )

        self.password_entry.grid(
            row=0,
            column=1,
            sticky="ew",
            ipady=5,
            pady=(0, 8)
        )

        confirm_label = tk.Label(
            form_frame,
            text="Confirm password",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )

        confirm_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(0, 15)
        )

        self.confirm_password_entry = tk.Entry(
            form_frame,
            show="•",
            font=Fonts.BODY,
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_PRIMARY,
            insertbackground=Colors.TEXT_PRIMARY,
            relief="flat",
            bd=0,
            highlightbackground=Colors.BORDER,
            highlightcolor=Colors.PRIMARY,
            highlightthickness=1
        )

        self.confirm_password_entry.grid(
            row=1,
            column=1,
            sticky="ew",
            ipady=5
        )

        options_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        options_frame.pack(
            fill="x",
            padx=15,
            pady=(2, 8)
        )

        self.show_password = tk.BooleanVar(value=False)

        self.show_password_checkbox = tk.Checkbutton(
            options_frame,
            text="Show passwords",
            variable=self.show_password,
            command=self._toggle_password_visibility,
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            activebackground=Colors.CARD,
            activeforeground=Colors.TEXT_PRIMARY,
            selectcolor=Colors.BACKGROUND,
            font=Fonts.SMALL,
            cursor="hand2"
        )

        self.show_password_checkbox.pack(
            side="left"
        )

        note_label = tk.Label(
            options_frame,
            text="Password required whenever the protected PDF is opened.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        note_label.pack(
            side="right"
        )

        self.validation_label = tk.Label(
            card,
            text="",
            bg=Colors.CARD,
            fg=Colors.ERROR,
            font=Fonts.SMALL,
            anchor="w"
        )


    def _create_action_section(self):
        action_frame = tk.Frame(
            self.content_frame,
            bg=Colors.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=(10, 2)
        )

        self.protect_button = tk.Button(
            action_frame,
            text="Protect PDF",
            width=20,
            command=self._process_pdf,
            cursor="hand2"
        )

        self.protect_button.config(
            state="disabled"
        )

        self.protect_button.pack()


    def _select_pdf(self):
        pass


    def _load_pdf_info(self):
        pass


    def _toggle_password_visibility(self):
        pass


    def _validate_settings(self):
        pass


    def _process_pdf(self):
        pass


    def _display_result(self, success):
        pass


    def _clear_selection(self):
        pass


    def _show_validation_message(self, message, color=Colors.ERROR):
        self.validation_label.config(
            text=message,
            fg=color
        )

        if not self.validation_label.winfo_manager():
            self.validation_label.pack(
                fill="x",
                padx=15,
                pady=(0, 8)
            )


    def _clear_validation_message(self):
        self.validation_label.config(text="")
        self.validation_label.pack_forget()


    def update_default_status(self):
        if not self.total_pages:
            self.status_label.config(
                text="Ready",
                fg=Colors.TEXT_SECONDARY
            )
            return

        page_text = "page" if self.total_pages == 1 else "pages"

        self.status_label.config(
            text=f"Selected PDF: {self.total_pages} {page_text}",
            fg=Colors.TEXT_SECONDARY
        )