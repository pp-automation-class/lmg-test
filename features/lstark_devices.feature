# Created by laurastark at 9/17/25
Feature: Test devices

  Background:
    Given I am on the dev environment login page
    When I enter "lauravstesting53@gmail.com" in the email field
    And  I enter "T8st8ng38!" in the password field
    And I click the login button

    @ls-smoke
  Scenario: ls Create new device
    Then ls Verify I on "My devices" page
    When ls I open Devices Settings
    And ls Press Add new device button
    And ls Choose "Airguard other" device type
    And ls Fill out name "Test1LS" of device
    And ls Press add new device button
    Then ls Verify device "Test1LS" exists in list of devices

    @ls-regression
  Scenario: ls Create 2nd device
    Then Verify I on "My devices" page
    When I open Devices Settings
    And Press Add new device button
    And Choose "Airguard other" device type
    And Fill out name "Test2LS" of device
    And Press add new device button
    Then Verify device "Test2LS" exists in list of devices