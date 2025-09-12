"""
Base Page Object Model
Contains common methods used across all pages
"""

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
        self.page_title = "//h5"


    # Navigation
    def ank_navigate(self, url: str):
        """Navigate to a specific URL"""
        self.page.goto(url)

    # Actions
    def ank_click_element(self, selector) -> None:
        """Click any element by selector"""
        self.page.click(selector)

    def ank_fill_input(self, selector, value):
        """Fill input field with value"""
        self.page.fill(selector, value)

    # Visibility & text
    def ank_is_element_visible(self, selector):
        """Check if the element is visible on the page"""
        return self.page.is_visible(selector)

    def ank_get_element_text(self, selector):
        """Get text content of an element, if visible"""
        if self.ank_is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    # Page-level convenience
    def ank_verify_page_title(self, expected_text):
        """Verify that the page title element contains expected_text (case-insensitive)."""
        actual_title = self.ank_get_element_text(self.page_title)
        if actual_title:
            return expected_text.lower() in actual_title.lower()
        return False

    # Helpful waits (optional but commonly needed)
    def ank_element_exists(self, xpath, wait: bool = False):
        try:
            locator = self.page.locator(xpath)
            if wait:
                locator.wait_for(state="visible", timeout=5000)
            return locator.is_visible()
        except Exception:
            return False

    def ank_verify_element_exists(self, xpath, wait: bool = False):
        return self.ank_element_exists(xpath, wait=wait)
