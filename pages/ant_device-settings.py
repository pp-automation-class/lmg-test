"""
Device Settings Page Object Model
Contains methods for interacting with the Device Settings Page
"""

from pages.base_page import BasePage


class AntDevicePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
        # Locators
        self.add_new_device = "//button[.//span[text()='Add new device']]"
        self.add_device = "//h3[@class='modal-title' and text()='Add device']"
        self.device_type = "//label[text()='Device type']"
        self.device_airguard = "//li[.//span[text()='Airguard other']]"
        self.device_name_field = "//input[@class='el-input__inner']"
        self.add_new_device_button = "//div[@class='form-submit']/button[.//span[text()='Add new device']]"
        self.delete_device_modal = "//h3[@class='modal-title' and text()='Delete device']"
        self.confirm_delete_button = "//button[text()='Delete']"
        self.delete_confirmation_message = "//*[contains(@class, 'el-message__content') and contains(text(), 'Device deleted')]"
