from pages.base_page import BasePage


class AddDeviceModal(BasePage):
    def __init__(self, page):
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

    def get_device_type_option_locator(self, option: str):
        return f"//li[@role='option']/span[text()='{option}']"

    def select_device_type(self, device_type: str):
        self.logger.info(f"Selecting device type: {device_type}")
        # Click on the dropdown
        self.click_element(self.device_type_dropdown)
        # Select the option
        self.click_element(self.get_device_type_option_locator(device_type))
        self.logger.debug(f"Successfully selected device type: {device_type}")

    def enter_device_name(self, name: str):
        self.logger.info(f"Entering device name: {name}")
        self.fill_input(self.device_name_input, name)
        self.logger.debug(f"Successfully entered device name: {name}")
        
    def select_imei(self, imei: str):
        self.logger.info(f"Selecting IMEI: {imei}")
        self.imei_dropdown.click()
        self.page.get_by_text(imei).click()
        self.logger.debug(f"Successfully selected IMEI: {imei}")
        
    def click_add_device(self):
        self.logger.info("Clicking add device button in modal")
        self.click_element(self.add_device_button)
        self.logger.debug("Successfully clicked add device button in modal")
        
    def close_modal(self):
        self.logger.info("Closing add device modal")
        self.close_button.click()
        self.logger.debug("Successfully closed add device modal")
        
    def is_modal_visible(self):
        self.logger.debug("Checking if add device modal is visible")
        is_visible = self.modal.is_visible()
        self.logger.debug(f"Add device modal visibility: {is_visible}")
        return is_visible