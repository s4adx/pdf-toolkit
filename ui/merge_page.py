import tkinter as tk
from pathlib import Path
from ui.base_page import BasePage
from utils.constants import Colors, Fonts
from utils.file_dialog import select_pdf_files, select_save_path
from backend.merge import merge_pdfs


class MergePage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.create_header(
            title="Merge PDFs",
            subtitle="Combine multiple PDF files into one document."
        )

        self._create_file_section()
        self._create_buttons()
        self._create_action_section()

        self.create_status_bar()
        
        self.selected_files = []

        self.update_default_status()


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
            command=self._add_pdfs
        )

        self.add_button.pack(
            side="left"
        )


        self.remove_button = tk.Button(
            button_frame,
            text="Remove Selected",
            width=15,
            command=self._remove_selected
        )
        self.remove_button.config(state="disabled")
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
            command=self._merge_pdfs
        )
        self.merge_button.config(state="disabled")
        self.merge_button.pack()

    
    def _add_pdfs(self):
        files = select_pdf_files() 

        self._add_selected_files(files)


    def _add_selected_files(self, files):
        if not files:
            return

        self.selected_files.extend(files)
        self._update_ui()
        self.update_default_status()


    def _update_listbox(self):
        self.file_listbox.delete(0, tk.END)

        for file in self.selected_files:
            self.file_listbox.insert(tk.END, Path(file).name)

        if not self.selected_files:
            self.file_listbox.insert(tk.END, "No PDF files selected.")


    def _remove_selected(self):
        selection = self.file_listbox.curselection()

        if not selection:
            return

        index = selection[0]

        if index >= len(self.selected_files):
            return

        self.selected_files.pop(index) 
        self._update_ui()
        self.update_default_status()


    def _merge_pdfs(self):
        if len(self.selected_files) < 2:
            self.update_status(
                "Select at least two PDF files",
                Colors.WARNING
            )
            return
        
        save_path = select_save_path()

        if not save_path:
            self.update_status(
                "Merge cancelled",
                Colors.ERROR
            )
            return
        

        success = merge_pdfs(
            self.selected_files,
            save_path
        )

        if success:
            self.update_status(
                "PDFs merged successfully.", 
                Colors.SUCCESS
            )
            self._clear_selection()
            

        else:
            self.update_status(
                "Failed to merge PDFs.", 
                Colors.ERROR
            )


    def update_default_status(self):
        count = len(self.selected_files)

        if count == 0:
            text = "Ready"
        elif count == 1:
            text = "1 PDF selected"
        else:
            text = f"{count} PDFs selected"

        self.status_label.config(
            text=text,
            fg=Colors.TEXT_SECONDARY
        )
            
    
    def _clear_selection(self):
        self.selected_files.clear()

        self._update_ui()


    def _update_buttons(self):
        if len(self.selected_files) >= 2:
            self.merge_button.config(state="normal")
        else:
            self.merge_button.config(state="disabled")

        if self.selected_files:
            self.remove_button.config(state="normal")
        else:
            self.remove_button.config(state="disabled")


    def _update_ui(self):
        self._update_listbox()
        self._update_buttons()
