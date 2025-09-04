
"""Create Account Page Object Model"""
from pages.base_page import BasePage

class CreateAccountPage(BasePage):
    """Represents the create account page with its elements and actions"""
    
    def __init__(self, page):
        """Initialize with Playwright page object"""
        super().__init__(page)  # Call parent class constructor
        
        # Define selectors for page elements
        self.page_title = "h1"
