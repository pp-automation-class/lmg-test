from pages.am_base_page import AmBasePage


class AmCreateAccountPage(AmBasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = "//h5[text()='Create an Account']"
        self.email_input = "//input[@class='el-input__inner']"
        self.checkbox = "//span[@class='el-checkbox__inner']"
        self.button = "//button[text()=' Register ']"
        self.terms_and_conditions = "//a[.='Terms and Conditions']"

    def create_account(self, email):
        self.enter_email(email)
        self.click_element(self.checkbox)
        self.click_button()

    def click_terms_and_conditions(self):
        self.click_element(self.terms_and_conditions)