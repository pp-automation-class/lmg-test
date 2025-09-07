"""
Base Page Object Model
Contains common methods used across all pages
"""
# from typing import Optional
#
# # Optional: if you want to type hints for "Page"
# try:
#     from playwright.sync_api import Page
# except Exception:
#     Page = object # fallback to avoid import errors if Playwright not present at type-check time

LINKMYGEAR_URL = "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com"
LOGIN_URL = "https://dev.linkmygear.com/login"
CREATE_ACCOUNT_URL = "https://dev.linkmygear.com/register"
RESTORE_PASSWORD_URL = "https://dev.linkmygear.com/restorePassword"
VERIFY_PATH = "//h5[.='Login to Your Account']"
ANKR_EMAIL = "autotest@gmail.com"
ANKR_PASSWORD = "12345"

class BasePage:
    """Base class with common page actions (synchronous Playwright API)."""

    def __init__(self, page):
        """Initialize with the Playwright Page instance"""
        self.page = page
        # Each child class can override this (e.g., "h1", "h5", etc.)
        self.page_title = "h5"
        # Default timeout for operations (ms). Adjust as needed.
        self.default_timeout_ms = 5000

    # Navigation
    def navigate(self, url: str) -> None:
        """Navigate to a specific URL"""
        self.page.goto(url, timeout=self.default_timeout_ms)

    # Actions
    def click_element(self, selector: str) -> None:
        """Click any element by selector"""
        self.page.click(selector, timeout=self.default_timeout_ms)

    def fill_input(self, selector: str, value: str) -> None:
        """Fill input field with value"""
        self.page.fill(selector, value, timeout=self.default_timeout_ms)

    # Visibility & text
    def is_element_visible(self, selector):
        """Check if the element is visible on the page"""
        return self.page.is_visible(selector, timeout=self.default_timeout_ms)

    def get_element_text(self, selector: str):
        """Get text content of an element, if visible"""
        if self.is_element_visible(selector):
            return self.page.text_content(selector, timeout=self.default_timeout_ms)
        return None

    # Page-level convenience
    def verify_page_title(self, expected_text: str) -> bool:
        """Verify that the page title element contains expected_text (case-insensitive)."""
        actual = self.get_element_text(self.page_title)
        return bool(actual) and expected_text.lower() in actual.lower()

    # Helpful waits (optional but commonly needed)
    def wait_for_url(self, expected_substring: str, timeout_ms: int = None) -> bool:
        """Wait until the current URL contains expected_substring."""
        to = timeout_ms or self.default_timeout_ms
        self.page.wait_for_url(f"**{expected_substring}**", timeout=to)
        return expected_substring in self.page.url

    def wait_for_visible(self, selector: str, timeout_ms: int = None) -> None:
        """Wait for an element to become visible."""
        to = timeout_ms or self.default_timeout_ms
        self.page.wait_for_selector(selector, state="visible", timeout=to)
