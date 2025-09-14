# Created by AnKrylo at 9/13/2025
Feature: Test of Devices Page

  Background:
    Given ank I am on the dev environment login page
    When ank I enter "akr.autotest@gmail.com" in the email field
    And ank I enter "12345" in the password field
    And ank I click the "Login " button

@ank-smoke
Scenario: Create New Device and Verify its Exists
  Then ank I verify on "My devices" page
  When ank I open devices Settings
  And ank I click "Add new device" button
  And ank I choose "Airguard other" device type
  And ank I fill out name "Test1" of device
  And ank I click "Add new device" button
  Then ank I verify device "Test1" exists in list of devices
#  And ank I wait for 3 seconds

@ank-regression
Scenario: Create second device
  Then ank I verify on "My devices" page
  When ank I open devices Settings
  And ank I click "Add new device" button
  And ank I choose "Airguard other" device type
  And ank I fill out name "Test2" of device
  And ank I click "Add new device" button
  Then ank I verify device "Test2" exists in list of devices

@ank-regression
Scenario: Create third device
  Then ank I verify on "My devices" page
  When ank I open devices Settings
  And ank I click "Add new device" button
  And ank I choose "Airguard other" device type
  And ank I fill out name "Test3" of device
  And ank I click "Add new device" button
  Then ank I verify device "Test3" exists in list of devices

@ank-regression
Scenario: Edit Device Name and Verify Changes
  Then ank I verify on "My devices" page
  When ank I open devices Settings
  And ank I click the "Edit" button for device "Test1"
  And ank I fill in device name "Test2"
  And ank I click "Update" button
  Then ank I get a notification "Test2 successfully updated"
  Then ank I verify device "Test2" exists in list of devices
#  And ank I wait for 3 seconds

@ank-regression
Scenario: Delete Device and Verify its Removal
  Then ank I click on "Delete" button for device "Test2"
  When ank I click "Delete" button for confirmation
  Then ank I get a notification "Device deleted"
