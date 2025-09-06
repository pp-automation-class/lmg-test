# Created by ant at 9/5/2025
Feature: Login Page
  As a user
  I want to log into the application
  So that I can access my account

  Background:
    Given I am on the login page

  @positive
  Scenario: Successful login with valid credentials
    When I enter "anton.bondarenko.test@gmail.com" in the username field
    And I enter "123459" in the password field
    And I click the login button
    Then I should be redirected to the devices page
    And I should see a welcome message

  @negative
  Scenario Outline: Login fails with invalid credentials
    When I enter "<username>" in the username field
    And I enter "<password>" in the password field
    And I click the login button
    Then I should see an error message "Invalid email or password"
    And I should remain on the login page

    Examples:
      | username                    | password      |
      | invalid.user@example.com    | wrongpassword |
      | wrongemail@test.com         | 123459        |
      | test@                       | validpass     |
      | anton.bondarenko.test@gmail.com | wrongpass |

  @negative
  Scenario: Login fails with empty credentials
    When I leave username field empty
    And I leave password field empty
    And I click the login button
    Then I should see validation error message "Email is required" for username field
    And I should see validation error message "Password is required" for password field
    And the login button should remain disabled