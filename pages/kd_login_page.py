"""
Login Page Object Model (KD)
"""

from pages.base_page import BasePage

class KdLoginPage(BasePage):
    """Represents the KD login page and its actions"""

    def __init__(self, page):
        super().__init__(page)

        # Common page title selector for BasePage.verify_page_title
        self.page_title = "h1"

        # Inputs (robust, multi-option selectors)
        self.email_input = (
            "input[type='email'], input[name='email'], input[placeholder='Email']"
        )
        self.password_input = (
            "input[type='password'], input[name='password'], input[placeholder='Password']"
        )

        # Buttons / links based on the screenshot
        self.login_button = "button:has-text('Login'), button[type='submit']"
        self.forgot_password_link = (
            "a:has-text('Forgot password'), a[href*='forgot'], a[href*='reset']"
        )
        self.create_account_link = (
            "a:has-text('Create an account'), a:has-text('Sign up'), a[href*='register']"
        )

        # Generic validation or error container
        self.validation_message = ".error-message, .validation-message, [role='alert']"

    # Navigation
    def kd_navigate_to_login(self, url: str) -> None:
        """Navigate to the login page"""
        self.navigate(url)

    # Field interactions
    def kd_enter_email(self, email: str) -> None:
        self.fill_input(self.email_input, email)

    def kd_enter_password(self, password: str) -> None:
        self.fill_input(self.password_input, password)

    # Actions
    def kd_click_login(self) -> None:
        self.click_element(self.login_button)

    def kd_login(self, email: str, password: str) -> None:
        """Complete the login flow using email and password"""
        self.kd_enter_email(email)
        self.kd_enter_password(password)
        self.kd_click_login()

    def kd_click_forgot_password(self) -> None:
        self.click_element(self.forgot_password_link)

    def kd_click_create_account(self) -> KdCreateAccountPage:
        """Click the Create an account link and return the create-account POM"""
        self.click_element(self.create_account_link)
        return KdCreateAccountPage(self.page)

    # Helpers
    def kd_get_validation_text(self):
        """Return the text from a visible validation/error message if present."""
        return self.get_element_text(self.validation_message)

    def kd_verify_title_contains(self, expected_text: str) -> bool:
        """Verify the page title contains expected text using BasePage logic."""
        return self.verify_page_title(expected_text)
