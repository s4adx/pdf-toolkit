from pypdf import PdfReader, PdfWriter

def protect_pdf(input_path, output_path, password):
    reader = None
    writer = None   

    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password, algorithm="AES-256")

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

