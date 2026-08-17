import pymupdf
from pathlib import Path

def compress_pdf(input_path, output_path, compression_level):
    pdf = None

    try:
        pdf = pymupdf.open(input_path)

        quality_map = {
            "low": 90,
            "recommended": 75,
            "high": 50
        }

        quality = quality_map[compression_level]

        for page in pdf:
            images = page.get_images(full=True)

            for image in images:
                xref = image[0]

                image_data = pdf.extract_image(xref)

                if not image_data:
                    continue

                image_bytes = image_data["image"]
                image_ext = image_data["ext"]

                if image_ext not in ("jpg", "jpeg", "png"):
                    continue

                try:
                    image_doc = pymupdf.open(
                        stream=image_bytes,
                        filetype=image_ext
                    )

                    image_page = image_doc[0]

                    pixmap = image_page.get_pixmap(
                        colorspace=pymupdf.csRGB,
                        alpha=False
                    )

                    compressed_bytes = pixmap.tobytes(
                        "jpeg",
                        jpg_quality=quality
                    )

                    page.replace_image(
                        xref,
                        stream=compressed_bytes
                    )

                    image_doc.close()

                except Exception as image_error:
                    print(f"Could not compress image.\n Error: {image_error}")

        pdf.save(
            output_path,
            garbage=4,
            deflate=True,
            clean=True
        )

        return True

    except Exception as e:
        print(e)
        return False

    finally:
        if pdf is not None:
            pdf.close()