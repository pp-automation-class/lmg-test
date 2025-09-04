"""
Create Account Page Object Model (KD)
"""

from pages.kd_base_page import KdBasePage


class KdCreateAccountPage(KdBasePage):
    """Represents create account page and actions on it"""

    def __init__(self, page):
        super().__init__(page)

        # Page title used by BasePage.verify_page_title
        self.page_title = "h1"

        # Elements on the new screen
        self.email_input = (
            "input[type='email'], input[placeholder='Your Email'], input[name='email']"
        )

        self.terms_checkbox = (
            "label:has-text('Agree'), label:has-text('Terms and Conditions'), input[type='checkbox']"
        )
        self.register_button = "button:has-text('Register'), button[type='submit']"
        self.login_link = "a:has-text('Log in'), a[href*='login']"

        self.validation_message = ".error-message, .validation-message, [role='alert']"

    # Navigation
    def kd_navigate_to_register(self, url):
        """Navigate to the registration page"""
        self.kd_navigate(url)

    # Interactions
    def kd_enter_email(self, value):
        self.kd_fill_input(self.email_input, value)

    def kd_check_terms(self):
        """Toggle/check the terms checkbox by clicking label/checkbox"""
        self.kd_click_element(self.terms_checkbox)

    def kd_click_register(self):
        self.kd_click_element(self.register_button)

    def kd_click_login_link(self):
        self.kd_click_element(self.login_link)

    # Composite flow
    def kd_register(self, email, accept_terms=True):
        self.kd_enter_email(email)
        if accept_terms:
            self.kd_check_terms()
        self.kd_click_register()

    # Validation helpers
    def kd_get_validation_text(self):
        return self.kd_get_element_text(self.validation_message)
