Feature: Link My Gear Login
  As a Link My Gear user
  I want to log into my account
  So that I can access my gear management features

  Background:
    Given I am on the Link My Gear login page

  Scenario: Successful login with valid credentials
    When I enter email "alena9tester@gmail.com"
    And I enter password "validPassword123"
    And I click the login button
    Then I should be logged in successfully
    And I should be redirected to the dashboard

  Scenario: Login with invalid email
    When I enter email "invalid-email"
    And I enter password "password123"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Login with empty email
    When I enter password "password123"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Login with empty password
    When I enter email "alena9tester@gmail.com"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Login with wrong password
    When I enter email "alena9tester@gmail.com"
    And I enter password "wrongPassword"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Login with empty credentials
    When I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Use forgot password link
    When I click the "Forgot password?" link
    Then I should be redirected to the password reset page

  Scenario: Use create account link
    When I click the "Create an account" link
    Then I should be redirected to the registration page

  Scenario: Verify login page elements
    Then I should see the login page title "Login to Your Account"
    And I should see the email field
    And I should see the password field
    And I should see the login button
    And I should see the "Forgot password?" link
    And I should see the "Create an account" link

  Scenario Outline: Login with multiple invalid credentials
    When I enter email "<email>"
    And I enter password "<password>"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

    Examples:
      | email                   | password     |
      | invalid.email          | password123  |
      | test@                  | password123  |
      | @example.com           | password123  |
      | alena9tester@gmail.com | 123          |
      | alena9tester@gmail.com | wrongpass    |