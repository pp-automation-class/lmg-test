from behave import step
from pages.lstark_login_page import LStarkLoginPage
from pages.lstark_devices_page import LStarkDevicesPage

@step("ls I am on the {env} environment login page")
def ls_navigate_to_login_page(context, env):
    # Map environment names to their respective URLs
    environments = {
        'prod': 'https://app.linkmygear.com/',
        'dev': 'https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com/login',
        'dev-v2': 'http://dev-v2.linkmygear.com/#/login'
    }

    # Get the URL for the specified environment
    url = environments.get(env.lower())
    if not url:
        raise ValueError(f"Unknown environment: {env}. Available: prod, dev, dev-v2")

    # Navigate to the appropriate login page
    context.page.goto(url)
    # Wait for page to load completely
    context.page.wait_for_load_state('networkidle')


@step('ls I enter {text} in the email field')
def ls_input_email(context,text):
    login_page = LStarkLoginPage(context.page)
    login_page.ls_enter_email(text)


@step('ls I enter {text} in the password field')
def ls_input_password(context,text):
    login_page = LStarkLoginPage(context.page)
    login_page.ls_enter_password(text)


@step("ls I click the login button")
def ls_click_login_button(context):
    login_page = LStarkLoginPage(context.page)
    login_page.ls_click_login()


# @step("ls I should be redirected to the devices page")
# def ls_verify_devices_page(context):
#     ls_verify_page_title = LStarkDevicesPage(context.page)





