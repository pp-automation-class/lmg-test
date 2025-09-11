Feature: am: Devices Page tests
  Log in and verify elements on the devices page
  I now have access to my devices and their details
  So I can manage and monitor them effectively

  Background:
    Given am: I navigate to the dev environment login page
    When  am: I login with valid credentials
    Then  am: I should be redirected to the devices page
    When  am: I click on the gear icon Devices Settings link
    Then  am: I should be redirected to the Devices Settings page

  @am-smoke @am-regression
  Scenario: am: Device Settings - Add New Device
    Given am: I click on button "Add new device"
    And   am: I click on dropdown "Device type" and select "Airguard other"
    When  am: I fill in device name "Test Device #1"
    And   am: I click "Add new device" button
    Then  am: I get a notification "New device has been added"
    And   am: I should see the device "Test Device #1" in the devices list

  @am-regression
  Scenario: am: Device Settings - Edit Device
    Given am: I click on button "Edit" for device "Test Device #1"
    When  am: I fill in device name "Test Device #2"
    And   am: I click "Update" button
    Then  am: I get a notification "Test Device #2 succesfully updated"
    Then  am: I should see the device "Test Device #2" in the devices list

  @am-regression
  Scenario: am: Device Settings - Delete Device
    Given am: I click on button "Delete" for device "Test Device #2"
    When  am: I click "Delete" button for confirmation
    Then  am: I get a notification "Device deleted"
