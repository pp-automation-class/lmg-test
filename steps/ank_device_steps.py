
from behave import step

from pages.ank_devices_page import AnkDevicesPage
from pages.ank_device_setting_page import AnkDeviceSetting
from pages.ank_add_device_model import AnkAddDeviceModal
from utils.logger import get_logger

logger = get_logger(__name__)


@step('ank I verify on "{page_name}" page')
def ank_verify_on_page(context, page_name):
    logger.info(f"ANK: Verifying on '{page_name}' page")
    if page_name == "My Devices":
        my_devices = AnkDevicesPage(context.page)
        result = my_devices.ank_verify_page_title(page_name)
        logger.info(f"ANK: Page verification result: {result}")
        assert result
    logger.debug(f"ANK: Successfully verified on '{page_name}' page")


@step('ank I open devices Settings')
def ank_open_devices_settings(context):
    logger.info("ANK: Opening Devices Settings")
    AnkDevicesPage(context.page).ank_open_device_settings()
    context.ank_devices_settings = AnkDeviceSetting(context.page)
    logger.debug("ANK: Successfully opened Devices Settings")


@step('ank I click "Add new device" button')
def ank_click_add_new_device(context):
    logger.info("ANK: Clicking Add new device button")
    # If the Add Device modal is already open, click the modal's Add button.
    modal = AnkAddDeviceModal(context.page)
    if modal.ank_is_modal_visible():
        modal.ank_click_add_device()
        logger.debug("ANK: Clicked Add button inside the modal")
    else:
        # Otherwise, click the Settings page Add new device button to open the modal.
        context.ank_devices_settings.ank_click_add_device()
        logger.debug("ANK: Clicked Add new device on Settings page to open modal")


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


@step('ank I verify device "{device_name}" exists in list of devices')
def ank_verify_device_exists(context, device_name):
    logger.info(f"ANK: Verifying device '{device_name}' exists in list")
    result = AnkDeviceSetting(context.page).ank_is_device_present(device_name)
    logger.info(f"ANK: Device verification result: {result}")
    assert result, f"Device '{device_name}' not found in the list"
    logger.debug(f"ANK: Successfully verified device '{device_name}' exists")


@step('ank I click the "Edit" button for device "{name}"')
def ank_click_edit_device(context, name: str):
    logger.debug(f"ANK: Clicking Edit button for device '{name}'")
    AnkDeviceSetting(context.page).ank_click_edit_device(name)


@step('ank I fill in device name "{name}"')
def ank_fill_device_name(context, name: str):
    AnkAddDeviceModal(context.page).ank_enter_device_name(name)
    logger.debug(f"ANK: Filling in device name '{name}'")


@step('ank I click "Update" button')
def ank_click_update(context):
    logger.debug("ANK: Clicking Update button")
    AnkAddDeviceModal(context.page).ank_click_update()


@step('ank I get a notification "{text}"')
def ank_get_notification(context, text: str):
    logger.debug(f"ANK: Getting notification with text '{text}'")
    AnkDevicesPage(context.page).ank_get_notification(text)


@step('ank I click on "Delete" button for device "{name}"')
def ank_click_delete_device(context, name: str):
    logger.debug(f"ANK: Clicking on Delete button for device '{name}'")
    AnkDeviceSetting(context.page).ank_click_delete_device(name)


@step('ank I click "Delete" button for confirmation')
def ank_click_delete_button(context):
    logger.debug("ANK: Clicking Delete button in confirmation dialog")
    AnkDeviceSetting(context.page).ank_click_delete_button_in_del_form()

