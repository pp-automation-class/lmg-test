Feature: Link My Gear Login Functionality
  As a Link My Gear user
  I want to be able to log into my account
  So that I can access my gear management features

  Background:
    Given I am on the Link My Gear login page
    And the login form is displayed

  Scenario: Successful login with valid credentials
    When I enter email "alena9tester@gmail.com"
    And I enter password "Hello"
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Login with invalid email format
    When I enter email "invalid-email"
    And I enter password "password123"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Login with empty credentials
    When I click the login button
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

  Scenario: Login with incorrect credentials
    When I enter email "alena9tester@gmail.com"
    And I enter password "wrongPassword"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

  Scenario: Clear form fields
    When I enter email "test@example.com"
    And I enter password "testpassword"
    And I clear the email field
    And I clear the password field
    Then the email field should be empty
    And the password field should be empty

  Scenario: Verify form elements are present
    Then I should see the login page title "Login to Your Account"
    And I should see the "Forgot password" link
    And I should see the "Create an account" link
    And the login button should be enabled

  Scenario: Use forgot password functionality
    When I click the "Forgot password" link
    Then I should be redirected to the password reset page

  Scenario: Use create account functionality
    When I click the "Create an account" link
    Then I should be redirected to the registration page

  Scenario Outline: Login with multiple invalid credentials
    When I enter email "<email>"
    And I enter password "<password>"
    And I click the login button
    Then I should see an error message
    And I should remain on the login page

    Examples:
      | email                    | password        |
      | invalid.email           | password123     |
      | test@                   | password123     |
      | @example.com            | password123     |
      | test@example            | password123     |
      | alena9tester@gmail.com  | 123             |
      | alena9tester@gmail.com  | wrongpassword   |

  Scenario: Login with credentials from data table
    When I enter the following login credentials:
      | email                    | password      |
      | alena9tester@gmail.com   | validPassword |
    And I click the login button
    Then I should be redirected to the dashboard

  Scenario: Verify multiple potential error messages
    When I enter email "invalid"
    And I enter password "wrong"
    And I click the login button
    Then I should see the following error messages:
      | error_message                    |
      | Invalid email format             |
      | Invalid credentials              |
      | Login failed                     |
      | Please check your email          |