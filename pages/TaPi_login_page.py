from pages.base_page import BasePage


class TaPiLoginPage(BasePage):
    """Login page with elements and actions."""

    def __init__(self, page):
        super().__init__(page)

        self.page_title = "h1"
        self.email_input = "//input[@name='username']"
        self.password_input = "input[type='password']"
        self.login_button = "button[type='submit']"
        self.error_message = ".error-message"

    def enter_email(self, email: str):
        self.fill_input(self.email_input, email)

    def enter_password(self, password: str):
        self.fill_input(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)

    def login(self, email: str, password: str):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        return self.get_element_text(self.error_message)
