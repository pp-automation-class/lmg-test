from pages.am_base_page import AmBasePage
from utils.am_utils import am_get_enviroment

class AmLoginPage(AmBasePage):
    """Page Object Model for Account Manager Login page.

    Extends AmBasePage to reuse common actions such as navigating, clicking,
    and fill inputs. Each locator is an XPath or CSS selector for
    an element on the login page.
    """

    def __init__(self, context):
        # Initialize the base class with the Playwright page instance
        super().__init__(context)

        # NOTE: URL contains basic auth credentials for the test environment.
        # Consider using environment variables or config to avoid hardcoding.
        self.url = am_get_enviroment(context.env, "url")
        self.email = am_get_enviroment(context.env, "email")
        self.password = am_get_enviroment(context.env, "password")

        # Locators
        # Visible page title for sanity checks on the correct page load
        self.page_title = "//h5[.='Login to Your Account']"
        # Email (username) input field
        self.email_input = "//input[@name='username']"
        # Password input field
        self.password_input = "//input[@name='password']"
        # Submit button for the login form
        self.button = "//button[@type='submit']"
        # Ancillary links on the login page
        self.forgot_password_link = "//a[@href='#/restorePassword']"
        self.create_an_account = "//a[@href='#/register']"
        self.go_to_login = "//a[@href='/']"
        # CSS selector for error messages shown on failed login attempts
        self.login_error_message = "//p[text()='Sorry, unrecognized username or password.']"
        # CSS selector for error message shown when email is empty
        self.empty_email_error_message = "//div[text()='Email is required']"
        # CSS selector for error message shown when password is empty
        self.empty_password_error_message = "//div[text()='Password is required']"

    def navigate_to_login(self):
        """
        Open the login page and verify it loaded by checking the page title.
        """
        self.navigate(self.url)
        # verify_page is expected to be provided by the base page hierarchy
        self.verify_page()

    def enter_email(self, email=None):
        """
        Enter an email into the email input field.

        Args:
            email (str): The email address to type into the field.
        """
        if not email:
            email = self.email
        self.fill_input(self.email_input, email)

    def enter_password(self, password=None):
        """Type the password into the password input field."""
        if not password:
            password = self.password
        self.fill_input(self.password_input, password)

    def login(self, email, password):
        """Complete the login flow by entering credentials and submitting.

        Assumes enter_email and click_button are defined in parent classes.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_button()

    def get_login_error_message(self):
        """Return text of an error message if visible, else None."""
        return self.get_element_text(self.login_error_message)

    def click_forgot_password(self):
        """Navigate to the password recovery page."""
        self.click_element(self.forgot_password_link)

    def click_create_an_account(self):
        """Navigate to the account registration page."""
        self.click_element(self.create_an_account)

    def get_empty_email_error_message(self):
        """Return text of an error message if visible, else None."""
        return self.get_element_text(self.empty_email_error_message)

    def get_empty_password_error_message(self):
        """Return text of an error message if visible, else None."""
        return self.get_element_text(self.empty_password_error_message)

