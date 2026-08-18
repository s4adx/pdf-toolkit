import tkinter as tk
from pathlib import Path
from ui.base_page import BasePage
from utils.constants import Colors, Fonts
from utils.file_dialog import select_pdf_file, select_save_path
from utils.helpers import count_pdf_pages
from backend.compress import compress_pdf

class CompressPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.selected_file = None
        self.total_pages = 0

        self.create_header( 
            title="Compress PDF",
            subtitle="Reduce PDF file size while maintaining useful document quality."
        )

        self._create_content_layout()
        self._create_file_section()
        self._create_settings_section()
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
            text="Choose the PDF that should be compressed.",
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


    def _create_settings_section(self):
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
            text="Compression Settings",
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
            text="Choose how strongly the PDF should be compressed.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        description.pack(
            anchor="w",
            padx=15
        )

        settings_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        settings_frame.pack(
            fill="x",
            padx=15,
            pady=(12, 10)
        )

        level_label = tk.Label(
            settings_frame,
            text="Compression level",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )

        level_label.pack(
            anchor="w",
            pady=(0, 8)
        )

        self.compression_level = tk.StringVar(value="recommended")

        options_frame = tk.Frame(
            settings_frame,
            bg=Colors.CARD
        )

        options_frame.pack(
            fill="x"
        )

        compression_options = [
            (
                "Low",
                "low",
                "Better quality with less size reduction."
            ),
            (
                "Recommended",
                "recommended",
                "Balanced file size and quality."
            ),
            (
                "High",
                "high",
                "Smaller file size with greater compression."
            )
        ]

        for text, value, description_text in compression_options:

            option_frame = tk.Frame(
                options_frame,
                bg=Colors.CARD
            )

            option_frame.pack(
                side="left",
                fill="x",
                expand=True,
                padx=(0, 8)
            )

            radio_button = tk.Radiobutton(
                option_frame,
                text=text,
                variable=self.compression_level,
                value=value,
                bg=Colors.CARD,
                fg=Colors.TEXT_PRIMARY,
                activebackground=Colors.CARD,
                activeforeground=Colors.TEXT_PRIMARY,
                selectcolor=Colors.BACKGROUND,
                font=Fonts.BODY,
                cursor="hand2"
            )

            radio_button.pack(
                anchor="w"
            )

            description_label = tk.Label(
                option_frame,
                text=description_text,
                bg=Colors.CARD,
                fg=Colors.TEXT_SECONDARY,
                font=Fonts.SMALL,
                wraplength=180,
                justify="left"
            )

            description_label.pack(
                anchor="w",
                pady=(2, 0)
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

        self.compress_button = tk.Button(
            action_frame,
            text="Compress PDF",
            width=20,
            command=self._process_pdf,
            cursor="hand2"
        )

        self.compress_button.config(
            state="disabled"
        )

        self.compress_button.pack()


    def _select_pdf(self):
        file = select_pdf_file()

        if not file:
            return

        self.selected_file = file
        self.pdf_name.config(text=Path(file).name)

        self._load_pdf_info()


    def _load_pdf_info(self):
        try:
            self.total_pages = count_pdf_pages(self.selected_file)

        except (ValueError, OSError) as error:
            self.selected_file = None
            self.total_pages = 0

            self.pdf_name.config(text="No PDF selected")
            self.compress_button.config(state="disabled")

            self._show_validation_message(
                f"Could not read the selected PDF: {error}"
            )

            return

        self._clear_validation_message()
        self.update_default_status()

        self.compress_button.config(state="normal")


    def _validate_settings(self):
        if not self.selected_file:
            self._show_validation_message(
                "Please select a PDF file."
            )
            return False

        if self.compression_level.get() not in ("low", "recommended", "high"):
            self._show_validation_message(
                "Select a valid compression level."
            )
            return False

        self._clear_validation_message()

        return True
            

    def _process_pdf(self):
        if not self._validate_settings():
            return

        selected_level = self.compression_level.get()

        output_path = select_save_path(default_name=f"{Path(self.selected_file).stem}_compressed.pdf")

        if not output_path:
            self.update_status(
                "Operation cancelled",
                Colors.ERROR
            )
            return

        success = compress_pdf(
            input_path=self.selected_file,
            output_path=output_path,
            compression_level=selected_level
        )

        self._display_result(success)


    def _display_result(self, success):
        if success:
            self._clear_selection()
    
            self.update_status(
                "PDF compressed successfully.", 
                Colors.SUCCESS
            )
    
        else:
            self.update_status(
                "Failed to compress the PDF.", 
                Colors.ERROR
            )


    def _clear_selection(self):
        self.selected_file = None
        self.total_pages = 0

        self.pdf_name.config(
            text="No PDF selected",
            fg=Colors.TEXT_SECONDARY
        )

        self.compression_level.set("recommended")
        self.compress_button.config(state="disabled")

        self._clear_validation_message()
        self.update_default_status()
        

    def _show_validation_message(
        self,
        message,
        color=Colors.ERROR
    ):
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

        page_text = (
            "page"
            if self.total_pages == 1
            else "pages"
        )

        self.status_label.config(
            text=f"Selected PDF: {self.total_pages} {page_text}",
            fg=Colors.TEXT_SECONDARY
        )