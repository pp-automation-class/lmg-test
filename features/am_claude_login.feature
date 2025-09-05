Feature: User Login
  As a registered user
  I want to log into my account
  So that I can access the application features

  Background:
    Given I am on the LinkMyGear homepage
    And I navigate to the login page

  Scenario: Successful login with valid credentials
    Given I have a registered account with email "test@example.com" and password "ValidPass123!"
    When I enter "test@example.com" in the email field
    And I enter "ValidPass123!" in the password field
    And I click the login button
    Then I should be redirected to the dashboard
    And I should see a welcome message
    And I should see my profile information

  Scenario: Failed login with invalid email
    When I enter "invalid-email@nonexistent.com" in the email field
    And I enter "SomePassword123!" in the password field
    And I click the login button
    Then I should see an error message "Invalid email or password"
    And I should remain on the login page

  Scenario: Failed login with invalid password
    Given I have a registered account with email "test@example.com"
    When I enter "test@example.com" in the email field
    And I enter "WrongPassword" in the password field
    And I click the login button
    Then I should see an error message "Invalid email or password"
    And I should remain on the login page

  Scenario: Failed login with empty credentials
    When I leave the email field empty
    And I leave the password field empty
    And I click the login button
    Then I should see validation errors for required fields
    And I should remain on the login page

  Scenario: Password visibility toggle
    When I enter "MyPassword123!" in the password field
    And I click the password visibility toggle
    Then the password should be visible as plain text
    When I click the password visibility toggle again
    Then the password should be hidden

  Scenario: Remember me functionality
    Given I have a registered account with email "test@example.com" and password "ValidPass123!"
    When I enter valid credentials
    And I check the "Remember me" checkbox
    And I click the login button
    And I log out
    And I return to the login page
    Then my email should be pre-filled

  Scenario: Login form validation
    When I enter "invalid-email" in the email field
    And I tab to the password field
    Then I should see an email format validation error
    When I enter "123" in the password field
    And I tab away from the password field
    Then I should see a password strength validation error

