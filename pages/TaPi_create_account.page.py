from pages.base_page import BasePage


class TaPiCreateAccountPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        # Basic header selector; adjust if a specific heading text exists in app
        self.page_title = "h5"

        # Common registration form elements
        self.email_input = "//input[@name='email' or @type='email']"
        self.enter_valid_email_error_message = "//div[@class='el-form-item__error' and contains(text(), 'Please enter you email address']"
        self.checkbox = "//span[@class='el-checkbox__inner']"
        self.save_button = "//button[normalize-space(.)='Create' or normalize-space(.)='Sign Up' or @type='submit']"
        self.back_to_login_link = "//a[contains(., 'Login') or contains(., 'Sign in') or @href='#/login']"

    # Actions
    def TaPi_set_email(self, email: str):
        self.fill_input(self.email_input, email)
    def TaPi_click_checkbox(self):
        self.click_element(self.checkbox)


    def Tapi_click_back_to_login(self):
        self.click_element(self.back_to_login_link)
