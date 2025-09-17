"""Devices Page's Page Object Model"""

from pages.lstark_base_page import LStarkBasePage

class LStarkDevicesPage(LStarkBasePage):
    """Learning: Represents the devices' page with its elements and actions"""

    def __init__(self, page):
        """Learning: Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h3[contains(text(),'My device')]"
        self.device_settings_button = "//a[@href='#/device-settings']"

      # We moved ALL these to the base page since they are common for all pages
        # self.menu_item_devices = "//a[text()='Devices']"
        # self.menu_item_records= "//a[text()='Records']"
        # self.menu_item_logbook = "//a[text()='Logbook']"
        #
        # We created function to get devices by name, but each device has unique name,
        # so we created variable {name} to be replaced with device name we'll use
        #
        # def ls_get_device_name_locator(self, name: str):
        #     """Learning: Return the locator for a specific device"""
        #     return f"//div[@class='lmg-device__info']/h4[text()='{name}']"



