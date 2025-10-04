"""
Base Page Object Model
Contains common methods used across all pages
"""

from utils.logger import get_logger

# LINKMYGEAR_URL = "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
# LOGIN_URL = "https://dev.linkmygear.com/login"
# CREATE_ACCOUNT_URL = "https://dev.linkmygear.com/register"
# RESTORE_PASSWORD_URL = "https://dev.linkmygear.com/restorePassword"
# VERIFY_PATH = "//h5[.='Login to Your Account']"
# ANK_EMAIL = "akr.autotest@gmail.com"
# ANK_PASSWORD = "12345"


class AnkBasePage:
    """Base class with common page actions (synchronous Playwright API)."""

    def __init__(self, page):
        """Initialize with the Playwright Page instance"""
        self.page = page
        self.logger = get_logger(self.__class__.__name__)
        # Each child class should define this
        self.page_title = "//h5"
        self.logger.debug(f"Initialized {self.__class__.__name__} page object")

    def ank_get_menu_item_locator(self, menu_item: str):
        """Return the locator for a specific menu item"""
        return f"//a[text()='{menu_item}']"

    # Navigation
    def ank_navigate(self, url: str):
        """Navigate to a specific URL"""
        self.logger.info(f"ANK: Navigating to URL: {url}")
        self.page.goto(url)
        self.logger.debug(f"ANK: Successfully navigated to {url}")

    # Actions
    def ank_click_element(self, selector) -> None:
        """Click any element by selector"""
        self.logger.debug(f"ANK: Clicking element with selector: {selector}")
        self.page.click(selector)
        self.logger.debug(f"ANK: Successfully clicked element: {selector}")

    def ank_fill_input(self, selector, value):
        """Fill input field with value"""
        self.logger.debug(f"ANK: Filling input {selector} with value: {value}")
        self.page.fill(selector, value)
        self.logger.debug(f"ANK: Successfully filled input: {selector}")

    # Visibility & text
    def ank_is_element_visible(self, selector):
        """Check if the element is visible on the page"""
        self.logger.debug(f"ANK: Checking visibility of element: {selector}")
        is_visible = self.page.is_visible(selector)
        self.logger.debug(f"ANK: Element {selector} visibility: {is_visible}")
        return is_visible

    def ank_get_element_text(self, selector):
        """Get text content of an element, if visible"""
        if self.ank_is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    # Page-level convenience
    def ank_verify_page_title(self, expected_text):
        """Verify that the page title element contains expected_text (case-insensitive)."""
        self.logger.debug(f"ANK: Verifying page title contains: {expected_text}")
        actual_title = self.ank_get_element_text(self.page_title)
        if actual_title:
            result = expected_text.lower() in actual_title.lower()
            self.logger.info(f"ANK: Page title verification - Expected: '{expected_text}', Actual: '{actual_title}', Result: {result}")
            return result
        self.logger.warning(f"ANK: Could not get page title text from selector: {self.page_title}")
        return False

    def ank_open_menu(self, menu_item: str):
        """Open a specific menu item"""
        self.logger.info(f"ANK: Opening menu item: {menu_item}")
        self.ank_click_element(self.ank_get_menu_item_locator(menu_item))
        self.logger.debug(f"ANK: Successfully opened menu item: {menu_item}")

    def ank_get_notification(self, text):
        """Get notification element by its text"""
        selector = f"//p[.='{text}']"
        self.ank_verify_page(selector)
        return selector

    def ank_verify_page(self, selector):
        """Verify that a specific element is visible on the page"""
        self.logger.debug(f"ANK: Verifying page element is visible: {selector}")
        if not self.ank_is_element_visible(selector):
            self.logger.error(f"ANK: Element not visible: {selector}")
            raise Exception(f"Element not visible: {selector}")
        self.logger.debug(f"ANK: Element is visible: {selector}")

    # Helpful waits (optional but commonly needed)
    def ank_element_exists(self, xpath, wait: bool = False):
        """Return True if an element matching xpath exists and is visible.
        If wait=True, wait up to 5s for it to become visible.
        """
        try:
            locator = self.page.locator(xpath)
            if wait:
                locator.wait_for(state="visible", timeout=5000)
            return locator.is_visible()
        except Exception:
            return False

    def ank_verify_element_exists(self, xpath, wait: bool = False):
        """Convenience wrapper over ank_element_exists"""
        return self.ank_element_exists(xpath, wait=wait)
