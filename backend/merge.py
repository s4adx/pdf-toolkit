from pypdf import PdfWriter

def merge_pdfs(input_files, output_path):
    merger = None

    try:
        merger = PdfWriter()

        for pdf in input_files:
            merger.append(pdf)

        with open(output_path, "wb") as f:
            merger.write(f)

        return True

    except Exception as e:
        print(e)    # Print error in terminal for easier debugging
        return False
    
    finally:
        if merger is not None:     
            merger.close()
