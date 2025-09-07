from behave import step
from pages.am_login_page import AmLoginPage
from pages.am_devices_page import AmDevicesPage

@step("am: I navigate to the {env} environment login page")
def am_navigate_to_login_page(context, env):
    """
    :param env:
    :type context: behave.runner.Context
    """
    # Environment type saved in context
    # Map environment names to their respective URLs
    context.env = env
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