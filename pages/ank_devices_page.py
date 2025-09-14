"""Devices Page Object Model"""
from pages.ank_base_page import AnkBasePage


class AnkDevicesPage(AnkBasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h3[text()='My devices ']"
        self.device_settings_button = "//a[@href='#/device-settings']"


    def ank_get_device_locator(self, name: str):
        """Return the locator for a specific device"""
        return f"//div[@class='lmg-device__info']/h4[text()='{name}']"


    def ank_open_device_settings(self):
        self.ank_click_element(self.device_settings_button)
