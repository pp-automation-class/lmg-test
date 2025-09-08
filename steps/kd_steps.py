from behave import step
from pages.kd_login_page import KdLoginPage

@step('kd I am on the {env} environment login page')
def kd_navigate_to_login_page(context, env):
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


@step('kd I enter "{text}" in the email field')
def kd_input_email(context, text):
    login_page = KdLoginPage(context.page)
    login_page.kd_enter_email(text)


@step('kd I enter "{text}" in the password field')
def kd_input_password(context, text):
    login_page = KdLoginPage(context.page)
    login_page.kd_enter_password(text)


@step('kd I click the "{button_text}" button')
def kd_click_login_button(context, button_text):
    login_page = KdLoginPage(context.page)
    login_page.kd_click_login()


@step('kd I should be redirected to the dashboard page')
def kd_verify_dashboard_page(context):
    login_page = KdLoginPage(context.page)
    assert login_page.kd_verify_dashboard_page(), "Dashboard page was not detected."


@step('I should see an error message "Sorry, unrecognized username or password"')
def kd_error_login_message(context):
    login_page = KdLoginPage(context.page)
    # Wait for the error message to appear and check visibility
    assert login_page.verify_element_exists(login_page.error_message, wait=True), "Error message was not displayed."
