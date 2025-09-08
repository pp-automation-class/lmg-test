@ui @dashboard @device @smoke
Feature: "My device" section is visible on the Dashboard

  Background:
    Given I am logged in to the application
    And I am on the Dashboard page

  @presence
  Scenario: The "My device" section is visible
    Then I should see the section heading "My device"
    And I should see a device card titled "Demo device"
    And I should see the text "Updated:"
    And I should see a "Show on map" button
    And I should see a "Demo Jump" button
    And I should see battery status with a percentage value
    And I should see power status text "On" or "Off"

  @ui
  Scenario: Buttons in "My device" are rendered with correct states
    Then the "Demo Jump" button is enabled
    And the "Show on map" button is visible
    # If your product expects it disabled for demo device, assert disabled:
    # And the "Show on map" button is disabled

  @layout
  Scenario: The "My device" section appears above the News block
    Then the "My device" section is displayed before the "News" section on the page

  @nav
  Scenario: The settings icon for "My device" opens device settings
    When I click the settings icon in the "My device" section
    Then I should see device settings content
    And I can navigate back to the Dashboard
