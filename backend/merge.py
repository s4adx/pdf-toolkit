from pypdf import PdfWriter

def merge_pdfs(input_files, output_path):

    try:
        merger = PdfWriter()

        for pdf in input_files:
            merger.append(pdf)

        with open(output_path, "wb") as f:
            merger.write(f)

        return True

    except Exception as e:
        print(e)
        return False
    
    finally:
        merger.close()
