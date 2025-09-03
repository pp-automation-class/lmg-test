Feature: Session persistence and remember me
  As a user
  I want my session to persist when I choose Remember me
  So I don't have to log in every time

  @auth @login @remember
  Scenario: Remember me keeps session after browser restart
    Given I navigate to "https://dev.linkmygear.com/login"
    And I wait for the page to be ready
    When I fill "Email" with "replace@test.com"
    And I fill "Password" with "replace_me1"
    And I check the checkbox "Remember me"
    And I click the button "Sign In"
    Then I should be redirected to a page with URL containing "/dashboard"
    When I close and reopen the browser context
    And I navigate to "https://dev.linkmygear.com/dashboard"
    Then I should stay signed in
