"""Devices Page Page Object Model"""
from pages.base_page import BasePage


class DevicesPage(BasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        super().__init__(page)

        self.page_title = "//h3[text()='My devices ']"
        self.device_settings_button = "//a[@href='#/device-settings']"

    def get_show_on_map_locator(self, device_name: str):
        return f"//div[contains(@class, 'lmg-device')][./div/h4[text()='{device_name}']]//button[text()=' Show on map ']"

    def get_device_locator(self, name: str):
        """Return the locator for a specific device"""
        return f"//div[@class='lmg-device__info']/h4[text()='{name}']"

    def open_device_settings(self):
        self.click_element(self.device_settings_button)
