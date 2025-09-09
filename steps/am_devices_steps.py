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
    AmDevicesSettingsPage(context).click_add_new_device()


@step("am: Test assertion")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError("STEP: And   am: Test assertion")
