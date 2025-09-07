Feature: KD - Login Page Scenarios
  As a user
  I want to verify basic functionality on the login page
  So that I can access my account or recover it if needed

  Background:
    Given I am on the login page

  @kd @login
  Scenario: Forgot password link navigates to reset page
    When I click the "Forgot Password?" link
    Then I should be redirected to the KD password restore page
    And I should see "Restore Password" heading

  @kd @login
  Scenario: "Create an account" link navigates to registration page
    When I click the "Create an account" link
    Then I should be redirected to the KD registration page
    And I should see "Create an Account" heading

  @kd @login
  Scenario: Login with valid credentials
    When I enter a valid email and password
    And I click the "Login" button
    Then I should be redirected to the KD dashboard

  @kd @login
  Scenario: Login with invalid credentials
    When I enter an invalid email or password
    And I click the "Login" button
    Then I should see an error message "Sorry, unrecognized username or password"

