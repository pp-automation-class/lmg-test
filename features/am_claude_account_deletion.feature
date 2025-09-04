Feature: Account Deletion
  As a user
  I want to delete my account
  So that I can remove my data from the platform

  Background:
    Given I am logged into my account
    And I navigate to the account settings page

  Scenario: Delete account with password confirmation
    When I click the "Delete Account" button
    Then I should see a confirmation dialog
    And I should see a warning about data deletion
    When I enter my password in the confirmation field
    And I type "DELETE" in the confirmation text field
    And I click "Permanently Delete Account"
    Then I should see a success message "Account deleted successfully"
    And I should be redirected to the homepage
    And I should not be able to log in with my old credentials

  Scenario: Cancel account deletion
    When I click the "Delete Account" button
    And I see the confirmation dialog
    And I click "Cancel"
    Then the dialog should close
    And I should remain on the account settings page
    And my account should remain active

  Scenario: Account deletion with incorrect password
    When I click the "Delete Account" button
    And I enter an incorrect password in the confirmation field
    And I type "DELETE" in the confirmation text field
    And I click "Permanently Delete Account"
    Then I should see an error message "Incorrect password"
    And the account deletion should not proceed
