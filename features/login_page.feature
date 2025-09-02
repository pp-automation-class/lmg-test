Feature: Login Page
  As a user
  I want to be able to log into the application
  So that I can access my account and protected features

  Background:
    Given I am on the login page

  @smoke @login
  Scenario: Successful login with valid credentials
    When I enter "testuser@example.com" in the email field
    And I enter "ValidPass123!" in the password field
    And I click the login button
    Then I should be redirected to the devices page
    And I should see "Welcome back" message

  @negative @login
  Scenario: Failed login with invalid password
    When I enter "testuser@example.com" in the email field
    And I enter "WrongPassword" in the password field
    And I click the login button
    Then I should remain on the login page
    And I should see error message "Invalid email or password"

  @negative @login
  Scenario: Failed login with invalid email
    When I enter "invalid-email" in the email field
    And I enter "ValidPass123!" in the password field
    And I click the login button
    Then I should remain on the login page
    And I should see error message "Please enter a valid email address"

  @negative @login
  Scenario: Failed login with empty credentials
    When I click the login button
    Then I should remain on the login page
    And I should see error message "Email is required"
    And I should see error message "Password is required"

  @login
  Scenario: Forgot password link navigation
    When I click the "Forgot Password?" link
    Then I should be redirected to the password reset page
    And I should see "Reset your password" heading

  @login
  Scenario: Sign up link navigation
    When I click the "Sign Up" link
    Then I should be redirected to the registration page
    And I should see "Create your account" heading

  @security @login
  Scenario Outline: Login attempts with various invalid inputs
    When I enter "<email>" in the email field
    And I enter "<password>" in the password field
    And I click the login button
    Then I should remain on the login page
    And I should see error message "<error_message>"

    Examples:
      | email                | password      | error_message                          |
      | test@                | ValidPass123! | Please enter a valid email             |
      | @example.com         | ValidPass123! | Please enter a valid email             |
      | testuser@example.com | short         | Password must be at least 8 characters |
      | testuser@example.com | 12345678      | Password must contain letters          |
      | admin@example.com    | ' OR '1'='1   | Invalid email or password              |
