"""
Base Page Object Model for Link My Gear
"""
from playwright.sync_api import Page


class LindaBasePage:
    """Base class for all pages"""

    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://linkmygear.com"

    def open(self, path=""):
        """Open page"""
        url = f"{self.base_url}{path}"
        self.page.goto(url)

    def click(self, selector):
        """Click on element"""
        self.page.locator(selector).click()

    def type_text(self, selector, text):
        """Type text into element"""
        self.page.locator(selector).fill(text)

    def get_text(self, selector):
        """Get element text"""
        return self.page.locator(selector).text_content()

    def is_visible(self, selector):
        """Check if element is visible"""
        return self.page.locator(selector).is_visible()

    def wait_for_element(self, selector):
        """Wait for element to appear"""
        self.page.locator(selector).wait_for()


class LindaLoginPage(LindaBasePage):
    """Login page"""

    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/login"

    # Element locators
    email_field = "input[type='email']"
    password_field = "input[type='password']"
    login_button = "button:has-text('Login')"
    forgot_password_link = "a:has-text('Forgot password')"
    create_account_link = "a:has-text('Create an account')"
    login_title = "h1, h2"

    def open_login_page(self):
        """Open login page"""
        self.open(self.path)

    def enter_email(self, email):
        """Enter email"""
        self.type_text(self.email_field, email)

    def enter_password(self, password):
        """Enter password"""
        self.type_text(self.password_field, password)

    def click_login_button(self):
        """Click login button"""
        self.click(self.login_button)

    def click_forgot_password(self):
        """Click forgot password link"""
        self.click(self.forgot_password_link)

    def click_create_account(self):
        """Click create account link"""
        self.click(self.create_account_link)

    def login(self, email, password):
        """Complete login process"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def get_login_title(self):
        """Get login page title text"""
        return self.get_text(self.login_title)

    def is_login_form_visible(self):
        """Check if login form is visible"""
        return (self.is_visible(self.email_field) and
                self.is_visible(self.password_field) and
                self.is_visible(self.login_button))


# Example usage:
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Create login page instance
    login_page = LoginPage(page)

    # Open login page
    login_page.open_login_page()

    # Perform login
    login_page.login("alena9tester@gmail.com", "your_password")

    # Check if form is visible
    if login_page.is_login_form_visible():
        print("Login form is visible")

    browser.close()
"""