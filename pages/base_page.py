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
