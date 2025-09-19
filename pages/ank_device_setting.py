"""Ank Device Settings Page Object Model (simple)"""
from pages.ank_base_page import AnkBasePage


class AnkDeviceSetting(AnkBasePage):
    """Simplified POM for the Ank Devices Settings page"""

    def __init__(self, page):
        super().__init__(page)

        # Basic locators
        self.page_title = "//h1[text()='Devices Settings']"
        self.ank_add_device_button = "//button[.//span[text()='Add new device']]"

        # Table locators
        self.device_table = page.locator("table").nth(1)
        self.table_rows = "//div[@class='el-table__body-wrapper']//tbody/tr"
        self.row_with_device_name = (
            "//div[@class='el-table__body-wrapper']//tr[.//td[1 and .='{name}']]"
        )

    # Actions
    def ank_click_add_device(self):
        self.logger.info("Clicking add device button")
        self.ank_add_device_button.click()
        self.logger.debug("Successfully clicked add device button")

    def ank_click_edit_device(self, device_name: str):
        self.logger.info(f"Clicking edit button for device: {device_name}")
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Edit").click()
        self.logger.debug(f"Successfully clicked edit for device: {device_name}")

    def ank_click_delete_device(self, device_name: str):
        self.logger.info(f"Clicking delete button for device: {device_name}")
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Delete").click()
        self.logger.debug(f"Successfully clicked delete for device: {device_name}")

    # Queries
    def ank_get_device_count(self) -> int:
        self.logger.debug("Getting device count from table")
        count = self.device_table.locator("tbody tr").count()
        self.logger.info(f"Found {count} devices in table")
        return count

    def ank_is_device_present(self, device_name: str) -> bool:
        self.logger.debug(f"Checking if device is present: {device_name}")
        locator = self.page.locator(f"tr:has-text('{device_name}')").is_visible()
        count = locator.count()
        is_present = count > 0
        self.logger.info(f"Device '{device_name}' present: {is_present} (found {count} matches)")
        return is_present

    def ank_click_update_button(self):
        self.logger.info("Clicking update button in modal")
        self.ank_click_element("//div[@class='form-submit']/button[.//span[text()='Update']]")
        self.logger.debug("Successfully clicked update button in modal")

    def ank_get_notification(self, text):
        selector = f"//p[.='{text}']"
        self.ank_verify_page_title(selector)
        self.logger.debug(f"Notification with text '{text}' is visible")


    def ank_click_delete_button(self):
        self.logger.info("Clicking delete button in modal")
        self.ank_click_element("//div[@class='form-submit']/button[.//span[text()='Delete']]")
        self.logger.debug("Successfully clicked delete button in modal")

