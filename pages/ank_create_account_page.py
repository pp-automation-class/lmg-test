"""Create Account Page Object Model"""
from pages.ank_base_page import AnkBasePage


class AnkCreateAccountPage(AnkBasePage):

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h5"
        self.email_input = "//input[@name='username']"
        self.password_input = "//input[@name='password']"
        self.register_button = "//button[text()=' Register ']"
        self.login_link = "//button[text()=' Login ']"
        self.validation_message = "//p[contains(text(), 'Sorry')]"

    # Navigation
    def ank_navigate_to_register(self, url):
        """Navigate to the registration page"""
        self.ank_navigate(url)

    # Interactions
    def ank_enter_email(self, value):
        self.ank_fill_input(self.email_input, value)

    def ank_check_terms(self):
        """Toggle/check the terms checkbox by clicking label/checkbox"""
        self.ank_click_element(self.terms_checkbox)

    def ank_click_register(self):
        self.ank_click_element(self.register_button)

    def ank_click_login_link(self):
        self.ank_click_element(self.login_link)

    def ank_register(self, email, accept_terms=True):
        self.ank_enter_email(email)
        if accept_terms:
            self.ank_check_terms()
        self.ank_click_register()

        # Validation helpers
    def ank_get_validation_text(self):
        return self.ank_get_validation_text(self.validation_message)

    def ank_verify_title_contains(self, expected_text: str) -> bool:
        return self.ank_verify_page_title(expected_text)
