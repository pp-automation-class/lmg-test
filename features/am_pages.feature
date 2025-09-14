Feature: am: Swith Pages tests

  Background:
    Given am: I navigate to the dev-v2 environment login page
    When  am: I login with valid credentials
    Then  am: I should be redirected to the devices page

  Scenario: am: Show Device on Map
    Given am: I click on button "Show on map" for device "John1"
    Then  am: I should be redirected to the new Google Maps page
    When  am: I verify
    And  am : I add label "Test Label" to the device location
    Then am: I close the Google Maps page and return to the devices page
    And  am: I should be redirected to the devices page
