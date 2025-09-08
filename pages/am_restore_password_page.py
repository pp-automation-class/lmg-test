from pages.am_base_page import AmBasePage
from utils.am_utils import am_get_enviroment

FORGOT_PASSWORD_EMAIL_INPUT_SELECTOR = "//input[@class='el-input__inner']"
FORGOT_PASSWORD_LOGIN_BUTTON_SELECTOR = "//button[text()=' Send ']"
FORGOT_PASSWORD_SEND_RESULT_MESSAGE = "//p[.='Unable to send email. Contact the site administrator if the problem persists.']"
EMPTY_RESTORE_EMAIL_ERROR_MESSAGE = "//div[text()='Please enter you email address']"
WRONG_FORMAT_RESTORE_EMAIL_ERROR_MESSAGE = "//div[text()='Please enter a valid email address']"

class AmRestorePasswordPage(AmBasePage):
    """
    Page Object representing the 'Restore Password' screen.
    Inherits common browser actions (e.g., clicking, typing, waiting)
    from AmBasePage.
    """

    def __init__(self, context):
        # Initialize the base page with the Playwright-like page instance
        super().__init__(context)

        # Locators for elements on the Restore Password page:
        self.page_title = (
            # Page header used to verify the correct page
            "//h5[text()='Restore Password']"
        )
        self.email = am_get_enviroment(context.env, "email")
        # Input where the user types the email to recover
        self.email_input = FORGOT_PASSWORD_EMAIL_INPUT_SELECTOR
        # Button that submits the password restore request
        self.button = FORGOT_PASSWORD_LOGIN_BUTTON_SELECTOR
        self.forgot_password_email_input_selector = FORGOT_PASSWORD_EMAIL_INPUT_SELECTOR
        self.forgot_password_login_button_selector = FORGOT_PASSWORD_LOGIN_BUTTON_SELECTOR
        self.forgot_password_send_result_message = FORGOT_PASSWORD_SEND_RESULT_MESSAGE
        self.empty_restore_email_error_message = EMPTY_RESTORE_EMAIL_ERROR_MESSAGE
        self.wrong_format_restore_email_error_message = WRONG_FORMAT_RESTORE_EMAIL_ERROR_MESSAGE

    def restore_password(self, email):
        """
        High-level action that performs the restore password flow:
        - Enters the provided email
        - Clicks the 'Send' button to request a reset link
        """
        # Fill the email field with the target user's email address
        self.enter_email(email)
        # Submit the form to trigger the restore password process
        self.click_button()

    def get_forgot_password_send_result_message(self):
        return self.verify_page(self.forgot_password_send_result_message)

    def get_empty_restore_email_error_message(self):
        return self.verify_page(self.empty_restore_email_error_message)

    def get_wrong_format_restore_email_error_message(self):
        return self.verify_page(self.wrong_format_restore_email_error_message)
