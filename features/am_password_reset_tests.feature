Feature: AM - UltimateQA Password Reset
  As a user who forgot the password
  I want to request a password reset
  So that I can regain access to my account

  Background:
    Given I navigate to "https://courses.ultimateqa.com/users/sign_in"

  @am @reset
  Scenario: Navigate to password reset page
    When I click the "Forgot password" link
    Then I should be on a page with URL containing "password"
    And I should see a heading containing "Reset" or "Forgot"
    And I should see the email input

  @am @reset
  Scenario: Submit password reset for a valid-looking email
    Given I am on the password reset page
    When I enter "someone@example.com" in the email field
    And I click the "Send reset instructions" button
    Then I should see a confirmation message
    And I should be advised to check my email

  @am @reset @negative
  Scenario: Submit password reset with empty email
    Given I am on the password reset page
    When I click the "Send reset instructions" button
    Then I should see a validation message for the email field
