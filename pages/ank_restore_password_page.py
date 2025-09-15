"""Restore password page Object Model"""
from pages.ank_base_page import AnkBasePage
from pages.ank_login_page import AnkLoginPage


class AnkRestorePasswordPage(AnkBasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h5"
        self.email_input = "//input[@class='el-input__inner']"
        self.send_button = "//button[text()=' Send ']"
        self.back_to_login_link = "//a[text()='Back to Login page']"
        self.validation_message = "//p[contains(text(), 'Sorry')]"

        # Navigation
    def ank_navigate_to_restore(self, url):
        """Navigate to the Restore Password page"""
        self.ank_navigate(url)

        # Interactions
    def ank_enter_email(self, email):
        self.ank_fill_input(self.email_input, email)

    def ank_click_send(self):
        self.ank_click_element(self.send_button)

    def ank_restore(self, email):
        """Fill email and submit restore password request"""
        self.ank_enter_email(email)
        self.ank_click_send()

    def ank_click_back_to_login(self) -> AnkLoginPage:
        """Click the back link and return the Login page POM"""
        self.ank_click_element(self.back_to_login_link)
        return AnkLoginPage(self.page)

        # Helpers
    def ank_get_validation_text(self):
        return self.ank_get_element_text(self.validation_message)

    def ank_verify_title_contains(self, expected_text):
        return self.ank_verify_page_title(expected_text)


