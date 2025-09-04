"""Restore Password Page Object Model"""
from pages.base_page import BasePage

class RestorePasswordPage(BasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        super().__init__(page)

        self.page_title = "h1"
