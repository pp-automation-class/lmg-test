# This module defines the main page object for the Account Manager UI.
# It exposes locators and behaviors specific to the "My device" landing page.

from pages.am_base_page import AmBasePage


class AmDevicesPage(AmBasePage):
    """Page Object for the Account Manager main page ("My device")."""

    def __init__(self, context):
        # Initialize common Playwright page utilities from the base page.
        super().__init__(context)
        """
        XPath locator for the page title used to assert the main page is shown.
        """
        self.page_title = "//h3[contains(text(), 'My device')]"
