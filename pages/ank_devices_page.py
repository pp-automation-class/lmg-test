"""Devices Page Object Model"""
from pages.ank_base_page import AnkBasePage


class AnkDevicesPage(AnkBasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        # Be lenient on whitespace/casing in the Devices header
        self.page_title = "//h3[contains(normalize-space(.), 'My devices')]"
        self.device_settings_button = "//a[@href='#/device-settings']"


    def get_show_on_map_locator(self, device_name: str):
        return f"//div[contains(@class, 'lmg-device')][./div/h4[text()='{device_name}']]//button[text()=' Show on map ']"


    def ank_get_device_locator(self, name: str):
        """Return the locator for a specific device"""
        # Match the device name exactly inside the device info header
        return f"//div[@class='lmg-device__info']/h4[text()='{name}']"

    def ank_open_device_settings(self):
        """Open the device settings page from the Devices screen."""
        self.ank_click_element(self.device_settings_button)
