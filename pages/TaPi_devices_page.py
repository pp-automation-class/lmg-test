from pages.base_page import BasePage


class TaPiDevicesPage(BasePage):
    """Represents the Devices page for the TaPi brand with its elements and actions."""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        super().__init__(page)

        # Devices page header/title. Use normalize-space to tolerate extra spaces.
        self.page_title = "//h3[normalize-space(.)='My Devices']"
        # Device settings navigation button/link
        self.device_settings_button = "//a[@href='#/device-settings']"

    def get_device_locator(self, name: str):
        """Return the locator for a specific device card by its display name."""
        # Match the device name exactly inside the device info header
        return f"//div[@class='lmg-device__info']/h4[normalize-space(text())='{name}']"

    def open_device_settings(self):
        """Open the device settings page from the Devices screen."""
        self.click_element(self.device_settings_button)
