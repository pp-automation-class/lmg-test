# Created by AnKrylo at 9/13/2025
Feature: Test of Devices Page
  Log in and verify elements on the Devices Page
    I now have access to my devices and their details
    So I can manage and monitor them effectively

  Background:
    Given ank I am on the dev environment login page
    When ank I enter "akr.autotest@gmail.com" in the email field
    And ank I enter "12345" in the password field
    And ank I click the "Login " button


  Scenario: Create New Device and Verify its Exists
    Then ank Verify I on "My devices" page
    When ank I open Devices Settings
    And ank I press Add new device button
    And ank I choose "Airguard other" device type
    And ank I fill out name "Test1" of device
    And ank I press add new device button
    Then ank I verify device "Test1" exists in list of devices
    # Enter steps herepage.feature and ank_steps.py