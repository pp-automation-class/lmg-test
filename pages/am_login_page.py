from pages.am_base_page import AmBasePage


class AmLoginPage(AmBasePage):

    def __init__(self, page):
        super().__init__(page)  # Call parent class constructor

        self.url = "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
        self.page_title = "//h5[.='Login to Your Account']"
        self.email_input = "//input[@name='username']"
        self.password_input = "//input[@name='password']"
        self.button = "//button[type='submit']"
        self.forgot_password_link = "//a[@href='#/restorePassword']"
        self.create_an_account = "//a[@href='#/register']"
        self.go_to_login = "//a[@href='/']"
        self.error_message = ".error-message"

    def navigate_to_login(self):
        self.navigate(self.url)
        self.verify_page()

    def enter_password(self, password):
       self.fill_input(self.password_input, password)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_button()

    def get_error_message(self):
        return self.get_element_text(self.error_message)

    def click_forgot_password(self):
        self.click_element(self.forgot_password_link)

    def click_create_an_account(self):
        self.click_element(self.create_an_account)
