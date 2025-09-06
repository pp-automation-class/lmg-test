from playwright.sync_api import sync_playwright


def before_all(context):
    # Launch Playwright and create browser instance
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=False  # Set to True for headless mode
    )


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    # Create a new browser context and page for each scenario
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    # Close the browser context after each scenario
    if hasattr(context, 'browser_context'):
        context.browser_context.close()


def after_feature(context, feature):
    pass


def after_all(context):
    # Clean up browser and Playwright instances
    if hasattr(context, 'browser'):
        context.browser.close()
    if hasattr(context, 'playwright'):
        context.playwright.stop()
