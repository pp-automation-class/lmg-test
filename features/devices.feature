# Created by andrey at 9/8/25
Feature: Test devices
  Background:
    Given I am on the dev environment login page
    When I enter "pcs.automationclass@gmail.com" in the email field
    And I enter "1234567" in the password field
    And I click the login button

  Scenario:
    Then Verify I on "My devices" page
    When I open Devices Settings
    And Press Add new device button
    And Choose "Airguard other" device type
    And Fill out name "Test1" of device
    And Wait for 3 seconds
    And Press add new device button
#    And Go to "My devices" page
#    Then Verify device "Test1" exists in list of devices


