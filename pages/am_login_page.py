from pages.am_base_page import AmBasePage
from utils.am_utils import am_get_enviroment


LOGIN_PAGE_TITLE = "//h5[.='Login to Your Account']"
RESTORE_PASSWORD_PAGE_TITLE = "//h5[.='Restore Password']"
EMAIL_INPUT_SELECTOR = "//input[@name='username']"
PASSWORD_INPUT_SELECTOR = "//input[@name='password']"
LOGIN_BUTTON_SELECTOR = "//button[@type='submit']"
FORGOT_PASSWORD_LINK = "//a[.='Forgot password?']"
CREATE_AN_ACCOUNT_LINK = "//a[@href='#/register']"
GO_TO_LOGIN_LINK = "//a[@href='/']"
LOGIN_ERROR_MESSAGE = "//p[text()='Sorry, unrecognized username or password.']"
EMPTY_EMAIL_ERROR_MESSAGE = "//div[text()='Email is required']"
EMPTY_PASSWORD_ERROR_MESSAGE = "//div[text()='Password is required']"


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
        self.page_title = LOGIN_PAGE_TITLE
        # Page title for the password recovery page
        self.restore_password_title = RESTORE_PASSWORD_PAGE_TITLE
        # Email (username) input field
        self.email_input = EMAIL_INPUT_SELECTOR
        # Password input field
        self.password_input = PASSWORD_INPUT_SELECTOR
        # Submit button for the login form
        self.button = LOGIN_BUTTON_SELECTOR
        # Ancillary links on the login page
        self.forgot_password_link = FORGOT_PASSWORD_LINK
        self.create_an_account_link = CREATE_AN_ACCOUNT_LINK
        self.go_to_login = GO_TO_LOGIN_LINK
        # CSS selector for error messages shown on failed login attempts
        self.login_error_message = LOGIN_ERROR_MESSAGE
        # CSS selector for an error message shown when email is empty
        self.empty_email_error_message = EMPTY_EMAIL_ERROR_MESSAGE
        # CSS selector for an error message shown when password is empty
        self.empty_password_error_message = EMPTY_PASSWORD_ERROR_MESSAGE
        # CSS selectors for elements on the password recovery page

    def navigate_to_login(self):
        """
        Open the login page and verify it loaded by checking the page title.
        """
        self.navigate(self.url)
        # verify_page is expected to be provided by the base page hierarchy
        self.verify_page()

    def enter_password(self, password=None):
        """Type the password into the password input field."""
        if not password:
            password = self.password
        self.fill_input(self.password_input, password)

    def login(self, email=None, password=None):
        """Complete the login flow by entering credentials and submitting.

        Assumes enter_email and click_button are defined in parent classes.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_button()

    def get_login_error_message(self):
        """Return text of an error message if visible, else None."""
        return self.verify_page(self.login_error_message)

    def click_forgot_password(self):
        """Navigate to the password recovery page."""
        self.click_element(self.forgot_password_link)

    def click_create_an_account(self):
        """Navigate to the account registration page."""
        self.click_element(self.create_an_account_link)

    def get_empty_email_error_message(self):
        """Return text of an error message if visible, else None."""
        return self.verify_page(self.empty_email_error_message)

    def get_empty_password_error_message(self):
        """Return text of an error message if visible, else None."""
        return self.verify_page(self.empty_password_error_message)

    def get_empty_restore_email_error_message(self):
        return self.verify_page(self.empty_restore_email_error_message)

    def get_wrong_format_restore_email_error_message(self):
        return self.verify_page(self.wrong_format_restore_email_error_message)
