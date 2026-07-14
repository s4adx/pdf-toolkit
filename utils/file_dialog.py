from tkinter import filedialog
import os


def select_pdf_files():
    file_paths = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_paths:
        return list(file_paths)
    
    else:
        return
    
    
def select_pdf_file():
    file_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF File", "*.pdf")]
    )

    if file_path:
        return file_path
    
    else:
        return
    

def select_save_path():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")  # Find system's default Downloads folder
    file_path = filedialog.asksaveasfilename(
        initialdir=downloads_folder,
        title="Save PDF File",
        initialfile="merged.pdf",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )

    if file_path:
        return file_path
    

def save_pdf():
    pass