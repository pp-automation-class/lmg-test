from pages.am_base_page import AmBasePage


class AmCreateAccountPage(AmBasePage):
    """Page Object for the 'Create an Account' screen.

    Encapsulates locators and actions to create a new account.
    """

    def __init__(self, page):
        """Initialize with Playwright's Page and define page locators."""
        super().__init__(page)

        # Page title to confirm we are on the correct page
        self.page_title = "//h5[text()='Create an Account']"
        # Email input field (generic class selector used by the UI library)
        self.email_input = "//input[@class='el-input__inner']"
        # Terms and conditions checkbox control (inner span element)
        self.checkbox = "//span[@class='el-checkbox__inner']"
        # Submit/registration button to create the account
        self.button = "//button[text()=' Register ']"
        # Link opening the terms and conditions document/page
        self.terms_and_conditions = "//a[.='Terms and Conditions']"

    def create_account(self, email):
        """Fill email, accept terms, and submit the registration form."""
        # Type the email into the email input
        self.enter_email(email)
        # Accept terms by clicking the checkbox
        self.click_element(self.checkbox)
        # Submit the form using the register button
        self.click_button()

    def click_terms_and_conditions(self):
        """Open the Terms and Conditions link."""
        self.click_element(self.terms_and_conditions)
