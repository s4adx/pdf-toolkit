import tkinter as tk
from pathlib import Path
from ui.base_page import BasePage
from utils.constants import Colors, Fonts
from utils.file_dialog import select_pdf_file, select_save_path
from utils.helpers import count_pdf_pages
from backend.rotate import rotate_pdf

class RotatePage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.selected_file = None
        self.total_pages = 0

        self.create_header(
            title="Rotate PDF",
            subtitle="Rotate all pages, a single page, or a selected page range."
        )
        
        self._create_content_layout()
        self._create_file_section()
        self._create_rotate_mode_section()
        self._create_rotation_selection_section()
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
            pady=(8, 0)
        )

        self.top_frame = tk.Frame(
            self.content_frame,
            bg=Colors.BACKGROUND
        )

        self.top_frame.pack(fill="x")

        self.top_frame.grid_columnconfigure(
            0,
            weight=1,
            uniform="top_cards"
        )

        self.top_frame.grid_columnconfigure(
            1,
            weight=1,
            uniform="top_cards"
        )


    def _create_file_section(self):
        card = tk.Frame(
            self.top_frame,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 6)
        )

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
            pady=(14, 5)
        )

        description = tk.Label(
            card,
            text="Choose the PDF file you want to rotate.",
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
            pady=(18, 14)
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


    def _create_rotate_mode_section(self):
        card = tk.Frame(
            self.top_frame,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(6, 0)
        )

        title = tk.Label(
            card,
            text="Pages to Rotate",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=(14, 5)
        )

        self.rotate_mode = tk.StringVar(value="all")

        mode_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        mode_frame.pack(
            fill="x",
            padx=15,
            pady=(5, 5)
        )

        options = [
            ("All", "all"),
            ("Single", "single"),
            ("Range", "range")
        ]

        for column, (text, value) in enumerate(options):
            mode_frame.grid_columnconfigure(
                column,
                weight=1,
                uniform="modes"
            )

            radio_button = tk.Radiobutton(
                mode_frame,
                text=text,
                variable=self.rotate_mode,
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
                padx=5,
                pady=7,
                cursor="hand2",
                command=self._on_mode_change
            )

            radio_button.grid(
                row=0,
                column=column,
                sticky="ew",
                padx=(0 if column == 0 else 4, 0)
            )

        self.settings_body = tk.Frame(
            card,
            bg=Colors.CARD
        )

        self.settings_body.pack(
            fill="x",
            padx=15,
            pady=(10,8)
        )

        self.validation_label = tk.Label(
            card,
            text="",
            bg=Colors.CARD,
            fg=Colors.ERROR,
            font=Fonts.SMALL,
            anchor="w"
        )

        self.validation_label.pack(
            fill="x",
            padx=15,
            pady=(0,12)
        )

        self._update_settings_section()


    def _create_rotation_selection_section(self):
        card = tk.Frame(
            self.content_frame,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.pack(
            fill="x",
            pady=(12, 0)
        )

        self.setting_title = tk.Label(
            card,
            text="Rotation Angle",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        self.setting_title.pack(
            anchor="w",
            padx=15,
            pady=(14, 5)
        )

        self.setting_description = tk.Label(
            card,
            text="Choose the direction in which the selected pages should turn.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        self.setting_description.pack(
            anchor="w",
            padx=15
        )

        self.rotation_angle = tk.IntVar(value=90)

        angle_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        angle_frame.pack(
            fill="x",
            padx=15,
            pady=(14, 14)
        )

        options = [
            ("↻ Rotate Right 90°", 90),
            ("↕ Flip 180°", 180),
            ("↺ Rotate Left 90°", -90)
        ]

        for column, (text, value) in enumerate(options):
            angle_frame.grid_columnconfigure(
                column,
                weight=1,
                uniform="angles"
            )

            radio_button = tk.Radiobutton(
                angle_frame,
                text=text,
                variable=self.rotation_angle,
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
                padx=5,
                pady=8,
                cursor="hand2"
            )

            radio_button.grid(
                row=0,
                column=column,
                sticky="ew",
                padx=(0 if column == 0 else 4, 0)
            )


    def _create_action_section(self):
        action_frame = tk.Frame(
            self.content_frame,
            bg=Colors.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=(18, 8)
        )

        self.rotate_button = tk.Button(
            action_frame,
            text="Rotate PDF",
            width=20,
            command=self._process_pdf,
            cursor="hand2"
        )

        self.rotate_button.config(state="disabled")
        self.rotate_button.pack()   


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
            self.rotate_button.config(state="disabled")

            self._show_validation_message(
                f"Could not read the selected PDF: {error}"
            )

            return
        
        self._clear_validation_message()
        self._update_spinbox_ranges()
        self.update_default_status()

        self.rotate_button.config(state="normal")


    def _show_all_settings(self):
        message_label = tk.Label(
            self.settings_body,
            text="All pages in the PDF will be rotated.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )

        message_label.pack(anchor="w")


    def _show_single_settings(self):
        page_label = tk.Label(
            self.settings_body,
            text="Page number",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.BODY
        )

        page_label.pack(side="left")

        self.single_page_spinbox = tk.Spinbox(
            self.settings_body,
            from_=1,
            to=100,
            width=8,
            justify="center",
            font=Fonts.BODY
        )

        self.single_page_spinbox.pack(
            side="left",
            padx=(12, 0)
        )


    def _show_range_settings(self):
        start_label = tk.Label(
            self.settings_body,
            text="Start page",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.BODY
        )

        start_label.pack(side="left")

        self.start_page_spinbox = tk.Spinbox(
            self.settings_body,
            from_=1,
            to=100,
            width=8,
            justify="center",
            font=Fonts.BODY
        )

        self.start_page_spinbox.pack(
            side="left",
            padx=(12, 25)
        )

        end_label = tk.Label(
            self.settings_body,
            text="End page",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.BODY
        )

        end_label.pack(side="left")

        self.end_page_spinbox = tk.Spinbox(
            self.settings_body,
            from_=1,
            to=100,
            width=8,
            justify="center",
            font=Fonts.BODY
        )

        self.end_page_spinbox.pack(
            side="left",
            padx=(12, 0)
        )


    def _update_settings_section(self):
        for widget in self.settings_body.winfo_children():
            widget.destroy()

        selected_mode = self.rotate_mode.get()

        if selected_mode == "all":
            self._show_all_settings()
        
        elif selected_mode == "single":
            self._show_single_settings()

        else:
            self._show_range_settings()

        self._update_spinbox_ranges()


    def _on_mode_change(self):
        self._clear_validation_message()
        self._update_settings_section()
    

    def _update_spinbox_ranges(self):
        if not self.total_pages:
            return
        
        selected_mode = self.rotate_mode.get()

        if selected_mode == "single":
            self.single_page_spinbox.config(
                from_=1,
                to=self.total_pages
            )

        elif selected_mode == "range":
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
    
        selected_mode = self.rotate_mode.get()

        try:
            if selected_mode == "single":
                page_number = int(self.single_page_spinbox.get())

                if not 1 <= page_number <= self.total_pages:
                    self._show_validation_message(
                        f"Page number must be between 1 and {self.total_pages}."
                    )
                    return False

            elif selected_mode == "range":
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
        if not self._validate_settings():
            return
        
        selected_mode = self.rotate_mode.get()
        
        output_path = select_save_path(default_name=f"{Path(self.selected_file).stem}_rotated.pdf")

        if not output_path:
            self.update_status(
                "Operation cancelled",
                Colors.ERROR
            )
            return

        angle = self.rotation_angle.get()

        if selected_mode == "range":
            start_page = int(self.start_page_spinbox.get())
            end_page = int(self.end_page_spinbox.get())

            success = rotate_pdf(
                input_path=self.selected_file,
                output_path=output_path,
                rotation_angle=angle,
                page_mode="range",
                start_page=start_page,
                end_page=end_page
            )

        elif selected_mode == "single":
            single_page = int(self.single_page_spinbox.get())

            success = rotate_pdf(
                input_path=self.selected_file,
                output_path=output_path,
                rotation_angle=angle,
                page_mode="single",
                start_page=single_page
            )

        else:
            success = rotate_pdf(
                input_path=self.selected_file,
                output_path=output_path,
                rotation_angle=angle,
                page_mode="all"
            )

        self._display_result(success)


    def _display_result(self, success):
        if success:
            self._clear_selection()
            
            self.update_status(
                "PDF rotated successfully.", 
                Colors.SUCCESS
            )

        else:
            self.update_status(
                "Failed to rotate PDF.", 
                Colors.ERROR
            )


    def _clear_selection(self):
        self.selected_file = None
        self.total_pages = 0

        self.pdf_name.config(
            text="No PDF selected",
            fg=Colors.TEXT_SECONDARY
        )

        self.rotate_mode.set("all")
        self.rotation_angle.set(value=90)
        self._update_settings_section()

        self.rotate_button.config(state="disabled")

        self._clear_validation_message()
        self.update_default_status()

    
    def _show_validation_message(self, message, color=Colors.ERROR):
        self.validation_label.config(
            text=message,
            fg=color
        )


    def _clear_validation_message(self):
        self.validation_label.config(text="")

    
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