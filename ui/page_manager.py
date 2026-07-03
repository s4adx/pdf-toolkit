from ui.home_page import HomePage

class PageManager:
    
    def __init__(self, container):
        self.container = container
        self.pages = {}

        self._create_pages()


    def _create_pages(self):
        home_page = HomePage(self.container)

        home_page.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.pages["home"] = home_page

        self.show_page("home")


    def show_page(self, page_name):
        page = self.pages.get(page_name)

        if page:
            page.tkraise()