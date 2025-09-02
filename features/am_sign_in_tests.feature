Feature: AM - UltimateQA Sign In Page
  As a visitor
  I want to sign in securely
  So that I can access my courses

  Background:
    Given I navigate to "https://courses.ultimateqa.com/users/sign_in"

  @am @signin @ui
  Scenario: Sign in page loads with essential elements
    Then I should see a heading containing "Sign in"
    And I should see the email input
    And I should see the password input
    And I should see a "Sign in" button
    And I should see a "Forgot password" link
    And I should see a "Create account" link

  @am @signin @validation
  Scenario: Required field validation for empty submission
    When I click the "Sign in" button
    Then I should remain on the sign in page
    And I should see a validation message for the email field
    And I should see a validation message for the password field

  @am @signin @validation
  Scenario Outline: Invalid email format is rejected
    When I enter "<email>" in the email field
    And I enter "SomePassword123!" in the password field
    And I click the "Sign in" button
    Then I should remain on the sign in page
    And I should see a validation message indicating an invalid email

    Examples:
      | email        |
      | test@        |
      | @example.com |
      | invalid      |

  @am @signin @negative
  Scenario: Incorrect credentials show a generic error
    When I enter "nonexistent.user@example.com" in the email field
    And I enter "WrongPassword!" in the password field
    And I click the "Sign in" button
    Then I should remain on the sign in page
    And I should see an authentication error message

  @am @signin @ux
  Scenario: Password field supports show/hide toggle (if available)
    When I toggle the password visibility control
    Then the password input type should switch between "password" and "text"
