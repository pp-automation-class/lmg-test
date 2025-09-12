"""
Login Page Object Model
Purpose: Minimal, consistent skeleton aligned with BasePage utilities.
"""

from pages.base_page import BasePage



class AnKrLoginPage(BasePage):
    """Represents the login page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page) # Call parent class constructor


    # Define selectors for page elements
        self.logo_img = "//img[@alt='Logo']"
        self.email_input = "input[@name='email']"
        self.password_input = "input[@name='password']"
        self.login_button = "button[text()=' Login ']"
        self.error_message = ".error-message"
        self.forgot_password_link = "a:has-text('Restore Password')"
        self.create_an_account_link = "a:has-text('Sign Up')"


    # Methods
    # Navigation
    def navigate_to_login(self, url):
        """Navigate to the login page"""
        # Optionally, just call parent (or remove this and call base from tests)
        super().navigate(url)

    # Field interactions
    def input_email(self, email):
        """Type email into the email field"""
        self.page.fill(self.email_input, email)

    def input_password(self, password):
        """Type password into the password field"""
        self.page.fill(self.password_input, password)

    # Actions
    def click_login(self):
        """Click the login button"""
        self.page.click(self.login_button)


    def login(self, email, password):
        """Complete the login flow with email and password"""
        self.input_email(email)
        self.input_password(password)
        self.click_login()

    # Retrievals
    def get_error_message(self):
        """Get text of the error message if displayed"""
        return self.get_element_text(self.error_message)

    # Navigation links
    def click_forgot_password(self):
        """Click the 'Forgot Password' link"""
        self.click_element(self.forgot_password_link)

    def click_create_an_account(self):
        """Click create an account link"""
        self.click_element(self.create_an_account_link)
