"""Devices Page Object Model"""
from pages.ank_base_page import AnkBasePage
from pages.ank_login_page import AnkLoginPage


class AnkDevicesPage(AnkBasePage):
    """Represents the restore password page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        self.page_title = "//h3[text()='My devices ']"
        self.device_settings_button = "//a[@href='#/device-settings']"
        self.menu_item_devices = "//a[text()='Devices']"
        self.menu_item_records= "//a[text()='Records']"
        self.menu_item_logbook= "//a[text()='LogBook']"



     def ank_device_locator(self, name: str):
        """Return the locator for a specific device"""
        return f"//div[@class='lmg-device__info']/h4[text()='{name}']"


    def ank_open_device_settings(self):
        self.ank_click_element(self.device_settings_button)


    def ank_navigate_to_devices(self):



