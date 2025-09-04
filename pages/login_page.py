"""
Login Page Object Model
Simple implementation for learning purposes
"""

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Represents the login page with its elements and actions"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        super().__init__(page)  # Call parent class constructor

        # Define selectors for page elements
        self.page_title = "h1"
        self.email_input = "input[type='email']"  # Email input field
        self.password_input = "input[type='password']"  # Password input field
        self.login_button = "button[type='submit']"  # Login submit button
        self.error_message = ".error-message"  # Error message container
        self.forgot_password_link = "a:has-text('Forgot Password')"  # Forgot password link
        self.create_an_account = "a:has-text('Sign Up')"  # Sign up link

    def navigate_to_login(self, url):
        """Navigate to login page"""
        super().navigate(url)  # Use parent class method

    def enter_email(self, email):
        """Type email into email field"""
        self.fill_input(self.email_input, email)  # Use parent method

    def enter_password(self, password):
        """Type password into password field"""
        self.fill_input(self.password_input, password)  # Use parent method

    def click_login(self):
        """Click the login button"""
        self.click_element(self.login_button)  # Use parent method

    def login(self, email, password):
        """Complete login flow with email and password"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        """Get text of error message if displayed"""
        return self.get_element_text(self.error_message)  # Use parent method

    def click_forgot_password(self):
        """Click forgot password link"""
        self.click_element(self.forgot_password_link)  # Use parent method

    def click_create_an_account(self):
        """Click create an account link"""
        self.click_element(self.create_an_account)  # Use parent method
