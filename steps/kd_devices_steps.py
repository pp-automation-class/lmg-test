from behave import step

from pages.add_device_modal import AddDeviceModal
@step('Verify I on "{page_name}" page')
def verify_on_page(context, page_name):
    if page_name == "My Devices":
        my_devices = KDDevicesPage(context.page)
        assert my_devices.verify_page_title(page_name)


@step('I open Devices Settings')
def open_devices_settings(context):
    context.page.get_by_role("heading", name="My devices").get_by_role("link").click()
    context.devices_page = DeviceSettings(context.page)


@step('Press Add new device button')
def press_add_new_device(context):
    context.devices_page.click_add_device()


@step('Choose "{device_type}" device type')
def choose_device_type(context, device_type):
    device_popup = AddDeviceModal(context.page)
    device_popup.select_device_type(device_type)


@step('Fill out name "{device_name}" of device')
def fill_device_name(context, device_name):
    device_popup = AddDeviceModal(context.page)
    device_popup.enter_device_name(device_name)


@step('Press add new device button')
def press_add_device_button(context):
    AddDeviceModal(context.page).click_add_device()


@step('Verify device "{device_name}" exists in list of devices')
def verify_device_exists(context, device_name):
    assert context.devices_page.is_device_present(device_name)
