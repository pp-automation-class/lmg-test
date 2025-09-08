Feature: KD - Login Page Scenarios
  As a user
  I want to verify basic functionality on the login page
  So that I can access my account or recover it if needed

  Background:
    Given kd I am on the dev environment login page

  @kd @login
  Scenario: Forgot password link navigates to reset page
    When kd I click on forget the password link
    Then kd I should be redirected to password restore page
    And kd I should see "Restore Password" heading

  @kd @login
  Scenario: "Create an account" link navigates to registration page
    When kd I click the "Create an account" link
    Then kd I should be redirected to registration page
    And kd I should see "Create an Account" heading

  @kd @login
  Scenario: Login with valid credentials
    When kd I enter "katedtest@gmail.com" in the email field
    And kd I enter "1234567890" in the password field
    And kd I click the "Login" button
    Then kd I should be redirected to the dashboard page

  @kd @negative @login
  Scenario: Login with invalid credentials
    When kd I enter "katedtest@gmail.com" in the email field
    And kd I enter "12345" in the password field
    And kd I click the "Login" button
    Then kd I should see an error message "Sorry, unrecognized username or password"