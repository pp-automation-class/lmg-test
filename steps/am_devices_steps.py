from behave import step

from pages.am_devices_page import AmDevicesPage
from pages.am_devices_settings_page import AmDevicesSettingsPage


@step("am: I click on the gear icon Devices Settings link")
def am_click_gear_icon(context):
    """
    :type context: behave.runner.Context
    """
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
    context.logger.debug("Clicking on Add new device button")
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
    context.logger.debug(f"Device name filled in: {device_name}")


@step('am: I click "Add new device" button')
def am_click_add_new_device(context):
    """
    :type context: behave.runner.Context
    """
    context.logger.debug("Add new device button clicked")
    AmDevicesSettingsPage(context).click_add_new_device_button_in_add_form()


@step('am: I should see the device "{name}" in the devices list')
def am_device_name_exists(context, name: str):
    """
    :param name:
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).device_name_exists(name)


@step('am: I click on button "Edit" for device "{name}"')
def am_click_edit_device(context, name: str):
    """
    :param name:
    :type context: behave.runner.Context
    """
    context.logger.debug(f"Clicking on Edit button for device '{name}'")
    AmDevicesSettingsPage(context).click_edit_device(name)


@step('am: I click "Update" button')
def am_click_update(context):
    """
    :type context: behave.runner.Context
    """
    context.logger.debug("Add update button clicked")
    AmDevicesSettingsPage(context).click_update_button_in_add_form()


@step('am: I click on button "Delete" for device "{name}"')
def am_click_delete_device(context, name: str):
    """
    :param name:
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).click_delete_device(name)


@step('am: I click "Delete" button for confirmation')
def am_click_delete_button(context):
    """
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).click_delete_button_in_del_form()


@step('am: I get a notification "{text}"')
def am_get_notification(context, text: str):
    """
    :param text:
    :type context: behave.runner.Context
    """
    AmDevicesSettingsPage(context).get_notification(text)