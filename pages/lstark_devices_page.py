"""Devices Page's Page Object Model"""

from pages.lstark_base_page import LStarkBasePage

class LStarkDevicesPage(LStarkBasePage):
    """Learning: Represents the devices' page with its elements and actions"""

    def __init__(self, page):
        """Learning: Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h3[contains(text(),'My device')]"
        self.device_settings_button = "//a[@href='#/device-settings']"

        # We found 3 locators for menu items below and moved them to the base_page since they are common
        # self.menu_item_devices = "//a[text()='Devices']"
        # self.menu_item_records= "//a[text()='Records']"
        # self.menu_item_logbook = "//a[text()='LogBook']"

        # and created 2 functions in the base page to work with them:
        # 1. def ls_get_menu_item_locator(self, menu_item: str):
        # 2. def ls_open_menu(self, menu_item: str):


        # We created function to get devices by name, but each device has unique name,
        # so we created variable {name} to be replaced with device name we'll use
        #
        # def get_device_name_locator(self, name: str):
        #     """Learning: Return the locator for a specific device"""
        #     return f"//div[@class='lmg-device__info']/h4[text()='{name}']"

        # def open_device_settings(self):
        #     self.click_element(self.device_settings_button)



