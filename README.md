# PDF Toolkit

A desktop PDF utility application built with Python and Tkinter for performing common PDF operations through a simple and user-friendly interface.

## Features

PDF Toolkit currently supports:

- **Merge PDFs** — Combine multiple PDF files into a single document.
- **Split PDF** — Split a PDF after a selected page.
- **Extract Pages** — Extract a selected range of pages into a new PDF.
- **Split Every Page** — Save each PDF page as an individual PDF file.
- **Rotate PDF** — Rotate selected PDF pages.
- **Delete Pages** — Remove selected pages from a PDF.
- **Images to PDF** — Combine multiple images into a single PDF.
- **PDF to Images** — Convert PDF pages into image files.
- **Compress PDF** — Reduce PDF file size using different compression levels.
- **Protect PDF** — Protect PDF files with password-based encryption.

## Tech Stack

- **Python**
- **Tkinter** — Desktop graphical user interface
- **pypdf** — PDF manipulation
- **PyMuPDF** — PDF rendering and image-related operations
- **Pillow** — Image processing

## Project Structure

```text
pdf-toolkit/
│
├── backend/
│   ├── compress.py
│   ├── delete.py
│   ├── images_to_pdf.py
│   ├── merge.py
│   ├── pdf_to_images.py
│   ├── protect.py
│   ├── rotate.py
│   └── split.py
│
├── ui/
│   ├── app.py
│   ├── base_page.py
│   ├── compress_page.py
│   ├── delete_page.py
│   ├── home_page.py
│   ├── images_to_pdf_page.py
│   ├── merge_page.py
│   ├── page_manager.py
│   ├── pdf_to_images_page.py
│   ├── protect_page.py
│   ├── rotate_page.py
│   ├── split_page.py
│   └── tools_card.py
│
├── utils/
│   ├── constants.py
│   ├── file_dialog.py
│   ├── helpers.py
│   └── validators.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd pdf-toolkit
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command from the project directory:

```bash
python main.py
```

The PDF Toolkit application will open in a desktop window.

## Usage

1. Launch the application.
2. Select the required PDF tool from the home page.
3. Choose the required files.
4. Configure the available settings.
5. Perform the operation.
6. Choose where to save the generated PDF or output files.

## Design

The application follows a modular structure:

- **UI layer** handles the interface, user interaction, validation, and status messages.
- **Backend layer** handles PDF and image processing.
- **Utils layer** contains reusable helpers, constants, and file-dialog functionality.

This separation keeps the individual features organized and makes the application easier to maintain and extend.

## Requirements

- Python 3.x
- Windows / Linux / macOS
- Required Python packages listed in `requirements.txt`

## Future Improvements

Possible future improvements include:

- PDF preview functionality
- Drag-and-drop file support
- Progress indicators for large files
- More advanced PDF compression options
- Additional PDF utilities
- Improved error reporting
