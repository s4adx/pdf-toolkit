import tkinter as tk
from utils.constants import Colors, Fonts

class ToolCard(tk.Frame):

    def __init__(self, parent, text, icon, command=None):
        super().__init__(parent)

        self.text = text
        self.icon = icon
        self.command = command
        
        self._configure_card()
        self._create_widgets()
        self._bind_events()

    
    def _configure_card(self):
        self.configure(
            width=160,
            height=130,
            bg=Colors.CARD,
            cursor="hand2",
            bd=0,
            highlightthickness=1,
            highlightbackground=Colors.BORDER,
            highlightcolor=Colors.PRIMARY
        )

        self.pack_propagate(False)
        self.grid_propagate(False)


    def _create_widgets(self):
        self.icon_label = tk.Label(
            self,
            text=self.icon,
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=("Segoe UI Emoji", 28)
        )

        self.text_label = tk.Label(
            self,
            text=self.text,
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        self.icon_label.pack(pady=(5, 0))
        self.text_label.pack(pady=(20, 0))
    

    def _bind_events(self):
        widgets = [
            self,
            self.icon_label,
            self.text_label
        ]

        for widget in widgets:
            widget.bind("<Button-1>", self._on_click)
            widget.bind("<Enter>", self._on_enter)
            widget.bind("<Leave>", self._on_leave)

    
    def _on_click(self, event):
        if self.command:
            self.command()

    
    def _on_enter(self, event):
        self.configure(bg=Colors.CARD_HOVER)
        self.icon_label.configure(bg=Colors.CARD_HOVER)
        self.text_label.configure(bg=Colors.CARD_HOVER)

    
    def _on_leave(self, event):
        self.configure(bg=Colors.CARD)
        self.icon_label.configure(bg=Colors.CARD)
        self.text_label.configure(bg=Colors.CARD)