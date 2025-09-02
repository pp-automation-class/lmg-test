# steps/am_sign_in_tests.py
import re
from behave import when, then
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

# Reusable regex patterns
HEADING_SIGNIN_REGEX = re.compile(r"\bsign\s*in\b", re.IGNORECASE)
PASSWORD_LABEL_REGEX = re.compile(r"password", re.IGNORECASE)
SIGNIN_BUTTON_REGEX = re.compile(r"\bsign\s*in\b", re.IGNORECASE)
FORGOT_PASSWORD_LINK_REGEX = re.compile(r"forgot.*password\??", re.IGNORECASE)
CREATE_ACCOUNT_LINK_REGEX = re.compile(r"(create.*account|sign\s*up|create\s*one)", re.IGNORECASE)

INVALID_EMAIL_TEXT_REGEXES = [
    re.compile(r"invalid\s*email", re.IGNORECASE),
    re.compile(r"enter.*valid.*email", re.IGNORECASE),
    re.compile(r"email.*format", re.IGNORECASE),
]

AUTH_ERROR_TEXT_REGEXES = [
    re.compile(r"invalid email or password", re.IGNORECASE),
    re.compile(r"incorrect email or password", re.IGNORECASE),
    re.compile(r"authentication.*(failed|error)", re.IGNORECASE),
    re.compile(r"could not.*sign.*in", re.IGNORECASE),
]

PASSWORD_VALIDATION_TEXT_REGEXES = [
    re.compile(r"password.*(required|can't be blank|cannot be blank)", re.IGNORECASE),
    re.compile(r"password.*(too short|min|at least)", re.IGNORECASE),
    re.compile(r"please enter.*password", re.IGNORECASE),
]


def _assert_any_text_visible(page, regex_list, timeout=5000):
    containers = [
        '[role="alert"]',
        '.alert, .alert-danger, .alert-error, .flash, .notice, .notification, .error-message',
        'main, body',
    ]
    for rx in regex_list:
        found = False
        for selector in containers:
            loc = page.locator(selector).filter(has_text=rx)
            try:
                loc.first.wait_for(state="visible", timeout=timeout)
                found = True
                break
            except PlaywrightTimeoutError:
                continue
        if not found:
            try:
                page.get_by_text(rx, exact=False).first.wait_for(state="visible", timeout=timeout)
                found = True
            except PlaywrightTimeoutError:
                pass
        if not found:
            raise AssertionError(f"Expected to find visible text matching: {rx.pattern}")


def _password_input(page):
    # Prefer actual password input
    pw = page.locator('input[type="password"]').first
    if pw.count():
        return pw
    # Fallbacks: labeled textbox or common selectors
    tb = page.get_by_role("textbox", name=PASSWORD_LABEL_REGEX)
    if tb.count():
        return tb.first
    return page.locator('input[name*="password" i], input[id*="password" i]').first


def _signin_button(page):
    btn = page.get_by_role("button", name=SIGNIN_BUTTON_REGEX)
    if btn.count():
        return btn.first
    # Fallback: any clickable element with "Sign in"
    return page.get_by_text(SIGNIN_BUTTON_REGEX, exact=False).first


@then('I should see a heading containing "Sign in"')
def step_see_signin_heading(context):
    page = context.page
    heading = page.get_by_role("heading", name=HEADING_SIGNIN_REGEX)
    try:
        heading.first.wait_for(state="visible", timeout=5000)
    except PlaywrightTimeoutError:
        # Fallback: generic heading tags
        page.locator("h1, h2, h3, [role='heading']").filter(has_text=HEADING_SIGNIN_REGEX).first.wait_for(
            state="visible", timeout=5000
        )


@then("I should see the password input")
def step_see_password_input(context):
    pw = _password_input(context.page)
    pw.wait_for(state="visible", timeout=5000)


@then('I should see a "Sign in" button')
def step_see_signin_button(context):
    _signin_button(context.page).wait_for(state="visible", timeout=5000)


@then('I should see a "Forgot password" link')
def step_see_forgot_password_link(context):
    link = context.page.get_by_role("link", name=FORGOT_PASSWORD_LINK_REGEX)
    if link.count():
        link.first.wait_for(state="visible", timeout=5000)
        return
    context.page.get_by_text(FORGOT_PASSWORD_LINK_REGEX, exact=False).first.wait_for(state="visible", timeout=5000)


@then('I should see a "Create account" link')
def step_see_create_account_link(context):
    link = context.page.get_by_role("link", name=CREATE_ACCOUNT_LINK_REGEX)
    if link.count():
        link.first.wait_for(state="visible", timeout=5000)
        return
    context.page.get_by_text(CREATE_ACCOUNT_LINK_REGEX, exact=False).first.wait_for(state="visible", timeout=5000)


@when('I click the "Sign in" button')
def step_click_signin(context):
    _signin_button(context.page).click()


@then("I should remain on the sign in page")
def step_remain_on_signin_page(context):
    url = context.page.url.lower()
    # Heuristic: URL contains 'sign_in' or heading is present
    if "sign_in" not in url and "signin" not in url and "login" not in url:
        # Validate by heading fallback
        step_see_signin_heading(context)


@when('I enter "{password}" in the password field')
def step_enter_password(context, password):
    pw = _password_input(context.page)
    pw.fill(password)


@then("I should see a validation message for the password field")
def step_password_validation_message(context):
    page = context.page
    pw = _password_input(page)

    # Check ARIA invalid and describedby pattern
    try:
        pw.wait_for(state="visible", timeout=3000)
        aria_invalid = pw.get_attribute("aria-invalid")
        if aria_invalid == "true":
            describedby = pw.get_attribute("aria-describedby")
            if describedby:
                err = page.locator(f"#{describedby}").first
                if err.count():
                    err.wait_for(state="visible", timeout=3000)
                    return
    except PlaywrightTimeoutError:
        pass

    # Common inline validation containers mentioning "password"
    error_candidates = page.locator(
        ".error, .field-error, .invalid-feedback, .help.is-danger, [role='alert'], .form-error, .error-message"
    )
    if error_candidates.count():
        try:
            error_candidates.filter(has_text=re.compile(r"password", re.IGNORECASE)).first.wait_for(
                state="visible", timeout=5000
            )
            return
        except PlaywrightTimeoutError:
            pass

    # Generic password validation phrases
    _assert_any_text_visible(page, PASSWORD_VALIDATION_TEXT_REGEXES, timeout=5000)


@then("I should see a validation message indicating an invalid email")
def step_invalid_email_message(context):
    _assert_any_text_visible(context.page, INVALID_EMAIL_TEXT_REGEXES, timeout=6000)


@then("I should see an authentication error message")
def step_authentication_error_message(context):
    _assert_any_text_visible(context.page, AUTH_ERROR_TEXT_REGEXES, timeout=7000)


@when("I toggle the password visibility control")
def step_toggle_password_visibility(context):
    page = context.page
    pw = _password_input(page)
    pw.wait_for(state="visible", timeout=5000)
    original_type = pw.get_attribute("type") or "password"

    # Locate a toggle control within the same field container
    container = pw.locator("xpath=ancestor::*[self::div or self::label or self::*[contains(@class,'field')]][1]")
    toggle = (
        container.get_by_role("button", name=re.compile(r"(show|hide|toggle|visibility)", re.IGNORECASE)).first
    )
    if not toggle.count():
        # Fallback: any button/icon next to the input
        toggle = container.locator("button, [role='button'], .icon, .toggle, .visibility").first

    if not toggle.count():
        # Global fallback: a button with a common name
        toggle = page.get_by_role("button", name=re.compile(r"(show|hide).*password", re.IGNORECASE)).first

    if not toggle.count():
        raise AssertionError("Password visibility toggle control not found")

    toggle.click()
    context.password_type_before = original_type
    try:
        # Wait for type to change
        page.wait_for_function(
            """(el, before) => el.getAttribute('type') && el.getAttribute('type') !== before""",
            arg=pw,
            timeout=3000,
            values=[original_type],
        )
    except PlaywrightTimeoutError:
        # Some UIs swap input elements; re-query by name
        pw2 = _password_input(page)
        context.password_type_after = pw2.get_attribute("type") or ""
        return

    context.password_type_after = pw.get_attribute("type") or ""


@then('the password input type should switch between "password" and "text"')
def step_assert_password_type_switched(context):
    before = (getattr(context, "password_type_before", None) or "").lower()
    after = (getattr(context, "password_type_after", None) or "").lower()
    if not before or not after:
        raise AssertionError("Password type before/after toggle not captured")
    expected = {"password", "text"}
    actual = {before, after}
    assert actual == expected and before != after, f"Expected types to switch between {expected}, got {before} -> {after}"
