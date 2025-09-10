"""
Behave Step Definitions for Link My Gear Login functionality
"""
from behave import given, when, then
from pages.login_page import LoginPage
import logging

logger = logging.getLogger(__name__)


@given('Linda:I am on the Link My Gear login page')
def step_navigate_to_login_page(context):
    """Navigate to the login page."""
    context.login_page = LoginPage(context.page)
    context.login_page.navigate()
    context.login_page.assert_login_page_loaded()


@given('Linda: the login form is displayed')
def step_login_form_displayed(context):
    """Verify that the login form is displayed."""
    assert context.login_page.is_login_form_displayed(), "Login form should be displayed"


@when('Linda: I enter email "{email}"')
def step_enter_email(context, email):
    """Enter email address."""
    context.login_page.enter_email(email)


@when('Linda: I enter password "{password}"')
def step_enter_password(context, password):
    """Enter password."""
    context.login_page.enter_password(password)


@when('Linda: I click the login button')
def step_click_login_button(context):
    """Click the login button."""
    context.login_page.click_login_button()


@when('Linda: I click the "Forgot password" link')
def step_click_forgot_password(context):
    """Click the forgot password link."""
    context.login_page.click_forgot_password()


@when('Linda: I click the "Create an account" link')
def step_click_create_account(context):
    """Click the create account link."""
    context.login_page.click_create_account()


@when('Linda: I perform login with email "{email}" and password "{password}"')
def step_perform_login(context, email, password):
    """Perform complete login action."""
    context.login_page.login(email, password)


@when('Linda: I clear the email field')
def step_clear_email_field(context):
    """Clear the email field."""
    context.login_page.clear_email_field()


@when('Linda: I clear the password field')
def step_clear_password_field(context):
    """Clear the password field."""
    context.login_page.clear_password_field()


@then('Linda: I should see the login page title "{title}"')
def step_verify_login_title(context, title):
    """Verify the login page title."""
    context.login_page.assert_login_title_displayed(title)


@then('Linda: I should see an error message')
def step_verify_error_message_displayed(context):
    """Verify that an error message is displayed."""
    context.login_page.assert_error_message_displayed()


@then('Linda: I should see an error message "{message}"')
def step_verify_specific_error_message(context, message):
    """Verify specific error message."""
    context.login_page.assert_error_message_displayed(message)


@then('Linda: I should not see any error message')
def step_verify_no_error_message(context):
    """Verify that no error message is displayed."""
    context.login_page.assert_no_error_message()


@then('Linda: the email field should be empty')
def step_verify_email_field_empty(context):
    """Verify that the email field is empty."""
    context.login_page.assert_email_field_empty()


@then('Linda: the password field should be empty')
def step_verify_password_field_empty(context):
    """Verify that the password field is empty."""
    context.login_page.assert_password_field_empty()


@then('Linda: the email field should contain "{expected_email}"')
def step_verify_email_field_value(context, expected_email):
    """Verify the email field contains expected value."""
    actual_email = context.login_page.get_email_value()
    assert actual_email == expected_email, f"Expected email '{expected_email}', but found '{actual_email}'"


@then('Linda: the login button should be enabled')
def step_verify_login_button_enabled(context):
    """Verify that the login button is enabled."""
    assert context.login_page.is_login_button_enabled(), "Login button should be enabled"


@then('Linda: the login button should be disabled')
def step_verify_login_button_disabled(context):
    """Verify that the login button is disabled."""
    assert not context.login_page.is_login_button_enabled(), "Login button should be disabled"


@then('Linda: I should see the "Forgot password" link')
def step_verify_forgot_password_link(context):
    """Verify that the forgot password link is present."""
    context.login_page.assert_forgot_password_link_present()


@then('Linda: I should see the "Create an account" link')
def step_verify_create_account_link(context):
    """Verify that the create account link is present."""
    context.login_page.assert_create_account_link_present()


@then('Linda: I should be redirected to the dashboard')
def step_verify_dashboard_redirect(context):
    """Verify redirection to dashboard after successful login."""
    # Wait for navigation
    context.page.wait_for_load_state("networkidle")

    # Check URL contains dashboard or home
    current_url = context.page.url
    assert "dashboard" in current_url.lower() or "home" in current_url.lower(), \
        f"Expected to be redirected to dashboard, but current URL is: {current_url}"


@then('Linda: I should remain on the login page')
def step_verify_remain_on_login_page(context):
    """Verify that user remains on login page."""
    current_url = context.page.url
    assert "login" in current_url.lower(), \
        f"Expected to remain on login page, but current URL is: {current_url}"


# Step definitions with data tables
@when('Linda: I enter the following login credentials')
def step_enter_login_credentials_table(context):
    """Enter login credentials from data table."""
    for row in context.table:
        email = row['email']
        password = row['password']
        context.login_page.enter_email(email)
        context.login_page.enter_password(password)
        break  # Take only the first row


@then('Linda: I should see the following error messages')
def step_verify_multiple_error_messages(context):
    """Verify multiple error messages from data table."""
    error_message = context.login_page.get_error_message()

    expected_messages = [row['error_message'] for row in context.table]

    message_found = False
    for expected_message in expected_messages:
        if expected_message.lower() in error_message.lower():
            message_found = True
            break

    assert message_found, f"Expected one of {expected_messages}, but got: {error_message}"