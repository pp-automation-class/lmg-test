Feature: AB - Login Page Links
  As a user participating in an A/B experiment
  I want to verify key navigation links on the login page
  So that account access and recovery paths work as expected

  Background:
    Given I am on the login page

  @ab @login
  Scenario: Forgot password link navigates to reset page
    When I click the "Forgot Password?" link
    Then I should be redirected to the password reset page
    And I should see "Reset your password" heading

  @ab @login
  Scenario: Create account link navigates to registration page
    When I click the "Sign Up" link
    Then I should be redirected to the registration page
    And I should see "Create your account" heading
