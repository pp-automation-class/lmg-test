"""
KD Base Page Object Model
"""

class KdBasePage:
    """Base class with common page actions (KD methods)"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        self.page = page
        # Each child class can override this selector
        self.page_title = "h1"

    # Navigation
    def kd_navigate(self, url):
        """Navigate to a specific URL"""
        self.page.goto(url)

    def kd_click_element(self, selector):
        """Click any element by selector"""
        self.page.click(selector)

    def kd_fill_input(self, selector, value):
        """Fill input field with value"""
        self.page.fill(selector, value)

    def kd_is_element_visible(self, selector):
        """Check if element is visible on page"""
        return self.page.is_visible(selector)

    def kd_get_element_text(self, selector):
        """Get text content of an element if visible; otherwise None"""
        if self.kd_is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    def kd_verify_page_title(self, expected_title):
        """Verify page title contains expected text using page_title selector"""
        actual_title = self.kd_get_element_text(self.page_title)
        if actual_title:
            return expected_title.lower() in actual_title.lower()
        return False
