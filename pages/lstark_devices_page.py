"""Devices Page's Page Object Model"""

from pages.lstark_base_page import LStarkBasePage

class LStarkDevicesPage(LStarkBasePage):
    """Learning: Represents the devices' page with its elements and actions"""

    def __init__(self, page):
        """Learning: Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h3[contains(text(),'My device')]"
        self.device_settings_button = "//a[@href='#/device-settings']"




