import os
from pathlib import Path
from tkinter import filedialog, simpledialog, messagebox


def select_pdf_files():
    file_paths = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_paths:
        return list(file_paths)
    

def select_pdf_file():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF File", "*.pdf")]
    )

    if file_path:
        return file_path
    

def select_save_path(default_name):
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")  # Find system's default Downloads folder
    file_path = filedialog.asksaveasfilename(
        initialdir=downloads_folder,
        title="Save PDF File",
        initialfile=default_name,
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )

    if file_path:
        return file_path


def create_output_folder(default_name="output"):
    parent_folder = filedialog.askdirectory(
        title="Choose Where to Save the Output Folder"
    )

    if not parent_folder:
        return 

    folder_name = simpledialog.askstring(
        title="Output Folder Name",
        prompt="Enter the name of the new output folder:",
        initialvalue=default_name
    )

    if not folder_name:
        return
    
    output_folder = Path(parent_folder) / folder_name.strip()

    if output_folder.exists():
        messagebox.showerror(
            "Folder Already Exists",
            "A folder with this name already exists.\nPlease choose another name."
        )
        return 
    
    try:
        output_folder.mkdir()
        return str(output_folder)

    except OSError:
        messagebox.showerror(
            "Folder Creation Failed",
            "The output folder could not be created"
        )
        return 


def save_pdf():
    pass