from pages.am_base_page import AmBasePage


class AmRestorePasswordPage(AmBasePage):

    def __init__(self, page):
        super().__init__(page)

        self.page_title = "//h5[text()='Restore Password']"
        self.email_input = "//input[@class='el-input__inner']"
        self.button = "//button[text()=' Send ']"

    def restore_password(self, email):
        self.enter_email(email)
        self.click_button()

