from pages.am_base_page import AmBasePage


class AmLoginPage(AmBasePage):
    """Page Object Model for Account Manager Login page.

    Extends AmBasePage to reuse common actions such as navigating, clicking,
    and fill inputs. Each locator is an XPath or CSS selector for
    an element on the login page.
    """

    def __init__(self, page):
        # Initialize the base class with the Playwright page instance
        super().__init__(page)

        # NOTE: URL contains basic auth credentials for the test environment.
        # Consider using environment variables or config to avoid hardcoding.
        self.url = "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"

        # Locators
        # Visible page title for sanity checks on the correct page load
        self.page_title = "//h5[.='Login to Your Account']"
        # Email (username) input field
        self.email_input = "//input[@name='username']"
        # Password input field
        self.password_input = "//input[@name='password']"
        # Submit button for the login form
        self.button = "//button[type='submit']"
        # Ancillary links on the login page
        self.forgot_password_link = "//a[@href='#/restorePassword']"
        self.create_an_account = "//a[@href='#/register']"
        self.go_to_login = "//a[@href='/']"
        # CSS selector for error messages shown on failed login attempts
        self.error_message = ".error-message"

    def navigate_to_login(self):
        """
        Open the login page and verify it loaded by checking the page title.
        """
        self.navigate(self.url)
        # verify_page is expected to be provided by the base page hierarchy
        self.verify_page()

    def enter_password(self, password):
        """Type the password into the password input field."""
        self.fill_input(self.password_input, password)

    def login(self, email, password):
        """Complete the login flow by entering credentials and submitting.

        Assumes enter_email and click_button are defined in parent classes.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_button()

    def get_error_message(self):
        """Return text of an error message if visible, else None."""
        return self.get_element_text(self.error_message)

    def click_forgot_password(self):
        """Navigate to the password recovery page."""
        self.click_element(self.forgot_password_link)

    def click_create_an_account(self):
        """Navigate to the account registration page."""
        self.click_element(self.create_an_account)
