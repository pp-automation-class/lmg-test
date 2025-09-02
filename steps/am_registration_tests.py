# steps/am_RegistrationNavigationSteps.py
from behave import given, when, then
from playwright.sync_api import expect
import re
from typing import List


def _split_or_options(opt1: str, opt2: str) -> List[str]:
    # Helper to normalize and deduplicate option strings
    options = []
    for o in (opt1, opt2):
        if o and o.strip():
            options.append(o.strip())
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for o in options:
        if o.lower() not in seen:
            seen.add(o.lower())
            unique.append(o)
    return unique


def _wait_for_url_contains_any(page, substrings: List[str], timeout_ms: int = 5000):
    # Poll the current URL until it contains any of the given substrings or timeout
    page.wait_for_load_state("networkidle")
    expect(page).to_have_url(re.compile("|".join(map(re.escape, substrings))), timeout=timeout_ms)


def _click_first_available(page, locators):
    # Click the first locator that resolves to at least 1 element and is visible
    for loc in locators:
        if page.locator(loc).first.count() > 0:
            first = page.locator(loc).first
            if first.is_visible():
                first.click()
                return True
    return False


@given('I navigate to "{url}"')
def step_navigate_to(context, url):
    page = context.page
    page.goto(url)
    page.wait_for_load_state("domcontentloaded")


@when('I click the "{link_text}" link')
def step_click_named_link(context, link_text):
    page = context.page
    # Prefer accessible role/name; fall back to link text selector
    clicked = False
    candidates = [
        lambda: page.get_by_role("link", name=re.compile(rf"^{re.escape(link_text)}$", re.I), exact=False),
        lambda: page.get_by_role("link", name=re.compile(re.escape(link_text), re.I), exact=False),
        lambda: page.locator(f'a:has-text("{link_text}")'),
    ]
    for candidate in candidates:
        locator = candidate()
        if locator.count() > 0:
            locator.first.click()
            clicked = True
            break
    if not clicked:
        raise AssertionError(f'Link with text "{link_text}" not found/clickable')


@then('I should be on a page with URL containing "{opt1}" or "{opt2}"')
def step_url_contains_either(context, opt1, opt2):
    page = context.page
    options = _split_or_options(opt1, opt2)
    _wait_for_url_contains_any(page, options, timeout_ms=8000)


@then('I should see a heading containing "{opt1}" or "{opt2}"')
def step_heading_contains_either(context, opt1, opt2):
    page = context.page
    options = _split_or_options(opt1, opt2)
    pattern = re.compile("|".join(map(re.escape, options)), re.I)
    heading = page.get_by_role("heading", name=pattern)
    expect(heading).to_be_visible()


@given("I am on the registration page")
def step_on_registration_page(context):
    page = context.page
    # If already on registration-like URL, keep it; otherwise try to navigate via common links
    reg_url_parts = ["sign_up", "register"]
    try:
        if any(part in page.url.lower() for part in reg_url_parts):
            return
    except Exception:
        pass

    # Try clicking common "create account" links on sign-in/login pages
    link_names = [
        "Create account",
        "Create Account",
        "Sign up",
        "Sign Up",
        "Register",
        "Create your account",
    ]

    for name in link_names:
        link = page.get_by_role("link", name=re.compile(rf"^{re.escape(name)}$", re.I), exact=False)
        if link.count() > 0 and link.first.is_visible():
            link.first.click()
            break

    # Validate we landed on registration
    _wait_for_url_contains_any(page, reg_url_parts, timeout_ms=8000)


@then("I should see the email input")
def step_see_email_input(context):
    page = context.page
    # Prefer accessible label
    candidates = [
        page.get_by_label(re.compile(r"email", re.I)),
        page.get_by_placeholder(re.compile(r"email", re.I)),
        page.locator('input[type="email"]'),
        page.locator('input[name*="email" i]'),
    ]
    for loc in candidates:
        if loc.count() > 0 and loc.first.is_visible():
            expect(loc.first).to_be_visible()
            return
    raise AssertionError("Email input not visible")


@then("I should see the password input")
def step_see_password_input(context):
    page = context.page
    candidates = [
        page.get_by_label(re.compile(r"password", re.I)),
        page.get_by_placeholder(re.compile(r"password", re.I)),
        page.locator('input[type="password"]'),
        page.locator('input[name*="password" i]'),
    ]
    for loc in candidates:
        if loc.count() > 0 and loc.first.is_visible():
            expect(loc.first).to_be_visible()
            return
    raise AssertionError("Password input not visible")


@when('I click the "Create account" button')
def step_click_create_account_button(context):
    page = context.page
    # Try common button names for registration submit
    name_pattern = re.compile(r"(Create account|Sign up|Register)", re.I)
    # Prefer role=button; fall back to input[type=submit]
    button_locators = [
        page.get_by_role("button", name=name_pattern),
        page.locator('button:has-text("Create account")'),
        page.locator('button:has-text("Sign up")'),
        page.locator('button:has-text("Register")'),
        page.locator('input[type="submit"][value]'),
    ]
    for loc in button_locators:
        if loc.count() > 0 and loc.first.is_enabled():
            loc.first.click()
            return
    raise AssertionError('Create account/Sign up/Register button not found or not enabled')


@then("I should see validation messages for required fields")
def step_see_required_field_validations(context):
    page = context.page
    # Common validation wordings
    validation_patterns = [
        r"required",
        r"can.?t be blank",
        r"is required",
        r"must be",
        r"please enter",
        r"this field",
    ]
    regex = re.compile("|".join(validation_patterns), re.I)

    # Try common places where validation appears
    locators = [
        page.get_by_role("alert"),
        page.locator('[aria-live="assertive"]'),
        page.locator('[class*="error" i]'),
        page.locator('[data-test*="error" i]'),
        page.locator('[data-qa*="error" i]'),
        page.locator("form >> text=/{}+/i".format("|".join(validation_patterns))),
        page.locator("text=/{}+/i".format("|".join(validation_patterns))),
    ]

    for loc in locators:
        # If any matching node is visible and contains our regex, pass
        count = loc.count()
        if count == 0:
            continue
        # Check text content for a match
        for i in range(min(count, 5)):  # scan up to first 5 matches
            el = loc.nth(i)
            try:
                text = el.inner_text(timeout=1000)
            except Exception:
                continue
            if regex.search(text or "") and el.is_visible():
                expect(el).to_be_visible()
                return

    # As a fallback, scan generic text on the page
    body_text = page.locator("body").inner_text(timeout=2000)
    if not regex.search(body_text or ""):
        raise AssertionError("Expected required field validation messages were not found")
