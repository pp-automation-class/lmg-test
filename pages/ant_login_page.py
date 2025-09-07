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
        self.user_name = "//input[@name='username']"
        self.password = "//input[@name='password']"
        self.login_button = "//button[text()=' Login ']"
        # Specify locators later
        # self.error_message = '.error-message'
        # self.username_error = '.username-error'
        # self.password_error = '.password-error'
        # self.welcome_message = '.welcome-message'

    def enter_username(self, username):
        """Enter username in the username field"""
        self.fill_input(self.user_name, username)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.fill_input(self.password, password)

    def click_login_button(self):
        """Click the login button"""
        self.click_element(self.login_button)

    def login(self, username, password):
        """Complete login flow with username and password"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()