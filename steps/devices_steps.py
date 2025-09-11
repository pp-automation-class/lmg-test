from behave import step

from pages.add_device_modal import AddDeviceModal
from pages.base_page import BasePage
from pages.devices_page import DevicesPage
from pages.devices_settings_page import DeviceSettings
from utils.logger import get_logger

logger = get_logger(__name__)


@step('Verify I on "{page_name}" page')
def verify_on_page(context, page_name):
    logger.info(f"Step: Verifying on '{page_name}' page")
    if page_name == "My Devices":
        my_devices = DevicesPage(context.page)
        result = my_devices.verify_page_title(page_name)
        logger.info(f"Page verification result: {result}")
        assert result
    logger.debug(f"Successfully verified on '{page_name}' page")


@step('I open Devices Settings')
def open_devices_settings(context):
    logger.info("Step: Opening Devices Settings")
    context.page.get_by_role("heading", name="My devices").get_by_role("link").click()
    context.devices_page = DeviceSettings(context.page)
    logger.debug("Successfully opened Devices Settings")


@step('Press Add new device button')
def press_add_new_device(context):
    logger.info("Step: Pressing Add new device button")
    context.devices_page.click_add_device()
    logger.debug("Successfully pressed Add new device button")


@step('Choose "{device_type}" device type')
def choose_device_type(context, device_type):
    logger.info(f"Step: Choosing device type '{device_type}'")
    device_popup = AddDeviceModal(context.page)
    device_popup.select_device_type(device_type)
    logger.debug(f"Successfully chose device type '{device_type}'")


@step('Fill out name "{device_name}" of device')
def fill_device_name(context, device_name):
    logger.info(f"Step: Filling out device name '{device_name}'")
    device_popup = AddDeviceModal(context.page)
    device_popup.enter_device_name(device_name)
    logger.debug(f"Successfully filled device name '{device_name}'")


@step('Press add new device button')
def press_add_device_button(context):
    logger.info("Step: Pressing add new device button in modal")
    AddDeviceModal(context.page).click_add_device()
    logger.debug("Successfully pressed add new device button in modal")


@step('Verify device "{device_name}" exists in list of devices')
def verify_device_exists(context, device_name):
    logger.info(f"Step: Verifying device '{device_name}' exists in list")
    result = DeviceSettings(context.page).is_device_present(device_name)
    logger.info(f"Device verification result: {result}")
    assert result, f"Device '{device_name}' not found in the list"
    logger.debug(f"Successfully verified device '{device_name}' exists")


@step('Go to "{page_name}" page')
def step_impl(context, page_name):
    logger.info(f"Step: Going to '{page_name}' page")
    BasePage(context.page).open_menu(page_name)
    logger.debug(f"Successfully navigated to '{page_name}' page")
