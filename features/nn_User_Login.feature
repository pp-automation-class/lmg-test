# Created by Owner at 9/2/2025
Feature: User Login
  As a registered user
  I want to login to my account
  So that I can access the application features
Background:
    Given I navigate to the login page "https://test:FjeKB9ySMzwvDUs2XACpfu@dev.linkmygear.com/#/login"
    And I should see the login form with title "Login to Your Account"
    And I should see the subtitle "Enter your username & password to login"

@smoke @positive
  Scenario: Successful login with valid credentials
    When I enter valid email "user@example.com" in the email field
    And I enter valid password "validPassword123" in the password field
    And I click the "Login" button
    Then I should be redirected to the dashboard
    And I should see a successful login message

  @negative
  Scenario: Login with invalid email format
    When I enter invalid email "invalid-email" in the email field
    And I enter valid password "validPassword123" in the password field
    And I click the "Login" button
    Then I should see an error message "Please enter a valid email address"
    And I should remain on the login page

  @negative
  Scenario: Login with empty email field
    When I leave the email field empty
    And I enter valid password "validPassword123" in the password field
    And I click the "Login" button
    Then I should see an error message "Email is required"
    And I should remain on the login page

  @negative
  Scenario: Login with empty password field
    When I enter valid email "user@example.com" in the email field
    And I leave the password field empty
    And I click the "Login" button
    Then I should see an error message "Password is required"
    And I should remain on the login page

    @functional @smoke
  Scenario: Navigate to forgot password page
    Given I am on the login page
    When I click on "Forgot password?" link
    Then I should be redirected to the forgot password page

  @functional @smoke
  Scenario: Navigate to create account page
    Given I am on the login page
    When I click on "Create an account" link
    Then I should be redirected to the registration page

    Examples:
      | email              | message                           |
      | invalid-email      | Please enter a valid email address |
      | @domain.com        | Please enter a valid email address |
      | user@              | Please enter a valid email address |
      | user@domain        | Please enter a valid email address |
      | user@domain.com    |                                        |