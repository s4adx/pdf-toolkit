from pypdf import PdfWriter

def merge_pdfs(input_files, output_path):
    # Return Boolean value
    try:
        merger = PdfWriter()

        for pdf in input_files:
            merger.append(pdf)


        with open(output_path, "wb") as f:
            merger.write(f)

        merger.close()

        print(f"Merged PDF saved to: {output_path}")
        
    except:
        pass