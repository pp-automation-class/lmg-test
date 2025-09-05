Feature: Profile Management
  As a logged-in user
  I want to manage my profile information
  So that I can keep my account details up to date

  Background:
    Given I am logged into my account
    And I navigate to my profile page

  Scenario: View profile information
    Then I should see my current email address
    And I should see my first name
    And I should see my last name
    And I should see my account creation date

  Scenario: Update profile information
    When I click the "Edit Profile" button
    And I change my first name to "Jane"
    And I change my last name to "Smith"
    And I click the "Save Changes" button
    Then I should see a success message "Profile updated successfully"
    And my profile should display the updated information

  Scenario: Change password
    When I click the "Change Password" button
    And I enter my current password "OldPass123!"
    And I enter "NewSecurePass456!" as the new password
    And I confirm the new password "NewSecurePass456!"
    And I click the "Update Password" button
    Then I should see a success message "Password changed successfully"
    And I should be able to login with the new password

  Scenario: Change password with incorrect current password
    When I click the "Change Password" button
    And I enter "WrongCurrentPass" as the current password
    And I enter "NewSecurePass456!" as the new password
    And I confirm the new password "NewSecurePass456!"
    And I click the "Update Password" button
    Then I should see an error message "Current password is incorrect"

  Scenario: Update email address
    When I click the "Change Email" button
    And I enter "newemail@example.com" in the new email field
    And I enter my current password for verification
    And I click the "Update Email" button
    Then I should see a message "Verification email sent to new address"
    And I should receive a verification email at the new address

