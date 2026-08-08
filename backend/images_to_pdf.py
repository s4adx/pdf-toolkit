from pypdf import PdfReader, PdfWriter
from PIL import Image, ImageOps

A4_PORTRAIT = (1240, 1754)
A4_LANDSCAPE = (1754, 1240)

def images_to_pdf(input_paths, output_path, page_size="image", orientation="auto"):
    try:
        processed_images = []

        for image_path in input_paths:
            image = Image.open(image_path)
            
            # Fix EXIF orientation
            image = ImageOps.exif_transpose(image)

            # Handle transparency / convert to RGB
            if image.mode in ("RGBA", "LA"):
                background = Image.new(
                    "RGB",
                    image.size,
                    "white"
                )

                alpha = image.getchannel("A")

                background.paste(
                    image,
                    mask=alpha
                )

                image = background

            elif image.mode != "RGB":
                image = image.convert("RGB")

            if page_size == "image":
                image = _apply_image_orientation(image, orientation)
                processed_images.append(image.copy())

            elif page_size == "a4":
                canvas = _create_a4_page(image, orientation)

                processed_images.append(canvas)

            image.close

        if not processed_images:
            return False

        first_image = processed_images[0]
        remaining_images = processed_images[1:]

        first_image.save(
            output_path,
            "PDF",
            save_all=True,
            append_images=remaining_images
        )

        return True

    except Exception as error:
        print(error)
        return False

    finally:
        for image in processed_images:
            try:
                image.close()
            except Exception:
                pass

def _apply_image_orientation(image, orientation):
    if orientation == "portrait":
        if image.width > image.height:
            image = image.rotate(90, expand=True)

    elif orientation == "landscape":
        if image.height > image.width:
            image = image.rotate(90, expand=True)

    return image


def _create_a4_page(image, orientation):
    if orientation == "portrait":
        canvas_size = A4_PORTRAIT

    elif orientation == "landscape":
        canvas_size = A4_LANDSCAPE

    else:
        if image.width > image.height:
            canvas_size = A4_LANDSCAPE
        else:
            canvas_size = A4_PORTRAIT

    canvas_width, canvas_height = canvas_size

    resized_image = image.copy()

    resized_image.thumbnail(canvas_size, Image.Resampling.LANCZOS)

    x = (canvas_width - resized_image.width) // 2
    y = (canvas_height - resized_image.height) // 2

    canvas = Image.new(
        "RGB",
        canvas_size,
        "white"
    )

    canvas.paste(resized_image, (x,y))

    resized_image.close()

    return canvas