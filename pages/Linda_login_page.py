"""
Login Page Object Model - Child class inheriting from BasePage
"""
from playwright.sync_api import Page
from pages.base_page import BasePage


class LindaLoginPage(BasePage):
    """Login page for Link My Gear - inherits from BasePage"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/login"

    # Page elements locators
    email_input = "input[type='email']"
    password_input = "input[type='password']"
    login_button = "button:has-text('Login')"
    forgot_password_link = "a:has-text('Forgot password')"
    create_account_link = "a:has-text('Create an account')"
    page_title = "h1:has-text('Login to Your Account')"

    # Page specific actions
    def open_login_page(self):
        """Open login page using inherited open method"""
        self.open(self.path)

    def enter_email(self, email):
        """Enter email using inherited type_text method"""
        self.type_text(self.email_input, email)

    def enter_password(self, password):
        """Enter password using inherited type_text method"""
        self.type_text(self.password_input, password)

    def click_login_button(self):
        """Click login button using inherited click method"""
        self.click(self.login_button)

    def click_forgot_password(self):
        """Click forgot password link using inherited click method"""
        self.click(self.forgot_password_link)

    def click_create_account(self):
        """Click create account link using inherited click method"""
        self.click(self.create_account_link)

    def login(self, email, password):
        """Complete login process"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    # Validations using inherited methods
    def is_login_page_loaded(self):
        """Check if login page is loaded using inherited is_visible method"""
        return self.is_visible(self.page_title)

    def is_email_field_visible(self):
        """Check if email field is visible using inherited is_visible method"""
        return self.is_visible(self.email_input)

    def is_password_field_visible(self):
        """Check if password field is visible using inherited is_visible method"""
        return self.is_visible(self.password_input)

    def is_login_button_visible(self):
        """Check if login button is visible using inherited is_visible method"""
        return self.is_visible(self.login_button)

    def is_login_form_visible(self):
        """Check if complete login form is visible"""
        return (self.is_email_field_visible() and
                self.is_password_field_visible() and
                self.is_login_button_visible())

    def get_login_title(self):
        """Get login page title using inherited get_text method"""
        return self.get_text(self.page_title)

    def get_email_value(self):
        """Get current email field value"""
        return self.page.input_value(self.email_input)

    def get_password_value(self):
        """Get current password field value"""
        return self.page.input_value(self.password_input)

    def wait_for_login_form(self):
        """Wait for login form to load using inherited wait_for_element method"""
        self.wait_for_element(self.email_input)
        self.wait_for_element(self.password_input)
        self.wait_for_element(self.login_button)


# Example usage:
"""
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Create login page instance (inherits all BasePage methods)
    login_page = LoginPage(page)

    # Use inherited and specific methods
    login_page.open_login_page()          # Specific method
    login_page.wait_for_login_form()      # Uses inherited wait_for_element
    login_page.login("test@email.com", "password")  # Specific method using inherited methods

    # Verify using inherited methods
    assert login_page.is_login_page_loaded()  # Uses inherited is_visible

    browser.close()
"""