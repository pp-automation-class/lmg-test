"""Devices Page Page Object Model"""
from pages.kd_base_page import KdBasePage


class KdDevicesPage(KdBasePage):
    """Represents the devices page with its elements and actions"""

    def __init__(self, page):
        """Initialize with Playwright page object"""
        super().__init__(page)

        self.page_title = "//h3[text()='My devices ']"
        self.device_settings_button = "//a[@href='#/device-settings']"


    def kd_get_device_locator(self, name: str):
        """Return the locator for a specific device"""
        return f"//div[@class='lmg-device__info']/h4[text()='{name}']"

    def kd_open_device_settings(self):
        self.kd_click_element(self.device_settings_button)