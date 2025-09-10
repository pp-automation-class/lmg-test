Feature: LinkMyGear Add New Device

  Background:
    Given kd I am on the dev environment login page
    When kd I enter "katedtest@gmail.com" in the email field
    And kd I enter "1234567890" in the password field
    Then kd I click the "Login" button

#  Scenario: Add new device
#    When I click on "//a[@class='section-title__icon']"
#    Then I verify element "//h3" contains text "Devices Settings"
#    When I click on "//span[text()='Add new device']"
#    Then I verify element "//h3[text()='Add device']" contains text "Add"
#    When I click on "//div[@class='el-select']"
#    And I click on "//li/span[text()='Airguard other']"
#    And I fill "iPhone 16 Pro" in element "//input[@class='el-input__inner']"
#    And I click on "//div[@class='modal-content']//button[.//span[text()='Add new device']]"
#    Then I verify element "//span[text()='iPhone 16 Pro']" exists

  Scenario: Add new device
    Then kd Verify I on "My devices" page
    When kd I open Devices Settings
    And kd Press Add new device button
    And kd Choose "Airguard other" device type
    And kd Fill out name "Test1" of device
    And kd Press add new device button
    And Go to "My devices" page
    Then kd Verify device "Test1" exists in list of devices

#  Scenario: Delete added device
#    When I click on "//a[@class='section-title__icon']"
#    Then I verify element "//h3" contains text "Devices Settings"
#    And I verify element "//span[text()='iPhone 16 Pro']" exists
#    When I click on "//tr[@class='el-table__row' and .//span[text()='iPhone 16 Pro']]//button[text()=' Delete ']"
#    Then I verify element "//h3[text()='Delete device']" exists
#    When I click on "//button[text()='Delete']"

  Scenario: Delete added device
    Then kd Verify I on "My devices" page
    When kd I open Devices Settings
    And kd Delete device "Test1"
    Then kd Verify device "Test1" is not in list of devices