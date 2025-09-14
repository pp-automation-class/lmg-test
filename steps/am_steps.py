import time

from behave import step

from pages.am_create_account_page import AmCreateAccountPage
from pages.am_login_page import AmLoginPage
from pages.am_devices_page import AmDevicesPage
from pages.am_restore_password_page import AmRestorePasswordPage
from utils.am_utils import random_email
from utils.logger import setup_logger


@step("am: I navigate to the {env} environment login page")
def am_navigate_to_login_page(context, env):
    """
    :param env:
    :type context: behave.runner.Context
    """
    # Environment type saved in context
    # Map environment names to their respective URLs
    context.env = env
    context.logger = setup_logger("test_framework", "DEBUG")
    AmLoginPage(context).navigate_to_login()


@step("am: I enter valid email in the email field")
def am_enter_valid_email(context):
    """
    :type context: behave.runner.Context
    """
    # By default, use the email from the environment variables
    AmLoginPage(context).enter_email()


@step("am: I enter valid password in the password field")
def am_enter_valid_password(context):
    """
    :type context: behave.runner.Context
    """
    # By default, use the password from the environment variables
    AmLoginPage(context).enter_password()


@step("am: I click the login button")
def am_click_login_button(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).click_button()


@step("am: I should be redirected to the devices page")
def am_verify_devices_page(context):
    """
    :type context: behave.runner.Context
    """
    AmDevicesPage(context).verify_page()


@step('am: I enter "{email}" in the email field')
def am_enter_email(context, email):
    """
    :param email:
    :type context: behave.runner.Context
    """
    AmLoginPage(context).enter_email(email)


@step('am: I enter "{password}" in the password field')
def am_enter_password(context, password):
    """
    :param password:
    :type context: behave.runner.Context
    """
    AmLoginPage(context).enter_password(password)


@step("am: I get the invalid login error message")
def am_get_login_error(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).get_login_error_message()


@step("am: I don't fill the email field")
def am_dont_fill_email_field(context):
    """
    :type context: behave.runner.Context
    """
    login_page = AmLoginPage(context)
    login_page.click_element(login_page.email_input)


@step("am: I get the empty email error message")
def am_get_empty_email_error(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).get_empty_email_error_message()


@step("am: I don't fill the password field")
def am_dont_fill_password_field(context):
    """
    :type context: behave.runner.Context
    """
    login_page = AmLoginPage(context)
    login_page.click_element(login_page.password_input)


@step("am: I get the empty password error message")
def am_get_empty_password_error(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).get_empty_password_error_message()


@step('am: I click on "Forgot password" link')
def am_click_forgot_password(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).click_forgot_password()


@step('am: I wait for "Restore Password" form to be visible')
def am_wait_for_restore_password_form(context):
    """
    :type context: behave.runner.Context
    """
    restore_page = AmRestorePasswordPage(context)
    restore_page.verify_page()


@step("am: I fill valid email in the restore email field")
def am_fill_valid_email(context):
    """
    :type context: behave.runner.Context
    """
    restore_page = AmRestorePasswordPage(context)
    restore_page.enter_email()


@step('am: I click on "Send" button')
def am_click_send_button(context):
    """
    :type context: behave.runner.Context
    """
    restore_page = AmRestorePasswordPage(context)
    restore_page.click_button()


@step("am: I wait for {sec} seconds")
def am_wait_for_some_seconds(context, sec):
    """
    :param sec:
    :type context: behave.runner.Context
    """
    time.sleep(float(sec))


@step("am: I get the strange message. Let's assume that everything is fine :)")
def am_get_send_result_message(context):
    """
    :type context: behave.runner.Context
    """
    restore_page = AmRestorePasswordPage(context)
    restore_page.get_forgot_password_send_result_message()


@step("am: I don't fill the restore email field")
def am_dont_fill_restore_email_field(context):
    """
    :type context: behave.runner.Context
    """
    restore_page = AmRestorePasswordPage(context)
    restore_page.click_element(restore_page.forgot_password_email_input_selector)


@step('am: I get "The empty restore email" error message')
def am_get_empty_restore_email_error(context):
    """
    :type context: behave.runner.Context
    """
    AmRestorePasswordPage(context).get_empty_restore_email_error_message()


@step('am: I fill "{email}" in the restore email field')
def am_enter_restore_email(context, email):
    restore_page = AmRestorePasswordPage(context)
    restore_page.enter_email(email)


@step('am: I get "The wrong format restore email" error message')
def am_get_wrong_format_restore_email_error(context):
    """
    :type context: behave.runner.Context
    """
    restore_page = AmRestorePasswordPage(context)
    restore_page.get_wrong_format_restore_email_error_message()


@step('am: I click on "Create an account" link')
def am_click_create_an_account(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).click_create_an_account()


@step('am: I wait for "Create an Account" form to be visible')
def am_wait_for_create_an_account_form(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.verify_page()


@step("am: I fill a random email in email input field")
def am_enter_random_email(context):
    create_page = AmCreateAccountPage(context)
    email = random_email()
    create_page.enter_email(email)
    context.logger.debug(f"Account is creating for: {email}")


@step("am: I check the terms and conditions checkbox")
def am_check_terms_checkbox(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.check(create_page.checkbox_accept)


@step('am: I click on "Register" button')
def am_click_register_button(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.click_button()


@step("am: I fill an existed email in email input field")
def am_fill_existed_email(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.enter_email(create_page.email)


@step('am: I get "The user already exists" error message')
def get_user_already_exists_error_message(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.get_user_already_exists_error_message()


@step('am: I get "Please enter you email address" error message')
def get_empty_email_error_message(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.get_empty_email_error_message()


@step('am: I fill "{email}" in email input field')
def am_enter_some_email(context, email):
    create_page = AmCreateAccountPage(context)
    create_page.enter_email(email)


@step('am: I get "Please enter a valid email address" error message')
def get_enter_valid_email_error_message(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.get_enter_valid_email_error_message()


@step("am: I click on email label to trigger validation")
def am_click_email_label(context):
    """
    :type context: behave.runner.Context
    """
    restore_page = AmRestorePasswordPage(context)
    restore_page.click_element(restore_page.email_label_selector)


@step("am: I click on registration email label to trigger validation")
def am_click_reg_email_label(context):
    """
    :type context: behave.runner.Context
    """
    create_page = AmCreateAccountPage(context)
    create_page.click_element(create_page.email_label_selector)


@step("am: I login with valid credentials")
def am_login_with_valid_credentials(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).login()
