class AmBasePage:

    def __init__(self, page):
        self.page = page
        self.page_title = "h1"
        self.email_input = "//input[@type='email']"
        self.button = "//button"
        self.go_to_login = "//a[@href='#/login']"

    def navigate(self, url):
        self.page.goto(url)

    def click_element(self, selector):
        self.page.click(selector)

    def fill_input(self, selector, value):
        self.page.fill(selector, value)

    def is_element_visible(self, selector):
        return self.page.is_visible(selector)

    def get_element_text(self, selector):
        if self.is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    def verify_page(self):
        self.page.wait_for_selector(self.page_title)

    def enter_email(self, email):
        self.fill_input(self.email_input, email)

    def click_button(self):
        self.click_element(self.button)

    def click_go_to_login(self):
        self.click_element(self.go_to_login)