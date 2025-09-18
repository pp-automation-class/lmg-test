"""
KD Base Page Object Model
"""

from utils.logger import get_logger


class KdBasePage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)
        self.page_title = "//h5"

        self.menu_item_devices = "//a[text()='Devices']"
        self.menu_item_records = "//a[text()='Records']"
        self.menu_item_logbook = "//a[text()='LogBook']"
        self.logger.debug(f"Initialized {self.__class__.__name__} page object")

    def kd_navigate(self, url):
        """Navigate to a specific URL"""
        self.logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)
        self.logger.debug(f"Successfully navigated to {url}")

    def kd_click_element(self, selector):
        """Click any element by selector"""
        self.logger.debug(f"Clicking element with selector: {selector}")
        self.page.click(selector)
        self.logger.debug(f"Successfully clicked element: {selector}")

    def kd_fill_input(self, selector, value):
        """Fill input field with value"""
        self.logger.debug(f"Filling input {selector} with value: {value}")
        self.page.fill(selector, value)
        self.logger.debug(f"Successfully filled input: {selector}")

    def kd_is_element_visible(self, selector):
        self.logger.debug(f"Checking visibility of element: {selector}")
        is_visible = self.page.is_visible(selector)
        self.logger.debug(f"Element {selector} visibility: {is_visible}")
        return is_visible

    def kd_get_element_text(self, selector):
        """Get text content of an element"""
        self.logger.debug(f"Getting text from element: {selector}")
        if self.kd_is_element_visible(selector):
            text = self.page.text_content(selector)
            self.logger.debug(f"Text content from {selector}: {text}")
            return text
        self.logger.debug(f"Element not visible for text retrieval: {selector}")
        return None

    def kd_verify_page_title(self, expected_title):
        """Verify page title contains expected text"""
        self.logger.debug(f"Verifying page title contains: {expected_title}")
        actual_title = self.kd_get_element_text(self.page_title)
        if actual_title:
            result = expected_title.lower() in actual_title.lower()
            self.logger.info(
                f"Page title verification - Expected: '{expected_title}', Actual: '{actual_title}', Result: {result}"
            )
            return result
        self.logger.warning(f"Could not get page title text from selector: {self.page_title}")
        return False

    def kd_element_exists(self, xpath: str, wait: bool = False) -> bool:
        self.logger.debug(f"Checking if element exists. XPath: {xpath}, wait: {wait}")
        try:
            locator = self.page.locator(xpath)
            if wait:
                self.logger.debug("Waiting for element to become visible (timeout=5000ms)")
                locator.wait_for(state="visible", timeout=5000)
            exists = locator.is_visible()
            self.logger.debug(f"Element exists/visible for '{xpath}': {exists}")
            return exists
        except Exception as e:
            self.logger.warning(f"Exception while checking element existence for '{xpath}': {e}")
            return False

    def kd_verify_element_exists(self, xpath, wait: bool = False):
        self.logger.debug(f"Verifying element exists via kd_element_exists. XPath: {xpath}, wait: {wait}")
        return self.kd_element_exists(xpath, wait=wait)

    def kd_get_menu_item_locator(self, menu_item: str):
        locator = f"//a[text()='{menu_item}']"
        self.logger.debug(f"Constructed menu item locator for '{menu_item}': {locator}")
        return locator

    def kd_open_menu(self, menu_item: str):
        """Open a menu item by its text"""
        self.logger.info(f"Opening menu item: {menu_item}")

        if menu_item == "Devices":
            self.logger.debug("Selecting 'Devices' menu item via predefined locator")
            self.kd_click_element(self.menu_item_devices)
        elif menu_item == "Records":
            self.logger.debug("Selecting 'Records' menu item via predefined locator")
            self.kd_click_element(self.menu_item_records)
        elif menu_item == "LogBook":
            self.logger.debug("Selecting 'LogBook' menu item via predefined locator")
            self.kd_click_element(self.menu_item_logbook)
        else:
            self.logger.warning(f"Invalid menu item requested: {menu_item}")
            raise ValueError(f"Invalid menu item: {menu_item}")

        self.kd_click_element(self.kd_get_menu_item_locator(menu_item))
        self.logger.debug(f"Successfully opened menu item: {menu_item}")

