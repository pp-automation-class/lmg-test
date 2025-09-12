"""Devices Page Object Model"""
from pages.ank_base_page import AnkBasePage
from pages.ank_login_page import AnkLoginPage


class AnkDevicesPage(AnkBasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h5"