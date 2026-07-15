from pathlib import Path
from pypdf import PdfWriter, PdfReader

def split_pdf(input_path, split_page, output_folder):
    reader = None
    writer1 = None
    writer2 = None

    try:
        reader = PdfReader(input_path)
        total_page = len(reader.pages)

        writer1 = PdfWriter()
        writer2 = PdfWriter()

        file_stem = Path(input_path).stem

        output1_path = Path(output_folder) / f"{file_stem}_part_1.pdf"
        output2_path = Path(output_folder) / f"{file_stem}_part_2.pdf"

        for i in range(0, split_page):
            writer1.add_page(reader.pages[i])

        with open(output1_path, "wb") as f:
            writer1.write(f)

        for i in range(split_page, total_page):
            writer2.add_page(reader.pages[i])

        with open(output2_path, "wb") as f:
            writer2.write(f)

        return True

    except Exception as e:
        print(e)    # Print error in terminal for easier debugigng
        return False

    finally:
        if writer1 is not None:
            writer1.close()

        if writer2 is not None:
            writer2.close()

        if reader is not None:
            reader.close()


def extract_pages(input_path, start_page, end_page, output_path):
    reader = None
    writer = None

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])

        with open(output_path, "wb") as f:
            writer.write(f)

        return True

    except Exception as e:
        print(e)    # Print error in terminal for easier debugigng
        return False
    
    finally:
        if reader is not None:
            reader.close()

        if writer is not None:
            writer.close()


def split_every_page(input_path, output_folder):
    reader = None

    try:
        reader = PdfReader(input_path)

        for index, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)

            output_file_path = Path(output_folder) / f"page_{index}.pdf"
            with open(output_file_path, "wb") as f:
                writer.write(f)

            writer.close()

        return True
    
    except Exception as e:
        print(e)    # Print error in terminal for easier debugigng
        return False

    finally:
        if reader is not None:
            reader.close()