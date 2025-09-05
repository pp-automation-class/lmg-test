"""
Login Page Object Model
Contains methods for interacting with the login page
"""

from pages.base_page import BasePage


class AntLoginPage(BasePage):
    """Login page with specific login functionality"""

    def __init__(self, page):
        """Initialize login page with selectors"""
        super().__init__(page)
        self.page_title = "h1"
        
        # Login page selectors
        self.username_field = 'input[type="email"]'
        self.password_field = 'input[type="password"]'
        self.login_button = 'button[type="submit"]'
        self.error_message = '.error-message'
        self.username_error = '.username-error'
        self.password_error = '.password-error'
        self.welcome_message = '.welcome-message'

    def enter_username(self, username):
        """Enter username in the username field"""
        self.fill_input(self.username_field, username)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.fill_input(self.password_field, password)

    def click_login_button(self):
        """Click the login button"""
        self.click_element(self.login_button)

    def login(self, username, password):
        """Complete login flow with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        """Get the general error message text"""
        return self.get_element_text(self.error_message)

    def get_username_error_message(self):
        """Get the username field error message"""
        return self.get_element_text(self.username_error)

    def get_password_error_message(self):
        """Get the password field error message"""
        return self.get_element_text(self.password_error)

    def get_welcome_message(self):
        """Get the welcome message after successful login"""
        return self.get_element_text(self.welcome_message)

    def is_login_button_enabled(self):
        """Check if login button is enabled"""
        return not self.page.is_disabled(self.login_button)

    def is_error_message_visible(self):
        """Check if error message is displayed"""
        return self.is_element_visible(self.error_message)

    def is_username_error_visible(self):
        """Check if username error message is displayed"""
        return self.is_element_visible(self.username_error)

    def is_password_error_visible(self):
        """Check if password error message is displayed"""
        return self.is_element_visible(self.password_error)

    def clear_username_field(self):
        """Clear the username field"""
        self.page.fill(self.username_field, "")

    def clear_password_field(self):
        """Clear the password field"""
        self.page.fill(self.password_field, "")

    def leave_username_empty(self):
        """Ensure username field is empty"""
        self.clear_username_field()

    def leave_password_empty(self):
        """Ensure password field is empty"""
        self.clear_password_field()