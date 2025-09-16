"""Create an Account Page Object Model"""

from pages.base_page import BasePage
from pages.lstark_base_page import LStarkBasePage


class LStarkCreateAnAccountPage(LStarkBasePage):
    def __init__(self, page):
        """Initialize page object with Playwright page instance"""
        super().__init__(page)  # Call parent constructor

        # Define CSS selectors for page elements
        self.page_title = "h1"  # Page heading selector # Tells us that we are on the correct page
        self.email_input = "//input[@class='el-input__inner']"
        self.terms_and_conditions_checkbox = "//input[@class='el-checkbox__original']"  # Learning: Specific checkbox selector
        self.terms_and_conditions_link = "//a[@href='https://linkmygear.com/terms-and-conditions/']"
        self.register_button = "//button[@class='lmg-btn lmg-btn--sm']"
        self.log_in_link = "//a[@href='#/login']"

#   def navigate_to_create_an_account_page(self, url):
#         """Navigate browser to login page"""
#         self.page.goto(url)

    def input_email(self, email):
        """Type email address into email field"""
        self.page.fill(self.email_input, email)

    def check_terms_and_conditions(self):
        """Learning: Check the terms and conditions checkbox"""
        self.page.check(self.terms_and_conditions_checkbox)  # Learning: Use .check() for checkboxes

    def uncheck_terms_and_conditions(self):
        """Learning: Uncheck the terms and conditions checkbox"""
        self.page.uncheck(self.terms_and_conditions_checkbox)  # Learning: Use .uncheck() for checkboxes

    def is_terms_and_conditions_checked(self):
        """Learning: Check if terms and conditions checkbox is already checked"""
        return self.page.is_checked(self.terms_and_conditions_checkbox)  # Learning: Returns True/False

    def click_terms_and_conditions_link(self):
        """Click terms and conditions link"""
        self.page.click(self.terms_and_conditions_link)

    def click_register_button(self):
        """Click the registration button"""
        self.page.click(self.register_button)

    def click_log_in_link(self):
        """Click log in link"""
        self.page.click(self.log_in_link)

    def is_on_create_an_account_page(self):
        """Learning: Check if currently is on login page"""
        return self.page.is_visible(self.page_title)