Feature: Maps Page


  Background:
    Given I am on the dev environment login page

  @ab-regression
  Scenario: Successful login with valid credentials
    When I enter "pcs.automationclass@gmail.com" in the email field
    And I enter "1234567" in the password field
    And I click the login button
    When I click show on map button for device with name "Device"
    And Wait for 3 seconds
#    Then I should be redirected to the devices page