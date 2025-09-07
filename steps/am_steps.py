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
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # By default, use the email from the environment variables
    AmLoginPage(context).enter_email()


@step("am: I enter valid password in the password field")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # By default, use the password from the environment variables
    AmLoginPage(context).enter_password()


@step("am: I click the login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    AmLoginPage(context).click_button()


@step("am: I should be redirected to the devices page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    AmDevicesPage(context).verify_page()
