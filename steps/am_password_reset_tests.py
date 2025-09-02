# steps/am_password_reset_steps.py
import re
from behave import given, when, then
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

HEADING_RESET_REGEX = re.compile(r"(Reset|Forgot).*password", re.IGNORECASE)
FORGOT_LINK_REGEX = re.compile(r"Forgot.*password\??", re.IGNORECASE)
EMAIL_LABEL_REGEX = re.compile(r"email", re.IGNORECASE)
RESET_BUTTON_REGEX = re.compile(r"(Send|Email).*reset.*instructions", re.IGNORECASE)

CONFIRMATION_TEXT_REGEXES = [
    re.compile(r"You will receive an email with instructions", re.IGNORECASE),
    re.compile(r"If your email address exists.*you will receive an email", re.IGNORECASE),
    re.compile(r"check your email", re.IGNORECASE),
]

VALIDATION_TEXT_REGEXES = [
    re.compile(r"can't be blank", re.IGNORECASE),
    re.compile(r"is required", re.IGNORECASE),
    re.compile(r"please enter.*email", re.IGNORECASE),
    re.compile(r"please fill out this field", re.IGNORECASE),  # native browser message (not always in DOM)
]


def _click_forgot_password_link(page):
    # Prefer role-based targeting with accessible name; fallback to text selector
    link = page.get_by_role("link", name=FORGOT_LINK_REGEX)
    if link.count():
        link.first.click()
        return
    page.get_by_text(FORGOT_LINK_REGEX, exact=False).first.click()


def _email_textbox(page):
    # Prefer role-based by accessible name; fallback to input[name="email"]
    tb = page.get_by_role("textbox", name=EMAIL_LABEL_REGEX)
    if tb.count():
        return tb.first
    return page.locator('input[type="email"], input[name="email"], input[id*="email" i]').first


def _reset_button(page):
    # Role-based button lookup with a fuzzy name
    btn = page.get_by_role("button", name=RESET_BUTTON_REGEX)
    if btn.count():
        return btn.first
    # Fallback to common text
    return page.get_byText(re.compile(r"reset.*instructions", re.IGNORECASE)).first


def _assert_any_text_visible(page, regex_list, timeout=5000):
    # Try common containers first (alerts, flash, notices), then any text on the page
    containers = [
        '[role="alert"]',
        '.alert, .alert-success, .alert-info, .notice, .flash, .notification',
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
            # Final fallback: any text
            try:
                page.get_by_text(rx, exact=False).first.wait_for(state="visible", timeout=timeout)
                found = True
            except PlaywrightTimeoutError:
                pass
        if not found:
            raise AssertionError(f"Expected to find visible text matching: {rx.pattern}")


@given('I navigate to "{url}"')
def step_navigate_to(context, url):
    context.page.goto(url)


@when('I click the "Forgot password" link')
def step_click_forgot_password(context):
    _click_forgot_password_link(context.page)


@then('I should be on a page with URL containing "password"')
def step_url_contains_password(context):
    assert "password" in context.page.url.lower(), f"Expected 'password' in URL, got: {context.page.url}"


@then('I should see a heading containing "Reset" or "Forgot"')
def step_heading_contains_reset_or_forgot(context):
    heading = context.page.get_by_role("heading", name=HEADING_RESET_REGEX)
    try:
        heading.first.wait_for(state="visible", timeout=5000)
    except PlaywrightTimeoutError:
        # Fallback: any heading tag with matching text
        loc = context.page.locator("h1, h2, h3, [role='heading']").filter(has_text=HEADING_RESET_REGEX)
        loc.first.wait_for(state="visible", timeout=5000)


@then("I should see the email input")
def step_see_email_input(context):
    tb = _email_textbox(context.page)
    tb.wait_for(state="visible", timeout=5000)


@given("I am on the password reset page")
def step_on_password_reset_page(context):
    # If already on a password-related page, do nothing; otherwise click the forgot link
    if "password" not in context.page.url.lower():
        _click_forgot_password_link(context.page)
    # Confirm
    step_url_contains_password(context)
    step_heading_contains_reset_or_forgot(context)
    step_see_email_input(context)


@when('I enter "{email}" in the email field')
def step_enter_email(context, email):
    tb = _email_textbox(context.page)
    tb.fill(email)


@when('I click the "Send reset instructions" button')
def step_click_send_reset(context):
    btn = context.page.get_by_role("button", name=RESET_BUTTON_REGEX)
    if btn.count():
        btn.first.click()
        return
    # Fallbacks: data-test, common text
    fallback = context.page.locator('[data-test="send-reset"], [data-testid="send-reset"]').first
    if fallback.count():
        fallback.click()
        return
    context.page.get_by_text(re.compile(r"send.*reset.*instructions", re.IGNORECASE)).first.click()


@then("I should see a confirmation message")
def step_confirmation_message(context):
    _assert_any_text_visible(context.page, CONFIRMATION_TEXT_REGEXES, timeout=7000)


@then("I should be advised to check my email")
def step_advised_check_email(context):
    _assert_any_text_visible(
        context.page,
        [
            re.compile(r"check your email", re.IGNORECASE),
            re.compile(r"email with instructions", re.IGNORECASE),
            re.compile(r"we have sent.*email", re.IGNORECASE),
        ],
        timeout=7000,
    )


@then("I should see a validation message for the email field")
def step_email_validation_message(context):
    page = context.page
    tb = _email_textbox(page)

    # 1) Try ARIA invalid state quickly
    try:
        tb.wait_for(state="visible", timeout=3000)
        aria_invalid = tb.get_attribute("aria-invalid")
        if aria_invalid == "true":
            # Look for the associated description or sibling error
            describedby = tb.get_attribute("aria-describedby")
            if describedby:
                err = page.locator(f"#{describedby}")
                if err.count():
                    err.first.wait_for(state="visible", timeout=3000)
                    return
    except PlaywrightTimeoutError:
        pass

    # 2) Common inline validation containers
    error_candidates = page.locator(
        ".error, .field-error, .invalid-feedback, .help.is-danger, [role='alert'], .form-error, .error-message"
    )
    if error_candidates.count():
        try:
            error_candidates.filter(has_text=re.compile(r"email|e-mail|mail", re.IGNORECASE)).first.wait_for(
                state="visible", timeout=5000
            )
            return
        except PlaywrightTimeoutError:
            # Try any known validation text
            pass

    # 3) Page-level messages
    _assert_any_text_visible(page, VALIDATION_TEXT_REGEXES, timeout=5000)
