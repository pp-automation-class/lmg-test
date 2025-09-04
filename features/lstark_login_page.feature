Feature: LS Login Page
  As a user
  I want quick access to account recovery and creation
  So that I can reset my password or create a new account

  Background:
    Given I am on the login page

  @lstark @login
  Scenario: Forgot password link navigates to reset page
    When I click the "Forgot Password?" link
    Then I should be redirected to the password reset page
    And I should see "Reset your password" heading

  @lstark @login
  Scenario: Sign up link navigates to registration page
    When I click the "Sign Up" link
    Then I should be redirected to the registration page
    And I should see "Create your account" heading
