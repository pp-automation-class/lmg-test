# This module defines the main page object for the Account Manager UI.
# It exposes locators and behaviors specific to the "My device" landing page.

from pages.am_base_page import AmBasePage


DEVICES_PAGE_TITLE = "//h3[contains(text(), 'My device')]"
RECORDS_LINK = "//a[@href='#/map']"
LOGBOOK_LINK = "//a[@href='#/logbook']"
PROFILE_LINK = "//a[@href='#/profile']"
SUBSCRIPTION_LINK = "//a[@href='#/subscription']"
DEVICE_SETTINGS_LINK = "//a[@href='#/device-settings']"
LOGOUT_LINK = "//a/span[.='Log out']"
NOTIFICATIONS_BUTTON = "//button[contains(@class,'profile-btn')]"
RESEND_ACTIVATION_BUTTON = "//button[contains(.,'Resend activation link')]"
DEMO_JUMP_BUTTON = "//button[contains(.,'Demo Jump')]"
DEVICES_NAMES_LOCATOR = "//div[@class='lmg-device']/div/h4"
DEVICES_BUTTONS_LOCATOR = "//div[@class='lmg-device']/div/button[.='Upload Logs']"


class AmDevicesPage(AmBasePage):
    """Page Object for the Account Manager main page ("My device")."""

    def __init__(self, context):
        # Initialize common Playwright page utilities from the base page.
        super().__init__(context)

        """
        XPath locator for the page title used to assert the main page is shown.
        """
        self.page_title = DEVICES_PAGE_TITLE
        # Links to other pages
        self.device_settings_link = DEVICE_SETTINGS_LINK
        self.records_link = RECORDS_LINK
        self.logbook_link = LOGBOOK_LINK
        self.profile_link = PROFILE_LINK
        self.subscription_link = SUBSCRIPTION_LINK
        self.logout_link = LOGOUT_LINK
        # Buttons
        self.notifications_button = NOTIFICATIONS_BUTTON
        self.resend_activation_button = RESEND_ACTIVATION_BUTTON
        self.demo_jump_button = DEMO_JUMP_BUTTON

    """
    Navigation to other pages
    """

    def click_device_settings(self):
        """Open the devices settings page."""
        self.click_element(self.device_settings_link)

    def click_records(self):
        """Navigate to the record map page."""
        self.click_element(self.records_link)

    def click_logbook(self):
        """Navigate to the logbook page."""
        self.click_element(self.logbook_link)

    def click_profile(self):
        """Navigate to the profile page."""
        self.click_element(self.profile_link)

    def click_subscription(self):
        """Navigate to the subscription page."""
        self.click_element(self.subscription_link)

    def click_logout(self):
        """Log out of the account."""
        self.click_element(self.logout_link)

    """
    Buttons
    """
    def click_notifications(self):
        """Click the notification button to open the notifications panel."""
        self.click_element(self.notifications_button)

    def click_resend_activation(self):
        """Click the resend activation button."""
        self.click_element(self.resend_activation_button)

    def click_demo_jump(self):
        """Click the demo jump button."""
        self.click_element(self.demo_jump_button)

    """
    Get devices elements
    """

    def get_devices_list(self):
        dev_list = []  # result
        """Get a list of device names displayed on the page."""
        names = self.page.locator(DEVICES_NAMES_LOCATOR)
        buttons = self.page.locator(DEVICES_BUTTONS_LOCATOR)
        # Wait until at least one element is present (optional but recommended)
        # Get count and iterate
        count = names.count()
        if count == buttons.count() and count > 0:
            for i in range(count):
                dev_list.append([names.nth(i).inner_text(), buttons.nth(i)])
        return dev_list
