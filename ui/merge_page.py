import tkinter as tk
from pathlib import Path
from ui.base_page import BasePage
from utils.constants import Colors, Fonts
from utils.file_dialog import select_pdf_files, select_save_path
from backend.merge import merge_pdfs


class MergePage(BasePage):

    def __init__(self, parent, page_manager):
        super().__init__(parent, page_manager)

        self.selected_files = []

        self.create_header(
            title="Merge PDFs",
            subtitle="Combine multiple PDF files into one document."
        )

        self._create_content_layout()
        self._create_file_section()
        self._create_action_section()

        self.create_status_bar()

        self._refresh_files_list()
        self.update_default_status()

        self._bind_events()


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


    def _create_file_section(self):
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
            text="Selected PDF Files",
            bg=Colors.CARD,
            fg=Colors.TEXT_PRIMARY,
            font=Fonts.SUBHEADING
        )

        title.pack(anchor="w")

        description = tk.Label(
            title_frame,
            text="Add PDFs and arrange them in the required merge order.",
            bg=Colors.CARD,
            fg=Colors.TEXT_SECONDARY,
            font=Fonts.SMALL
        )

        description.pack(
            anchor="w",
            pady=(2, 0)
        )

        self.add_pdfs_button = tk.Button(
            header_frame,
            text="Add PDFs",
            width=12,
            command=self._add_pdfs,
            cursor="hand2"
        )

        self.add_pdfs_button.pack(
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

        self.file_listbox = tk.Listbox(
            list_frame,
            height=10,
            selectmode="extended",
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

        self.file_listbox.pack(
            side="left",
            fill="x",
            expand=True
        )

        scrollbar = tk.Scrollbar(
            list_frame,
            command=self.file_listbox.yview
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.file_listbox.config(
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

        self.remove_button.pack(
            side="left"
        )

        self.clear_button = tk.Button(
            controls_frame,
            text="Clear All",
            width=10,
            command=self._clear_files,
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

        self.move_down_button.pack(
            side="right"
        )

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



    def _create_action_section(self):
        action_frame = tk.Frame(
            self.content_frame,
            bg=Colors.BACKGROUND
        )

        action_frame.pack(
            fill="x",
            pady=(8, 1)
        )

        self.merge_button = tk.Button(
            action_frame,
            text="Merge PDFs",
            width=20,
            command=self._merge_pdfs,
            cursor="hand2"
        )

        self.merge_button.config(
            state="disabled"
        )

        self.merge_button.pack()


    def _bind_events(self):
        self.file_listbox.bind("<Delete>",lambda event: self._remove_selected())

        self.file_listbox.bind("<BackSpace>",lambda event: self._remove_selected())

        self.file_listbox.bind("<Control-a>",self._select_all)

        self.file_listbox.bind("<Control-A>",self._select_all)

        self.file_listbox.bind("<Control-Up>", lambda event: self._move_up())

        self.file_listbox.bind("<Control-Down>", lambda event: self._move_down())

        self.file_listbox.bind("<<ListboxSelect>>", lambda event: self._update_buttons())

        self.file_listbox.bind("<Escape>", self._clear_list_selection)


    def _add_pdfs(self):
        files = select_pdf_files()

        if not files:
            return

        for file in files:
            if file not in self.selected_files:
                self.selected_files.append(file)

        self._refresh_files_list()


    def _remove_selected(self):
        selection = self.file_listbox.curselection()

        if not selection:
            return

        for index in reversed(selection):
            if index < len(self.selected_files):
                self.selected_files.pop(index)

        self._refresh_files_list()


    def _clear_files(self):
        self.selected_files.clear()

        self._refresh_files_list()


    def _move_up(self):
        selection = self.file_listbox.curselection()

        if not selection:
            return

        index = selection[0]

        if index <= 0 or index >= len(self.selected_files):
            return

        self._swap_items(
            index,
            index - 1
        )

        self._refresh_files_list()
        self._refocus_listbox(index - 1)


    def _move_down(self):
        selection = self.file_listbox.curselection()

        if not selection:
            return

        index = selection[0]

        if index < 0 or index >= len(self.selected_files) - 1:
            return

        self._swap_items(
            index,
            index + 1
        )

        self._refresh_files_list()
        self._refocus_listbox(index + 1)


    def _swap_items(self, a, b):
        self.selected_files[a], self.selected_files[b] = (
            self.selected_files[b],
            self.selected_files[a]
        )


    def _refocus_listbox(self, new_index):
        self.file_listbox.selection_clear(0, tk.END)

        self.file_listbox.selection_set(new_index)
        self.file_listbox.activate(new_index)
        self.file_listbox.see(new_index)

        self.file_listbox.focus_set()

        self._update_buttons()


    def _clear_list_selection(self, event=None):
        self.file_listbox.selection_clear(0, tk.END)
        return "break"


    def _select_all(self, event=None):
        if not self.selected_files:
            return "break"

        self.file_listbox.selection_set(0, tk.END)
        return "break"


    def _refresh_files_list(self):
        self.file_listbox.delete(0, tk.END)

        for file in self.selected_files:
            self.file_listbox.insert(
                tk.END,
                Path(file).name
            )

        if not self.selected_files:
            self.file_listbox.insert(
                tk.END,
                "No PDF files selected."
            )

        self._update_buttons()
        self.update_default_status()


    def _update_buttons(self):
        selection = self.file_listbox.curselection()

        if len(self.selected_files) >= 2:
            self.merge_button.config(state="normal")
        else:
            self.merge_button.config(state="disabled")

        if self.selected_files:
            self.clear_button.config(state="normal")
        else:
            self.clear_button.config(state="disabled")

        if selection:
            self.remove_button.config(state="normal")
        else:
            self.remove_button.config(state="disabled")

        if not selection:
            self.move_up_button.config(state="disabled")

            self.move_down_button.config(state="disabled")

            return

        index = selection[0]

        if index > 0:
            self.move_up_button.config(
                state="normal"
            )
        else:
            self.move_up_button.config(
                state="disabled"
            )

        if index < len(self.selected_files) - 1:
            self.move_down_button.config(
                state="normal"
            )
        else:
            self.move_down_button.config(
                state="disabled"
            )


    def _merge_pdfs(self):
        if len(self.selected_files) < 2:
            self.update_status(
                "Select at least two PDF files.",
                Colors.WARNING
            )
            return

        save_path = select_save_path("merged.pdf")

        if not save_path:
            self.update_status(
                "Merge cancelled.",
                Colors.ERROR
            )
            return

        success = merge_pdfs(
            input_files=self.selected_files,
            output_path=save_path
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


    def _clear_selection(self):
        self.selected_files.clear()

        self._refresh_files_list()


    def update_default_status(self):
        count = len(self.selected_files)

        if count == 0:
            text = "Ready"

        elif count == 1:
            text = "Selected: 1 PDF"

        else:
            text = f"Selected: {count} PDFs"

        self.status_label.config(
            text=text,
            fg=Colors.TEXT_SECONDARY
        )