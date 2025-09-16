from pages.base_page import BasePage


class TaPiCreateAccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # Basic header selector; adjust if a specific heading text exists in app
        self.page_title = "h5"

        # Common registration form elements
        self.email_input = "//input[@name='email' or @type='email']"
        self.empty_email_error_message = "//div[text()='Please enter you email address']"

        self.enter_valid_email_error_message = "//div[text()='Please enter a valid email address']"
        self.checkbox = "//span[@class='el-checkbox__inner']"
        self.terms_and_conditions = "//a[text()='Terms and Conditions']"
        self.register_button = "//button"
        self.back_to_login_link = "//a[text()='Log in']"


    # Actions
    def TaPi_set_email(self, email: str):
        self.fill_input(self.email_input, email)

    def TaPi_get_empty_email_error_message(self) -> str:
        return self.get_element_text(self.empty_email_error_message)

    def TaPi_get_enter_valid_email_error_message(self) -> str:
        return self.get_element_text(self.enter_valid_email_error_message)

    def TaPi_click_checkbox(self):
        self.click_element(self.checkbox)

    def TaPi_click_terms_and_conditions(self):
        self.click_element(self.terms_and_conditions)

    def TaPi_click_register(self):
        self.click_element(self.register_button)

    def TaPi_click_back_to_login(self):
        self.click_element(self.back_to_login_link)




