from pages.am_base_page import AmBasePage


class AmRestorePasswordPage(AmBasePage):
    """
    Page Object representing the 'Restore Password' screen.
    Inherits common browser actions (e.g., clicking, typing, waiting)
    from AmBasePage.
    """

    def __init__(self, page):
        # Initialize the base page with the Playwright-like page instance
        super().__init__(page)

        # Locators for elements on the Restore Password page:
        self.page_title = (
            # Page header used to verify the correct page
            "//h5[text()='Restore Password']"
        )
        # Input where the user types the email to recover
        self.email_input = "//input[@class='el-input__inner']"
        # Button that submits the password restore request
        self.button = "//button[text()=' Send ']"

    def restore_password(self, email):
        """
        High-level action that performs the restore password flow:
        - Enters the provided email
        - Clicks the 'Send' button to request a reset link
        """
        # Fill the email field with the target user's email address
        self.enter_email(email)
        # Submit the form to trigger the restore password process
        self.click_button()
