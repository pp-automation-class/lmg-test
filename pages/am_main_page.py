from pages.am_base_page import AmBasePage


class AmMainPage(AmBasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = "//h3[contains(text(), 'My device')]"
