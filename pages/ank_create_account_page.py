"""Create Account Page Object Model"""
from pages.base_page import BasePage


class AnKrCreateAccountPage(BasePage):

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)


        self.page_title = "h5"
