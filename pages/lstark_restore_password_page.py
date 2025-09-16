"""LStark Restore Password Page Object Model"""
from pages.lstark_base_page import LStarkBasePage


class LStarkRestorePassword(LStarkBasePage):
    def __init__(self, page):
        super().__init__(page)  # Call parent constructor

        # Define CSS selectors for page elements
        self.page_title = "h1"  # Page heading selector # Tells us that we are on the correct page
        self.email_input = "//input[@class='el-input__inner']"
        self.send_button = "//button[@class='btn btn-primary w-100']"
        self.back_to_login_page_link = "//a[@href='#/login']"

    def input_email(self, email):
        self.page.fill(self.email_input, email)

    def click_send_button(self):
        self.page.click(self.send_button)

    def click_back_to_login_page_link(self):
        self.page.click(self.back_to_login_page_link)

