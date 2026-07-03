import tkinter as tk
from ui.page_manager import PageManager
from utils.constants import Window, Colors

class PDFToolkitApp:
    
    def __init__(self):
        self.root = tk.Tk()

        self._configure_window()
        self._create_page_container()
        self.page_manager = PageManager(self.page_container)

        
    def _configure_window(self):
        self.root.title(Window.TITLE)

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position to center the window
        x = (screen_width - Window.WIDTH) // 2
        y = (screen_height - Window.HEIGHT) // 2

        # Geometry format: (w)x(h)+(x)+(y)
        self.root.geometry(f"{Window.WIDTH}x{Window.HEIGHT}+{x}+{y}")

        self.root.resizable(False, False)  

        self.root.configure(bg=Colors.BACKGROUND)


    def _create_page_container(self):
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.page_container = tk.Frame(
            self.root,
            bg=Colors.BACKGROUND,
        )
        self.page_container.grid(row=0, column=0, sticky="nsew")


    def run(self):
        self.root.mainloop()