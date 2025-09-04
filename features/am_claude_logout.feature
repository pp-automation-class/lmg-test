Feature: User Logout
  As a logged-in user
  I want to log out of my account
  So that I can secure my session

  Background:
    Given I am logged into my account
    And I am on the dashboard

  Scenario: Successful logout
    When I click the logout button
    Then I should be redirected to the homepage
    And I should see the login option
    And my session should be terminated

  Scenario: Logout from user menu
    When I click on my profile menu
    And I click the "Logout" option
    Then I should be logged out successfully
    And I should be redirected to the homepage

  Scenario: Session timeout logout
    Given I have been inactive for the session timeout period
    When I try to access a protected page
    Then I should be automatically logged out
    And I should be redirected to the login page
    And I should see a session timeout message

