from playwright.sync_api import sync_playwright
from utils.logger import setup_logger, get_logger
import allure
from allure_commons.types import AttachmentType

# Initialize logging for the test framework
logger = setup_logger("test_framework", "DEBUG")


def before_all(context):
    logger.info("=" * 80)
    logger.info("=== Starting test execution ===")
    logger.info("Launching Playwright and creating browser instance")
    # Launch Playwright and create browser instance
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=True # Set to True for headless mode
    )
    logger.debug("Browser instance created successfully")


def before_feature(context, feature):
    logger.info(f"=== Starting Feature: {feature.name} ===")
    logger.debug(f"Feature file: {feature.filename}")


def before_scenario(context, scenario):
    logger.info(f"--- Starting Scenario: {scenario.name} ---")
    logger.debug(f"Scenario tags: {list(scenario.tags)}")
    
    # Add Allure test info
    allure.dynamic.title(scenario.name)
    allure.dynamic.description(f"Feature: {scenario.feature.name}")
    
    # Add tags as labels
    for tag in scenario.tags:
        allure.dynamic.tag(tag)
    
    # Create a new browser context and page for each scenario
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()
    logger.debug("New browser context and page created for scenario")


def before_step(context, step):
    logger.debug(f"Executing step: {step.step_type} {step.name}")


def after_step(context, step):
    if step.status.name == "passed":
        logger.debug(f"Step completed successfully: {step.step_type} {step.name}")
    elif step.status.name == "failed":
        logger.error(f"Step failed: {step.step_type} {step.name}")
        if step.exception:
            logger.error(f"Error details: {step.exception}")
            
        # Capture screenshot on step failure
        if hasattr(context, 'page') and context.page:
            try:
                screenshot = context.page.screenshot()
                allure.attach(screenshot, name=f"Step Failed: {step.name}", attachment_type=AttachmentType.PNG)
                logger.debug("Screenshot attached to Allure report")
            except Exception as e:
                logger.warning(f"Failed to capture screenshot: {e}")
                
    elif step.status.name == "skipped":
        logger.warning(f"Step skipped: {step.step_type} {step.name}")
        
    # Add step information to Allure report
    with allure.step(f"{step.step_type.capitalize()}: {step.name}"):
        if step.status.name == "failed" and step.exception:
            allure.attach(str(step.exception), name="Error Details", attachment_type=AttachmentType.TEXT)


def after_scenario(context, scenario):
    # Capture final screenshot before closing browser
    if hasattr(context, 'page') and context.page:
        try:
            screenshot = context.page.screenshot()
            allure.attach(screenshot, name=f"Final Screenshot - {scenario.status.name.upper()}", attachment_type=AttachmentType.PNG)
            logger.debug("Final screenshot attached to Allure report")
        except Exception as e:
            logger.warning(f"Failed to capture final screenshot: {e}")
    
    if scenario.status.name == "passed":
        logger.info(f"--- Scenario PASSED: {scenario.name} ---")
    elif scenario.status.name == "failed":
        logger.error(f"--- Scenario FAILED: {scenario.name} ---")
    elif scenario.status.name == "skipped":
        logger.warning(f"--- Scenario SKIPPED: {scenario.name} ---")
    
    # Close the browser context after each scenario
    if hasattr(context, 'browser_context'):
        context.browser_context.close()
        logger.debug("Browser context closed")


def after_feature(context, feature):
    logger.info(f"=== Feature completed: {feature.name} ===")
    logger.info(f"Feature status: {feature.status}")


def after_all(context):
    logger.info("=== Test execution completed ===")
    # Clean up browser and Playwright instances
    if hasattr(context, 'browser'):
        context.browser.close()
        logger.debug("Browser closed")
    if hasattr(context, 'playwright'):
        context.playwright.stop()
        logger.debug("Playwright stopped")
    logger.info("=== Cleanup completed ===")
