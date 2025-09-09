# Created by ant at 9/8/2025
Feature: Device Management
  As a system administrator
  I want to manage devices in the system
  So that I can add new devices and remove obsolete ones

  Background:
    Given I am on the login page
    When I enter "anton.bondarenko.test@gmail.com" in the username field
    And I enter "123459" in the password field
    And I click the login button
    Then I should be redirected to the devices page

  Scenario: Successfully add a new device
    When I navigate to "https://dev.linkmygear.com/#/device-settings"
    And I click the "Add new device" button
    And I select "Airgaurd other" in device type dropdown
    And I fill device name field with "New test Device"
    And I click the "Add new device" button
    Then I should see "New device has been added" message
    And the device "New test Device" should appear in the devices list

  Scenario: Successfully delete an existing device
    When I navigate to "https://dev.linkmygear.com/#/device-settings"
    And the device "New test Device" should appear in the devices list
    And I click the "Delete" button in "New test Device" table row
    And I click the "Delete" button to confirm
    Then I should see "Device deleted" message
    And the device "New test Device" should be absent from the devices list
