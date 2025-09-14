
from behave import step

from pages.ank_devices_page import AnkDevicesPage
from pages.ank_device_setting import AnkDeviceSetting
from pages.ank_add_device_model import AnkAddDeviceModal
from utils.logger import get_logger

logger = get_logger(__name__)


@step('ank Verify I on "{page_name}" page')
def ank_verify_on_page(context, page_name):
    logger.info(f"ANK: Verifying on '{page_name}' page")
    if page_name == "My Devices":
        my_devices = AnkDevicesPage(context.page)
        result = my_devices.ank_verify_page_title(page_name)
        logger.info(f"ANK: Page verification result: {result}")
        assert result
     logger.debug(f"ANK: Successfully verified on '{page_name}' page")


@step('ank I open Devices Settings')
def ank_open_devices_settings(context):
    logger.info("ANK: Opening Devices Settings")
    AnkDevicesPage(context.page).ank_open_device_settings()
    context.ank_devices_settings = AnkDeviceSetting(context.page)
    logger.debug("ANK: Successfully opened Devices Settings")


@step('ank I press Add new device button')
def ank_press_add_new_device(context):
    logger.info("ANK: Pressing Add new device button")
    # Ensure we have the settings page object
    settings = getattr(context, 'ank_devices_settings', AnkDeviceSetting(context.page))
    settings.ank_click_add_device()
    logger.debug("ANK: Successfully pressed Add new device button")


@step('ank I choose "{device_type}" device type')
def ank_choose_device_type(context, device_type):
    logger.info(f"ANK: Choosing device type '{device_type}'")
    device_popup = AnkAddDeviceModal(context.page)
    device_popup.ank_select_device_type(device_type)
    logger.debug(f"ANK: Successfully chose device type '{device_type}'")


@step('ank I fill out name "{device_name}" of device')
def ank_fill_device_name(context, device_name):
    logger.info(f"ANK: Filling out device name '{device_name}'")
    device_popup = AnkAddDeviceModal(context.page)
    device_popup.ank_enter_device_name(device_name)
    logger.debug(f"ANK: Successfully filled device name '{device_name}'")


@step('ank I press add new device button')
def ank_press_add_device_button(context):
    logger.info("ANK: Pressing add new device button in modal")
    AnkAddDeviceModal(context.page).ank_click_add_device()
    logger.debug("ANK: Successfully pressed add new device button in modal")


@step('ank I verify device "{device_name}" exists in list of devices')
def ank_verify_device_exists(context, device_name):
    logger.info(f"ANK: Verifying device '{device_name}' exists in list")
    settings = AnkDeviceSetting(context.page)
    result = settings.ank_is_device_present(device_name)
    logger.info(f"ANK: Device verification result: {result}")
    assert result, f"Device '{device_name}' not found in the list"
    logger.debug(f"ANK: Successfully verified device '{device_name}' exists")
