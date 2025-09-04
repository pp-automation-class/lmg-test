Feature: Account Security
  As a user
  I want to ensure my account is secure
  So that my personal information is protected

  Background:
    Given I am logged into my account

  Scenario: View login history
    When I navigate to the security settings page
    Then I should see my recent login history
    And each login entry should show the date, time, and location
    And I should see the current session marked as "Current"

  Scenario: Enable two-factor authentication
    Given I am on the security settings page
    When I click "Enable Two-Factor Authentication"
    And I scan the QR code with my authenticator app
    And I enter the verification code from my app
    And I click "Verify and Enable"
    Then I should see a success message "Two-factor authentication enabled"
    And I should see backup codes
    And 2FA should be marked as enabled in my settings

  Scenario: Login with two-factor authentication
    Given I have two-factor authentication enabled
    When I log out and return to the login page
    And I enter my valid credentials
    And I click the login button
    Then I should be redirected to the 2FA verification page
    When I enter a valid authenticator code
    And I click "Verify"
    Then I should be logged in successfully

  Scenario: Disable two-factor authentication
    Given I have two-factor authentication enabled
    When I navigate to the security settings page
    And I click "Disable Two-Factor Authentication"
    And I enter my password for confirmation
    And I enter a current authenticator code
    And I click "Disable 2FA"
    Then I should see a success message "Two-factor authentication disabled"
    And 2FA should be marked as disabled in my settings

