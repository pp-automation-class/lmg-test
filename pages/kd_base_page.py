"""
KD Base Page Object Model
"""


class KdBasePage:

    def __init__(self, page):
        self.page = page
        self.page_title = "//h5"

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
        return self.page.is_visible(selector)

    def kd_get_element_text(self, selector):
        if self.kd_is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    def kd_verify_page_title(self, expected_title):
        actual_title = self.kd_get_element_text(self.page_title)
        if actual_title:
            return expected_title.lower() in actual_title.lower()
        return False

    def kd_element_exists(self, xpath: str, wait: bool = False) -> bool:
        try:
            locator = self.page.locator(xpath)
            if wait:
                locator.wait_for(state="visible", timeout=5000)
            return locator.is_visible()
        except Exception:
            return False

    def verify_element_exists(self, xpath, wait: bool = False):
        return self.kd_element_exists(xpath, wait=wait)
