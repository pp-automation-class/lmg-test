from pages.base_page import BasePage


class DeviceSettings(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        # Locators
        self.page_title = page.get_by_role("heading", name="Devices Settings")
        self.add_device_button = page.get_by_role("button", name="Add new device")
        self.device_table = page.locator("table").nth(1)
        
    def click_add_device(self):
        self.add_device_button.click()
        
    def click_edit_device(self, device_name: str):
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Edit").click()
        
    def click_delete_device(self, device_name: str):
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Delete").click()
        
    def get_device_count(self):
        return self.device_table.locator("tbody tr").count()
        
    def is_device_present(self, device_name: str):
        return self.page.locator(f"//div/span[text()='{device_name}']")