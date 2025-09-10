from behave import step
from pages.kd_devices_page import KdDevicesPage
from pages.kd_devices_settings_page import KdDevicesSettingsPage
from pages.kd_add_device_model import KdAddDeviceModal


@step('kd Verify I on "{page_name}" page')
def kd_verify_on_page(context, page_name):
    if page_name == "My Devices":
        my_devices = KdDevicesPage(context.page)
        assert my_devices.kd_verify_page_title(page_name)


@step('kd I open Devices Settings')
def kd_open_devices_settings(context):
    context.page.get_by_role("heading", name="My devices").get_by_role("link").click()
    context.kd_devices_page = KdDevicesSettingsPage(context.page)


@step('kd Press Add new device button')
def kd_press_add_new_device(context):
    context.kd_devices_page.click_add_device()


@step('kd Choose "{device_type}" device type')
def kd_choose_device_type(context, device_type):
    device_popup = KdAddDeviceModal(context.page)
    device_popup.kd_select_device_type(device_type)


@step('kd Fill out name "{device_name}" of device')
def kd_fill_device_name(context, device_name):
    device_popup = KdAddDeviceModal(context.page)
    device_popup.kd_enter_device_name(device_name)


@step('kd Press add new device button')
def kd_press_add_device_button(context):
    KdAddDeviceModal(context.page).kd_click_add_device()


@step('kd Verify device "{device_name}" exists in list of devices')
def kd_verify_device_exists(context, device_name):
    device_locator = context.kd_devices_page.kd_get_device_locator(device_name)
    assert context.kd_devices_page.kd_verify_element_exists(device_locator, wait=True), f"Device '{device_name}' not found on the devices page."
