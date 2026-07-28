from pypdf import PdfReader, PdfWriter

def rotate_pdf(input_path, output_path, rotation_angle, page_mode, start_page=None, end_page=None):
    reader = None
    writer = None
    
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for index, page in enumerate(reader.pages):
            should_rotate = False

            if page_mode == "all":
                should_rotate = True

            elif page_mode == "single":
                should_rotate = index == start_page - 1

            elif page_mode == "range":
                should_rotate = start_page - 1 <= index <= end_page - 1

            if should_rotate:
                page.rotate(rotation_angle)

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

