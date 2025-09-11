"""
Base Page Object Model
Contains common methods used across all pages
"""

from utils.logger import get_logger


class BasePage:
    """Base class with common page actions"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        self.page = page
        self.logger = get_logger(self.__class__.__name__)
        # Each child class should define this
        self.page_title = "h1"
        self.logger.debug(f"Initialized {self.__class__.__name__} page object")

    def get_menu_item_locator(self, menu_item: str):
        """Return the locator for a specific menu item"""
        return f"//a[text()='{menu_item}']"

    def navigate(self, url):
        """Navigate to a specific URL"""
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)
        self.logger.debug(f"Successfully navigated to {url}")

    def click_element(self, selector):
        """Click any element by selector"""
        self.logger.debug(f"Clicking element with selector: {selector}")
        self.page.click(selector)
        self.logger.debug(f"Successfully clicked element: {selector}")

    def fill_input(self, selector, value):
        """Fill input field with value"""
        self.logger.debug(f"Filling input {selector} with value: {value}")
        self.page.fill(selector, value)
        self.logger.debug(f"Successfully filled input: {selector}")

    def is_element_visible(self, selector):
        """Check if element is visible on page"""
        self.logger.debug(f"Checking visibility of element: {selector}")
        is_visible = self.page.is_visible(selector)
        self.logger.debug(f"Element {selector} visibility: {is_visible}")
        return is_visible

    def get_element_text(self, selector):
        """Get text content of an element"""
        if self.is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    def verify_page_title(self, expected_title):
        """Verify page title contains expected text"""
        self.logger.debug(f"Verifying page title contains: {expected_title}")
        # Use the page-specific title selector
        actual_title = self.get_element_text(self.page_title)
        if actual_title:
            result = expected_title.lower() in actual_title.lower()
            self.logger.info(f"Page title verification - Expected: '{expected_title}', Actual: '{actual_title}', Result: {result}")
            return result
        self.logger.warning(f"Could not get page title text from selector: {self.page_title}")
        return False

    def open_menu(self, menu_item: str):
        """Open a menu item by its text"""
        self.logger.info(f"Opening menu item: {menu_item}")
        self.click_element(self.get_menu_item_locator(menu_item))
        self.logger.debug(f"Successfully opened menu item: {menu_item}")


