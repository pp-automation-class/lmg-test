from pages.am_base_page import AmBasePage
from utils.am_utils import am_get_enviroment

CREATE_AN_ACCOUNT_PAGE_TITLE = "//h5[.='Create an Account']"
CREATE_AN_ACCOUNT_EMAIL_INPUT_SELECTOR = "//input[@class='el-input__inner']"
CREATE_AN_ACCOUNT_LOGIN_BUTTON_SELECTOR = "//button[text()=' Register ']"
CHECKBOX_ACCEPT_SELECTOR = "//span[@class='el-checkbox__inner']"
TERMS_AND_CONDITIONS_LINK = "//a[.='Terms and Conditions']"
USER_ALREADY_EXISTS_ERROR_MESSAGE = "//p[contains(text(), 'The user already exists')]"
EMPTY_EMAIL_ERROR_MESSAGE = "//div[text()='Please enter you email address']"
ENTER_VALID_EMAIL_ERROR_MESSAGE = "//div[text()='Please enter a valid email address']"
EMAIL_LABEL_SELECTOR = "//label[text()='Your Email']"


class AmCreateAccountPage(AmBasePage):
    """Page Object for the 'Create an Account' screen.

    Encapsulates locators and actions to create a new account.
    """

    def __init__(self, context):
        """Initialize with Playwright's Page and define page locators."""
        super().__init__(context)

        # Page title to confirm we are on the correct page
        self.page_title = CREATE_AN_ACCOUNT_PAGE_TITLE
        # Email input field (generic class selector used by the UI library)
        self.email_input = CREATE_AN_ACCOUNT_EMAIL_INPUT_SELECTOR
        # Terms and conditions checkbox control (inner span element)
        self.checkbox_accept = CHECKBOX_ACCEPT_SELECTOR
        # Submit/registration button to create the account
        self.button = CREATE_AN_ACCOUNT_LOGIN_BUTTON_SELECTOR
        # Link opening the terms and conditions document/page
        self.terms_and_conditions = TERMS_AND_CONDITIONS_LINK
        # Email address to use for the account
        self.email = am_get_enviroment(context.env, "email")

        self.user_already_exists_error_message = USER_ALREADY_EXISTS_ERROR_MESSAGE
        self.empty_email_error_message = EMPTY_EMAIL_ERROR_MESSAGE
        self.enter_valid_email_error_message = ENTER_VALID_EMAIL_ERROR_MESSAGE
        self.email_label_selector = EMAIL_LABEL_SELECTOR

    def create_account(self, email):
        """Fill email, accept terms, and submit the registration form."""
        # Type the email into the email input
        self.enter_email(email)
        # Accept terms by clicking the checkbox
        self.check(self.checkbox_accept)
        # Submit the form using the register button
        self.click_button()

    def click_terms_and_conditions(self):
        """Open the Terms and Conditions link."""
        self.click_element(self.terms_and_conditions)

    def get_user_already_exists_error_message(self):
        return self.verify_page(self.user_already_exists_error_message)

    def get_empty_email_error_message(self):
        return self.verify_page(self.empty_email_error_message)

    def get_enter_valid_email_error_message(self):
        return self.verify_page(self.enter_valid_email_error_message)
