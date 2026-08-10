import tkinter as tk
from pathlib import Path
from ui.base_page import BasePage
from utils.constants import Colors, Fonts
from utils.helpers import count_pdf_pages 
from utils.file_dialog import select_pdf_file, select_save_path

class PdfToImagesPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.selected_file = None
        self.total_pages = 0

        self.create_header(
            title="PDF to Images",
            subtitle="Convert PDF pages into individual image files."
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
            text="Choose the PDF that should be converted into images.",
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
            text="Export Settings",
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
            text="Choose the image format and PDF pages to export.",
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
            pady=(12, 8)
        )

        format_frame = tk.Frame(
            settings_frame,
            bg=Colors.CARD
        )

        format_frame.pack(
            fill="x",
            pady=(0, 10)
        )

        format_label = tk.Label(
            format_frame,
            text="Image format",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )

        format_label.pack(
            side="left",
            padx=(0, 15)
        )

        self.image_format = tk.StringVar(value="png")

        format_options = [
            ("PNG", "png"),
            ("JPG", "jpg")
        ]

        for text, value in format_options:
            radio_button = tk.Radiobutton(
                format_frame,
                text=text,
                variable=self.image_format,
                value=value,
                indicatoron=False,
                bg=Colors.BACKGROUND,
                fg=Colors.TEXT_PRIMARY,
                activebackground=Colors.CARD_HOVER,
                activeforeground=Colors.TEXT_PRIMARY,
                selectcolor=Colors.PRIMARY,
                font=Fonts.SMALL,
                relief="flat",
                bd=0,
                padx=18,
                pady=6,
                cursor="hand2"
            )

            radio_button.pack(
                side="left",
                padx=(0, 6)
            )

        selection_frame = tk.Frame(
            settings_frame,
            bg=Colors.CARD
        )

        selection_frame.pack(fill="x")

        selection_label = tk.Label(
            selection_frame,
            text="Pages",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )

        selection_label.pack(
            side="left",
            padx=(0, 15)
        )

        self.page_mode = tk.StringVar(value="all")

        page_options = [
            ("All Pages", "all"),
            ("Page Range", "range")
        ]

        for text, value in page_options:
            radio_button = tk.Radiobutton(
                selection_frame,
                text=text,
                variable=self.page_mode,
                value=value,
                indicatoron=False,
                bg=Colors.BACKGROUND,
                fg=Colors.TEXT_PRIMARY,
                activebackground=Colors.CARD_HOVER,
                activeforeground=Colors.TEXT_PRIMARY,
                selectcolor=Colors.PRIMARY,
                font=Fonts.SMALL,
                relief="flat",
                bd=0,
                padx=18,
                pady=6,
                cursor="hand2",
                command=self._on_mode_change
            )

            radio_button.pack(
                side="left",
                padx=(0, 6)
            )

        self.range_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        self.range_frame.pack(
            fill="x",
            padx=15,
            pady=(2, 8)
        )

        self.validation_label = tk.Label(
            card,
            text="",
            bg=Colors.CARD,
            fg=Colors.ERROR,
            font=Fonts.SMALL,
            anchor="w"
        )

        self._update_range_section()


    def _create_action_section(self):
        action_frame = tk.Frame(
            self.content_frame,
            bg=Colors.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=(10, 2)
        )

        self.convert_button = tk.Button(
            action_frame,
            text="Convert to Images",
            width=20,
            command=self._process_pdf,
            cursor="hand2"
        )

        self.convert_button.config(
            state="disabled"
        )

        self.convert_button.pack()


    def _update_range_section(self):
        for widget in self.range_frame.winfo_children():
            widget.destroy()

        if self.page_mode.get() == "all":
            message = tk.Label(
                self.range_frame,
                text="All PDF pages will be exported.",
                bg=Colors.CARD,
                fg=Colors.TEXT_SECONDARY,
                font=Fonts.SMALL
            )

            message.pack(anchor="w")

        else:
            start_label = tk.Label(
                self.range_frame,
                text="Start page",
                bg=Colors.CARD,
                fg=Colors.TEXT_PRIMARY,
                font=Fonts.BODY
            )

            start_label.pack(side="left")

            self.start_page_spinbox = tk.Spinbox(
                self.range_frame,
                from_=1,
                to=100,
                width=8,
                justify="center",
                font=Fonts.BODY
            )

            self.start_page_spinbox.pack(
                side="left",
                padx=(10, 22)
            )

            end_label = tk.Label(
                self.range_frame,
                text="End page",
                bg=Colors.CARD,
                fg=Colors.TEXT_PRIMARY,
                font=Fonts.BODY
            )

            end_label.pack(side="left")

            self.end_page_spinbox = tk.Spinbox(
                self.range_frame,
                from_=1,
                to=100,
                width=8,
                justify="center",
                font=Fonts.BODY
            )

            self.end_page_spinbox.pack(
                side="left",
                padx=(10, 0)
            )

            self._update_spinbox_ranges()


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
            self.convert_button.config(state="disabled")

            self._show_validation_message(
                f"Could not read the selected PDF: {error}"
            )

            return

        self._clear_validation_message()
        self._update_spinbox_ranges()
        self.update_default_status()

        self.convert_button.config(state="normal")


    def _on_mode_change(self):
        self._clear_validation_message()
        self._update_range_section()


    def _update_spinbox_ranges(self):
        if not self.total_pages:
            return
        
        selected_mode = self.page_mode.get()


        if selected_mode == "range":
            self.start_page_spinbox.config(to=self.total_pages)
            self.end_page_spinbox.config(to=self.total_pages)

            self.end_page_spinbox.delete(0, tk.END)
            self.end_page_spinbox.insert(0, str(self.total_pages))



    def _validate_settings(self):
        if not self.selected_file:
            self._show_validation_message(
                "Please select a PDF file."
            )
            return False

        if self.image_format.get() not in ("png", "jpg"):
            self._show_validation_message(
                "Select a valid image format."
            )
            return False

        if self.page_mode.get() == "range":
            try: 
                start_page = int(self.start_page_spinbox.get())
                end_page = int(self.end_page_spinbox.get())

                if not 1 <= start_page <= self.total_pages:
                    self._show_validation_message(
                        f"Start page must be between 1 and {self.total_pages}."
                    )
                    return False

                if not 1 <= end_page <= self.total_pages:
                    self._show_validation_message(
                        f"End page must be between 1 and {self.total_pages}."
                    )
                    return False

                if start_page > end_page:
                    self._show_validation_message(
                        "Start page cannot be greater than end page."
                    )
                    return False

            except ValueError:
                self._show_validation_message(
                    "Page values must be whole numbers."
                )
                return False
    
        self._clear_validation_message()
    
        return True


    def _process_pdf(self):
        pass


    def _display_result(self, success):
        pass


    def _clear_selection(self):
        pass


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

        page_text = ("page" if self.total_pages == 1 else "pages")

        self.status_label.config(
            text=f"Selected PDF: {self.total_pages} {page_text}",
            fg=Colors.TEXT_SECONDARY
        )