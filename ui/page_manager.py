from ui.home_page import HomePage
from ui.merge_page import MergePage
from ui.split_page import SplitPage
from ui.rotate_page import RotatePage
from ui.delete_page import DeletePage
from ui.extract_page import ExtractPage
from ui.images_to_pdf_page import ImagesToPdfPage
from ui.pdf_to_images_page import PdfToImagesPage
from ui.compress_page import CompressPage 


class PageManager:
    
    def __init__(self, container):
        self.container = container
        self.pages = {}

        self.pages_classes = {
            "home": HomePage,
            "merge": MergePage,
            "split": SplitPage,
            "rotate": RotatePage,
            "delete": DeletePage,
            "extract": ExtractPage,
            "images_to_pdf": ImagesToPdfPage,
            "pdf_to_images": PdfToImagesPage,
            "compress": CompressPage,
        }

        self._create_pages()


    def _create_pages(self):

        for page_name, PageClass in self.pages_classes.items():

            page = PageClass(self.container, self)

            page.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

            self.pages[page_name] = page

        self.show_page("home")


    def show_page(self, page_name):
        page = self.pages.get(page_name)

        if page:
            page.tkraise()