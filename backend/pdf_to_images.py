import pymupdf
from pathlib import Path

def pdf_to_images(input_path, output_folder, image_format, pages):
    pdf = None

    try:
        pdf = pymupdf.open(input_path)

        output_folder = Path(output_folder)
        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        for page_index in sorted(pages):
            page = pdf[page_index]

            pixmap = page.get_pixmap(dpi=200)

            output_path = output_folder/f"page_{page_index + 1}.{image_format}"

            if image_format == "jpg":
                pixmap.save(
                    str(output_path),
                    jpg_quality=95
                )

            else:
                pixmap.save(str(output_path))

        return True

    except Exception as e:
        print(e)
        return False

    finally:
        if pdf is not None:
            pdf.close()
        