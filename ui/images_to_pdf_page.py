import tkinter as tk

from ui.base_page import BasePage
from utils.constants import Colors, Fonts


class ImagesToPdfPage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.selected_images = []

        self.create_header(
            title="Images to PDF",
            subtitle="Combine multiple images into a single PDF in the preferred order."
        )

        self._create_content_layout()
        self._create_images_section()
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
            pady=(4, 0)
        )


    def _create_images_section(self):
        card = tk.Frame(
            self.content_frame,
            bg=Colors.CARD,
            highlightbackground=Colors.BORDER,
            highlightthickness=1
        )

        card.pack(fill="x")

        header_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        header_frame.pack(
            fill="x",
            padx=15,
            pady=(9, 4)
        )

        title_frame = tk.Frame(
            header_frame,
            bg=Colors.CARD
        )

        title_frame.pack(
            side="left",
            fill="x",
            expand=True
        )

        title = tk.Label(
            title_frame,
            text="Selected Images",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(anchor="w")

        description = tk.Label(
            title_frame,
            text="Add images and arrange them in the required PDF page order.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        description.pack(
            anchor="w",
            pady=(2, 0)
        )

        self.add_images_button = tk.Button(
            header_frame,
            text="Add Images",
            width=12,
            command=self._add_images,
            cursor="hand2"
        )

        self.add_images_button.pack(
            side="right",
            padx=(10, 0)
        )

        list_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        list_frame.pack(
            fill="x",
            padx=15,
            pady=(4, 6)
        )

        self.images_listbox = tk.Listbox(
            list_frame,
            height=6,
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_PRIMARY,
            selectbackground=Colors.PRIMARY,
            selectforeground=Colors.TEXT_PRIMARY,
            font=Fonts.BODY,
            relief="flat",
            bd=0,
            highlightbackground=Colors.BORDER,
            highlightcolor=Colors.PRIMARY,
            highlightthickness=1,
            activestyle="none",
            exportselection=False
        )

        self.images_listbox.pack(
            side="left",
            fill="x",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            list_frame,
            command=self.images_listbox.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.images_listbox.config(
            yscrollcommand=scrollbar.set
        )

        controls_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        controls_frame.pack(
            fill="x",
            padx=15,
            pady=(0, 8)
        )

        self.remove_button = tk.Button(
            controls_frame,
            text="Remove Selected",
            width=15,
            command=self._remove_selected,
            cursor="hand2"
        )

        self.remove_button.pack(side="left")

        self.clear_button = tk.Button(
            controls_frame,
            text="Clear All",
            width=10,
            command=self._clear_images,
            cursor="hand2"
        )

        self.clear_button.pack(
            side="left",
            padx=(8, 0)
        )

        self.move_down_button = tk.Button(
            controls_frame,
            text="Move Down",
            width=11,
            command=self._move_down,
            cursor="hand2"
        )

        self.move_down_button.pack(side="right")

        self.move_up_button = tk.Button(
            controls_frame,
            text="Move Up",
            width=11,
            command=self._move_up,
            cursor="hand2"
        )

        self.move_up_button.pack(
            side="right",
            padx=(0, 8)
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
            pady=(8, 0)
        )

        header_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        header_frame.pack(
            fill="x",
            padx=15,
            pady=(8, 5)
        )

        title = tk.Label(
            header_frame,
            text="PDF Settings",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(side="left")

        description = tk.Label(
            header_frame,
            text="Choose the page format and orientation.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        description.pack(
            side="left",
            padx=(14, 0)
        )

        settings_frame = tk.Frame(
            card,
            bg=Colors.CARD
        )

        settings_frame.pack(
            fill="x",
            padx=15,
            pady=(2, 8)
        )

        settings_frame.grid_columnconfigure(
            0,
            weight=1,
            uniform="settings"
        )

        settings_frame.grid_columnconfigure(
            1,
            weight=1,
            uniform="settings"
        )

        page_size_frame = tk.Frame(
            settings_frame,
            bg=Colors.CARD
        )

        page_size_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(0, 8)
        )

        page_size_label = tk.Label(
            page_size_frame,
            text="Page size",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        page_size_label.pack(
            side="left",
            padx=(0, 10)
        )

        self.page_size = tk.StringVar(value="image")

        page_size_options = [
            ("Fit to Image", "image"),
            ("A4", "a4")
        ]

        for text, value in page_size_options:
            radio_button = tk.Radiobutton(
                page_size_frame,
                text=text,
                variable=self.page_size,
                value=value,
                bg=Colors.CARD,
                fg=Colors.TEXT_PRIMARY,
                activebackground=Colors.CARD,
                activeforeground=Colors.TEXT_PRIMARY,
                selectcolor=Colors.BACKGROUND,
                font=Fonts.SMALL,
                cursor="hand2"
            )

            radio_button.pack(
                side="left",
                padx=(0, 8)
            )

        orientation_frame = tk.Frame(
            settings_frame,
            bg=Colors.CARD
        )

        orientation_frame.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(8, 0)
        )

        orientation_label = tk.Label(
            orientation_frame,
            text="Orientation",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        orientation_label.pack(
            side="left",
            padx=(0, 10)
        )

        self.orientation = tk.StringVar(value="auto")

        orientation_options = [
            ("Auto", "auto"),
            ("Portrait", "portrait"),
            ("Landscape", "landscape")
        ]

        for text, value in orientation_options:
            radio_button = tk.Radiobutton(
                orientation_frame,
                text=text,
                variable=self.orientation,
                value=value,
                bg=Colors.CARD,
                fg=Colors.TEXT_PRIMARY,
                activebackground=Colors.CARD,
                activeforeground=Colors.TEXT_PRIMARY,
                selectcolor=Colors.BACKGROUND,
                font=Fonts.SMALL,
                cursor="hand2"
            )

            radio_button.pack(
                side="left",
                padx=(0, 6)
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
            pady=(8, 1)
        )

        self.create_pdf_button = tk.Button(
            action_frame,
            text="Create PDF",
            width=20,
            command=self._process_images,
            cursor="hand2"
        )

        self.create_pdf_button.config(
            state="disabled"
        )

        self.create_pdf_button.pack()


    def _add_images(self):
        pass


    def _remove_selected(self):
        pass


    def _clear_images(self):
        pass


    def _move_up(self):
        pass


    def _move_down(self):
        pass


    def _refresh_images_list(self):
        pass


    def _validate_settings(self):
        pass


    def _process_images(self):
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
                pady=(0, 6)
            )


    def _clear_validation_message(self):
        self.validation_label.config(text="")
        self.validation_label.pack_forget()


    def update_default_status(self):
        image_count = len(self.selected_images)

        if image_count == 0:
            self.status_label.config(
                text="Ready",
                fg=Colors.TEXT_SECONDARY
            )
            return

        image_text = (
            "image"
            if image_count == 1
            else "images"
        )

        self.status_label.config(
            text=f"Selected: {image_count} {image_text}",
            fg=Colors.TEXT_SECONDARY
        )