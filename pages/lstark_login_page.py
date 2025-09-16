"""
Learning: Login Page Object Model for Laura Stark
Learning: Simple implementation demonstrating page object pattern basics
"""

from pages.lstark_base_page import LStarkBasePage


class LStarkLoginPage(LStarkBasePage):
    """Learning: Represents login page with basic elements and actions"""

    def __init__(self, page):
        """Learning: Initialize a page object with a Playwright page instance"""
        super().__init__(page)  # Learning: Call parent constructor
        
        # Learning: Define CSS selectors for page elements # Define CSS selectors for page elements
        self.page_title = "h1"  # Learning: Page heading selector # Tells us that we are on the correct page
        self.email_input = "input[type='email']"  # Learning: Email field
        self.password_input = "input[type='password']"  # Learning: Password field
        self.login_button = "button[type='submit']"  # Learning: Submit button
        # To verify XPath later for .error-message
        self.error_message = ".error-message" # Learning: Error message container
        self.forgot_password_link = "//a[href='#/restorePassword']"  # Learning: Reset link
        self.create_an_account_link = "//a[@href='#/register']"  # Learning: Registration link

    def ls_navigate_to_login(self, url):
        """Learning: Navigate browser to a login page"""
        super().navigate(url)  # Learning: Use parent method

    def ls_enter_email(self, email):
        """Learning: Type email address into email field"""
        self.fill_input(self.email_input, email)  # Learning: Use parent method

    def ls_enter_password(self, password):
        """Learning: Type password into password's field"""
        self.fill_input(self.password_input, password)  # Learning: Use parent method

    def ls_click_login(self):
        """Learning: Click the login submit button"""
        self.click_element(self.login_button)  # Learning: Use parent method

    def ls_login(self, email, password):
        """Learning: Perform full login action"""
        self.ls_enter_email(email)
        self.ls_enter_password(password)
        self.ls_click_login()

    # def get_error_message(self):
    #   """Learning: Retrieve error message text if present"""
    #     if self.page.is_visible(self.error_message):
    #         return self.page.text_context(self.error_message)
    #     return None

    def ls_get_error_message(self):
        """Learning: Retrieve error message text if present"""
        return self.get_element_text(self.error_message)

    def ls_click_forgot_password(self):
        """Learning: Click forgot a password link"""
        self.click_element(self.forgot_password_link)  # Learning: Use parent method

    def ls_click_create_an_account(self):
        """Learning: Click create an account link"""
        self.click_element(self.create_an_account_link)  # Learning: Use parent method


