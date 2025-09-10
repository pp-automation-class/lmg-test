"""
Base Page Object Model for Playwright-Behave Framework
"""
from abc import ABC, abstractmethod
from typing import Optional, List, Any
from playwright.sync_api import Page, Locator, expect
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage(ABC):
    """
    Base Page Object class that all page objects should inherit from.
    Provides common functionality and enforces consistent patterns.
    """

    def __init__(self, page: Page, base_url: str = ""):
        """
        Initialize the base page.

        Args:
            page: Playwright page instance
            base_url: Base URL for the application
        """
        self.page = page
        self.base_url = base_url
        self.timeout = 30000  # 30 seconds default timeout

    @property
    @abstractmethod
    def url_path(self) -> str:
        """
        Abstract property that must be implemented by child classes.
        Should return the relative path for the page.
        """
        pass

    @property
    def full_url(self) -> str:
        """Return the full URL for this page."""
        return f"{self.base_url.rstrip('/')}{self.url_path}"

    def navigate(self) -> None:
        """Navigate to this page."""
        logger.info(f"Navigating to {self.full_url}")
        self.page.goto(self.full_url)
        self.wait_for_page_load()

    def wait_for_page_load(self) -> None:
        """
        Wait for page to be fully loaded.
        Override in child classes for specific loading indicators.
        """
        self.page.wait_for_load_state("networkidle", timeout=self.timeout)

    def get_title(self) -> str:
        """Get the page title."""
        return self.page.title()

    def get_url(self) -> str:
        """Get the current page URL."""
        return self.page.url

    def wait_for_element(self, selector: str, state: str = "visible") -> Locator:
        """
        Wait for an element to reach a specific state.

        Args:
            selector: CSS selector or other locator strategy
            state: Element state to wait for (visible, hidden, attached, detached)

        Returns:
            Locator object
        """
        locator = self.page.locator(selector)
        locator.wait_for(state=state, timeout=self.timeout)
        return locator

    def click_element(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Click on an element.

        Args:
            selector: CSS selector or other locator strategy
            timeout: Optional timeout override
        """
        timeout = timeout or self.timeout
        logger.info(f"Clicking element: {selector}")
        locator = self.page.locator(selector)
        locator.click(timeout=timeout)

    def type_text(self, selector: str, text: str, clear: bool = True, timeout: Optional[int] = None) -> None:
        """
        Type text into an input field.

        Args:
            selector: CSS selector for the input field
            text: Text to type
            clear: Whether to clear the field first
            timeout: Optional timeout override
        """
        timeout = timeout or self.timeout
        logger.info(f"Typing text into {selector}: {text}")
        locator = self.page.locator(selector)

        if clear:
            locator.clear(timeout=timeout)

        locator.type(text, timeout=timeout)

    def get_text(self, selector: str, timeout: Optional[int] = None) -> str:
        """
        Get text content from an element.

        Args:
            selector: CSS selector
            timeout: Optional timeout override

        Returns:
            Text content of the element
        """
        timeout = timeout or self.timeout
        locator = self.page.locator(selector)
        return locator.text_content(timeout=timeout) or ""

    def get_attribute(self, selector: str, attribute: str, timeout: Optional[int] = None) -> Optional[str]:
        """
        Get an attribute value from an element.

        Args:
            selector: CSS selector
            attribute: Attribute name
            timeout: Optional timeout override

        Returns:
            Attribute value or None if not found
        """
        timeout = timeout or self.timeout
        locator = self.page.locator(selector)
        return locator.get_attribute(attribute, timeout=timeout)

    def is_element_visible(self, selector: str, timeout: Optional[int] = None) -> bool:
        """
        Check if an element is visible.

        Args:
            selector: CSS selector
            timeout: Optional timeout override

        Returns:
            True if element is visible, False otherwise
        """
        timeout = timeout or self.timeout
        try:
            locator = self.page.locator(selector)
            locator.wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    def is_element_present(self, selector: str) -> bool:
        """
        Check if an element is present in DOM (regardless of visibility).

        Args:
            selector: CSS selector

        Returns:
            True if element is present, False otherwise
        """
        return self.page.locator(selector).count() > 0

    def get_elements(self, selector: str) -> List[Locator]:
        """
        Get all elements matching the selector.

        Args:
            selector: CSS selector

        Returns:
            List of Locator objects
        """
        return self.page.locator(selector).all()

    def scroll_to_element(self, selector: str) -> None:
        """
        Scroll to an element.

        Args:
            selector: CSS selector
        """
        logger.info(f"Scrolling to element: {selector}")
        locator = self.page.locator(selector)
        locator.scroll_into_view_if_needed()

    def take_screenshot(self, filename: Optional[str] = None, full_page: bool = False) -> bytes:
        """
        Take a screenshot of the page.

        Args:
            filename: Optional filename to save screenshot
            full_page: Whether to capture the full page

        Returns:
            Screenshot as bytes
        """
        screenshot_options = {"full_page": full_page}
        if filename:
            screenshot_options["path"] = filename

        logger.info(f"Taking screenshot: {filename or 'in-memory'}")
        return self.page.screenshot(**screenshot_options)

    def wait_for_navigation(self, action_func, timeout: Optional[int] = None) -> None:
        """
        Wait for navigation after performing an action.

        Args:
            action_func: Function that triggers navigation
            timeout: Optional timeout override
        """
        timeout = timeout or self.timeout
        with self.page.expect_navigation(timeout=timeout):
            action_func()

    def switch_to_new_tab(self) -> Page:
        """
        Switch to a new tab/window.

        Returns:
            New page object
        """
        with self.page.context.expect_page() as new_page_info:
            # Trigger action that opens new tab here
            pass

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page

    def close_page(self) -> None:
        """Close the current page."""
        logger.info("Closing page")
        self.page.close()

    # Assertion helpers using Playwright's expect
    def assert_title_contains(self, expected_text: str) -> None:
        """Assert that page title contains expected text."""
        expect(self.page).to_have_title(expected_text)

    def assert_url_contains(self, expected_text: str) -> None:
        """Assert that current URL contains expected text."""
        expect(self.page).to_have_url(expected_text)

    def assert_element_visible(self, selector: str) -> None:
        """Assert that an element is visible."""
        expect(self.page.locator(selector)).to_be_visible()

    def assert_element_hidden(self, selector: str) -> None:
        """Assert that an element is hidden."""
        expect(self.page.locator(selector)).to_be_hidden()

    def assert_text_contains(self, selector: str, expected_text: str) -> None:
        """Assert that element text contains expected text."""
        expect(self.page.locator(selector)).to_contain_text(expected_text)

    def assert_text_equals(self, selector: str, expected_text: str) -> None:
        """Assert that element text equals expected text."""
        expect(self.page.locator(selector)).to_have_text(expected_text)

    def assert_attribute_equals(self, selector: str, attribute: str, expected_value: str) -> None:
        """Assert that element attribute equals expected value."""
        expect(self.page.locator(selector)).to_have_attribute(attribute, expected_value)


class PageObjectManager:
    """
    Manager class to handle page object instances and browser context.
    """
