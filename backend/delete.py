from pypdf import PdfReader, PdfWriter

def delete_pages(input_path, output_path, pages_to_delete):
    reader = None
    writer = None

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page_number, page in enumerate(reader.pages, start=1):
            if page_number not in pages_to_delete:
                writer.add_page(page)

        with open(output_path, "wb") as file:
            writer.write(file)

        return True
    
    except Exception as e:
        print(e)    # Print error in terminal for easier debugging
        return False

    finally:
        if writer is not None:
            writer.close()

        if reader is not None:
            reader.close()
