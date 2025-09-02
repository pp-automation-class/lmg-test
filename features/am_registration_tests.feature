Feature: AM - UltimateQA Registration Navigation
  As a prospective user
  I want to navigate to the account creation page
  So that I can register for access

  Background:
    Given I navigate to "https://courses.ultimateqa.com/users/sign_in"

  @am @register
  Scenario: Sign up link navigates to registration page
    When I click the "Create account" link
    Then I should be on a page with URL containing "sign_up" or "register"
    And I should see a heading containing "Sign up" or "Create your account"

  @am @register @backnav
  Scenario: Returning to sign in from registration
    Given I am on the registration page
    When I click the "Sign in" link
    Then I should be on a page with URL containing "sign_in" or "login"
    And I should see the email input
    And I should see the password input

  @am @register @validation
  Scenario: Registration page shows required field validations
    Given I am on the registration page
    When I click the "Create account" button
    Then I should see validation messages for required fields
