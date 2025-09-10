"""
Link My Gear Login Page Object Model
Extends the BasePage class for the login functionality
"""
from pages.base_page import BasePage
from playwright.sync_api import Page
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class LindaLoginPage(BasePage):
    """
    Page Object Model for Link My Gear login page.
    """

    def __init__(self, page: Page, base_url: str = "https://linkmygear.com"):
        super().__init__(page, base_url)

    @property
    def url_path(self) -> str:
        """Return the relative path for the login page."""
        return "/login"  # Adjust this based on the actual URL path

    # Page Elements - Locators
    @property
    def logo(self) -> str:
        """Link My Gear logo locator."""
        return "img[alt*='link my gear'], .logo, [data-testid='logo']"

    @property
    def login_form(self) -> str:
        """Login form container locator."""
        return "form, [data-testid='login-form']"

    @property
    def login_title(self) -> str:
        """Login form title locator."""
        return "h1, h2, .login-title"

    @property
    def email_field(self) -> str:
        """Email input field locator."""
        return "input[type='email'], input[name='email'], input[placeholder*='email']"

    @property
    def email_label(self) -> str:
        """Email field label locator."""
        return "label[for*='email'], label:has-text('Email')"

    @property
    def password_field(self) -> str:
        """Password input field locator."""
        return "input[type='password'], input[name='password']"

    @property
    def password_label(self) -> str:
        """Password field label locator."""
        return "label[for*='password'], label:has-text('Password')"

    @property
    def login_button(self) -> str:
        """Login button locator."""
        return "button[type='submit'], button:has-text('Login'), .login-btn"

    @property
    def forgot_password_link(self) -> str:
        """Forgot password link locator."""
        return "a:has-text('Forgot password'), a[href*='forgot'], a[href*='reset']"

    @property
    def create_account_link(self) -> str:
        """Create account link locator."""
        return "a:has-text('Create an account'), a[href*='register'], a[href*='signup']"

    @property
    def error_message(self) -> str:
        """Error message locator."""
        return ".error, .alert-danger, [data-testid='error'], .error-message"

    @property
    def success_message(self) -> str:
        """Success message locator."""
        return ".success, .alert-success, [data-testid='success'], .success-message"

    # Page Actions
    def wait_for_page_load(self) -> None:
        """Wait for login page to be fully loaded."""
        logger.info("Waiting for login page to load")
        self.wait_for_element(self.login_form)
        self.wait_for_element(self.email_field)
        self.wait_for_element(self.password_field)
        self.wait_for_element(self.login_button)

    def enter_email(self, email: str) -> None:
        """
        Enter email address in the email field.

        Args:
            email: Email address to enter
        """
        logger.info(f"Entering email: {email}")
        self.type_text(self.email_field, email)

    def enter_password(self, password: str) -> None:
        """
        Enter password in the password field.

        Args:
            password: Password to enter
        """
        logger.info("Entering password")
        self.type_text(self.password_field, password)

    def click_login_button(self) -> None:
        """Click the login button."""
        logger.info("Clicking login button")
        self.click_element(self.login_button)

    def click_forgot_password(self) -> None:
        """Click the forgot password link."""
        logger.info("Clicking forgot password link")
        self.click_element(self.forgot_password_link)

    def click_create_account(self) -> None:
        """Click the create account link."""
        logger.info("Clicking create account link")
        self.click_element(self.create_account_link)

    def get_email_value(self) -> str:
        """Get the current value in the email field."""
        return self.get_attribute(self.email_field, "value") or ""

    def get_password_value(self) -> str:
        """Get the current value in the password field."""
        return self.get_attribute(self.password_field, "value") or ""

    def clear_email_field(self) -> None:
        """Clear the email field."""
        logger.info("Clearing email field")
        self.page.locator(self.email_field).clear()

    def clear_password_field(self) -> None:
        """Clear the password field."""
        logger.info("Clearing password field")
        self.page.locator(self.password_field).clear()

    def get_error_message(self) -> str:
        """
        Get error message text if present.

        Returns:
            Error message text or empty string if no error
        """
        if self.is_element_visible(self.error_message, timeout=5000):
            return self.get_text(self.error_message)
        return ""

    def get_success_message(self) -> str:
        """
        Get success message text if present.

        Returns:
            Success message text or empty string if no success message
        """
        if self.is_element_visible(self.success_message, timeout=5000):
            return self.get_text(self.success_message)
        return ""

    # High-level Actions
    def login(self, email: str, password: str, wait_for_navigation: bool = True) -> None:
        """
        Perform complete login action.

        Args:
            email: Email address
            password: Password
            wait_for_navigation: Whether to wait for page navigation after login
        """
        logger.info(f"Performing login for user: {email}")
        self.enter_email(email)
        self.enter_password(password)

        if wait_for_navigation:
            def click_login():
                self.click_login_button()

            self.wait_for_navigation(click_login)
        else:
            self.click_login_button()

    def is_login_form_displayed(self) -> bool:
        """
        Check if login form is displayed.

        Returns:
            True if login form is visible, False otherwise
        """
        return (self.is_element_visible(self.login_form) and
                self.is_element_visible(self.email_field) and
                self.is_element_visible(self.password_field) and
                self.is_element_visible(self.login_button))

    def is_email_field_focused(self) -> bool:
        """Check if email field is currently focused."""
        return self.page.locator(self.email_field).is_focused()

    def is_login_button_enabled(self) -> bool:
        """Check if login button is enabled."""
        return self.page.locator(self.login_button).is_enabled()

    # Validation methods
    def validate_email_format(self, email: str) -> bool:
        """
        Basic email format validation.

        Args:
            email: Email to validate

        Returns:
            True if email format is valid, False otherwise
        """
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))

    # Assertion methods specific to login page
    def assert_login_page_loaded(self) -> None:
        """Assert that login page is properly loaded."""
        self.assert_element_visible(self.login_form)
        self.assert_element_visible(self.email_field)
        self.assert_element_visible(self.password_field)
        self.assert_element_visible(self.login_button)
        logger.info("Login page loaded successfully")

    def assert_login_title_displayed(self, expected_title: str = "Login to Your Account") -> None:
        """Assert that login title is displayed with expected text."""
        self.assert_text_contains(self.login_title, expected_title)

    def assert_email_field_empty(self) -> None:
        """Assert that email field is empty."""
        email_value = self.get_email_value()
        assert email_value == "", f"Email field should be empty, but contains: {email_value}"

    def assert_password_field_empty(self) -> None:
        """Assert that password field is empty."""
        password_value = self.get_password_value()
        assert password_value == "", f"Password field should be empty, but contains: {password_value}"

    def assert_error_message_displayed(self, expected_message: Optional[str] = None) -> None:
        """
        Assert that error message is displayed.

        Args:
            expected_message: Optional expected error message text
        """
        self.assert_element_visible(self.error_message)
        if expected_message:
            self.assert_text_contains(self.error_message, expected_message)

    def assert_no_error_message(self) -> None:
        """Assert that no error message is displayed."""
        self.assert_element_hidden(self.error_message)

    def assert_forgot_password_link_present(self) -> None:
        """Assert that forgot password link is present."""
        self.assert_element_visible(self.forgot_password_link)

    def assert_create_account_link_present(self) -> None:
        """Assert that create account link is present."""
        self.assert_element_visible(self.create_account_link)