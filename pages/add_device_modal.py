from pages.base_page import BasePage


class AddDeviceModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        # Modal locators
        self.modal = page.locator("dialog")
        self.modal_title = self.modal.get_by_role("heading", name="Add device")
        self.close_button = self.modal.get_by_role("button", name="Close")
        
        # Form field locators
        self.device_type_dropdown = page.locator("dialog div:has-text('* Device type') >> div").nth(1)
        self.device_name_input = page.get_by_placeholder("Device name")
        self.imei_dropdown = page.locator("div").filter(has_text="IMEI").nth(2).locator("div").nth(1)
        
        # Button locators
        self.add_device_button = self.modal.get_by_role("button", name="Add new device")
        
    def select_device_type(self, device_type: str):
        # Click on the dropdown - find the div containing "Airguard" text that also has an img element
        dropdown = self.page.locator("dialog").locator("div:has(img)").filter(has_text="Airguard").nth(0)
        dropdown.click()
        # Select the option
        self.page.get_by_role("option", name=device_type).click()
        
    def enter_device_name(self, name: str):
        self.device_name_input.fill(name)
        
    def select_imei(self, imei: str):
        self.imei_dropdown.click()
        self.page.get_by_text(imei).click()
        
    def click_add_device(self):
        self.add_device_button.click()
        
    def close_modal(self):
        self.close_button.click()
        
    def is_modal_visible(self):
        return self.modal.is_visible()