Feature: Password reset
  As a user who forgot the password
  I want to request a password reset
  So I can regain access to my account

  Background:
    Given I navigate to "https://dev.linkmygear.com/password/reset"
    And I wait for the page to be ready

  @auth @password @smoke
  Scenario: Request reset with registered email
    When I fill "Email" with "registered-user@test.com"
    And I click the button "Send reset link"
    Then I should see a success message containing "email" or "sent"

  @auth @password
  Scenario: Request reset with unknown email shows generic response
    When I fill "Email" with "unknown-user@test.com"
    And I click the button "Send reset link"
    Then I should see a message containing "email" or "sent"

  @auth @password
  Scenario: Reset form validates required email
    When I click the button "Send reset link"
    Then I should see a validation message for "Email"

  @auth @password
  Scenario Outline: Reset form validates email format
    When I fill "Email" with "<email>"
    And I click the button "Send reset link"
    Then I should see a validation message for "Email"

    Examples:
      | email        |
      | not-an-email |
      | user@        |
