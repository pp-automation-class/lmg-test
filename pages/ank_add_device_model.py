"""Devices Page Object Model"""

from pages.ank_base_page import AnkBasePage

class AnkAddDeviceModal(AnkBasePage):
    """Represents the devices page with its elements and actions"""

    def __init__(self, page):
        """Initialize with the Playwright page object"""
        super().__init__(page)

        # Modal locators
        self.modal = page.locator("dialog")
        self.modal_title = self.modal.get_by_role("heading", name="Add device")
        self.close_button = self.modal.get_by_role("button", name="Close")

        # Form field locators
        self.device_type_dropdown = "//div[./label[text()='Device type']]//div[contains(@class,'el-select__wrapper')]"

        self.device_name_input = "//input[@class='el-input__inner']"
        self.imei_dropdown = page.locator("div").filter(has_text="IMEI").nth(2).locator("div").nth(1)

        # Button locators
        self.add_device_button = "//div[@class='form-submit']//span[text()='Add new device']"


    def ank_get_device_type_option_locator(self, option: str):
        return f"//li[@role='option']/span[text()='{option}']"

    def ank_select_device_type(self, device_type: str):
        self.logger.info(f"ANK: Selecting device type: {device_type}")
        # Click on the dropdown
        self.ank_click_element(self.device_type_dropdown)
        # Select the option
        self.ank_click_element(self.ank_get_device_type_option_locator(device_type))
        self.logger.debug(f"ANK: Successfully selected device type: {device_type}")

    def ank_enter_device_name(self, name: str):
        self.logger.info(f"ANK: Entering device name: {name}")
        self.ank_fill_input(self.device_name_input, name)
        self.logger.debug(f"ANK: Successfully entered device name: {name}")

    def ank_select_imei(self, imei: str):
        self.logger.info(f"ANK: Selecting IMEI: {imei}")
        self.imei_dropdown.click()
        self.page.get_by_text(imei).click()
        self.logger.debug(f"ANK: Successfully selected IMEI: {imei}")

    def ank_click_add_device(self):
        self.logger.info("ANK: Clicking add device button in modal")
        self.ank_click_element(self.add_device_button)
        self.logger.debug("ANK: Successfully clicked add device button in modal")

    def ank_close_modal(self):
        self.logger.info("ANK: Closing add device modal")
        self.close_button.click()
        self.logger.debug("ANK: Successfully closed add device modal")

    def ank_is_modal_visible(self):
        self.logger.debug("ANK: Checking if add device modal is visible")
        is_visible = self.modal.is_visible()
        self.logger.debug(f"ANK: Add device modal visibility: {is_visible}")
        return is_visible
