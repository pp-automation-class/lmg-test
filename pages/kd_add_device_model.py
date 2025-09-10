from pages.kd_base_page import KdBasePage


class KdAddDeviceModal(KdBasePage):
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

    def kd_select_device_type(self, device_type: str):
        # Click on the dropdown
        self.kd_click_element(self.device_type_dropdown)
        # Select the option
        self.kd_click_element(self.get_device_type_option_locator(device_type))

    def kd_enter_device_name(self, name: str):
        self.kd_fill_input(self.device_name_input, name)

    def kd_select_imei(self, imei: str):
        self.imei_dropdown.click()
        self.page.get_by_text(imei).click()

    def kd_click_add_device(self):
        self.kd_click_element(self.add_device_button)

    def kd_close_modal(self):
        self.close_button.click()

    def kd_is_modal_visible(self):
        return self.modal.is_visible()