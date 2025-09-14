from behave import step
import os
from pages.ank_login_page import AnkLoginPage
from pages.ank_create_account_page import AnkCreateAccountPage
from pages.ank_restore_password_page import AnkRestorePasswordPage


@step('ank I am on the {env} environment login page')
def ank_navigate_to_login_page(context, env):
    # Map environment names to their respective URLs
    environments = {
        'prod': 'https://app.linkmygear.com/',
        'dev': 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com/login',
        'dev-v2': 'https://dev-v2.linkmygear.com/#/login'
    }

    # Get the URL for the specified environment
    url = environments.get(env.lower())
    if not url:
        raise ValueError(f"Unknown environment: {env}. Available: prod, dev, dev-v2")

    # Navigate to the appropriate login page
    context.page.goto(url)
    # Wait for page to load completely
    context.page.wait_for_load_state('networkidle')


@step('ank I enter "{text}" in the email field')
def ank_input_email(context, text):
    login_page = AnkLoginPage(context.page)
    login_page.ank_enter_email(text)


@step('ank I enter "{text}" in the password field')
def ank_input_password(context, text):
    login_page = AnkLoginPage(context.page)
    login_page.ank_enter_password(text)


@step('ank I click the "{button_text}" button')
def ank_click_login_button(context, button_text):
    login_page = AnkLoginPage(context.page)
    login_page.ank_click_login()


@step("ank I should be redirected to the dashboard page")
def ank_verify_dashboard_page(context):
    login_page = AnkLoginPage(context.page)
    assert login_page.ank_verify_dashboard_page(), "Dashboard page was not displayed"


@step('ank I click the "Create an Account" link')
def ank_click_create_account_link(context):
    login_page = AnkLoginPage(context.page)
    login_page.ank_click_create_account()


@step("ank I should be redirected to registration page")
def ank_registration_page(context):
    registration_page = AnkCreateAccountPage(context.page)
    assert registration_page.ank_verify_title_contains("Create an Account")


@step('ank I should see "Create an Account" heading')
def ank_create_account_heading(context):
    registration_page = AnkCreateAccountPage(context.page)
    assert registration_page.ank_verify_title_contains("Create an Account")


@step('ank I should see error message "Sorry, unrecognized username or password"')
def ank_error_loging_message(context):
    loging_page = AnkLoginPage(context.page)
    assert loging_page.ank_verify_element_exists(loging_page.error_message, wait=True)


@step("ank I click on forgot the password link")
def ank_click_forgot_password(context):
    login_page = AnkLoginPage(context.page)
    login_page.ank_click_forgot_password()


@step("ank I should be redirected to password restore page")
def ank_redirect_restore_page(context):
    restore_page = AnkRestorePasswordPage(context.page)
    assert restore_page.ank_verify_title_contains("Restore Password")


@step('ank I should see "Restore Password" heading')
def ank_see_restore_password_heading(context):
    restore_page = AnkRestorePasswordPage(context.page)
    assert restore_page.ank_verify_title_contains("Restore Password")


@step('ank I should see error message "Email is required"')
def ank_see_error_message_email(context):
    login_page = AnkLoginPage(context.page)
    assert login_page.ank_verify_title_contains("Email is required")


@step('ank I should see error message "Password is required"')
def ank_see_error_message_password(context):
    login_page = AnkLoginPage(context.page)
    assert login_page.ank_verify_title_contains("Password is required")


@step("ank Wait for {sec} seconds")
def ank_wait_for_sec(context, sec):
    context.page.ank_wait_for_timeout(int(sec) * 1000)


from pages.ank_devices_page import AnkDevicesPage
from pages.ank_device_setting import AnkDeviceSetting
from pages.add_device_modal import AddDeviceModal


@step('ank Verify I on "{page_name}" page')
def ank_verify_on_page(context, page_name):
    devices_page = AnkDevicesPage(context.page)
    result = devices_page.ank_verify_page_title(page_name)
    assert result, f"Expected to be on '{page_name}' page, but title did not match"


@step('ank I open Devices Settings')
def ank_open_devices_settings(context):
    AnkDevicesPage(context.page).ank_open_device_settings()
    context.ank_devices_settings = AnkDeviceSetting(context.page)


@step('ank I press Add new device button')
def ank_press_add_new_device(context):
    # Ensure we have the settings page object
    settings = getattr(context, 'ank_devices_settings', AnkDeviceSetting(context.page))
    settings.ank_click_add_device()


@step('ank I choose "{device_type}" device type')
def ank_choose_device_type(context, device_type):
    device_popup = AddDeviceModal(context.page)
    device_popup.select_device_type(device_type)


@step('ank I fill out name "{device_name}" of device')
def ank_fill_device_name(context, device_name):
    device_popup = AddDeviceModal(context.page)
    device_popup.enter_device_name(device_name)


@step('ank I press add new device button')
def ank_press_add_device_button(context):
    AddDeviceModal(context.page).click_add_device()


@step('ank I verify device "{device_name}" exists in list of devices')
def ank_verify_device_exists(context, device_name):
    settings = AnkDeviceSetting(context.page)
    assert settings.ank_is_device_present(device_name), f"Device '{device_name}' not found in the list" 