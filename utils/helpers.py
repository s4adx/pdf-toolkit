from pypdf import PdfReader
from pypdf.errors import PdfReadError


def count_pdf_pages(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        return len(reader.pages)
    
    except PdfReadError as error:
        raise ValueError(f"Could not read PDF: {pdf_path}") from error