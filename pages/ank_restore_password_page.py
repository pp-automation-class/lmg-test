"""Restore password page Object Model"""
from pages.base_page import BasePage


class AnKrRestorePasswordPage(BasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "h5"
