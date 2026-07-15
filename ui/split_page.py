import tkinter as tk
from pathlib import Path
from ui.base_page import BasePage
from utils.constants import Colors, Fonts 
from utils.file_dialog import select_pdf_file, create_output_folder, select_save_path
from utils.helpers import count_pdf_pages
from backend.split import split_pdf, extract_pages, split_every_page


class SplitPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.selected_file = None
        self.total_pages = 0

        self.create_header(
            title="Split PDF",
            subtitle="Split a PDF by page, extract a page range, or split every page."
        )

        self._create_content_layout()

        self._create_file_section()
        self._create_split_mode_section()
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
            text="Choose the PDF file you want to split.",
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
            command=self._select_pdf
        )

        self.browse_button.pack(side="right")


    def _create_split_mode_section(self):
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
            text="Split Mode",
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
            text="Select how the PDF should be divided.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        description.pack(
            anchor="w",
            padx=15
        )

        self.split_mode = tk.StringVar(value="split")

        mode_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        mode_frame.pack(
            fill="x",
            padx=15,
            pady=(18, 14)
        )

        options = [
            ("Split", "split"),
            ("Extract", "extract"),
            ("Every Page", "every")
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
                variable=self.split_mode,
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


    def _create_settings_section(self):
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
            text="",
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
            text="",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        self.setting_description.pack(
            anchor="w",
            padx=15
        )

        self.settings_body = tk.Frame(
            card,
            bg=Colors.CARD
        )

        self.settings_body.pack(
            fill="x",
            padx=15,
            pady=(14, 8)
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
            pady=(0, 12)
        )

        self._update_settings_section()
        
    
    def _create_action_section(self):
        action_frame = tk.Frame(
            self.content_frame,
            bg=Colors.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=(18, 8)
        )

        self.split_button = tk.Button(
            action_frame,
            text="Split PDF",
            width=20,
            command=self._process_pdf
        )

        self.split_button.config(state="disabled")
        self.split_button.pack()    

    
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
            self.split_button.config(state="disabled")

            self._show_validation_message(
                f"Could not read the selected PDF: {error}"
            )
            return

        self._clear_validation_message()
        self._update_spinbox_ranges()
        self.update_default_status()

        self.split_button.config(state="normal")


    def _update_spinbox_ranges(self):
        if not self.total_pages:
            return
        
        selected_mode = self.split_mode.get()

        if selected_mode == "split":
            if self.total_pages < 2:
                self.split_page_spinbox.config(
                    from_=1,
                    to=1,
                    state="disabled"
                )
            else:
                self.split_page_spinbox.config(
                    from_=1,
                    to=self.total_pages - 1,
                    state="normal"
                )

        elif selected_mode == "extract":
            self.start_page_spinbox.config(to=self.total_pages)
            self.end_page_spinbox.config(to=self.total_pages)

            self.end_page_spinbox.delete(0, tk.END)
            self.end_page_spinbox.insert(0, str(self.total_pages))

    
    def _update_action_button(self):
        selected_mode = self.split_mode.get()

        button_text = {
            "split": "Split PDF",
            "extract": "Extract PDF",
            "every": "Split Every Page"
        }

        self.split_button.config(text=button_text[selected_mode])

    
    def _on_mode_change(self):
        self._clear_validation_message()
        self._update_settings_section()
        self._update_action_button()


    def _update_settings_section(self):
        for widget in self.settings_body.winfo_children():
            widget.destroy()

        selected_mode = self.split_mode.get()

        if selected_mode == "split":
            self._show_split_settings()
        
        elif selected_mode == "extract":
            self._show_extract_settings()

        else:
            self._show_every_page_settings()

        self._update_spinbox_ranges()


    def _show_split_settings(self):
        self.setting_title.config(text="Split After Page")

        self.setting_description.config(text="Choose the page after which the PDF should be split.")

        page_label = tk.Label(
            self.settings_body,
            text="Page number",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.BODY
        )

        page_label.pack(side="left")

        self.split_page_spinbox = tk.Spinbox(
            self.settings_body,
            from_=1,
            to=100,
            width=8,
            justify="center",
            font=Fonts.BODY
        )

        self.split_page_spinbox.pack(
            side="left",
            padx=(12, 15)
        )

        helper_label = tk.Label(
            self.settings_body,
            text="Example: 10 creates pages 1–10 and 11–end.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        helper_label.pack(side="left")


    def _show_extract_settings(self):
        self.setting_title.config(text="Extract Page Range")
        self.setting_description.config(text="Enter the starting and ending pages to extract.")

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


    def _show_every_page_settings(self):
        self.setting_title.config(
            text="Split Every Page"
        )

        self.setting_description.config(
            text="Each page will be saved as an individual PDF file."
        )

        message_label = tk.Label(
            self.settings_body,
            text="No additional settings are required.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )

        message_label.pack(anchor="w")

    
    def _validate_settings(self):
        if not self.selected_file:
            self._show_validation_message("Please select a PDF file.")
            return False
        
        selected_mode = self.split_mode.get()

        try:
            if selected_mode == "split":
                if self.total_pages < 2:
                    self._show_validation_message(
                        "This PDF must have at least 2 pages to be split."
                    )
                    return False

                split_page = int(self.split_page_spinbox.get())

                if not 1 <= split_page < self.total_pages:
                    self._show_validation_message(
                        f"Split page must be between 1 and {self.total_pages - 1}."
                    )
                    return False
                
            elif selected_mode == "extract":
                start_page = int(self.start_page_spinbox.get())
                end_page = int(self.end_page_spinbox.get())

                if not 1 <= start_page <= self.total_pages:
                    self._show_validation_message(
                        f"Start page must be between 1 and {self.total_pages}."
                    )
                    return False

                if start_page > end_page:
                    self._show_validation_message(
                        "Start page must be less than the end page."
                    )
                    return False      
                  
                if not start_page <= end_page <= self.total_pages:
                    self._show_validation_message(
                        f"End page must be between {start_page} and {self.total_pages}."
                    )
                    return False
                          
        except ValueError:
            self._show_validation_message("Page values must be whole numbers.")
            return False
        
        self._clear_validation_message()
        return True
    

    def _process_pdf(self):
        if not self._validate_settings():
            return
        
        selected_mode = self.split_mode.get()

        if selected_mode == "split":
            output_folder = create_output_folder(default_name=f"{Path(self.selected_file).stem}_split")
        
            if not output_folder:
                self.update_status(
                    "Operation cancelled",
                    Colors.ERROR
                )
                return

            split_page = int(self.split_page_spinbox.get())

            success = split_pdf(
                input_path=self.selected_file,
                split_page=split_page,
                output_folder=output_folder
            )

            if success:
                self._clear_selection()
                
                self.update_status(
                    "PDF split successfully.", 
                    Colors.SUCCESS
                )

            else:
                self.update_status(
                    "Failed to split PDF.", 
                    Colors.ERROR
                )

        elif selected_mode == "extract":
            save_path = select_save_path(default_name="extracted.pdf")

            if not save_path:
                self.update_status(
                    "Operation cancelled",
                    Colors.ERROR
                )
                return
            
            start_page = int(self.start_page_spinbox.get())
            end_page = int(self.end_page_spinbox.get())

            success = extract_pages(
                input_path=self.selected_file,
                start_page=start_page,
                end_page=end_page,
                output_path=save_path
            )

            if success:
                self._clear_selection()

                self.update_status(
                    "Extracted page range successfully.", 
                    Colors.SUCCESS
                )

            else:
                self.update_status(
                    "Failed to extract page range.", 
                    Colors.ERROR
                )

        else:
            output_folder = create_output_folder(default_name=f"{Path(self.selected_file).stem}_pages")
            
            if not output_folder:
                self.update_status(
                    "Operation cancelled",
                    Colors.ERROR
                )
                return
            
            success = split_every_page(
                input_path=self.selected_file,
                output_folder=output_folder
            )

            if success:
                self._clear_selection()

                self.update_status(
                    "PDF split into separate pages successfully.", 
                    Colors.SUCCESS
                )

            else:
                self.update_status(
                    "Failed to split PDF into separate pages.", 
                    Colors.ERROR
                )
    

    def _clear_selection(self):
        self.selected_file = None
        self.total_pages = 0

        self.pdf_name.config(
            text="No PDF selected",
            fg=Colors.TEXT_SECONDARY
        )

        self.split_mode.set("split")
        self._update_settings_section()

        self.split_button.config(
            text="Split PDF",
            state="disabled"
        )

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