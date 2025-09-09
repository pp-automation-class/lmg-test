import logging

from behave import step

from pages.am_devices_page import AmDevicesPage
from pages.am_devices_settings_page import AmDevicesSettingsPage
from utils.am_utils import log_files_path


@step("am: I click on the gear icon Devices Settings link")
def am_click_gear_icon(context):
    """
    :type context: behave.runner.Context
    """
    logging.basicConfig(
        filename=log_files_path("devices_page.log"),
        level=logging.DEBUG,
        format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.info("Starting Devices Settings")
    AmDevicesPage(context).click_device_settings()


@step("am: I should be redirected to the Devices Settings page")
def am_verify_devices_settings__page(context):
    """
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).verify_page()


@step('am: I click on button "Add new device"')
def am_click_add_new_device(context):
    """
    :type context: behave.runner.Context
    """
    logging.debug("Clicking on Add new device button")
    AmDevicesSettingsPage(context).click_add_new_device()


@step("am: Test assertion")
def am_test_assertion(context):
    """
    :type context: behave.runner.Context
    """
    # This step is intended to demonstrate a failing hard assertion.
    # Using AssertionError ensures Behave/PyCharm reports a failure and stops (with --stop).
    assert False, "Intentional AssertionError: Test assertion should fail and stop the run"


@step("am: I Check List of devices")
def am_list_of_devices(context):
    """
    :type context: behave.runner.Context
    """
    _list = AmDevicesPage(context).get_devices_list()
    logging.info(f"List:{_list}")


@step('am: I click on dropdown "{label}" and select "{item}"')
def am_select_dropdown_item(context, label: str, item: str):
    """
    :param item:
    :param label:
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).select_dropdown_item(label, item)


@step('am: I fill in device name "{device_name}"')
def am_fill_device_name(context, device_name: str):
    """
    :param device_name:
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).fill_device_name(device_name)
    logging.info(f"Device name filled in: {device_name}")


@step('am: I click "Add new device" button')
def am_click_add_new_device(context):
    """
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).click_add_new_device_button_in_add_form()
    logging.info("Add new device button clicked")


@step('am: I should see the new device "{name}" in the devices list')
def step_impl(context, name: str):
    """
    :param name:
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).device_name_exists(name)