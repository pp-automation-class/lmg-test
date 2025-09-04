"""
Login Page Object Model (KD)
"""

from pages.kd_base_page import KdBasePage
from pages.kd_create_account_page import KdCreateAccountPage


class KdLoginPage(KdBasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = "//h5"
        self.email_input = "//input[@name='username']"
        self.password_input = "//input[@name='password']"
        self.login_button = "//button[text()=' Login ']"
        self.forgot_password_link = "//a[text()='Forgot password?']"
        self.create_account_link = "//a[text()='Create an account']"

        # Generic validation or error container
        # self.validation_message = ".error-message, .validation-message, [role='alert']"

    # Navigation
    def kd_navigate_to_login(self, url: str) -> None:
        """Navigate to the login page"""
        self.kd_navigate(url)

    # Field interactions
    def kd_enter_email(self, email: str) -> None:
        self.kd_fill_input(self.email_input, email)

    def kd_enter_password(self, password: str) -> None:
        self.kd_fill_input(self.password_input, password)

    # Actions
    def kd_click_login(self) -> None:
        self.kd_click_element(self.login_button)

    def kd_login(self, email: str, password: str) -> None:
        """Complete the login flow using email and password"""
        self.kd_enter_email(email)
        self.kd_enter_password(password)
        self.kd_click_login()

    def kd_click_forgot_password(self) -> None:
        self.kd_click_element(self.forgot_password_link)

    def kd_click_create_account(self) -> KdCreateAccountPage:
        self.kd_click_element(self.create_account_link)
        return KdCreateAccountPage(self.page)

    # Helpers
    # def kd_get_validation_text(self):
    #     return self.kd_get_element_text(self.validation_message)

    # def kd_verify_title_contains(self, expected_text: str) -> bool:
    #     return self.kd_verify_page_title(expected_text)
