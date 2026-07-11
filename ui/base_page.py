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


        subtitle_label = tk.Label(
            self.header_frame,
            text=subtitle,
            bg=Colors.BACKGROUND,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.BODY
        )
        subtitle_label.grid(row=2, column=0, columnspan=2, sticky="w")


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

        self.bind_header_events()

    
    def bind_header_events(self):
        self.header_widgets = [
            self.back_arrow,
            self.back
        ]

        for widget in self.header_widgets:
            widget.bind("<Button-1>", self._on_back_click)
            widget.bind("<Enter>", self._on_back_enter)
            widget.bind("<Leave>", self._on_back_leave)

    
    def _on_back_click(self, event):
        self.page_manager.show_page("home")


    def _on_back_enter(self, event):
        self.back_arrow.config(fg=Colors.PRIMARY, cursor="hand2")
        self.back.config(fg=Colors.PRIMARY, cursor="hand2")
    

    def _on_back_leave(self, event):
        self.back_arrow.config(fg=Colors.TEXT_PRIMARY)
        self.back.config(fg=Colors.TEXT_PRIMARY)


    def create_status_bar(self):

        self.status_timer = None

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
        
    
    def update_status(self, message, color=Colors.TEXT_SECONDARY):

        self.status_label.config(text=message, fg=color)

        # Cancel the previous timer (if one exists)
        if self.status_timer is not None:
            self.after_cancel(self.status_timer)
        
        # Start a new timer
        self.status_timer = self.after(
            3000,
            self.update_default_status
        )


    def update_default_status(self):
        self.status_label.config(
            text="Ready",
            fg=Colors.TEXT_SECONDARY
        )