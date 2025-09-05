"""
Restore Password Page Object Model (KD)
"""

from pages.kd_base_page import KdBasePage
from pages.kd_login_page import KdLoginPage


class KdRestorePasswordPage(KdBasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = "//h5"
        self.email_input = "//input[@id='el-id-9524-9']"
        self.send_button = "//button[text()=' Send ']"
        self.back_to_login_link = "//a[text()='Back to Login page']"
        self.validation_message = "//p[contains(text(), 'Sorry')]"

    # Navigation
    def kd_navigate_to_restore(self, url: str) -> None:
        """Navigate to the Restore Password page"""
        self.kd_navigate(url)

    # Interactions
    def kd_enter_email(self, email: str) -> None:
        self.kd_fill_input(self.email_input, email)

    def kd_click_send(self) -> None:
        self.kd_click_element(self.send_button)

    def kd_restore(self, email: str) -> None:
        """Fill email and submit restore password request"""
        self.kd_enter_email(email)
        self.kd_click_send()

    def kd_click_back_to_login(self) -> KdLoginPage:
        """Click the back link and return the Login page POM"""
        self.kd_click_element(self.back_to_login_link)
        return KdLoginPage(self.page)

    # Helpers
    def kd_get_validation_text(self):
        return self.kd_get_element_text(self.validation_message)

    def kd_verify_title_contains(self, expected_text: str) -> bool:
        return self.kd_verify_page_title(expected_text)
