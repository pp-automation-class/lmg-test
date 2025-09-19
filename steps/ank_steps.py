from behave import step

from pages.ank_login_page import AnkLoginPage
from pages.ank_devices_page import AnkDevicesPage
from pages.ank_create_account_page import AnkCreateAccountPage
from pages.ank_restore_password_page import AnkRestorePasswordPage


@step('ank I am on the {env} environment login page')
def ank_navigate_to_login_page(context, env):
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


@step("ank I wait for {sec} seconds")
def ank_wait_for_sec(context, sec):
    context.page.ank_wait_for_timeout(int(sec) * 1000)


@step("ank I should be redirected to the devices page")
def ank_should_be_on_device_page(context):
     """Verify that user is on the Devices page after successful login."""
     device_page = AnkDevicesPage(context.page)
     # Wait for routing/rendering to settle
     context.page.wait_for_load_state('networkidle')
     # Explicitly wait for the Devices header to become visible
     context.page.wait_for_selector(device_page.page_title, state="visible")
     assert device_page.ank_verify_page_title("My device"), (
         "Expected to be on Devices page, but the page title did not match."
    )


@step('ank I click the "{button_text}" button')
def ank_click_login_button(context, button_text):
    login_page = AnkLoginPage(context.page)
    login_page.ank_click_login()


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
    assert loging_page.ank_get_element_text(loging_page.error_message)


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
    assert login_page.ank_get_element_text(login_page.email_required_message)


@step('ank I should see error message "Password is required"')
def ank_see_error_message_password(context):
    login_page = AnkLoginPage(context.page)
    assert login_page.ank_get_element_text(login_page.password_required_message)


@step('ank I click the {button_text} button"')
def ank_click_send_button(context, button_text):
    restore_page = AnkRestorePasswordPage(context.page)
    restore_page.ank_click_send()


@step("ank I wait for {sec} seconds")
def ank_wait_for_sec(context, sec):
    context.page.wait_for_timeout(int(sec) * 1000)
