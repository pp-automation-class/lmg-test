from pages.am_base_page import AmBasePage

DEVICES_SETTINGS_PAGE_TITLE = "//h3[contains(@class,'section-title') and text()='Devices Settings']"
ADD_NEW_DEVICE_BUTTON = "//button[.//span[text()='Add new device']]"
DEVICE_NAME_INPUT = "//input[@class='el-input__inner']"
ADD_NEW_DEVICE_BUTTON_IN_ADD_FORM = "//div[@class='form-submit']/button[.//span[text()='Add new device']]"
DEVICE_NAMES_TABLE_NAME_COLUMN = "//div[@class='el-table__body-wrapper']//td[1]"
TABLE_ROW_WITH_DEVICE_NAME = (
    "//div[@class='el-table__body-wrapper']//tr[.//td[1 and .='{name}']]"
)

EDIT_BUTTON_FOR_DEVICE_WITH_NAME = "//button[.=' Edit ']"
UPDATE_BUTTON_IN_ADD_FORM = "//div[@class='form-submit']/button[.//span[text()='Update']]"
DELETE_BUTTON_FOR_DEVICE_WITH_NAME = "//button[.=' Delete ']"
DELETE_BUTTON_IN_DEL_FORM = "//button[.='Delete']"


class AmDevicesSettingsPage(AmBasePage):
    """Page Object for the Account Manager main page ("My device")."""

    def __init__(self, context):
        # Initialize common Playwright page utilities from the base page.
        super().__init__(context)

        """
        XPath locator for the page title used to assert the main page is shown.
        """
        self.page_title = DEVICES_SETTINGS_PAGE_TITLE
        self.add_new_device_button = ADD_NEW_DEVICE_BUTTON
        self.device_name_input = DEVICE_NAME_INPUT
        self.add_new_device_button_in_add_form = ADD_NEW_DEVICE_BUTTON_IN_ADD_FORM
        self.device_names_table_name_column = DEVICE_NAMES_TABLE_NAME_COLUMN
        self.edit_button_for_device_with_name = EDIT_BUTTON_FOR_DEVICE_WITH_NAME
        self.update_button_in_add_form = UPDATE_BUTTON_IN_ADD_FORM
        self.delete_button_for_device_with_name = DELETE_BUTTON_FOR_DEVICE_WITH_NAME
        self.delete_button_in_del_form = DELETE_BUTTON_IN_DEL_FORM
        self.table_row_with_device_name = TABLE_ROW_WITH_DEVICE_NAME

        # Links to other pages

    """
    Buttons
    """

    # Add a new device
    def click_add_new_device(self):
        self.click_element(self.add_new_device_button)

    """
    Methods
    """

    # Select a dropdown item
    def select_dropdown_item(self, label: str, item: str):
        self.click_element(f"//label[text()='{label}']")
        self.click_element(f"//li[.//span[text()='{item}']]")

    # Fill device name
    def fill_device_name(self, device_name):
        self.fill_input(self.device_name_input, device_name)

    # Click add new device button
    def click_add_new_device_button_in_add_form(self):
        self.click_element(self.add_new_device_button_in_add_form)

    def device_name_exists(self, name: str):
        self.get_row_with_device_name(name)

    def click_edit_device(self, name):
        self.click_device_button(name, self.edit_button_for_device_with_name)

    def click_update_button_in_add_form(self):
        self.click_element(self.update_button_in_add_form)

    def click_delete_device(self, name):
        self.click_device_button(name, self.delete_button_for_device_with_name)

    def get_row_with_device_name(self, name: str):
        selector = self.table_row_with_device_name.format(name=name)
        locator = self.page.locator(selector)
        self.element_exists(selector, timeout=1000)
        assert locator.count(), f"Device '{name}' not found in the list of devices."
        return selector

    def click_device_button(self, name: str, button_selector: str):
        selector = self.get_row_with_device_name(name)+button_selector
        self.click_element(selector)

    def click_delete_button_in_del_form(self):
        self.click_element(self.delete_button_in_del_form)

    def get_notification(self, text):
        selector = f"//p[.='{text}']"
        self.verify_page(selector)
