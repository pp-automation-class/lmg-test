@auth @forgot_password
Feature: Password recovery (Forgot password)
  As a user who forgot the password
  I want to request a reset link
  So that I can restore access to my account

  Background:
    Given I open the Login page
    When I click the "Forgot password?" link
    Then I should be on the "Restore Password" page
    And I should see the "Your Email" field and the "Send" button

  @smoke
  Scenario: Registered user requests a reset link
    Given I am on the "Restore Password" page
    When I fill "Your Email" with "alena9tester@gmail.com"
    And I click the "Send" button
    Then a success message is shown containing "email" and "reset"
    And the "Back to Login page" link is visible

  @negative
  Scenario Outline: Invalid email format is rejected
    Given I am on the "Restore Password" page
    When I fill "Your Email" with "<invalid_email>"
    And I click the "Send" button
    Then a validation error is shown for the "Your Email" field
    And the "Send" button remains enabled

    Examples:
      | invalid_email     |
      | test              |
      | user@             |
      | @domain.com       |
      | user@domain       |
      | user@@domain.com  |

  @negative
  Scenario: Empty email cannot be submitted
    Given I am on the "Restore Password" page
    When I leave "Your Email" empty
    And I click the "Send" button
    Then a validation error is shown for the "Your Email" field

  @navigation
  Scenario: Go back to Login from Restore Password
    Given I am on the "Restore Password" page
    When I click the "Back to Login page" link
    Then I should be on the Login page
    And I should see the heading "Login to Your Account"
