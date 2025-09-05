Feature: Logout
  As an authenticated user
  I want to log out
  So that my session is terminated

  Background:
    Given I am logged in as "replace@test.com" with password "replace_me1"
    And I wait for the page to be ready

  @auth @logout @smoke
  Scenario: Logout from user menu
    When I open the user menu
    And I click the menu item "Sign out"
    Then I should be redirected to a page with URL containing "/login"
    And I should see text "Sign In"

  @auth @logout
  Scenario: Prevent accessing protected page after logout
    When I open the user menu
    And I click the menu item "Sign out"
    And I navigate to "https://dev.linkmygear.com/dashboard"
    Then I should be redirected to a page with URL containing "/login"
