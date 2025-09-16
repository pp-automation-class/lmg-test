from pages.base_page import BasePage


class TaPiRestorePasswordPage:

    def __init__(self, page):
        super().__init__(page)
        # Basic locators consistent with TaPi_login_page style and other restore pages
        self.page_title = "h5"
        self.email_input = "//input[@class='el-input__inner']"
        self.send_button = "//button[text()=' Send ']"
        self.back_to_login_link = "//a[@href='#/login']"
        # Common validation/selectors seen in other brand pages
        self.error_empty_email = "//div[text()='Please enter you email address']"
        self.error_invalid_email = "//div[text()='Please enter a valid email address']"

    # Actions
    def TaPi_enter_email(self, email: str):
        self.fill_input(self.email_input, email)

    def TaPi_click_send(self):
        self.click_element(self.send_button)

    def TaPi_click_back_to_login(self):
        self.click_element(self.back_to_login_link)

    def TaPi_restore_password(self, email: str):
        """High-level flow to request password reset."""
        self.enter_email(email)
        self.click_send()

    # Getters/Verifications
    def TaPi_get_empty_email_error(self) -> str:
        return self.get_element_text(self.error_empty_email)

    def TaPi_get_invalid_email_error(self) -> str:
        return self.get_element_text(self.error_invalid_email)


