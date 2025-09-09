"""
Base Page Object Model
Contains common methods used across all pages
"""


class BasePage:
    """Base class with common page actions"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        self.page = page
        # Each child class should define this
        self.page_title = "h1"

        # self.menu_item_devices = "//a[text()='Devices']"
        # self.menu_item_records = "//a[text()='Records']"
        # self.menu_item_logbook = "//a[text()='LogBook']"

    def get_menu_item_locator(self, menu_item: str):
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

    def verify_page_title(self, expected_title):
        """Verify page title contains expected text"""
        # Use the page-specific title selector
        actual_title = self.get_element_text(self.page_title)
        if actual_title:
            return expected_title.lower() in actual_title.lower()
        return False

    def open_menu(self, menu_item: str):
        """Open a menu item by its text"""

        # if menu_item == "Devices":
        #     self.click_element(self.menu_item_devices)
        # elif menu_item == "Records":
        #     self.click_element(self.menu_item_records)
        # elif menu_item == "LogBook":
        #     self.click_element(self.menu_item_logbook)
        # else:
        #     raise ValueError(f"Invalid menu item: {menu_item}")

        self.click_element(self.get_menu_item_locator(menu_item))


