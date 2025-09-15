from pages.am_base_page import AmBasePage


GOOGLE_MAP_PAGE_TITLE = "//a[@aria-label='Google apps']"
BUTTON_DIRECTIONS = "//button/div[.='Directions']"
BUTTON_DRIVING = "//button/div[@aria-label='Driving']"
STARTING_POINT_INPUT = "//input[@aria-label='Choose starting point, or click on the map...']"


class AmGoogleMapPage(AmBasePage):
    """Page Object for the Account Manager main page ("My device")."""

    def __init__(self, context):
        # Initialize common Playwright page utilities from the base page.
        super().__init__(context)

        """
        XPath locator for the page title used to assert the main page is shown.
        """
        self.page_title = GOOGLE_MAP_PAGE_TITLE
        self.button_directions = BUTTON_DIRECTIONS
        self.button_driving = BUTTON_DRIVING
        self.starting_point_input = STARTING_POINT_INPUT


    def click_button_directions(self):
        selector = self.button_directions
        self.click_element(selector)

    def click_button_driving(self):
        selector = self.button_driving
        self.click_element(selector)

    def input_starting_point(self, address):
        self.fill_input(self.starting_point_input, address)

    def close_page(self):
        old_page = self.page.context.pages[0]
        self.page.close()
        return old_page
