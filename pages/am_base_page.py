class AmBasePage:
    """
    Base page object that wraps a browser automation `page` instance
    and exposes a small set of reusable UI actions and common selectors.

    This class centralizes:
      - Navigation helpers (navigate)
      - Generic element interactions (click, fill, visibility checks)
      - Frequently used selectors (page title, email input, button, login link)

    Expected `page` API:
      - goto(url): navigate to a URL
      - click(selector): click an element matching selector
      - fill(selector, value): fill an input
      - is_visible(selector): check element visibility
      - text_content(selector): get element's text
      - wait_for_selector(selector): wait until an element is present/visible
    """

    def __init__(self, context):
        """
        Initialize the base page with a browser `page` object.

        Args:
            context: An object exposing Playwright methods used in this class.
        """
        self.page = context.page
        self.email = ""
        # Commonly reused selectors across pages:
        self.page_title = "h1"  # Page heading (CSS)
        self.email_input = "//input[@type='email']"  # Email input (XPath)
        self.button = "//button"  # Generic button (XPath)
        self.go_to_login = "//a[@href='#/login']"  # Login link (XPath)

    def navigate(self, url):
        """
        Navigate the browser to the provided URL.

        Args:
            url (str): Absolute or relative URL to open.
        """
        self.page.goto(url)

    def click_element(self, selector):
        """
        Click an element located by the given selector.

        Args:
            selector (str): CSS/XPath selector for the target element.
        """
        self.page.click(selector)

    def fill_input(self, selector, value):
        """
        Fill an input element with the given value.

        Args:
            selector (str): CSS/XPath selector for the input element.
            value (str): The text to enter into the input.
        """
        self.page.fill(selector, value)

    def is_element_visible(self, selector):
        """
        Check whether an element matching the selector is visible.

        Args:
            selector (str): CSS/XPath selector.

        Returns:
            bool: True if visible; otherwise False.
        """
        return self.page.is_visible(selector)

    def get_element_text(self, selector):
        """
        Get the text content of an element if it is visible.

        Args:
            selector (str): CSS/XPath selector.

        Returns:
            str | None: The element text if visible; None otherwise.
        """
        if self.is_element_visible(selector):
            return self.page.text_content(selector)
        return None

    def verify_page(self, selector=None):
        """
        Wait until the page is considered loaded by ensuring the title element
        is present/visible in the DOM.
        """
        if not selector:
            selector = self.page_title
        try:
            self.page.wait_for_selector(selector, timeout=3000)
        except Exception as e:
            assert False, f"Text not found! {e}"

    def check(self, selector: str) -> None:
        """Check the checkbox"""
        self.page.locator(selector).check()

    def uncheck(self, selector: str) -> None:
        """Uncheck the checkbox"""
        self.page.locator(selector).uncheck()

    def enter_email(self, email=None):
        """
        Enter an email into the email input field.

        Args:
            email (str): The email address to type into the field.
        """
        if not email:
            email = self.email
        self.fill_input(self.email_input, email)

    def click_button(self):
        """
        Click a generic button using the shared button selector.

        Note:
            If multiple buttons exist on the page,
            this will click the first match.
        """
        self.click_element(self.button)

    def click_go_to_login(self):
        """
        Click the 'Go to Login' link to navigate to the login view.
        """
        self.click_element(self.go_to_login)
