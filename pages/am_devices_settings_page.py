from pages.am_base_page import AmBasePage


DEVICES_SETTINGS_PAGE_TITLE = "//h3[contains(@class,'section-title') and text()='Devices Settings']"
ADD_NEW_DEVICE_BUTTON = "//button[.//span[text()='Add new device']]"


class AmDevicesSettingsPage(AmBasePage):
    """Page Object for the Account Manager main page ("My device")."""

    def __init__(self, context):
        # Initialize common Playwright page utilities from the base page.
        super().__init__(context)

        """
        XPath locator for the page title used to assert the main page is shown.
        """
        self.page_title = DEVICES_SETTINGS_PAGE_TITLE
        self.add_new_device_button = ADD_NEW_DEVICE_BUTTON

        # Links to other pages

    """
    Buttons
    """
    def click_add_new_device(self):
        self.click_element(self.add_new_device_button)
