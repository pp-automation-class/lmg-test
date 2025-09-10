"""
Login Page Object Model for Link My Gear
"""
from playwright.sync_api import Page


class LindaLoginPage:
    """Login page for Link My Gear"""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://linkmygear.com/login"

    # Page elements
    email_input = "input[type='email']"
    password_input = "input[type='password']"
    login_button = "button:has-text('Login')"
    forgot_password_link = "a:has-text('Forgot password')"
    create_account_link = "a:has-text('Create an account')"
    page_title = "h1:has-text('Login to Your Account')"

    # Actions
    def open(self):
        """Open login page"""
        self.page.goto(self.url)

    def enter_email(self, email):
        """Enter email address"""
        self.page.fill(self.email_input, email)

    def enter_password(self, password):
        """Enter password"""
        self.page.fill(self.password_input, password)

    def click_login(self):
        """Click login button"""
        self.page.click(self.login_button)

    def click_forgot_password(self):
        """Click forgot password link"""
        self.page.click(self.forgot_password_link)

    def click_create_account(self):
        """Click create account link"""
        self.page.click(self.create_account_link)

    def login(self, email, password):
        """Complete login process"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    # Validations
    def is_page_loaded(self):
        """Check if login page is loaded"""
        return self.page.is_visible(self.page_title)

    def is_email_field_visible(self):
        """Check if email field is visible"""
        return self.page.is_visible(self.email_input)

    def is_password_field_visible(self):
        """Check if password field is visible"""
        return self.page.is_visible(self.password_input)

    def is_login_button_visible(self):
        """Check if login button is visible"""
        return self.page.is_visible(self.login_button)

    def get_email_value(self):
        """Get current email field value"""
        return self.page.input_value(self.email_input)

    def get_password_value(self):
        """Get current password field value"""
        return self.page.input_value(self.password_input)


# Example usage:
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Create login page
    login_page = LoginPage(page)

    # Open and use login page
    login_page.open()
    login_page.login("alena9tester@gmail.com", "your_password")

    # Verify page loaded
    assert login_page.is_page_loaded()

    browser.close()
"""