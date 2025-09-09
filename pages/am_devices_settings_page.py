from pages.am_base_page import AmBasePage


DEVICES_SETTINGS_PAGE_TITLE = "//h3[contains(@class,'section-title') and text()='Devices Settings']"
ADD_NEW_DEVICE_BUTTON = "//button[.//span[text()='Add new device']]"
DEVICE_NAME_INPUT = "//input[@class='el-input__inner']"
ADD_NEW_DEVICE_BUTTON_IN_ADD_FORM = "//div[@class='form-submit']/button[.//span[text()='Add new device']]"


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

        # Links to other pages

    """
    Buttons
    """
    # Add new device
    def click_add_new_device(self):
        self.click_element(self.add_new_device_button)

    """
    Methods
    """
    # Select dropdown item
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
        devices = self.page.locator("//div[@class='el-table__body-wrapper']//td[1]").all_text_contents()
        assert name in devices, f"Device name '{name}' not found in the list of devices."


