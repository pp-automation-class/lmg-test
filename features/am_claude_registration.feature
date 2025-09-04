Feature: User Registration
  As a new user
  I want to create an account
  So that I can use the LinkMyGear platform

  Background:
    Given I am on the LinkMyGear homepage
    And I navigate to the registration page

  Scenario: Successful registration with valid information
    When I enter "newuser@example.com" in the email field
    And I enter "John" in the first name field
    And I enter "Doe" in the last name field
    And I enter "SecurePass123!" in the password field
    And I enter "SecurePass123!" in the confirm password field
    And I check the terms and conditions checkbox
    And I click the register button
    Then I should see a success message
    And I should receive a verification email
    And I should be redirected to the email verification page

  Scenario: Failed registration with existing email
    Given a user already exists with email "existing@example.com"
    When I enter "existing@example.com" in the email field
    And I fill in all other required fields with valid data
    And I click the register button
    Then I should see an error message "Email already exists"
    And I should remain on the registration page

  Scenario: Failed registration with mismatched passwords
    When I enter valid information in all fields
    And I enter "Password123!" in the password field
    And I enter "DifferentPass456!" in the confirm password field
    And I click the register button
    Then I should see an error message "Passwords do not match"
    And I should remain on the registration page

  Scenario: Registration form validation
    When I enter "invalid-email" in the email field
    And I tab to the next field
    Then I should see an email format validation error
    When I enter "weak" in the password field
    And I tab to the next field
    Then I should see a password strength validation error
    When I leave the first name field empty
    And I tab to the next field
    Then I should see a required field validation error

  Scenario: Terms and conditions requirement
    When I fill in all required fields with valid data
    And I leave the terms and conditions checkbox unchecked
    And I click the register button
    Then I should see an error message "Please accept the terms and conditions"
    And I should remain on the registration page

  Scenario: Password strength requirements
    When I enter "abc" in the password field
    Then I should see "Weak password" indicator
    When I enter "Password123" in the password field
    Then I should see "Medium password" indicator
    When I enter "SecurePass123!" in the password field
    Then I should see "Strong password" indicator

