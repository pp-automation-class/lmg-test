"""
Base Page Object Model
Contains common methods used across all pages
"""


class LStarkBasePage:
    """Base class with common page actions"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        self.page = page
        # Each child class should define this
        self.page_title = "h1"

        # self.menu_item_devices = "//a[text()='Devices']"
        # self.menu_item_records= "//a[text()='Records']"
        # self.menu_item_logbook = "//a[text()='LogBook']"
        # We created function to get_menu_item_locator instead of keeping these 3 lines
        # so we created variable {menu_item} - instead of: Devices, Records, and LogBook

    def ls_get_menu_item_locator(self, menu_item: str):
        """Return the locator for a specific menu item"""
        return f"//a[text()='{menu_item}']"

    def navigate(self, url):
        """Navigate to a specific URL"""
        self.page.goto(url)

    def click_element(self, selector):
        """Click any element by selector"""
        self.page.click(selector)

    def fill_input(self, selector, value):
        """Fill input field with value"""
        self.page.fill(selector, value)

    def is_element_visible(self, selector):
        """Check if element is visible on page"""
        return self.page.is_visible(selector)

    def get_element_text(self, selector):
        """Get text content of an element"""
        if self.is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    def ls_verify_page_title(self, expected_title):
        """Verify page title contains expected text"""
        # Use the page-specific title selector
        actual_title = self.get_element_text(self.page_title)
        if actual_title:
            return expected_title.lower() in actual_title.lower()
        return False

    def ls_open_menu(self, menu_item: str):
        """Click on a specific menu item"""
        self.click_element(self.ls_get_menu_item_locator(menu_item))