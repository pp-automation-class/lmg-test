from behave import step

from pages.login_page import LoginPage


@step("I am on the {env} environment login page")
def navigate_to_login_page(context, env):
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


@step('I enter "{text}" in the email field')
def input_email(context, text):
    login_page = LoginPage(context.page)
    login_page.enter_email(text)


@step('I enter "{text}" in the password field')
def input_password(context, text):
    login_page = LoginPage(context.page)
    login_page.enter_password(text)

@step('Wait for {sec} seconds')
def wait_for_sec(context, sec):
    context.page.wait_for_timeout(int(sec) * 1000)


@step('I click the login button')
def click_login_button(context):
    login_page = LoginPage(context.page)
    login_page.click_login()
