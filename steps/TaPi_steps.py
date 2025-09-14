from behave import step

from pages.TaPi_login_page import TaPiLoginPage
from pages.TaPi_devices_page import TaPiDevicesPage


@step("I should be redirected to the devices page")
def should_be_on_devices_page(context):
    """Verify that user is on the Devices page after successful login."""
    devices_page = TaPiDevicesPage(context.page)
    # Wait for routing/rendering to settle
    context.page.wait_for_load_state('networkidle')
    # Explicitly wait for the Devices header to become visible
    context.page.wait_for_selector(devices_page.page_title, state="visible",
                                   timeout=15000)
    assert devices_page.verify_page_title("My Devices"), (
        "Expected to be on Devices page, but the page title did not match."
    )


@step("I should remain on the login page")
def should_remain_on_login_page(context):
    """Verify that user remains on the Login page (no redirect)."""
    login_page = TaPiLoginPage(context.page)
    # If still on login page, email input should be visible
    assert login_page.is_element_visible(login_page.email_input), \
        "Expected to remain on Login page, but login elements are not visible."


@step('I should see error message "{text}"')
def should_see_error_message(context, text):
    login_page = TaPiLoginPage(context.page)

    # Wait up to 10s for either the specific error element
    # or the text to appear
    try:
        context.page.wait_for_selector(f"text={text}", timeout=10000,
                                       state="visible")
    except Exception:
        # If the text didn’t appear via text engine, try the page object’s
        # error locator
        try:
            context.page.wait_for_selector(login_page.error_message,
                                           timeout=10000, state="visible")
        except Exception:
            pass

    actual = login_page.get_error_message()
    if actual:
        assert text.lower() in actual.lower(), (f"Expected error message "
                                                f"to contain '{text}', "
                                                f"got '{actual}'")
    else:
        is_visible = context.page.is_visible(f"text={text}")
        assert is_visible, (f"Expected to see error message '{text}',"
                            f" but it was not visible.")
