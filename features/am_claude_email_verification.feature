Feature: Email Verification
  As a newly registered user
  I want to verify my email address
  So that I can activate my account

  Background:
    Given I have registered with email "newuser@example.com"
    And I have received a verification email

  Scenario: Successful email verification
    When I click the verification link in the email
    Then I should be redirected to the verification success page
    And I should see a success message "Email verified successfully"
    And my account should be activated
    And I should be able to log in

  Scenario: Email verification with expired token
    Given I have an expired verification token
    When I click the verification link
    Then I should see an error message "Verification link has expired"
    And I should see an option to resend verification email

  Scenario: Resend verification email
    Given I am on the email verification page
    When I click the "Resend verification email" button
    Then I should see a success message "Verification email sent"
    And I should receive a new verification email

  Scenario: Email verification with invalid token
    When I visit the verification page with an invalid token
    Then I should see an error message "Invalid verification link"
    And I should be redirected to the login page

