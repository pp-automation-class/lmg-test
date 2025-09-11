from pages.base_page import BasePage


class DeviceSettings(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        # Locators
        self.page_title = page.get_by_role("heading", name="Devices Settings")
        self.add_device_button = page.get_by_role("button", name="Add new device")
        self.device_table = page.locator("table").nth(1)
        
    def click_add_device(self):
        self.logger.info("Clicking add device button")
        self.add_device_button.click()
        self.logger.debug("Successfully clicked add device button")
        
    def click_edit_device(self, device_name: str):
        self.logger.info(f"Clicking edit button for device: {device_name}")
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Edit").click()
        self.logger.debug(f"Successfully clicked edit for device: {device_name}")
        
    def click_delete_device(self, device_name: str):
        self.logger.info(f"Clicking delete button for device: {device_name}")
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Delete").click()
        self.logger.debug(f"Successfully clicked delete for device: {device_name}")
        
    def get_device_count(self):
        self.logger.debug("Getting device count from table")
        count = self.device_table.locator("tbody tr").count()
        self.logger.info(f"Found {count} devices in table")
        return count
        
    def is_device_present(self, device_name: str):
        self.logger.debug(f"Checking if device is present: {device_name}")
        locator = self.page.locator(f"//div/span[text()='{device_name}']")
        count = locator.count()
        is_present = count > 0
        self.logger.info(f"Device '{device_name}' present: {is_present} (found {count} matches)")
        return is_present