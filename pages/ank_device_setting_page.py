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
        self.delete_button_in_del_form = "//button[.='Delete']"
        # Actions
    def ank_click_add_device(self):
        self.ank_add_device_button.click()

    def ank_click_edit_device(self, device_name: str):
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Edit").click()

    def ank_click_delete_device(self, device_name: str):
        row = self.page.locator(f"tr:has-text('{device_name}')")
        row.get_by_role("button", name="Delete").click()

    # Queries
    def ank_get_device_count(self) -> int:
        count = self.device_table.locator("tbody tr").count()
        return count

    def ank_is_device_present(self, device_name: str) -> bool:
        return self.page.locator(f"//div/span[text()='{device_name}']").is_visible()

    def ank_get_notification(self, text: str):
        selector = f"//p[.='{text}']"
        self.ank_verify_page_title(selector)

    def ank_click_delete_button_in_del_form(self):
        self.ank_click_element(self.delete_button_in_del_form)




