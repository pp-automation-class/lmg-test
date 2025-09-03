Feature: Forgot Password
  As a user who forgot their password
  I want to reset my password
  So that I can regain access to my account

  Background:
    Given I am on the LinkMyGear homepage
    And I navigate to the login page
    And I click the "Forgot Password" link

  Scenario: Successful password reset request
    Given a user exists with email "user@example.com"
    When I enter "user@example.com" in the email field
    And I click the "Send Reset Link" button
    Then I should see a success message "Password reset link sent to your email"
    And I should receive a password reset email
    And the email should contain a valid reset link

  Scenario: Password reset request with non-existent email
    When I enter "nonexistent@example.com" in the email field
    And I click the "Send Reset Link" button
    Then I should see a message "If this email exists, you will receive a reset link"
    And no email should be sent

  Scenario: Password reset with valid token
    Given I have received a password reset email
    When I click the reset link in the email
    Then I should be redirected to the password reset page
    And I should see the reset password form

  Scenario: Successful password reset
    Given I am on the password reset page with a valid token
    When I enter "NewSecurePass123!" in the new password field
    And I enter "NewSecurePass123!" in the confirm password field
    And I click the "Reset Password" button
    Then I should see a success message "Password has been reset successfully"
    And I should be redirected to the login page
    And I should be able to login with the new password

  Scenario: Password reset with expired token
    Given I have an expired password reset token
    When I visit the reset link
    Then I should see an error message "Reset link has expired"
    And I should be redirected to the forgot password page

  Scenario: Password reset validation
    Given I am on the password reset page with a valid token
    When I enter "weak" in the new password field
    And I enter "different" in the confirm password field
    And I click the "Reset Password" button
    Then I should see password validation errors
    And I should remain on the password reset page

