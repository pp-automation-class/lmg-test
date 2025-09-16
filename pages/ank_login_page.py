"""
Login Page Object Model
Purpose: Minimal, consistent skeleton aligned with BasePage utilities.
"""

from pages.ank_base_page import AnkBasePage
from pages.ank_create_account_page import AnkCreateAccountPage


class AnkLoginPage(AnkBasePage):
    """Represents the login page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)  # Call parent class constructor

    # Define selectors for page elements

        self.page_title = "//h5"
        self.email_input = "//input[@name='username']"
        self.password_input = "//input[@name='password']"
        self.login_button = "//button[text()=' Login ']"
        self.forgot_password_link = "//a[text()='Forgot password?']"
        self.create_account_link = "//a[text()='Create an account']"
        self.restore_password_link = "//h5[text()='Restore Password']"
        self.validation_message = "//p[contains(text(), 'Sorry')]"
        self.device_page= "//h3[contains(text(), 'My devices')]"
        self.error_message = "//p[contains(text(), 'Sorry, unrecognized username or password')]"

    # Navigation
    def ank_navigate_to_login(self, url):
        """Navigate to the login page"""
        # Optionally, just call parent (or remove this and call base from tests)
        self.ank_navigate(url)

    # Field interactions
    def ank_enter_email(self, email):
        """Type email into the email field"""
        self.ank_fill_input(self.email_input, email)

    def ank_enter_password(self, password):
        """Type password into the password field"""
        self.ank_fill_input(self.password_input, password)

    # Actions
    def ank_click_login(self):
        """Click the login button"""
        self.ank_click_element(self.login_button)

    def ank_login(self, email, password):
        """Complete the login flow with email and password"""
        self.ank_enter_email()
        self.ank_enter_password()
        self.ank_click_login()

    # Navigation links
    def ank_click_forgot_password(self):
        """Click the 'Forgot Password' link"""
        self.ank_click_element(self.forgot_password_link)

    def ank_click_create_account(self) -> AnkCreateAccountPage:
        """Click create an account link"""
        self.ank_click_element(self.create_account_link)
        return AnkCreateAccountPage(self.page)

    # Helpers
    def ank_get_validation_text(self):
        return self.ank_get_element_text(self.validation_message)

    def ank_verify_title_contains(self, expected_text):
        return self.ank_verify_page_title(expected_text)

    def ank_verify_device_page(self, xpath: str = None):
        """Check if an element exists on the page by xpath. If not provided, use default dashboard xpath."""
        xpath = xpath or self.device_page
        return self.ank_element_exists(xpath, wait=True)

    def ank_verify_element_exists(self, error_message, wait):
        return self.ank_element_exists(error_message, wait)
        pass

    def ank_element_exists(self, xpath, wait):
        pass
